# for string
# seq_string = 'Python'
# print(list(reversed(seq_string)))

# for tuple
# seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# print(list(reversed(seq_tuple)))

# for range
# seq_range = range(5, 9)
# print(list(reversed(seq_range)))

# for list
# seq_list = [1, 2, 4, 3, 5]
# print(list(reversed(seq_list)))


# TAKE THE SIZE OF LIST FROM THE USER
print("Enter the number of list one by one:\n")
size = int(input("Enter the size of list\n"))

#INTIALIZE A BLANK LIST
mylist = []

# TAKE THE INPUTE FROM USER ONE BY ONE
for i in range(size):
    mylist.append(int(input("enter the elements\n")))
print(f"list is {mylist}")

mylist = [2, 5, 6, 4, 3]
print(f"list1 is {mylist}\n")

# FIRST METHOD OF PRINTING THE REVERSE LIST
rev1 = mylist[:]
mylist.reverse()
print(f"My first reverse list of {rev1} is {mylist}")


rev2 = mylist[::-1]
# SECOND METHOD OF PRINTING REVERSE LIST
print(f"My second reverse list of {mylist} is {rev2}")

#THIRD METHOD

rev3 = mylist[:]
for i in range(len(rev3)//2):
    rev3[i], rev3[len(rev3)-i-1] = rev3[(len(rev3))-i-1], rev3[i]
    # print(f"the reverse list at i={i} is {rev2}") list of reversing order

print(f"My third reverse list of {mylist} is {rev3}")

if rev1 == rev2 and rev2 == rev3:
    print("All three numbers give same result\n")