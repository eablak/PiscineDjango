class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return(self.Coffee())


if __name__ == "__main__":
    i1 = Intern()
    i2 = Intern("Mark")

    print(i1.__str__())
    # print(i1)
    print(i2.__str__())
    print(i2.make_coffee())
    try:
        i1.work()
    except Exception as e:
        print(e)