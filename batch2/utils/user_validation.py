def validate_name(name):
    if name.strip() == "":
        return "Name cannot be empty."
    return None

def validate_email(email):
    if email.strip() == "":
        return "Email cannot be empty."
    if "@" not in email:
        return "Invalid email format."
    return None

def validate_password(password):
    if password.strip() == "":
        return "Password cannot be empty."
    if len(password) < 5:
        return "Password must be at least 5 characters long."
    return None