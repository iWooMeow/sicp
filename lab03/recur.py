def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(1)
    if n == 1:
        return 1
    elif n % 2 == 1:
        return hailstone(n * 3 + 1)
    elif n % 2 == 0:
        return hailstone(n // 2)
