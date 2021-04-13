def my_func(x, y):
    result = x ** y

    if result > 1:
        print("Choose other negative number")

    elif result < 1:
        print(result)


my_func(float(input("Insert the base number: ")), int(input("Insert the negative power number: ")))
