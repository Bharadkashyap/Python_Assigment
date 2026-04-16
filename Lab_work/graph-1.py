#31-01-2024
import matplotlib.pyplot as p
"""x=[1,2,3,4,5]
y=[10,20,30,40,50]
f1={'family':'Arial','color':'red','size':25}
f2={'family':'Arial','color':'green','size':20}

f3={'family':'Arial','color':'pink','size':30}
p.title("chart1",fontdict=f3,loc="left")
p.xlabel("x-axis",fontdict=f1)
p.ylabel("y-axis",fontdict=f2)
p.plot(x,y,marker='*',ls='-.',c="blue")
p.grid()
p.show()"""
"""
#Bar graph
x=["keyboard","mouse","screen"]
y=[1,2,3]
color=["red","blue","green"]
p.bar(x,y,color=color)
p.show()
#pie graphs
pl=[15,25,35]
my=["Delhi","pune","rajkot"]
myc=["red","green","pink"]
p.pie(pl,labels=my,colors=myc)
p.legend(title="threecities")
p.show()"""
#scatter graph
a=[1,2,3,4,5]
b=[5,4,3,2,1]
colors=["red","green","pink","blue","black"]
p.scatter(a,b,c=colors)
p.show()
