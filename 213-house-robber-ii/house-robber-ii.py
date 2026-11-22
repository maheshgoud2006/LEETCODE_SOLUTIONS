class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n == 1:
            return nums[0]

        def solve(nums):

            prev1=0
            prev2=0

            for num in nums:
                curr=max(prev1,num+prev2)
                prev2=prev1
                prev1=curr
            return prev1
        return max(solve(nums[:-1]),solve(nums[1:]))
