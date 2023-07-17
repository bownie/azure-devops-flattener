import uuid
from .backlog_item import BacklogItem

class Backlog:
    backlog_name: str
    backlog_uuid: str
    team_id: str
    workitems: list

    def __init__(self, name, team_id):
        self.backlog_name = name
        self.team_id = team_id
        self.backlog_uuid = uuid.uuid4
