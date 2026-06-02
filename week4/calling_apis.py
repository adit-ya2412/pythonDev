import requests
from dataclasses import dataclass
url="https://jsonplaceholder.typicode.com/users"
try:
    response=requests.get(url,timeout=5)
    response.raise_for_status()
    data=response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.RequestException as e:
    print(e)


# print(data)

@dataclass
class User:
    id:str
    name:str
    username:str
    email:str
    address:object
    phone:str
    website:str
    company:object

users=[]

for user in data:
        users.append(User(user["id"],user["name"],user["username"],user["email"],user["address"],user["phone"],user["website"],user["company"]))

print(f"Total users :{len(users)}")
user_names=[u.name for u in users]
print(f"User names -> :{user_names}")
print(user)

romaguera_users = [
    user.name
    for user in users
    if user.company["name"] == "Romaguera-Crona"
]

print(romaguera_users)

company_users = {}

for user in users:

    company = user.company["name"]

    if company not in company_users:
        company_users[company] = []

    company_users[company].append(user.name)

print(company_users)