# asmevents

This script is to retrieve events from an ASM (Application Security Manager) device.

### Current Version

1.0 released on 24th Jan 2023

## Usage

```bash
Few examples
Display All events                           : # asmevents --host x.x.x.x -u <username> 
Display only blocked events                  : # asmevents --host x.x.x.x -s blocked -u <username> 
Display only legal events                    : # asmevents --host x.x.x.x -s legal -u <username>
```

## Arguments
* `--host` : The IP address or hostname of the ASM device.
* `-u`, `--user` : The username to use for authentication.
* `-s`, `--status` : The status of events to retrieve. Choices are: "legal", "illegal", "blocked", "unblocked", "challenged", "all".
* `-rq` : When set, print raw request data.

## Notes
* If the `--host` argument is not provided, the script will exit with an error message.
* If the `-u` or `--user` argument is not provided, the script will use the default value of "admin".
* If the `-s` or `--status` argument is not provided, the script will retrieve all events.
* If the `-rq` argument is not provided, the script won't retrieve raw requsets data.

## Usage examples

#### Without defining arguments
```bash
python3 asmevents.py --host lab.es.com        
The status is set to all if -s isn't used; to pull specific status records, use the flag -s or --status
The user is set to default GUI admin, to use different username use the flag -u or --user
Enter password for the user admin: 
╒═════════════════════╤═════════════╤══════════════════╤════════════╤═══════════════╤════════════════════╤══════════════════╕
│            Event ID │ Source IP   │ Destination IP   │ Protocol   │   Source Port │   Destination Port │ Request Status   │
╞═════════════════════╪═════════════╪══════════════════╪════════════╪═══════════════╪════════════════════╪══════════════════╡
│ 9855905000251722760 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         50482 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722752 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         54136 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722744 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         50640 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722736 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         39570 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722690 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         47818 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722728 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         56062 │                 80 │ blocked          │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┤
│ 9855905000251722682 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         57072 │                 80 │ blocked          │
╘═════════════════════╧═════════════╧══════════════════╧════════════╧═══════════════╧════════════════════╧══════════════════╛
```
#### With -rq argument
```bash
python3 asmevents.py --host lab.es.com -rq
The status is set to all if -s isn't used; to pull specific status records, use the flag -s or --status
The user is set to default GUI admin, to use different username use the flag -u or --user
Enter password for the user admin: 

╒═════════════════════╤═════════════╤══════════════════╤════════════╤═══════════════╤════════════════════╤══════════════════╤═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╕
│            Event ID │ Source IP   │ Destination IP   │ Protocol   │   Source Port │   Destination Port │ Request Status   │ Raw Request                                                                                                                                     │
╞═════════════════════╪═════════════╪══════════════════╪════════════╪═══════════════╪════════════════════╪══════════════════╪═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
│ 9855905000251722760 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         50482 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722752 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         54136 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722744 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         50640 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722736 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         39570 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722690 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         47818 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722728 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         56062 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
├─────────────────────┼─────────────┼──────────────────┼────────────┼───────────────┼────────────────────┼─────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9855905000251722682 │ 10.1.29.1   │ 10.1.156.207     │ HTTP/1.1   │         57072 │                 80 │ blocked          │ GET / HTTP/1.1                                                                                                                                  │
│                     │             │                  │            │               │                    │                  │ Host: 209.71.214.63                                                                                                                             │
│                     │             │                  │            │               │                    │                  │ Connection: keep-alive                                                                                                                          │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"                                                                    │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-mobile: ?1                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ sec-ch-ua-platform: "Android"                                                                                                                   │
│                     │             │                  │            │               │                    │                  │ Upgrade-Insecure-Requests: 1                                                                                                                    │
│                     │             │                  │            │               │                    │                  │ User-Agent: Mozilla/5.0 (Linux; Android 13; SM-A715W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36              │
│                     │             │                  │            │               │                    │                  │ Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Site: none                                                                                                                            │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Mode: navigate                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-User: ?1                                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Sec-Fetch-Dest: document                                                                                                                        │
│                     │             │                  │            │               │                    │                  │ Accept-Encoding: gzip, deflate, br                                                                                                              │
│                     │             │                  │            │               │                    │                  │ Accept-Language: fr-CA,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6                                                                                │
╘═════════════════════╧═════════════╧══════════════════╧════════════╧═══════════════╧════════════════════╧══════════════════╧═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╛
```
