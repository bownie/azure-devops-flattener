import uuid
from .user import User

class Team:
    def __init__(self, name):
        self.team_name = name
        self.team_uuid = uuid.uuid4
        self.users = []

    def generate_users(self) -> None:
        list.append(User())
