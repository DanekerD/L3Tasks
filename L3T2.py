a = str(input("Type your name here: ")).title()
b = str(input("Type your second name here: ")).title()
c = str(input("type here your birth date: "))
d = str(input("Type here your city, where you live: "))
e = str(input("Type here your e-mail: "))
f = str(input("Type here your telephone number: "))


def my_fun(var_1=f"Name: {a}", var_2=f"Second Name: {b}", var_3=f"Birth date: {c}", var_4=f"City: {d}",
           var_5=f"E-mail: {e}", var_6=f"Telephone number {f}"):
    f_str = (var_1, var_2, var_3, var_4, var_5, var_6)
    return f_str


result = my_fun()
print(result)
