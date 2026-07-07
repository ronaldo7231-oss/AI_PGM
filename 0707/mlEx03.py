from sklearn.datasets import load_iris
import pandas as pd
from sklearn import svm
import plotly.express as px

iris = load_iris()
df = pd.DataFrame(iris.data)
s=svm.SVC(gamma=0.1,C=10)
s.fit(iris.data,iris.target)

new_d=[[6.4,3.2,6.0,2.5],[7.1,3.1,4.7,1.35]]

res=s.predict(new_d)
print("새로운 2개의 샘플의 부류는",res)

#print(iris.data)
#print(iris.target)
#print(iris.target_names)
#print(iris.feature_names)
#print(iris.DESCR)

df = px.data.iris()
# petal_length를 제외하여 3차원 공간 구성
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer="browser")
