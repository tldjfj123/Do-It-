from typing import Any
from collections import deque

class Stack :
    def __init__(self, maxlen : int = 256) -> None :
        self.capacity = maxlen
        self.stack = deque([], maxlen)
    
    def __len__(self) -> int :
        return len(self.stack)
    
    def is_empty(self) -> bool :
        return len(self.stack) == 0
    
    def is_full(self) -> bool :
        return len(self.stack) == self.stack.maxlen
    
    def push(self, value : Any) -> None :
        self.stack.append(value)
    
    def pop(self) -> Any :
        return self.stack.pop()

    def peek(self) -> Any :
        return self.stack[-1]
    
    def clear(self) -> None :
        self.stack.clear()
    
    def find(self, value : Any) -> Any :
        try :
            return self.stack.index(value)
        except ValueError :
            return -1
    
    def count(self, value : Any) -> int :
        return self.stack.count(value)
    
    def __contains__(self, value : Any) -> bool :
        return self.count(value)
    
    def dump(self) -> int :
        print(list(self.stack))
            