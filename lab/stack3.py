def factorial(n, depth=0):
    print("  " * depth + f"push factorial({n})")
    r = 1 if n <= 1 else n * factorial(n - 1, depth + 1)
    print("  " * depth + f"pop  factorial({n}) = {r}")
    return r


print("3) factorial(4):")
factorial(4)