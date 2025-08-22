from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        forecast: List[int] = [0] * len(temperatures)
        stack_temp_to_idx: List[Tuple[int, int]] = []
        
        for i, temp in enumerate(temperatures):
            while stack_temp_to_idx and temp > stack_temp_to_idx[-1][0]:
                _, stackIdx = stack_temp_to_idx.pop()
                forecast[stackIdx] = i - stackIdx
            stack_temp_to_idx.append((temp, i))
        
        return forecast


if __name__ == "__main__":
    temperatures = [30,38,30,36,35,40,28]
    forecast = Solution().dailyTemperatures(temperatures)
    print(forecast)
