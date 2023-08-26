import time
from src import course_recommender

def main():
    print('Welcome to the College Course Recommender Program!')
    
    time.sleep(3)
    
    print("Are you still undecided on what course you want to take for college? Don't worry, this program has your back. Just enter a few of your interests and the program will generate recommended courses for you.")

    time.sleep(6)
    
    print("Get started when you're ready.")

    time.sleep(6)
    
    input_interests = input("Enter your interests (comma-separated): ")
    user_interests = set(interest.strip() for interest in input_interests.split(','))

    print("Generating recommended courses for you, please wait...")

    
    time.sleep(10)

    recommended_courses = course_recommender.recommended_courses(user_interests)

    if recommended_courses:
        print("\nRecommended Courses for you:")
        for course in recommended_courses:
            print(f"Name: {course['name']}")
            print(f"Years to Study: {course['years_to_study']} years")
            print(f"Description: {course['description']}\n")
    else:
        print("\nSorry, no courses found with the given interests.")

if __name__ == "__main__":
    main()