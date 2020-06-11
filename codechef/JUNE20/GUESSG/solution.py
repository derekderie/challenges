def search(vals, asker):
    while True:

        if len(vals) < 4:
            for v in vals:
                s = asker.ask(v)
                if s == 'E':
                    return v

        m = len(vals)

        bound1 = m // 3
        bound2 = 2 * bound1

        s1 = asker.ask(vals[bound1])

        if s1 == 'E':
            return vals[bound1]

        s2 = asker.ask(vals[bound2])

        if s2 == 'E':
            return vals[bound2]
        elif s1 == 'L' and s2 == 'L':
            vals = vals[:bound2]
            continue
        elif s1 == 'G' and s2 == 'G':
            vals = vals[bound1 + 1:]
            continue

        s3 = asker.ask(vals[bound2])

        if s2 == 'L' and s3 == 'L':
            vals = vals[:bound2]
            continue
        elif s2 == 'G' and s3 == 'G':
            vals = vals[bound2 + 1:]
            continue

        s4 = asker.ask(vals[bound1])

        if s3 == 'L' and s4 == 'L':
            vals = vals[:bound2]
        elif s3 == 'G' and s4 == 'G':
            vals = vals[bound1 + 1:]
        else:
            vals = vals[:bound1] + vals[bound2 + 1:]


class Gamer:
    def ask(self, val):
        print(val)
        return input()


def main():
    n = int(input())
    search(list(range(1, n + 1)), Gamer())

# main()
