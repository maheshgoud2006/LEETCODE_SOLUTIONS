class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        j=0
        for ch in s:
            if ch=="(":
                count+=1
            else:
                if count >0:
                    count-=1
                else:
                    j+=1
        return count+j
            



        
        