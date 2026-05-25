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
    
    def delete_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return user
        return None
    
    def update_user(self, user_id, field_to_update):
        for user in self.users:
            if user.id == user_id:
                user.name = field_to_update.name
                user.email = field_to_update.email
                user.password = field_to_update.password
                return user
        return None

    
    