def swap_cases(str1):

    newstr = ""
    for i in str1:
        if i == i.upper():
            newstr += i.lower()
        else:
            newstr += i.upper()

    print(newstr)
    
swap_cases("GHerer")