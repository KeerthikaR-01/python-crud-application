class UserRepository:

    users = []

    def add_user(self, new_user):
        self.users.append(new_user)

    def get_users(self):
        return self.users
    
    def get_user_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None