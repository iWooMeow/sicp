def partitions(n, m):
    """Part postive n with max part m
    >>>partitions(5,1)
    1
    """
    # if n < 0 or m == 0:
    #     yield ""
    if n > 0 and m > 0:
        # With m
        if n == m:
            yield str(m)
            # for instance ,here str(m) is enough; The possibility of partition(n, m-1) is considered in the last line.
        for ans in partitions(n - m, m):
            yield str(m) + "+" + ans
        # Without m
        yield from partitions(n, m - 1)


# 1.Functional Abstraction and return values: return an iterator over the ans for ans in partitions
# 2.Arguments: n is the number to be partitioned, m is the maximum partition size


# The RV of a single yield statement in generator only focus on a single value not all of them as long as the RV in all yields are complete.
# The RV in regular function focus on all results


def partitionsNon(n, m):
    if n <= 0 or m <= 0:
        return []
    # elif n == 0:
    #     return [str(m)]
    else:
        if n == m:
            # With m         and Without m
            return [str(m)] + partitionsNon(n, m - 1)
        else:

            # With m
            return [
                str(m) + "+" + elem
                for elem in partitionsNon(n - m, m)
                # and Without m
            ] + partitionsNon(n, m - 1)


# Each return needs to be totally complete


# 1.Functional Abstration: Calculate all the partitions of n with the max part m
# 2.Arguments: n is the number to be partitioned, m is the maximum partition size
# 3.Return value: a list of different partitions combinations delimited by '+'


def count(n, m):
    if n < 0 or m <= 0:
        return 0
    elif n == 0:
        return 1
    else:
        ans = 0
        for i in reversed(range(1, m + 1)):
            ans += count(n - i, i)
        # if n == m:
        #     return 1 + ans
        # else:
        return ans


def enumArgs(args, cnt, start, end):
    if cnt == -1:
        print(args)
    else:
        for i in range(start, end):
            args[cnt] = i
            enumArgs(args, cnt - 1, i + 1, end)


# enum = lambda args, end: enumArgs(args, 0, 0, end)
def enum(end, K):
    args = [0 for _ in range(K)]
    enumArgs(args, K - 1, 0, end)


enum(7, 3)
