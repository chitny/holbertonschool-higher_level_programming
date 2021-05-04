def replace_in_list(my_list, idx, element):
    largo = len(my_list)
    if idx in range(largo):
        my_list[idx] = element
        return my_list
    else:
        return
