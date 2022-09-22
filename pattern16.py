# Print the following pattern

#       *
#     * *
#   * * *
# * * * *

n = int(input("Enter a number: "))

for i in range(n):
    space = n-i
    for j in range(space):
        print(" ", end='')
        space = space-1
    for k in range(i+1):
        print("*", end='')
    print("")
