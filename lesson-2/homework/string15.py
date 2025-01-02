text = input("Matn kiriting: ")
txt = text.split()
name = ''
for i in range(len(txt)):
    name += txt[i][0]
print(name)