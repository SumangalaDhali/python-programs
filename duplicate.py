# Program To print duplicate and missing numbers

def answer(List):
    m=min(List)
    n=len(List)
    temp=[i for i in range(m,m+n)]
    a=[]
    repeated=-1
    missing =-1
    for i in List:
        if i not in a:
            a.append(i)
        else:
            repeated=i
    for i in temp:
        if i not in a:
            missing = i
    print(repeated,missing)

answer([17,19,18,18,21])





        



    
    

        
