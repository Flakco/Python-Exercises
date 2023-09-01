def change(str1):
    
    if len(str1) >= 3 and str1[-3:]!="ing":
        str1 = str1 + "ing"
    elif len(str1) >= 3 and str1[-3:]=="ing":
        str1 = str1 + "ly"
    print(str1)

change("st")