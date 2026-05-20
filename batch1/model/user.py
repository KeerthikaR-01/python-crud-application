class User:
    id: None
    name: None  
    email: None
    password: None

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password