'''
n=int(input("Enter a Number: "))
if n==0:
    print("Wrong input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
         '''

'''
n=int(input("enter an integer value:"))
print(float(n))
'''
x=0
str1="******************"
for i in str1:
    x=x-1
    print(str1[0:x])

for i in str1:
     x = x+ 1
     print(str1[0:x])


'''
x=int(input("Enter the number:"))
j=x
for i in range(x):
    print("\n")
    for j in range(x):
        print("*")

        j = j + 1

    i=i+1
'''

'''
a1=1045
a3="10100"
a2=int(format(int(a3,2),'d'))
print(a2)
a4=1045
a5=format(a4,'x')
print(a5)
'''
'''
a=input("Enter the numbers separated by space:")
x=[float(i) for i in a.split()]
avg=sum(x)/len(x)
print(avg)
'''
'''
a, b, c = map(float, input("Enter three sides of the triangle (space separated): ").split())
is_right_angle_triangle = sorted([a, b, c])[0]**2 + sorted([a, b, c])[1]**2 == sorted([a, b, c])[2]**2
print("It is a right-angled triangle." if is_right_angle_triangle else "It is not a right-angled triangle.")
'''
#Factorial of number1st
'''n=int(input("Enter a Number: "))
if n==0:    print("Wrong input")
else:    factorial=1
    for i in range(1,n+1):        factorial *= i
    print(factorial)
'''
#1st 7 multiples of 7 2nd one
'''i=7
j=1n=7
while(j<=n):    print(i,"*",j,"=",i*j)
    j+=1'''
#Right Angle Triangle 3rd one
'''x=0
str1="******************"for i in str1:
    x=x-1    print(str1[0:x])
for i in str1:
     x = x+ 1     print(str1[0:x])
         '''
'''
def binary_divisible_by_five(sequence):    binary_numbers = sequence.split(',')
    result_numbers = []
    for binary_number in binary_numbers:        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:            result_numbers.append(binary_number)
    result_sequence = ','.join(result_numbers)
    return result_sequence
# Sample data
#5th program
input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
# Process the input and print the resultoutput_sequence = binary_divisible_by_five(input_sequence)
print("Numbers divisible by 5:", output_sequence)
'''
#program1(Power)
''''n=int(input("Enter a Number"))
if n==0:    print("Wrong Input")
else:    for i in range (n,n+1):
        val = n*(n*1)        print(val)
'''
#program2(Print String increasing )'''''
x=0str1="ThisismyCountryIndia"
for i in str1:    x=x-1
    print(str1[0:x])for i in str1:
    x=x+1    print(str1[0:x])

#program3(pattern)
'''# Program for printing "*" according to the given input
n=int(input("Enter number of astriks you need:")) 
x=n for i in range (n):     
        print("*"*x) 
        x=x-1 x=1 
for i in range (n):         print("*"*x) 
        x=x+1
#program4(binary , decimal convertor)
a1="1010"
a2=int(format(int(a1,2),'d'))print(a2)
a3=1045
a4=format(a3,'x')print(a4)


#LAB EXCERCISE 1
#Calculate Average

a=(10,20,30,40,50,60,70,80,90,100)
c=sum(a)/len(a)print(c)

#Print type
a=input("Enter a value :")print(type(a))
b=int(input("Enter b value :"))print(type(b))

#add complex,float,int values
a=complex(input("Enter a complex value :"))b=complex(input("Enter another complex value :"))
c=a+bprint(c)
m=float(input("Enter a float value :"))
n=float(input("Enter another float value :"))o=m+n
print(o)
x=int(input("Enter a int value :"))y=int(input("Enter another int value :"))
z=x+yprint(z)

#convert int to float
n=int(input("Enter an integer value"))
print(float(n))
#addition of str and int

string = "123"
number = int(string)
print(f"Original string: {number}")print(f"After conversion to integer: {number}")
'''