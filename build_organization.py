import pprint
import organization.organization

org = organization.organization.Organization()

pprint.pprint("Org name = " + org.get_name())

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5