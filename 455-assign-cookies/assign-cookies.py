class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        i=0
        j=0
        count=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count 




        