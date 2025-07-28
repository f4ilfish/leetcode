from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains_to_idx: Dict[int, int] = {}
        
        for i, num in enumerate(nums):
            
            if num in remains_to_idx:
                return [remains_to_idx[num], i]

            remainder = target - num
            remains_to_idx[remainder] = i
        
        return [-1, -1]
