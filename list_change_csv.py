'''
将pycharm中列表转化为csv文件
'''
import pandas as pd
dataSet=[[1,3,3,1,1],
[1,3,3,2,1],
[2,3,3,1,2],
[3,2,3,1,2],
[3,1,2,1,2],
[3,1,2,2,1],
[2,1,2,2,2],
[1,2,3,1,1],
[1,1,2,1,2],
[3,2,2,1,2],
[1,2,2,2,2],
[2,2,3,2,2],
[2,3,2,1,2],
[3,2,3,2,1]]

labels = ['weather', 'temp', 'humidity', 'wind','bad_good']
test2=pd.DataFrame(columns=labels,data=dataSet)
test2.to_csv('D:/PyCharmProject/DataMining/experiment/ex3/data/test2.csv')