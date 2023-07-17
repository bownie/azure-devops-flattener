import uuid
from .backlog_item_type import BacklogItemType
from .backlog_item_type import BacklogItemTypes

class Organization:
    def __init__(self, name):
        self.organization_name = name
        self.organization_uuid = uuid.uuid4
        self.backlog_item_types = []
        self.backlog_items = []

        # build items
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.FEATURE, "Feature"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.EPIC, "Epic"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.USER_STORY, "User Story"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.TASK, "Task"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.SPIKE, "Spike"))
