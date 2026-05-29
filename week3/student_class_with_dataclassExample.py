from dataclasses import dataclass

@dataclass
class Student:
    name:str
    marks:list[int]
    
    def average(self):
        self.average_marks= sum(self.marks)/len(self.marks)
        return self.average_marks
    
    def grade(self):

        if self.average_marks >= 90:
            return "A"
        elif self.average_marks >= 75:
            return "B"
        elif self.average_marks >= 50:
            return "C"
        return "F"
    

students=[
        Student("Aditya",[78, 85, 90]),
        Student("Aditi",[45, 50, 39]),
        Student("Sakshi",[92, 88, 95])
    ]

for student in students:
    print(f"Report card for {student.name}")
    print(f"Average is :{student.average():.2f}")
    print(f"Grade is : {student.grade()}")
    print("\n")