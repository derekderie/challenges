def search(search_space, asker):
    while True:

        if search_space.length() < 4:
            for v in search_space.get_flat_values():
                s = asker.ask(v)
                if s == 'E':
                    return v

        bound1, bound2 = search_space.get_thirds()

        s1 = asker.ask(bound1)

        if s1 == 'E':
            return bound1

        s2 = asker.ask(bound2)

        if s2 == 'E':
            return bound2
        elif s1 == 'L' and s2 == 'L':
            search_space = search_space.get_up_to_value(bound2)
            continue
        elif s1 == 'G' and s2 == 'G':
            search_space = search_space.get_over_value(bound1)
            continue

        s3 = asker.ask(bound2)

        if s2 == 'L' and s3 == 'L':
            search_space = search_space.get_up_to_value(bound2)
            continue
        elif s2 == 'G' and s3 == 'G':
            search_space = search_space.get_over_value(bound2)
            continue

        s4 = asker.ask(bound1)

        if s3 == 'L' and s4 == 'L':
            search_space = search_space.get_up_to_value(bound2)
        elif s3 == 'G' and s4 == 'G':
            search_space = search_space.get_over_value(bound1)
        else:
            search_space = search_space.get_split(bound1, bound2)


class Gamer:
    def ask(self, val):
        print(val)
        return input()


class SearchSpace:
    def __init__(self, ranges):
        self.ranges = ranges

    def length(self):
        return sum(1 + (b - a) for a, b in self.ranges)

    def get_flat_values(self):
        ans = []
        for a, b in self.ranges:
            ans += list(range(a, b + 1))
        return ans

    def get_thirds(self):
        total_length = self.length()
        b1 = total_length // 3
        b2 = 2 * b1

        bound1, bound2 = None, None

        so_far = 0
        for a, b in self.ranges:
            if so_far + 1 + (b - a) >= b1:
                bound1 = a + (b1 - so_far)
                break
            else:
                so_far += 1 + (b - a)

        so_far = 0
        for a, b in self.ranges:
            if so_far + 1 + (b - a) >= b2:
                bound2 = a + (b2 - so_far)
                break
            else:
                so_far += 1 + (b - a)

        return bound1, bound2

    def get_up_to_value(self, val):
        return SearchSpace([(a, min(b, val - 1)) for (a, b) in self.ranges if a < val])

    def get_over_value(self, val):
        return SearchSpace([(max(a, val + 1), b) for (a, b) in self.ranges if b > val])

    def get_split(self, bound1, bound2):
        up_to = [(a, min(b, bound1 - 1)) for (a, b) in self.ranges if a < bound1]
        over = [(max(a, bound2 + 1), b) for (a, b) in self.ranges if b > bound2]
        return SearchSpace(up_to + over)


def main():
    n = int(input())
    search(SearchSpace([(1, n)]), Gamer())

# main()
