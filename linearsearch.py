def linearsearch(list ,n,x):
    #going through the array sequentially
    for i in range(0,n):
        if (list[i]==x):
            return i
    return -1

list = [3,6,9,1,22,3,8]
x=22
n = len(list)
result=linearsearch(list,n,x)
if result == -1:
    print("element not found")
else:
    print("element found",result)