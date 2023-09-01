def not_poor(str1):
    word1 = str1.find("not")
    word2 = str1.find("poor")

    if word1 < word2 and word1 > 0 and word2 > 0:
        str1 = str1.replace(str1[word1:(word2+4)], "good")
    print(str1)

not_poor('The lyrics is not that poor!')
not_poor('The lyrics is poor!')
