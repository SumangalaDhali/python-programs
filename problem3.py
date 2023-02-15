# longest subarray with sum 0 on time complexitity O(n)
def longestsubarr(array):
    sums = {}
    sum=0
    max_length = 0
    for i,j in enumerate(array):
        sum+=j
        if sum==0:
            max_length = i+1
        elif sum in sums:
            length = i-sums[sum]
            if length > max_length:
                max_length=length
        else:
            sums[sum]=i
    return max_length
    
Array=longestsubarr([2,2,1,-3,4,3,1,-8,6,-2,-1])
print("the length of longest subarray is:",Array)
print("the time complexity O(n)")

    
   