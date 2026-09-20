#1 Display prime numbers from 1 to 500 (14th Sept)

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

# FOR SPecific Number
        
# n = int(input("Please, enter any number :- "))
# counter = True
# half_life = int(n/2+1)
# for i in range(2, half_life):
#     if i % n == 0:
#         counter = False
#         break
#     else:
#         counter = True

# if counter:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")  


#2 Given two strings, str1, and str2, where str1 contains exactly one character more than str2, 
# find the indices of the characters in str1 that can be removed to make str1 equal to str2. 
# Return the array of indices in increasing order. If it is not possible, return the array \[-1\]. 
# **Note:** Use 0-based indexing.
# **Example**
# str1 = "abdgggda"
# str2 = "abdggda"
# Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return \[3, 4, 5\].

str1 = "12444489"        # 0[1] 1[2] 2[4] 3[4] 4[4] 5[8] 6[9]
str2 = "124489"

flag = 0
index = 0
str1_len = len(str1)-1
for i in range(0, str1_len):
    if str1[i] == str1[i+1]:
        flag += 1
        if flag == 1:
            index = i

flag = flag + 1
end = index + flag

for i in range(index, end):
    print(f"[{i}]")             
    