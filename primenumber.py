n=int(input("Enter n numbers to be printed"))
for i in range(2,n+1):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
            break
    if c==0:
        print(i,end=" ")
    continue
