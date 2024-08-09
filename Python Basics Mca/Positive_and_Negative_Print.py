# Write a Python Program to print all negative and postive number in a list

list1 = [10, -21, 4, -45, 66, -93, 1]
 
neg_count = 0
 

print("Negative Numbers List :")
for num in list1:
 
    if num <= 0:
        print(num)
        
        
print("Positive Number List :")

for num in list1:
    
    if num >= 0:
        print(num)