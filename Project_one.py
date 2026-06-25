import random
import string

def check_password(password):
    if len(password) < 8:
        return "Weak Password"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    
    return "Medium "

def generate_passowrd():
    return ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=") for _ in range(8))


password = generate_passowrd()
print("Password Strength:", check_password('123466'))
print("Suggested Password:", password)
