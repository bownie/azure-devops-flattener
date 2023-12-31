import uuid
from .backlog_item import BacklogItem

class Backlog:
    def __init__(self, name):
        self.backlog_name = name
        self.team_uuid = None
        self.backlog_uuid = uuid.uuid4
        self.work_items = []

    def add_backlog_item(self, backlog_item_type, name, description):
        self.work_items.append(BacklogItem(backlog_item_type, name, description))

    def assign_team(self, team_uuid):
        self.team_uuid = team_uuid
