class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        countT,window={},{}
        res,resLen=[-1,-1],float("infinity")
        l=0
        for i in t:
            countT[i]=countT.get(i,0)+1
        have,need=0,len(countT)
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    resLen=(r-l+1)
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1]

        
        