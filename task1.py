# Sum of two numbers - Take input and print their sum
print("SUM OF TWO NUMBERS - TAKE INPUT AND PRINT THEIR SUM")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=a+b
print("Sum of two numbers:",s)

# Odd or even checker- Check if a number is even or odd
print("ODD OR EVEN CHECKER - CHECK IF A NUMBER IS EVEN OR ODD")
n=int(input("Enter number:"))
if(n%2==0):
    print("Even number")
else:
    print("Odd number")
    
# Factorial Calculation (Using Loop)
print("FACTORIAL CALCULATION (USING LOOP)")
n=int(input("Enter number:"))
f=1
for i in range(1,n+1):
    f*=i
print("Factorial:",f)

# Factorial Calculation (Using Recursion)
print("FACTORIAL CALCULATION (USING RECURSION)")
def facto(n):
    if(n==0 or n==1):
        return(1)
    else:
        return(n*facto(n-1))
a=int(input("Enter number:"))
print("Factorial:",facto(a))

# Fibonacci Sequence - Generate First n numbers
print("FIBONACCI SEQUENCE - GENERATE FIRST N NUMBERS")
n=int(input("Enter how many numbers to be generated in Fibonacci Sequence:"))
a,b=0,1
print(f"Fibonacci Sequence of first {n} numbers are:")
for i in range(n):
    print(a)
    a,b=b,a+b
    
# String Reverse - Reverse user input string
print("STRING REVERSE - REVERSE USER INPUT STRING")
s1=input("Enter string:")
s2=""
for i in s1:
    s2=i+s2
print("Reversed string:",s2)

# Palindrome Check - Is the word same forward and backward?
print("PALINDROME CHECK - IS THE WORD SAME FORWARD AND BACKWARD?")
s1=input("Enter string:")
s2=""
for i in s1:
    s2=i+s2
if(s1.lower()==s2.lower()):
    print("Palindrome String")
else:
    print("Not Palindrome String")
    
# Leap Year Check - Check if a given year is leap year
print("LEAP YEAR CHECK - CHECK IF A GIVEN YEAR IS LEAP YEAR")
n=int(input("Enter year:"))
if(n%100==0):
    if(n%400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    if(n%4==0):
        print("Leap Year")
    else:
        print("Not Leap Year")

# Check Armstrong Number
print("ARMSTRONG NUMBER CHECKER")
def armstrong(n):
    copy=n
    c=0
    while(copy>0):
        c+=1
        copy//=10
    copy1=n
    s=0
    while(copy1>0):
        s+=((copy1%10)**c)
        copy1//=10
    return(s)
a=int(input("Enter number:"))
if(a==armstrong(a)):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
        
        
