#Numpy
#Write a python program to perform the following:
#Create a numpy 1D array named my_array that has the following elements and
#print it:
import numpy as np
my_array=np.array([10,-20,56,67,78,-89,34,-45,56])
print(my_array)
#Print the dimensions of my_array
print("dimensions is =",my_array.ndim)

#Search the elements less than 0 in an array and print it
new_array=np.where(my_array<0)
print(" the elements less than 0 is =",new_array)



#Print the my_array in a sorted manner.
new_array=np.sort(my_array)
print("sorted manner=",new_array)

# Convert my_array into a 2D (3X3) array named new_array.
n_array=np.array([[10,-20,56],[67,78,-89],[34,-45,56]])
print(n_array)
# Print the dimensions of the new_array.
print(n_array.ndim)
# How many rows and columns new_array have?
print(n_array.shape)




#Pandas
# Write a python program to perform the following:
import pandas as pd
#Create a dataframe that contain the following information of 3 employee:
#(id,name,salary,department,designation)
data={ "ID":[101,201,301],
        "name":["kashyap","parth","meet"],
        "salary":[50000,4500,60000],
        "department":["B.C.A.","B.B.A.","B.com"],
        "designation":["professor","researsch","principal"]
       }
df=pd.DataFrame(data)
print(data)
print(df)
print(type(df))


# Read that CSV file and print the data.

a = pd.read_csv('assigment3.csv')
print(a)

# w.a.p to read data.xlsx files and print the first 10 records 
a = pd.read_excel('data.xlsx')
print(a)
print(a.head(10))

