n=int(input("Enter the number:"))
a=1
count=0
while(a<=n):
    if(n%a==0):
        count+=1
    a+=1
if(count==2):
    print("The number is a prime")
else:
    print("The number is not a prime")
    