from typing import List


class MinStack:

    def __init__(self):
        self._stack: List[int] = []
        self._min_stack: List[int] = []
        
    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min_stack:
            current_value = min(self._min_stack[-1], val)
            self._min_stack.append(current_value)
        else:
            self._min_stack.append(val)
        return None

    def pop(self) -> None:           
        self._stack.pop()
        self._min_stack.pop()
        return None

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
