
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
        i = 0
        while i < len(s):
            char = s[i]
            if char in close_to_open_chars.values():
                stack.append(s[i])
            if char in close_to_open_chars.keys():
                try:
                    open_char = stack.pop()
                    if open_char != close_to_open_chars[char]:
                        return False
                except IndexError:
                    return False
            i += 1
        return False if i == len(s) else True

if __name__ == "__main__":
    s="[]"
    is_valid_parentheses = Solution().isValid(s)
    print(is_valid_parentheses)
