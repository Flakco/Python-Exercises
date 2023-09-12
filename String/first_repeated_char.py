def first_repeated_char(str1):

    list = []

    for w in str1.lower():
        
        if w in list:
            return print(f"The first repeated character is: {w}")
        else:
            list.append(w)


first_repeated_char("The Time the time time the rust time")