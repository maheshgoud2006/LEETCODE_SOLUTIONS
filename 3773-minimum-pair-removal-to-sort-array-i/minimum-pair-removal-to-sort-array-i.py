class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution(object):
    def minimumPairRemoval(self, nums):
        operations = 0

        while True:
            
            sorted_array = True

            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_array = False
                    break

            if sorted_array:
                return operations

            
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]

                if current_sum < min_sum:
                    min_sum = current_sum
                    index = i

        
            nums[index] = nums[index] + nums[index + 1]
            nums.pop(index + 1)

            
            operations += 1













        