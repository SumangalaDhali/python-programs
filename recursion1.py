def tri_recursion(k):
    if (k > 10):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\n Recursion Example Results")
tri_recursion(20)
