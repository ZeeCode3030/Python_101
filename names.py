names = []
name = input('what is your name? ')

file = open('names.txt', 'a') #opens the file to be written to 'w'/'a' for append
file.write(name) #Write the value of name into the names.txt file
