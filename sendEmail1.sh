#!/bin/bash

. /u01/oracle/Oracle/Middleware/Oracle_Home/oracle_common/common/bin/setWlstEnv.sh

SCRIPT_HOME=/u01/mazahir/scripts/serverStatus

cd $SCRIPT_HOME
# Run the WLST script to get server status and write to the temporary file
java weblogic.WLST serverStatus1.py

serverCount="4"

statusCount=`cat server_status.txt | grep -o RUNNING | wc -l`

if [ $serverCount != $statusCount ] ; then
echo "Server Status" | mail -s "Server Status" sendmailfromlinux@gmail.com < server_status.txt
fi
