import main as main

print("welcome", "ola", "senıor")

# myInput = input()

# print("You have written: " + myInput)

print("\n")
myList = [23, 54, 3, 3, 5, 3, 21, 5, 23, 4, 23, 42, 4, 52, 5, 25, 235, 34, 3, 4]
myList.remove(3)  # removes the firs element
myList.pop(0)  # if no parameter given it removes last element
myList.append(2323232)
myList.sort()
main.show(myList)

print("\n")
stringList = ["qas", "par", "tek", "araba"]
main.show(stringList)
stringList.sort(reverse=True)
main.show(sorted(stringList))  # maintains original order
main.show(stringList)

print("\n")
cars = ["bmw", "audi", "merces", "toyota"]
main.show(cars)
cars.reverse()
main.show(cars)

print("\n")
myList1 = ["ola", "miamigo", "elma"]
myList2 = [23, 345, 3, 5, 2, 23, 423, 4]
resultList = myList2 + myList1
main.show(resultList)

print("\n")

list20 = [123, 54, 3, 1]
print(1 in list20)
if not list20:
    print("this is null")
if list20:
    print("this is not null")


print("\n")
course = "INF101X"
char1 = "X"
if char1 in course:
    print(f"There exist a {char1} in {course}")

