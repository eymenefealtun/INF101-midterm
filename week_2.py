import main

myList = range(1, 201)  # from 1 to 200
myList2 = range(0, 201, 2)  # from 0 to 200 two by two

main.show(myList)
main.show(myList2)

letters = ["a", "b", "c", "d", "e"]
main.show(letters)
copyLetters = letters[2:4]  # including 2 except 4

main.show(copyLetters)

name = "Eymen Efe Altun"
print(name[2:7])  # men E
