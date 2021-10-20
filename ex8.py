p, q, x, g = 0, 0, 0, 0


print("Enter the two positive integer numbers")
p = int(input())
q = int(input())

for i in range(1, p + 1):
    if i <= q:
        if p % i == 0 and q % i == 0:
            g = i

x = (p * q) / g

print("\nThe LCM of two positive numbers ", p, " & ", q, " is ", x, ".")
