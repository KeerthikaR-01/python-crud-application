class UserRepository:
    users = []

    def add_user(self, new_user):
        self.users.append(new_user)

    def get_users(self):
        return self.users
    
    