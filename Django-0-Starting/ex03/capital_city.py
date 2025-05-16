import sys

def capital_city():

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
        arg = sys.argv[1]
        if arg in states:
            val = states[arg]
            print(capital_cities[val])
        else:
            print("Unknown state")


if __name__ == "__main__":
    capital_city()