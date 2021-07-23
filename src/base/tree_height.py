import sys
from typing import Dict, List


def calculate_height(node: int, parents: List, heights: Dict = {}):
    if parents[node] == -1:
        heights[node] = 1
    else:
        if parents[node] not in heights:
            calculate_height(parents[node], parents)
        heights[node] = 1 + heights[parents[node]]

    return heights[node]


sys.setrecursionlimit(10000)

n = int(input())
parents = [int(i) for i in input().split()]
print(max([calculate_height(node, parents) for node in range(n)]))
