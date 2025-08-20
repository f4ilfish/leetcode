from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paranthesises: List[str] = []
        brackets = ["(", ")"]
        self._backtrack(brackets, n*2, 0, 0, [], paranthesises)
        return paranthesises

    def _backtrack(
        self, 
        brackets: List[str], 
        paranthesis_length: int,
        open_brackets_count: int,
        close_brackets_count: int,
        paranthesis: List[str],
        paranthesises: List[str],
    ) -> None:
        
        if close_brackets_count > open_brackets_count:
            return
        
        if len(paranthesis) == paranthesis_length:

            if open_brackets_count != close_brackets_count:
                return

            paranthesises.append("".join(paranthesis))
            return

        for bracket in brackets:
            paranthesis.append(bracket)
            if bracket == "(":
                open_brackets_count += 1
            else:
                close_brackets_count += 1
            self._backtrack(
                brackets, 
                paranthesis_length, 
                open_brackets_count, 
                close_brackets_count,
                paranthesis, 
                paranthesises,
            )
            paranthesis.pop()
            if bracket == "(":
                open_brackets_count -= 1
            else:
                close_brackets_count -= 1
            

if __name__ == "__main__":
    n = 3
    parenthesises = Solution().generateParenthesis(n)
    print(parenthesises)
