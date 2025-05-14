from grade_calc import grade_calc

def process_student(name, grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    letter = grade_calc(average)
    return f"{name}'s average is {average}, {letter}"

   
 

print(process_student('andrea',50,60,70))
