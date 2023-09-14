def longer_than_n(list,n):

    newlist = []

    for word in list:
        if len(word) > n:
            newlist.append(word)

    print(newlist)

longer_than_n(["hello","yes","no","food","chef"],4)