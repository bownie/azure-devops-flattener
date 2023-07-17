import uuid

class BacklogItemType:
    backlog_item_type_name: str
    backlog_item_type_id: int
    backlog_item_type_uuid: str
    backlog_item_description: str
 
    def __init__(self, name, type_id):
        self.backlog_item_name = name
        self.backlog_type_id = type_id
        self.backlog_item_type_uuid = uuid.uuid4
