import sys

def lowercase_dict(my_dict):

    new_dict = {}
    for key,value in my_dict.items():
        new_dict[key.lower()] = value.lower()
    return new_dict


def handle_arg(args, flag):

    arg_list = args.split(",")
    arg_list = list(map(str.strip, arg_list))
    if flag == 1:
        arg_list = list(map(str.lower, arg_list))
    return arg_list


def find_capital(val_state, arg, capital_cities) -> int:
    
    for key,value in capital_cities.items():
        if val_state == key:
            print(f"{value.title()} is the capital city of {arg.title()}")
            return 1
    return 0


def find_capitals_state(capital_city, key_arg, states) -> int:
    
    for key,value in states.items():
        if key_arg == value:
            print(f"{capital_city.title()} is the capital of {key.title()}")
            return 1
    return 0


def check_match(arg_list, old_arg_list, states, capital_cities):
    
    for index, arg in enumerate(arg_list):
        flag = 0
        for key, value in states.items():
            if arg == key:
                flag = find_capital(value, arg, capital_cities)
        if flag == 0:
            for key, value in capital_cities.items():
                if arg == value:
                    flag = find_capitals_state(arg, key, states)
        if flag == 0 and arg != "":
            print(f"{old_arg_list[index]} is neither a capital city nor a state")


def all_in():

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) == 2:
        sys.argv.pop(0)
        states = lowercase_dict(states)
        capital_cities = lowercase_dict(capital_cities)
        lower_arg_list = handle_arg(str(sys.argv[0]), flag=1)
        original_arg_list = handle_arg(str(sys.argv[0]), flag=0)
        check_match(lower_arg_list, original_arg_list, states, capital_cities)


if __name__ == "__main__":
    all_in()