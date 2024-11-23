'''
x = int(input ("What is x?"))
y = int(input ("What is y?"))
x = float(input ("What is x?"))
y = float(input ("What is y?"))
z = round(x + y)

'''
# int is necessary to convert the x or y which are strings to integers
'''
x = input ("What is x?")
y = input ("What is y?")
z = x + y
print (z)
'''
'''
# print (f{z:,}) : this is a format string 
x = float(input ("What is x?"))
y = float(input ("What is y?"))

z = x / y
print ( f"{z:.2f}") #.2f is specifying the decimal
'''

def main():
    no = int(input('Square a number '))
    square(no)

def square(num):
    print(num * num)


if __name__ == '__main__':
    main()