from collections import deque

size, n = [int(i) for i in input().split()]
buffer = deque()
for _ in range(n):
    arrival, duration = [int(i) for i in input().split()]

    while buffer and buffer[-1] <= arrival:
        buffer.pop()

    processing_start_time = -1
    if len(buffer) != size:
        if not buffer:
            processing_start_time = arrival
        else:
            processing_start_time = max(buffer[0], arrival)
        buffer.appendleft(processing_start_time + duration)

    print(processing_start_time)
