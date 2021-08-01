from random import randint
from collections import deque


def calculate_hash(s, coef, p):
    h = 0
    for i, char in enumerate(s):
        h += ord(char) * coef[i] % p
    return h % p


def recalculate_hash(hash, new_char, deleted_char, coef, p):
    return ((hash - ord(deleted_char) * coef[-1]) * coef[1] + ord(new_char)) % p


if __name__ == '__main__':
    p = 1_000_000_007
    x = randint(1, p - 1)

    pattern = deque(input())
    text = input()

    if len(pattern) == 1:
        pattern = pattern[0]
        print(' '.join([str(i) for i, char in enumerate(text) if char == pattern]))
    else:
        coef = [pow(x, i, p) for i in range(len(pattern))]
        entries = []
        m = len(pattern)

        pattern_hash = calculate_hash(pattern, coef, p)
        window = deque(text[-m:])
        current_hash = calculate_hash(window, coef, p)

        if current_hash == pattern_hash and window == pattern:
            entries.append(len(text) - m)

        for i in range(len(text) - m - 1, -1, -1):
            current_hash = recalculate_hash(current_hash, text[i], text[i + m], coef, p)
            window.pop()
            window.appendleft(text[i])
            if current_hash == pattern_hash and window == pattern:
                entries.append(i)

        print(' '.join([str(i) for i in entries[::-1]]))
