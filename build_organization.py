import pprint
import organization.organization

org = organization.organization.Organization("my organization")

pprint.pprint("Org name = " + org.organization_name)

org.create_product_team("Product Team #1", 5)

org.generate_historic_data(6)

org.pretty_print()