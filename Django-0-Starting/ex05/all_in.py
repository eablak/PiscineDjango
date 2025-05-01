import sys

def lowercase_dict(my_dict):

    new_dict = {}
    for key,value in my_dict.items():
        new_dict[key.lower()] = value.lower()
    return new_dict



def handle_arg(args):

    for arg in args:
        print(arg)


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
        handle_arg(sys.argv)


if __name__ == "__main__":
    all_in()