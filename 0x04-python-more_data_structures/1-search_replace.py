#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = (list(map((replace if search in my_list else search), i)) for i in my_list)
    return my_list

ls = [1,2,3,45,5,6,7,8,9,12]
nw = search_replace(ls, 2, 89)
print(nw)
# print(ls)