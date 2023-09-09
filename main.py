import random
base =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int(input("какой размер пороля"))

password = ""

123
for i in range(size):
    k = random.randint(0, len(base) - 1)
    password += base [k]

print(password)





