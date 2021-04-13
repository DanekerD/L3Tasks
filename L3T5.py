def my_fun():
    s = 0
    while True:
        in_list = input("Type numbers or if you want to cancel operation type 'q': ").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("to exit the program, enter - 'q'.")
        print(f"Sum of numbers = {s}")


print(my_fun())