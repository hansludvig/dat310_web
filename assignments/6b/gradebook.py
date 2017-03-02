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
                result_list = [course_code, semester, grade]
                if student_no in self.__grades:
                    self.__grades[student_no].append(result_list)
                else:
                    self.__grades[student_no] = [result_list]

    def __generate_student_files(self):
        print("Generating student file ...")
        for s, n in self.__students.items():
            sPath = "output/students/{}".format(s)
            with open(sPath, "w") as f:
                f.write(HTML_FRAME_TOP.replace("{title}", "Grades " + str(s)).replace("{css_path}", "../"))
                f.write("<h1>Student</h1><table>")
                f.write("<tr><td><strong>Student no:</td><td>{}</td></tr>".format(s))
                f.write("<tr><td><strong>Name:</td><td>{}</td></tr>".format(n))
                f.write("</table><br />\n<table>\n<thead>\n<tr><th>Course code</th><th>Name</th><th>Grade</th></tr>\n"
                        "</thead>\n<tbody>\n")
                print(self.__grades[s])
                list_of_results = self.insertion_sort(self.__grades[s])  # Sort semesters
                tmp = '0'
                for i in list_of_results:

                    if tmp != i[1]:
                        f.write("<tr><td colspan=\"3\"><em>Semester {}</em></td></tr>".format(i[1]))
                        f.write("<tr><td>{}</td><td>{}</td><td> B</td></tr>".format(i[0], self.__courses[i[0]]))
                    else:
                        f.write("<tr><td>{}</td><td>{}</td><td> B</td></tr>".format(i[0], self.__courses[i[0]]))
                    tmp = i[1]
                f.write("</tbody>\n</table>")
                f.write(HTML_FRAME_BOTTOM)

    def __generate_course_files(self):
        print("Generating course file ...")
        for c, n in self.__courses.items():
            sPath = "output/students/{}".format(c)
            with open(sPath, "w") as f:
                f.write(HTML_FRAME_TOP.replace("{title}", "Course " + str(c)).replace("{css_path}", "../"))
                f.write("<tr><th>Student no</th><th>Grade</th></tr>\n</thead>\n<tbody>\n")
                c_name = []
                for s, meta  in self.__grades.items():
                    stud_and_grade = self.__search_for_course(str(c), meta)
                    c_name.append(stud_and_grade)
                    if stud_and_grade != 0:
                        f.write("<tr><td>{}</td><td>{}</td></tr>".format(s, c_name[0]))
                f.write("</tbody>\n</table>\n<h3>Summary</h3><table>\n<thead>\n<tr><th>Grade</th><th>Count</th></tr>\n"
                        "</thead>\n<tbody>")
                for a in range(0, len(c_name)):
                    # try catch ...

    def __generate_semester_files(self):
        """Generates HTML files for semesters."""
        pass

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

            # list of semesters

            f.write(HTML_FRAME_BOTTOM)

    def generate_files(self):
        self.__create_folders()
        self.__load_data()
        self.__generate_student_files()
        # self.__generate_course_files()
        # self.__generate_semester_files()
        # self.__generate_index_file()


def main():
    gradebook = Gradebook()
    gradebook.generate_files()

if __name__ == '__main__':
    main()