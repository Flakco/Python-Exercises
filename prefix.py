import textwrap
def prefix(str1):
        print(textwrap.indent(str1, prefix="*"))


prefix('''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    ''')

