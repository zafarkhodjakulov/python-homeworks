import csv
filepath = "./python-homeworks/lesson-10/homework/grades.csv"

def read_grades(file_path):
    grades = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({
                "Name": row["Name"],
                "Subject": row["Subject"],
                "Grade": float(row["Grade"])
            })
    return grades

def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}

    for entry in grades:
        subject = entry["Subject"]
        grade = entry["Grade"]

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    averages = {}
    for subject in subject_totals:
        averages[subject] = subject_totals[subject] / subject_counts[subject]

    return averages

def write_average_grades(file_path, averages):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg_grade in averages.items():
            writer.writerow([subject, avg_grade])

def main():
    input_file = "./python-homeworks/lesson-10/homework/grades.csv"
    output_file = "./python-homeworks/lesson-10/homework/average_grades.csv"

    grades = read_grades(input_file)

    averages = calculate_average_grades(grades)

    write_average_grades(output_file, averages)

    print(f"Average grades have been written to {output_file}.")

