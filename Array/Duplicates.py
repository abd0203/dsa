from typing import *

def containsDuplicate(self, nums: List[int]) -> bool:
    check = {}
    for i in range(len(nums)):
        if nums[i] in check:
            return True
        else:
            check[nums[i]] = 1
    return False

def containsDuplicates2(nums:List[int])-> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
        else:
            return False

