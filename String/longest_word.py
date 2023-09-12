def longest(list1):
    long = ""
    for word in list1:
        if len(word) > len(long):
            long = word

    print(f"Longest word: {long}")
    print(f"Length of the longest word: {len(long)}")
    
longest(["uno","dos","Exercises","World of the Travelers"])