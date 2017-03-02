d = {
    "123": "John",
    "456": "Mary"
}

key = "123"

if key in d:
    print(d[key])

d.get(key, None)

for key in d:
    print(key, d[key])

for key, val in d.items():
    print(key, val)

d2 = {
    "B": [2,4],
    "C": [],
    "A": [1,4,7]
}

for key, val in sorted(d2.items()):
    print(key,val)

grade = {
    "1": {"DAT310": "A", "DAT100": "B"},
    "3": {"DAT630": "A"},
    "2": {"DAT500": "C"}
}

grade2 = {
    "123456":{
        "1": {"DAT310": "A", "DAT100": "B"},
        "3": {"DAT630": "A"},
        "2": {"DAT500": "C"}
    },
    "111111":{

    }
}


courses = {
    "DAT100": "objecy",
    "DAT310": "WEB"
}

for semester, sem_grades in grade.items():
    print(semester)
    for course_id, grade in sorted(sem_grades.items()):
        print("\t{}: {}".format(course_id, grade))
    for course_id, grade in sorted(sem_grades.items()):
        print("\t{}: {}".format(course_id[course_id], grade))
    for course_id, grade in sorted(sem_grades.items()):
        print("\t{}: {}".format(course_id.get(course_id, course_id), grade))
