from typing import *

# [-2,1,-3,4,-1,2,1,-5,4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if max < sum:
                max = sum
            if sum < 0:
                sum = 0
        return max

sol = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(sol)
