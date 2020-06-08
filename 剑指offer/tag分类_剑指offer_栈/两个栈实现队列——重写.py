
# 还行，没啥难度

class CQueue:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def appendTail(self, value: int) -> None:
        # 原 -> 临时
        while self.stack:
            self.temp_stack.append(self.stack[-1])
            self.stack.pop()
        self.stack.append(value)
        while self.temp_stack:
            self.stack.append(self.temp_stack[-1])
            self.temp_stack.pop()

    def deleteHead(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()
