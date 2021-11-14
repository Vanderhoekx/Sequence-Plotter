from collections import deque

class Queue:
    def __init__(self):
        self.rec_items = deque()
        self.penta_items = deque()
        self.prime_items = deque()

    def is_empty(self, sequence: list) -> bool:
        return not sequence

    def enqueue(self, item: int, sequence: list) -> list:
        return sequence.append(item)
    
    def dequeue(self, sequence: list):
        return sequence.popleft()
    
    def peek(self, sequence: list):
        return sequence[0]
    
    def size(self, sequence: list) -> int:
        return len(sequence)

    def __str__(self, sequence: list) -> str:
        return str(sequence)

