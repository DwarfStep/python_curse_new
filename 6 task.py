from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# # 1 point
# np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
# dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
#
# dataset = np.around(dataset, 2)
# print(dataset)
# Y = dataset[:, -1]
# X = dataset[:, :-1]
#
# model = Sequential()
# model.add(Dense(12, input_dim=8, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
#
# # Обучение
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(X, Y, epochs=15, batch_size=10, verbose=2)
# print('Предсказание')
# prediction_0 = model.predict(np.array(X[:3]))
# print(prediction_0)
# print('\nПравильные ответы')
# print(Y[:3])

# 2 point


class Neiron:

    @staticmethod
    def data(file, input_d, num_sin_1, num_sin_2, result_n):

        np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
        dataset = np.genfromtxt(file, delimiter=',', dtype=float)
        dataset = np.around(dataset, 2)
        print(dataset)
        Y = dataset[:, -1]
        X = dataset[:, :-1]

        model = Sequential()
        model.add(Dense(num_sin_1, input_dim=input_d, activation='relu'))
        model.add(Dense(num_sin_2, activation='relu'))
        model.add(Dense(result_n, activation='sigmoid'))
        return X, Y, model

    @staticmethod
    def learn(los, opti, epoch, batch_s, verbos, model, X, Y):
        model.compile(loss=los, optimizer=opti, metrics=['accuracy'])
        model.fit(X, Y, epochs=epoch, batch_size=batch_s, verbose=verbos)
        return model

    @staticmethod
    def finall(num, model, X, Y):
        print('Предсказание')
        prediction = model.predict(np.array(X[:3]))
        print(prediction)
        print('\nПравильные ответы')
        print(Y[:num])


X, Y, model = Neiron.data('data.txt', 8, 12, 8, 1)
model = Neiron.learn('binary_crossentropy', 'adam', 15, 10, 2, model, X, Y)
Neiron.finall(3, model, X, Y)