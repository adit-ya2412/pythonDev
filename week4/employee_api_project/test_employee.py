from employee import User, get_average_salary, find_user_by_id,group_by_department,get_salary_range

test_users=[ User(1, "A", "Eng", 100, "X"),
        User(2, "B", "Eng", 300, "Y")]


def test_find_user_by_id():
    result=find_user_by_id(test_users,1)

    assert result == test_users[0]



def test_average_salary():

    result = get_average_salary([
        User(1, "A", "Eng", 100, "X"),
        User(2, "B", "Eng", 300, "Y")
    ])

    assert result == 200

def test_group_by_department():
    result=group_by_department(test_users)

    assert result == {"Eng" :["A","B"]}


def test_get_salary_range():
    result=get_salary_range(test_users)

    assert result == (100,300)