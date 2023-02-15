element = []
for i in range(10,1001):
    rev = 0
    temp = i
    while i>0:
        r=i%10
        rev = rev*10+r 
        i//=10
    if temp == rev:
        element.append(rev)
print(element)