class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []


        

    def push(self, val: int) -> None:
        
        if not self.stack:
            self.stack_min.append(val)

        elif val <= self.stack_min[-1]:
            self.stack_min.append(val)

        self.stack.append(val)
        

    def pop(self) -> None:
        
        if self.stack[-1] > self.stack_min[-1]:
            self.stack.pop()
        
        else:
            self.stack_min.pop()
            self.stack.pop()              
        

        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.stack_min[-1] if self.stack_min else None

        
