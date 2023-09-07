import difflib

def sequence_matcher(str1, str2):

    result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    print(result.ratio())

sequence_matcher("Python Exercises","Python Exercise")