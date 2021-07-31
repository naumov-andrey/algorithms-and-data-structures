if __name__ == '__main__':
    n = int(input())
    name_for_number = {}
    for _ in range(n):
        cmd = input().split()

        if cmd[0] == 'add':
            number, name = cmd[1:]
            name_for_number[number] = name

        elif cmd[0] == 'del':
            number = cmd[1]
            if number in name_for_number:
                name_for_number.pop(number)

        elif cmd[0] == 'find':
            number = cmd[1]
            if number in name_for_number:
                print(name_for_number[number])
            else:
                print('not found')
