with open("input.txt") as file:
    content = file.readlines()
#for i in range(len(content)):
#    content[i] = content[i].replace("\n", "")
#print(content)

for i in content:
    print(i.strip())


with open("output.txt","w") as o_file:
    o_file.write("Efe"+"\n")
    o_file.write("Altun")