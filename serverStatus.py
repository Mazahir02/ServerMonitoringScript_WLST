# Function to connect to the server
connect()

# Get a list of servers in the current domain
servers = cmo.getServers()

# Print a header for domain status
print "-------------------------------------------------------"
print "\t" + cmo.getName() + " domain status"
print "-------------------------------------------------------"

# Loop through each server and display its status
for server in servers:
    # Function to display the state of a server with its name and type
    state(server.getName(), server.getType())

# Print a footer after displaying all server statuses
print "-------------------------------------------------------"
