import numpy as np
array  = np.array([[1,2,3],
                  [4,5,6],
                  [7,9,4]],dtype=int)
print(array.dtype)
print(array.ndim)
print(array.shape)
print(array.size)

# array2 = np.zeros((3,4))
# array2 = np.ones((3,4))

array2 = np.arange(9).reshape((3,3))

array3 = np.linspace(1,10,6).reshape((2,3))

array4= 10*np.sin(array2)

# print(array<3)

array5 = array*array2 #逐个相乘

#矩阵乘法
#array6 = np.dot(array,array2)
array6=array.dot(array2)

print(array)
print(array2)
print(array5)
print(array6)

print(np.sum(array,axis = 0))
#axis = 0指的是垂直操作，对行的索引进行遍历
print(np.max(array,axis = 1))
#axis = 1指的是水平操作，对列的索引进行遍历

print(np.argmin(array))#索引

#平均值
print(np.average(array))
print(np.mean(array))
#中位数
print(np.median(array))
#累加
print(array)
print(np.cumsum(array))
#累差
print(np.diff(array))

#矩阵的转置(或者用transpose())
print(array.T)

#把array中小于3的数变成3，大于8的数变成8
print(np.clip(array,3,8))

#索引
print(array)
print(array[1,2])
print(array[0:2,1:3])
#打印第0到1行，第1到2列

print(array[1][:])#打印第1行的所有元素    

for i in array:
    print(i)#打印每一行

for j in array.T:
    print(j)#打印每一列

for m in array.flat:
    print(m,end=" ")#打印每一个元素
print()
#合并元素(方法一)
arrayA = np.array([1,2,3])
arrayB = np.array([7,8,9])
arrayC = np.vstack((arrayA,arrayB))#垂直合并
arrayD = np.hstack((arrayA,arrayB))#水平合并
print(arrayC)
print(arrayD)

#增加维度
#增加纵向维度(列)
#这会将数组转换为一个多行、一列的结构（列向量）
arrayE = arrayA[:,np.newaxis]
print(arrayE)   

#增加横向维度(行)
#这会将数组转换为一个一行、多列的结构（行向量）
arrayF = arrayA[np.newaxis,:]
print(arrayF)

#合并元素(方法二)
arrayE=np.concatenate((arrayE,arrayE),axis=1)
print(arrayE)
arrayF=np.concatenate((arrayF,arrayF),axis=0)
print(arrayF)

#分割元素（平均分割）
arrayG = np.arange(1,13).reshape((3,4))
print(arrayG)
arrayH = np.split(arrayG,2,axis=1)#纵向分割成2个部分，axis=1表示按列分割,水平操作
print(arrayH)   
arrayI = np.split(arrayG,3,axis=0)#横向分割成3个部分，axis=0表示按行分割，垂直操作
print(arrayI)

#分隔元素（不平均分割）
arrayJ = np.array_split(arrayG,3,axis=1)#纵向分割成3个部分，axis=1表示按列分割,水平操作
print(arrayJ)
#分割元素（快捷分割）但是只能平均分割
print(np.vsplit(arrayG,3))#按行分割成3个部分
print(np.hsplit(arrayG,2))#按列分割成2个部分

#赋值
arrayK = arrayG
 #当前赋值，arrayK和arrayG指向同一块内存区域

arrayR = arrayG.copy()
#深拷贝，arrayR和arrayG指向不同内存区域
