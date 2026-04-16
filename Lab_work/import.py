#immporting package of array
import array as a
#integer array
my_array=a.array('i',[1,2,3,4,5,6])
print(my_array)
#indexing & slicing
print()
print("3rd element",my_array[2])
print("last element",my_array[-1])
print("first element",my_array[0])
print("3rd to 5th  element",my_array[2:5])
print("4th to last  element",my_array[3:])
print()
#float array
my_array=a.array('f',[1.7,2.4,3.66,4.54,5.6,6.7])
print(my_array)
print()
#itration of array
for i in my_array:
    print(i)
print()
for i in my_array:
    print("%.3f"%i)
    print()
#chnging array element

my_array[2]=3.5
print(my_array)

my_array[-1]=5.5
print(my_array)
#delete element from array
del my_array[0]
print(my_array)
#character array
my_array=a.array('u',['a','t','m','i','y','a'])
print(my_array)
print()



