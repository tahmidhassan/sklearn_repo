import pandas as pd 
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

x_data = pd.read_csv('cambau_train_x.csv')
y_data = pd.read_csv('cambau_train_y.csv')

x_data = x_data.values
y_data = y_data.values

y_data = y_data.reshape(-1)

xtrain, xtest, ytrain, ytest = train_test_split(x_data,y_data, test_size=0.1)

clf = tree.DecisionTreeClassifier()
clf.fit(xtrain,ytrain)

predictions = clf.predict(xtest)

accuracy = accuracy_score(predictions,ytest)

print(accuracy)