def findNextGreater(arr):
    stack=[]
    nge= [-1] *len(arr)
    for i,ele in enumerate(arr):
        while stack and arr[stack[-1]] < ele:
            stackTop = stack.pop()
            nge[stackTop]=ele
        stack.append(i)
    return nge

print(findNextGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))


def previousGreater(arr):
    stack=[]
    pge =[-1]*len(arr)
    for i,ele in enumerate(arr):

        while stack and arr[stack[-1]] <=ele:
            stackTop = stack.pop()

        if stack:
            pge[i]= arr[stack[-1]]

        stack.append(i)
    return pge
print(previousGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))

def nextAndPreviousGreater(arr):
    stack =[]
    pge = [-1]*len(arr)
    nge =[-1]*len(arr)
    for i, ele in enumerate(arr):
        while stack and arr[stack[-1]] < ele:
            stackTop = stack.pop()
            nge[stackTop] = ele
        if stack:
            pge[i] = arr[stack[-1]]

        stack.append(i)
    return pge,nge

print(nextAndPreviousGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
