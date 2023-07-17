import uuid
from .backlog_item_type import BacklogItemType

class Organization:
    org_name: str
    org_uuid: str
    backlog_item_types = []

    def __init__(self, name):
        self.org_name = name
        self.org_uuid = uuid.uuid4

        # build items
        self.backlog_item_types.append(BacklogItemType("Feature", 1))
        self.backlog_item_types.append(BacklogItemType("Epic", 2))
        self.backlog_item_types.append(BacklogItemType("User Story", 3))
        self.backlog_item_types.append(BacklogItemType("Task", 4))
        self.backlog_item_types.append(BacklogItemType("Spike", 5))

    def get_name(self) -> str:
        return self.org_name
    
    def get_backlog_item_types(self):
        return self.backlog_item_types
