def lu(n):
    if n < 10:
        return n
    else:
        return luD(n // 10) + n % 10


def luD(n):
    luDigit = n % 10 * 2
    return lu(n // 10) + luDigit % 10 + luDigit // 10
