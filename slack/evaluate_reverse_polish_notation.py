# Problem: Evaluate Reverse Polish Notation
# Pattern: Stack
# Time: O(n)
# Space: O(n)

class Solution:

    def evalRPN(self, tokens):

        stack = []

        for c in tokens:

            if c == "+":
                stack.append(stack.pop() + stack.pop())

            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(c))

        return stack[0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.evalRPN(["1","2","+","3","*","4","-"]))   # 5
    print(sol.evalRPN(["2","1","+","3","*"]))           # 9
    print(sol.evalRPN(["4","13","5","/","+"]))          # 6