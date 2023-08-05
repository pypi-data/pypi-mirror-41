#  -*- coding: utf-8 -*-

import numpy as np

np.random.seed(1337)

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import SimpleRNN, Activation, Dense
from keras.optimizers import Adam

# 每个图片就是28行,一个时间段就读取一行
TIME_STEPS = 28
# 输入就是一个时间段输入28个列
INPUT_SIZE = 28
# 一次循环放入多少张图片
BATCH_SIZE = 50
#
BATCH_INDEX = 0
# 输出的标签大小是多少
OUTPUT_SIZE = 10
# RNN中间神经元的数量
CELL_SIZE = 60
# 学习率
LR = 0.001

(X_train, y_train), (X_test, y_test) = mnist.load_data()


# data process---------------------------
X_train = X_train.reshape(-1, 28, 28) / 255.  # normalize
X_test = X_test.reshape(-1, 28, 28) / 255.  # normalize


# 对标签进行one-hot 编码
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

# start to build RNN model----------------
model = Sequential()
# model.add(SimpleRNN(input_dim=INPUT_SIZE, input_length=TIME_STEPS, output_dim=CELL_SIZE,
#                     unroll=True))
model.add(SimpleRNN(input_dim=INPUT_SIZE, input_length=TIME_STEPS, output_dim=CELL_SIZE,
                    unroll=True))

# 输出层
model.add(Dense(OUTPUT_SIZE))
model.add(Activation('softmax'))

# 优化器设置
adam = Adam(LR)


# 输出模型的参数信息
model.summary()
# exit()
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# 训练
# 迭代次数
train_num = 5000

for step in range(train_num):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch = X_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :, :]
    Y_batch = y_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :]

    # 画出minist 数字
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # plt.imshow(X_batch[0],cmap = 'binary')#黑白显示
    # plt.show()
    # print(X_batch.shape)
    # exit()
    cost = model.train_on_batch(X_batch, Y_batch)
    BATCH_INDEX += BATCH_SIZE
    BATCH_INDEX = 0 if BATCH_INDEX >= X_train.shape[0] else BATCH_INDEX

    if step % 500 == 0:
        cost, accuracy = model.evaluate(X_test, y_test, batch_size=y_test.shape[0], verbose=False)
        print('test cost: ', cost, 'test accuracy: ', accuracy)