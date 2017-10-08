from oauth2client.client import flow_from_clientsecrets

flow = flow_from_clientsecrets('oura_client_secrets.json',
                               redirect_uri='http://example.com/auth_return')