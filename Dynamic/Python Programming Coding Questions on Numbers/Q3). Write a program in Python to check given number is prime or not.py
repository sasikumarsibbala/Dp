n = 11
temp = 0
for i in (2, n // 2):
    if n % i == 0:
        temp = 1
        break
if temp == 1:
    print("no")
else:
    print("yes")
