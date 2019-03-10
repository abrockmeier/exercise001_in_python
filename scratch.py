

def print_list_and_type(list_):
    print()
    print(list_)
    print("Type of (%s) is :" % list_)
    print(type(list_))
    print()


def times_list(n, list_):
    for index, value in enumerate(list_):
        list_[index] = n * value
    return list_


my_list = [1, 2, 3]
my_list2 = times_list(2, [1, 2, 3])
my_list3 = times_list(3, [1, 2, 3])

# Wrong output on first and last List-Element!
lists_of_lists = [my_list, my_list2, my_list3]

print_list_and_type(my_list)
print_list_and_type(my_list2)
print_list_and_type(my_list3)
print_list_and_type(lists_of_lists)

