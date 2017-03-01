
grades = {}

print("Loading grades.tsv ...")
with open("grades.tsv", "r") as h:
    for line in h:
        student_no, course_code, semester, grade = line.strip().split("\t")
        result_list = [course_code, semester, grade]
        if student_no in grades:
            grades[student_no].append(result_list)
        else:
            grades[student_no] = [result_list]

arr = []
for g in grades:
    for i in grades[g]:
        for x in range(1, 10):
            if str(x) in i:
                arr.append(x)
            else:
                continue

print(arr)

print(grades['111111'])

my_list = grades['111111']

for q in grades['111111']:
    print(q)

print(my_list[0][1])

if my_list[0][1] == '1':
    print(my_list[0][0])

a = grades['111111']
for j in range(1, len(a)):
    key = a[j][1]
    i = j - 1
    while i >= 0 and a[i][1] > key:
        a[i + 1][1] = a[i][1]
        i = i - 1
    a[i + 1][1] = key

print(a)