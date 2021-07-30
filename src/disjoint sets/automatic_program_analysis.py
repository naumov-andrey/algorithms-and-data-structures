def find(parent, i):
    if i != parent[i]:
        parent[i] = find(parent, parent[i])
    return parent[i]


is_possible = True

n, e, d = [int(i) for i in input().split()]
parent = list(range(n))
rank = [0 for _ in range(n)]

for _ in range(e):
    i_id, j_id = [find(parent, int(i) - 1) for i in input().split()]
    if i_id != j_id:
        if rank[i_id] < rank[j_id]:
            parent[i_id] = j_id
        else:
            if rank[i_id] == rank[j_id]:
                rank[i_id] += 1
            parent[j_id] = i_id

for _ in range(d):
    i_id, j_id = [find(parent, int(i) - 1) for i in input().split()]
    if i_id == j_id:
        is_possible = False
        break

print(int(is_possible))
