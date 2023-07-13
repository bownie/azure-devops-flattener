from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
from configparser import ConfigParser

# config
config = ConfigParser()
config.read('user.ini')

# Fill in with your personal access token and org URL
personal_access_token = config.get('section_main', 'PAT')
organization_url = config.get('section_main', 'ADO_URL')

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

project_collections = core_client.get_project_collections()

# Get the first page of projects
get_projects_response = core_client.get_projects()
get_teams_response = core_client.get_all_teams()

for project in get_projects_response:
    pprint.pprint("Project = " + project.name + " (id = " + project.id + ")")

    #project_stuff = core_client.get_project(project.id)
    #pprint.pprint(project_stuff)

    for team in get_teams_response:
        pprint.pprint("Team = " + team.name + " (id = " + team.id + ")")

        connected_services = core_client.get_connected_services(project.id)
        #team_members = core_client.get_team_members_with_extended_properties(project.id, team.id)

        pprint.pprint(connected_services)


