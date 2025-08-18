
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if s.strip() == "":
            return False        
        if len(s) % 2 != 0:
            return False
        close_to_open_chars = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack: List[str] = []
        for char in s:
            if char in close_to_open_chars.values():
                stack.append(char)
            if char in close_to_open_chars.keys():
                if stack and stack[-1] == close_to_open_chars[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


if __name__ == "__main__":
    s="[]"
    is_valid_parentheses = Solution().isValid(s)
    print(is_valid_parentheses)
