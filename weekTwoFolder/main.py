from student_pro import process_student



def main():
    """Main function to run the program."""
    print("Welcome to the Student Grade Calculator")
    # Process each student using the same function
    process_student("Alex", 85, 90, 78)
    process_student("Taylor", 92, 88, 95)
    process_student("Jordan", 76, 82, 79)
    print("\nThank you for using the Student Grade Calculator!")
# Run the program

print(process_student("Alex", 85, 90, 78))
print(process_student("Taylor", 92, 88, 95))
print(process_student("Jordan", 76, 82, 79))
if __name__ == "__main__":
    main()