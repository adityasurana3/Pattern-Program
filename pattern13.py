# Print the following pattern

# A
# B C
# D E F

n = int(input("Enter a number: "))
count = 'A'
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count, ' ', end='')
        count = chr(ord(count)+1)
    print("")
