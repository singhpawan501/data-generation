import random as r
d=6
f=open("file12.csv",'w')
f.write("x1,x2,x3,x4,x5,x6,strenght")
f.write("\n")
def fitness(x) :
    sum=0
    for i in range(0,d-1):
        sum=sum+100*(x[i+1]-x[i]*x[i])*(x[i+1]-x[i]*x[i]) + (x[i]-1)*(x[i]-1)
    return sum
for j in range(1000) :
    
     x1=round(r.uniform(10,100),2)
     x2=round(r.uniform(-9,0),2) 
     x3=round(r.uniform(-50,-10),2)
     x4=round(r.uniform(-20,-10),2) 
     x5=round(r.uniform(0,1),2)
     x6=round(r.uniform(-5.0,-1.0),2) 
     list1=[x1,x2,x3,x4,x5,x6]
     
     f.write(str(x1))
     f.write(",")
     f.write(str(x2))
     f.write(",")
     f.write(str(x3))
     f.write(",")
     f.write(str(x4))
     f.write(",")
     f.write(str(x5))
     f.write(",")
     f.write(str(x6))
     f.write(",")
     f.write(str(fitness(list1)))
     f.write("\n")
     print(j,": answer is of ",list1,"and fitness values : ",fitness(list1))
f.close()     
print("done!!!")     