def smallest_largest(str1):

    newstr = str1.split(" ")
    small = ""
    largest = ""

    for word in newstr:
        if len(word) > len(largest):
            largest = word
        elif len(word) > 1 and len(word) < len(small):
            small = word

    print(f"Smallest word: {min(newstr, key=len)}\nLargest word: {largest}")


smallest_largest("Production of the best computer in a the world")