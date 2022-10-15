def digit_replacer(predicate, transformer):
    def result(x):
        ans, count = 0, 0
        while x > 0:
            if predicate(x % 10) == True:
                ans = ans + transformer(x % 10) * pow(10, count)
            else:
                ans = ans + x % 10 * pow(10, count)
            count += 1
            x //= 10
        return ans

    return result


is_even = lambda d: d % 2 == 0
floor_divide_two = lambda d: d // 2
