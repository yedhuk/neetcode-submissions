class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpn_stack = []
        operators = set(['+', '-', '*','/'])

        for t in tokens:
            
            if t not in operators:
                rpn_stack.append(t)
                print(f"added {t} to stack")

            else:
                ro = int(rpn_stack.pop())
                lo = int(rpn_stack.pop())
                print(f"applying {t} on {lo} and {ro}")
                match t:
                    case '+':
                        result = lo + ro
                    case '-':
                        result = lo - ro
                    case '*':
                        result = lo * ro
                    case '/':
                        result = lo / ro
                
                rpn_stack.append(result)
        print(f"RPN Stack : {rpn_stack}")
        if rpn_stack:
            result = int(rpn_stack[-1])

        return result

        