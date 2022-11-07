 def helper(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)

# Alternate solution 1
def pingpong_next(x, i, step):
    if i == n:
        return x
    return pingpong_next(x + step, i + 1, next_dir(step, i+1))

def next_dir(step, i):
    if i % 8 == 0 or num_eights(i) > 0:
        return -step
    return step

# Alternate solution 2
def pingpong_alt(n):
    if n <= 8:
        return n
    return direction(n) + pingpong_alt(n-1)

def direction(n):
    if n < 8:
        return 1
    if (n-1) % 8 == 0 or num_eights(n-1) > 0:
        return -1 * direction(n-1)
    return direction(n-1)
