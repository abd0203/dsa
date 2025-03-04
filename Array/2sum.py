from typing import *
class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        nums_dict ={}
        for i in range(len(nums)):
            nums_dict[nums[i]] =i
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums_dict and nums_dict[dif]!= i:
                return [i,nums_dict[dif]]

data = Solution().twoSum(nums = [2,7,11,15], target = 9)
print(data)