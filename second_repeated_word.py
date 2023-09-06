def second_repeated_word(str1):
    dic = {}
    repeated = []

    for word in str1.lower().split(" "):
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    for value, key in dic.items():
        if key > 1:
            repeated.append(value)
 
    #print(dic)
    #print(repeated)
    print(f"The second most repeated word is: {repeated[1]}")
 
second_repeated_word("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster.")