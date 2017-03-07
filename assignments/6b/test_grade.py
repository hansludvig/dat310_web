
grades = {}

print("Loading grades.tsv ...")
with open("grades.tsv", "r") as h:
    for line in h:
        student_no, course_code, semester, grade = line.strip().split("\t")
        current_result = {semester: {course_code: grade}}
        if student_no in grades:
            if semester in grades[student_no]:
                if course_code in grades[student_no][semester]:
                    pass # if the coures is already added, do nothing.
                else:
                    grades[student_no][semester][course_code] = grade
            else:
                grades[student_no][semester] = {course_code: grade}
        else:
            grades[student_no] = current_result

print(grades)

'''
result_list = {semester: {course_code: grade}}
if student_no in grades:
    grades[student_no].append(result_list)
else:
    grades[student_no] = result_list

    '''