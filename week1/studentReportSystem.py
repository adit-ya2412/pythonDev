students = [
    {"name": "Aditya", "marks": [78, 85, 90]},
    {"name": "Rohan", "marks": [45, 50, 39]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Aman", "marks": [60, 65, 70]}
]


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    return "F"


def generate_report(student):
    average = calculate_average(student["marks"])
    grade = calculate_grade(average)

    return {
        "name": student["name"],
        "average": average,
        "grade": grade
    }

def pass_percentage(total_failed,total_students):
    pass_students=total_students-total_failed
    return (pass_students/total_students) *100;

def find_subject_toppers(students):
   
   subjects=["Maths","Science","English"]

   subject_toppers={
       "Maths":{"name":"","marks":0},
       "Science":{"name":"","marks":0},
       "English":{"name":"","marks":0},
   }
   for student in students:
       for index,marks in enumerate(student["marks"]):
           subject=subjects[index]
        
           if subject_toppers[subject]["marks"]<marks:
                subject_toppers[subject]["marks"]=marks
                subject_toppers[subject]["name"]=student["name"]
        
   return subject_toppers
           
print (find_subject_toppers(students))