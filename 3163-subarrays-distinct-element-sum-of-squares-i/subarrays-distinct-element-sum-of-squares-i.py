class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            seen=set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                total = total + len(seen)**2
        return total


            




        