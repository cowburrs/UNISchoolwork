def p(n):
    if n == 1:
        return 60
    if n == 2:
        return 54
    else:
        return 0.5 * p(n - 1) + 0.3 * p(n - 2)

# [print(p(x+1)) for x in range(10)]
print(p(6))
