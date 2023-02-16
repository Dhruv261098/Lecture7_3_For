my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_distionary = {"key1": "1", "key2": "2", "key3": "3"}


for list in my_list:
    print(list)

for tuple in my_tuple:
    print(tuple)

for set in my_set:
    print(set)

for dictionary in my_distionary:
    print(dictionary)

for key, value in my_distionary.items():  # to print key and value both for dictionary
    print(key)
    print(value)

