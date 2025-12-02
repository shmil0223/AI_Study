import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# s = pd.Series([1,2,6,np.nan,44,5])
# print(s)

# dates = pd.date_range('20230101',periods=6)
# print(dates)

# #相当于二维numpy,index行标签，columns列标签
# df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# print(df)

# print(pd.DataFrame(np.arange(12).reshape((3,4))))

# #可以使用字典创建
# df2 = pd.DataFrame({'A':1.,
#                     'B':pd.Timestamp('20230102'),
#                     'C':pd.Series(1,index=list(range(4)),dtype='float32'),
#                     'D':np.array([3]*4,dtype='int32'),
#                     'E':pd.Categorical(['test','train','test','train']),
#                     'F':'foo'})
# print(df2)
# print(df2.dtypes)
# print(df2.index)
# print(df2.columns)
# print(df2.values)
# print(df2.describe())#快速统计汇总
# print(df2.T)#转置
# #按列标签排序
# print(df2.sort_index(axis=1,ascending=False))

# print(df2.A)

# print(df[0:3])#按行索引切片
# print(df['2023-01-02':'2023-01-04'])#按日期切片

# print(df.loc[dates[0]])#按行标签取值
# print(df.loc[:,['A','B']])#按列标签取值
# print(df.loc['2023-01-02':'2023-01-04',['A','B']])#按行列标签取值

# print(df.iloc[3])#按行索引取值
# print(df.iloc[3:5,0:2])#按行列索引取

# print(df[df.A>0.5])#按条件取值

# df.iloc[2,2] = 1111
# df.loc[dates[0],'B'] = 2222
# df.A[df.A>0.5] = 0


# df['E'] = ['one','one','two','three','four','three']
 
# print(df.dropna(how='any'))#删除含有NA的行
# print(df.dropna(how='all'))#删除全部是NA的行

# print(df.fillna(value=0))#用指定值填充NA

# print(pd.isna(df))#判断是否为NA
# print(np.any(df.isna() == True))


#数据合并
df1 = pd.DataFrame(np.random.randn(3,4),columns=list('ABCD'))
df2 = pd.DataFrame(np.random.randn(3,4),columns=list('BCDE'))
# print(pd.concat([df1,df2],axis=0, ignore_index=True))#按行合并,垂直操作
# print(pd.concat([df1,df2],axis=1))#按列合并,水平操作

# join操作,处理不同列名的情况
# inner 交集
res = pd.concat([df1,df2],axis=0,join='inner',ignore_index=True)
# outer 并集
res = pd.concat([df1,df2],axis=0,join='outer',ignore_index=True)

# 以df1的行为基准进行合并
res = pd.concat([df1,df2],axis=1).reindex(df1.index)

# append 操作在 Pandas 2.x 中已移除，使用 concat 等价替代
res = pd.concat([df1, df2], axis=0, ignore_index=True)


#merge操作,类似数据库的join操作
left = pd.DataFrame({'key1':['K0','K1','K1','K4'],
                     'key2':['K0','K1','K0','K1'],  
                     'A':['A0','A1','A2','A3'], 
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['K0','K1','K2','K4'],
                      'key2':['K0','K0','K0','K1'],  
                      'C':['C0','C1','C2','C4'],
                      'D':['D0','D1','D2','D4']})

res = pd.merge(left,right,on=['key1', 'key2'],how = 'outer',indicator=True)

#merge by index
res = pd.merge(left,right,left_index=True,right_index=True,suffixes=('_left', '_right'),how = 'inner')

#plot 

# Series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

# #DataFrame
# data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
# data = data.cumsum()
# ax = data.plot.scatter(x='A', y='B',color='DarkBlue', label='Class 1')
# data.plot.scatter(x='A', y='C',color='DarkGreen', label='Class 2',ax=ax)#放到一张图上
# plt.show()