subj1=int(input("Enter the mark of 1st Subject:"))
subj2=int(input("Enter the mark of 2nd Subject:"))
subj3=int(input("Enter the mark of 3rd Subject:"))
subj4=int(input("Enter the mark of 4th Subject:"))
subj5=int(input("Enter the mark of 5th Subject:"))
avg=(subj1+subj2+subj3+subj4+subj5)/5
if(avg>=10):
    print("grade:A")
elif(avg>=80 and avg<=90):
    print("grade:B")
elif(avg>=70 and avg<80):
    print("grade:C")
elif(avg>=60 and avg<70):
    print("grade:D")
else:
    print("grade:E")
