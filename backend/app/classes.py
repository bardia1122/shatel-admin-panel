class KB:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_permission(self):
        return self.role
