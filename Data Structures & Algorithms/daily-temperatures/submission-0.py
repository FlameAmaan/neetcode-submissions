class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[] #index,temp
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                stackIdx,stackTemp=stack.pop()
                res[stackIdx]=i-stackIdx
            stack.append([i,temp])
        return res
