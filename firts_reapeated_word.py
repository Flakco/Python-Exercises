def first_repeated_word(str1):

    list = []

    for w in str1.lower().split(" "):
        
        if w in list:
            return print(f"The first repeated word is: {w}")
        else:
            list.append(w)


first_repeated_word("The Time Time the time time the rust time")