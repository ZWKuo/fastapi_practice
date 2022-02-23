from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify(Login_password , Hash_password):
    return pwd_context.verify(Login_password , Hash_password)