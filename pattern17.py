# Print the following pattern

# * * * *
#   * * *
#     * *
#       *

n = int(input("Enter a number: "))

for i in range(1, n+1):
    space = i - 1
    for j in range(space):
        print(" ", end='')
        space = space + 1
    for k in range(n-i+1):
        print("*", end='')
    print("")
