import random
import string

def password_generate():
    size = 14
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(size))
    return password

new_password = password_generate()
print("Your new password generate is:", new_password)
