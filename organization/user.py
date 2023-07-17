from enum import Enum

class UserType(Enum):
    STAKEHOLDER = 1
    DEVELOPER = 2
    PROJECTOWNER = 3
    ORGANIZATIONOWNER = 4

class User:
    def __init__(self, name, role):
        self.user_name = name
        self.user_role = role
