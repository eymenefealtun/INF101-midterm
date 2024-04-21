Physics = [4, 3, 3.5]
Math = [2, 3, 3]
Biology = [3, 3, 4]
Names = ['John', 'Ali', 'Pelin']
Transcript = {}


i = 0

while i < len(Names):
    avarage = (Physics[i] + Math[i] + Biology[i]) / 3
    Transcript[Names[i]] = avarage
    i += 1

print(Transcript)

