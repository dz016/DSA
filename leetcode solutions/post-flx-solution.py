class Solution:
    

    def evalRPN(self, tokens: List[str]) -> int:
            stack = []
            operators = {
                '+': lambda b, a: b + a,
                '-': lambda b, a: b - a,
                '*': lambda b, a: b * a,
                '/': lambda b, a: int(b / a),  # using int() to truncate towards zero
            }
            
            for token in tokens:
                if token in operators:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(operators[token](b, a))
                else:
                    stack.append(int(token))
            
            return stack[-1]