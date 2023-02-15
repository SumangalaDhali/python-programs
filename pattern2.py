rows=int(input("enter the rows: "))
for i in range(rows):
    for j in range(rows):
        if i+j>=rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
     
for i in range(rows):
    for j in range(rows):
        print(" ",end=" ")
    for j in range(rows-i):
        print("*",end=" ")
    print()






    

