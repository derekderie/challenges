from JUNE20.GUESSG.solution import lie_answer, truthful_answer, search


class Truthful:
    def __init__(self, ans):
        self.ans = ans

    def ask(self, val):
        ans = truthful_answer(val, self.ans)
        print("asking ", val, "returning", ans)
        return ans


class LieEveryOther:
    def __init__(self, lie_on_start, ans):
        self.lie = lie_on_start
        self.ans = ans

    def ask(self, val):
        ans = lie_answer(val, self.ans) if self.lie else truthful_answer(val, self.ans)
        print("asking ", val, "returning", ans)
        self.lie = not self.lie
        return ans


def main():
    n = 20

    start_list = list(range(1, n + 1))

    if True:
        for k in range(1, 10):
            ans = k
            assert ans == search(start_list, Truthful(ans)), "Error with Truthful and ans=%d" % ans
            assert (ans == search(start_list, LieEveryOther(True, ans))), "Error with LEO-T and ans=%d" % ans
            assert (ans == search(start_list, LieEveryOther(False, ans))), "Error with LEO-F and ans=%d" % ans

    if True:
        ans = 5
        print("Ans: ", ans)
        print("Truthful", search(start_list, Truthful(ans)))
        print("LieEveryOther (True)", search(start_list, LieEveryOther(True, ans)))
        print("LieEveryOther (False)", search(start_list, LieEveryOther(False, ans)))

    # search(start_list, Gamer())


main()
