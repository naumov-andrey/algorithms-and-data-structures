class Hash:
    def __init__(self, m, x, p):
        self.coef = [1]
        self.x = x
        self.p = p
        self.m = m

    def calculate(self, str_):
        hash_ = 0
        for i, char in enumerate(str_):
            if i == len(self.coef):
                self.coef.append(self.coef[-1] * self.x % self.p)
            hash_ += ord(char) * self.coef[i] % self.p
        return hash_ % self.p % self.m


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    hash_table = [[] for _ in range(m)]
    h = Hash(m, x=263, p=1_000_000_007)
    for _ in range(n):
        cmd = input().split()

        if cmd[0] == 'add':
            s = cmd[1]
            hash_ = h.calculate(s)
            if s not in hash_table[hash_]:
                hash_table[hash_].insert(0, s)

        elif cmd[0] == 'del':
            s = cmd[1]
            hash_ = h.calculate(s)
            if s in hash_table[hash_]:
                hash_table[hash_].remove(s)

        elif cmd[0] == 'find':
            s = cmd[1]
            if s in hash_table[h.calculate(s)]:
                print('yes')
            else:
                print('no')

        elif cmd[0] == 'check':
            print(' '.join(hash_table[int(cmd[1])]))
