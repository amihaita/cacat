def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1
    return total
print(while_version([0,2,6,81,15,7,8,4,12,14,21,16]))