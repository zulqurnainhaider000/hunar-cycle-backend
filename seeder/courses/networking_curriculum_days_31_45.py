"""
Computer Networking Basics 60-Day Curriculum - Part 3 (Days 31 to 45)
Module 6: Core Network Services & Protocols (Days 31-37)
Module 7: Wireless & WAN Technologies (Days 38-45)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_45 = [
    # -------------------------------------------------------------
    # DAY 31
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Port Numbers (Well-Known, Registered & Ephemeral)",
        concept="Demultiplexing network traffic at Layer 4: 16-bit port spaces, Sockets (IP:Port), Well-Known ports (0-1023), Registered ports (1024-49151), and Ephemeral ports",
        analogy="Think of an IP address like the street address of a giant apartment high-rise building with 65,535 individual apartments inside. If mail arrives addressed only to 'Building 192.168.1.1', the mail carrier doesn't know who gets it. The **Port Number** is the exact apartment unit number! Apartment 80 is the Web Restaurant (HTTP), Apartment 443 is the Secure Vault (HTTPS), and Apartment 22 is the Security Guard Office (SSH)!",
        theory_sections=[
            {
                "heading": "The 16-bit Port Number Architecture",
                "body": "Transport protocols (TCP and UDP) use 16-bit port numbers (ranging from 0 to 65,535) to direct incoming network packets to the exact software application process intended on the host (**Demultiplexing**). An IP address combined with a Port number forms a unique **Socket** (e.g. `192.168.1.50:443`)."
            },
            {
                "heading": "The Three IANA Port Ranges",
                "body": "The Internet Assigned Numbers Authority (IANA) divides port numbers into three distinct tiers: (1) **Well-Known / System Ports (0 to 1023)**: Assigned to core privileged system services (e.g. HTTP 80, HTTPS 443, SSH 22, DNS 53); (2) **Registered Ports (1024 to 49151)**: Assigned to commercial software vendors (e.g. MySQL 3306, PostgreSQL 5432, RDP 3389); (3) **Dynamic / Ephemeral / Private Ports (49152 to 65535)**: Assigned temporarily by the client OS as source ports for outbound connections."
            }
        ],
        code_snippets=[
            {
                "title": "Essential Well-Known & Registered Ports Reference Table",
                "language": "text",
                "code": "Port #    Protocol    Layer 4     Full Service Name\n20 / 21   FTP         TCP         File Transfer Protocol (Data / Control)\n22        SSH         TCP         Secure Shell (Encrypted remote terminal)\n23        Telnet      TCP         Unencrypted remote terminal\n25        SMTP        TCP         Simple Mail Transfer Protocol (Outgoing email)\n53        DNS         UDP & TCP   Domain Name System (Name to IP resolution)\n67 / 68   DHCP        UDP         Dynamic Host Configuration Protocol\n80        HTTP        TCP         Hypertext Transfer Protocol (Unencrypted web)\n110       POP3        TCP         Post Office Protocol v3 (Email retrieval)\n123       NTP         UDP         Network Time Protocol (Clock synchronization)\n143       IMAP        TCP         Internet Message Access Protocol\n161       SNMP        UDP         Simple Network Management Protocol\n443       HTTPS       TCP         HTTP Secure (TLS/SSL encrypted web)\n3306      MySQL       TCP         MySQL Database Server\n3389      RDP         TCP         Microsoft Remote Desktop Protocol\n5432      PostgreSQL  TCP         PostgreSQL Database Server",
                "explanation": "Reference chart of common network port allocations across TCP and UDP."
            },
            {
                "title": "Inspecting Open Ports and Socket Bindings in Linux",
                "language": "bash",
                "code": "# Show all active TCP and UDP listening ports with process names\nsudo ss -tulnp\n\n# Or testing if port 443 is open on remote server using Netcat\nnc -zv api.github.com 443",
                "explanation": "CLI commands to inspect active sockets and test port connectivity across networks."
            },
            {
                "title": "Testing Remote Port Connectivity with PowerShell",
                "language": "powershell",
                "code": "# Test TCP port reachability on Windows (modern alternative to telnet)\nTest-NetConnection -ComputerName google.com -Port 443\n# TcpTestSucceeded : True",
                "explanation": "PowerShell command to verify whether a remote server port is accepting TCP handshakes."
            },
            {
                "title": "Python Port Range Classifier",
                "language": "python",
                "code": "def classify_port(port: int) -> str:\n    if not isinstance(port, int) or port < 0 or port > 65535:\n        return 'Invalid Port Number'\n    if port <= 1023:\n        return 'Well-Known (System) Port'\n    elif port <= 49151:\n        return 'Registered (User) Port'\n    else:\n        return 'Dynamic / Ephemeral (Private) Port'",
                "explanation": "Classifies an integer port into its IANA tier."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Service to Default Port Matcher",
            description="Write a Python function `get_default_port(service: str) -> int` that maps service names `'HTTP'`, `'HTTPS'`, `'SSH'`, `'DNS'`, and `'RDP'` to their default port numbers (80, 443, 22, 53, 3389). Return 0 for unknown services.",
            starter_code="def get_default_port(service: str) -> int:\n    # Return standard port number\n    pass",
            solution_code="def get_default_port(service: str) -> int:\n    mapping = {\n        'HTTP': 80,\n        'HTTPS': 443,\n        'SSH': 22,\n        'DNS': 53,\n        'RDP': 3389\n    }\n    return mapping.get(service.strip().upper(), 0)",
            expected_output="get_default_port('HTTPS') == 443, get_default_port('SSH') == 22, get_default_port('DNS') == 53"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the total number of port numbers available per transport protocol (TCP and UDP)?",
                options=[
                    "65,536 ports (0 to 65,535)",
                    "1,024 ports",
                    "256 ports",
                    "4.29 billion ports"
                ],
                correct_answer="65,536 ports (0 to 65,535)",
                explanation="Ports are represented by 16-bit fields in TCP and UDP headers (`2^16 = 65,536`)."
            ),
            QuizQuestionBlueprint(
                question="What IANA port range is reserved for 'Well-Known' standard system services (like HTTP, SSH, and DNS)?",
                options=[
                    "Ports 0 to 1023",
                    "Ports 1024 to 49151",
                    "Ports 49152 to 65535",
                    "Ports 8000 to 9000"
                ],
                correct_answer="Ports 0 to 1023",
                explanation="Ports 0 to 1023 are Well-Known ports assigned to core infrastructure services."
            ),
            QuizQuestionBlueprint(
                question="What is an 'Ephemeral Port' in client-server networking?",
                options=[
                    "A short-lived dynamic source port (49152-65535) chosen automatically by the client OS to track an outbound request session",
                    "A port that deletes hard drive files",
                    "A port reserved exclusively for printers",
                    "A port that only works without electricity"
                ],
                correct_answer="A short-lived dynamic source port (49152-65535) chosen automatically by the client OS to track an outbound request session",
                explanation="Ephemeral ports are dynamically assigned by the OS as source ports for return traffic."
            ),
            QuizQuestionBlueprint(
                question="What standard TCP port is used for secure encrypted web traffic over HTTPS?",
                options=[
                    "Port 443",
                    "Port 80",
                    "Port 22",
                    "Port 53"
                ],
                correct_answer="Port 443",
                explanation="HTTPS runs over TCP port 443 with TLS/SSL encryption."
            ),
            QuizQuestionBlueprint(
                question="What is the combination of an IP address and a Port number called (e.g. `192.168.1.50:22`)?",
                options=[
                    "A Network Socket",
                    "A Subnet Mask",
                    "A MAC address",
                    "A VLAN Tag"
                ],
                correct_answer="A Network Socket",
                explanation="The combination of an IP address and a port number forms a network socket."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: DHCP (Dynamic Host Configuration Protocol & DORA)",
        concept="Automating network configuration: The 4-step DORA process (Discover, Offer, Request, Acknowledge), DHCP leases, scope options, and DHCP Relay Agents",
        analogy="Think of DHCP like checking into a luxury hotel. When you walk into the lobby with no room, you shout into the room: 'Does anyone have an open room?!' (**DHCP Discover** - Broadcast). The front desk clerk smiles and says: 'I have Room 304 available with ocean view and keycard' (**DHCP Offer** - Unicast). You say: 'Great, I will take Room 304!' (**DHCP Request**). The clerk stamps your passport: 'Room 304 is officially yours for 3 days!' (**DHCP Acknowledge** - Lease).",
        theory_sections=[
            {
                "heading": "The 4-Step DORA Process",
                "body": "DHCP (RFC 2131) operates via UDP ports 67 (Server) and 68 (Client) using the **DORA** sequence: (1) **Discover**: Client with IP `0.0.0.0` broadcasts to `255.255.255.255` searching for a DHCP server; (2) **Offer**: DHCP server reserves an IP and unicasts/broadcasts an offer with subnet mask, gateway, and lease duration; (3) **Request**: Client formally requests the offered IP; (4) **Acknowledge (ACK)**: Server commits the lease in its database and confirms configuration to the client."
            },
            {
                "heading": "DHCP Options & The IP Helper-Address (Relay Agent)",
                "body": "A DHCP server provides more than just an IP: it pushes **DHCP Options** including Default Gateway (Option 3), DNS Servers (Option 6), and Domain Name (Option 15). Because routers do not forward Layer 2 broadcast Discover packets, a router interface connected to a remote LAN must be configured with `ip helper-address <dhcp_server_ip>` (**DHCP Relay Agent**) to convert broadcasts into unicast packets routed to the central server."
            }
        ],
        code_snippets=[
            {
                "title": "The 4-Step DORA Message Exchange Protocol",
                "language": "text",
                "code": "Client (Port 68)                                   DHCP Server (Port 67)\n  │                                                          │\n  │ ── 1. DHCP Discover (Src: 0.0.0.0, Dst: 255.255.255.255) ─> │ (Broadcast on LAN)\n  │                                                          │\n  │ <── 2. DHCP Offer (Offered IP: 192.168.1.100, Mask, GW) ─│ (Server reserves IP)\n  │                                                          │\n  │ ── 3. DHCP Request (Accepting 192.168.1.100) ───────────> │ (Broadcast approval)\n  │                                                          │\n  │ <── 4. DHCP ACK (Lease committed: 8 Days) ───────────────│ (Client configures NIC)",
                "explanation": "Protocol diagram showing the 4-step DORA message exchange between client and DHCP server."
            },
            {
                "title": "Configuring a DHCP Server Pool on a Cisco Router",
                "language": "text",
                "code": "-- Step 1: Exclude statically assigned server and printer IPs\nRouter(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.20\n\n-- Step 2: Create and configure DHCP Pool\nRouter(config)# ip dhcp pool LAN_CLIENTS\nRouter(dhcp-config)# network 192.168.1.0 255.255.255.0\nRouter(dhcp-config)# default-router 192.168.1.1      -- Option 3 (Gateway)\nRouter(dhcp-config)# dns-server 8.8.8.8 1.1.1.1     -- Option 6 (DNS)\nRouter(dhcp-config)# domain-name hunar.internal      -- Option 15\nRouter(dhcp-config)# lease 7                         -- Lease duration 7 days",
                "explanation": "Configures an embedded DHCP server pool with scope, exclusions, gateway, and DNS options."
            },
            {
                "title": "Configuring DHCP Relay Agent (ip helper-address)",
                "language": "text",
                "code": "-- On Router interface receiving client DHCP broadcasts:\nRouter(config)# interface GigabitEthernet0/0/1\nRouter(config-if)# description Client-LAN-Interface\nRouter(config-if)# ip helper-address 10.50.1.100\n# Forwards incoming UDP 67/68 broadcasts as UNICAST packets directly to 10.50.1.100!",
                "explanation": "Converts local client broadcast Discover packets into routed unicast packets destined for a central server."
            },
            {
                "title": "Releasing and Renewing DHCP Leases in Windows & Linux",
                "language": "bash",
                "code": "# Windows:\nipconfig /release\nipconfig /renew\n\n# Linux (dhclient):\nsudo dhclient -r eth0  # Release lease\nsudo dhclient eth0     # Request fresh DORA lease",
                "explanation": "Commands to release and renew IP configuration from the DHCP server."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DORA Acronym Sequence Validator",
            description="Write a Python function `is_valid_dora_step(step_number: int, message_name: str) -> bool` that verifies whether steps 1, 2, 3, and 4 correspond to `'DISCOVER'`, `'OFFER'`, `'REQUEST'`, and `'ACKNOWLEDGE'` (or `'ACK'`).",
            starter_code="def is_valid_dora_step(step_number: int, message_name: str) -> bool:\n    # Verify DORA sequence\n    pass",
            solution_code="def is_valid_dora_step(step_number: int, message_name: str) -> bool:\n    m = message_name.strip().upper()\n    dora = {1: 'DISCOVER', 2: 'OFFER', 3: 'REQUEST', 4: 'ACKNOWLEDGE'}\n    if step_number == 4 and m == 'ACK':\n        return True\n    return dora.get(step_number) == m",
            expected_output="is_valid_dora_step(1, 'Discover') == True, is_valid_dora_step(2, 'Request') == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the correct 4-step sequence of messages exchanged during a DHCP address lease acquisition?",
                options=[
                    "DORA: Discover -> Offer -> Request -> Acknowledge (ACK)",
                    "DORA: Deliver -> Open -> Receive -> Accept",
                    "SYN -> SYN-ACK -> ACK -> FIN",
                    "Ping -> ARP -> Route -> Connect"
                ],
                correct_answer="DORA: Discover -> Offer -> Request -> Acknowledge (ACK)",
                explanation="DORA represents the four message stages: Discover, Offer, Request, and Acknowledgment."
            ),
            QuizQuestionBlueprint(
                question="What transport layer protocol and UDP ports are used by DHCP communication?",
                options=[
                    "UDP Port 67 (Server) and UDP Port 68 (Client)",
                    "TCP Port 80 and TCP Port 443",
                    "TCP Port 22 and Port 23",
                    "UDP Port 53"
                ],
                correct_answer="UDP Port 67 (Server) and UDP Port 68 (Client)",
                explanation="DHCP communicates over UDP: servers listen on port 67, and clients receive on port 68."
            ),
            QuizQuestionBlueprint(
                question="Why is the `ip helper-address` command required on a router interface when the DHCP server is on a different subnet?",
                options=[
                    "Because routers do not forward Layer 2 broadcast Discover frames by default; the helper-address converts them to routed unicast",
                    "Because routers cannot assign IP addresses",
                    "Because DHCP only works over satellite",
                    "To encrypt the password"
                ],
                correct_answer="Because routers do not forward Layer 2 broadcast Discover frames by default; the helper-address converts them to routed unicast",
                explanation="DHCP Discover broadcasts cannot cross routers without a relay agent (`ip helper-address`)."
            ),
            QuizQuestionBlueprint(
                question="What source IP address does an unconfigured client computer use when sending an initial DHCP Discover packet?",
                options=[
                    "0.0.0.0",
                    "255.255.255.255",
                    "127.0.0.1",
                    "192.168.1.1"
                ],
                correct_answer="0.0.0.0",
                explanation="A client with no assigned IP uses `0.0.0.0` as its source IP during initial discovery."
            ),
            QuizQuestionBlueprint(
                question="What DHCP scope option number distributes the Default Gateway IP address to connecting clients?",
                options=[
                    "DHCP Option 3",
                    "DHCP Option 6 (DNS)",
                    "DHCP Option 15 (Domain Name)",
                    "DHCP Option 100"
                ],
                correct_answer="DHCP Option 3",
                explanation="DHCP Option 3 defines the Default Router / Gateway IP for the subnet."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: DNS (Domain Name System & Record Types)",
        concept="The phonebook of the Internet: Hierarchical namespace (Root, TLD, Authoritative), Recursive vs Iterative queries, and DNS Record Types (A, AAAA, CNAME, MX, TXT, NS, PTR, SOA)",
        analogy="Think of the Domain Name System (DNS) like the contact directory on your smartphone. Humans are great at remembering names like 'Mom' or 'Pizza Hut' (**Domain Names: google.com**). But telephone cell towers and routers can only dial digits (**IP Addresses: 142.250.190.46**). When you tap 'Mom', your phone transparently converts the name to a 10-digit number. DNS is that global distributed phonebook translating human names into computer IP numbers in 15 milliseconds!",
        theory_sections=[
            {
                "heading": "The Hierarchical Tree Architecture",
                "body": "DNS operates as an inverted hierarchical tree: (1) **Root Domain (`.`)**: Managed by 13 root server clusters globally; (2) **Top-Level Domains (TLD)**: Generic TLDs (`.com`, `.org`) managed by registries like Verisign and country-code TLDs (`.pk`, `.uk`); (3) **Second-Level Domains**: Registered domain names (e.g. `hunar.app`); (4) **Subdomains / Hosts**: Individual services (e.g. `api.hunar.app`, `www.hunar.app`)."
            },
            {
                "heading": "Essential DNS Record Types",
                "body": "(1) **A Record**: Maps hostname to IPv4; (2) **AAAA Record**: Maps hostname to IPv6; (3) **CNAME (Canonical Name)**: Alias pointing one name to another; (4) **MX (Mail Exchange)**: Routes email to mail servers with priority; (5) **TXT**: Holds arbitrary text (SPF, DKIM, DMARC for email security); (6) **NS (Name Server)**: Delegates zone authority; (7) **PTR (Pointer)**: Reverse DNS mapping IP back to hostname."
            }
        ],
        code_snippets=[
            {
                "title": "Comprehensive DNS Record Types Summary Matrix",
                "language": "text",
                "code": "Record Type  Full Name                Points To                Example Entry\nA            Address Record (IPv4)    32-bit IPv4 Address      api.hunar.app.  IN  A      104.21.42.15\nAAAA         IPv6 Address Record      128-bit IPv6 Address     api.hunar.app.  IN  AAAA   2606:4700::6815:2a0f\nCNAME        Canonical Name (Alias)   Another Hostname         www.hunar.app.  IN  CNAME  hunar.app.\nMX           Mail Exchange            Mail Server + Priority   hunar.app.      IN  MX 10  mail.google.com.\nTXT          Text Record              Human/Machine Strings    hunar.app.      IN  TXT    \"v=spf1 include:_spf.google.com ~all\"\nNS           Name Server              Authoritative Server     hunar.app.      IN  NS     ns1.cloudflare.com.\nPTR          Pointer Record           Reverse DNS (IP -> Name) 15.42.21.104... IN  PTR    api.hunar.app.",
                "explanation": "Summary of common DNS resource records, targets, and practical use cases."
            },
            {
                "title": "Querying DNS Records with dig and nslookup",
                "language": "bash",
                "code": "# Query IPv4 'A' record using dig\ndig +short A google.com\n# 142.250.190.46\n\n# Query MX mail records using nslookup\nnslookup -type=MX google.com\n\n# Trace full recursive resolution path from Root (.) down to authoritative server\ndig +trace api.github.com",
                "explanation": "CLI tools for querying DNS records, testing resolution, and tracing hierarchical query paths."
            },
            {
                "title": "Local Host Resolution: The /etc/hosts File",
                "language": "bash",
                "code": "# OS checks local hosts file BEFORE querying remote DNS servers!\n# /etc/hosts (Linux/Mac) or C:\\Windows\\System32\\drivers\\etc\\hosts (Windows)\ncat /etc/hosts\n# 127.0.0.1   localhost\n# 192.168.1.50 staging.internal.server",
                "explanation": "Operating systems inspect the local hosts file prior to initiating network DNS queries."
            },
            {
                "title": "Python DNS Resolution Script (socket & dnspython)",
                "language": "python",
                "code": "import socket\n\ndef resolve_hostname(domain: str) -> dict:\n    try:\n        ipv4 = socket.gethostbyname(domain)\n        name, aliases, ip_list = socket.gethostbyname_ex(domain)\n        return {'domain': domain, 'primary_ip': ipv4, 'all_ips': ip_list}\n    except socket.gaierror as e:\n        return {'error': f'Resolution failed: {e}'}\n\nprint(resolve_hostname('cloudflare.com'))",
                "explanation": "Resolves domain names programmatically using standard Python networking libraries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DNS Record Type Query Formatter",
            description="Write a Python function `build_dig_command(domain: str, record_type: str = 'A', dns_server: str = '') -> str` that formats a valid `dig` CLI command. If `dns_server` is provided, prepend `@<server>`.",
            starter_code="def build_dig_command(domain: str, record_type: str = 'A', dns_server: str = '') -> str:\n    # Generate dig command string\n    pass",
            solution_code="def build_dig_command(domain: str, record_type: str = 'A', dns_server: str = '') -> str:\n    server_part = f\"@{dns_server.strip()} \" if dns_server and dns_server.strip() else \"\"\n    return f\"dig {server_part}{domain.strip()} {record_type.strip().upper()}\"",
            expected_output="build_dig_command('google.com', 'MX') == 'dig google.com MX', build_dig_command('google.com', 'A', '8.8.8.8') == 'dig @8.8.8.8 google.com A'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which DNS record type maps a human-readable domain name directly to a 32-bit IPv4 address?",
                options=[
                    "A Record",
                    "AAAA Record",
                    "CNAME Record",
                    "MX Record"
                ],
                correct_answer="A Record",
                explanation="The 'A' (Address) record maps hostnames to IPv4 addresses."
            ),
            QuizQuestionBlueprint(
                question="Which DNS record type is used to map an IPv6 address to a domain name?",
                options=[
                    "AAAA Record (Quad-A)",
                    "A Record",
                    "PTR Record",
                    "TXT Record"
                ],
                correct_answer="AAAA Record (Quad-A)",
                explanation="AAAA (Quad-A) records map hostnames to 128-bit IPv6 addresses."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of an 'MX' (Mail Exchange) record?",
                options=[
                    "It directs inbound email for a domain to the designated mail server hostnames, ordered by priority",
                    "It speeds up video streaming",
                    "It assigns MAC addresses to computers",
                    "It creates wireless connections"
                ],
                correct_answer="It directs inbound email for a domain to the designated mail server hostnames, ordered by priority",
                explanation="MX records identify mail servers responsible for accepting incoming emails for that domain."
            ),
            QuizQuestionBlueprint(
                question="What transport layer protocol and port number does standard DNS query resolution use by default?",
                options=[
                    "UDP Port 53",
                    "TCP Port 80",
                    "UDP Port 67",
                    "TCP Port 443"
                ],
                correct_answer="UDP Port 53",
                explanation="Standard DNS queries use lightweight UDP port 53; TCP 53 is used for zone transfers or large responses."
            ),
            QuizQuestionBlueprint(
                question="What is a 'CNAME' (Canonical Name) record used for in DNS?",
                options=[
                    "Creating an alias that points one domain name to another domain name (e.g. `www.example.com` -> `example.com`)",
                    "Encrypting credit cards",
                    "Setting the computer time clock",
                    "Deleting old domains"
                ],
                correct_answer="Creating an alias that points one domain name to another domain name (e.g. `www.example.com` -> `example.com`)",
                explanation="A CNAME record aliases one hostname to another canonical hostname."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: NAT & PAT (Network Address Translation & Overload)",
        concept="Bridging private and public IP realms: Static NAT, Dynamic NAT, PAT (Port Address Translation / NAT Overload), and the NAT translation table",
        analogy="Think of Port Address Translation (PAT) like the front desk of a busy international hotel with 500 guests but only ONE single official outside telephone line. When Guest in Room 201 calls London, the hotel switchboard puts the call through on the main telephone line, but tags the call on internal channel #5001. When London answers, the switchboard looks at channel #5001 (**Source Port**) and routes the voice directly back to Room 201. All 500 guests share one phone number simultaneously!",
        theory_sections=[
            {
                "heading": "The Three Types of NAT",
                "body": "(1) **Static NAT (1:1)**: Maps one private IP permanently to one public IP (used for hosting internal web servers accessible to the Internet); (2) **Dynamic NAT (M:N)**: Maps private IPs to a shared pool of public IPs on a first-come, first-served basis; (3) **PAT (Port Address Translation / NAT Overload)**: Maps thousands of private IPs to a **single public IP** by assigning unique Layer 4 source port numbers. PAT is universally deployed on all home Wi-Fi routers and enterprise firewalls."
            },
            {
                "heading": "Inside vs Outside NAT Terminology",
                "body": "Cisco defines four NAT address types: (1) **Inside Local**: The private IP assigned to an internal host (e.g. `192.168.1.50`); (2) **Inside Global**: The public IP representing the internal host to the outside world; (3) **Outside Local**: The IP of the external host as seen by internal hosts; (4) **Outside Global**: The true public IP assigned to the external host."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Port Address Translation (PAT / NAT Overload) on Cisco Router",
                "language": "text",
                "code": "-- Step 1: Define internal interface and external Internet interface\nRouter(config)# interface GigabitEthernet0/0/0\nRouter(config-if)# ip address 192.168.1.1 255.255.255.0\nRouter(config-if)# ip nat inside\n\nRouter(config)# interface GigabitEthernet0/0/1\nRouter(config-if)# ip address 203.0.113.1 255.255.255.0\nRouter(config-if)# ip nat outside\n\n-- Step 2: Define Standard ACL identifying private hosts permitted to be translated\nRouter(config)# access-list 1 permit 192.168.1.0 0.0.0.255\n\n-- Step 3: Activate NAT Overload (PAT) on the outside exit interface\nRouter(config)# ip nat inside source list 1 interface GigabitEthernet0/0/1 overload",
                "explanation": "Configures PAT/Overload, allowing the entire private LAN to share the public IP of interface Gi0/0/1."
            },
            {
                "title": "Configuring Static 1:1 NAT for an Internal Web Server",
                "language": "text",
                "code": "-- Maps public IP 203.0.113.10 permanently to private server 192.168.1.100\nRouter(config)# ip nat inside source static 192.168.1.100 203.0.113.10",
                "explanation": "Static 1:1 NAT allows external Internet users to reach an internal private web server."
            },
            {
                "title": "Inspecting the Active NAT Translation Table",
                "language": "text",
                "code": "Router# show ip nat translations\nPro  Inside global         Inside local          Outside local        Outside global\ntcp  203.0.113.1:10521     192.168.1.50:54321    142.250.190.46:443   142.250.190.46:443\ntcp  203.0.113.1:10522     192.168.1.60:49180    151.101.1.140:80     151.101.1.140:80\n# Notice unique source port mappings (10521 vs 10522) distinguishing internal hosts!",
                "explanation": "Shows the dynamic NAT state table matching private socket connections to translated public ports."
            },
            {
                "title": "Clearing Dynamic NAT Table Entries",
                "language": "text",
                "code": "Router# clear ip nat translation *\n# Clears dynamic translation entries from router RAM during troubleshooting",
                "explanation": "Flushes dynamic NAT state records to reset connections during network testing."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="NAT Address Terminology Classifier",
            description="Write a Python function `classify_nat_term(is_inside: bool, is_local: bool) -> str` that returns `'Inside Local'`, `'Inside Global'`, `'Outside Local'`, or `'Outside Global'` based on boolean parameters.",
            starter_code="def classify_nat_term(is_inside: bool, is_local: bool) -> str:\n    # Return proper Cisco NAT terminology\n    pass",
            solution_code="def classify_nat_term(is_inside: bool, is_local: bool) -> str:\n    realm = 'Inside' if is_inside else 'Outside'\n    loc = 'Local' if is_local else 'Global'\n    return f\"{realm} {loc}\"",
            expected_output="classify_nat_term(True, True) == 'Inside Local', classify_nat_term(True, False) == 'Inside Global'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between standard NAT and PAT (Port Address Translation / NAT Overload)?",
                options=[
                    "PAT maps thousands of private IP addresses to a single public IP by tracking unique Layer 4 source port numbers; basic NAT requires a 1:1 IP ratio",
                    "PAT only works on optical fiber",
                    "Basic NAT is faster than light",
                    "PAT was invented for satellite TV"
                ],
                correct_answer="PAT maps thousands of private IP addresses to a single public IP by tracking unique Layer 4 source port numbers; basic NAT requires a 1:1 IP ratio",
                explanation="PAT multiplexes multiple private IPs over a single public address using port translation."
            ),
            QuizQuestionBlueprint(
                question="In Cisco NAT terminology, what is an 'Inside Local' address?",
                options=[
                    "The private IPv4 address assigned to a host computer on the internal private LAN",
                    "The public IP of Google",
                    "The MAC address of the printer",
                    "The Wi-Fi password"
                ],
                correct_answer="The private IPv4 address assigned to a host computer on the internal private LAN",
                explanation="Inside Local refers to the private IP assigned to an internal host within the local LAN."
            ),
            QuizQuestionBlueprint(
                question="What keyword is added to the Cisco IOS `ip nat inside source list ...` command to activate Port Address Translation (PAT)?",
                options=[
                    "overload",
                    "pat_enable",
                    "multiplex",
                    "share_all"
                ],
                correct_answer="overload",
                explanation="The `overload` keyword tells Cisco IOS to use port translation on the designated interface."
            ),
            QuizQuestionBlueprint(
                question="What type of NAT is typically used when an organization needs to host a public web server with a private IP address inside their DMZ?",
                options=[
                    "Static 1:1 NAT",
                    "Dynamic NAT",
                    "PAT Overload",
                    "APIPA"
                ],
                correct_answer="Static 1:1 NAT",
                explanation="Static 1:1 NAT provides a permanent bidirectional mapping from a public IP to an internal private server."
            ),
            QuizQuestionBlueprint(
                question="What Cisco IOS command displays active live NAT connections currently undergoing translation in router memory?",
                options=[
                    "show ip nat translations",
                    "show nat all",
                    "display translation table",
                    "show ip routes"
                ],
                correct_answer="show ip nat translations",
                explanation="`show ip nat translations` prints the active session mapping table in router memory."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 35
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: ARP (Address Resolution Protocol & Gratuitous ARP)",
        concept="Bridging Layer 3 to Layer 2: How ARP maps IP addresses to physical MAC addresses, ARP Request broadcasts, ARP Reply unicasts, and Gratuitous ARP (GARP)",
        analogy="Think of ARP like being seated in a crowded conference lecture hall where you have a list of attendee names (**IP Addresses**), but you have no idea what anyone looks like (**MAC Addresses**). You need to give an envelope to 'Zainab'. You stand up and shout to the entire room (**ARP Request - Broadcast**): 'Who here is Zainab? Please tell me your seat number!' Zainab stands up and whispers directly to you (**ARP Reply - Unicast**): 'I am Zainab, I sit in Seat 4B!' You write that in your notebook (**ARP Cache**)!",
        theory_sections=[
            {
                "heading": "How Address Resolution Protocol (ARP) Works",
                "body": "Before a computer can encapsulate an IP packet into an Ethernet frame, it must discover the destination's Layer 2 MAC address. If the target MAC is not in its local **ARP Cache**, the host initiates ARP: (1) **ARP Request**: Broadcast frame (`FF:FF:FF:FF:FF:FF`) asking *'Who has IP 192.168.1.1? Tell 192.168.1.50'*; (2) **ARP Reply**: The owner of that IP responds with a unicast frame *'192.168.1.1 is at MAC 00:50:56:E8:11:02'*; (3) The sender saves this mapping in its ARP table with an expiration timer."
            },
            {
                "heading": "Gratuitous ARP (GARP) & ARP Spoofing Vulnerabilities",
                "body": "A **Gratuitous ARP (GARP)** is an unprompted ARP reply broadcasted by a host to announce its own IP/MAC mapping to the entire LAN. It is used to detect duplicate IP conflicts and update switch CAM tables upon high-availability failover. Because standard ARP lacks cryptographic authentication, it is vulnerable to **ARP Poisoning/Spoofing**, where attackers inject fake MAC mappings to intercept traffic (MITM)."
            }
        ],
        code_snippets=[
            {
                "title": "ARP Packet Structure Breakdown",
                "language": "text",
                "code": "Field                    Size        Value in Typical ARP Request\nHardware Type (HTYPE)    2 Bytes     0x0001 (Ethernet)\nProtocol Type (PTYPE)    2 Bytes     0x0800 (IPv4)\nHardware Address Length  1 Byte      6 (MAC length)\nProtocol Address Length  1 Byte      4 (IPv4 length)\nOpcode                   2 Bytes     1 = Request, 2 = Reply\nSender MAC Address       6 Bytes     00:1A:2B:3C:4D:5E (Client MAC)\nSender IP Address        4 Bytes     192.168.1.50\nTarget MAC Address       6 Bytes     00:00:00:00:00:00 (Unknown in Request)\nTarget IP Address        4 Bytes     192.168.1.1 (Target to resolve)",
                "explanation": "Field specifications for Address Resolution Protocol request and reply packets."
            },
            {
                "title": "Inspecting and Flushing ARP Cache on Windows and Linux",
                "language": "bash",
                "code": "# View ARP table\narp -a\n# or in modern Linux:\nip neigh show\n\n# Flush / Clear ARP cache (forces immediate re-resolution)\nsudo ip neigh flush all\n# or on Windows:\nnetsh interface ip delete arpcache",
                "explanation": "Commands to view and purge dynamic ARP cache entries."
            },
            {
                "title": "Inspecting Cisco Router ARP Table and Static ARP Entry",
                "language": "text",
                "code": "Router# show ip arp\nProtocol  Address          Age (min)  Hardware Addr   Type   Interface\nInternet  192.168.1.1             -   0014.2201.1111  ARPA   GigabitEthernet0/0/0\nInternet  192.168.1.50           12   0050.7966.6801  ARPA   GigabitEthernet0/0/0\n\n-- Create a static ARP binding for security\nRouter(config)# arp 192.168.1.100 0011.2233.4455 arpa",
                "explanation": "Views learned ARP entries and adds static bindings to thwart ARP poisoning."
            },
            {
                "title": "Simulating ARP Resolution in Python",
                "language": "python",
                "code": "class ArpTable:\n    def __init__(self):\n        self.cache = {}\n        \n    def resolve(self, target_ip: str, local_network_hosts: dict):\n        if target_ip in self.cache:\n            return self.cache[target_ip] # Cache Hit\n        # ARP Request Broadcast\n        for ip, mac in local_network_hosts.items():\n            if ip == target_ip:\n                self.cache[target_ip] = mac # Store ARP Reply\n                return mac\n        return None # Host Unreachable\n\narp = ArpTable()\nhosts = {'192.168.1.1': '00:50:56:e8:11:02'}\nprint('Resolved MAC:', arp.resolve('192.168.1.1', hosts))",
                "explanation": "Python simulation of ARP cache lookup and broadcast resolution."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="ARP Opcode Classifier",
            description="Write a Python function `get_arp_opcode_name(opcode: int) -> str` that maps opcode `1` to `'ARP Request'`, `2` to `'ARP Reply'`, `3` to `'RARP Request'`, and `4` to `'RARP Reply'`. Return `'Unknown'` for others.",
            starter_code="def get_arp_opcode_name(opcode: int) -> str:\n    # Return ARP opcode description\n    pass",
            solution_code="def get_arp_opcode_name(opcode: int) -> str:\n    mapping = {1: 'ARP Request', 2: 'ARP Reply', 3: 'RARP Request', 4: 'RARP Reply'}\n    return mapping.get(opcode, 'Unknown')",
            expected_output="get_arp_opcode_name(1) == 'ARP Request', get_arp_opcode_name(2) == 'ARP Reply'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary role of the Address Resolution Protocol (ARP) in IPv4 networking?",
                options=[
                    "To resolve a known Layer 3 IPv4 address to an unknown physical Layer 2 MAC address on the local network",
                    "To translate domain names to IP addresses",
                    "To assign IP addresses dynamically to hosts",
                    "To route packets between different cities"
                ],
                correct_answer="To resolve a known Layer 3 IPv4 address to an unknown physical Layer 2 MAC address on the local network",
                explanation="ARP maps known logical IP addresses to physical MAC hardware addresses."
            ),
            QuizQuestionBlueprint(
                question="What destination MAC address is used in an initial ARP Request frame?",
                options=[
                    "FF:FF:FF:FF:FF:FF (Broadcast)",
                    "00:00:00:00:00:00",
                    "The router's MAC address",
                    "The client's own MAC address"
                ],
                correct_answer="FF:FF:FF:FF:FF:FF (Broadcast)",
                explanation="ARP requests are broadcast (FF:FF:FF:FF:FF:FF) so all local nodes receive the query."
            ),
            QuizQuestionBlueprint(
                question="How does the target host reply to an ARP Request?",
                options=[
                    "Via a Unicast frame addressed directly to the sender's MAC address",
                    "Via another Broadcast to the entire network",
                    "By sending an email",
                    "By shutting down its network port"
                ],
                correct_answer="Via a Unicast frame addressed directly to the sender's MAC address",
                explanation="The ARP reply is unicast directly back to the requesting host's MAC address."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Gratuitous ARP' (GARP)?",
                options=[
                    "An unrequested ARP reply broadcast by a device to announce its IP/MAC mapping to the LAN and detect IP conflicts",
                    "A fee charged by the ISP for each ARP query",
                    "An error message sent when a cable is unplugged",
                    "A tool for deleting old routes"
                ],
                correct_answer="An unrequested ARP reply broadcast by a device to announce its IP/MAC mapping to the LAN and detect IP conflicts",
                explanation="Gratuitous ARP is an unprompted announcement updating local neighbor caches and checking for duplicate IPs."
            ),
            QuizQuestionBlueprint(
                question="What security vulnerability exploits the lack of authentication in ARP to execute Man-In-The-Middle (MITM) attacks?",
                options=[
                    "ARP Poisoning / ARP Spoofing",
                    "SYN Flood attack",
                    "Buffer Overflow",
                    "SQL Injection"
                ],
                correct_answer="ARP Poisoning / ARP Spoofing",
                explanation="ARP spoofing sends falsified ARP messages, associating the attacker's MAC with an authorized IP (e.g. gateway)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 36
    # -------------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: ICMP (Ping, Traceroute/Tracert & Path MTU)",
        concept="Network layer diagnostics: ICMP message types (Echo Request/Reply, Destination Unreachable, Time Exceeded), Ping latency, and how Traceroute uses TTL decrements",
        analogy="Think of ICMP like sending a sonar ping from a submarine or sending an exploratory scout into a deep cavern. **Ping** shouts into the cave: 'Echo!' (**Echo Request**), and listens for the sound bouncing off the back wall: 'Echo!' (**Echo Reply**) to calculate distance in milliseconds. **Traceroute** is sending a sequence of scouts with timers: Scout 1 has a 1-second timer (**TTL=1**), expiring at the first checkpoint; Scout 2 has a 2-second timer (**TTL=2**), expiring at the second checkpoint. You map out every step along the trail!",
        theory_sections=[
            {
                "heading": "The Purpose of ICMP (Internet Control Message Protocol)",
                "body": "Defined in RFC 792, ICMP operates at Layer 3 (encapsulated directly in IP packets with Protocol number 1). It is not designed to carry user application data; rather, it reports network transmission errors and diagnostics. Key ICMP Types: **Type 8** (Echo Request), **Type 0** (Echo Reply), **Type 3** (Destination Unreachable), and **Type 11** (Time Exceeded)."
            },
            {
                "heading": "How Traceroute / Tracert Works (TTL Manipulation)",
                "body": "Traceroute maps the exact hop-by-hop router path to a destination using IP Time-To-Live (TTL): (1) Sends packet with `TTL = 1`. The first router decrements TTL to 0, drops the packet, and returns an **ICMP Type 11 (Time Exceeded)** packet, revealing Router 1's IP; (2) Sends packet with `TTL = 2`, revealing Router 2's IP; (3) Continues incrementing TTL until the final target returns an ICMP Echo Reply or Port Unreachable."
            }
        ],
        code_snippets=[
            {
                "title": "Common ICMP Message Types and Codes",
                "language": "text",
                "code": "Type #  Code #  Name                         Description\n0       0       Echo Reply                   Ping successful response\n3       0       Net Unreachable              Router has no route to destination network\n3       1       Host Unreachable             Destination host not responding (ARP failure)\n3       3       Port Unreachable             Target UDP port is closed\n3       4       Fragmentation Needed (DF)    Packet exceeds MTU but DF bit is set\n8       0       Echo Request                 Ping outbound probe\n11      0       Time-to-Live Exceeded in Tx  Router decremented TTL to 0 (Traceroute hop)",
                "explanation": "Reference chart detailing ICMP types, codes, and operational triggers."
            },
            {
                "title": "Using Traceroute / Tracert CLI for Path Analysis",
                "language": "bash",
                "code": "# Linux / macOS (Sends UDP or ICMP probes)\ntraceroute 8.8.8.8\n\n# Windows (Sends ICMP Echo Requests)\ntracert 8.8.8.8\n# 1   <1 ms    <1 ms    <1 ms  192.168.1.1 (Local Gateway)\n# 2    8 ms     7 ms     8 ms  10.200.0.1  (ISP Edge Router)\n# 3   14 ms    15 ms    14 ms  72.14.215.1 (Transit Backbone)\n# 4   15 ms    14 ms    15 ms  8.8.8.8     (Final Google DNS Destination)",
                "explanation": "Displays latency and router IP addresses for each Layer 3 hop along the path."
            },
            {
                "title": "Path MTU Discovery (PMTUD) Simulation with Ping",
                "language": "bash",
                "code": "# Ping with Don't Fragment flag to discover maximum unfragmented MTU\nping -c 2 -M do -s 1460 google.com\n# If a hop along the path has MTU 1400, it returns ICMP Type 3 Code 4: \n# 'Frag needed and DF set' with next-hop MTU suggestion!",
                "explanation": "Demonstrates Path MTU Discovery using ICMP Type 3 Code 4 feedback."
            },
            {
                "title": "Python ICMP Ping Latency Analyzer (Simple Ping Parser)",
                "language": "python",
                "code": "import subprocess\nimport re\n\ndef test_host_latency(host: str) -> dict:\n    cmd = ['ping', '-c', '3', host] # Use '-n' on Windows\n    res = subprocess.run(cmd, capture_output=True, text=True)\n    if res.returncode == 0:\n        times = re.findall(r'time=([0-9.]+) ms', res.stdout)\n        float_times = [float(t) for t in times]\n        avg_lat = sum(float_times) / len(float_times) if float_times else 0.0\n        return {'host': host, 'status': 'ONLINE', 'avg_ms': round(avg_lat, 2)}\n    return {'host': host, 'status': 'OFFLINE', 'avg_ms': None}",
                "explanation": "Executes system ping and parses roundtrip latency statistics."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="ICMP Message Name Resolver",
            description="Write a Python function `get_icmp_type_name(type_num: int) -> str` that maps `0` to `'Echo Reply'`, `8` to `'Echo Request'`, `3` to `'Destination Unreachable'`, and `11` to `'Time Exceeded'`. Return `'Other'` for any other number.",
            starter_code="def get_icmp_type_name(type_num: int) -> str:\n    # Return ICMP message name\n    pass",
            solution_code="def get_icmp_type_name(type_num: int) -> str:\n    mapping = {0: 'Echo Reply', 8: 'Echo Request', 3: 'Destination Unreachable', 11: 'Time Exceeded'}\n    return mapping.get(type_num, 'Other')",
            expected_output="get_icmp_type_name(8) == 'Echo Request', get_icmp_type_name(0) == 'Echo Reply', get_icmp_type_name(11) == 'Time Exceeded'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which ICMP message type is sent by a diagnostic utility when executing an outbound `ping` probe?",
                options=[
                    "ICMP Type 8 (Echo Request)",
                    "ICMP Type 0 (Echo Reply)",
                    "ICMP Type 3 (Unreachable)",
                    "ICMP Type 11 (Time Exceeded)"
                ],
                correct_answer="ICMP Type 8 (Echo Request)",
                explanation="Ping transmits ICMP Type 8 Echo Requests and listens for incoming Type 0 Echo Replies."
            ),
            QuizQuestionBlueprint(
                question="How does Traceroute determine the IP address of each router along the path to a destination?",
                options=[
                    "It transmits probe packets with incrementally increasing IP Time-To-Live (TTL = 1, 2, 3...) values and records the source IP of returning ICMP Type 11 (Time Exceeded) messages",
                    "It asks the DNS server to list all routers",
                    "It sends a text message to each router",
                    "It decrypts the router's password"
                ],
                correct_answer="It transmits probe packets with incrementally increasing IP Time-To-Live (TTL = 1, 2, 3...) values and records the source IP of returning ICMP Type 11 (Time Exceeded) messages",
                explanation="Traceroute forces routers to drop packets at incremental TTL hops, eliciting ICMP Time Exceeded replies."
            ),
            QuizQuestionBlueprint(
                question="What ICMP message is generated by an intermediate router when a packet with the Don't Fragment (DF) bit set exceeds the next-hop interface MTU?",
                options=[
                    "ICMP Type 3 Code 4 (Destination Unreachable: Fragmentation Needed and DF Set)",
                    "ICMP Type 0 (Echo Reply)",
                    "ICMP Type 8 (Echo Request)",
                    "ICMP Type 12 (Parameter Problem)"
                ],
                correct_answer="ICMP Type 3 Code 4 (Destination Unreachable: Fragmentation Needed and DF Set)",
                explanation="Type 3 Code 4 powers Path MTU Discovery by reporting when packets exceed MTU constraints."
            ),
            QuizQuestionBlueprint(
                question="At which layer of the OSI model does the Internet Control Message Protocol (ICMP) operate?",
                options=[
                    "Layer 3 (Network Layer)",
                    "Layer 4 (Transport Layer)",
                    "Layer 7 (Application Layer)",
                    "Layer 2 (Data Link Layer)"
                ],
                correct_answer="Layer 3 (Network Layer)",
                explanation="ICMP is encapsulated directly inside IPv4 packets (Protocol 1) at the Network Layer."
            ),
            QuizQuestionBlueprint(
                question="Why do network administrators sometimes block ICMP Echo Requests (Type 8) on enterprise edge firewalls?",
                options=[
                    "To prevent automated reconnaissance scanners from discovering live active hosts and mitigate ping flood DoS attacks",
                    "Because ICMP uses too much electricity",
                    "Because ICMP slows down internet speed by 90%",
                    "Because ping is forbidden on weekends"
                ],
                correct_answer="To prevent automated reconnaissance scanners from discovering live active hosts and mitigate ping flood DoS attacks",
                explanation="Blocking inbound ICMP hides external interfaces from automated vulnerability scanners."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 37
    # -------------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37 (Project): Core Network Services Lab (DHCP, NAT & Routing)",
        concept="Integrating foundational enterprise services: Building an end-to-end multi-subnet network with DHCP server pools, PAT/Overload to ISP, and static/dynamic inter-branch routing",
        analogy="Think of this project like building a fully functioning modern smart city district from scratch. You install water mains (**Layer 3 Routing**), set up the city postal administration that assigns official street addresses to every new resident arriving in town (**DHCP Pool**), and build an international border customs checkpoint that converts internal resident IDs into international passports so citizens can browse the global world (**NAT / PAT Overload**)! Everything comes together into one living system.",
        theory_sections=[
            {
                "heading": "Module 6 Capstone Architecture",
                "body": "In this project, you construct a complete enterprise edge and core services infrastructure: (1) An enterprise Edge Router connecting an internal dual-VLAN campus (VLAN 10 Engineering, VLAN 20 Sales) to an upstream ISP gateway; (2) Configuring an automated DHCP server on the router with DNS options and exclusions; (3) Configuring dynamic Port Address Translation (PAT/Overload) so both internal subnets share a single public IP address; (4) Establishing static and dynamic routing to remote branch offices."
            },
            {
                "heading": "End-to-End Verification Pipeline",
                "body": "Success is verified when an unconfigured host PC connects to an access switch, dynamically receives an IP lease via DORA, ping-resolves local intra-VLAN and inter-VLAN default gateways, and successfully transmits packets out to the public simulated ISP address (`203.0.113.1`), with the Edge Router dynamically logging NAT translations in its state table."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Edge Router Configuration Script (Edge-Router.cfg)",
                "language": "text",
                "code": "-- Step 1: Configure Internal Gateway Sub-Interfaces\nRouter(config)# interface GigabitEthernet0/0/0.10\nRouter(config-subif)# encapsulation dot1Q 10\nRouter(config-subif)# ip address 192.168.10.1 255.255.255.0\nRouter(config-subif)# ip nat inside\n\nRouter(config)# interface GigabitEthernet0/0/0.20\nRouter(config-subif)# encapsulation dot1Q 20\nRouter(config-subif)# ip address 192.168.20.1 255.255.255.0\nRouter(config-subif)# ip nat inside\n\n-- Step 2: Configure External ISP WAN Interface\nRouter(config)# interface GigabitEthernet0/0/1\nRouter(config-if)# description ISP-Uplink\nRouter(config-if)# ip address 203.0.113.2 255.255.255.252\nRouter(config-if)# ip nat outside\nRouter(config-if)# no shutdown\n\n-- Step 3: Default Route to ISP\nRouter(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1",
                "explanation": "Configures inside sub-interfaces, outside ISP interface, and the default gateway route."
            },
            {
                "title": "DHCP Pools and NAT Overload Configuration",
                "language": "text",
                "code": "-- Exclude gateways from DHCP leases\nRouter(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.10\nRouter(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.10\n\n-- DHCP Pool for VLAN 10\nRouter(config)# ip dhcp pool POOL_ENG\nRouter(dhcp-config)# network 192.168.10.0 255.255.255.0\nRouter(dhcp-config)# default-router 192.168.10.1\nRouter(dhcp-config)# dns-server 8.8.8.8\n\n-- Access List for PAT and Overload Activation\nRouter(config)# access-list 10 permit 192.168.10.0 0.0.0.255\nRouter(config)# access-list 10 permit 192.168.20.0 0.0.0.255\nRouter(config)# ip nat inside source list 10 interface GigabitEthernet0/0/1 overload",
                "explanation": "Sets up automated DHCP pools and enables PAT overload across both internal subnets."
            },
            {
                "title": "Comprehensive Verification Commands",
                "language": "text",
                "code": "Edge-Router# show ip dhcp binding\n# Displays active IP leases handed out to client MAC addresses\n\nEdge-Router# show ip nat translations\n# Proves that private IPs are actively translating to 203.0.113.2 with unique ports\n\nEdge-Router# show ip route\n# Verifies default route (S* 0.0.0.0/0) points toward the ISP next-hop",
                "explanation": "Diagnostic suite confirming active DHCP client leases, NAT session mappings, and routing table integrity."
            },
            {
                "title": "Python End-to-End Core Services Test Automation",
                "language": "python",
                "code": "def verify_edge_services(dhcp_bound: bool, nat_translations_count: int, default_route_exists: bool) -> dict:\n    passed = dhcp_bound and (nat_translations_count > 0) and default_route_exists\n    return {\n        'dhcp_operational': dhcp_bound,\n        'pat_active': nat_translations_count > 0,\n        'wan_route_active': default_route_exists,\n        'lab_status': 'PASSED - FULL CONNECTIVITY' if passed else 'FAILED - CONFIG INCOMPLETE'\n    }",
                "explanation": "Automated verification script validating that DHCP, NAT, and default routing are operating in unison."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Core Services Readiness Checker",
            description="Write a Python function `check_core_services_readiness(has_dhcp: bool, has_nat: bool, has_default_route: bool) -> bool` that returns `True` only if all three essential core services are configured and operational.",
            starter_code="def check_core_services_readiness(has_dhcp: bool, has_nat: bool, has_default_route: bool) -> bool:\n    # Return True if all 3 services are active\n    pass",
            solution_code="def check_core_services_readiness(has_dhcp: bool, has_nat: bool, has_default_route: bool) -> bool:\n    return has_dhcp and has_nat and has_default_route",
            expected_output="check_core_services_readiness(True, True, True) == True, check_core_services_readiness(True, False, True) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In the Core Services lab, why must `ip nat inside` be configured on BOTH sub-interfaces (`Gig0/0/0.10` and `Gig0/0/0.20`)?",
                options=[
                    "Because both VLAN subnets represent internal private networks whose traffic must be translated before heading out to the Internet",
                    "To increase the speed of the copper cable",
                    "Because sub-interfaces cannot have IP addresses without NAT",
                    "It is optional and does nothing"
                ],
                correct_answer="Because both VLAN subnets represent internal private networks whose traffic must be translated before heading out to the Internet",
                explanation="NAT requires marking all internal facing interfaces with `ip nat inside` so the engine knows what to translate."
            ),
            QuizQuestionBlueprint(
                question="What Cisco command displays the list of IP addresses dynamically leased to client MAC addresses by the local DHCP server?",
                options=[
                    "show ip dhcp binding",
                    "show dhcp leases",
                    "display dhcp users",
                    "show ip pool all"
                ],
                correct_answer="show ip dhcp binding",
                explanation="`show ip dhcp binding` lists all active DHCP leases, client MAC addresses, and lease expirations."
            ),
            QuizQuestionBlueprint(
                question="Why is `ip dhcp excluded-address` configured before creating the DHCP network pool?",
                options=[
                    "To prevent the DHCP server from assigning statically configured gateway and server IP addresses to random client devices",
                    "To save money on cloud hosting",
                    "To format the router flash memory",
                    "To prevent computers from turning on"
                ],
                correct_answer="To prevent the DHCP server from assigning statically configured gateway and server IP addresses to random client devices",
                explanation="Excluding gateway and server IPs prevents duplicate IP address conflicts on the network."
            ),
            QuizQuestionBlueprint(
                question="What happens to outbound client traffic if the default route (`ip route 0.0.0.0 0.0.0.0 <isp_ip>`) is missing from the Edge Router?",
                options=[
                    "The router drops all outbound Internet traffic because it has no path to resolve non-local external IP addresses",
                    "The switch takes over and routes packets to Google",
                    "The client computers convert to dial-up modems",
                    "Packets are sent via Bluetooth"
                ],
                correct_answer="The router drops all outbound Internet traffic because it has no path to resolve non-local external IP addresses",
                explanation="Without a default route (gateway of last resort), non-local Internet traffic is dropped as unroutable."
            ),
            QuizQuestionBlueprint(
                question="What ACL type is used in the `ip nat inside source list <num> interface ...` command to select which private subnets participate in PAT?",
                options=[
                    "Standard Access Control List (Permitting internal subnets)",
                    "MAC address access list",
                    "Extended VLAN filter",
                    "Password list"
                ],
                correct_answer="Standard Access Control List (Permitting internal subnets)",
                explanation="A Standard ACL specifies which internal source IP networks are permitted to be translated via NAT."
            )
        ],
        is_project_day=True,
        project_name="Core Network Services Architecture Lab"
    ),

    # -------------------------------------------------------------
    # DAY 38
    # -------------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Wi-Fi Standards (IEEE 802.11a/b/g/n/ac/ax/be & Wi-Fi 4/5/6/7)",
        concept="The evolution of wireless local area networks: IEEE 802.11 standards, consumer Wi-Fi generational naming (Wi-Fi 4 through Wi-Fi 7), channel bandwidths, and spatial streams",
        analogy="Think of Wi-Fi standards like the evolution of wireless cargo helicopters. **Wi-Fi 1/2 (802.11b)** was an old single-propeller helicopter that could only carry 11 pounds of cargo slowly. **Wi-Fi 5 (802.11ac)** was a twin-engine cargo helicopter flying on a dedicated 5GHz sky highway at 1 Gbps. **Wi-Fi 6 (802.11ax)** is a smart delivery fleet where multiple drones take off in parallel (**OFDMA**), sharing the airspace without colliding even in a packed stadium!",
        theory_sections=[
            {
                "heading": "The Evolution from 802.11b to Wi-Fi 7 (802.11be)",
                "body": "Wireless networks operate under IEEE 802.11 standards using radio frequency (RF) bands. To simplify technical jargon for consumers, the Wi-Fi Alliance introduced generational naming: **Wi-Fi 4 (802.11n)** introduced 2.4/5GHz MIMO; **Wi-Fi 5 (802.11ac)** introduced 5GHz only, 80/160MHz channels, and MU-MIMO; **Wi-Fi 6 / 6E (802.11ax)** introduced the clean 6GHz band, OFDMA, and 1024-QAM; **Wi-Fi 7 (802.11be)** introduces 320MHz ultrawide channels, 4096-QAM, and Multi-Link Operation (MLO) delivering up to 46 Gbps."
            },
            {
                "heading": "Key Wireless Technologies: MIMO, MU-MIMO & OFDMA",
                "body": "**MIMO (Multiple-Input Multiple-Output)** uses multiple antennas to transmit independent spatial data streams simultaneously. **MU-MIMO (Multi-User MIMO)** allows an Access Point to talk to multiple client devices concurrently rather than waiting in turn. **OFDMA (Orthogonal Frequency Division Multiple Access)** subdivides wireless channels into smaller sub-carriers, allowing an AP to transmit to 30 low-bandwidth IoT devices in a single radio transmission cycle."
            }
        ],
        code_snippets=[
            {
                "title": "IEEE 802.11 Wireless Generational Standards Table",
                "language": "text",
                "code": "Wi-Fi Gen   IEEE Standard   Year   Frequencies Supported   Max Channel Width  Max Theoretical Speed\nLegacy      802.11b         1999   2.4 GHz                 20 MHz             11 Mbps\nLegacy      802.11a/g       2003   5 GHz / 2.4 GHz         20 MHz             54 Mbps\nWi-Fi 4     802.11n         2009   2.4 GHz & 5 GHz         40 MHz             600 Mbps (4x4 MIMO)\nWi-Fi 5     802.11ac        2014   5 GHz only              160 MHz            6.9 Gbps (8x8 MU-MIMO)\nWi-Fi 6     802.11ax        2019   2.4 GHz & 5 GHz         160 MHz            9.6 Gbps (OFDMA, 1024-QAM)\nWi-Fi 6E    802.11ax (6E)   2021   6 GHz band              160 MHz            9.6 Gbps (Clean 6GHz spectrum)\nWi-Fi 7     802.11be        2024   2.4, 5, and 6 GHz       320 MHz            46.1 Gbps (4096-QAM, MLO)",
                "explanation": "Reference chart contrasting IEEE standards, consumer names, frequency bands, and speeds."
            },
            {
                "title": "Inspecting Wi-Fi Link Speed, Frequency and Standard in Linux",
                "language": "bash",
                "code": "# Inspect active wireless connection details\niwconfig wlan0\n# or with modern iw tool:\niw dev wlan0 link\n# Connected to 00:14:22:01:aa:bb\n# SSID: Hunar-Enterprise-WiFi\n# freq: 5240 (5 GHz band, Channel 48)\n# rx bitrate: 866.7 MBit/s 80MHz (Wi-Fi 5 / 802.11ac)",
                "explanation": "CLI command displaying current wireless radio frequency, channel width, and negotiated bitrate."
            },
            {
                "title": "Scanning Wireless Access Points in Windows (netsh)",
                "language": "powershell",
                "code": "# Show all detected wireless networks, signal strength, and radio types\nnetsh wlan show networks mode=bssid\n# Radio type : 802.11ax (Wi-Fi 6)\n# Signal     : 98%\n# Channel    : 36 (5 GHz)",
                "explanation": "Scans surrounding wireless access points, detailing supported IEEE radio types and signal percentages."
            },
            {
                "title": "Python Wi-Fi Generation Standard Resolver",
                "language": "python",
                "code": "WIFI_STANDARDS = {\n    '802.11b': 'Legacy Wi-Fi',\n    '802.11g': 'Legacy Wi-Fi',\n    '802.11n': 'Wi-Fi 4',\n    '802.11ac': 'Wi-Fi 5',\n    '802.11ax': 'Wi-Fi 6 / 6E',\n    '802.11be': 'Wi-Fi 7'\n}\n\ndef resolve_wifi_gen(standard_str: str) -> str:\n    return WIFI_STANDARDS.get(standard_str.strip().lower(), 'Unknown Standard')",
                "explanation": "Maps IEEE 802.11 standard strings to user-friendly Wi-Fi Alliance generational numbers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Wi-Fi Generation Formatter",
            description="Write a Python function `get_wifi_name(ieee_standard: str) -> str` that maps `'802.11n'` to `'Wi-Fi 4'`, `'802.11ac'` to `'Wi-Fi 5'`, `'802.11ax'` to `'Wi-Fi 6'`, and `'802.11be'` to `'Wi-Fi 7'`. Return `'Legacy'` for others.",
            starter_code="def get_wifi_name(ieee_standard: str) -> str:\n    # Return Wi-Fi generational name\n    pass",
            solution_code="def get_wifi_name(ieee_standard: str) -> str:\n    mapping = {\n        '802.11n': 'Wi-Fi 4',\n        '802.11ac': 'Wi-Fi 5',\n        '802.11ax': 'Wi-Fi 6',\n        '802.11be': 'Wi-Fi 7'\n    }\n    return mapping.get(ieee_standard.strip().lower(), 'Legacy')",
            expected_output="get_wifi_name('802.11ax') == 'Wi-Fi 6', get_wifi_name('802.11ac') == 'Wi-Fi 5'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What consumer-friendly name was assigned by the Wi-Fi Alliance to the IEEE 802.11ax standard?",
                options=[
                    "Wi-Fi 6 (and Wi-Fi 6E)",
                    "Wi-Fi 5",
                    "Wi-Fi 7",
                    "Wi-Fi 4"
                ],
                correct_answer="Wi-Fi 6 (and Wi-Fi 6E)",
                explanation="IEEE 802.11ax is branded as Wi-Fi 6 (operating in 2.4/5GHz) and Wi-Fi 6E (operating in 6GHz)."
            ),
            QuizQuestionBlueprint(
                question="What wireless technology in Wi-Fi 6 (802.11ax) allows an Access Point to split a channel into smaller sub-carriers to communicate with multiple devices simultaneously?",
                options=[
                    "OFDMA (Orthogonal Frequency Division Multiple Access)",
                    "Bluetooth",
                    "Token Ring",
                    "EtherChannel"
                ],
                correct_answer="OFDMA (Orthogonal Frequency Division Multiple Access)",
                explanation="OFDMA partitions channel bandwidth into Resource Units, serving multiple clients concurrently."
            ),
            QuizQuestionBlueprint(
                question="Which Wi-Fi standard operates EXCLUSIVELY in the 5 GHz radio frequency band?",
                options=[
                    "Wi-Fi 5 (802.11ac)",
                    "Wi-Fi 4 (802.11n)",
                    "Wi-Fi 6 (802.11ax)",
                    "802.11b"
                ],
                correct_answer="Wi-Fi 5 (802.11ac)",
                explanation="802.11ac (Wi-Fi 5) was designed strictly for 5 GHz to avoid congested 2.4 GHz spectrum."
            ),
            QuizQuestionBlueprint(
                question="What does 'MIMO' stand for in wireless networking?",
                options=[
                    "Multiple-Input Multiple-Output (using multiple antennas to send parallel spatial data streams)",
                    "Micro Internet Master Operator",
                    "Modem Interface Mode Online",
                    "Memory Internal Memory Outside"
                ],
                correct_answer="Multiple-Input Multiple-Output (using multiple antennas to send parallel spatial data streams)",
                explanation="MIMO transmits multiple spatial streams over multiple antennas, multiplying throughput."
            ),
            QuizQuestionBlueprint(
                question="What is the key technological addition in Wi-Fi 7 (802.11be) that allows devices to transmit and receive across both 5GHz and 6GHz bands simultaneously?",
                options=[
                    "MLO (Multi-Link Operation)",
                    "Copper wires",
                    "Analog modulation",
                    "Infrared LEDs"
                ],
                correct_answer="MLO (Multi-Link Operation)",
                explanation="Multi-Link Operation (MLO) allows Wi-Fi 7 devices to aggregate multiple bands concurrently for low latency."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 39
    # -------------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Wireless Frequencies & Channels (2.4 GHz vs 5 GHz)",
        concept="Radio frequency physics: Range vs Speed trade-offs, non-overlapping channels (1, 6, 11 in 2.4GHz), UNII bands in 5GHz, DFS radar detection, and co-channel interference",
        analogy="Think of wireless frequencies like musical sound waves. **2.4 GHz** is a deep, low-frequency bass drum: the sound waves pass easily through thick concrete walls and travel long distances into the garden, but low frequency can't pack much data per second (**slow speed, crowded 3-lane road**). **5 GHz** is a high-pitched flute: it carries immense crisp detail (**superfast multi-gigabit speed**), but gets blocked by the very first closed wooden bedroom door (**short range, wide 25-lane highway**)!",
        theory_sections=[
            {
                "heading": "Physics of 2.4 GHz vs 5 GHz vs 6 GHz",
                "body": "Higher radio frequencies provide higher bandwidth but suffer greater attenuation through physical obstacles: (1) **2.4 GHz**: Superior wall penetration and coverage range (~45m indoors), but crowded (microwaves, Bluetooth share the band) with narrow channels; (2) **5 GHz**: Less crowded, shorter range (~15m indoors), supports wide 80MHz/160MHz channels for gigabit speeds; (3) **6 GHz**: Pristine, wide spectrum with zero legacy device interference."
            },
            {
                "heading": "Non-Overlapping Channels: The 1, 6, 11 Rule in 2.4 GHz",
                "body": "In 2.4 GHz, channels are 20 MHz wide but spaced only 5 MHz apart. Adjacent channels overlap, causing destructive **Co-Channel Interference (CCI)**. In North America and global standards, there are **only THREE non-overlapping channels: Channel 1, Channel 6, and Channel 11**. In 5 GHz, there are up to 25 non-overlapping 20MHz channels organized into UNII bands (UNII-1, UNII-2/DFS, UNII-3)."
            }
        ],
        code_snippets=[
            {
                "title": "2.4 GHz Non-Overlapping Channel Layout Diagram",
                "language": "text",
                "code": "Frequency (MHz): 2412   2417   2422   2427   2432   2437   2442   2447   2452   2457   2462\nChannel #:        1      2      3      4      5      6      7      8      9      10     11\n                [--- Channel 1 (22MHz) ---]        [--- Channel 6 (22MHz) ---]        [--- Channel 11 (22MHz) ---]\nNotice: Channels 1, 6, and 11 do NOT touch or overlap! Any other channel choices cause interference!",
                "explanation": "Diagram showing how channels 1, 6, and 11 provide interference-free channel separation in 2.4GHz."
            },
            {
                "title": "Analyzing Wi-Fi Channel Saturation with Linux Wavemon",
                "language": "bash",
                "code": "# Real-time terminal wireless signal monitor\nsudo wavemon\n# Displays link quality, signal level in dBm (-45 dBm = Excellent, -80 dBm = Poor),\n# and active channel frequency",
                "explanation": "Wavemon displays live signal-to-noise ratio (SNR) and received signal strength indication (RSSI)."
            },
            {
                "title": "Configuring 2.4 GHz and 5 GHz Radios on Cisco AP",
                "language": "text",
                "code": "-- Radio 0: 2.4 GHz Band (Set to Non-overlapping Channel 6)\nAP(config)# interface Dot11Radio 0\nAP(config-if)# channel 2437  -- Channel 6\nAP(config-if)# power local 100\n\n-- Radio 1: 5 GHz Band (Set to UNII-1 Channel 36, 80MHz channel width)\nAP(config)# interface Dot11Radio 1\nAP(config-if)# channel 5180  -- Channel 36\nAP(config-if)# channel-width 80",
                "explanation": "Configures channel numbers and channel widths across 2.4 GHz and 5 GHz radios."
            },
            {
                "title": "Python Non-Overlapping Channel Plan Checker",
                "language": "python",
                "code": "def check_channel_plan_2ghz(ap_channels: list[int]) -> bool:\n    \"\"\"Valid enterprise 2.4GHz plan must use ONLY channels 1, 6, and 11\"\"\"\n    valid_non_overlap = {1, 6, 11}\n    for ch in ap_channels:\n        if ch not in valid_non_overlap:\n            print(f'Warning: Channel {ch} causes destructive adjacent channel interference!')\n            return False\n    return True\n\nprint(check_channel_plan_2ghz([1, 6, 11, 6, 1])) # True (Clean Plan)",
                "explanation": "Validates that a 2.4 GHz wireless plan uses only non-overlapping channels (1, 6, and 11)."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="2.4 GHz Non-Overlapping Channel Validator",
            description="Write a Python function `is_clean_2ghz_channel(channel: int) -> bool` that returns `True` if `channel` is 1, 6, or 11 (the only three non-overlapping channels in 2.4GHz), and `False` otherwise.",
            starter_code="def is_clean_2ghz_channel(channel: int) -> bool:\n    # Return True if 1, 6, or 11\n    pass",
            solution_code="def is_clean_2ghz_channel(channel: int) -> bool:\n    return channel in [1, 6, 11]",
            expected_output="is_clean_2ghz_channel(1) == True, is_clean_2ghz_channel(6) == True, is_clean_2ghz_channel(3) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the ONLY three non-overlapping channels available in the standard 2.4 GHz Wi-Fi spectrum in North America and global standards?",
                options=[
                    "Channels 1, 6, and 11",
                    "Channels 1, 2, and 3",
                    "Channels 2, 4, and 8",
                    "Channels 36, 40, and 44"
                ],
                correct_answer="Channels 1, 6, and 11",
                explanation="Channels 1, 6, and 11 are spaced 25 MHz apart, avoiding channel overlap in the 2.4 GHz band."
            ),
            QuizQuestionBlueprint(
                question="Why does a 2.4 GHz Wi-Fi signal penetrate walls and cover larger physical distances better than a 5 GHz signal?",
                options=[
                    "Lower radio frequencies have longer wavelengths that experience lower physical attenuation through solid obstacles like drywall and brick",
                    "2.4 GHz cables are thicker",
                    "5 GHz is blocked by cloud rain only",
                    "2.4 GHz uses nuclear energy"
                ],
                correct_answer="Lower radio frequencies have longer wavelengths that experience lower physical attenuation through solid obstacles like drywall and brick",
                explanation="Lower frequencies have longer wavelengths, suffering less absorption through physical barriers."
            ),
            QuizQuestionBlueprint(
                question="What is the primary advantage of the 5 GHz Wi-Fi band over the 2.4 GHz band?",
                options=[
                    "Much wider spectrum availability, allowing 40MHz, 80MHz, and 160MHz wide channels with higher throughput and less interference",
                    "It has infinite transmission range",
                    "It does not require antennas",
                    "It eliminates the need for passwords"
                ],
                correct_answer="Much wider spectrum availability, allowing 40MHz, 80MHz, and 160MHz wide channels with higher throughput and less interference",
                explanation="5 GHz offers up to 25 non-overlapping channels and wide channel bonding for higher speeds."
            ),
            QuizQuestionBlueprint(
                question="What is 'DFS' (Dynamic Frequency Selection) in the 5 GHz Wi-Fi spectrum?",
                options=[
                    "A mandatory regulatory mechanism where an AP monitors for weather radar and military radar signals, dynamically vacating the channel if radar is detected",
                    "A tool for downloading games faster",
                    "A feature that boosts Wi-Fi battery life",
                    "An encryption algorithm"
                ],
                correct_answer="A mandatory regulatory mechanism where an AP monitors for weather radar and military radar signals, dynamically vacating the channel if radar is detected",
                explanation="DFS requires APs on certain 5GHz channels to yield frequency if radar pulses are detected."
            ),
            QuizQuestionBlueprint(
                question="What is an ideal Received Signal Strength Indicator (RSSI) reading in dBm for a healthy, high-speed Wi-Fi connection?",
                options=[
                    "-50 dBm to -65 dBm (Strong signal)",
                    "-95 dBm (Disconnected / Extreme noise)",
                    "+100 dBm (Impossible)",
                    "0 dBm"
                ],
                correct_answer="-50 dBm to -65 dBm (Strong signal)",
                explanation="RSSI is measured in negative numbers; -50 dBm to -65 dBm indicates a healthy, strong wireless signal."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 40
    # -------------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Wireless Architectures (Autonomous vs Controller-Based WLC)",
        concept="Scaling wireless enterprise networks: Standalone Autonomous APs vs Lightweight APs (LAP), CAPWAP tunneling, and Wireless LAN Controllers (WLC)",
        analogy="Think of managing wireless access points like managing security guards at an airport. An **Autonomous AP** is an independent private guard: you must walk up to each guard individually and train them on rules, passwords, and shift schedules (configuring 100 APs one by one is a nightmare!). A **Controller-Based (Lightweight) AP** architecture is having 100 security cameras connected to a central command desk (**WLC**). The central chief pushes rules to all 100 cameras in 2 seconds!",
        theory_sections=[
            {
                "heading": "Autonomous APs vs Lightweight APs (LAP)",
                "body": "**Autonomous (Standalone) APs** handle both the Control Plane (radio management, authentication, encryption) and Data Plane (forwarding user frames) locally. Managing 200 autonomous APs requires configuring each IP and SSID individually. **Lightweight APs (LAP)** offload the Control Plane to a central **Wireless LAN Controller (WLC)**, handling only real-time Layer 1/2 RF transmissions."
            },
            {
                "heading": "CAPWAP Protocol & Centralized Management",
                "body": "Lightweight APs communicate with the central WLC using the **CAPWAP (Control and Provisioning of Wireless Access Points)** protocol (UDP ports 5246/5247). CAPWAP creates two encrypted tunnels: (1) **Control Tunnel**: WLC pushes configurations, radio channels, and firmware; (2) **Data Tunnel**: Client wireless frames are encapsulated and tunneled back to the WLC for centralized policy enforcement and seamless Layer 2 roaming."
            }
        ],
        code_snippets=[
            {
                "title": "Autonomous AP vs Controller-Based (LAP) Architecture Comparison",
                "language": "text",
                "code": "Feature                 Autonomous AP                    Lightweight AP + WLC (Centralized)\nManagement              Decentralized (Configure each AP) Unified Dashboard (Configure 1000s at once)\nProtocol Used           Standard Standalone              CAPWAP (UDP 5246 Control, 5247 Data)\nControl Plane           On the local AP hardware         Centralized on Wireless LAN Controller (WLC)\nData Plane              Local switching at AP            Tunneled to WLC (or FlexConnect local switch)\nSeamless Roaming        Difficult / High latency         Instant Layer 2/3 roaming managed by WLC\nFirmware Updates        Manual per device                Automated mass image push from WLC",
                "explanation": "Reference chart contrasting autonomous standalone APs with centralized WLC architectures."
            },
            {
                "title": "Inspecting CAPWAP Tunnels on Cisco Wireless LAN Controller",
                "language": "text",
                "code": "(Cisco Controller) > show ap summary\nNumber of APs.................................... 12\n\nAP Name          Slots  AP Model             Ethernet MAC       IP Address       Port  State\n---------------- ----- -------------------- ------------------ ---------------- ----- -------\nAP-Floor1-North   2     AIR-AP3802I-B-K9     00:14:22:aa:bb:01  10.10.1.50       1     Registered\nAP-Floor1-South   2     AIR-AP3802I-B-K9     00:14:22:aa:bb:02  10.10.1.51       1     Registered\n# 'State: Registered' confirms active CAPWAP control and data tunnels formed!",
                "explanation": "Displays operational status of lightweight APs connected via CAPWAP to a central WLC."
            },
            {
                "title": "Configuring FlexConnect Mode on an Access Point",
                "language": "text",
                "code": "-- FlexConnect allows branch APs to switch user traffic locally into the local VLAN\n-- even if the WAN connection to the central WLC goes down!\n(Cisco Controller) > config ap mode flexconnect AP-Floor1-North\n(Cisco Controller) > config ap flexconnect vlan enable AP-Floor1-North",
                "explanation": "FlexConnect allows local data switching at branch sites while retaining centralized management."
            },
            {
                "title": "Python WLC Discovery Simulation via DHCP Option 43",
                "language": "python",
                "code": "def parse_dhcp_option_43(hex_str: str) -> list[str]:\n    \"\"\"Extracts WLC Controller IP addresses from DHCP Option 43 vendor string\"\"\"\n    clean = hex_str.replace(':', '').replace(' ', '')\n    ips = []\n    # Each IPv4 is 8 hex characters (4 bytes)\n    for i in range(0, len(clean), 8):\n        chunk = clean[i:i+8]\n        if len(chunk) == 8:\n            ip = '.'.join(str(int(chunk[j:j+2], 16)) for j in range(0, 8, 2))\n            ips.append(ip)\n    return ips\n\nprint(parse_dhcp_option_43('c0a80164')) # Output: ['192.168.1.100'] (WLC IP)",
                "explanation": "Decodes DHCP Option 43 vendor payloads used by APs to locate their WLC upon boot."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="CAPWAP Port Classifier",
            description="Write a Python function `get_capwap_port_type(port: int) -> str` that returns `'Control'` for port 5246, `'Data'` for port 5247, and `'Invalid'` for any other port.",
            starter_code="def get_capwap_port_type(port: int) -> str:\n    # Return CAPWAP port role\n    pass",
            solution_code="def get_capwap_port_type(port: int) -> str:\n    if port == 5246:\n        return 'Control'\n    elif port == 5247:\n        return 'Data'\n    return 'Invalid'",
            expected_output="get_capwap_port_type(5246) == 'Control', get_capwap_port_type(5247) == 'Data', get_capwap_port_type(80) == 'Invalid'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What protocol is used by Lightweight Access Points (LAPs) to communicate and tunnel traffic to a Wireless LAN Controller (WLC)?",
                options=[
                    "CAPWAP (Control and Provisioning of Wireless Access Points)",
                    "BGP",
                    "RIPv2",
                    "HTTP"
                ],
                correct_answer="CAPWAP (Control and Provisioning of Wireless Access Points)",
                explanation="CAPWAP (RFC 5415/5416) is the standard protocol governing WLC-to-AP communication."
            ),
            QuizQuestionBlueprint(
                question="What UDP ports are used by CAPWAP for Control and Data tunnels?",
                options=[
                    "UDP Port 5246 (Control) and UDP Port 5247 (Data)",
                    "TCP Port 80 and 443",
                    "UDP Port 67 and 68",
                    "TCP Port 22 and 23"
                ],
                correct_answer="UDP Port 5246 (Control) and UDP Port 5247 (Data)",
                explanation="CAPWAP uses UDP port 5246 for management/control and port 5247 for data encapsulation."
            ),
            QuizQuestionBlueprint(
                question="What is a major operational benefit of a Controller-Based (WLC) wireless architecture over autonomous APs?",
                options=[
                    "Centralized management, automated RF channel optimization, seamless client roaming, and mass firmware updates across hundreds of APs",
                    "It eliminates the need for Wi-Fi antennas",
                    "It converts radio waves into copper cables",
                    "It provides free electricity to APs"
                ],
                correct_answer="Centralized management, automated RF channel optimization, seamless client roaming, and mass firmware updates across hundreds of APs",
                explanation="WLC architectures centralize control planes, simplifying mass management and seamless client handoffs."
            ),
            QuizQuestionBlueprint(
                question="What is 'Cisco FlexConnect' mode on a Lightweight Access Point?",
                options=[
                    "A feature that allows branch office APs to switch user traffic locally onto the local LAN even if the WAN link to the central WLC fails",
                    "A bendable antenna for physical APs",
                    "A tool for creating fake SSIDs",
                    "A cable tester"
                ],
                correct_answer="A feature that allows branch office APs to switch user traffic locally onto the local LAN even if the WAN link to the central WLC fails",
                explanation="FlexConnect enables local switching at branch sites, surviving central controller disconnects."
            ),
            QuizQuestionBlueprint(
                question="What DHCP Option number is commonly configured on enterprise DHCP servers to inform newly booted APs of the WLC's IP address?",
                options=[
                    "DHCP Option 43",
                    "DHCP Option 3",
                    "DHCP Option 6",
                    "DHCP Option 15"
                ],
                correct_answer="DHCP Option 43",
                explanation="DHCP Option 43 provides vendor-specific options containing WLC IP addresses."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 41
    # -------------------------------------------------------------
    DayBlueprint(
        order=41,
        title="Day 41: Wireless Security Protocols (WEP, WPA2, WPA3 & 802.1X)",
        concept="Securing the airwaves: The fatal flaws of WEP (RC4), WPA2 (AES-CCMP, 4-Way Handshake, KRACK), WPA3 (SAE Dragonfly, 192-bit crypto), and WPA-Enterprise (802.1X / RADIUS)",
        analogy="Think of wireless security like locking your front bicycle gate. **WEP** is a cheap plastic combination lock whose code can be cracked with a paperclip in 60 seconds. **WPA2-Personal** is a solid steel lock, but everyone in the neighborhood shares the exact same secret key (**Pre-Shared Key**—if an angry roommate leaves, they still have the key!). **WPA3** uses a dynamic holographic biometric scanner (**SAE Handshake**); even if a thief records the signals, they cannot crack it with offline dictionary attacks! **WPA-Enterprise (802.1X)** gives every employee their own personal electronic badge linked to HR records!",
        theory_sections=[
            {
                "heading": "The Evolution of Wi-Fi Encryption Protocols",
                "body": "(1) **WEP (Wired Equivalent Privacy)**: Deprecated in 2004 due to tiny 24-bit Initialization Vectors (IV) and weak RC4 encryption, crackable in minutes; (2) **WPA (TKIP)**: Interim temporary fix; (3) **WPA2 (IEEE 802.11i)**: Introduced mandatory **AES-CCMP** encryption; robust for over a decade, but vulnerable to offline dictionary brute-forcing if an attacker captures the 4-Way Handshake, as well as KRACK (Key Reinstallation Attacks)."
            },
            {
                "heading": "WPA3 Innovation & WPA-Enterprise (802.1X)",
                "body": "**WPA3** (introduced in 2018) revolutionizes security: replaces Pre-Shared Keys with **SAE (Simultaneous Authentication of Equals / Dragonfly Handshake)**, offering Forward Secrecy and complete immunity against offline dictionary attacks. **WPA-Enterprise (802.1X)** replaces shared passwords with centralized authentication: client credentials (EAP-TLS, PEAP) are verified against a backend **RADIUS / AAA Server** (Cisco ISE, FreeRADIUS)."
            }
        ],
        code_snippets=[
            {
                "title": "Wi-Fi Security Evolution Summary Table",
                "language": "text",
                "code": "Standard     Encryption Cipher  Authentication Method          Vulnerability Status\nWEP          RC4 (24-bit IV)    Open / Shared Secret           COMPLETELY BROKEN (Cracked in 60s)\nWPA          RC4 / TKIP         Pre-Shared Key (PSK) / 802.1X  DEPRECATED\nWPA2-PSK     AES-CCMP           4-Way Handshake with PSK       Vulnerable to offline dictionary attacks / KRACK\nWPA2-Ent     AES-CCMP           802.1X / EAP (RADIUS Server)   Strong Enterprise Security\nWPA3-SAE     AES-GCM-256        SAE (Dragonfly Handshake)      CURRENT GOLD STANDARD (Forward Secrecy)\nWPA3-Ent     CNSA 192-bit Suite 802.1X / EAP-TLS with PKI      Maximum Military / Government Security",
                "explanation": "Reference chart contrasting encryption ciphers, authentication methods, and security postures."
            },
            {
                "title": "Configuring WPA3-Personal (SAE) on Cisco Access Point",
                "language": "text",
                "code": "AP(config)# wlan Corporate-WiFi\nAP(config-wlan)# security wpa psk set-key ascii MySuperSecretPreSharedKey2026\nAP(config-wlan)# security wpa wpa3\nAP(config-wlan)# security wpa wpa3 ciphers aes-gcm-256\nAP(config-wlan)# security pmf mandatory   -- Protected Management Frames (802.11w) mandatory in WPA3!",
                "explanation": "Configures WPA3 SAE with mandatory Protected Management Frames (PMF) preventing deauth attacks."
            },
            {
                "title": "Configuring WPA2-Enterprise with 802.1X RADIUS Authentication",
                "language": "text",
                "code": "-- Define centralized RADIUS authentication server (Cisco ISE / FreeRADIUS)\nSwitch(config)# radius-server host 10.1.1.50 auth-port 1812 acct-port 1813 key RadiusSecretKey\n\n-- Configure WLAN for 802.1X EAP authentication\n(Controller) > config wlan security wpa enable 1\n(Controller) > config wlan security wpa wpa2 enable 1\n(Controller) > config wlan security wpa wpa2 ciphers aes enable 1\n(Controller) > config wlan security wpa akm 802.1x enable 1",
                "explanation": "Sets up 802.1X enterprise authentication delegating user validation to a central RADIUS server."
            },
            {
                "title": "Python WPA3 SAE Handshake Security Validator",
                "language": "python",
                "code": "def evaluate_wifi_security(protocol: str, uses_pmf: bool) -> dict:\n    p = protocol.strip().upper()\n    if p in ['WEP', 'WPA', 'WPA-TKIP']:\n        return {'security_grade': 'F', 'recommendation': 'CRITICAL: Insecure legacy protocol! Upgrade immediately.'}\n    elif p == 'WPA2-PSK':\n        return {'security_grade': 'B', 'recommendation': 'Good, but vulnerable to offline dictionary attack if weak password used.'}\n    elif p == 'WPA3-SAE' and uses_pmf:\n        return {'security_grade': 'A+', 'recommendation': 'Optimal: Protected against offline brute force with Forward Secrecy.'}\n    return {'security_grade': 'C', 'recommendation': 'Review configuration'}",
                "explanation": "Audits wireless security configurations and flags deprecated or vulnerable settings."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Wi-Fi Security Grade Evaluator",
            description="Write a Python function `get_wifi_security_grade(protocol: str) -> str` that returns `'Dangerous'` for `'WEP'`, `'Deprecated'` for `'WPA'`, `'Acceptable'` for `'WPA2'`, and `'Optimal'` for `'WPA3'`.",
            starter_code="def get_wifi_security_grade(protocol: str) -> str:\n    # Return security evaluation grade\n    pass",
            solution_code="def get_wifi_security_grade(protocol: str) -> str:\n    p = protocol.strip().upper()\n    if 'WEP' in p:\n        return 'Dangerous'\n    elif p == 'WPA':\n        return 'Deprecated'\n    elif 'WPA2' in p:\n        return 'Acceptable'\n    elif 'WPA3' in p:\n        return 'Optimal'\n    return 'Unknown'",
            expected_output="get_wifi_security_grade('WPA3') == 'Optimal', get_wifi_security_grade('WEP') == 'Dangerous'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is WEP (Wired Equivalent Privacy) considered completely insecure and banned in modern networks?",
                options=[
                    "It uses weak RC4 encryption with a tiny 24-bit Initialization Vector (IV), allowing attackers to recover the secret key in minutes using passive packet sniffing",
                    "It causes laptops to overheat",
                    "It charges high license fees",
                    "It cannot support English passwords"
                ],
                correct_answer="It uses weak RC4 encryption with a tiny 24-bit Initialization Vector (IV), allowing attackers to recover the secret key in minutes using passive packet sniffing",
                explanation="WEP's short 24-bit IV results in keystream reuse, allowing complete decryption via statistical tools."
            ),
            QuizQuestionBlueprint(
                question="What authentication mechanism in WPA3 replaces the vulnerable Pre-Shared Key 4-Way Handshake to prevent offline dictionary brute-force attacks?",
                options=[
                    "SAE (Simultaneous Authentication of Equals / Dragonfly Handshake)",
                    "WEP Key",
                    "Telnet password",
                    "MD5 checksum"
                ],
                correct_answer="SAE (Simultaneous Authentication of Equals / Dragonfly Handshake)",
                explanation="SAE uses zero-knowledge proof mechanics to resist offline dictionary cracking and provide forward secrecy."
            ),
            QuizQuestionBlueprint(
                question="What security standard is mandatory in WPA3 to protect management frames (like Disassociation and Deauthentication) from spoofing attacks?",
                options=[
                    "Protected Management Frames (PMF / IEEE 802.11w)",
                    "VLAN Tagging",
                    "Spanning Tree",
                    "PortFast"
                ],
                correct_answer="Protected Management Frames (PMF / IEEE 802.11w)",
                explanation="PMF (802.11w) cryptographically signs management frames, preventing rogue deauthentication attacks."
            ),
            QuizQuestionBlueprint(
                question="What is the primary difference between WPA2-Personal and WPA2-Enterprise?",
                options=[
                    "WPA2-Personal uses a shared single password (PSK) for all users; WPA2-Enterprise uses individual usernames/credentials authenticated via an 802.1X RADIUS server",
                    "WPA2-Enterprise only works on Apple devices",
                    "WPA2-Personal requires no electricity",
                    "There is no difference"
                ],
                correct_answer="WPA2-Personal uses a shared single password (PSK) for all users; WPA2-Enterprise uses individual usernames/credentials authenticated via an 802.1X RADIUS server",
                explanation="Enterprise 802.1X ties authentication to unique user credentials verified by a backend RADIUS server."
            ),
            QuizQuestionBlueprint(
                question="What encryption cipher is used by WPA2 to secure user data payloads over the air?",
                options=[
                    "AES-CCMP (Advanced Encryption Standard)",
                    "DES (56-bit)",
                    "Plaintext ASCII",
                    "Caesar Cipher"
                ],
                correct_answer="AES-CCMP (Advanced Encryption Standard)",
                explanation="WPA2 mandates AES-CCMP encryption, replacing weak legacy RC4/TKIP ciphers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 42
    # -------------------------------------------------------------
    DayBlueprint(
        order=42,
        title="Day 42: Leased Lines & Metro Ethernet (WAN Fundamentals)",
        concept="Connecting remote corporate branches: T1/E1, T3/E3, Synchronous Optical Network (SONET/SDH), and Carrier Ethernet (E-Line, E-LAN, E-Tree)",
        analogy="Think of connecting branch offices like transportation between distant cities. Traditional **Leased Lines (T1/T3)** were like renting a dedicated private single-track railway line through the desert: you paid a fortune every month whether you sent 100 trains a day or zero trains (guaranteed speed, but rigid and expensive). **Metro Ethernet** is like connecting your branch offices directly into a high-speed fiber city metro subway system (**Layer 2 Ethernet over Fiber**)—cheap, scalable up to 100 Gbps, and plugs right into your standard switch!",
        theory_sections=[
            {
                "heading": "Traditional Leased Lines: T-Carrier & Optical Backbones",
                "body": "Historically, enterprise WANs relied on dedicated point-to-point **Leased Lines**: T1 (1.544 Mbps in North America), E1 (2.048 Mbps in Europe), T3 (44.736 Mbps), and SONET/SDH optical rings (OC-3 to OC-192). Leased lines use Time-Division Multiplexing (TDM), providing guaranteed constant bit rate (CBR) and deterministic latency, but suffer from high recurring costs and rigid bandwidth ceilings."
            },
            {
                "heading": "Metro Ethernet (Carrier Ethernet) Revolution",
                "body": "Today, telcos deliver **Metro Ethernet** (defined by MEF - Metro Ethernet Forum) directly over metropolitan fiber rings, eliminating costly CSU/DSU serial equipment. Service Types: (1) **E-Line (Ethernet Private Line)**: Point-to-point connection bridging two sites as if connected by a single patch cord; (2) **E-LAN (Ethernet Private LAN)**: Multipoint-to-multipoint connecting multiple branch offices into a shared Layer 2 broadcast domain; (3) **E-Tree**: Point-to-multipoint (hub and spoke)."
            }
        ],
        code_snippets=[
            {
                "title": "Legacy T1/T3 vs Modern Metro Ethernet Comparison",
                "language": "text",
                "code": "Technology      Bandwidth Options    Interface Type           Topology                Standard\nT1 / E1         1.544 / 2.048 Mbps   Serial (RJ-48 / V.35)    Point-to-Point (TDM)    ANSI T1.403\nT3 / E3         44.736 / 34.368 Mbps Coaxial BNC              Point-to-Point          ANSI T1.107\nMetro Ethernet  10 Mbps to 100 Gbps  Standard RJ-45 / SFP+    E-Line, E-LAN, E-Tree   MEF Carrier Ethernet 2.0",
                "explanation": "Reference chart contrasting legacy serial TDM leased lines with modern high-speed Carrier Ethernet."
            },
            {
                "title": "Configuring Metro Ethernet Uplink on an Enterprise Cisco Router",
                "language": "text",
                "code": "-- Modern Metro Ethernet handoff is a standard RJ-45 or SFP fiber Gigabit interface!\nRouter(config)# interface GigabitEthernet0/0/2\nRouter(config-if)# description Metro-Ethernet-E-Line-to-Headquarters\nRouter(config-if)# ip address 10.254.1.2 255.255.255.252\nRouter(config-if)# speed 1000\nRouter(config-if)# duplex full\nRouter(config-if)# no shutdown\n# No serial encapsulation (HDLC/PPP) needed—it's pure native Ethernet!",
                "explanation": "Configures a high-speed Metro Ethernet WAN interface using standard Layer 3 Ethernet commands."
            },
            {
                "title": "Verifying WAN Link Bandwidth and Errors in Cisco IOS",
                "language": "text",
                "code": "Router# show interfaces GigabitEthernet0/0/2\nGigabitEthernet0/0/2 is up, line protocol is up\n  Hardware is CN Gigabit Ethernet, address is 0014.2201.3333\n  Description: Metro-Ethernet-E-Line-to-Headquarters\n  Internet address is 10.254.1.2/30\n  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec\n     0 input errors, 0 CRC, 0 frame, 0 overrun",
                "explanation": "Verifies that the line protocol is up and confirms zero CRC errors on the fiber WAN handoff."
            },
            {
                "title": "Python T1 vs Metro Ethernet Cost/Speed Efficiency Calculator",
                "language": "python",
                "code": "def compare_wan_efficiency(speed_mbps: float, monthly_cost_usd: float) -> dict:\n    cost_per_mbps = monthly_cost_usd / speed_mbps\n    return {\n        'speed_mbps': speed_mbps,\n        'cost_usd': monthly_cost_usd,\n        'cost_per_mbps_usd': round(cost_per_mbps, 2)\n    }\n\n# T1: 1.54 Mbps at $300/mo ($194/Mbps) vs MetroE: 1000 Mbps at $800/mo ($0.80/Mbps!)\nprint('MetroE Efficiency:', compare_wan_efficiency(1000.0, 800.0))",
                "explanation": "Calculates cost per megabit, demonstrating the financial and bandwidth advantages of Metro Ethernet."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Carrier Bandwidth Standard Mapper",
            description="Write a Python function `get_legacy_wan_speed(carrier_code: str) -> float` that returns `1.544` for `'T1'`, `2.048` for `'E1'`, `44.736` for `'T3'`, and `0.0` for any unknown carrier acronym.",
            starter_code="def get_legacy_wan_speed(carrier_code: str) -> float:\n    # Return legacy speed in Mbps\n    pass",
            solution_code="def get_legacy_wan_speed(carrier_code: str) -> float:\n    mapping = {'T1': 1.544, 'E1': 2.048, 'T3': 44.736, 'E3': 34.368}\n    return mapping.get(carrier_code.strip().upper(), 0.0)",
            expected_output="get_legacy_wan_speed('T1') == 1.544, get_legacy_wan_speed('E1') == 2.048"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the dedicated bandwidth speed of a standard North American T1 leased line?",
                options=[
                    "1.544 Mbps",
                    "100 Mbps",
                    "10.0 Mbps",
                    "44.736 Mbps"
                ],
                correct_answer="1.544 Mbps",
                explanation="A T1 line bundles 24 DS0 channels (64 kbps each + 8 kbps framing) to yield 1.544 Mbps."
            ),
            QuizQuestionBlueprint(
                question="Why has Metro Ethernet largely replaced traditional legacy serial leased lines (T1/T3) in modern WAN deployments?",
                options=[
                    "It offers vastly higher bandwidth (from 10 Mbps to 100 Gbps) at much lower cost and connects using standard Ethernet switch ports",
                    "It requires no cables",
                    "It only works on satellites",
                    "It was invented by telephone companies in 1920"
                ],
                correct_answer="It offers vastly higher bandwidth (from 10 Mbps to 100 Gbps) at much lower cost and connects using standard Ethernet switch ports",
                explanation="Metro Ethernet delivers gigabit speeds over standard Ethernet interfaces without expensive serial hardware."
            ),
            QuizQuestionBlueprint(
                question="In Metro Ethernet terminology (MEF), what service type provides a direct point-to-point connection between two corporate sites (acting like a long virtual Ethernet cable)?",
                options=[
                    "E-Line (Ethernet Private Line)",
                    "E-LAN (Ethernet Private LAN)",
                    "E-Tree",
                    "Wi-Fi 6"
                ],
                correct_answer="E-Line (Ethernet Private Line)",
                explanation="E-Line provides point-to-point Layer 2 Ethernet connectivity between two customer premises."
            ),
            QuizQuestionBlueprint(
                question="What MEF service type connects multiple branch offices into a multipoint-to-multipoint shared Layer 2 broadcast domain?",
                options=[
                    "E-LAN (Ethernet Private LAN)",
                    "E-Line",
                    "T1",
                    "DSL"
                ],
                correct_answer="E-LAN (Ethernet Private LAN)",
                explanation="E-LAN creates a multipoint Layer 2 network, behaving like a single distributed switch across sites."
            ),
            QuizQuestionBlueprint(
                question="What is the bandwidth capacity of an E1 line used predominantly in Europe and international telecommunications?",
                options=[
                    "2.048 Mbps",
                    "1.544 Mbps",
                    "10.0 Mbps",
                    "54.0 Mbps"
                ],
                correct_answer="2.048 Mbps",
                explanation="An E1 line bundles 32 channels of 64 kbps each, delivering 2.048 Mbps."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 43
    # -------------------------------------------------------------
    DayBlueprint(
        order=43,
        title="Day 43: MPLS (Multiprotocol Label Switching Architecture)",
        concept="High-speed label switching: Layer 2.5 architecture, Label Distribution Protocol (LDP), Label Edge Routers (LER / PE), Label Switching Routers (LSR / P), and MPLS VPNs",
        analogy="Think of MPLS like luggage sorting at a mega airport. In standard IP routing, at every single conveyor belt intersection, a postal worker must unpack the luggage, read the full 30-word passenger home address (**IP Routing Table Lookup - Slow!**), and re-tape the box. In **MPLS**, at the check-in desk (**Label Edge Router**), a barcode sticker (**MPLS Label: #501**) is slapped on the handle. Subsequent conveyor workers (**Label Switch Routers**) only look at barcode #501—swapping it in 1 microsecond without reading the address!",
        theory_sections=[
            {
                "heading": "What is MPLS? The Layer 2.5 Shim Header",
                "body": "Multiprotocol Label Switching (MPLS) is a high-performance forwarding technology operating between Layer 2 (Data Link) and Layer 3 (Network). Instead of inspecting long IP headers and performing complex routing table lookups at every intermediate hop, MPLS inserts a 32-bit **MPLS Label (Shim Header)** into the packet at the network ingress, forwarding packets using fast hardware **Label Swapping**."
            },
            {
                "heading": "MPLS Router Roles & L3VPNs",
                "body": "(1) **CE (Customer Edge)**: Customer router on-premises; (2) **PE / LER (Provider Edge / Label Edge Router)**: Service provider boundary router that inspects IP packets, pushes labels (**Push**), or removes labels at egress (**Pop**); (3) **P / LSR (Provider / Label Switching Router)**: Core transit routers that rapidly swap incoming labels for outgoing labels (**Swap**). MPLS enables service providers to offer private, secure **Layer 3 VPNs (MPLS L3VPN)** to multiple enterprises over a single shared core."
            }
        ],
        code_snippets=[
            {
                "title": "32-bit MPLS Shim Header Structure Breakdown",
                "language": "text",
                "code": "MPLS Label Header (Inserted between Layer 2 Ethernet and Layer 3 IP):\n[ Layer 2 Header | MPLS Label (32 Bits / 4 Bytes) | Layer 3 IP Header | Payload ]\n                 │\n                 ├── Label Value (20 Bits): 0 to 1,048,575 (Forwarding identifier)\n                 ├── Traffic Class / EXP (3 Bits): Quality of Service (QoS)\n                 ├── Bottom of Stack / S (1 Bit): 1 if bottom label, 0 if nested label stack\n                 └── Time-To-Live / TTL (8 Bits): Decremented per hop to prevent loops",
                "explanation": "Field specifications for the 32-bit MPLS label header inserted between Layer 2 and Layer 3."
            },
            {
                "title": "Enabling MPLS and LDP on a Cisco Core Router Interface",
                "language": "text",
                "code": "-- Enable CEF (Cisco Express Forwarding) - Mandatory for MPLS\nRouter(config)# ip cef\n\n-- Activate MPLS and Label Distribution Protocol (LDP) on transit links\nRouter(config)# interface GigabitEthernet0/0/0\nRouter(config-if)# mpls ip\nRouter(config-if)# mpls label protocol ldp\nRouter(config-if)# no shutdown",
                "explanation": "Enables Cisco Express Forwarding and turns on LDP label distribution on core interfaces."
            },
            {
                "title": "Inspecting the MPLS Forwarding Table (LFIB)",
                "language": "text",
                "code": "Router# show mpls forwarding-table\nLocal  Outgoing   Prefix            Bytes Label   Outgoing   Next Hop\nLabel  Label      or Tunnel Id      Switched      interface\n16     Pop Label  10.1.1.0/24       14205         Gi0/0/1    192.168.1.2\n17     24         172.16.0.0/16     895000        Gi0/0/2    10.50.1.1\n# 'Local 17 -> Outgoing 24' indicates rapid hardware Label Swapping!",
                "explanation": "Inspects the Label Forwarding Information Base (LFIB) mapping incoming labels to outgoing swap labels."
            },
            {
                "title": "Python MPLS Label Stack Simulator",
                "language": "python",
                "code": "class MplsPacket:\n    def __init__(self, ip_payload: str):\n        self.payload = ip_payload\n        self.label_stack = []\n        \n    def push_label(self, label: int):\n        \"\"\"Executed by Ingress PE Router\"\"\"\n        self.label_stack.append(label)\n        \n    def swap_label(self, new_label: int):\n        \"\"\"Executed by Core P Router\"\"\"\n        if self.label_stack:\n            self.label_stack[-1] = new_label\n            \n    def pop_label(self) -> int:\n        \"\"\"Executed by Egress PE Router\"\"\"\n        return self.label_stack.pop() if self.label_stack else None",
                "explanation": "Python simulation of MPLS Push, Swap, and Pop label operations across network boundaries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="MPLS Label Range Validator",
            description="Write a Python function `is_valid_mpls_label(label: int) -> bool` that verifies whether an integer is within the 20-bit MPLS label space (0 to 1,048,575).",
            starter_code="def is_valid_mpls_label(label: int) -> bool:\n    # Return True if within 20-bit label range\n    pass",
            solution_code="def is_valid_mpls_label(label: int) -> bool:\n    return isinstance(label, int) and 0 <= label <= 1048575",
            expected_output="is_valid_mpls_label(16) == True, is_valid_mpls_label(1048576) == False, is_valid_mpls_label(-1) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="At what conceptual layer of the OSI model does MPLS operate?",
                options=[
                    "Layer 2.5 (between Layer 2 Data Link and Layer 3 Network)",
                    "Layer 7 (Application)",
                    "Layer 1 (Physical only)",
                    "Layer 4 (Transport)"
                ],
                correct_answer="Layer 2.5 (between Layer 2 Data Link and Layer 3 Network)",
                explanation="MPLS is termed 'Layer 2.5' because its shim header sits between Layer 2 and Layer 3."
            ),
            QuizQuestionBlueprint(
                question="How large is an individual standard MPLS label in bits (and bytes)?",
                options=[
                    "32 bits (4 bytes), with a 20-bit label value field",
                    "128 bits",
                    "64 bits",
                    "16 bits"
                ],
                correct_answer="32 bits (4 bytes), with a 20-bit label value field",
                explanation="An MPLS shim header is 32 bits long, containing a 20-bit label value, 3-bit EXP, 1-bit S, and 8-bit TTL."
            ),
            QuizQuestionBlueprint(
                question="What label operation is performed by an Ingress Provider Edge (PE) router when receiving an unlabelled IP packet from a customer?",
                options=[
                    "PUSH (inserts an MPLS label header)",
                    "POP (removes label)",
                    "SWAP (replaces label)",
                    "DROP"
                ],
                correct_answer="PUSH (inserts an MPLS label header)",
                explanation="The ingress PE router pushes an MPLS label onto incoming customer IP packets."
            ),
            QuizQuestionBlueprint(
                question="What protocol is used by MPLS-enabled routers to negotiate and distribute label bindings to their neighbors?",
                options=[
                    "LDP (Label Distribution Protocol)",
                    "BGP",
                    "DHCP",
                    "ARP"
                ],
                correct_answer="LDP (Label Distribution Protocol)",
                explanation="LDP distributes label-to-prefix mappings between adjacent Label Switch Routers."
            ),
            QuizQuestionBlueprint(
                question="What is the primary operational advantage of MPLS in service provider backbones?",
                options=[
                    "Extremely fast hardware label-switching without re-examining routing tables at every hop, and scalable Layer 3 VPN isolation",
                    "It eliminates the need for routers",
                    "It converts electricity into wireless signals",
                    "It gives free internet to all customers"
                ],
                correct_answer="Extremely fast hardware label-switching without re-examining routing tables at every hop, and scalable Layer 3 VPN isolation",
                explanation="MPLS provides high-speed forwarding and enables isolated multi-tenant enterprise VPN services."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 44
    # -------------------------------------------------------------
    DayBlueprint(
        order=44,
        title="Day 44: PPPoE (Point-to-Point Protocol over Ethernet)",
        concept="Broadband residential connectivity: Encapsulating PPP within Ethernet frames, PPPoE Active Discovery (PADI, PADO, PADR, PADS), MTU 1492 constraints, and authentication (PAP/CHAP)",
        analogy="Think of PPPoE like sending a sealed private courier envelope inside an open public school bus. The school bus (**Ethernet**) stops at everyone's house and drops off multiple kids (**multi-access network**). But your bank demands a private two-person contract (**Point-to-Point Protocol**) with personal username and password authentication before opening an account. **PPPoE** wraps that private authenticated two-person contract inside the school bus frame so your DSL/Fiber modem can authenticate with your ISP!",
        theory_sections=[
            {
                "heading": "Why PPPoE? Authenticating Broadband Customers",
                "body": "Ethernet does not natively support user authentication (usernames and passwords), metering, or session billing. The legacy Point-to-Point Protocol (PPP) natively supported **PAP and CHAP authentication**, but only ran over serial cables. **PPPoE (PPP over Ethernet - RFC 2516)** encapsulates PPP frames inside standard Ethernet frames, allowing DSL and Fiber-to-the-Home (FTTH) ISPs to authenticate individual subscribers, track billing, and assign dynamic IP addresses."
            },
            {
                "heading": "The 8-Byte Overhead & MTU 1492 Rule",
                "body": "Standard Ethernet has an MTU of 1500 bytes. The PPPoE header consumes **6 bytes**, and the internal PPP protocol ID consumes **2 bytes** (Total = 8 bytes). Therefore, **the Maximum Transmission Unit for PPPoE connections is strictly 1492 bytes (1500 - 8)**. If a router does not adjust the TCP Maximum Segment Size (MSS) via `ip tcp adjust-mss 1452`, web browsing will hang on large packets."
            }
        ],
        code_snippets=[
            {
                "title": "PPPoE Active Discovery Stage (PAD Sequence)",
                "language": "text",
                "code": "Client Host                                            ISP Access Concentrator (BRAS)\n  │                                                          │\n  │ ── 1. PADI (PPPoE Active Discovery Initiation - Bcast) ─>│ (Client broadcasts for BRAS)\n  │                                                          │\n  │ <── 2. PADO (PPPoE Active Discovery Offer - Unicast) ───│ (BRAS responds with offer)\n  │                                                          │\n  │ ── 3. PADR (PPPoE Active Discovery Request) ────────────>│ (Client requests session)\n  │                                                          │\n  │ <── 4. PADS (PPPoE Active Discovery Session-confirmation)│ (Session ID assigned!)\n  │                                                          │\n  └─── [ PPP LCP & CHAP Authentication Negotiates -> IP Assigned ] ───┘",
                "explanation": "Illustrates the 4-step PPPoE Active Discovery sequence establishing a session ID."
            },
            {
                "title": "Configuring PPPoE Client with Dialer Interface (Cisco IOS)",
                "language": "text",
                "code": "-- Step 1: Configure physical Ethernet interface connecting to DSL/Fiber modem\nRouter(config)# interface GigabitEthernet0/0/1\nRouter(config-if)# description Connected-to-FTTH-Modem\nRouter(config-if)# no ip address\nRouter(config-if)# pppoe-client dial-pool-number 1\nRouter(config-if)# no shutdown\n\n-- Step 2: Configure logical Dialer interface with CHAP authentication & MTU 1492\nRouter(config)# interface Dialer 1\nRouter(config-if)# ip address negotiated          -- Obtains IP via IPCP from ISP\nRouter(config-if)# mtu 1492                       -- Mandatory 8-byte reduction!\nRouter(config-if)# ip tcp adjust-mss 1452         -- Prevents web page hanging\nRouter(config-if)# encapsulation ppp\nRouter(config-if)# dialer pool 1\nRouter(config-if)# ppp chap hostname customer_user@isp.net\nRouter(config-if)# ppp chap password SuperSecretIspPassword",
                "explanation": "Complete configuration of a Cisco PPPoE client dialer interface with CHAP credentials and MTU adjustments."
            },
            {
                "title": "Verifying Active PPPoE Session and Dialer Status",
                "language": "text",
                "code": "Router# show pppoe session\n     1 client session, total 1 session\nSession Id    Binding CoS   Remote MAC      Local MAC       Intf\n142           Dialer1       0050.56e8.1102  0014.2201.3333  Gi0/0/1\n# 'Session Id 142' confirms active authenticated PPPoE broadband connection!",
                "explanation": "Confirms established session ID and binding between physical interface and logical Dialer."
            },
            {
                "title": "Python PPPoE Header & MTU Calculation Helper",
                "language": "python",
                "code": "def calculate_pppoe_mtu(standard_ethernet_mtu: int = 1500) -> dict:\n    pppoe_header_bytes = 6\n    ppp_protocol_bytes = 2\n    overhead = pppoe_header_bytes + ppp_protocol_bytes  # 8 bytes\n    optimal_mtu = standard_ethernet_mtu - overhead      # 1492 bytes\n    optimal_mss = optimal_mtu - 40                      # 1452 bytes (subtract IP + TCP headers)\n    \n    return {\n        'pppoe_mtu': optimal_mtu,\n        'pppoe_overhead': overhead,\n        'optimal_tcp_mss': optimal_mss\n    }\n\nprint(calculate_pppoe_mtu()) # Output: {'pppoe_mtu': 1492, 'optimal_tcp_mss': 1452}",
                "explanation": "Calculates the mandatory 8-byte MTU reduction and 1452-byte TCP MSS clamping for PPPoE."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="PPPoE MTU Calculator",
            description="Write a Python function `get_pppoe_mtu(ethernet_mtu: int = 1500) -> int` that subtracts the 8-byte PPPoE encapsulation overhead from standard MTU.",
            starter_code="def get_pppoe_mtu(ethernet_mtu: int = 1500) -> int:\n    # Calculate PPPoE MTU\n    pass",
            solution_code="def get_pppoe_mtu(ethernet_mtu: int = 1500) -> int:\n    return ethernet_mtu - 8",
            expected_output="get_pppoe_mtu(1500) == 1492, get_pppoe_mtu(9000) == 8992"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is the maximum MTU on a standard PPPoE connection set to 1492 bytes instead of 1500 bytes?",
                options=[
                    "Because the PPPoE header (6 bytes) and PPP protocol ID (2 bytes) consume 8 bytes of encapsulation overhead from the 1500-byte Ethernet frame",
                    "To save electricity on the router",
                    "Because telephone cables cannot transmit more than 1492 bytes",
                    "It is a random number chosen by ISPs"
                ],
                correct_answer="Because the PPPoE header (6 bytes) and PPP protocol ID (2 bytes) consume 8 bytes of encapsulation overhead from the 1500-byte Ethernet frame",
                explanation="1500 byte standard MTU minus 8 bytes of PPPoE overhead equals exactly 1492 bytes."
            ),
            QuizQuestionBlueprint(
                question="Why do broadband Internet Service Providers (ISPs) use PPPoE on residential DSL and fiber connections?",
                options=[
                    "To authenticate individual subscriber sessions with usernames and passwords (PAP/CHAP) and meter data usage for billing",
                    "Because Ethernet cables don't work without PPPoE",
                    "To turn on Wi-Fi automatically",
                    "To convert digital signals into analog"
                ],
                correct_answer="To authenticate individual subscriber sessions with usernames and passwords (PAP/CHAP) and meter data usage for billing",
                explanation="PPPoE adds user authentication (PAP/CHAP) and session accounting to standard Ethernet."
            ),
            QuizQuestionBlueprint(
                question="What initial packet does a PPPoE client broadcast onto the network to discover available ISP Access Concentrators?",
                options=[
                    "PADI (PPPoE Active Discovery Initiation)",
                    "PADO (Offer)",
                    "PADR (Request)",
                    "PADS (Session)"
                ],
                correct_answer="PADI (PPPoE Active Discovery Initiation)",
                explanation="PADI is the initial broadcast sent by the client to locate an available BRAS."
            ),
            QuizQuestionBlueprint(
                question="What Cisco command prevents web pages from hanging or failing to load over PPPoE by clamping the TCP segment size?",
                options=[
                    "ip tcp adjust-mss 1452",
                    "no ip routing",
                    "speed 1000",
                    "duplex full"
                ],
                correct_answer="ip tcp adjust-mss 1452",
                explanation="`ip tcp adjust-mss 1452` rewrites the SYN packet MSS option to fit within 1492 MTU."
            ),
            QuizQuestionBlueprint(
                question="What virtual logical interface is configured on a Cisco router to handle PPPoE connection state and credentials?",
                options=[
                    "Dialer Interface (e.g. `interface Dialer 1`)",
                    "Loopback Interface",
                    "Null Interface",
                    "VLAN Interface"
                ],
                correct_answer="Dialer Interface (e.g. `interface Dialer 1`)",
                explanation="Dialer interfaces manage PPP authentication, negotiated IP acquisition, and MTU settings."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 45
    # -------------------------------------------------------------
    DayBlueprint(
        order=45,
        title="Day 45: SD-WAN (Software-Defined Wide Area Networking)",
        concept="The revolution in enterprise WAN: Decoupling Control Plane from Data Plane, Overlay vs Underlay, Application-Aware Routing, and Zero Touch Provisioning (ZTP)",
        analogy="Think of traditional WAN routing like hiring 100 truck drivers where each driver navigates purely by looking at printed paper maps in their hands. If an expensive toll bridge (**MPLS Circuit**) has light traffic, all drivers take it, racking up massive bills while the adjacent free public highway (**Commodity Broadband**) sits completely empty! **SD-WAN** is a central robotic dispatch computer with live satellite feeds: it steers encrypted traffic over the cheapest broadband highway for YouTube and automatically redirects crystal-clear Zoom video to MPLS the second jitter occurs (**Application-Aware Routing**)!",
        theory_sections=[
            {
                "heading": "Underlay vs Overlay Architecture",
                "body": "In SD-WAN: (1) The **Underlay Network** represents the physical transport circuits (MPLS links, broadband fiber, 4G/5G cellular, satellite); (2) The **Overlay Network** is an automated mesh of dynamic encrypted tunnels (IPsec/GRE) constructed over the underlay. SD-WAN abstracts the physical transport, treating all connections as an active-active pool of bandwidth."
            },
            {
                "heading": "Cisco SD-WAN (Viptela) Component Planes",
                "body": "(1) **Management Plane (vManage)**: Single pane of glass web GUI for centralized configuration and monitoring; (2) **Control Plane (vSmart)**: Central brain that distributes routing policies and encryption keys via **OMP (Overlay Management Protocol)**; (3) **Data Plane (vEdge / cEdge)**: Physical or virtual routers at branches that forward traffic; (4) **Orchestration Plane (vBond)**: Authenticates devices and facilitates **Zero-Touch Provisioning (ZTP)**."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco SD-WAN Plane Architecture Component Chart",
                "language": "text",
                "code": "Plane             Component Name   Primary Function\nManagement Plane  vManage          Single GUI dashboard for centralized policy & telemetry\nControl Plane     vSmart           Central brain: calculates topology & distributes routes (OMP)\nOrchestration     vBond            Gatekeeper: authenticates devices & facilitates ZTP discovery\nData Plane        vEdge / cEdge    Branch & Data Center routers executing IPsec forwarding",
                "explanation": "Reference chart summarizing the 4 decoupled architectural planes of Cisco SD-WAN."
            },
            {
                "title": "Simulating Application-Aware Routing (AAR) Policy in Python",
                "language": "python",
                "code": "def evaluate_aar_policy(latency_ms: float, loss_percent: float, jitter_ms: float) -> str:\n    \"\"\"SLA Requirements for Voice/VoIP: Latency < 150ms, Loss < 1%, Jitter < 30ms\"\"\"\n    if latency_ms < 150 and loss_percent < 1.0 and jitter_ms < 30:\n        return 'Forward via High-Speed Broadband Underlay (SLA Met)'\n    else:\n        return 'SLA Violated! Dynamically Steering Voice to Premium MPLS Underlay'",
                "explanation": "Demonstrates real-time telemetry-based path steering driven by application SLA policies."
            },
            {
                "title": "Inspecting SD-WAN Control Connections via CLI (vEdge)",
                "language": "text",
                "code": "vEdge# show control connections\nPEER    PEER             PEER       SITE        DOMAIN  PEER             PRIV  PEER\nTYPE    ORGANIZATION     PRIV IP    ID          ID      PUB IP           PORT  STATE\nvbond   Hunar-Corp       10.1.1.1   0           0       203.0.113.10     12346 up\nvmanage Hunar-Corp       10.1.1.2   0           0       203.0.113.11     12346 up\nvsmart  Hunar-Corp       10.1.1.3   0           1       203.0.113.12     12346 up\n# 'State up' proves router authenticated and received routing policies via OMP!",
                "explanation": "Confirms established control connections to vBond, vManage, and vSmart controllers."
            },
            {
                "title": "Inspecting BFD (Bidirectional Forwarding Detection) Tunnel Latency",
                "language": "text",
                "code": "vEdge# show bfd sessions\nSRC IP          DST IP          SYSTEM IP   SITE ID  STATE  LOCAL COLOR    LATENCY  LOSS\n203.0.113.50    198.51.100.2    1.1.1.2     100      up     biz-internet   18 ms    0.0%\n203.0.113.50    198.51.100.3    1.1.1.3     200      up     mpls           12 ms    0.0%",
                "explanation": "Shows real-time BFD probes measuring latency, packet loss, and jitter across underlay tunnels."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SD-WAN SLA Compliance Checker",
            description="Write a Python function `meets_voip_sla(latency: float, jitter: float, packet_loss: float) -> bool` that returns `True` if `latency <= 150.0`, `jitter <= 30.0`, and `packet_loss <= 1.0`.",
            starter_code="def meets_voip_sla(latency: float, jitter: float, packet_loss: float) -> bool:\n    # Return True if SLA parameters satisfy VoIP requirements\n    pass",
            solution_code="def meets_voip_sla(latency: float, jitter: float, packet_loss: float) -> bool:\n    return latency <= 150.0 and jitter <= 30.0 and packet_loss <= 1.0",
            expected_output="meets_voip_sla(120.0, 15.0, 0.2) == True, meets_voip_sla(180.0, 10.0, 0.0) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the foundational architectural principle of Software-Defined WAN (SD-WAN)?",
                options=[
                    "Decoupling the central Control Plane (decision-making) from the distributed Data Plane (packet-forwarding hardware)",
                    "Removing all cables and operating only on 4G",
                    "Replacing all routers with unmanaged hubs",
                    "Making the Internet free of charge"
                ],
                correct_answer="Decoupling the central Control Plane (decision-making) from the distributed Data Plane (packet-forwarding hardware)",
                explanation="SD-WAN abstracts control planes to centralized software controllers, leaving data planes on edge devices."
            ),
            QuizQuestionBlueprint(
                question="In Cisco SD-WAN architecture, which controller acts as the central brain that calculates topology and distributes routing policies via OMP?",
                options=[
                    "vSmart",
                    "vManage",
                    "vBond",
                    "vEdge"
                ],
                correct_answer="vSmart",
                explanation="vSmart is the centralized control-plane engine distributing routes, security policies, and keys."
            ),
            QuizQuestionBlueprint(
                question="What is 'Zero-Touch Provisioning' (ZTP) in modern SD-WAN deployments?",
                options=[
                    "A capability where a new branch router automatically downloads its configuration and joins the enterprise network simply by plugging in power and an Internet cable",
                    "Operating a computer without touching the keyboard",
                    "A wireless router with no buttons",
                    "A tool for deleting configurations"
                ],
                correct_answer="A capability where a new branch router automatically downloads its configuration and joins the enterprise network simply by plugging in power and an Internet cable",
                explanation="ZTP enables non-technical personnel to install branch routers that self-configure upon connecting to the internet."
            ),
            QuizQuestionBlueprint(
                question="What protocol does SD-WAN use to continuously measure real-time latency, jitter, and packet loss across active tunnels for Application-Aware Routing?",
                options=[
                    "BFD (Bidirectional Forwarding Detection)",
                    "SNMP",
                    "Telnet",
                    "FTP"
                ],
                correct_answer="BFD (Bidirectional Forwarding Detection)",
                explanation="BFD probes run across all data tunnels, measuring latency and loss to inform dynamic path steering."
            ),
            QuizQuestionBlueprint(
                question="In SD-WAN terminology, what is the 'Overlay Network'?",
                options=[
                    "The virtual network of dynamic, encrypted IPsec tunnels built on top of physical underlay circuits (broadband, MPLS, LTE)",
                    "The plastic cover placed on top of routers",
                    "The Wi-Fi network in the parking lot",
                    "A backup server"
                ],
                correct_answer="The virtual network of dynamic, encrypted IPsec tunnels built on top of physical underlay circuits (broadband, MPLS, LTE)",
                explanation="The overlay is the software-defined encrypted tunnel fabric running across physical underlay circuits."
            )
        ]
    )
]
