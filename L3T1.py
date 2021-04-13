"""Your Selected numbers will be divided like a / b"""

arg_1 = int(input("Select one number: "))
arg_2 = int(input("Select a second number: "))


try:
    def my_div(arg_1, arg_2):
        l_division = arg_1 / arg_2
        return l_division


    f_division = my_div(arg_1, arg_2)
    print(f"Your divisions result is equal to: {f_division}")
except ZeroDivisionError as err:
    print("Oops! Error!")
