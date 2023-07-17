import uuid

class BacklogItem:
    backlog_item_name: str
    backlog_type_id: int
    backlog_item_id: str
    backlog_item_description: str
    backlog_parent_id: str
 
    def __init__(self, name, type_id):
        self.backlog_item_name = name
        self.backlog_type_id = type_id
        self.backlog_item_id = uuid.uuid4
