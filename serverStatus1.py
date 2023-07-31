# get_server_status.py
# WLST script to get server status

# Function to get the state of a server
def get_server_state(server_name):
    try:
        domainRuntime()
        server = getMBean('/ServerRuntimes/' + server_name)
        server_state = server.getState()
        return server_name + " state: " + server_state
    except:
        return server_name + " state: Not Reachable"

# Function to check server status
def get_server_status():
    output = "-------------------------------------------------------\n"
    output += "\t" + cmo.getName() + " domain status\n"
    output += "-------------------------------------------------------\n"

    servers = cmo.getServers()
    for server in servers:
        output += get_server_state(server.getName()) + "\n"

    output += "-------------------------------------------------------\n"
    return output

# Connect to the WebLogic Server
connect()

# Get server status
server_status_output = get_server_status()

# Disconnect from the WebLogic Server
disconnect()

# Write the server status output to a temporary file
file = open('server_status.txt', 'w')
file.write(server_status_output)
file.close()
