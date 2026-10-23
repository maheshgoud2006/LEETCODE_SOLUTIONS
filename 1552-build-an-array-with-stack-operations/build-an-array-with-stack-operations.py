class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result=[]
        for i in range(1,n+1):
            result.append("Push")
            if i  not in target:
                result.append("Pop")
            if target[-1]==i:
                break
        return result
            

            
                






        