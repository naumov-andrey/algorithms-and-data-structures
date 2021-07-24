class MaxStack:
    def __init__(self):
        self._data = []
        self._max = []

    def push(self, val):
        self._data.append(val)
        if not self._max:
            self._max.append(val)
        else:
            self._max.append(max(self._max[-1], val))

    def pop(self):
        self._max.pop()
        self._data.pop()

    def max(self):
        return self._max[-1]


q = int(input())
max_stack = MaxStack()
for _ in range(q):
    cmd = input()
    if cmd.startswith('push'):
        max_stack.push(int(cmd.split()[1]))
    elif cmd == 'pop':
        max_stack.pop()
    elif cmd == 'max':
        print(max_stack.max())
