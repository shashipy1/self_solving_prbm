'''
Author : S.K. Ranjha
Date : 03/10/2021
purpose : For practics
'''

def next_palindrom(n):
    n = n+1
    while not is_palindrom(n):
        n += 1
    return n

def is_palindrom(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("enter numbers of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number"))
        numbers.append(number)
    # print(numbers)
    for i in range(n):
        print(f"Next palindrom for {numbers[i]} is {next_palindrom(numbers[i])}")