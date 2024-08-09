# Write a Python Program to# Write a Python Program to# Write a Python Program to Count Even and Odd number in list

list1 = [11, 5, 17, 18, 23]

length = len(list1)
even = 0
odd = 0
for ele in list1:
    
    if ele % 2 == 0:
        even+= 1        
    else:
        odd+= 1
        
print("Even Count : ",even)
print("Odd Count : ",odd)

