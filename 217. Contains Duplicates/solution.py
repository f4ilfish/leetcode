from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums: Set[int] = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False
