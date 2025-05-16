def my_var():
    variable = 42
    text = "has a type "
    fr_text = "quarante-deux"
    dict_var = {variable: variable}
    tuple_var = (variable,)
    print(f"{variable} {text} {type(variable)}")
    print(f"{variable} {text} {type(str(variable))}")
    print(f"{fr_text} {text} {type(str(variable))}")
    print(f"{float(variable)} {text} {type(float(variable))}")
    print(f"{bool(variable)} {text} {type(bool(variable))}")
    print(f"{[variable]} {text} {type([variable])}")
    print(f"{dict_var} {text} {type(dict_var)}")
    print(f"{tuple_var} {text} {type(tuple_var)}")
    print(f"{set()} {text} {type(set())}")

if __name__ == '__main__':
    my_var()