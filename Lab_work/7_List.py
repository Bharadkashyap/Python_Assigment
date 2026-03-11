list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5,6,7]
list3=list1+list2
print("I Concatenation:",list3)#Concatenation
list2.remove(3)
print("II Remove:",list2)#Remove
list1.append("Java")
print("III Add java:",list1)#Add Java
list2[3]=11
print("IV Update 3 position to 11:",list2)#Update TO 11
del list2[2]
print("V Del:",list2)#Remove

print("Welcome to Marwadi university\n"*4)# VI Printing 4 times

print("VII Slicing",list1[-2],"\n",list1[1:3],"\n",list1[-1:-3])#Slicing
print("VIII Length of list 2",len(list2))#Length
print("IX Maximum",max(list2))#maximum from list 2
print("X Minimum",min(list2))#Minimum from list 2
list2.append(100)
print("XI Append",list2)#Appending list 2

list1.extend(list2)

print("XII Extends:",list1)#Extending list1








