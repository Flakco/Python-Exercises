def replace(str1):

    newstr1 = str1.maketrans
    newstr = str1.translate(newstr1(",.",".,"))
    print(newstr)

replace("23423,354,768.68")