def filter_list(lst, num):
    new_lst = lst.copy()
    if num == 0:
        for number in new_lst:
            if number % 2 == 0:
                lst.remove(son)
                return lst
            else:
                for son in new_lst:
                    if son % 2 == 0:
                        lst.remove(son)

                    return lst
print(filter_list([1, 2, 3, 4, 5, 6], 0))
# print(filter_list([3, 5, 3, 6], 1))