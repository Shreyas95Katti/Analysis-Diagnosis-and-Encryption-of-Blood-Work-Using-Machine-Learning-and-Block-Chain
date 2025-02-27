import glob
from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import keras as k

#Load the data
df = pd.read_csv("kidney_disease.csv")
df.head()

df.shape

col_of_study = ['sg', 'al', 'sc', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'classification']
df = df.drop([col for col in df.columns if not col in col_of_study], axis = 1)

df = df.dropna(axis = 0)

#Encoding
for column in df.columns:
    if df[column].dtype == np.number:
        continue
    df[column] = LabelEncoder().fit_transform(df[column])

df.head()

#Splitting dataset into FeatureMatrix and TargetMatrix
X = df.drop(['classification'], axis = 1)
y = df['classification']

#Feature scaling, scales all input feature to lie between 0 and 1
X_scaler = MinMaxScaler()
X_scaler.fit(X)
column_names = X.columns
X[column_names] = X_scaler.transform(X)

#Splitting data into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = True)

#Build the model
model = Sequential()
model.add(Dense(256, input_dim = len(X.columns), kernel_initializer = k.initializers.random_normal(seed = 13), activation = 'relu'))
model.add(Dense(1, activation = 'hard_sigmoid'))

#Compile the model
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

#Train the model
history = model.fit(X_train, y_train, epochs = 2000, batch_size = X_train.shape[0])

#Save the model
model.save('ckd.model')

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('Model Accuracy and Loss')
plt.ylabel('Accuracy and Loss')
plt.xlabel('Epoch')

pred = model.predict(X_test)
pred = [1 if y>=0.5 else 0 for y in pred]
accuracy_score(pred, y_test)

sg = float(input("Please enter the specific gravity of patient: "))
al = float(input("Please enter the albumin level of the patient: "))
sc = float(input("Please enter the Serum-Creatinine level of the patient: "))
hemo = float(input("Please enter the haemoglobin level of the patient: "))
pcv = int(input("Please enter the packed cell volume of the patient: "))
wc = int(input("Please enter the white blood cell count of the patient: "))
rc = float(input("Please enter the red blood cell count of the patient: "))
htn = int(input("Does the patient suffer from hyper tension - 1 if yes, 0 if no"))

X_patient = np.array([[sg, al, sc, hemo, pcv, wc, rc, htn]])
X_scaler.fit(X_patient)
pred = model.predict(X_patient)

if pred == 1:
    print("Congratulations you are safe from Chronic Kidney Disease!!")
else:
    print("I am sorry to inform you, you suffer from chronic Kidney Disease. Please contact your family doctor immediately and acquire some medications. Get well soon!")

