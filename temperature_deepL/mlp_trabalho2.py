# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:22:05 2023

@author: ADM
"""
from numpy import array
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

from keras.models import Sequential
from keras.layers import Dense
import pandas as pd 
from tensorflow.keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing


# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    sequence2=np.transpose(sequence)
    for i in range(len(sequence)):
		# find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence2[:,i:end_ix], sequence2[:,end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


# define input sequence
dataset_name = 'microclima'
path = f'{dataset_name}.csv'
raw_data = pd.read_csv(path, ) 
raw_data=  raw_data.value
raw_data=raw_data.array.reshape(-1, 1)
scaler = preprocessing.MinMaxScaler()
data_norm = scaler.fit_transform(raw_data)

# choose a number of time steps
n_steps = 12

# split into samples
X, y = split_sequence(data_norm, n_steps)
# summarize the data

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True)
X_train = X_train.reshape(-1, X_train.shape[-1])
X_test = X_test.reshape(-1, X_test.shape[-1])

# univariate mlp example
# hyperparameters   
epochs=2000
activation1='relu' #sigmoid, relu, tanh
activation2='tanh' #sigmoid, relu, tanh
hn1=10 # number of neurons of the first hidden layer
hn2=10 # number of neurons of the second hidden layer
lr = 0.0001
patience=20
#optimizer='RMSprop' #RMSprop,AdaGrad, SGD, adam
#optimizer='RMSprop'
#optimizer='AdaGrad'
#optimizer='SGD'
#optimizer='adam'

optimizers = ['RMSprop',
              'AdaGrad',
              'SGD',
              'adam'
             ]
for optimizer in optimizers:

    # define model
    model = Sequential()
    model.add(Dense(hn1, activation=activation1, input_dim=n_steps))
    model.add(Dense(hn2, activation=activation2))
    model.add(Dense(1))
    model.compile(optimizer=optimizer, loss='mse', metrics=['mse'])
    ces = EarlyStopping(
                        monitor='val_mse', 
                        patience=patience,
                        min_delta=0.01, 
                        mode='max'
                        )
    mc = ModelCheckpoint('best_model.h5', monitor='val_mse',  mode='max', verbose=0, save_best_only=True) #

    # fit model
    history = model.fit(X_train, y_train,
                    #batch_size= 64,
                    epochs= epochs,
                    validation_split=0.2,
                    verbose=0,
                    callbacks=[ces, mc]
                )


    def plot_metric(history, metric):
        train_metrics = history.history[metric]
        val_metrics = history.history['val_'+metric]
        epochs = range(1, len(train_metrics) + 1)
        plt.plot(epochs, train_metrics, 'b--')
        plt.plot(epochs, val_metrics, 'r-')
        plt.title('Training and validation '+ metric)
        plt.xlabel("Epochs")
        plt.ylabel(metric)
        plt.legend(["train_"+metric, 'val_'+metric])
        plt.show()
        
    plot_metric(history, 'mse') 

    # demonstrate prediction
    # x_input = array([70, 80, 90])
    # x_input = x_input.reshape((1, n_steps))

    y_pred = model.predict(X_test, verbose=0)
    plt.plot(y_test)
    plt.plot(y_pred)
    plt.legend(['Original','Predicted'])
    d = y_test - y_pred
    mse_f = np.mean(d**2)
    mae_f = np.mean(abs(d))
    rmse_f = np.sqrt(mse_f)
    r2_f = 1-(sum(d**2)/sum((y_test-np.mean(y))**2))
    print("Resultados Teste")
    print("MAE:",mae_f)
    print("MSE:", mse_f)
    print("RMSE:", rmse_f)
    print("MAPE:", mean_absolute_percentage_error(y_test, y_pred))
    print("R-Squared:", r2_f)
    print('Saída prevista:')
    print(y_pred)