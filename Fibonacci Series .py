a=int(input("Enter the terms -"))
f=0
s=1
if a<=0:
    print("Incorrect Input")
else:
    print("The requested series is",a)
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
