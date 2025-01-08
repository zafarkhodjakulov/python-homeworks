universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments = [university[1] for university in universities]
tuitions = [university[2] for university in universities]

total_students = sum(enrollments)
total_tuition = sum(tuitions)

student_mean = sum(enrollments) / len(enrollments)
sorted_enrollments = sorted(enrollments)
if len(sorted_enrollments) % 2 == 0:
    student_median = (sorted_enrollments[len(sorted_enrollments) // 2 - 1] + sorted_enrollments[len(sorted_enrollments) // 2]) / 2
else:
    student_median = sorted_enrollments[len(sorted_enrollments) // 2]

tuition_mean = sum(tuitions) / len(tuitions)
sorted_tuitions = sorted(tuitions)
if len(sorted_tuitions) % 2 == 0:
    tuition_median = (sorted_tuitions[len(sorted_tuitions) // 2 - 1] + sorted_tuitions[len(sorted_tuitions) // 2]) / 2
else:
    tuition_median = sorted_tuitions[len(sorted_tuitions) // 2]

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)
