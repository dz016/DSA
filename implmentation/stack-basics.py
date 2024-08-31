# Dictionary for operator precedence
precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3
}

# Function to convert infix expression to postfix expression
def infix2postfix(string):
    stack = []  # Initialize an empty stack
    ans = ""    # Resultant postfix expression
    i = 0       # Pointer to traverse the infix expression

    while i < len(string):
        # If character is an operator
        if string[i] in precedence:
            # Pop from stack to ans if top of stack has higher or equal precedence
            while len(stack) != 0 and precedence.get(stack[-1], -1) >= precedence[string[i]]:
                ans += stack.pop()
            stack.append(string[i])
        else:
            # If character is a closing parenthesis, pop until an opening parenthesis is found
            if string[i] == ")":
                while len(stack) != 0 and stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()  # Pop the opening parenthesis
            elif string[i] == "(":
                stack.append("(")  # Push the opening parenthesis to stack
            else:
                ans += string[i]  # Add operand to the resultant expression
        i += 1

    # Pop all the remaining operators in the stack
    while len(stack) != 0:
        ans += stack.pop()

    return ans

# Function to convert postfix expression to infix expression
def postfix2infix(string):
    stack = []  # Initialize an empty stack
    i = 0       # Pointer to traverse the postfix expression

    while i < len(string):
        # If character is an operand, push it to stack
        if string[i] not in precedence:
            stack.append(string[i])
        else:
            # Pop two elements from stack, form infix expression and push it back
            b = stack.pop()
            a = stack.pop()
            stack.append("(" + a + string[i] + b + ")")
        i += 1

    return stack[-1]

# Function to convert prefix expression to infix expression
def prefix2infix(string):
    stack = []  # Initialize an empty stack
    i = len(string) - 1  # Pointer to traverse the prefix expression from right to left

    while i >= 0:
        # If character is an operand, push it to stack
        if string[i] not in precedence:
            stack.append(string[i])
        else:
            # Pop two elements from stack, form infix expression and push it back
            a = stack.pop()
            b = stack.pop()
            stack.append("(" + a + string[i] + b + ")")
        i -= 1

    return stack[-1]

# Function to convert prefix expression to postfix expression
def prefix2postfix(string):
    stack = []  # Initialize an empty stack
    i = len(string) - 1  # Pointer to traverse the prefix expression from right to left

    while i >= 0:
        # If character is an operand, push it to stack
        if string[i] not in precedence:
            stack.append(string[i])
        else:
            # Pop two elements from stack, form postfix expression and push it back
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + string[i])
        i -= 1

    return stack[-1]

# Function to convert postfix expression to prefix expression
def postfix2prefix(string):
    stack = []  # Initialize an empty stack
    i = 0       # Pointer to traverse the postfix expression

    while i < len(string):
        # If character is an operand, push it to stack
        if string[i] not in precedence:
            stack.append(string[i])
        else:
            # Pop two elements from stack, form prefix expression and push it back
            a = stack.pop()
            b = stack.pop()
            stack.append(string[i] + b + a)
        i += 1

    return stack[-1]


# Test infix2postfix
print("Infix to Postfix:")
print(infix2postfix("a/f^b+c/(d+z/y+x)"),"Expected: afb^/cdzy/+x+/+")  # Expected: afb^/cdzy/+x+/+

# Test postfix2infix
print("\nPostfix to Infix:")
print(postfix2infix("ab+c*"),"Expected: ((a+b)*c)")  # Expected: ((a+b)*c)

# Test prefix2infix
print("\nPrefix to Infix:")
print(prefix2infix("+*AB/CD")," Expected: ((A*B)+(C/D))")  # Expected: ((a+b)*c)

# Test prefix2postfix
print("\nPrefix to Postfix:")
print(prefix2postfix("*+AB-CD"),"AB+CD-*")  # Expected: ab+c*+

# Test postfix2prefix
print("\nPostfix to Prefix:")
print(postfix2prefix("ab+c*"),"*+abc")  # Expected: *+abc
