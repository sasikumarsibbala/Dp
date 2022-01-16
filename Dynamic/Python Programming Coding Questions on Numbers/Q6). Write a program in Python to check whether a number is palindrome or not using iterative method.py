st = "sasi"


def palindrome_check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1]:
            return False
    return True


print(palindrome_check(st))
