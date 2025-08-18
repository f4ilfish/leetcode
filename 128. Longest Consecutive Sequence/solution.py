from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = set(nums)
        sort_nums = list(unique_nums)
        sort_nums.sort()
        
        last_max_streak = 1
        current_streak = 1
        for i in range(1, len(sort_nums)):
            if (sort_nums[i] - 1) not in unique_nums:
                last_max_streak = max(last_max_streak, current_streak)
                current_streak = 1
                continue
            current_streak += 1
            
        return max(last_max_streak, current_streak)


if __name__ == "__main__":
    nums=[9,1,4,7,3,-1,0,5,8,-1,6]
    max_length = Solution().longestConsecutive(nums=nums)
    print(max_length)
