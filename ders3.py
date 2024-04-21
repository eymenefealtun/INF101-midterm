def fact(num):
    value = 1
    for i in range(2, num + 1):
        value *= i
    print(value)


fact(9)

given_func = "+5x^4 -2x^2 +3x^1 -5x^0"

values = given_func.split(" ")
print(values)

result = ""
for value in values:
    number = int(value[0:2])
    power = int(value[-1])
    if power != 0:
        number *= power
        power -= 1
    else:
        number= 0

    if number >0:
        result += f"+{number}x^{power} "
    elif number<0:
        result += f"{number}x^{power} "
 


print(result)