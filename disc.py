def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
    #
    #
    #
    #
    #
    #
    #
    #
    # #Correct Version
    # if is_leaf(t) and label(t) != x:
    #     return None
    # elif label(t) == x:
    #     return [label(t)]
    # else:
    #     for b in branches(t):
    #         if find_path(b, x):
    #             return [label(t)] +find_path(b, x)


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def minkk(s):
    uuu = list(map(abs, s))
    # return [i for i in range(len(uuu)) if uuu[i] == min(uuu)]
    return list(filter(lambda x: uuu[x] == min(uuu), range(len(uuu))))


def mmm(s):
    # return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    return max([a + b for a, b in zip(s[:-1], s[1:])])


def dict(s):
    # ans = {}
    # for ele in s:
    #     if ele % 10 not in ans:
    #         ans[ele % 10] = [ele]
    #     else:
    #         ans[ele % 10].append(ele)
    # return ans
    return {
        key: [ele for ele in s if ele % 10 == key]
        for key in range(10)
        if any([key == ele % 10 for ele in s])
    }


def equalall(s):
    # s = sorted(s)
    # return any([s[i] == s[i + 1] for i in range(len(s) - 1)])
    return all(
        map(
            lambda x: x > 1,
            [sum([1 for ele in s if s[i] == ele]) for i in range(len(s))],
        )
    )


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        assert isinstance(rest, Link) or rest is Link.empty
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"
lnk = Link(3, Link(4))
lnk2 = Link(2, Link(3, Link(4)))


def is_sorted(s, f):
    # while s is not Link.empty and s.rest is not Link.empty:
    #     if f(s.first) > f(s.rest.first):
    #         return False
    #     s = s.rest
    # return True
    if s is Link.empty or s.rest is Link.empty:
        return True
    else:
        return f(s.first) <= f(s.rest.first) and is_sorted(s.rest, f)


def merge(s, t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    else:
        l1 = s.first
        l2 = t.first
        return Link(min(l1, l2), Link(max(l1, l2), merge(s.rest, t.rest)))


def merge_iter(s, t):
    ans = Link(None)
    ptr = ans
    while s is not Link.empty and t is not Link.empty:
        ptr.rest = Link(min(t.first, s.first), Link(max(s.first, t.first)))
        ptr = ptr.rest.rest
        s, t = s.rest, t.rest
    if s is Link.empty:
        ptr.rest = t
    if t is Link.empty:
        ptr.rest = s
    return ans.rest
    # ans = Link.empty
    # ptr = ans
    # while s is not Link.empty and t is not Link.empty:
    #     if ans == Link.empty:
    #         ans = Link(min(t.first, s.first), Link(max(s.first, t.first)))
    #         ptr = ans
    #     else:
    #         ptr.rest = Link(min(t.first, s.first), Link(max(s.first, t.first)))
    #         ptr = ptr.rest.rest
    #         s, t = s.rest, t.rest
    # if s is Link.empty:
    #     ptr.rest = t
    # if t is Link.empty:
    #     ptr.rest = s
    # return ans




def merge_mutation(s, t):
    # if s is Link.empty:
    #     return t
    # elif t is Link.empty:
    #     return s
    # elif s.first <= t.first:
    #     s.rest = merge_mutation(s.rest, t)
    #     return s
    # else:
    #     t.rest = merge_mutation(s, t.rest)
    #     return t
    if s is Link.empty or t is Link.empty:
        return
    if s.first <= t.first:
        merge_mutation(s.rest, t)

