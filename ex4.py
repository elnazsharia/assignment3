
# factorial of any number
def isFactorial(m):
    i = 1
    while(True):

        if (m % i == 0):
            m //= i

        else:
            break

        i += 1

    if (m == 1):
        return True

    else:
        return False


# Driver Code
if __name__ == "__main__":
    n = input("enter a number!")
    m = int(n)
    ans = isFactorial(m)

    if (ans == 1):
        print("Yes")

    else:
        print("No")

# This code is contributed by kanugargng
