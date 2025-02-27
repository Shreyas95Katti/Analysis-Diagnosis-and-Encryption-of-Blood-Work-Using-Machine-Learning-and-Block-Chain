import numpy as np
import pandas as pd
from numpy import loadtxt

df = loadtxt("diabetes.csv", delimiter = ",")

df

df.shape

X_train = df[0:600,0:8]
Y_train = df[0:600:,8]
X_test = df[600:768, 0:8]
Y_test = df[600:768:,8]
X_train

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(256,input_dim = 8,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Dense(64,activation="relu"))
model.add(Dense(32,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])

model.fit(X_train,Y_train,batch_size=50,epochs = 10)

model.evaluate(X_test,Y_test)

# model.save("Deeplearning.h5")

model.summary()

# from tensorflow.keras.models import load_model
# model2 = load_model("Deeplearning.h5")

import pickle
filename='diabetes.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open('diabetes.sav','rb'))

loaded_model.summary()

predict = loaded_model.predict([[5,116,74,0,0,25.6,0.201,30]])
predict
