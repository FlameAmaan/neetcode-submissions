class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charS=set()
        longest=0
        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l+=1
            charS.add(s[r])
            longest=max(longest,len(charS))
        return longest

