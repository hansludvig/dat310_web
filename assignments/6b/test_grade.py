
grades = {}

print("Loading grades.tsv ...")
with open("grades.tsv", "r") as h:
    for line in h:
        student_no, course_code, semester, grade = line.strip().split("\t")
        result_list = {semester: {course_code: grade}}
        if student_no in grades:
            grades[student_no].append(result_list)
        else:
            grades[student_no] = result_list

print(grades)