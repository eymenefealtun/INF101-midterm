def show(givenList):
    givenList = list(givenList)
    myString = ""
    for i in range(len(givenList)):
        myString += str(givenList[i])
        myString += " "
    print(myString)