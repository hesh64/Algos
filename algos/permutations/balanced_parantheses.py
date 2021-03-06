from collections import deque


def balances(n):
    if n == 1:
        return ['()']

    p = balances(n - 1)
    n = []
    for v in p:
        n.append('(' + v + ')')
        if '()' + v != v + '()':
            n.append('()' + v)
            n.append(v + '()')
        else:
            n.append('()' + v)

    return n


class Pran:
    def __init__(self, str, l, r):
        self.str = str
        self.l = l
        self.r = r

    def copy(self):
        return Pran(str(self.str), int(self.l), int(self.r))

    def __repr__(self):
        return self.str + f' - ({self.l},{self.r})'


def balance(n):
    results = []
    q = deque()
    q.append(Pran('', 0, 0))
    while q:
        cur = q.popleft()
        print(506)
        print(cur)
        if cur.l == n and cur.r == n:
            print(cur)
            results.append(cur.str)
        else:
            if cur.l < n:
                q.append(Pran(cur.str + '(', cur.l + 1, cur.r))

            if cur.l > cur.r:
                q.append(Pran(cur.str + ')', cur.l, cur.r + 1))

    return results


def main():
    n = 2
    # result = balance(n)
    # print(result)

    n = 3
    result = balance(n)
    print(result)


main()
