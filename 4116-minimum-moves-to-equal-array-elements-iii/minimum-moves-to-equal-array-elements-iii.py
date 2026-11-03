class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=max(nums)
        c=0
        
        for i in nums:
            if i<=k:
                c=c+(k-i)
        return c