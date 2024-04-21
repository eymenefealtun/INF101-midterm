import main


def showItem(item, time=10):  # DEFAULT PARAMETER
    for i in range(time):
        print(f"This is the {item}")


showItem("eymen")


def statictics(nums):
    min = nums[0]
    max = nums[0]
    sum = 0
    for i in nums:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i

    return min, max, sum


myNumbers = [23, 53, 34, 562, 21, 12, 34, 2, 1, 1, 23, 313, 15, 135, -34, 2, 34, 12131]
print(statictics(myNumbers))
print(statictics(myNumbers)[0])
print(statictics(myNumbers)[1])
print(statictics(myNumbers)[2])

print("\n")
print("STRINGS")

myName = "Eymen Efe Altun"
print(myName.count("e", 4, len(myName)))
print(myName.replace(" ", ""))

nameList = myName.split(" ")
print(nameList)