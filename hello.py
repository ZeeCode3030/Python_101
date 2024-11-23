def main():
    name = input("What's your name? ")
    hello(name)
# remove whitespace
# name = name.strip().title()
'''
name= name.strip().capitalize()
if name.find(" "):
    first, last = name.split(" ")
    print ("hello,", first, last )
else: 
    print ("hello,", name)
'''
# say hello to the user
# you can use /" or backspace in front of anything in the print function to exempt

def hello (to="everyone"):
    '''if to.find() > -1:
        first, last = to.split(" ")
        to = print ("hello",first, last )
    else: 
        print ("hello,", to)'''
    print('hello,', to)
    return to


# PYTHON NEEDS YOUR FUNCTION TO BE DEFINED BEFORE/ABOVE YOUR USE OF IT
# use def main() to help that

main()
        

