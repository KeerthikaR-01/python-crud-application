class UserRepository:
    users = []

    def add_user(self, new_user):
        self.users.append(new_user)

    def get_users(self):
        return self.users
    
    def get_users_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    
    