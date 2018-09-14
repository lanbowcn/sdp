import numpy as np
import pandas as pd
import datetime
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

def readfiles(projects):
    for project in projects:
        foldpath = "../dataset2"
        my_matrix = pd.read_csv(open(foldpath+'/'+project))
        print(my_matrix.tail(5))
    return my_matrix

# def divedeTosubsets(data,folds,seed):
#     # seed使得结果可复现，打乱现有顺序
#     np.random.seed(seed)
#     np.random.shuffle(data)
#     #数据集切分(array_split不等量分割# )
#     sub=np.array_split(data,folds)
#     return sub

if __name__ == '__main__':
    projects=['jdt.csv']
    # data = readfiles(projects)
    data = pd.read_csv('../dataset2/jdt.csv', index_col='commitdate', parse_dates=True).sort_index()
    print(data.tail(5))
    print("------------")
    print(data.sort_index)
    # for str in data['commitdate']:
        # np.Series a = datetime.datetime.strptime(data['commitdate'],"%Y/%m/%d  %H:%M:%S")

