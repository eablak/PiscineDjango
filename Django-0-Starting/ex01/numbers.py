def print_numbers():
    f = open("numbers.txt")
    numbers = f.read()
    numbers = numbers.split(",")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    print_numbers()