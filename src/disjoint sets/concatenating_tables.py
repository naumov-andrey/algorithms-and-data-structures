def find(parent, i):
    if i != parent[i]:
        parent[i] = find(parent, parent[i])
    return parent[i]


n, m = [int(i) for i in input().split()]
table_parent = [i for i in range(n)]
table_columns = [int(i) for i in input().split()]
max_columns = max(table_columns)

for _ in range(m):
    dst_id, src_id = [find(table_parent, int(i) - 1) for i in input().split()]
    if dst_id != src_id:
        table_parent[src_id] = dst_id

        table_columns[dst_id] += table_columns[src_id]
        table_columns[src_id] = 0
        max_columns = max(max_columns, table_columns[dst_id])

    print(max_columns)
