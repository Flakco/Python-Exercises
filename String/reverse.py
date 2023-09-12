def reverse(str1):
    if len(str1) % 4 == 0:
        print(str1[::-1])
    else:
        print(str1)

reverse("times to buy")