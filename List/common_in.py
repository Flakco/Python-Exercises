def common_in(list1,list2):

    for word in list1:
        if word in list2:
            return True


print(common_in(["no","yes","food"],["one","good","time","yes"]))