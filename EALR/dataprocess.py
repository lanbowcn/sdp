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

#Series转list后去重
def quchong(list):
    ym=[]
    for i in list:
        if i not in ym:
            ym.append(i)
    return(ym)

# def divedeTosubsets(data,folds,seed):
#     # seed使得结果可复现，打乱现有顺序
#     np.random.seed(seed)
#     np.random.shuffle(data)
#     #数据集切分(array_split不等量分割# )
#     sub=np.array_split(data,folds)
#     return sub

if __name__ == '__main__':
    # projects=['jdt.csv']
    # # data = readfiles(projects)
    # data = pd.read_csv('../dataset2/jdt.csv', index_col='commitdate', parse_dates=True).sort_index()
    # print(data.tail(5))
    # print("------------")
    # print(data.sort_index)

    df = pd.read_csv('../dataset2/jdt.csv', sep=",")
    df['commitdate'] = pd.to_datetime(df['commitdate'], format='%Y/%m/%d %H:%M:%S')
    df.set_index('commitdate',inplace=True)
    df = df.sort_index()#按时间进行排序
    # print(df['2001-09'])需要获取年月字符串组


    print(type(df.index))
    #获取所有的年月信息
    pydate_array = df.index.to_pydatetime()
    date_only_array = np.vectorize(lambda s: s.strftime('%Y-%m'))(pydate_array)
    date_only_series = pd.Series(date_only_array)

    ym = quchong(date_only_series)

    sub=[]
    for i in range(len(ym)):
        sub.append(df[ym[i]])

    fit = sub[0].append(sub[1])
    est = sub[4].append(sub[5])








