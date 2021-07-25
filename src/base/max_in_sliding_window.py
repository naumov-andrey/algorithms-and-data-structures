n = int(input())
data = [int(i) for i in input().split()]
m = int(input())

in_stack = data[:m]
in_max = max(in_stack)

out_stack = []
out_max = [-1]

print(in_max, end=' ')
for val in data[m:]:
    if len(in_stack) < m:
        in_max = max(val, in_max)
    else:
        in_max = val

        while in_stack:
            out_stack.append(in_stack.pop())
            out_max.append(max(out_stack[-1], out_max[-1]))

    in_stack.append(val)
    out_stack.pop()
    out_max.pop()
    print(max(in_max, out_max[-1]), end=' ')
