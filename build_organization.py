import pprint
import organization.organization

org = organization.organization.Organization("my organization")

pprint.pprint("Org name = " + org.get_name())
