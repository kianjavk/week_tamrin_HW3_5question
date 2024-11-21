# steo 1: open the file students
def read_students(filename):
    """Reads student names from a file and returns them as a set."""

    with open(filename, 'r') as file:
        return set(line.strip() for line in file)


def compare_classes(class_A, class_B):
    """Compares two sets of students and prints the results."""
    both_of_them = class_A & class_B
    only_class_A = class_A - class_B
    only_class_B = class_B - class_A

    print(f"Students who are in both classes: {both_of_them}")
    print(f"Students who are only in class A: {only_class_A}")
    print(f"Students who are only in class B: {only_class_B}")

