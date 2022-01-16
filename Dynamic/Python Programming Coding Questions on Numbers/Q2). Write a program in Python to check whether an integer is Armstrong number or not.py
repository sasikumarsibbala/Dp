n = 153
# armstrong number is addition of cube of each digit is equal to number
output = 0
for i in str(n):
    num = int(i)
    output = output + (num * num * num)
print(output == n)

