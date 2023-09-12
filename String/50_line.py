import textwrap 

def line_50(str1):
    print("\n".join(textwrap.wrap(str1, 50 ,break_long_words=False)))
    print(textwrap.fill(str1, 50 ,break_long_words=False))

line_50("Time to run for the eternity and grasp wisdom for the soul")