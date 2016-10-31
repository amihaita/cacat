def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True

    return total
print(for_version([0,2,6,81,15,7,8,4,12,14,21,16]))