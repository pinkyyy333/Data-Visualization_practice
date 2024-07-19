import numpy as np
'''
#建立簡單陣列
ndarr=np.array([3,4,-5])
print(ndarr)
print(ndarr.size)

#一維陣列
data=np.array([3,2,6,4])
print(data)
data=np.empty(4)
print(data)
data=np.zeros(3)
print(data)
data=np.ones(3)
print(data)
data=np.arange(5)
print(data)

#二維陣列
data=np.array([ #3*3
    [2,3,2],
    [1,5,2],
    [4,2,1]
])
print(data)
data=np.empty([3,3])
print(data)
data=np.ones([2,3])
print(data)

#三維陣列
data=np.array([
    [
        [3,1],[1,2]
    ],
    [
        [2,5],[10,2]
    ]
])
print(data)
data=np.zeros([3,1,3])
print(data)
#多維陣列
data=np.array([
    [
        [
            [3,2,1],
            [5,5,10]
        ]
    ]
])
print(data)
data=np.ones([2,1,1,2])
print(data)

#矩陣運算
#逐元運算(elementwise)
data1=np.array([3,2,10])
data2=np.array([1,3,6])
result=data1+data2
print("加法",result)
result=data1*data2
print("乘法",result)
result=data1>data2
print("大於",result)
result=data1==data2
print("是否相等",result)

#矩陣運算(matrix)
data1=np.array([
    [1,3]
]) #1*2
data2=np.array([
    [2,-1,3],
    [-2,4,1]
]) #2*3
result=data1.dot(data2) #1*3
result1=data1@data2
print("內積",result)
print("內積1",result1)
result=np.outer(data1,data2)
print("外積",result)

#統計運算(statistics)
# ndarray 多維陣列
data=np.array([
    [2,1,7],
    [-5,3,8]
]) #2*3

result=data.sum()
print("總和",result)
result=data.max()
print("最大值",result)
result=data.mean()
print("平均數",result)
result=data.std()
print("標準差",result)
result=data.sum(axis=0) #針對欄位總和column(針對第一個相度做總和)
print(result)
result=data.sum(axis=1) #針對列位總和row(針對第二個相度做總和)
print(result)
result=data.max(axis=0)
print(result)
result=data.mean(axis=1)
print(result)
result=data.cumsum() #針對欄位總和column(針對第一個相度做逐數累加)
print(result)
'''
#多維陣列維度/形狀操作
#觀察資料形狀
'''
data=np.ones(10)
print(data)
print(data.shape)
data=np.array([
    [3,1,5],
    [1,2,3]
])
print(data.shape)
#資料轉置
data=np.array([
    [2,4,2],
    [1,5,0]
])
print(data.shape)
print(data.T)
print(data.T.shape)
'''
#扁平化資料
data=np.array([
    [
        [2,1,3],[1,2,3]
    ],
    [
        [0,2,1],[8,9,10]
    ]
])
newData=data.ravel()
print(newData)
print(newData.shape)
#重塑資料形狀
newData=data.reshape(3,4)
print(newData)
newData=data.reshape(1,2,6)
print(newData)
#初始化資料
data=np.zeros(18).reshape(3,6)
print(data)

data=np.arange(9).reshape(3,3)
print(data)
print(data.T)