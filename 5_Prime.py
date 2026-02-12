num=51
for num in range(2, num):
    for i in range(2, num):
     if num % i == 0:
         break
     else:
         print(num)
