"""dictionary = {key, value}"""

programming_dictionary = {
    'Bug': "An error in a program that prevents the program from running as expected.",
    'Function': "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary['Bug'])

programming_dictionary['Loop'] = "The action of doing something over and over again."
print(programming_dictionary)

'''Creating empty dictionary'''
empty_dictionary = programming_dictionary
print(empty_dictionary)

'''Clearing dictionary'''
empty_dictionary = {}
print(empty_dictionary)

'''Edit an item in a dictionary'''
programming_dictionary['Bug'] = "A moth in your computer"
print(programming_dictionary['Bug'])

'''Loop through a dictionary'''
for key in programming_dictionary:
    print(key)  # The key will be printed
    print(programming_dictionary[key])  # The value will be printed


"""Student Grades"""
'''
- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail" '''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
# TODO 1: Loop through all the student in student_score
for student in student_scores:
    # TODO 2: Extracting the score from student_score
    score = student_scores[student]
    # TODO 3: Assigning the grade based on score
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    # TODO 4: Saving the grade into new dictionary student_grades
    student_grades[student] = grade
print(student_grades)


"""Nesting List and Dictionary"""
'''nested_dictionary = {key1: [value1],
                        key2: {value2}'''

capitals = {
    'France': 'Paris',
    'German': 'Berlin',
}

'''Nested list in dictionary'''
travel_log = {
    'France': ['Paris', 'Little', 'Dijon'],
    'German': ['Stuttgart', 'Berlin']
}
print(travel_log['France'])
print(travel_log['France'][1])

"""Nested dictionary"""
travel_log = {
    'France': {
        'num_visited': 8,
        'cities_visited': ['Paris', 'Little', 'Dijon'],
    },
    'German': {
        'num_visited': 5,
        'cities_visited': ['Berlin', 'Stuttgart', 'Hamburg'],
    },
}
print(travel_log['German']['num_visited'])
print(travel_log['German']['cities_visited'][2])
