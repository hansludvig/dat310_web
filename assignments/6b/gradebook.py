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

        # Load grades

    def __generate_student_files(self):
        """Generates HTML files for students."""
        pass

    def __generate_course_files(self):
        """Generates HTML files for courses."""
        pass

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
        self.__generate_course_files()
        self.__generate_semester_files()
        self.__generate_index_file()


def main():
    gradebook = Gradebook()
    gradebook.generate_files()

if __name__ == '__main__':
    main()