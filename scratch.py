liste = [1,2,3]
liste_original = [1,2,3]

print(liste)


def times_list(n, list):
    for index, value in enumerate(list):
        list[index] = n * value
    return liste


liste = times_list(2, liste)


print()
print(liste)

# Wrong output on first and last List-Element!
listsOFlists = [liste_original], [liste], [times_list(2,liste_original)]

print()
print(listsOFlists)