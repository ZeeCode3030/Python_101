'''i = 0

while i  < 3:
    print ("meow")
    i = i + 1

# for i in [0,1,2]: #will automatically increment i
for i in range(3): 
    print ("bark")

print ("meow\n" * 3, end="") # another way to make meow 3 times
# other languages do not have this

while True:
    n = input( "What is n?")
    if n > 0:
        break

for _ in range(n):
    print("moo")
'''
def main():
    no = ask()
    for _ in range (no):
        print("moo")

def ask ():
    while True: 
        n = int(input ("What is n? "))
        if n > 0: 
            break
    return n

main()