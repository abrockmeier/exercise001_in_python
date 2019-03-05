liste = [1,2,3]


print(liste)


print()


def times_list(n,list):
    for index, value in enumerate(list):
        list[index] = n * value
    return liste




liste2 = times_list(2,liste)


print(liste2)

