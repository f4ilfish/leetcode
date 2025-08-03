from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency: Dict[int, int] = {}
        for num in nums:
            if num not in num_to_frequency:
                num_to_frequency[num] = 1
            else:
                num_to_frequency[num] += 1   
        sorted_numbers = [
            k for k, _ in 
            sorted(num_to_frequency.items(), key=lambda item: item[1], reverse=True)
        ]
        return [sorted_numbers[i] for i in range(k)]
