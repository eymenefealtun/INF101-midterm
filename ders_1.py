dict1 = {'a': 2, 'c': 8, 'e': 1}
dict2 = {'e': 1, 'c': 8, 'a': 1}

if len(dict1) != len(dict2):
    print('The dictionaries are not equal!')
else:
    flag = True
    for i in dict1.keys():
        if i not in dict2.keys():
            flag = False
            break
        else:
            if dict1[i] != dict2[i]:
                flag = False
                break

    if flag:
        print('The dictionaries are equal.')
    else:
        print('The dictionaries are not equal.')


names = ["emirhan", "eymen", "john","mustafa"]
