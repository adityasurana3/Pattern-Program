# Print the following pattern

# 1
# 2 3
# 4 5 6

n = int(input("Enter a number: "))
count = 1
for i in range(n):
    for j in range(i):
        print(count, " ", end='')
        count = count+1
    print("")
