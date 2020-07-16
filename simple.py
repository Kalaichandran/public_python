#Basic arithmetic program

a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
print("Addition of %d and %d : %d" %(a,b,a+b))
print("subtraction of %d and %d : %d" %(a,b,a-b))
print("Multiplication of %d and %d : %d" %(a,b,a*b))
print("Division of %d and %d : %d" %(a,b,a/b))
print("Modulus of %d and %d : %d" %(a,b,a%b))


#Datatypes

a=10
b=float(a)
print(a,b)

li=[56,78,929,462,322]
print(li)
print(li[3])
print(li[2:4])
print(li.sort())
li[3]=89
print(li)

d={'name':'kavya','course':'Python'}
print(d)
d['phone']='7092909192'


#Conditional Statement

name=str(input("Enter the name"))
pwd=int(input("Enter the pwd"))
name1='hitech'
pd=1234
if name==name1 and pwd==pd:
    print("Login Sucessful !!")
else:
    print("Login Failed !!")

#Looping Program

num=int(input("Enter the value"))
for i in num:
    print("i value",i)


#Function Program

def add(a,b,c):
    d=a+b+c
    print("Addition of three numbers:",d)
add(1,2,3)
add(10,20,30)
























    
            
