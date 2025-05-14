def calculate_grades(name, score1, score2, score3):
    total = sum([score1,score2,score3])
    average = total / 3
    print(f'Student {name}')
    print(f'Scores: {score1}, {score2}, {score3}')
    print(f'Average: {average}')

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
calculate_grades('Alice', 65,77,99)       
print("\nThank you for using the Student Grade Calculator!")