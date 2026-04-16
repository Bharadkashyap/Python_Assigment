f=open("d:\\kashyap\\python\\one.txt","w");
f.write("hello world\nmy name is kashyap ")
f.close()

f=open("d:\\kashyap\\python\\one.txt","r");
if f:
    print(f.read())
    f.close()
