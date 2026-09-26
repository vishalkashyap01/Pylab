# import random as rm

# n = 0
# while n != 7:
#     n = rm.randint(1, 10)
#     print(n)


import random as vishal

num = vishal.randint(11, 50)
user_value = 0
user_attempt = 0

# cheating 
# print(num)

while num != user_value:
    print("Please, enter a number (1 to 50): ")
    user_value = int(input())
    
    user_attempt += 1
    
    if user_value == num:
        print(f"Great! You guess the number in {user_attempt}TH Attempt")
        
    elif user_value > num:
        print(f"Value is little bit Higher, Try Again...")
        
    elif user_value < num:
        print(f"Value is little bit Lower, Try Again...")
        
    else:
        print("Invalid!")    