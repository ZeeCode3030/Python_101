def main():
    x = get_int("what is x?")
    print(f'x is {x}') # this is a literal


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # x = int(input('what is the x? '))
        except ValueError:
            print('x is not an integer')
            # pass
            # you can use pass rather than say anything to the user
        else: 
            break       
            
main()