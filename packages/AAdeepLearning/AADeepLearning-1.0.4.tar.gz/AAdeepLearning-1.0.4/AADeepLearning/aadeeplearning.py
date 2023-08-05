"""Training-related part of the Keras engine.
"""
# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
#
# import warnings
# import copy
import time
import json
import pickle
import numpy as np
from .layer.fully_connected import FullyConnected
from .layer.dropout import Dropout
from .layer.batch_normalization import BatchNormalization
from .layer.rnn import RNN
from .layer.lstm import LSTM
from .layer.relu import Relu
from .layer.softmax import SoftMax
from .layer.convolutional import Convolutional
from .layer.pooling import Pooling
from .layer.flatten import Flatten
from .config import get_default_config
import matplotlib.pyplot as plt

"""
如果每一层神经元的尺寸如下：
weight_1.shape： (256, 784)
bias_1.shape： (256, 1)
weight_2.shape： (128, 256)
bias_2.shape： (128, 1)
weight_3.shape： (10, 128)
bias_3.shape： (10, 1)

那么数据前向传播和反向传播尺寸的变化情况如下

第1层，前向传播输出数据尺寸： (256, 64)  =    神经元尺寸 (256, 784) *数据尺寸(784,64)
第2层，前向传播输出数据尺寸： (128, 64)  =     神经元尺寸 (128, 256)*数据尺寸(256, 64)
第3层，前向传播输出数据尺寸： (10, 64)    =      神经元尺寸  (10, 128) *数据尺寸(128, 64)

第3层，因为是从softmax层回传过来的，尺寸不变 (10, 64)
第2层，反向传播输出数据尺寸： (128, 64)  =   下一层weight 尺寸.T (128, 10)*流动数据尺寸(10, 64)
第1层，反向传播输出数据尺寸： (256, 64)  =   下一层weight尺寸.T (256, 128)*流动数据尺寸(128, 64)
"""


class AADeepLearning:
    config = None
    # 损失值
    loss = []
    # 训练数据 shape: (60000, 28, 28, 1)  (样本数, 宽, 高, 通道数)
    train_data = []
    # 训练数据标签
    train_label = []
    # 损失值
    test_data = []
    # 损失值
    test_lable = []
    # 损失值
    input_shape = 0
    # 学习率
    learning_rate = 0
    # 神经网络层数
    layer_number = 0
    # 神经网络参数 weight和bias
    net = {}

    def __init__(self, net={}, config={}):
        # 合并配置文件，后者覆盖前者
        self.config = {**get_default_config(), **config}
        # 网络结构和定义层一致
        self.net = net
        self.learning_rate = self.config['learning_rate']
        self.net = self.init_net(net)
        self.is_load_model = False
        if self.config["load_model"] != "":
            self.reload(self.config["load_model"])
            self.is_load_model = True

    def init_net(self, net):
        for i, layer in enumerate(net):
            if layer['type'] == 'convolutional':
                net[i]['object'] = Convolutional()
            elif layer['type'] == 'pooling':
                net[i]['object'] = Pooling()
            elif layer['type'] == 'flatten':
                net[i]['object'] = Flatten()
            elif layer['type'] == 'fully_connected':
                net[i]['object'] = FullyConnected()
            elif layer['type'] == 'dropout':
                net[i]['object'] = Dropout()
            elif layer['type'] == 'batch_normalization':
                net[i]['object'] = BatchNormalization()
            elif layer['type'] == 'relu':
                net[i]['object'] = Relu()
            elif layer['type'] == 'rnn':
                net[i]['object'] = RNN()
            elif layer['type'] == 'lstm':
                net[i]['object'] = LSTM()
            elif layer['type'] == 'softmax':
                net[i]['object'] = SoftMax()
        return net

    def train(self, x_train=None, y_train=None, is_train=True):
        if len(x_train.shape) == 4:
            # 训练立方体数据 例如图片数据  宽*高*通道数
            flow_data_shape = {
                "batch_size": self.config['batch_size'],
                "channel": x_train.shape[1],
                "height": x_train.shape[2],
                "width": x_train.shape[3]
            }
        else:
            # 训练序列数据 样本 * 序列个数 * 序列长度
            flow_data_shape = {
                "batch_size": self.config['batch_size'],
                "sequence_number": x_train.shape[1],
                "sequence_length": x_train.shape[2]
            }
        # 1，初始化网络参数
        if self.is_load_model == False:
            # 没有载入已训练好的模型，则初始化
            self.net = self.init_parameters(flow_data_shape)
        loss_list = []
        for iteration in range(1, self.config['number_iteration'] + 1):
            x_train_batch, y_train_batch = self.next_batch(x_train, y_train, self.config['batch_size'])
            # 2，前向传播
            flow_data = self.forward_pass(self.net, x_train_batch, is_train=is_train)
            # if iteration % self.config["display"] == 0:
            #     print("forword flow_data|<1e-8 :", np.sum(abs(flow_data) < 1e-8), "/",
            #           flow_data.shape[0] * flow_data.shape[1])
            #     print(flow_data)
            # 3，计算损失
            loss = self.compute_cost(flow_data, y_train_batch)
            loss_list.append(loss)
            # 4，反向传播，求梯度
            self.net = self.backward_pass(self.net, flow_data, y_train_batch)
            # if iteration == 100:
            # self.gradient_check(x=x_train_batch, y=y_train_batch, net=self.net, layer_name='rnn_1', weight_key='W', gradient_key='dW')
            # exit()
            # 5，根据梯度更新一次参数
            self.net = self.update_parameters(self.net, iteration)
            if iteration % self.config["display"] == 0:
                # self.check_weight(self.net)
                _, accuracy = self.predict(x_train_batch, y_train_batch, is_train=is_train)
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print(now_time, '   iteration:', iteration, '   loss:', loss, ' accuracy:', accuracy)
            if self.config["save_model"] != "" and iteration % self.config["save_iteration"] == 0:
                print('saving model...')
                self.save(self.config["save_model"] + "-" + str(iteration) + '.model')
        # self.net = net
        # plt.plot(loss_list, 'r')
        # plt.xlabel("iteration")
        # plt.ylabel("loss")
        # plt.show()

    def init_parameters(self, flow_data_shape):
        net = self.net
        # flow_data_shape = {}
        for i, layer in enumerate(net):
            print(layer["name"])
            net[i], flow_data_shape = layer['object'].init(layer=layer, flow_data_shape=flow_data_shape,
                                                           config=self.config)
        return net

    def forward_pass(self, net, x, is_train=False):
        # X_train shape: (60000, 28, 28, 1) ——> (784, 60000)
        # 流动数据，一层一层的计算，并先后流动
        # flow_data = data.reshape(data.shape[0], -1).T
        flow_data = x
        for i, layer in enumerate(net):
            # 缓存当前层的输入
            net[i]['input'] = flow_data
            flow_data, net[i] = layer["object"].forword(flow_data=flow_data, layer=layer, is_train=is_train)
            # 缓存当前层的输出
            net[i]['output'] = flow_data
        return flow_data

    def compute_cost(self, layer_output, batch_label):
        batch_size = self.config['batch_size']
        loss = 0.0
        for i in range(batch_size):
            loss += -np.sum(np.dot(batch_label[i], np.log(layer_output[:, i])))
        loss = loss / batch_size
        return loss

    def backward_pass(self, net, flow_data, train_label):
        layer_number = len(net)
        for i in reversed(range(0, layer_number)):
            layer = net[i]
            if layer['type'] == 'softmax':
                flow_data = layer["object"].backword(flow_data=flow_data, label=train_label)
            else:
                flow_data, net[i] = layer["object"].backword(flow_data=flow_data, layer=layer, config=self.config)
        return net

    def update_parameters(self, net, iteration):
        for i, layer in enumerate(net):
            net[i] = layer['object'].update_parameters(layer=layer, config=self.config, iteration=iteration)
        return net

    def save(self, path="AA.model"):
        with open(path, "wb") as f:
            pickle.dump(self.net, f)

    def reload(self, path="AA.model"):
        with open(path, "rb") as f:
            self.net = pickle.load(f)

    def predict(self, x_test=None, y_test=None, is_train=False):
        if x_test.shape[0] > 500:
            print("Verify the accuracy on " + str(x_test.shape[0]) + " test set, please wait a moment.")
        flow_data = self.forward_pass(self.net, x_test, is_train)
        flow_data = np.array(flow_data).T
        batch_size = y_test.shape[0]
        right = 0
        for i in range(0, batch_size):
            index = np.argmax(flow_data[i])
            if y_test[i][index] == 1:
                right += 1
        accuracy = right / batch_size
        return flow_data, accuracy

    def next_batch(self, train_data, train_label, batch_size):
        index = [i for i in range(0, len(train_label))]
        # 洗牌后卷积核个数居然会改变固定位置的图片？
        np.random.shuffle(index)
        batch_data = []
        batch_label = []
        for i in range(0, batch_size):
            batch_data.append(train_data[index[i]])
            batch_label.append(train_label[index[i]])
        batch_data = np.array(batch_data)
        batch_label = np.array(batch_label)
        return batch_data, batch_label

    def check_weight(self, net):
        for i, layer in enumerate(net):
            if layer['type'] == 'fully_connected':
                print(layer["name"], ":dW|<1e-8 :", np.sum(abs(layer['dW']) < 1e-8), "/",
                      layer['dW'].shape[0] * layer['dW'].shape[1])
                print(layer['name'] + ":db|<1e-8 :", np.sum(abs(layer['db']) < 1e-8), "/",
                      layer['db'].shape[0] * layer['db'].shape[1])
            elif layer['type'] == 'convolutional':
                print(layer["name"], ":dW|<1e-8 :", np.sum(abs(layer['dW']) < 1e-8), "/",
                      layer['dW'].shape[0] * layer['dW'].shape[1] * layer['dW'].shape[2] * layer['dW'].shape[3])
                print(layer['name'] + ":db|<1e-8 :", np.sum(abs(layer['db']) < 1e-8), "/",
                      layer['db'].shape[0] * layer['db'].shape[1] * layer['db'].shape[2])
            elif layer['type'] == 'rnn':
                print(layer['name'] + ":weight_U_gradient" + str(i) + "|<1e-8 :",
                      np.sum(abs(layer['weight_U_gradient']) < 1e-8), "/",
                      layer['weight_U_gradient'].shape[0] * layer['weight_U_gradient'].shape[1])
                print(layer['name'] + ":weight_W_gradient" + str(i) + "|<1e-8 :",
                      np.sum(abs(layer['weight_W_gradient']) < 1e-8), "/",
                      layer['weight_W_gradient'].shape[0] * layer['weight_W_gradient'].shape[1])
                print(layer['name'] + ":weight_V_gradient" + str(i) + "|<1e-8 :",
                      np.sum(abs(layer['weight_V_gradient']) < 1e-8), "/",
                      layer['weight_V_gradient'].shape[0] * layer['weight_V_gradient'].shape[1])
            elif layer['type'] == 'lstm':
                print(layer['name'] + ":dWf" + str(i) + "|<1e-8 :", np.sum(abs(layer['dWf']) < 1e-8), "/",
                      layer['dWf'].shape[0] * layer['dWf'].shape[1])
                print(layer['name'] + ":dUf" + str(i) + "|<1e-8 :", np.sum(abs(layer['dUf']) < 1e-8), "/",
                      layer['dUf'].shape[0] * layer['dUf'].shape[1])
                print(layer['name'] + ":dbf" + str(i) + "|<1e-8 :", np.sum(abs(layer['dbf']) < 1e-8), "/",
                      layer['dbf'].shape[0] * layer['dbf'].shape[1])

                print(layer['name'] + ":dWi" + str(i) + "|<1e-8 :", np.sum(abs(layer['dWi']) < 1e-8), "/",
                      layer['dWi'].shape[0] * layer['dWi'].shape[1])
                print(layer['name'] + ":dUf" + str(i) + "|<1e-8 :", np.sum(abs(layer['dUf']) < 1e-8), "/",
                      layer['dUi'].shape[0] * layer['dUi'].shape[1])
                print(layer['name'] + ":dbf" + str(i) + "|<1e-8 :", np.sum(abs(layer['dbf']) < 1e-8), "/",
                      layer['dbi'].shape[0] * layer['dbi'].shape[1])

    def gradient_check(self, x, y, net, layer_name, weight_key, gradient_key, epsilon=1e-4):
        # 1,要检验的梯度展成一列
        layer_number = -1  # 第几层
        for j, layer in enumerate(net):
            if layer['name'] == layer_name:
                layer_number = j
                break
        assert layer_number != -1
        # 梯度字典转列向量(n,1)
        gradient_vector = np.reshape(net[layer_number][gradient_key], (-1, 1))
        # 参数字典转列向量(n,1)
        weight_vector = np.reshape(net[layer_number][weight_key], (-1, 1))

        # 数值逼近求得的梯度
        gradient_vector_approach = np.zeros(gradient_vector.shape)
        len = weight_vector.shape[0]
        # 遍历
        for i in range(len):
            if i % 10 == 0:
                print("gradient checking i/len=", i, "/", len)
            weight_vector_plus = np.copy(weight_vector)
            weight_vector_plus[i][0] = weight_vector_plus[i][0] + epsilon
            net[layer_number][weight_key] = np.reshape(weight_vector_plus, net[layer_number][weight_key].shape)
            # 2，前向传播
            flow_data = self.forward_pass(net=net, x=x)
            # 3，计算损失
            J_plus_epsilon = self.compute_cost(flow_data, y)

            weight_vector_minus = np.copy(weight_vector)
            weight_vector_minus[i][0] = weight_vector_minus[i][0] - epsilon
            net[layer_number][weight_key] = np.reshape(weight_vector_minus, net[layer_number][weight_key].shape)
            # 2，前向传播
            flow_data = self.forward_pass(net=net, x=x)
            # 3，计算损失
            J_minus_epsilon = self.compute_cost(flow_data, y)

            # 数值逼近求得梯度
            gradient_vector_approach[i][0] = (J_plus_epsilon - J_minus_epsilon) / (epsilon * 2)

        # 和解析解求得的梯度做欧式距离
        diff = np.sqrt(np.sum((gradient_vector - gradient_vector_approach) ** 2)) / (
                    np.sqrt(np.sum((gradient_vector) ** 2)) + np.sqrt(np.sum((gradient_vector_approach) ** 2)))
        if diff > 1e-4:
            print("Maybe a mistake in your bakeward pass!!!  diff=", diff)
        else:
            print("No problem in your bakeward pass!!!  diff=", diff)
