import sys


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def is_BST(node: Node, left_border=None, right_border=None):
    if not node:
        return True

    if left_border and node.key <= left_border:
        return False
    if right_border and node.key >= right_border:
        return False

    return is_BST(node.left, left_border, node.key) and is_BST(node.right, node.key, right_border)


if __name__ == '__main__':
    sys.setrecursionlimit(1_000_000)

    n = int(input())
    nodes = [Node(*[int(i) for i in input().split()]) for _ in range(n)]
    for node in nodes:
        node.left = None if node.left == -1 else nodes[node.left]
        node.right = None if node.right == -1 else nodes[node.right]

    root = nodes[0] if len(nodes) > 0 else None
    print('CORRECT' if is_BST(root) else 'INCORRECT')
