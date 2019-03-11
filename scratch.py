import numpy as np


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


def print_np_object_properties(np_array):
    print("LISTING FOR numpy OBJECT:")
    print("Data-type of Array:")
    print(np_array.dtype)
    print("Data-type size of an item: (byte)")
    print(np_array.itemsize)
    print("Total number of elements in the array:")
    print(np_array.size)


my_list = [1, 2, 3]
my_list2 = times_list(2, [1, 2, 3])
my_list3 = times_list(3, [1, 2, 3])

lists_of_lists = [my_list, my_list2, my_list3]

print_list_and_type(my_list)
print_list_and_type(my_list2)
print_list_and_type(my_list3)
print_list_and_type(lists_of_lists)

yet_another_list_of_lists = [(times_list(1, my_list)), (times_list(1, my_list2)), (times_list(1, my_list3))]
print_list_and_type(yet_another_list_of_lists)

# for more flexibility from now on using numpy:

np_array_from_list_of_lists = np.array(lists_of_lists)
print_np_object_properties(np_array_from_list_of_lists)

np_array_3d = np.arange(24).reshape(2,3,4)
print(np_array_3d)
print
print_list_and_type(np_array_3d)
np_array_3d_2 = np_array_3d*2
print(np_array_3d_2)
print()
print_list_and_type(np_array_3d_2)