# data_structures.py

class Stack:
    ### A simple stack implementation. ###
    def __init__(self):
        self.stack = []

        def push(self, item):
            self.stack.append(item)

            def pop(self):
                return self.stack.pop() if self.stack else None

            def is_empty(self):
                return len(self.stack) == 0

            class Queue:
                ### A simple queue implementation. ###
                def __init__(self):
                    self.queue = []

                    def enqueue(self, item):
                        self.queue.append(item)

                        def dequeue(self):
                            return self.queue.pop(0) if self.queue else None

                        def is_empty(self):
                            return len(self.queue) == 0

