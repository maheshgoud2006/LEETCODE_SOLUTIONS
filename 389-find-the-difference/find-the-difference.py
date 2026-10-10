class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count=0
        for i in t:
            if t.count(i)!=s.count(i) or i not in s:   
                return i
                break

            
        