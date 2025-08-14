from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products, suffix_products = [1], [1]
        for i in range(1, len(nums)):
            previouse_prefix = prefix_products[i-1]
            current_prefix_multiplier = nums[i-1]
            prefix_products.append(previouse_prefix * current_prefix_multiplier)

            previouse_suffix = suffix_products[i-1]
            current_suffix_multiplier = nums[-i]
            suffix_products.append(previouse_suffix * current_suffix_multiplier)

        products: List[int] = []
        for i in range(len(nums)):
            prefix_multiplier = prefix_products[i]
            suffix_multiplier = suffix_products[-i-1]
            products.append(prefix_multiplier * suffix_multiplier)
        
        return products

if __name__ == "__main__":
    nums = [1,2,4,6]
    products = Solution().productExceptSelf(nums=nums)
    print(f"Input: {nums}")
    print(f"Output: {products}")
