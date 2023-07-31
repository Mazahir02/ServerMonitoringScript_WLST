#!/bin/bash

. /u01/oracle/Oracle/Middleware/Oracle_Home/oracle_common/common/bin/setWlstEnv.sh

SCRIPT_HOME=/u01/mazahir/scripts/serverStatus

cd $SCRIPT_HOME

# Run the WLST script to get server status and write to the temporary file
java weblogic.WLST serverStatus1.py

echo "Server Status" | mail -s "Server Status" sendmailfromlinux@gmail.com < server_status.txt
