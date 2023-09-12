import textwrap

def identation_first(str1):

    str2 =  textwrap.dedent(str1).strip()
    print(textwrap.fill(str2,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))

identation_first('''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    ''')