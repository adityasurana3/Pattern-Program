# Print the following pattern

# A
# B C
# C D E
# D E F G

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord('A')+i+j-2), " ", end='')
    print("")
