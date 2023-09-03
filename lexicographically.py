def lex(str1):
    sorted_word = " ".join(sorted(str1, key=str.lower))
    sorted_word2 = sorted(str1)
    print(sorted_word)
    print(sorted_word2)

lex("running")