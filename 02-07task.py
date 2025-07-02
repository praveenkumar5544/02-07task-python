#1.Write a program to input two numbers from the user and display the result of addition, subtraction, multiplication, and division


a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))

print('Addition: ',a+b)
print('Subtraction: ',a-b)
print('Multiplication: ',a*b)
print('Division:',a/b)


# 2. Accept marks from the user and print the grade:

# 90–100: A

# 80–89: B

# 70–79: C

# 60–69: D

# <60: F


mark = int (input('you mark : '))

if  mark < 100 :
    print ('grade A')

elif mark > 80 and mark < 89 :
    print ('grade B')

elif mark > 70 and mark < 79 :
    print ('grade C')

elif mark > 60 and mark < 69 :
    print ('grade D')

else :
    print('fail')    

# 3. Write a program that takes three numbers and prints the largest one
        
one = int(input('enter first number : '))
two = int (input('enter the second number : '))
three = int (input('enter the 3rd number : '))

if one > two and one > three :
    print('1st number')

elif two > one and two > three :
    print ('2nd number')

else:
    print ('3rd number')
