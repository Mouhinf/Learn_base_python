x = float(input())

term = x
sin_x = x
i = 1

while abs(term) > 1e-6:
    term *= -x * x / ((2 * i) * (2 * i + 1))
    sin_x += term
    i += 1

print(sin_x)

