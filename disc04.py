def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # return sum([count_k(n - i, k) for i in range(1, k + 1)])
        ans = 0
        for i in range(1, k + 1):
            ans += count_k(n - i, k)
        return ans


# i = 1
# while i <=k:
#     result += count_k(n-i,k)
# return result

# else:
#        total = 0
#        i = 1
#        while i <= k:
#            total += count_k(n - i, k)
#            i += 1
#        return total
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        # ans = max(s)
        # tmp = 1
        # for i in range(len(s)):
        #     for j in range(2, len(s) + 1):
        #         for element in s[i::j]:
        #             tmp *= element
        #         ans = max(tmp, ans)
        #         tmp = 1
        # return ans
        return max(max_product(s[2:]) * s[len(s) - 1],max_product(s[1:]))
