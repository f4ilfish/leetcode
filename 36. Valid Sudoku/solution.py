from typing import List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets: List[Set[str]] = [set() for _ in range(len(board))]
        column_sets: List[Set[str]] = [set() for _ in range(len(board))]
        
        for row_idx, row in enumerate(board):
            for column_idx, element in enumerate(row):
                if element == ".":
                    continue
                if element in row_sets[row_idx]:
                    return False
                if element in column_sets[column_idx]:
                    return False
                row_sets[row_idx].add(element)
                column_sets[column_idx].add(element)

        for square_idx in range(len(board)):
            square_elements: Set[str] = set()
            for i in range(3):
                for j in range(3):
                    row_idx = (square_idx // 3) * 3 + i
                    column_idx = (square_idx % 3) * 3 + j
                    element = board[row_idx][column_idx]
                    if element == ".":
                        continue
                    if element in square_elements:
                        return False
                    square_elements.add(element)
        
        return True

if __name__ == "__main__":
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    is_valid = Solution().isValidSudoku(board=board)
    print(is_valid)
