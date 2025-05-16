import sys

def state():
    
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
        search_val = ""
        
        for key, val in capital_cities.items():
            if val == arg:
                search_val = key
        
        if search_val == "":
            print("Unknown capital city")
            return
        
        for key,val in states.items():
            if search_val == val:
                print(key)
                return
        


if __name__ == "__main__":
    state()