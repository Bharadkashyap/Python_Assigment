import pandas as pd
"""student={'roll':[1,2,3,4,5],
         'name':['','b','c','','e'],
         'city':['r','g','','m','d']
         }
print(student)
df=pd.DataFrame(student)
print(df)
df.to_csv('student.csv')
df=pd.read_csv('student.csv')
ndf=df.dropna()
print(ndf)
df.dropna(subset=['name'],inplace=True)
print(df)

df.fillna("kashyap",inplace=True)
print(df)
df["name"].fillna("kashyap",inplace=True)
print(df)
n=df.isnull()
print(n)
n=df.notnull()
print(n)
df.replace(to_replace="g",value="rajkot",inplace=True)
print(df)"""

data={'name':['kashyap','hardip','hardik','hardip'],
      'age':[40,20,30,20],
      'city':['rajkot','goa','div','goa']
      }
print(data)
df=pd.DataFrame(data)
print(df)
"""print(df.duplicated())
print(df.drop_duplicates())
print(df[df['age']>30])
df.loc[3,'age']=30
print(df)
df['salary']=[50000,40000,30000,23000]
df['increment']=[1000,2000,4000,5000]
df.to_csv('data.csv')
df=pd.read_csv('data.csv')
print(df)
#renaming
df.rename(columns={'salary':'sal'},inplace=True)
df.to_csv('data.csv')
df=pd.read_csv('data.csv')
print(df)
#removing column
df.drop('data.csv',axis=1,inplace=True)
df.to_csv('data.csv')
df=pd.read_csv('data.csv')
print(df)"""
#matching & filter
df=pd.read_csv('data.csv')
print(df[df.sal==30000])
print(df[df.sal>40000])












