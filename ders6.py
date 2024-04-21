def toplama(sayi1, sayi2):
    result = sayi1 + sayi2
    return result


işlem_sonucu = toplama(45, 31)
print(işlem_sonucu)

nums = [123, 3123, 234, 234, 345, 345]
print(nums)
print(nums[2:4])

for i in range(100):
    print(i)

number = 100
while number > 0:
    print("DENEME", number)
    number -= 1

number = True
while number:
    print("omerhaba")
    break

my_number = 0
while True:
    print(my_number)
    my_number+=1
    if my_number == 101:
        break