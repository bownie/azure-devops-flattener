import pytest
import organization.organization

ORGANIZATION_NAME = "Test Organization"
org = organization.organization.Organization(ORGANIZATION_NAME)

def raise_exception():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        raise_exception()

def test_organization():
    assert org.organization_name == ORGANIZATION_NAME
    assert len(org.backlog_item_types) == 5
