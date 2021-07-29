def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def sift_down(heap, i):
    min_ = i

    l = left_child(i)
    if l < len(heap) and heap[l] < heap[min_]:
        min_ = l

    r = right_child(i)
    if r < len(heap) and heap[r] < heap[min_]:
        min_ = r

    if min_ != i:
        heap[min_], heap[i] = heap[i], heap[min_]
        sift_down(heap, min_)


n, m = [int(i) for i in input().split()]
processor_release_times = [[0, i] for i in range(n)]
for t in [int(i) for i in input().split()]:
    print(*processor_release_times[0][::-1])
    processor_release_times[0][0] += t
    sift_down(processor_release_times, 0)
