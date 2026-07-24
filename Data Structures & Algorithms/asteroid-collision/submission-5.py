class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] == abs(ast):
                    stack.pop()
                    break
                elif stack[-1] < abs(ast):
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(ast)
        return stack