def last_two(str1):

    if len(str1) >= 2:
        newstr1 = str1[-2:]
        print(newstr1 * 4)
    else:
        raise ValueError("The string must have at least 2 characters")

last_two("Python")