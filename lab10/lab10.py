def even_subset(link):
    if link == Link.empty:
        return []
    elif link.first % 2 == 0:
        ans = []
        for l in even_subset(link.rest):
            l.insert(0, link.first)
            ans.append(l)
        return ans + even_subset(link.rest) + [[link.first]]
    else:
        ans = []
        for l in odd_subset(link.rest):
            l.insert(0, link.first)
            ans.append(l)
        return ans + even_subset(link.rest)


def odd_subset(link):
    if link == Link.empty:
        return []
    elif link.first % 2 == 1:
        ans = []
        for l in even_subset(link.rest):
            l.insert(0, link.first)
            ans.append(l)
        return ans + odd_subset(link.rest) + [[link.first]]
    else:
        ans = []
        for l in odd_subset(link.rest):
            l.insert(0, link.first)
            ans.append(l)
        return ans + odd_subset(link.rest)


class Link:
    empty = []

    def __init__(self, first, rest=[]):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest == Link.empty:
            return "Link(" + str(self.first) + ")"

        else:
            return "Link(" + str(self.first) + ", " + repr(self.rest) + ")"


a = Link(3, Link(5, Link(8)))
print(repr(a))
print(even_subset(a))
