text = input("Matn kiriting: ")
vowels = "aeiouyAEIOUY"

vowel_count = 0
consonant_count = 0

for i in text:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Unli harflar: {vowel_count}")
print(f"Undosh harflar: {consonant_count}")