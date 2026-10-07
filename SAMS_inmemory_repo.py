student_records = []

COURSE_CATALOGUE = (
    ("CS501", "Database Systems", 4),
    ("CS502", "Operating Systems", 4),
    ("CS503", "Web Development using Python", 3),
)

enrolled_students = {
    "CS501": set(),
    "CS502": set(),
    "CS503": set()
}

faculty_course_map = {}


def add_student(roll_no, name):
    student_records.append({
        "roll_no": roll_no,
        "name": name
    })


def enrol_student(roll_no, course_code):
    if course_code in enrolled_students:
        enrolled_students[course_code].add(roll_no)
    else:
        print("Invalid course code:", course_code)


def assign_faculty(faculty_name, course_codes):
    valid_courses = []

    for course_code in course_codes:
        if course_code in enrolled_students:
            valid_courses.append(course_code)
        else:
            print("Invalid course code:", course_code)

    faculty_course_map[faculty_name] = valid_courses


if __name__ == "__main__":

    add_student("2500520024", "MUSUNURI SIVA NAGA GANESH")
    add_student("2500520037", "G KRISHNA REDDY")

    enrol_student("2500520024", "CS501")
    enrol_student("2500520037", "CS501")
    enrol_student("2500520024", "CS503")

    assign_faculty("Dr.Y RAMAKRISHNA", ["CS501", "CS502"])

    print("=== SAMS In-Memory Repository ===")
    print("Students:", student_records)
    print("Catalogue:", COURSE_CATALOGUE)
    print("CS501 enrolled:", enrolled_students["CS501"])
    print("Faculty map:", faculty_course_map)