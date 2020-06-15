from codechef.JUNE20.GUESSG.solution import search, SearchSpace


def truthful_answer(val, ans):
    if ans == val:
        return 'E'
    elif ans < val:
        return 'L'
    else:
        return 'G'


def lie_answer(val, ans):
    if ans == val:
        return 'E'
    elif ans < val:
        return 'G'
    else:
        return 'L'


class Asker:
    def __init__(self, ans, verbose=False):
        self.ans = ans
        self.verbose = verbose
        self.ask_count = 0

    def ask(self, val):
        self.ask_count += 1


class Truthful(Asker):

    def ask(self, val):
        super().ask(val)
        ans = truthful_answer(val, self.ans)
        if self.verbose:
            print("asking ", val, "returning", ans)
        return ans


class LieEveryOther(Asker):
    def __init__(self, lie_on_start, ans):
        self.lie = lie_on_start
        super().__init__(ans)

    def ask(self, val):
        ans = lie_answer(val, self.ans) if self.lie else truthful_answer(val, self.ans)
        if self.verbose:
            print("asking ", val, "returning", ans)
        self.lie = not self.lie

        super().ask(val)
        return ans


class MightLie(Asker):
    def __init__(self, frac, ans):
        self.did_lie = False
        self.frac = frac
        super().__init__(ans)

    def ask(self, val):
        if self.did_lie:
            self.did_lie = False
            ans = truthful_answer(val, self.ans)
        elif random.random() < self.frac:
            self.did_lie = True
            ans = lie_answer(val, self.ans)
        else:
            ans = truthful_answer(val, self.ans)

        super().ask(val)
        return ans


def main():
    n = 10 ** 9

    # start_list = list(range(1, n + 1))
    start_space = SearchSpace([(1, n)])

    # for k in range(1, 10):
    #     ans = k
    #     assert ans == search(start_list, Truthful(ans)), "Error with Truthful and ans=%d" % ans
    #     assert (ans == search(start_list, LieEveryOther(True, ans))), "Error with LEO-T and ans=%d" % ans
    #     assert (ans == search(start_list, LieEveryOther(False, ans))), "Error with LEO-F and ans=%d" % ans

    ans = 5
    # print("Ans: ", ans)
    # print("Truthful", search(start_space, Truthful(ans)))
    # print("LieEveryOther (True)", search(start_space, LieEveryOther(True, ans)))
    # print("LieEveryOther (False)", search(start_space, LieEveryOther(False, ans)))

    # search(start_list, Gamer())

    do_sampling_experiment()


import random


def do_sampling_experiment():
    n = 10 ** 9

    # start_list = list(range(1, n + 1))
    search_space = SearchSpace([(1, n)])

    make_askers = [lambda ans: Truthful(ans),
                   lambda ans: LieEveryOther(True, ans),
                   lambda ans: LieEveryOther(False, ans),
                   lambda ans: MightLie(0.5, ans)]

    for k in range(20000):
        ans = random.randint(1, n)
        for make_asker in make_askers:
            asker = make_asker(ans)
            assert ans == search(search_space, asker), "Error with %s" % asker
            print(f"Found {ans} with {asker} in {asker.ask_count} steps")

    print("Everything went okay")


main()
