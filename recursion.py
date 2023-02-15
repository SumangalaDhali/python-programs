def func(List):
    n=len(List)
    for i in range(n-1):
        if List[i]>List[i+1]:
            List[i],List[i+1] = List[i+1],List[i]
            func(List)
    return List

print(func([0,1,0,1,-1,0,-1,-1]*1000))
        