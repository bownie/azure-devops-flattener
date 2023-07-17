import uuid
from .user import User

class Team:
    '''Team'''
    team_name: str
    team_uuid: str
    users: list

    def __init__(self, name):
        self.team_name = name
        self.team_uuid = uuid.uuid4

    def generate_users(self) -> None:
        user = User()
        list.append(user)
