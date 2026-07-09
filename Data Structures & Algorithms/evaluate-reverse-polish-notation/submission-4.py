class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=set(["+","-","*","/"])
        stack=[]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(a-b)
                elif i=="*":
                    stack.append(a*b)
                elif i=="/":
                    stack.append(int(a/b))
                else:
                    return False
        return stack[-1]