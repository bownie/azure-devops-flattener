import uuid
from .backlog_item_type import BacklogItemType
from .backlog_item_type import BacklogItemTypes
from .team import Team
from .user import UserType

class Organization:
    def __init__(self, name):
        self.organization_name = name
        self.organization_uuid = uuid.uuid4
        self.backlog_item_types = []
        self.backlog_items = []
        self.users = []
        self.backlogs = []
        self.teams = []

    def setup_defaults(self):
        # build items
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.FEATURE, "Feature"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.EPIC, "Epic"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.USER_STORY, "User Story"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.TASK, "Task"))
        self.backlog_item_types.append(BacklogItemType(BacklogItemTypes.SPIKE, "Spike"))

        team = Team("My Team")
        team.add_user("Richard", UserType.ORGANIZATIONOWNER)
        team.add_user("Claire", UserType.PROJECTOWNER)
        team.add_user("Sam", UserType.DEVELOPER)
        team.add_user("Lois", UserType.STAKEHOLDER)
        team.add_user("Kirsten", UserType.STAKEHOLDER)

        self.teams.append(team)
