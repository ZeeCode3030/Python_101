# sys is the way to use command line arguments
import sys

'''try:
    print('hello, my name is', sys.argv[1])
except IndexError:
    print('too many arguments')'''

if len(sys.argv) < 2:
    print("too few arguments")
    # sys.exit can just exit the program 
elif len(sys.argv) > 3:
    print ('too many arguments')
else:
    for arg in sys.argv[1:]:
        print('hello my name is ', arg)