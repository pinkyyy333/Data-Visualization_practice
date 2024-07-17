import pandas as pd
'''
data=pd.Series([20,10,15])
print(data)
print("Max",data.max())
print("Median",data.median())
data=data*2
print(data)
data=data==20
print(data)
'''
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
print(data)
print(data["name"])
print(data.iloc[0])