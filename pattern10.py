# Print the following pattern

# A B C
# D E F
# G H I

n = int(input("Enter a number: "))
ch = 65
for i in range(n):
    for j in range(n):
        print(chr(ch), " ", end='')
        ch = ch+1
    print("")
