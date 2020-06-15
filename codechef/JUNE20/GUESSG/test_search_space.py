from codechef.JUNE20.GUESSG.solution import SearchSpace


def test_search_space():
    ss = SearchSpace(10)
    print(ss.ranges)

    ss.ranges = [(1, 10), (15, 20), (50, 55)]
    print(ss.get_thirds())
    

test_search_space()
