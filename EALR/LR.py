from sklearn import linear_model
from sklearn import datasets
clf=linear_model.LinearRegression()
x=[[0,0],[1,1],[2,2]]
y=[0,1,2]
clf.fit(x,y)
print(clf.coef_)
print(clf.intercept_)
print(clf(6,6))
iris = datasets.load_iris()
x=iris.data
y=iris.target
print(type(x))

