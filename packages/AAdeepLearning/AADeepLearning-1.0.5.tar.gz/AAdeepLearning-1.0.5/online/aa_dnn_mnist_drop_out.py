from __future__ import print_function
import numpy as np

np.random.seed(1337)
# 生产环境
# from aa_deep_learning.aadeeplearning.aadeeplearning_old import AADeepLearning
from aa_deep_learning.AADeepLearning import AADeepLearning
from aa_deep_learning.AADeepLearning.datasets import mnist
from aa_deep_learning.AADeepLearning.datasets import np_utils

# 测试环境
# from aadeeplearning import aadeeplearning as aa

# 输入图像的维度，此处是mnist图像，因此是28*28
img_rows, img_cols = 28, 28
# 10分类
nb_classes = 10

# keras中的mnist数据集已经被划分成了60,000个训练集，10,000个测试集的形式，按以下格式调用即可
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# X_test = X_test[:100]
# y_test = y_test[:100]

# print(X_test[0])

# 画出minist 数字
# import matplotlib.pyplot as plt
# fig = plt.figure()
# plt.imshow(X_test[0],cmap = 'binary')#黑白显示
# plt.show()

# 后端使用tensorflow时，即tf模式下，
# 会将100张RGB三通道的16*32彩色图表示为(100,16,32,3)，
# 第一个维度是样本维，表示样本的数目，
# 第二和第三个维度是高和宽，
# 最后一个维度是通道维，表示颜色通道数
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

# 将X_train, X_test的数据格式转为float32
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# 归一化
X_train /= 255
X_test /= 255
# 打印出相关信息
print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
# X_train shape: (60000, 28, 28, 1)
# 60000 train samples
# 10000 test samples

# 将类别向量(从0到nb_classes的整数向量)映射为二值类别矩阵，
# 相当于将向量用one-hot重新编码
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)
# print(Y_test.shape)
# 网络配置文件
config = {
    # 训练多少次
    "number_iteration": 2000,
    "display": 100,
}

net = [
    {
        # 层名
        "name": "flatten_1",
        # 层类型
        "type": "flatten"
    },
    {
        # 层名
        "name": "fully_connected_1",
        # 层类型
        "type": "fully_connected",
        # 神经元个数
        "neurons_number": 128,
        # 权重初始化方式  msra/gaussian
        "weight_init": "msra"
    },
    {
        # 层名
        "name": "relu_1",
        # 层类型 可选，relu，sigmoid，tanh，
        "type": "relu",
        # relu函数的上界限制值；   注： 不做设置或者设置为0意味着是普通的relu函数
        "threshold": 0
    },
    {
        # 层名
        "name": "dropout_1",
        # 层类型
        "type": "dropout",
        # dropout比例（置零比例）
        "drop_rate": 0.5
    },
    # {
    #     # 层名
    #     "name": "fully_connected_2",
    #     # 层类型
    #     "type": "fully_connected",
    #     # 神经元个数
    #     "neurons_number": 32,
    #     # 权重初始化方式  msra/gaussian
    #     "weight_init": "msra"
    # },
    # {
    #     # 层名
    #     "name": "relu_2",
    #     # 层类型
    #     "type": "relu",
    #     # relu函数的上界限制值；   注： 不做设置或者设置为0意味着是普通的relu函数
    #     "threshold": 0
    # },
    # {
    #     # 层名
    #     "name": "dropout_2",
    #     # 层类型
    #     "type": "dropout",
    #     # dropout比例（置零比例）
    #     "drop_rate": 0.5
    # },
    # {
    #     # 层名
    #     "name": "fully_connected_3",
    #     # 层类型
    #     "type": "fully_connected",
    #     # 神经元个数
    #     "neurons_number": 32,
    #     # 权重初始化方式  msra/gaussian
    #     "weight_init": "msra"
    # },
    # {
    #     # 层名
    #     "name": "relu_3",
    #     # 层类型
    #     "type": "relu",
    #     # relu函数的上界限制值；   注： 不做设置或者设置为0意味着是普通的relu函数
    #     "threshold": 0
    # },
    # {
    #     # 层名
    #     "name": "dropout_3",
    #     # 层类型
    #     "type": "dropout",
    #     # dropout比例（置零比例）
    #     "drop_rate": 0.5
    # },
    {
        # 层名
        "name": "fully_connected_3",
        # 层类型
        "type": "fully_connected",
        # 神经元个数
        "neurons_number": 10,
        # 权重初始化方式  msra/gaussian
        "weight_init": "msra"
    },
    {
        # 层名
        "name": "softmax",
        # 层类型
        "type": "softmax"
    }
]


AA = AADeepLearning(net=net, config=config)
# 训练模型
AA.train(X_train, Y_train)

# 按batch计算在某些输入数据上模型的误差
score, accuracy = AA.predict(X_test, Y_test)
print(accuracy)

"""
# 输出训练好的模型在测试集上的表现
print('Test score:', score[0])
print('Test accuracy:', score[1])

# Test score: 0.032927570413
# Test accuracy: 0.9892
"""
