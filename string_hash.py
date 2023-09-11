def string_hash(str1):
    newstr = ""
    for word in str1.split(" "):
        if len(word) > 4:
            newstr += word.replace(word,"#"*len(word)) + " "
        else:
            newstr += word + " "

    print(newstr)

string_hash("Count the lowercase letters in the said list of words")