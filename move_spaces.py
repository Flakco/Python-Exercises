def move_spaces(str1):
    newstr = "" 
    char = ""
    for move in str1:
        if move == " ":
            move.replace(" ","")
            newstr += move
        else:
            char += move

    print(newstr+char)

move_spaces(" THE TIME TO G R A SP ")
                    
