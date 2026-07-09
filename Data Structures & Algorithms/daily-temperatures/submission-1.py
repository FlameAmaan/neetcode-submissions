class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[] #index
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                stackIdx=stack.pop()
                res[stackIdx]=i-stackIdx
            stack.append(i)
        return res
