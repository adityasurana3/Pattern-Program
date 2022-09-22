# Print the following pattern

# A B C
# B C D
# C D E

# n = int(input("Enter a number: "))
# ch = 65
# # print(ch)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+j+ch-2)," ",end='')
#     print(" ")

# 2nd Method
n = int(input("Enter a number: "))

for i in range(n):
    start = chr(ord('A')+i)
    for j in range(0, n):
        print(start, " ", end='')
        start = chr(ord(start)+1)
    print("")
