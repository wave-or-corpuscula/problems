# https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=problem-list-v2&envId=dsa-sequence-valley-queue

from collections import deque


class MyQueue:

    def __init__(self):
        self._queue = deque([])
        self._buffer = deque([])
        

    def push(self, x: int) -> None:
        N = len(self._queue)
        for _ in range(N):
            self._buffer.append(self._queue.pop())
        self._queue.append(x)
        for _ in range(N):
            self._queue.append(self._buffer.pop())

    def pop(self) -> int:
        return self._queue.pop()

    def peek(self) -> int:
        peek = self._queue.pop()
        self._queue.append(peek)
        return peek

    def empty(self) -> bool:
        return len(self._queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()