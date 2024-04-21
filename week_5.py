import main


# RECURSIVE FUNCTIONS

def fact(num):
    value = 1
    for i in range(2, num + 1):
        value *= i
    print(value)


fact(4)


def rec_fac(num):
    if num == 1:
        return num
    return num * rec_fac(num - 1)


print(rec_fac(4))


def is_palindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


print("palindrome",is_palindrome("efe"))

name = "eymen"
print(name[1:-1])
reverse_name = ""
for i in range(len(name)):
    reverse_name += name[-(i + 1)]
print(reverse_name)
