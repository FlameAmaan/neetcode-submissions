class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sHash={}
        tHash={}
        for i in s:
            if i in sHash:
                sHash[i]+=1
            else:
                sHash[i]=1
        for i in t:
            if i in tHash:
                tHash[i]+=1
            else:
                tHash[i]=1
        for i in sHash:
            if i in tHash and tHash[i]!=sHash[i] or i not in tHash:
                return False
        return True
            


        