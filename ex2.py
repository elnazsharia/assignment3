
from random import randint

i = 0
Num = []
user_n = input("how many numbers you wanna add to your array?")


while (i < int(user_n)):
    numbers = randint(1, 100)
    if numbers not in Num:
        Num.append(numbers)
        i += 1

print(Num)
