import pprint
from configparser import ConfigParser
from azure.devops.v7_1.work import TeamContext 
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# config
config = ConfigParser()
config.read('user.ini')

# Fill in with your personal access token and org URL
personal_access_token = config.get('section_main', 'PAT')
organization_url = config.get('section_main', 'ADO_URL')

pprint.pprint("ADO_URL = " + organization_url)

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# set up the clients
core_client = connection.clients.get_core_client()
work_item_tracking_client = connection.clients.get_work_item_tracking_client()
feature_management_client = connection.clients.get_feature_management_client()
work_client = connection.clients.get_work_client()

project_collections = core_client.get_project_collections()

# Get the first page of projects
get_projects_response = core_client.get_projects()
get_teams_response = core_client.get_all_teams()

for project in get_projects_response:
    pprint.pprint("Project = " + project.name + " (id = " + project.id + ")")

    for team in get_teams_response:
        pprint.pprint("Team = " + team.name + " (id = " + team.id + ")")

        team_context =  TeamContext(project.name, project.id, team.name, team.id)

        try:
            backlog_configuration = work_client.get_backlog_configurations(team_context)
            pprint.pprint("    " + backlog_configuration)
        except:
            pprint.pprint("  Can't get Backlog Configuration: no permission")

        for work_item_type in work_item_tracking_client.get_work_item_types(project.id):
            print("  Work Item Type = " + work_item_type.name +
                  " (ref name = " + work_item_type.reference_name + ")")
            