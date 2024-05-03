#!/usr/bin/env python
# coding: utf-8

# In[28]:


# assigment operators
# Comparision operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# In[3]:


# 1) calculate the sum , difference, product, and quotient of two number?

number1 = int(input("Enter the frist number..."))
number2 = int(input("Enter the secound number..."))

print("The valve of Sum", number1,"+",number2,"is : ",number1+number2)
print("The valve of Difference", number1,"-",number2,"is : ",number1-number2)
print("The valve of Product", number1,"*",number2,"is : ",number1*number2)
print("The valve of Quotient ", number1,"/",number2,"is : ",number1/number2)
print("The valve of Remainder", number1,"%",number2,"is : ",number1%number2)


# In[4]:


number1 = int(input("Enter the frist number..."))
number2 = int(input("Enter the secound number..."))

ch = input("Enter any of these char for specific operation +,-,*,/,%, : ")

#result = 0
if ch == "+" :
    print("sum is", number1+number2)
elif ch == "-":
    print("Difference is",number1-number2)
elif ch == "*":
    print("Product is", number1*number2)
elif ch == "/":
    print("Quotient is",number1/number2)
elif ch == "%":
    print("Remainder is",number1%number2)
else:
    print("Input character is not recognized...")
    
#print(number1, ch, number2, " : ",result)    


# In[1]:


# 2) perform various assignment operation on a variable?

# List of assignment Operators.
# 1) Assign = (=)
# 2) Add and Assign(+=)
# 3) Subtract and Assigment(-=)
# 4) Multiply and Assign(*=)
# 5) Divide and assign(/=)
# 6) Modulus and assign(%=)
# 7)  Divide (floor) and assign(//=)

x = 10
y = 20
x = x+y
print("This is assign operators",x) 
x +=y
print("This is add and assign",x)
x 

-=y
print("This is substraction and assign",x)
x *=y
print("This is Multiply and assign",x)
x /=y
print("This is Divied and assign",x)
x %=y
print("This is Modules and assign",x)
x //=y
print("This is Divide(floor) and assign",x)


# In[4]:


# 3 Compare two number and print the result ?

num1 = int(input("Enter the frist number..."))
num2 = int(input("Enter the secound number..."))

if num1 > num2:
    print(num1," is greater then ",num2)
elif num1 < num2:
    print(num1," is small then ",num2)   
elif num1 == num2:
    print("The two given number are equal...")
elif num1 >=0 and num1<= num2:
    print(num1," is greater then equal to ",num2)    # 10>=20
elif num1 <= num2:  
    print(num1," is smaller then equal to ",num2)   
elif num1 !=  num2:
    print(num1," is not equal to ",num2)  
else:
    print("could not find true expresstion...")
#print(number1, ch, number2, " :",result) 


# In[5]:


# 4 Cheak the condition using logical operators?

#   and = cheak two or more condition if true
#   or = cheak if at least one condition is true
#   not = true if condition is false,and vise versa

a = int(input("Enter a any  frist number  ..."))
b = int(input("Enter a any secound value ..."))

print("This is and operators=", a >b and b < a)
    
print("This is or operators =", a >b or b < a)
 
print("This is not operators =",not (a<0))    


# In[ ]:


# 5 Cheak the identity of variables.
x = 10
y = 10
print(x is y)
z=x
print(z is x)
print(id(x))
print(id(y))
print(id(z))


# In[29]:


# 6) perform bitwise opertions on any two integers.

print("Bitwise AND")
a = (0b1010)
b = (0b1100)
c = a & b  # 1000
print(bin(c))

print("Bitwise OR")
a = (0b1010)
b = (0b1100)
c = a or b  #     1110
print(bin(c))

print("Bitwise XOR")
a1 = (0b1010)
a2 = (0b1100)
c = a1 ^ a2  # 0110
print(bin(c))

print("Bitwise not")
a = (0b1010)
c = ~a
print(bin(c))

print("Bitwise left shift")
a = 0b1010
c = a <<2
print(bin(c))

print("Bitwise right shift")
a = 0b1010
c = a >> 1
print(bin(c))


# In[55]:


# 7) Use unary opertors to change the sign of a number.
# unary opertors >> requide only one operand
# unary opertors >> unary +,unary -,invert or complement(~)

# unary +
x = 7
x
x = +x
x

# unary -
y = 4
-y

# complement unary

~34


# In[2]:


# 8) Use the ternary operator to assign valves based on condition.

age = int(input("Enter your age ..."))
print("adult" if age >=18 else "Minor")


# In[4]:


num = int(input("Enter the number..."))
print("Positive" if num >0 else "Nagative")

