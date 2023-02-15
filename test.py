List=[28,31,31,29,30]
l=[]
n=len(List)
for i in List:
    if i not in l:
        l.append(i)
    else:
        repeated=i
print(repeated,end=" ")
m=min(List)
temp = [i for i in range(m,m+n)]
for k in temp:
    if k not in List:
        missing = k
print(missing)



