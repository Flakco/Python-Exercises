def vowel(str1):

    newstr = ""

    for l in str1:
        if l not in "AEIOUaeiou":
            newstr += f"-{l}-"
        else:
            newstr += l
            
    print(newstr)

vowel("Green")