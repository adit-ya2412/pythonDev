# This is week 1 , we are going to take input from  terminal, 
# create a random string out of it from name, last name and date of birth.
#first 3 letters of first name + last 3 letters of last name + last 2 digits of birth year

def generate_random_name(name,last_name,dob_year):
    sanitized_first_name=name.replace(" ","").strip().lower()
    sanitized_last_name=last_name.replace(" ","").strip().lower()
    sanitized_dob_year=dob_year.strip()

    if not sanitized_first_name or not sanitized_last_name:
        return "Invalid name"
    
    if not sanitized_dob_year.isdigit():
        return "Invalid birth date"
    
    year=sanitized_dob_year[-2:]

    if  len(sanitized_first_name)<3 and len(sanitized_last_name)<3 :
        return f"{sanitized_first_name}{sanitized_last_name}_{year}"
    
    first=sanitized_first_name if len(sanitized_first_name)<3 else sanitized_first_name[:3]
    last=sanitized_last_name if len(sanitized_last_name)<3 else sanitized_last_name[-3:]
    return f"{first}_{last}_{year}"
    
# print(generate_random_name("Adi","Cha","2000"))


#######################################################
# day2 
#Password strength checker 
# the condition for this is as follows 
# Requirements:
# Input: password string
# Check:
# length ≥ 8
# has uppercase
# has lowercase
# has digit
# has special char (!@#$%^&*)

def password_strength_checker(password):
    password_strength_counter=0
    passwordhelpHint=[]

    if len(password)>=8:
        password_strength_counter +=1
    else :
        passwordhelpHint.append("Length less than 8")
    if hasUpperCase(password):
        password_strength_counter+=1
    else :
        passwordhelpHint.append("Password with a  upper case is recommended")
    if hasLowerCase(password):
        password_strength_counter+=1
    else :
        passwordhelpHint.append("Password with a lower case is recommended")
    if hasDigit(password):
        password_strength_counter+=1
    else :
        passwordhelpHint.append("Password with a digit is recommended")
    if hasSpecialChar(password):
        password_strength_counter+=1
    else :
        passwordhelpHint.append("Password with a special character is recommended")
    
    print(passwordhelpHint)
    
    hints='\n- '.join(passwordhelpHint)

    if password_strength_counter<=2 :
      return f"Weak Password hints->\n- {hints}"
    if password_strength_counter<5:

        return f"Medium Strength hints->\n- {hints}"
    return "Strong"

def hasUpperCase(password):
    return any(char.isupper() for char in password)

def hasLowerCase(password):
    return any(char.islower() for char in password)
def hasDigit(password):
    return any(char.isdigit() for char in password )
def hasSpecialChar(password):
    special_chars = "!@#$%^&*"
    return any(char in special_chars for char in password)


print(password_strength_checker("Super12"))


    