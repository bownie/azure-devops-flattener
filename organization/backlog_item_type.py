import uuid
from enum import Enum

class BacklogItemTypes(Enum):
    EPIC = 1
    FEATURE = 2
    USER_STORY = 3
    TASK = 4
    SPIKE = 5
    BUG = 6

class BacklogItemType():
    def __init__(self, type_id, name):
        self.backlog_item_type_name = name
        self.backlog_item_type_id = type_id
        self.backlog_item_type_uuid = uuid.uuid4
