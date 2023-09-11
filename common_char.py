def common_char(str1,str2):

    common = ""

    for l in str1:
        if l in str2:
            common += l

    if len(common) > 0:
        print(f"The string contains duplicates: {True}")
    else:
        print(f"The string don't contains duplicates: {False}")

    print(f"Common characters: {sorted(common)}")

common_char("w3source","python and swift")