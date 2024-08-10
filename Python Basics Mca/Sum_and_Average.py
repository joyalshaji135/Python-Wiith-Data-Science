# Write a Python Program to find sum and average of list 

total = 0
 
list1 = [11, 5, 17, 18, 23]

length = len(list1)

for ele in range(0, len(list1)):
    total = total + list1[ele]

average = total / length

print("Sum of all elements in given list: ", total)

print("Average of all elements in given list: ", average)

