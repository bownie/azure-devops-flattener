import pytest
import organization.organization

ORGANIZATION_NAME = "Test Organization"
org = organization.organization.Organization(ORGANIZATION_NAME)

def test_exception():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        test_exception()

def test_organization():
    assert org.get_name() == ORGANIZATION_NAME
