"""
Assignment 6B: Gradebook
"""

import os

HTML_FRAME_TOP = "<!DOCTYPE HTML>\n<html>\n<head>\n<title>{title}</title>\n" \
                 "<link rel=\"stylesheet\" href=\"{css_path}gradebook.css\"/>\n</head>\n<body>\n"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"


class Gradebook(object):

    def __init__(self):
        self.__students = {}  # dict with student_no as key and name as value
        self.__courses = {}
        self.__grades = {}
        self.__semester_and_course = {}

    def insertion_sort(self, a):

        for j in range(1, len(a)):
            key = a[j][1]
            i = j - 1
            while i >= 0 and a[i][1] > key:
                a[i + 1][1] = a[i][1]
                i = i - 1
            a[i + 1][1] = key

        return a

    def __search_for_course(self, value, double_arr):

        for j in range(0, len(double_arr)):
            if double_arr[j][0] == value:
                course_and_grad = [double_arr[j][0], double_arr[j][2]]
                return course_and_grad
        return '0'

    def __create_folders(self):
        """Generates folder structure."""
        print("Generating folder structure ... ")
        for d in ["courses", "semesters", "students"]:
            os.makedirs("output/" + d, exist_ok=True)

    def __load_data(self):
        """Loads data from input tsv files."""
        # Load students
        print("Loading students.tsv ...")
        with open("students.tsv", "r") as f:
            for line in f:
                student_no, name = line.strip().split("\t")
                self.__students[student_no] = name

        # Load courses
        print("Loading courses.csv ...")
        with open("courses.tsv", "r") as g:
            for line in g:
                course_code, course_name = line.strip().split("\t")
                self.__courses[course_code] = course_name

        # Load grades
        print("Loading grades.tsv ...")
        with open("grades.tsv", "r") as h:
            for line in h:
                student_no, course_code, semester, grade = line.strip().split("\t")
                current_result = {semester: {course_code: grade}}
                if student_no in self.__grades:
                    if semester in self.__grades[student_no]:
                        if course_code in self.__grades[student_no][semester]:
                            pass  # if the course is allready added, do nothing.
                        else:
                            self.__grades[student_no][semester][course_code] = grade
                    else:
                        self.__grades[student_no][semester] = {course_code: grade}
                else:
                    self.__grades[student_no] = current_result

    def __generate_student_files(self):
        print("Generating student file ...")
        for s, n in self.__students.items():
            sPath = "output/students/{}.html".format(s)
            with open(sPath, "w") as f:
                f.write(HTML_FRAME_TOP.replace("{title}", "Grades " + str(s)).replace("{css_path}", "../"))
                f.write("<h1>Student</h1><table>")
                f.write("<tr><td><strong>Student no:</td><td>{}</td></tr>".format(s))
                f.write("<tr><td><strong>Name:</td><td>{}</td></tr>".format(n))
                f.write("</table><br />\n<table>\n<thead>\n<tr><th>Course code</th><th>Name</th><th>Grade</th></tr>\n"
                        "</thead>\n<tbody>\n")

                for semester, subject in self.__grades[s].items():
                    tmp = 1
                    for sub, g in subject.items():

                        if len(subject) > 1:
                            if tmp == 1:
                                f.write("<tr><td colspan=\"3\"><em>Semester {}</em></td></tr>".format(semester))
                                tmp = 0
                            f.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(sub, self.__courses[sub], g))
                        else:
                            f.write("<tr><td colspan=\"3\"><em>Semester {}</em></td></tr>".format(semester))
                            f.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(sub, self.__courses[sub], g))

                f.write("</tbody>\n</table>")
                f.write(HTML_FRAME_BOTTOM)

    def __generate_course_files(self):
        print("Generating course files ...")
        for code, name in self.__courses.items():
            sPath = "output/courses/{}.html".format(code)
            with open(sPath, "w") as f:
                f.write(HTML_FRAME_TOP.replace("{title}", "Course " + code).replace("{css_path}", "../"))
                f.write("<h1>Course {}</h1><h2>{}</h2><table>".format(code, name))
                f.write("<thead>\n<tr><th>Student no</th><th>Grade</th></tr>\n</thead>\n<tbody>\n")
                store_grade = {}
                for stud, sem in self.__grades.items():
                    for c, g in sem.items():
                        for course, grade in g.items():
                            if course == code:
                                f.write("<tr><td>{}</td><td>{}</td></tr>".format(stud, grade))
                                if (store_grade == {}) or ((grade in store_grade) == False):
                                    store_grade[grade] = 1
                                else:
                                    count = store_grade[grade] + 1
                                    store_grade[grade] = count

                f.write("</tbody>\n</table>\n<h3>Summary</h3><table>\n<thead>\n<tr><th>Grade</th><th>Count</th></tr>"
                        "\n</thead>\n<tbody>")
                for g, c in sorted(store_grade.items()):
                    f.write("<tr><td>{}</td><td>{}</td></tr>".format(g, c))
                f.write("</tbody>\n</table>\n")
                f.write(HTML_FRAME_BOTTOM)

    def __generate_semester_files(self):
        print("Generating semester files ...")
        for stud, sem in self.__grades.items():
            for nr, course in sem.items():
                for c, g in course.items():

                    if self.__semester_and_course == {}:
                        self.__semester_and_course[nr] = {c: 1}
                    elif nr not in self.__semester_and_course:
                        self.__semester_and_course[nr] = {c: 1}

                    elif nr in self.__semester_and_course:
                        if c in self.__semester_and_course[nr]:
                            count = self.__semester_and_course[nr][c] + 1
                            self.__semester_and_course[nr][c] = count
                        else:
                            self.__semester_and_course[nr].update({c: 1})
                    else:
                        pass  # do nothing

        print(self.__semester_and_course)

        for semester, value in self.__semester_and_course.items():

            sPath = "output/semesters/{}.html".format(semester)
            with open(sPath, "w") as f:
                f.write(HTML_FRAME_TOP.replace("{title}", "Semester " + semester).replace("{css_path}", "../"))
                f.write("<h1>Semester {}</h1><table>".format(semester))
                f.write("<thead>\n<tr><th>Course code</th><th>Name</th><th>#Students</th></tr>\n</thead>\n<tbody>")
                for i, j in value.items():
                    f.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(i, self.__courses[i], j))
                f.write("</tbody>\n</table>\n")
                f.write(HTML_FRAME_BOTTOM)

    def __generate_index_file(self):
        """Generates the index HTML file."""
        print("Generating index file ...")
        with open("output/index.html", "w") as f:
            f.write(HTML_FRAME_TOP.replace("{title}", "Gradebook Index").replace("{css_path}", "../"))


            # list of students
            f.write("<h2>Students</h2>")
            f.write("<table>\n<thead>\n<tr><th>Student no</th><th>Name</th></tr>\n</thead>\n<tbody>\n")
            for student_no, name in sorted(self.__students.items()):
                row = "<tr><td><a href=\"students/{student_no}.html\">{student_no}</a></td><td>{name}</td></tr>\n"
                f.write(row.replace("{student_no}", student_no).replace("{name}", name))
            f.write("</tbody>\n</table>\n")

            # list of courses
            f.write("<h2>Courses</h2><table>\n<thead>\n<tr><th>Course code</th><th>Name</th></tr>\n</thead>\n<tbody>\n")
            for course, name in sorted(self.__courses.items()):
                f.write("<tr><td><a href=\"courses/{}.html\">{}</a></td><td>{}</td></tr>\n".format(course, course, name))
            f.write("</tbody>\n</table>\n")

            # list of semesters
            f.write("<h2>Semesters</h2><table>\n<thead>\n")
            f.write("<tr><th>Semester</th><th>Courses</th></tr>\n</thead>\n<tbody>\n")
            for semester, value in sorted(self.__semester_and_course.items()):
                f.write("<tr><td><a href=\"semesters/{}.html\">{}</a></td><td>\n".format(semester, semester))
                for i, j in sorted(value.items()):
                    f.write("<a href=\"courses/{}.html\">{}</a> ".format(i, i))
                f.write("</td></tr>\n")
            f.write("</tbody>\n</table>\n")

            f.write(HTML_FRAME_BOTTOM)

    def generate_files(self):
        self.__create_folders()
        self.__load_data()
        self.__generate_student_files()
        self.__generate_course_files()
        self.__generate_semester_files()
        self.__generate_index_file()


def main():
    gradebook = Gradebook()
    gradebook.generate_files()

if __name__ == '__main__':
    main()