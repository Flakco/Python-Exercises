def remove_duplicate_words(str1):

    words = [l for l in str1.split(" ")]
    newstr = []

    for word in words:
        if word not in newstr:
            newstr.append(word)

    print(" ".join(newstr))


remove_duplicate_words("hello hello hello time to time to for time")
    