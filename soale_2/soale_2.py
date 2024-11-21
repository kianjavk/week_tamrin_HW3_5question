# student_operations.py, and import this module into
# your main script to display the results
from student_operations import *



def main():

    class_A_students = read_students('students_class_A.txt')
    class_B_students = read_students('students_class_B.txt')

    compare_classes(class_A_students, class_B_students)


# Main script
if __name__ == "__main__":
    main()