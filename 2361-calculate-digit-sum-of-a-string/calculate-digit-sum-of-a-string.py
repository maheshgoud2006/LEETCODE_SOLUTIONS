class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=len(s)
        if l<=k:
            return s
        else:
            m=[]
            for i in range(0,len(s),k):
                m.append(s[i:i+k])

            res=""
            for group in m:
                total=0
                for digit in group:
                    total+=int(digit)
                res+=str(total)
            
            return self.digitSum(res, k)
        


         


        



       
            





        