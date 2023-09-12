def multi_line_list(str1):

    newstr = []

    for line in str1.split("\n"):
        newstr.append(line)

    print(newstr)
    print(str1)

multi_line_list("""This
is a
multiline
string.""")