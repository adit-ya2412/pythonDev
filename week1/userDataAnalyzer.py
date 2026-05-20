users = [
    {"name": "Aditya", "age": 24, "is_active": True},
    {"name": "Rohan", "age": 17, "is_active": False},
    {"name": "Priya", "age": 29, "is_active": True},
    {"name": "Aman", "age": 15, "is_active": False},
    {"name": "Neha", "age": 31, "is_active": True}
]

analysis = {
    "total_users": len(users),
    "active_users": 0,
    "average_age": 0,
    "oldest_active_user": "",
    "minors": [],
    "adults": [],
    "teenagers": 0,
    "young_adults": 0,
    "30_and_above": 0
}

total_age = 0
oldest_age = 0


for user in users:
    age = user["age"]
    name = user["name"]

    total_age += age

    # active users
    if user["is_active"]:
        analysis["active_users"] += 1

        if age > oldest_age:
            oldest_age = age
            analysis["oldest_active_user"] = name

    # age categories
    if 13 <= age <= 19:
        analysis["teenagers"] += 1
    elif 20 <= age <= 29:
        analysis["young_adults"] += 1
    elif age >= 30:
        analysis["30_and_above"] += 1

    # grouping
    if age >= 18:
        analysis["adults"].append(name)
    else:
        analysis["minors"].append(name)


analysis["average_age"] = total_age / len(users)


print(f"Total users: {analysis['total_users']}")
print(f"Active users: {analysis['active_users']}")
print(f"Average age: {analysis['average_age']:.1f}")
print(f"Oldest active user: {analysis['oldest_active_user']}")

print("\nAdults:")
for adult in analysis["adults"]:
    print(f"- {adult}")

print("\nMinors:")
for minor in analysis["minors"]:
    print(f"- {minor}")

print(f"\nTeenagers: {analysis['teenagers']}")
print(f"Young Adults: {analysis['young_adults']}")
print(f"30 and above: {analysis['30_and_above']}")