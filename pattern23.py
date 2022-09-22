# Print the following pattern

# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 * * 4 3 2 1
# 1 2 3 * * * * 3 2 1
# 1 2 * * * * * * 2 1
# 1 * * * * * * * * 1

n = int(input("Enter a number: "))

for i in range(1, n+1):
    count = n-i+1
    for j in range(1, count+1):
        print(j, " ", end='')

    star = i*2
    for k in range(2, star):
        print("*", " ", end='')

    count2 = n-i+1
    for l in range(1, count+1):
        print(count2, " ", end='')
        count2 = count2-1

    print("")
