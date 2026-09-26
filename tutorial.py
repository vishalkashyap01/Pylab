""""Comments"""
# comments


# Integer
# a = 9
# print(type(a))

# float
# f = 9.7
# g = 4/8
# print(type(f))
# print(type(g))

# String
# gtr = "any symbols, letters, numbers, and spaces"
# print(type(gtr))

# Boolean      (first letter of bollean is Captial)
# sde = True
# print(type(sde))

# Comple x numbers
# h = 3 + 4j   (only j is used to represent complex numbers in python)
# print(type(h))

# c = 4j
# print(type(c))


# Strings
# a = "v"
# print(ord(a))  # ord() function returns the Unicode code point for a given character
# print(chr(118))  # chr() function returns the character for a given Unicode code point


# simple string
# name = "Vishal"
# age = 22
# print("My name is ", name, " and my age is ", age)

# # Formated String
# job = "Software Engineer"
# org = "Deloitte"
# ctc = 18_00_000
# print(f"I'm a {job} at {org} with the ctc of {ctc} per annum")


# Input
# input("enter role: ")
# num = int(input("enter number: "))
# print(num)


# Operators
# Arithmetic Operators
# +, -, *, /, %, **, //

# a = 10
# b = 5
# print(a/b) # division " / " returns float value  --> 2.0
# print(a//b) # floor division " // " returns integer value  --> 2
# print(2**8) # exponentiation " ** " returns power value  --> 256
# print(10%3) # modulus " % " returns remainder value  --> 1


# Assignment Problems - 1
# gen = input("Please, enter your gender: ")
# if gen == "m":
#     print(f"Good evening, Sir!")
# else:
#     print(f"Good evening, Ma'am!")    

# problem - 2
# name = input("Please, enter your name: ")
# age = int(input("put your age here: "))

# if age >= 18:
#     print(f"Hello {name}, you are eligible to vote!")
# else:
#     print(f"Hello {name}, you are not eligible to vote!")
#     print(f" you will vote after {18 - age} years")    


# Problem  - 3
# # leap year (century year - /400, reg yr - /4)

# year = int(input("Please, tell me year:- "))
# if year % 4 == 0:
#     if year % 400 == 0 and year % 100 == 0:
#         print(f"{year} is a century leap year")
#     else:
#         print(f"{year} is a regular leap year")
# else:
#     print(f"{year} is not a leap year")             



# range() function
# a = range(2, 25, 3)
# print(a)
# print(list(a))

# Loops - for & while

# For loop
# 20 - 50 
# for i in range(20, 51):
#     print(i)
    
# 10 - 4
# for i in range(10, 3, -1):
#     print(i)    

# -3 to -15
# for i in range(-2, -16, -1):
#     print(i)

# for i in range(1, 11):
#     print(i*5)

# str = "JAI SHREE RADHE"

# print(len(str))
# for i in range(len(str)):
#     print(str[i])
# for i in str:
#     print(i)
# for i in range(len(str)-1, -1, -1):
#     print(str[i])
# for i in str[::-1]:
#     print(i)

# Falsy values
# print(bool(0))
# print(bool(""))
# print(bool([])) 
# print(bool(()))
# print(bool({}))
# print(bool(None))
# print(bool(False))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# prime = True
# for i in range(2, 500):
#     half_life = int(i/2+1)
#     for j in range(2, half_life):
#         if i % j == 0:
#             prime = False
#             break
#         else:
#             prime = True
#     if prime:
#         print(i)


# PRACTICE QS 

# n = int(input("Please, type number - "))
# for i in range(1, n+1):
#     print("solve more & more problems")


# n = int(input("Please, type number - "))
# for i in range(1, n+1):
#     print(i)


# n = int(input("Please, type number - "))
# for i in range(n, 0, -1):
#     print(i)
    

# n = int(input("please, enter any number: "))   
# sum = 0 
# for i in range(1, n+1):
#     sum += i
# print(sum)    



# n = int(input("please, enter any number: "))   
# factorial = 1 
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)    



# n = int(input("Please, give some number here "))
# for i in range(2, int(n/2+1)):
#     if n % i == 0:
#         print(f"{n}'s factor is {i}")       



# Check number is Perfect or Not
# n = int(input("enter a number - "))
# flag = 1
# for i in range(1, int(n/2+1)):
#     if flag < n:
#         flag *= i
#         if flag == n:
#             print(f"{n} is Perfect number")
#             break
# else:
#     print(f"{n} is not perfect number")


# Pallindrome string

# str = input("Pleae, enterr any string: ")
# new_str = ""
# for i in range(len(str)-1, -1, -1):
#     new_str += str[i]

# if str == new_str:
#     print(f"{str} is a pallindrome string")
# else:
#     print(f"{str} is not a pallindrome string")    


# for i in range(18, 181, 18):
#     print(i)

# n  = int(input("Please, enter any number: "))
# for i in range(n, n*10+1, n):
#     print(i)


# ??? else with For loop when loop breaks without completing all iterations, else block will not execute.
# break exceute --> else block will not execute.
# break not execute --> else block will execute.

# for i in range(10, 51,10):
#     if i == 25:
#         break
#     print(i)    
# else:
#     print("Else executed")    


# for i in range(1, 10):
#     if i == 8:
#         break
#     print(i)    
# else:
#     print("Else executed")  


# # Reverse String
# str = input("Please, enter any string: ")
# for i in range(len(str)-1, -1, -1):
#     print(str[i])



# str = "abhscb&^$#@$0982rgO21"
# dgit = 0
# alpha = 0
# keys = 0
# for i in str:
#     if i.isdigit():
#         dgit += 1
#     elif i.isalpha():
#         alpha += 1  
#     else:
#         keys += 1
        
# print(f"Total digits in string are {dgit}")
# print(f"Total alphabets in string are {alpha}")
# print(f"Total special characters in string are {keys}")                


# WHILE LOOP  (ctrl + c ---> stop terminal for infinite loop)

# a = 5
# while a < 10:
#     print(a)
#     # a += 1
        
# REVERSE NUMBER OR PALINDROME NUMBER
# n = int(input("Please, enter any number : "))
# reference = n
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10    
# print(rev)  

# if reference == rev:
#     print(f"{reference} is a Palindrome")
# else:
#     print(f"{reference} is Not Palindrome")    


# Seperate digit from number

# n = int(input("enter a value here: "))
# while n != 0:
#     print(f"digit - {n % 10}")
#     n = n // 10  

# functions

# positional arguments :- Args()

def greet():
    print("Good evening! Vishal")
    print("heavy raining outside... happy coding </>")

greet()


# Keyword arguments :- K-Args()

# def greet(name, temp):
#     print(f"Hello, {name} \n weather condintions : {temp} C")

# greet(temp = 27, name = "Vishal")       # keyword args 
# greet("kavita", 24)         # positional args































