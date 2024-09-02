
import math
def solution(rectangles):
    maxLen = min(min(rectangles,key= lambda x:min(x)))
    print(maxLen)
    count =0
    for i in range(len(rectangles)):
        if min(rectangles[i])==maxLen:
            count +=1
    return count









print(solution([[5,2],[3,9],[4,12],[16,5]]))
