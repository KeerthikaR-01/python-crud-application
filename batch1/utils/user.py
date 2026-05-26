from utils.file import File
from model.user import User

def convert_to_csv(users):
    csv_data = ''
    for user in users:
        csv_data += f"{user.id},{user.name},{user.email},{user.password}\n"
    return csv_data

def convert_csv_to_users(csv_data):
    users = []
    lines = csv_data.strip().split('\n')
    for line in lines:
        id, name, email, password = line.split(',')
        user = User(id=int(id), name=name, email=email, password=password)
        users.append(user)
    return users

def save_users_to_file(users):
    file = File('data/users.csv')
    file.write(convert_to_csv(users))

def read_users_from_file():
    file = File('data/users.csv')
    csv_data = file.read()
    return convert_csv_to_users(csv_data)