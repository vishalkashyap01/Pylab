# Display prime numbers from 1 to 500 (14th Sept)

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
        
n = int(input("Please, enter any number :- "))
counter = True
half_life = int(n/2+1)
for i in range(2, half_life):
    if i % n == 0:
        counter = False
        break
    else:
        counter = True

if counter:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")  