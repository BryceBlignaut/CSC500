# Dictionary containing course information
# The course numbers are the keys to other attribute information
courses = {
    "CSC101": {"Room Number": "3004", "Instructor": "Haynes", "Meeting Time": "8:00 a.m."},
    "CSC102": {"Room Number": "4501", "Instructor": "Alvarado", "Meeting Time": "9:00 a.m."},
    "CSC103": {"Room Number": "6755", "Instructor": "Rich", "Meeting Time": "10:00 a.m."},
    "NET110": {"Room Number": "1244", "Instructor": "Burke", "Meeting Time": "11:00 a.m."},
    "COM241": {"Room Number": "1411", "Instructor": "Lee", "Meeting Time": "1:00 p.m."}}

# prompt user for course number input
def enter_course_number():
    return input("Enter a Course Number: ").strip().upper()

# continue to run program until a correct input is provided via the enter_course_number()
while True:
    course_number = enter_course_number()

# print course information
    if course_number in courses:
        print("Course Information")
        print(f"Course Number: {course_number}")
        print(f"Room Number: {courses[course_number]['Room Number']}")
        print(f"Instructor: {courses[course_number]['Instructor']}")
        print(f"Meeting Time: {courses[course_number]['Meeting Time']}")
        break

# the user a list of no has the correct keys available to provide the correct input
    else:
        print(f"Invalid course: Please choose a course from the list: {courses.keys()}")
