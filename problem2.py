#local minima with O(n)
def localminima(Array):
    l1=[]
    for i in range(len(Array)-1):
        if Array[i-1]>Array[i]<Array[i+1]:
            l1.append(Array[i])
    if Array[-1] < Array[-2]:
        l1.append(Array[-1])
    return min(l1)

local=localminima([-1,2,1,-3,4,3,1,-8,6,2,-1])
print("local minima with O(n) time complexity:",local)
