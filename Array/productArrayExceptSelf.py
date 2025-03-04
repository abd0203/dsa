nums = [1, 2, 3, 4]
def product_array_except_self(nums):
    n = len(nums)
    result = [0] * n
    pre_product = 1
    post_product = 1
    for i in range(len(nums)):
        result[i] = pre_product
        pre_product = result[i] * nums[i]
    for i in range(len(nums)-1,-1,-1):
        result[i] = result[i]* post_product
        post_product = post_product*nums[i]
    return result
print(product_array_except_self(nums))
