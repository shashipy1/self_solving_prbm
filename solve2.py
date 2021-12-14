n = int(input("Enter the value of n: "))
mn = int(input("Enter the value of mn: "))
mx = int(input("Enter the value of mx: "))

for i in range(mn, mx+1):
    if n%i==0:
        print(f"{i} is divisor of {n}")
    else:
        print(f"{i} is not divisor of {n}")

