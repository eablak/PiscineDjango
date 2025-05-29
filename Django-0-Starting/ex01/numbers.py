def print_numbers():

    try:
        f = open("numbers.txt")
    except FileNotFoundError:
        raise FileNotFoundError("File not Found!")
    
    numbers = f.read().split(",")
    
    for num in numbers:
        print(num)


if __name__ == "__main__":
    print_numbers()