from typing import *

def maxProduct(self, nums: List[int]) -> int:
    maxx = nums[0]
    pro = 1
    suf = 1
    for i in range(len(nums)):
        pro = pro * nums[i]
        suf = suf * nums[len(nums) - i - 1]
        if pro > maxx:
            maxx = pro
        if suf > maxx:
            maxx = suf
        if pro == 0:
            pro = 1
        elif suf == 0:
            suf = 1
    return maxx