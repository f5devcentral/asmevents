#!/usr/bin/python

import math
import argparse
import sys
import getpass
import requests
import json
import socket

from tabulate import tabulate


parser = argparse.ArgumentParser(
    prog='asmevents',
    usage='\n\n \
Few examples\n \
Display All events                           : # asmevents --host x.x.x.x -u <username> \n \
Display only blocked events                  : # asmevents --host x.x.x.x -s blocked -u <username> \n \
Display only legal events                    : # asmevents --host x.x.x.x -s legal -u <username>\n',
            description='Display ASM events', 
            epilog=' ', 
            add_help=True,
            )

parser.add_argument('--host', nargs='?', const=-1, help='set host with value')
parser.add_argument('-u', '--user', nargs='?', const=-1, help='set user with value', default='None')
parser.add_argument('-s', '--status', nargs='?', const=-1, choices=['legal', 'illegal', 'blocked', 'unblocked', 'challenged', 'all'], help='set the status of the operation', default='None')
parser.add_argument('-rq', action='store_true', help='when set, print raw request data', default=False)

args = parser.parse_args()

def is_valid_hostname_or_ip(host):
    try:
        socket.getaddrinfo(host, None)
        return True
    except socket.gaierror:
        return False

if args.status == "None":
    print("The status is set to all if -s isn't used; to pull specific status records, use the flag -s or --status")
    args.status = "all"
else:
    pass

if args.host:
    if is_valid_hostname_or_ip(args.host):
        pass
    else:
        print("The host is set incorrectlly, please provide correct host using --host flag")
        sys.exit()
else:
    print("The host is not set, please provide the host using --host flag")
    sys.exit()

if args.user == "None":
    args.user = "admin"
    print("The user is set to default GUI admin, to use different username use the flag -u or --user")
else:
    pass

# Define ASM REST API endpoint and credentials
asm_url = args.host
username = args.user

# prompt the user to enter the password and hide the value
if args.host and args.user:
    password = getpass.getpass(prompt='Enter password for the user ' + args.user + ': ')
else:
    sys.exit()

if args.status == "all":
    #Send GET request to ASM REST API to total number of event log
    requests.packages.urllib3.disable_warnings()
    stage = requests.get(f"https://{asm_url}/mgmt/tm/asm/events/requests", auth=(username, password), verify=False)
    # Parse response JSON
    p_stage = json.loads(json.dumps(stage.json()))
    # Pull total number of events
    real_total_events = p_stage["totalItems"]
    total_events = math.ceil(p_stage["totalItems"]/ 500) * 500
    # Create an empty list to store the events
    event_list = []
    # Iterate through events to find the requested event action 
    i = 0
    while i <= total_events:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(f"https://{asm_url}/mgmt/tm/asm/events/requests?$skip={i}&top=500", auth=(username, password), verify=False)
        # Parse response JSON
        events = json.loads(json.dumps(response.json()))
        for x in range(len(events["items"])):
            try:
                if args.rq is True:
                    event_list.append([events["items"][x]["id"],events["items"][x]["clientIp"],events["items"][x]["serverIp"],events["items"][x]["protocolInfo"],events["items"][x]["clientPort"],events["items"][x]["serverPort"],events["items"][x]["requestStatus"],events["items"][x]["rawRequest"]["httpRequestUnescaped"]])
                else:
                    event_list.append([events["items"][x]["id"],events["items"][x]["clientIp"],events["items"][x]["serverIp"],events["items"][x]["protocolInfo"],events["items"][x]["clientPort"],events["items"][x]["serverPort"],events["items"][x]["requestStatus"]])
            except Exception as e:
                pass
        i +=500
else:
    #Send GET request to ASM REST API to total number of event log specified in args.status
    requests.packages.urllib3.disable_warnings()
    stage = requests.get(f"https://{asm_url}/mgmt/tm/asm/events/requests?$filter=requestStatus+eq+{args.status}", auth=(username, password), verify=False)
    # Parse response JSON
    p_stage = json.loads(json.dumps(stage.json()))
    # Pull total number of events
    real_total_events = p_stage["totalItems"]
    total_events = math.ceil(p_stage["totalItems"]/ 500) * 500
    # Create an empty list to store the events
    event_list = []
    # Iterate through events to find the requested event action 
    i = 0
    while i <= total_events:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(f"https://{asm_url}/mgmt/tm/asm/events/requests?$skip={i}&top=500&$filter=requestStatus+eq+{args.status}", auth=(username, password), verify=False)
        # Parse response JSON
        events = json.loads(json.dumps(response.json()))
        for x in range(len(events["items"])):
            try:
                if args.rq is True:
                    event_list.append([events["items"][x]["id"],events["items"][x]["clientIp"],events["items"][x]["serverIp"],events["items"][x]["protocolInfo"],events["items"][x]["clientPort"],events["items"][x]["serverPort"],events["items"][x]["requestStatus"],events["items"][x]["rawRequest"]["httpRequestUnescaped"]])
                else:
                    event_list.append([events["items"][x]["id"],events["items"][x]["clientIp"],events["items"][x]["serverIp"],events["items"][x]["protocolInfo"],events["items"][x]["clientPort"],events["items"][x]["serverPort"],events["items"][x]["requestStatus"]])
            except Exception as e:
                pass
        i +=500

# Print the event list in tabular format
headers = ["Event ID", "Source IP", "Destination IP", "Protocol", "Source Port", "Destination Port", "Request Status", "Raw Request"]
print(tabulate(event_list, headers, tablefmt="fancy_grid"))
