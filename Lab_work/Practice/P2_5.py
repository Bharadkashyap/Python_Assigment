with open("file1.txt","r") as f:
          d=f.read()
          print(d)
          w=d.split()
          print(len(d))
with open("file2.txt","w") as o:
            o.write(d)
print("Success")
