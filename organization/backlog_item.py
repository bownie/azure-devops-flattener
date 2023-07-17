import uuid

class BacklogItem:
    def __init__(self, type_id, name, description):
        self.backlog_item_name = name
        self.backlog_type_id = type_id
        self.backlog_item_id = uuid.uuid4
        self.backlog_item_description = description
        self.backlog_linked_items = []
