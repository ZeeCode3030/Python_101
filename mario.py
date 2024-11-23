def main():
    number = int(input('What is size? '))
    print_square(number)

def print_square (size):
    #for each row in square 
    for _ in range(size):
        print('#' * size)


def print_row(size):
    for _ in range(size):
        print('#' * size)


main()
