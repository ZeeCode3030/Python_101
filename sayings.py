def main():
    name = input('what is your name?')
    hello(name)
    goodbye()


def goodbye():
    print("goodbye!")

def hello(name):
    print ("Hello", name)

if __name__ == "__main__":
    main()

