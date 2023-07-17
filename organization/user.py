from enum import Enum

class UserTypes(Enum):
    Stakeholder = 1
    Developer = 2
    ProjectOwner = 3
    OrganizationOwner = 4

class User:
    def __init__(self, name, role):
        self.user_name = name
        self.user_role = role
