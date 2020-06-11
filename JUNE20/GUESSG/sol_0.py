# cook your dish here

def ask(x):
    print(x)
    return input()


def search(lower, upper):
    bound1 = lower + ((upper - lower) // 3)
    bound2 = lower + (2 * ((upper - lower) // 3))

    s1 = ask(bound1)

    if s1 == 'E':
        return

    s2 = ask(bound2)

    if s2 == 'E':
        return

    if s1 == 'L' and s2 == 'L':
        return search(lower, bound2)
    elif s1 == 'G' and s2 == 'G':
        return search(bound1, upper)
    elif s1 == 'G' and s2 == 'L':
        return search(lower, bound2)
    else:


# split in two domains, but check which one first!


def main():
    search(1, int(input()))


main()