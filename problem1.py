#1 The length of longest array with time complexity O(n**2)

def longsubArray(arr):
    max_length=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum == 0:
                max_length=max(max_length,j-i+1)
    return max_length          
l= longsubArray([2,2,1,-3,4,3,1,-8,6,-2,-1])
print("the length longest sub array with sum 0 is:",l)
print("With the time complexity O(n**2)")


            
