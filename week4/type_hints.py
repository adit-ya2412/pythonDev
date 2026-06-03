from dataclasses import dataclass
employees = [
    {"id": 101, "name": "Aditya", "department": "Engineering", "salary": 85000,"Company":"sdase"},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 60000,"Company":"Tata"},
    {"id": 103, "name": "Rohan", "department": "Engineering", "salary": 95000,"Company":"sdase"},
    {"id": 104, "name": "Neha", "department": "Finance", "salary": 75000,"Company":"Reliance"},
    {"id": 105, "name": "Aman", "department": "Engineering", "salary": 70000,"Company":"Adani"}
]
@dataclass
class User:
    id:int
    name:str
    department:str
    salary:int
    company:str

users=[]
for emp in employees:
    users.append(User(emp["id"],emp["name"],emp["department"],emp["salary"],emp["Company"]))

# def find_highest_paid(users: list[User]) -> User:
#     return max(users, key=lambda user: user.salary)
def find_highest_paid(users:list[User]) -> User:

    highest = users[0]

    for user in users:

        if user.salary > highest.salary:
            highest = user

    return highest


print(find_highest_paid(users))

def get_average_salary(users:list[User]) -> float:
    total_salary=sum(u.salary for u in users)
    return total_salary/len(users)

print(get_average_salary(users))

def get_company_users(users:list[User],company_name:str)-> list[str]:
    user_names=[]
    for u in users:
        if u.company==company_name:
            user_names.append(u.name)
    return user_names

print(get_company_users(users,"Tata"))


def find_user_by_id(users:list[User],user_id:int)-> User | None:
    
    user= list(filter(lambda x:x.id == user_id,users))
    if len(user) == 0:
        return None
    else :
        return user[0]

print(find_user_by_id(users,103
                      ))

def group_by_department(users:list[User])-> dict[str,list[str]]:
    departments_dict={}
    for u in users:
        if u.department not in departments_dict:
            departments_dict[u.department]=[]   
        departments_dict[u.department].append(u.name)
        
    return departments_dict

print(group_by_department(users))


def get_salary_range(users:list[User])->tuple[int,int]:
    max_salary=max(users,key=lambda x:x.salary).salary

    min_salary=min(users,key=lambda x :x.salary).salary
    return min_salary,max_salary


print(get_salary_range(users))