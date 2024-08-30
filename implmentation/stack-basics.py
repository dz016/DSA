#basic stack problems and implementation to learn stack

prcedence = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3

}


#infix2postfix
def infix2postfix(string):
    stack =[]
    ans=""
    i=0
    while i<len(string):
        if string[i] in prcedence:
            while len(stack) != 0 and prcedence.get(stack[-1],-1) >= prcedence[string[i]]:
                ans = ans + stack.pop()
            stack.append(string[i])
        else:
            if string[i] ==")":
                while len(stack) != 0 and stack[-1] != "(":
                    ans = ans + stack.pop()
                stack.pop()
            elif string[i] =="(":
                stack.append("(")
            else:
                ans = ans + string[i]
        i+=1
    while len(stack) != 0:
            ans += stack.pop()
    return ans

print(infix2postfix("a/f^b+c/(d+z/y+x)"))

#psotfix2infix
#afb^/cdzy/+x+/+

def postfix2infix(string):
    stack=[]
    i =0
    while i<len(string):
        if string[i] not in prcedence:
            stack.append(string[i])
        else:
            b= stack.pop()
            a= stack.pop()
            stack.append("(" + a + string[i] +b +")")
        i+=1
    return stack[-1]

def prefix2infix(string):
    stack=[]
    i =len(string)-1
    while i>=0:
        if string[i] not in prcedence:
            stack.append(string[i])
        else:
            a= stack.pop()
            b= stack.pop()
            stack.append("(" + a + string[i] +b +")")

        i-=1
    return stack[-1]

print("prefix2infix",prefix2infix("*-A/BC-/AKL")=="((A-(B/C))*((A/K)-L))")


print(postfix2infix("afb^/cdzy/+x+/+"))

def postfix2prefix(string):
    i = 0
    stack=[]
    while i<len(string):
        if string[i] not in prcedence:
            stack.append(string[i])
        else:
            a= stack.pop()
            b= stack.pop()
            stack.append(string[i] + b + a)

        i+=1
    return stack[-1]


print(postfix2prefix("ABC/-AK/L-*") =="*-A/BC-/AKL")
