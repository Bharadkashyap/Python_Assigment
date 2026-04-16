#06-03-2024
#file write&read


"""
f1=open("d:\\kashyap\\python\\2.txt","a");
f1.write("3hello guys!!\n How are you\n My name is kashyap")

f1=open("d:\\kashyap\\python\\2.txt","r");
if f1:
    print(f1.read())
    f1.seek(0)
    print(f1.read(5))
    f1.seek(0)
    print(f1.readline())
    print(f1.readline())
    print(f1.readline())
    print(f1.tell())
    f1.close()"""
import os
os.rename("two.txt","2.txt")
#os.remove("two.txt")
