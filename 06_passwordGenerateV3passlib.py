from passlib.context import CryptContext
import random
import string

password_context = CryptContext(schemes=["bcrypt"])

def generate_pssw():
    size = 9
    return password_context.hash("".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size)))

new_pssw = generate_pssw()
print("Your new password is:", new_pssw)


