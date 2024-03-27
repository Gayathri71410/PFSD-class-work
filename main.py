#Program to Calculate the average

#a=(10,20,30,40,50,60,70,80,90,100)
#c=sum(a)/len(a)
#print(c)

a1=[10,20,30,40,50,60,70,80,90,100]
print("List after reversing :" , a1.reverse())
print("List after sorting",a1.sort())
print("Does the list contains 50 :",a1._contains_(50))
print("POP :",a1.pop(1))
print("List after popping : ",a1)


#Program to accept an integer value from a user in python and to convert an input string value into integer using int function
a=input("Enter a value :")
print(type(a))
b=int(input("Enter b value :"))
print(type(b))

#Programme to add two complex float and integer numbers
a=complex(input("Enter a complex value :"))
b=complex(input("Enter another complex value :"))
c=a+b