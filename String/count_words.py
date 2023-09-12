def count_words(str1):

    words = str1.split()
    dic = {}

    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    print(dic)

count_words("time to get up in the morning and buy some coffe to drink")