from organization.backlog import Backlog
from organization.backlog_item import BacklogItem
from organization.backlog_item_type import BacklogItemType, BacklogItemTypes


FEATURE_TYPE_TEST_NAME = "FeatureTestType"
FEATURE_NAME="New Feature"
FEATURE_DESCRIPTION="New Feature Description"
BACKLOG_NAME="My Backlog"

backlog_item_type = BacklogItemType(BacklogItemTypes.FEATURE, FEATURE_TYPE_TEST_NAME)

backlog_item = BacklogItem(BacklogItemTypes.FEATURE, FEATURE_NAME, FEATURE_DESCRIPTION)

backlog = Backlog(BACKLOG_NAME)

def test_backlog_item_type():
    assert backlog_item_type.backlog_item_type_name == FEATURE_TYPE_TEST_NAME

def test_backlog_item():
    assert backlog_item.backlog_item_name == FEATURE_NAME
    assert backlog_item.backlog_item_description == FEATURE_DESCRIPTION

def test_backlog():
    assert backlog.backlog_name == BACKLOG_NAME
    backlog.add_backlog_item(BacklogItemTypes.FEATURE, FEATURE_NAME, FEATURE_DESCRIPTION)
    assert len(backlog.work_items) == 1
