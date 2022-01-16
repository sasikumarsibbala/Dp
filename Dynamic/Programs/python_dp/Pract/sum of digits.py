def sum_of_digits(num):
    s = str(num)
    sum1 = 0
    for x in s:
        sum1 = sum1 + int(x)
    return sum1


print(sum_of_digits(12333333333333333333333993339333933939399393939393939399339939393939393939393993939393939399339339393))
