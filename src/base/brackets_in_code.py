s = input()
brackets = []
open = ('(', '[', '{')
close = (')', ']', '}')
close_to_open = {close[i]: open[i] for i in range(len(open))}

for i, char in enumerate(s):
    if char in open:
        brackets.append((i, char))

    if char in close:
        if not brackets or brackets[-1][1] != close_to_open[char]:
            print(i + 1)
            break
        brackets.pop()

else:
    if brackets:
        print(brackets[0][0] + 1)
    else:
        print('Success')
