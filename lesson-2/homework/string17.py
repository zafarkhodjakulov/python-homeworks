text = input('Matn kiriting: ')

vowels = 'aeiouAEIOU'

for i in text:
    if i in vowels:
        text = text.replace(i, '*')
print(text)