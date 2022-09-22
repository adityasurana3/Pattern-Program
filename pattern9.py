# Print the following pattern

# A B C
# A B C
# A B C

n = int(input("Enter a number: "))
for i in range(n):
    ch = 65
    for j in range(n):
        print(chr(ch), " ", end='')
        ch = ch+1
    print("")
