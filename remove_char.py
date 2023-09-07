def remove_char(str1, str2):

    newstr = [l for l in str1 if l not in str2]

    print("".join(newstr))

remove_char("hellto", "hell")