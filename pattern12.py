# Print the following pattern

# A
# B B
# C C C

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(i+ord('A')-1), " ", end="")
    print(" ")
