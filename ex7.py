first_num = input('Please input the first integer:')
second_num = input('Please input the second integer:')

for i in range(1, second_num+1):
    if first_num % i == 0 and second_num % i == 0:
        gcd = i
print(gcd)
