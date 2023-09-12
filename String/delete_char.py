def delete_char(str1,char):

    newstr = ""

    for l in str1:
        if l == char:
            newstr += l.replace(l, "")
        else:
            newstr += l
    
    print(newstr)


delete_char("aconcagua","a")