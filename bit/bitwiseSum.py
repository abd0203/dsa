class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_masking = 0xffffffff
        while((b & bit_masking)>0):
            carry = (a & b ) << 1
            a = (a ^ b)
            b = carry
        return a & bit_masking if b > 0 else a