def custom_filter(some_list: list) -> bool:
    summa = 0
    for i in some_list:
        if type(i) == int and i % 7 == 0:
            summa += i
    return summa <= 83
print(custom_filter([7, 14, 28, 32, 32, 56]))