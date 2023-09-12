def sum_digit_string(str1):

    sum = 0
    for l in str1:
        if l.isdigit():
            sum += int(l)

    print(sum)


sum_digit_string("23fd54345")