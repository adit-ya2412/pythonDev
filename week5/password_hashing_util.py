from passlib.context import CryptContext

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_password_hash(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# hashed=get_password_hash("admin123")
# print(hashed)
# print(verify_password("admin123",hashed))

