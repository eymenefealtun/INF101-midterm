grades = [23, 345, 34, 33334, 41]
names = ["eymen", "talha", "john", "murat", "saban"]

my_dicstionay = {}
for i in range(len(names)):
    my_dicstionay[names[i]] = grades[i]

print(my_dicstionay)



sorted_dictionary = {}
sorted_values=  sorted(my_dicstionay.values())

for y in range(len(sorted_values)):
        for i in my_dicstionay.keys():
             if my_dicstionay[i] == sorted_values[y]:
                sorted_dictionary[i] = sorted_values[y]

print(sorted_dictionary)