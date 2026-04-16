#10-01-2024

#py for ds in hindi
#deid learning
#greate learning
import pandas as pd
Data={
    'Name':['ankit','kashyap','ram'],
    'age':[20,21,23],
    'city':['rajkot','goa','pune']}
df=pd.DataFrame(Data,columns=['age'])
print(df)
#custome index
df=pd.DataFrame(Data,index=['a','b','c'])
print(df)

#For particular Rows within a dataframe
df=pd.DataFrame(Data)
print(df.loc[0])

#Selected multiple rows

df=pd.DataFrame(Data)
print(df.loc[[0,2]])
#to extract a portion of a d.f.

a=pd.DataFrame(Data)
print(a[0:2])
#to achive a single value within a df
df=pd.DataFrame(Data)
print(df['Name'][0])
#Boolean values
df=pd.DataFrame(Data)
print(df.isin(['ankit',21]))
#condition satisfied
df=pd.DataFrame(Data)
print(df[df.isin(['ankit',21])])
#Deleting a column
df=pd.DataFrame(Data)
print(df)
del df['age']
print(df)

#nested dictionary
data={'Rno=1':{'exam1':50,'exam2':60},
    'Rno2':{'exam1':70}
    }
df=pd.DataFrame(data)
print(df)
#Transposition of df

Data={
    'Name':['ankit','kashyap','ram'],
    'age':[20,21,23],
    'city':['rajkot','goa','pune']}
df=pd.DataFrame(Data)
print(df)
print(df.T)

#!!!Reading and writing .csv file!!!

users={'Name':['a','b','c'],'age':[10,20,30]}
df=pd.DataFrame(users)
print(df)
'''
#writing a csv file
df.to_csv('users.csv',index=False)
'''
#Reading csv file
users={'Name':['a','b','c'],'age':[10,20,30]}
n_df=pd.read_csv('users.csv')
print(n_df)

#!!!Reading and writing excel file!!!
user={'Name':['a','b','c'],'age':[10,20,30]}
df=pd.DataFrame(user)
print(df)
'''
#writing a excel file
df.to_excel('user.xlsx',index=False)
'''
#Reading excel file
n_df=pd.read_excel('user.xlsx')
print(n_df)















