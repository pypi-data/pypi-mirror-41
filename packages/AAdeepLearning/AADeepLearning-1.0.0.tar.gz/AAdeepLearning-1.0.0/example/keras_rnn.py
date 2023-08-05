#####数据准备
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer

import re

re_tag = re.compile(r'<[^>]+>')


def rm_tags(text):
    return re_tag.sub('', text)


import os


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print('read', filetype, 'files:', len(file_list))

    all_labels = ([1] * 12500 + [0] * 12500)

    all_texts = []

    for fi in file_list:
        with open(fi, encoding='utf8') as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")
y_test, test_text = read_files("test")
token = Tokenizer(num_words=3800)
token.fit_on_texts(train_text)
x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)
x_train = sequence.pad_sequences(x_train_seq, maxlen=380)
x_test = sequence.pad_sequences(x_test_seq, maxlen=380)

#####建立模型
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import SimpleRNN

model = Sequential()

model.add(Embedding(output_dim=32,
                    input_dim=3800,
                    input_length=380))
model.add(Dropout(0.35))

model.add(SimpleRNN(units=16))

model.add(Dense(units=256, activation='relu'))

model.add(Dropout(0.35))

model.add(Dense(units=1, activation='sigmoid'))

model.summary()

#####训练模型
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

train_history = model.fit(x_train, y_train, batch_size=100,
                          epochs=10, verbose=2,
                          validation_split=0.2)

import matplotlib.pyplot as plt


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


show_train_history(train_history, 'acc', 'val_acc')
show_train_history(train_history, 'loss', 'val_loss')

#####评估模型的准确率
scores = model.evaluate(x_test, y_test, verbose=1)
scores[1]

#####预测概率
probility = model.predict(x_test)
probility[:10]

for p in probility[12500:12510]:
    print(p)

#####预测结果
predict = model.predict_classes(x_test)

predict[:10]
predict.shape
predict_classes = predict.reshape(25000)
predict_classes

#####查看预测结果
SentimentDict = {1: '正面的', 0: '负面的'}


def display_test_Sentiment(i):
    print(test_text[i])
    print('label真实值:', SentimentDict[y_test[i]],
          '预测结果:', SentimentDict[predict_classes[i]])


display_test_Sentiment(2)
'''
注：以下是程序输出（不包括此句）
As a recreational golfer with some knowledge of the sport's history, I was pleased with Disney's sensitivity to the issues of class in golf in the early twentieth century. The movie depicted well the psychological battles that Harry Vardon fought within himself, from his childhood trauma of being evicted to his own inability to break that glass ceiling that prevents him from being accepted as an equal in English golf society. Likewise, the young Ouimet goes through his own class struggles, being a mere caddie in the eyes of the upper crust Americans who scoff at his attempts to rise above his standing. What I loved best, however, is how this theme of class is manifested in the characters of Ouimet's parents. His father is a working-class drone who sees the value of hard work but is intimidated by the upper class; his mother, however, recognizes her son's talent and desire and encourages him to pursue his dream of competing against those who think he is inferior.Finally, the golf scenes are well photographed. Although the course used in the movie was not the actual site of the historical tournament, the little liberties taken by Disney do not detract from the beauty of the film. There's one little Disney moment at the pool table; otherwise, the viewer does not really think Disney. The ending, as in "Miracle," is not some Disney creation, but one that only human history could have written.
label真实值: 正面的 预测结果: 正面的
'''

display_test_Sentiment(3)
'''
注：以下是程序输出（不包括此句）
I saw this film in a sneak preview, and it is delightful. The cinematography is unusually creative, the acting is good, and the story is fabulous. If this movie does not do well, it won't be because it doesn't deserve to. Before this film, I didn't realize how charming Shia Lebouf could be. He does a marvelous, self-contained, job as the lead. There's something incredibly sweet about him, and it makes the movie even better. The other actors do a good job as well, and the film contains moments of really high suspense, more than one might expect from a movie about golf. Sports movies are a dime a dozen, but this one stands out. This is one I'd recommend to anyone.
label真实值: 正面的 预测结果: 正面的
'''
predict_classes[12500:12510]
'''
注：以下是程序输出（不包括此句）
array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
'''
display_test_Sentiment(12502)
'''
注：以下是程序输出（不包括此句）
First of all I hate those moronic rappers, who could'nt act if they had a gun pressed against their foreheads. All they do is curse and shoot each other and acting like cliché'e version of gangsters.The movie doesn't take more than five minutes to explain what is going on before we're already at the warehouse There is not a single sympathetic character in this movie, except for the homeless guy, who is also the only one with half a brain.Bill Paxton and William Sadler are both hill billies and Sadlers character is just as much a villain as the gangsters. I did'nt like him right from the start.The movie is filled with pointless violence and Walter Hills specialty: people falling through windows with glass flying everywhere. There is pretty much no plot and it is a big problem when you root for no-one. Everybody dies, except from Paxton and the homeless guy and everybody get what they deserve.The only two black people that can act is the homeless guy and the junkie but they're actors by profession, not annoying ugly brain dead rappers.Stay away from this crap and watch 48 hours 1 and 2 instead. At lest they have characters you care about, a sense of humor and nothing but real actors in the cast.
label真实值: 负面的 预测结果: 负面的
'''

# 预测新的影评
input_text = '''
I can't vote because I have not watched this movie yet. I've been wanting to watch this movie since the time they announced making it which is about 2 years ago (!)
I was planning to go with the family to see the anticipated movie but my nieces had school exams at the opening time so we all decided to wait for the next weekend. I was utterly shocked to learn yesterday that they pulled the movie from the Kuwaiti theaters "temporarily" so that the outrageous censorship system can remove some unwanted scenes.
The controversial gay "moment" according to my online research is barely there, so I can't find any logical reason for all the fuss that's been going on. And it was bad enough when fanatics and haters tried (in vain) to kill the movie with low ratings and negative reviews even before it was in the cinemas and I'm pretty sure most of those trolls never got the chance to watch the movie at that time.
Based on the trailers, I think the movie is very promising and entertaining and you can't simply overlook the tremendous efforts made to bring this beloved tale to life. To knock down hundreds of people's obvious hard work with unprofessional critique and negative reviews just for the sake of hatred is unfathomable. I hope people won't judge a movie before having the experience of watching it in the first place.
Impatiently waiting for the Kuwaiti cinemas to bring back the movie... 
'''
input_seq = token.texts_to_sequences([input_text])
pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)
predict_result = model.predict_classes(pad_input_seq)
SentimentDict[predict_result[0][0]]
'''
'负面的'
'''


def predict_review(input_text):
    input_seq = token.texts_to_sequences([input_text])
    pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)
    predict_result = model.predict_classes(pad_input_seq)
    print(SentimentDict[predict_result[0][0]])


predict_review('''
As a fan of the original Disney film (Personally I feel it's their masterpiece) I was taken aback to the fact that a new version was in the making. Still excited I had high hopes for the film. Most of was shattered in the first 10 minutes. Campy acting with badly performed singing starts off a long journey holding hands with some of the worst CGI Hollywood have managed to but to screen in ages.
A film that is over 50% GCI, should focus on making that part believable, unfortunately for this film, it's far from that. It looks like the original film was ripped apart frame by frame and the beautiful hand-painted drawings have been replaced with digital caricatures. Besides CGI that is bad, it's mostly creepy. As the little teacup boy will give me nightmares for several nights to come. Emma Watson plays the same character as she always does, with very little acting effort and very little conviction as Belle. Although I can see why she was cast in the film based on merits, she is far from the right choice for the role. Dan Stevens does alright under as some motion captured dead-eyed Beast, but his performance feels flat as well. Luke Evans makes for a great pompous Gaston, but a character that has little depth doesn't really make for a great viewing experience. Josh Gad is a great comic relief just like the original movie's LeFou. Other than that, none of the cast stands out enough for me to remember them. Human or CHI creature. I was just bored through out the whole experience. And for a project costing $160 000 000, I can see why the PR department is pushing it so hard because they really need to get some cash back on this pile of wet stinky CGI-fur!
All and all, I might be bias from really loving Disney's first adaptation. That for me marks the high-point of all their work, perfectly combining the skills of their animators along with some CGI in a majestic blend. This film however is more like the bucket you wash off your paintbrush in, it has all the same colors, but muddled with water and to thin to make a captivating story from. The film is quite frankly not worth your time, you would be better off watching the original one more time. 
''')
'''
注：以下是程序输出（不包括此句）
1/1 [==============================] - 0s
正面的
'''

predict_review('''
The original Beauty and the Beast was my favorite cartoon as a kid but it did have major plot holes. Why had no one else ever seen the castle or knew where it was? Didn't anyone miss the people who were cursed? All of that gets an explanation when the enchantress places her curse in the beginning. Why did Belle and her Father move to a small town? Her mother died and the father thought it as best to leave. I love the new songs and added lyrics to the originals. I like the way the cgi beast looks (just the face is CGi). I think Emma Watson is a perfect Belle who is outspoken, fearless, and different. The set design is perfect for the era in France.
I know a lot of people disagree but I found this remake with all its changes to be more enchanting, beautiful, and complete than the original 1991 movie. To each his own but I think everyone should see it for themselves. 
''')
'''
注：以下是程序输出（不包括此句）
1/1 [==============================] - 0s
正面的
'''
