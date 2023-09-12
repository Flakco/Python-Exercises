def replace(str1 , str2):
    newstr1 = str2[:2] + str1[2:]
    newstr2 = str1[:2] + str2[2:]
    print(f"{newstr1} {newstr2}")


replace("abc","xyz")
replace("1234","5678")