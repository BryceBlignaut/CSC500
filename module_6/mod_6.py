from collections import Counter


squares = {x: x * x for x in range(1, 78)}

print(squares[77])

print()

temperature = [94, 90, 87, 35, 62]

for i in range(len(temperature)):

    temp = temperature[i] + 1
    temperature.append(temp)

print(temperature)


def second_largest(list_input):

    largest = None
    second_largest = None

    for num in list_input:
        if largest == None:
            largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest == None:
            second_largest = num

# Dictionaries containing course information
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt the user to enter a course number
course_number = input("Enter a course number: ").strip()

# Display course details if the course exists
if course_number in room_numbers:
    print(f"Room Number: {room_numbers[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting Time: {meeting_times[course_number]}")
else:
    print("Course not found.")

