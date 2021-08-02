class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: Node):
    if root.left:
        in_order_traversal(root.left)
    print(root.val, end=' ')
    if root.right:
        in_order_traversal(root.right)


def pre_order_traversal(root: Node):
    print(root.val, end=' ')
    if root.left:
        pre_order_traversal(root.left)
    if root.right:
        pre_order_traversal(root.right)


def post_order_traversal(root: Node):
    if root.left:
        post_order_traversal(root.left)
    if root.right:
        post_order_traversal(root.right)
    print(root.val, end=' ')


if __name__ == '__main__':
    n = int(input())
    nodes = [Node(*[int(i) for i in input().split()]) for _ in range(n)]
    for node in nodes:
        node.left = None if node.left == -1 else nodes[node.left]
        node.right = None if node.right == -1 else nodes[node.right]

    root = nodes[0]
    in_order_traversal(root)
    print()

    pre_order_traversal(root)
    print()

    post_order_traversal(root)
    print()
