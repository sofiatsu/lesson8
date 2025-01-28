def add_one(some_list):
    string = ''
    for num in some_list:
        string += str(num)
    number = str(int(string) + 1)
    my_lst = []
    for lst in number:
        my_lst.append(int(lst))
    return my_lst

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")