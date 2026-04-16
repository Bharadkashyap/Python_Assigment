#name:Bharad kashyap R.
#Rollno:14

Teacher=[101,"kashyap",50000,9988776655,"B.C.A.",["b1","b2","b3","b4"],["ds","RDBMS"]]

print(Teacher)
#a
print(Teacher[:2])
#b
print(len(Teacher[6]))
#c
print(Teacher[6][0])
#d
print(Teacher[6])
#e
print(Teacher[4])

#F
Teacher.append("06-07-2005")
print(Teacher)
#g
Teacher[3]=11223344
print(Teacher)
#h
Teacher.remove(50000)
print(Teacher)
#i
Teacher.clear()
print(Teacher)
#j
del Teacher
print(Teacher)
