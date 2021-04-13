print("There will be distinguished two maximum numbers and sum of them")
print("Please type the numbers in the column step-by-step")


def my_fun(arg_1, arg_2, arg_3):
    list_1 = [arg_1, arg_2, arg_3]
    n_1 = min(list_1)
    ind_1 = list_1.index(n_1)
    n_2 = list_1.pop(ind_1)
    result = sum(list_1)
    print(result)
    return result


my_fun(int(input()), int(input()), int(input()))
