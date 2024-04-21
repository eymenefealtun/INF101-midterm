import main

isDone = False

while isDone == False:
    break
    answer = input("Do you want to continue? (y/n): ")
    if answer == "y":
        print("hello")
    elif answer == "n":
        isDone = True

languages = ["eymen", "john", "ada", "patty"]

for i in languages:
    if i == "patty":
        print("patty has been found")
        break
    print("trial1")

print("\n")
print("TUPLES\n")

dimensions = (200, 323, 54)
a, b, c = dimensions
print(b)
dimensions = (43, 5, 65, 3, 345, 6, 34, 234,)  # you can assign a new value
main.show(dimensions)
#dimensions[2] = 123 THIS CAN NOT BE DONE IN TUPLES
print(dimensions[2])

print("\n")
print("DICTIONARIES\n")

students_grades = {"Eymen": 100, "John": 50, "Patty": 84}
students_grades["Xia"] = 23

students_grades.pop("Eymen")
del students_grades["John"]

for i in students_grades.keys():
    print(i)
for i in students_grades.values():
    print(i),

print("\n")

print(students_grades["Patty"])
print(type(students_grades.keys()))

# print(students_grades["Eymen"]) # this throws exception because Eymen does not exist in the dict
print(students_grades.get("Eymen"))  # if not found returns None unlike the [] using
print(students_grades.get("Eymen", "Eymen not found"))  # or give parameter for default result

students_grades["Azra"] = 23
students_grades["Yücel"] = 423
students_grades["Terim"] = 73

for key, value in students_grades.items():
    print(key, value)

print("\n")
print("SETS\n")  # each item is unique in sets

fruits = {"apple", "strawberry", "banana", "pineapple", "pineapple"}
fruits.add("deneme")
main.show(fruits)
for i in fruits:
    print(i)
