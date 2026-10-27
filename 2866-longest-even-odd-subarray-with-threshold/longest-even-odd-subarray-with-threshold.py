class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        ans = 0
        i = 0

        while i < n:
            if nums[i] % 2 != 0 or nums[i] > threshold:
                i += 1
                continue

            j = i

            while j < n and nums[j] <= threshold:
                if j > i and nums[j] % 2 == nums[j - 1] % 2:
                    break
                j += 1

            ans = max(ans, j - i)
            i = j if j > i else i + 1

        return ans