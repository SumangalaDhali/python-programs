
def sort(List):
    c=len(List)//2
    for i in range(c):
        List[i],List[c+i]=List[c+i],List[i]
    return List

print(sort([1,2,3,-1,-2,-3]))