def findNextGreater(arr):
    stack=[]
    nge= [-1] *len(arr)
    for i,val in enumerate(arr):
        while stack and arr[stack[-1]] < arr[i]:
            stackTop = stack.pop()
            nge[stackTop]=i
        stack.append(i)
    return nge

print(findNextGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
