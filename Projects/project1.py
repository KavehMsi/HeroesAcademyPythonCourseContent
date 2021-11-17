

def print_menu():
    print("================================================")
    print("1-Enter Students' Data")
    print("2-Print All Students' Grades Average")
    print("3-Print the Best Student's Grade Average")
    print("4-Print the School's Grade Average")
    print("5-Exit")
    print("================================================")
    print()


def get_student_data():
    print("Please enter number of students:")
    m = int(input())
    data = {}
    for i in range(m):
        temp = input().split()
        data[temp[0]] = [float(temp[1]), float(temp[2]), float(temp[3])]
    return data


def calc_average(grades):
    grade_sum = 0
    for grade in grades:
        grade_sum += grade
    average = grade_sum / len(grades)
    return average


def print_all_student_grade_average(data):
    if len(data) == 0:
        print("No Student Found")
        return
    else:
        for name, grades in data.items():
            print("================================================")
            print("Name: ", name)
            grade_average = calc_average(grades)
            print("Grade average: ", grade_average)
            print("================================================")


def print_best_student_grade_average(data):
    max_average = -1
    for grades in data.values():
        temp_average = calc_average(grades)
        if temp_average > max_average:
            max_average = temp_average
    print("Max grade average is:", max_average)


def print_school_grade_average(data):
    grade_averages = []
    for grade in data.values():
        temp = calc_average(grade)
        grade_averages.append(temp)
    school_average = calc_average(grade_averages)
    print("The school's grade average is:", school_average)


def main():
    data = {}
    while True:
        print_menu()
        n = int(input())
        if n == 1:
            data = get_student_data()
        elif n == 2:
            print_all_student_grade_average(data)
        elif n == 3:
            print_best_student_grade_average(data)
        elif n == 4:
            print_school_grade_average(data)
        elif n == 5:
            print("Good Luck!")
            break
        else:
            print("Wrong Input, try again.")


main()
