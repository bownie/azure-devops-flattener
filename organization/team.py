import uuid
from enum import Enum
from .user import User, UserType

class TeamType(Enum):
    SCRUM = 1
    KANBAN = 2
    SCRUMBAN = 3

class Team:
    def __init__(self, name):
        self.team_name = name
        self.team_uuid = uuid.uuid4
        self.team_type_id = TeamType.SCRUM
        self.users = []

    def add_user(self, user_name, user_type):
        self.users.append(User(user_name, user_type))

    def generate_default_users(self):
        self.users.append(User("Richard", UserType.ORGANIZATIONOWNER))
        self.users.append(User("Claire", UserType.PROJECTOWNER))
        self.users.append(User("Sam", UserType.DEVELOPER))
        self.users.append(User("Lois", UserType.STAKEHOLDER))
        self.users.append(User("Kirsten", UserType.STAKEHOLDER))
