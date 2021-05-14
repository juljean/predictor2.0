import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
from numpy import array
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
#import seaborn as sns
from tensorflow.keras.layers import Bidirectional, Dropout, Activation, Dense, LSTM
from tensorflow.keras.models import Sequential


RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)

df = pd.read_csv("C:\\Users\\Jul\\Desktop\\python3.72\\neural\\ETHUSD.csv", parse_dates=['Date'])

scaler = MinMaxScaler()
close_price = df.Close.values.reshape(-1, 1)
scaled_close = scaler.fit_transform(close_price)

scaled_close = scaled_close[~np.isnan(scaled_close)]
scaled_close = scaled_close.reshape(-1, 1)

#print(scaled_close)
training_size=int(len(scaled_close)*0.9)
test_size=len(scaled_close)-training_size
train_data,test_data=scaled_close[0:training_size,:],scaled_close[training_size:len(scaled_close),:1]

#preprocessing
SEQ_LEN = 100
def to_sequences(data, seq_len):
    d = []
    for index in range(len(data) - seq_len):
        d.append(data[index: index + seq_len])

    return np.array(d)

def preprocess(data_raw, seq_len, train_split):
    data = to_sequences(data_raw, seq_len)
    num_train = int(train_split * data.shape[0])
    x_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]

    x_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]

    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = preprocess(scaled_close, SEQ_LEN, train_split = 0.9)

DROPOUT = 0.2
WINDOW_SIZE = SEQ_LEN - 1

# model = keras.Sequential()
#
# model.add(Bidirectional(LSTM(WINDOW_SIZE, return_sequences=True),
#                         input_shape=(WINDOW_SIZE, x_train.shape[-1])))
# model.add(Dropout(rate=DROPOUT))
#
# model.add(Bidirectional(LSTM((WINDOW_SIZE * 2), return_sequences=True)))
# model.add(Dropout(rate=DROPOUT))
#
# model.add(Bidirectional(LSTM(WINDOW_SIZE, return_sequences=False)))
#
# model.add(Dense(units=1))
#
# model.add(Activation('linear'))
#
# model.compile(
#     loss = 'mean_squared_error',
#     optimizer='adam'
# )
#
# BATCH_SIZE = 64
#
# history = model.fit(
#     x_train,
#     y_train,
#     epochs=50,
#     batch_size=64,
#     shuffle=False,
#     validation_split=0.1
# )
#
# model.save("forecast_model")

# It can be used to reconstruct the model identically.
reconstructed_model = keras.models.load_model("forecast_model")


results = reconstructed_model.evaluate(x_test, y_test, batch_size = 128)
print("test loss:", results)

y_hat = reconstructed_model.predict(x_test)

y_test_inverse = scaler.inverse_transform(y_test)
y_hat_inverse = scaler.inverse_transform(y_hat)

# plt.plot(y_test_inverse, label="Actual Price", color='green')
# plt.plot(y_hat_inverse, label="Predicted Price", color='red')
#
# plt.title('Bitcoin price prediction')
# plt.xlabel('Time [days]')
# plt.ylabel('Price')
# plt.legend(loc='best')
#
# plt.show()

print(len(test_data))
x_input = test_data[81:].reshape(1, -1)
print(x_input.shape)

temp_input=list(x_input)
temp_input=temp_input[0].tolist()
#print(temp_input)
print(len(temp_input))
lst_output = []
n_steps = 99
i = 0
while (i < 30):

    if (len(temp_input) > 99):
        # print(temp_input)
        x_input = np.array(temp_input[1:])
        print("{} day input {}".format(i, x_input))
        x_input = x_input.reshape(1, -1)
        x_input = x_input.reshape((1, n_steps, 1))
        # print(x_input)
        yhat = reconstructed_model.predict(x_input, verbose=0)
        print("{} day output {}".format(i, yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        # print(temp_input)
        lst_output.extend(yhat.tolist())
        i = i + 1
    else:
        x_input = x_input.reshape((1, n_steps, 1))
        yhat = reconstructed_model.predict(x_input, verbose=0)
        print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i = i + 1

# day_new=np.arange(1,100)
# day_pred=np.arange(100,130)
# print(len(scaled_close))
# plt.plot(day_new,scaler.inverse_transform(scaled_close[1711:]))
# plt.plot(day_pred,scaler.inverse_transform(lst_output))


df3=scaled_close.tolist()
df3.extend(lst_output)
df3=scaler.inverse_transform(df3).tolist()
plt.plot(df3)
plt.show()
