r= int(input("enter the rows:"))
for i in range(r):
    for j in range(r-1-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
