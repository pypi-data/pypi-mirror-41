#!/usr/bin/python
from __future__ import print_function

from keras.layers import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
from keras.utils.vis_utils import plot_model
import numpy as np


# using simpleRNN to generate next letter
class RNNSimple:
    def __init__(self, hidden_size=128, batch_size=128,
                 num_iter=24, num_epoch=1, num_pred=100, seq_len=10, step=1):
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.num_iter = num_iter
        self.num_epoch = num_epoch
        self.num_pred = num_pred
        self.seq_len = seq_len
        self.step = step

    def read_text(self, file_path):
        lines = []
        with open(file_path, 'rb') as f:
            for line in f:
                line = line.strip().lower()
                line = line.decode('ascii', 'ignore')
                if len(line) == 0:
                    continue
                lines.append(line)
        text = ' '.join(lines)
        return text

    def vectorize(self, text):
        # generate index
        chars = set([c for c in text])
        self.chars_count = len(chars)
        self.char2index = dict((c, i) for i, c in enumerate(chars))
        self.index2char = dict((i, c) for i, c in enumerate(chars))
        print(self.char2index)
        print(self.index2char)
        # generate input and label
        self.input_chars = []
        self.label_chars = []
        for i in range(0, len(text) - self.seq_len, self.step):
            self.input_chars.append(text[i: i + self.seq_len])
            self.label_chars.append(text[i + self.seq_len])
        print(self.input_chars)
        print(self.label_chars)
        # one-hot to vectorize input and label
        X = np.zeros((len(self.input_chars), self.seq_len, self.chars_count), dtype=np.bool)
        Y = np.zeros((len(self.input_chars), self.chars_count), dtype=np.bool)
        for i, input_char in enumerate(self.input_chars):
            for j, c in enumerate(input_char):
                X[i, j, self.char2index[c]] = 1
            Y[i, self.char2index[self.label_chars[i]]] = 1

        print(X.shape)
        print(Y.shape)
        return X, Y

    def train(self, X, Y):
        # build model
        model = Sequential()
        model.add(SimpleRNN(self.hidden_size, return_sequences=False,
                            input_shape=(self.seq_len, self.chars_count), unroll=True))
        model.add(Dense(self.chars_count))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
        # training and predict
        for iteration in range(self.num_iter):
            print('Iteration: %d' % iteration)
            # print(X.shape)
            # exit()
            model.fit(X, Y, batch_size=self.batch_size, epochs=self.num_epoch)
        return model

    def predict(self, model, test_chars):
        result = test_chars
        epoch_chars = test_chars
        for i in range(self.num_pred):
            vect_test = np.zeros((1, self.seq_len, self.chars_count))
            # label char index of vector as 1 which appear in test chars
            for i, ch in enumerate(epoch_chars):
                vect_test[0, i, self.char2index[ch]] = 1
            pred = model.predict(vect_test, verbose=0)[0]
            pred_char = self.index2char[np.argmax(pred)]
            result += pred_char
            epoch_chars = epoch_chars[1:] + pred_char
        return result

    def process(self):
        # 1. read text from file
        text = self.read_text('./test.txt')
        print(len(text))
        # 2. vectorize text
        X, Y = self.vectorize(text)
        # 3. train based on X, Y
        model = self.train(X, Y)
        # 4. try predict
        test_idx = np.random.randint(len(self.input_chars))

        test_chars = self.input_chars[test_idx]
        # test_chars = 'e f g'

        print('test seed is: %s' % test_chars)
        result = self.predict(model, test_chars)
        print('result is: %s' % result)

if __name__ == '__main__':
    rnn_simple = RNNSimple(num_pred=50)
    rnn_simple.process()