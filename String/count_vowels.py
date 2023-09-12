def count_vowels(str1):

    vowels = ["a","e","i","o","u"]
    count = 0
    for l in str1:
        if l in vowels:
            count += 1
    
    print(f"Contains {count} vowels.")


count_vowels("dbiqweojsndaa")

