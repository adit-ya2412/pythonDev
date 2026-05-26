employees = [
    {"name": "Aditya", "salary": 85000},
    {"name": "Priya", "salary": 60000},
    {"name": "Rohan", "salary": 95000},
    {"name": "Neha", "salary": 75000}
]


def salary_generator():
    for emp in employees:
        yield emp["salary"]



def get_high_salary():
    for emp in employees:
        if emp["salary"]>80000:
            yield emp["salary"]


n=0

def infinie_generator():
    n=1
    while True:

        yield n
        n+=1

def readFile():

      with open("recoveryCode.txt","r") as file:

       for line in file:
            yield line.strip('\n')

def fibonacci_generator():
    a,b=1,1
    while True:
       
       yield a
       a,b=b,a+b

def prime_number_generator():
    n=2
    while True:
        flag=True
        range_check= int (n/2)
        for i in range(2,range_check):
            if n % i ==0:
                flag=False
                break
            
        if flag :
            yield n
        n+=1

prime_gen=prime_number_generator()
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))

# getLine=readFile()

# print(next(getLine))

# fibonacci_gen=fibonacci_generator()

# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))
# print(next(fibonacci_gen))



high_salary_gen=get_high_salary()

infinie_gen=infinie_generator()
print(next(infinie_gen))
print(next(infinie_gen))
print(next(infinie_gen))
print(next(infinie_gen))
print(next(infinie_gen))
print(next(high_salary_gen))
salary_gen=salary_generator()
print(next(salary_gen))

print(next(salary_gen))
print(next(salary_gen))
print(next(salary_gen))