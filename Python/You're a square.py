def is_square(n):
    if n < 0:
        return False
    return n**0.5 == int(n**0.5)