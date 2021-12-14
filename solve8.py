import random

def rohanMultiolication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1
    return None


if __name__ == '__main__':
    # print(rohanMultiolication(7))
    number = int(input("Enter the number\n"))
    myTable = rohanMultiolication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")

