import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def load_courses():
    courses_file_path = os.path.join(current_dir, '..', 'data', 'courses.json')
    with open(courses_file_path, 'r') as file:
        return json.load(file)

def recommended_courses(user_interests):
    courses = load_courses()

    matching_courses = []

    for course in courses["courses"]:
        if any(interest in course["interests"] for interest in user_interests):
            matching_courses.append(course)

    return matching_courses