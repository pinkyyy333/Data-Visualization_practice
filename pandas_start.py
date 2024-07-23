import pandas as pd

#----------基礎表格建立-----------
data=pd.Series([20,10,15])
print(data)
print("Max",data.max())
print("Median",data.median())
data=data*2
print(data)
data=data==20
print(data)

data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
print(data)
print(data["name"])
print(data.iloc[0])

#----------Series單維度資料-----------

data1=pd.Series([5,4,-2,3,7])
#print(data)
data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
print(data)
#觀察資料
print("資料型態",data.dtype)
print("資料數量",data.size)
print("資料索引",data.index)
#取得資料:根據順序、根據索引
#print(data[2],data[0])
print(data.iloc[2],data.iloc[0])
print(data["e"],data["d"])

#數字運算:基本、統計、順序
print("最大值", data.max())
print("總和",data.sum())
print("標準差",data.std())
print("中位數",data.median())
print("最大的三個數",data.nlargest(3))
print("最小的兩個數",data.nsmallest(2))

#字串運算:基本、串接、搜尋、取代
data=pd.Series(["您好","Python","Pandas"])
print(data.str.lower()) #小寫
print(data.str.len()) #算出每個字串長度
print(data.str.cat(sep="-")) #把字串串起來，可以自訂串接的符號
print(data.str.contains("P")) #判斷每個字串是否包含特定字元
print(data.str.replace("您好","Hello"))

#----------DataFrame雙維度資料-----------

data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
}, index=["a","b","c"])
print(data)
#觀察資料

print("資料數量",data.size)
print("資料形狀(列,欄)",data.shape)
print("資料索引",data.index)

#取得列(row/橫向)的series資料，根據順序、根據索引
print("取得第二列",data.iloc[1],sep="\n")
print("取得第C列",data.loc["c"],sep="\n")

#取得欄(column/直向)的series資料，根據欄位的名稱
print("取得name欄位",data["name"],sep="\n")
names=data["name"] #取得單維度的Series資料
print("把name全部轉大寫",names.str.upper(),sep="\n")
#計算薪水平均值
salaries=data["salary"]
print("薪水的平均值",salaries.mean())

#建立新欄位
data["revenue"]=[500000,400000,300000]
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)

#----------篩選資料-----------

#篩選練習 Serial
data=pd.Series([30,15,20])
condition=[True,False,True]
filteredData=data[condition]
print(filteredData)
condition=data>18
print(condition)
filteredData=data[condition]
print(filteredData)

data=pd.Series(["您好","Python","Pandas"])
condition=[True,False,True]
filteredData=data[condition]
print(filteredData)
condition=data.str.contains("P")
print(condition)
filteredData=data[condition]
print(filteredData)

#篩選練習 DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
}, index=["a","b","c"])
print(data)
condition=[False,True,True]
filteredData=data[condition]
print(filteredData)
condition=data["salary"]>=40000
print(condition)
filteredData=data[condition]
print(filteredData)
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)