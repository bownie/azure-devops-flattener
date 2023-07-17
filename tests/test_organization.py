import pytest
import organization.organization

organization_name = "Test Organization"
org = organization.organization.Organization(organization_name)

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

def test_organization():
    assert org.get_name() == organization_name