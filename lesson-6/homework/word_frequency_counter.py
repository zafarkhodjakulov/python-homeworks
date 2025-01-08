from collections import Counter
file_path = "./python-homeworks/lesson-6/homework/sample.txt"
save_file = "./python-homeworks/lesson-6/homework/word_counter_report.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file 'sample.txt' does not exist.")
    print("Please create it by typing a paragraph below:")
    user_input = input("Enter your paragraph: \n")
    with open("sample.txt", "w") as file:
        file.write(user_input)
    content = user_input

content = content.lower()
punctuation = "!"
for char in punctuation:
    content = content.replace(char, "")
    
words = content.split()
word_counts = Counter(words)
total_words = sum(word_counts.values())
top_5_words = word_counts.most_common(5)

print(f"Total words: {total_words}")
print("Top 5 most common words:")
for word, count in top_5_words:
    print(f"{word} - {count} {'time' if count == 1 else 'times'}")

with open(save_file, "w") as report_file:
    report_file.write("Word Count Report\n")
    report_file.write(f"Total Words: {total_words}\n")
    report_file.write("Top 5 Words:\n")
    for word, count in top_5_words:
        report_file.write(f"{word} - {count}\n")
