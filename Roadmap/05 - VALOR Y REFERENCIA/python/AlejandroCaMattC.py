"""Value and reference in Python"""

# Types of data per value
my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Types of data per reference

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Functions with data per value

my_int_c = 10


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_func(my_int_c)
print(my_int_c)

# Functions with data per reference

my_list_c = [10, 20]


def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)

    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list_e)
    print(my_list_d)


my_list_func(my_list_c)
print(my_list_c)
