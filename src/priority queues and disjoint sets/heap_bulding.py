def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def sift_down(heap, i, log):
    min_ = i

    l = left_child(i)
    if l < len(heap) and heap[l] < heap[min_]:
        min_ = l

    r = right_child(i)
    if r < len(heap) and heap[r] < heap[min_]:
        min_ = r

    if min_ != i:
        log.append((i, min_))

        heap[min_], heap[i] = heap[i], heap[min_]
        sift_down(heap, min_, log)


def build_heap(array):
    log = []

    for i in range(len(array) // 2, -1, -1):
        sift_down(array, i, log)

    print(len(log))
    for record in log:
        print(record[0], record[1])


n = int(input())
build_heap([int(i) for i in input().split()])
