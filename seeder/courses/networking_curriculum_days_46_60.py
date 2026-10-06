"""
Computer Networking Basics 60-Day Curriculum - Part 4 (Days 46 to 60)
Module 8: Network Security (Days 46-51)
Module 9: Optimization & High Availability (Days 52-54)
Module 10: Modern Networking & Automation (Days 55-60)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_46_TO_60 = [
    # -------------------------------------------------------------
    # DAY 46
    # -------------------------------------------------------------
    DayBlueprint(
        order=46,
        title="Day 46: Firewalls (Stateful, Stateless, & Next-Gen NGFW)",
        concept="Network Firewalls and Inspection Architectures: Packet filtering, state tables, deep packet inspection (DPI), and application-layer control",
        analogy="A stateless firewall is like a security guard with a strict guest list who checks your ID every single time you walk in or out, completely oblivious to whether you just stepped outside for 5 seconds to tie your shoes. A stateful firewall is like a vigilant bouncer who remembers you entered 5 minutes ago and automatically allows your return traffic because an established session exists in his memory. A Next-Generation Firewall (NGFW) is like an airport TSA checkpoint with X-ray scanners, sniffing dogs, and facial recognition: it inspects luggage down to Layer 7 application payloads, detecting viruses and unauthorized applications even if they disguise themselves on open HTTP/HTTPS ports.",
        theory_sections=[
            {
                "heading": "Firewall Evolution: Packet Filters vs Stateful Inspection",
                "body": "A **Stateless Firewall** (Packet Filter) evaluates every incoming and outgoing packet in total isolation. It checks Layer 3 and Layer 4 headers against access control rules (source/dest IP, source/dest port, protocol). Because it maintains no memory of connection state, return traffic for an outbound HTTP request must be explicitly permitted with a reverse rule, creating severe security vulnerabilities.\n\nA **Stateful Firewall** keeps a dynamically updated **State Table** (Connection Table) in RAM. When an internal host initiates an outbound TCP 3-way handshake or UDP request, the firewall records the session (Source IP/Port, Destination IP/Port, Sequence numbers, TCP flags). Inbound return traffic matching an active, established connection is automatically permitted without requiring clumsy, permissive inbound ACLs."
            },
            {
                "heading": "Next-Generation Firewalls (NGFW) & Deep Packet Inspection",
                "body": "Traditional port-based firewalls are easily circumvented by applications using standard ports (e.g., BitTorrent or malware tunnels over TCP port 443 HTTPS). **Next-Generation Firewalls (NGFWs)** (such as Palo Alto Networks, Fortinet FortiGate, and Cisco Secure Firewall) incorporate:\n- **Deep Packet Inspection (DPI)**: Scrutinizes Layer 7 application payloads beyond TCP/UDP headers.\n- **Application Visibility & Control (AVC / App-ID)**: Identifies actual software signatures (e.g., Skype vs Facebook vs SSH) regardless of port or encryption.\n- **Integrated Threat Prevention**: Bundles Intrusion Prevention Systems (IPS), real-time antivirus, anti-spyware, and URL filtering directly into the hardware pipeline.\n- **SSL/TLS Decryption**: Terminates encrypted client-server sessions to scan decrypted payloads before re-encrypting them."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco ASA / FTD Stateful Inspection Configuration",
                "language": "cisco",
                "code": "# Inspect TCP and UDP state globally on Cisco ASA\nciscoasa(config)# class-map inspection_default\nciscoasa(config-cmap)# match default-inspection-traffic\nciscoasa(config-cmap)# exit\nciscoasa(config)# policy-map global_policy\nciscoasa(config-pmap)# class inspection_default\nciscoasa(config-pmap-c)# inspect http\nciscoasa(config-pmap-c)# inspect dns\nciscoasa(config-pmap-c)# inspect icmp\nciscoasa(config-pmap-c)# exit\nciscoasa(config)# service-policy global_policy global",
                "explanation": "Enables application-aware stateful inspection engines on a Cisco ASA security appliance."
            },
            {
                "title": "Linux iptables Stateful Connection Tracking Rules",
                "language": "bash",
                "code": "# Flush existing rules\niptables -F\n\n# Allow loopback\niptables -A INPUT -i lo -j ACCEPT\n\n# Allow return traffic for ESTABLISHED and RELATED sessions\niptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT\n\n# Allow new incoming SSH connections on port 22\niptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT\n\n# Drop everything else\niptables -P INPUT DROP",
                "explanation": "Uses the Linux Netfilter conntrack module to enforce stateful firewalling."
            },
            {
                "title": "Inspecting the Linux conntrack Table",
                "language": "bash",
                "code": "# View live connection state table entries\nsudo conntrack -L\n# Output:\n# tcp 6 431999 ESTABLISHED src=192.168.1.50 dst=93.184.216.34 sport=54210 dport=443 [ASSURED]",
                "explanation": "Queries the active Linux kernel state table tracking active Layer 4 connections."
            },
            {
                "title": "Python Script: Basic Stateful Connection Tracker Simulator",
                "language": "python",
                "code": "state_table = {}\n\ndef process_packet(src_ip, dst_ip, src_port, dst_port, flag):\n    flow_key = (src_ip, dst_ip, src_port, dst_port)\n    reverse_key = (dst_ip, src_ip, dst_port, src_port)\n\n    if flag == 'SYN':\n        state_table[flow_key] = 'SYN_SENT'\n        return 'OUTBOUND ALLOWED (New Session)'\n    elif flag == 'SYN-ACK' and reverse_key in state_table:\n        state_table[flow_key] = 'ESTABLISHED'\n        return 'INBOUND ALLOWED (State matched)'\n    elif reverse_key in state_table or flow_key in state_table:\n        return 'TRAFFIC ALLOWED (Session active)'\n    return 'BLOCKED (Untracked state)'\n\nprint(process_packet('10.0.0.5', '8.8.8.8', 50000, 53, 'SYN'))\nprint(process_packet('8.8.8.8', '10.0.0.5', 53, 50000, 'SYN-ACK'))",
                "explanation": "Demonstrates how stateful firewalls record bidirectional flow tuples to permit legitimate return packets."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Stateful Packet Filtering Simulator",
            description="Implement a Python function `evaluate_firewall_rule(packet: dict, state_table: set) -> str` that acts as a stateful firewall. `packet` is a dictionary: `{'direction': 'inbound'|'outbound', 'src': ip, 'dst': ip, 'port': int, 'is_new': bool}`. If `direction == 'outbound'` and `is_new == True`, add `(dst, src, port)` to `state_table` and return `'PERMIT_NEW'`. If `direction == 'inbound'`, check if `(src, dst, port)` exists in `state_table`; if yes, return `'PERMIT_ESTABLISHED'`. Otherwise, return `'DENY_UNSOLICITED'`.",
            starter_code="def evaluate_firewall_rule(packet: dict, state_table: set) -> str:\n    # Write stateful firewall evaluation logic\n    pass",
            solution_code="def evaluate_firewall_rule(packet: dict, state_table: set) -> str:\n    direction = packet.get('direction')\n    src = packet.get('src')\n    dst = packet.get('dst')\n    port = packet.get('port')\n    is_new = packet.get('is_new', False)\n\n    if direction == 'outbound' and is_new:\n        state_table.add((dst, src, port))\n        return 'PERMIT_NEW'\n    elif direction == 'inbound':\n        if (src, dst, port) in state_table:\n            return 'PERMIT_ESTABLISHED'\n        return 'DENY_UNSOLICITED'\n    return 'DENY_DEFAULT'",
            expected_output="PERMIT_NEW\nPERMIT_ESTABLISHED\nDENY_UNSOLICITED"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What fundamental capability distinguishes a stateful firewall from a stateless packet filter?",
                options=[
                    "A stateful firewall maintains a dynamic state table to track established active sessions and allow return traffic automatically",
                    "A stateful firewall inspects optical fiber light wavelengths instead of electrical voltage levels",
                    "A stateful firewall cannot block ports higher than 1024",
                    "A stateful firewall requires every packet to be manually signed with an SSH private key"
                ],
                correct_answer="A stateful firewall maintains a dynamic state table to track established active sessions and allow return traffic automatically",
                explanation="Stateful inspection tracks TCP sequence numbers and UDP flow tuples in an active state table, permitting legitimate return traffic automatically."
            ),
            QuizQuestionBlueprint(
                question="Which feature is a defining attribute of a Next-Generation Firewall (NGFW) compared to a legacy stateful firewall?",
                options=[
                    "Deep Packet Inspection (DPI) and Layer 7 Application Visibility & Control (AVC)",
                    "Replacing Ethernet MAC addresses with serial numbers",
                    "Inability to filter IPv4 addresses",
                    "Limiting network bandwidth to 10 Mbps maximum"
                ],
                correct_answer="Deep Packet Inspection (DPI) and Layer 7 Application Visibility & Control (AVC)",
                explanation="NGFWs identify specific applications at Layer 7 and perform deep payload inspection regardless of the port number used."
            ),
            QuizQuestionBlueprint(
                question="In Linux iptables, which connection state flag matches incoming packets that belong to a pre-existing, established connection?",
                options=[
                    "ESTABLISHED",
                    "SYN_RECEIVED",
                    "TRANSPARENT",
                    "PASSIVE"
                ],
                correct_answer="ESTABLISHED",
                explanation="The conntrack state 'ESTABLISHED' denotes packets associated with a two-way connection that has already seen traffic in both directions."
            ),
            QuizQuestionBlueprint(
                question="What security issue occurs if a network relies purely on stateless packet filters without tracking session states?",
                options=[
                    "High-numbered ephemeral return ports must be left wide open inbound, exposing internal endpoints to port scans and unauthorized probes",
                    "The router completely disables Layer 2 ARP broadcasts",
                    "Switches will enter half-duplex mode automatically",
                    "Ethernet cables overheat due to excessive voltage"
                ],
                correct_answer="High-numbered ephemeral return ports must be left wide open inbound, exposing internal endpoints to port scans and unauthorized probes",
                explanation="Because stateless filters cannot know if an inbound packet is a legitimate reply, administrators are forced to leave high ports open inbound, creating dangerous vulnerabilities."
            ),
            QuizQuestionBlueprint(
                question="Why is SSL/TLS decryption necessary on modern Next-Generation Firewalls?",
                options=[
                    "Because over 85% of web and enterprise traffic is encrypted with TLS, blinding inspection engines unless traffic is decrypted and inspected for malware",
                    "Because TLS prevents routers from reading Layer 3 IP headers",
                    "Because Ethernet frames cannot transport encrypted bytes without dropping packets",
                    "Because TLS certificates expire every 5 minutes"
                ],
                correct_answer="Because over 85% of web and enterprise traffic is encrypted with TLS, blinding inspection engines unless traffic is decrypted and inspected for malware",
                explanation="Without TLS decryption, encrypted payloads pass through firewalls as unreadable ciphertext, preventing the detection of malware or data exfiltration."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 47
    # -------------------------------------------------------------
    DayBlueprint(
        order=47,
        title="Day 47: ACLs (Access Control Lists - Standard & Extended)",
        concept="Access Control Lists and Packet Filtering: Standard vs Extended ACLs, wildcard masks, and interface placement rules",
        analogy="An Access Control List (ACL) is like a VIP nightclub door policy written on an index card. A Standard ACL is like a crude rule that only checks the guest's home town (Source IP address only): 'If you are from Springfield, you cannot enter.' An Extended ACL is a comprehensive background check: 'Guests from Springfield can only enter if they are wearing a tuxedo (Protocol TCP), coming between 8 PM and 2 AM, and heading specifically to Table 80 (Destination IP & Port).'",
        theory_sections=[
            {
                "heading": "Standard vs Extended Access Control Lists",
                "body": "Access Control Lists (ACLs) are ordered lists of permit and deny statements applied to router/switch interfaces:\n- **Standard ACLs (Numbered 1-99 & 1300-1999)**: Filter traffic based **strictly on Source IPv4 Address**. They cannot filter by destination IP, protocol (TCP/UDP), or port numbers. Rule of thumb: Place Standard ACLs **as close to the destination as possible** to avoid accidentally blocking valid traffic to other destinations.\n- **Extended ACLs (Numbered 100-199 & 2000-2699)**: Filter traffic based on **Source IP, Destination IP, Protocol (IP, TCP, UDP, ICMP), and Source/Destination Port numbers**. Rule of thumb: Place Extended ACLs **as close to the source as possible** to drop unwanted traffic before it consumes network bandwidth."
            },
            {
                "heading": "Wildcard Masks & The Implicit Deny",
                "body": "Cisco ACLs use **Wildcard Masks** (inverted subnet masks) to determine which bits must match:\n- `0` bit = Must match exactly.\n- `1` bit = Ignore (don't care bit).\nExample: Subnet mask `255.255.255.0` inverted is Wildcard Mask `0.0.0.255` (`255.255.255.255 - Subnet Mask`).\n- A single host (`/32`) uses wildcard `0.0.0.0` or keyword `host`.\n- Any IP (`0.0.0.0/0`) uses wildcard `255.255.255.255` or keyword `any`.\n\n**Crucial Rule**: Every Cisco ACL ends with an invisible, silent **implicit deny all** (`deny ip any any`). If a packet does not match any permit statement in the ACL, it is discarded immediately."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: Standard Numbered & Named ACL Configuration",
                "language": "cisco",
                "code": "# Numbered Standard ACL (1-99)\nRouter(config)# access-list 10 deny 192.168.1.50 0.0.0.0\nRouter(config)# access-list 10 permit 192.168.1.0 0.0.0.255\nRouter(config)# access-list 10 deny any\n\n# Named Standard ACL\nRouter(config)# ip access-list standard BLOCK_FINANCE_PC\nRouter(config-std-nacl)# 10 deny host 10.1.1.99\nRouter(config-std-nacl)# 20 permit any\nRouter(config)# interface GigabitEthernet0/0\nRouter(config-if)# ip access-group BLOCK_FINANCE_PC out",
                "explanation": "Standard ACLs match source addresses only and are placed closest to the destination."
            },
            {
                "title": "Cisco IOS: Extended Named ACL Configuration",
                "language": "cisco",
                "code": "Router(config)# ip access-list extended FILTER_WEB_SERVICES\n# Allow internal LAN (172.16.10.0/24) to reach Web Server 203.0.113.10 on HTTP/HTTPS\nRouter(config-ext-nacl)# permit tcp 172.16.10.0 0.0.0.255 host 203.0.113.10 eq 80\nRouter(config-ext-nacl)# permit tcp 172.16.10.0 0.0.0.255 host 203.0.113.10 eq 443\n# Deny any other traffic from that subnet to the server\nRouter(config-ext-nacl)# deny ip 172.16.10.0 0.0.0.255 host 203.0.113.10\n# Permit all other outbound internet traffic\nRouter(config-ext-nacl)# permit ip any any\n\n# Apply inbound on ingress interface\nRouter(config)# interface GigabitEthernet0/1\nRouter(config-if)# ip access-group FILTER_WEB_SERVICES in",
                "explanation": "Extended ACL specifies Layer 3 source/destination and Layer 4 protocol ports."
            },
            {
                "title": "Verifying ACLs on Cisco IOS",
                "language": "cisco",
                "code": "Router# show ip access-lists\n# Extended IP access list FILTER_WEB_SERVICES\n#     10 permit tcp 172.16.10.0 0.0.0.255 host 203.0.113.10 eq www (452 matches)\n#     20 permit tcp 172.16.10.0 0.0.0.255 host 203.0.113.10 eq 443 (1893 matches)\n#     30 deny ip 172.16.10.0 0.0.0.255 host 203.0.113.10 (37 matches)\n#     40 permit ip any any (8240 matches)",
                "explanation": "Displays hit counters for each access-list statement to verify rule efficacy."
            },
            {
                "title": "Python Script: Calculating Wildcard Masks from Subnet Masks",
                "language": "python",
                "code": "def subnet_to_wildcard(subnet_mask: str) -> str:\n    mask_octets = [int(o) for o in subnet_mask.split('.')]\n    wildcard_octets = [255 - o for o in mask_octets]\n    return '.'.join(str(w) for w in wildcard_octets)\n\nprint('/24 (255.255.255.0) -> Wildcard:', subnet_to_wildcard('255.255.255.0'))\nprint('/28 (255.255.255.240)-> Wildcard:', subnet_to_wildcard('255.255.255.240'))\nprint('/30 (255.255.255.252)-> Wildcard:', subnet_to_wildcard('255.255.255.252'))",
                "explanation": "Calculates wildcard masks by subtracting each subnet mask octet from 255."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cisco Wildcard Mask Calculator",
            description="Write a Python function `get_cisco_wildcard(prefix_length: int) -> str` that converts a CIDR prefix length (e.g., 24, 26, 30) into its exact 4-octet Cisco wildcard mask string.",
            starter_code="def get_cisco_wildcard(prefix_length: int) -> str:\n    # Convert CIDR prefix length (0-32) to wildcard mask string\n    pass",
            solution_code="def get_cisco_wildcard(prefix_length: int) -> str:\n    wildcard_int = (1 << (32 - prefix_length)) - 1\n    octets = [\n        (wildcard_int >> 24) & 0xFF,\n        (wildcard_int >> 16) & 0xFF,\n        (wildcard_int >> 8) & 0xFF,\n        wildcard_int & 0xFF\n    ]\n    return f'{octets[0]}.{octets[1]}.{octets[2]}.{octets[3]}'",
            expected_output="0.0.0.255\n0.0.0.63\n0.0.0.3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between a Standard ACL and an Extended ACL in Cisco IOS?",
                options=[
                    "Standard ACLs can only filter on Source IP address, whereas Extended ACLs filter on Source IP, Destination IP, Protocol, and Port numbers",
                    "Standard ACLs use letters, while Extended ACLs only use Roman numerals",
                    "Standard ACLs operate at Layer 7, while Extended ACLs operate at Layer 1",
                    "Standard ACLs can only be applied on trunk ports"
                ],
                correct_answer="Standard ACLs can only filter on Source IP address, whereas Extended ACLs filter on Source IP, Destination IP, Protocol, and Port numbers",
                explanation="Standard ACLs check only source IPv4 addresses; Extended ACLs inspect full Layer 3 source/destination and Layer 4 protocol/port information."
            ),
            QuizQuestionBlueprint(
                question="Where is the best practice location to place an Extended ACL?",
                options=[
                    "As close to the source of the traffic as possible",
                    "As close to the destination of the traffic as possible",
                    "On the ISP root DNS server",
                    "Directly on the workstation's display adapter"
                ],
                correct_answer="As close to the source of the traffic as possible",
                explanation="Extended ACLs should be placed close to the source to discard prohibited traffic immediately before it traverses the network core."
            ),
            QuizQuestionBlueprint(
                question="What is the wildcard mask for a /27 subnet mask (255.255.255.224)?",
                options=[
                    "0.0.0.31",
                    "0.0.0.224",
                    "0.0.0.63",
                    "255.255.255.0"
                ],
                correct_answer="0.0.0.31",
                explanation="255 - 224 = 31, so the wildcard mask for a /27 subnet is 0.0.0.31."
            ),
            QuizQuestionBlueprint(
                question="What happens to a packet that does not match any explicit permit or deny statements in a Cisco ACL?",
                options=[
                    "It is silently dropped by the invisible implicit deny at the end of the ACL",
                    "It is broadcasted to all VLANs across the campus",
                    "It is automatically encrypted and sent to the cloud",
                    "It is forwarded directly to the console port"
                ],
                correct_answer="It is silently dropped by the invisible implicit deny at the end of the ACL",
                explanation="All Cisco ACLs end with an implicit 'deny ip any any' rule; any unmatched packet is discarded."
            ),
            QuizQuestionBlueprint(
                question="Which number range represents standard numbered IPv4 ACLs in Cisco IOS?",
                options=[
                    "1-99 and 1300-1999",
                    "100-199 and 2000-2699",
                    "500-599",
                    "60000-65535"
                ],
                correct_answer="1-99 and 1300-1999",
                explanation="Cisco IOS reserves numbers 1-99 and expanded range 1300-1999 for Standard IPv4 ACLs."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 48
    # -------------------------------------------------------------
    DayBlueprint(
        order=48,
        title="Day 48: VPNs (Site-to-Site, Remote Access, IPsec, & SSL/TLS)",
        concept="Virtual Private Networks and Cryptographic Tunnels: Site-to-site vs remote access, IPsec (IKE, ESP, AH), and SSL/TLS VPNs",
        analogy="Sending raw data over the public Internet is like sending a handwritten postcard: every mail carrier, sorter, and passerby can read your secrets or alter the message. A VPN is like placing your letters inside an armored, tamper-evident courier box with heavy combination locks. Even though the box travels in an ordinary postal delivery truck across open public highways, no outsider can read inside or alter the contents without breaking the encryption.",
        theory_sections=[
            {
                "heading": "VPN Types: Site-to-Site vs Remote Access",
                "body": "A **Virtual Private Network (VPN)** extends a private network across a public network by encrypting data packets:\n- **Site-to-Site VPN**: Connects two fixed physical networks (e.g., Branch Office router to Corporate Headquarters firewall). The edge routers/firewalls encrypt and decrypt traffic automatically; individual end-user PCs require no special software.\n- **Remote Access VPN**: Connects mobile teleworkers or travelers to the enterprise intranet. Users install client software (e.g., Cisco AnyConnect, WireGuard, OpenVPN) to build an encrypted tunnel from their laptop to the corporate gateway."
            },
            {
                "heading": "IPsec Framework & SSL/TLS VPNs",
                "body": "**IPsec (Internet Protocol Security)** operates at Layer 3 and secures any IP protocol:\n- **IKE (Internet Key Exchange - IKEv1/IKEv2)**: Negotiates security associations (SAs), authenticates peers (Pre-Shared Key or RSA certificates), and performs Diffie-Hellman (DH) key exchange.\n- **ESP (Encapsulating Security Payload - IP protocol 50)**: Provides data confidentiality (AES encryption), integrity, and authentication (SHA-256 HMAC).\n- **AH (Authentication Header - IP protocol 51)**: Provides integrity and authentication only (no encryption; rarely used today).\n- **Tunnel Mode vs Transport Mode**: Tunnel mode encrypts the entire original IP packet (adding a brand-new outer IP header); transport mode encrypts only the payload.\n\n**SSL/TLS VPNs**: Operate at the transport/session layer (TCP 443). They easily traverse NAT and firewalls without requiring complex UDP/IP protocol permissions."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: IPsec Site-to-Site VPN (IKEv2) Configuration",
                "language": "cisco",
                "code": "# 1. Define IKEv2 Proposal & Policy\ncrypto ikev2 proposal IKE2_PROP\n encryption aes-cbc-256\n integrity sha256\n group 14\n!\n# 2. Define Transform Set for ESP\ncrypto ipsec transform-set TS_AES256_SHA esp-aes 256 esp-sha256-hmac\n mode tunnel\n!\n# 3. Crypto Map linking ACL & Peer IP\ncrypto map IPSEC_MAP 10 ipsec-isakmp\n set peer 203.0.113.2\n set transform-set TS_AES256_SHA\n match address VPN_INTERESTING_TRAFFIC\n!\n# Apply to WAN interface\ninterface GigabitEthernet0/0\n crypto map IPSEC_MAP",
                "explanation": "Configures modern IKEv2 IPsec tunnel mode encryption between two Cisco routers."
            },
            {
                "title": "WireGuard VPN Server Configuration (wg0.conf)",
                "language": "ini",
                "code": "[Interface]\nAddress = 10.8.0.1/24\nListenPort = 51820\nPrivateKey = aAAAa1111...ServerPrivateKey...\n\n[Peer]\n# Remote Mobile Client\nPublicKey = bBBBb2222...ClientPublicKey...\nAllowedIPs = 10.8.0.2/32",
                "explanation": "Modern lightweight WireGuard VPN server configuration using Curve25519 public-key cryptography."
            },
            {
                "title": "Verifying Active IPsec Security Associations (SAs)",
                "language": "cisco",
                "code": "Router# show crypto ipsec sa\ninterface: GigabitEthernet0/0\n    Crypto map tag: IPSEC_MAP, local addr 198.51.100.1\n   #pkts encaps: 14205, #pkts encrypt: 14205\n   #pkts decaps: 13980, #pkts decrypt: 13980",
                "explanation": "Checks active IPsec tunnel packet counters, encryption/decryption stats, and peer SA state."
            },
            {
                "title": "Python Script: Calculating HMAC-SHA256 Packet Integrity",
                "language": "python",
                "code": "import hmac\nimport hashlib\n\nshared_key = b'SuperSecretVPNPreSharedKey'\npacket_data = b'SRC=192.168.1.10;DST=192.168.2.20;PAYLOAD=SalaryReport'\n\n# Generate HMAC (Integrity check tag)\nmac = hmac.new(shared_key, packet_data, hashlib.sha256).hexdigest()\nprint('Packet Integrity HMAC:', mac)\n\n# Verification\nverify_mac = hmac.new(shared_key, packet_data, hashlib.sha256).hexdigest()\nprint('Valid match?', hmac.compare_digest(mac, verify_mac))",
                "explanation": "Simulates IPsec packet integrity verification using SHA256 HMAC hashing."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="IPsec Tunnel Health Monitor",
            description="Write a Python function `check_ipsec_status(tunnel_stats: dict) -> dict` that evaluates IPsec tunnel health. If `encaps > 0`, `decaps > 0`, and `errors == 0`, return `{'status': 'UP', 'health': 'EXCELLENT'}`. If `errors > 0` but less than `encaps`, return `{'status': 'UP', 'health': 'DEGRADED'}`. Otherwise, return `{'status': 'DOWN', 'health': 'CRITICAL'}`.",
            starter_code="def check_ipsec_status(tunnel_stats: dict) -> dict:\n    # Evaluate tunnel health based on encapsulation, decapsulation, and error counters\n    pass",
            solution_code="def check_ipsec_status(tunnel_stats: dict) -> dict:\n    encaps = tunnel_stats.get('encaps', 0)\n    decaps = tunnel_stats.get('decaps', 0)\n    errors = tunnel_stats.get('errors', 0)\n\n    if encaps > 0 and decaps > 0 and errors == 0:\n        return {'status': 'UP', 'health': 'EXCELLENT'}\n    elif errors > 0 and errors < encaps:\n        return {'status': 'UP', 'health': 'DEGRADED'}\n    return {'status': 'DOWN', 'health': 'CRITICAL'}",
            expected_output="{'status': 'UP', 'health': 'EXCELLENT'}\n{'status': 'UP', 'health': 'DEGRADED'}\n{'status': 'DOWN', 'health': 'CRITICAL'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which IPsec protocol provides both data confidentiality (encryption) and data integrity?",
                options=[
                    "ESP (Encapsulating Security Payload - IP Protocol 50)",
                    "AH (Authentication Header - IP Protocol 51)",
                    "RIP (Routing Information Protocol)",
                    "DHCP (Dynamic Host Configuration Protocol)"
                ],
                correct_answer="ESP (Encapsulating Security Payload - IP Protocol 50)",
                explanation="ESP provides confidentiality through symmetric encryption (AES) and integrity through HMAC hashing. AH provides integrity but no encryption."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between IPsec Tunnel Mode and IPsec Transport Mode?",
                options=[
                    "Tunnel Mode encrypts the entire original IP packet and adds a new outer IP header; Transport Mode encrypts only the payload",
                    "Tunnel mode requires physical copper tunnels under the building",
                    "Transport mode can only be used on airplanes",
                    "Tunnel mode converts IPv4 addresses into MAC addresses"
                ],
                correct_answer="Tunnel Mode encrypts the entire original IP packet and adds a new outer IP header; Transport Mode encrypts only the payload",
                explanation="In Tunnel Mode, the entire original IP packet (header and payload) is encapsulated and encrypted inside a new IP packet, ideal for site-to-site VPNs."
            ),
            QuizQuestionBlueprint(
                question="Which protocol handles automated peer authentication and symmetric key exchange in an IPsec connection?",
                options=[
                    "IKE (Internet Key Exchange / ISAKMP)",
                    "DNS (Domain Name System)",
                    "BGP (Border Gateway Protocol)",
                    "ARP (Address Resolution Protocol)"
                ],
                correct_answer="IKE (Internet Key Exchange / ISAKMP)",
                explanation="IKE (IKEv1 / IKEv2) authenticates endpoints and securely negotiates cryptographic session keys using Diffie-Hellman."
            ),
            QuizQuestionBlueprint(
                question="Why are SSL/TLS VPNs (like Cisco AnyConnect or OpenVPN on port 443) popular for remote teleworkers?",
                options=[
                    "TCP port 443 (HTTPS) easily traverses NAT gateways and restrictive hotel/coffee-shop firewalls without requiring special firewall exceptions",
                    "SSL VPNs eliminate the need for computer passwords",
                    "SSL VPNs bypass physics to achieve speeds faster than light",
                    "SSL VPNs only work when routers are powered off"
                ],
                correct_answer="TCP port 443 (HTTPS) easily traverses NAT gateways and restrictive hotel/coffee-shop firewalls without requiring special firewall exceptions",
                explanation="Because port 443 is universally open for HTTPS web traffic, SSL/TLS VPNs reliably connect from remote networks where IPsec protocol 50 (ESP) is blocked."
            ),
            QuizQuestionBlueprint(
                question="What type of VPN connects a branch office corporate network directly to headquarters without requiring VPN client software on each individual PC?",
                options=[
                    "Site-to-Site VPN",
                    "Remote Access VPN",
                    "Peer-to-Peer Tor Network",
                    "Bluetooth Personal Area Network"
                ],
                correct_answer="Site-to-Site VPN",
                explanation="Site-to-Site VPNs terminate on gateway routers or firewalls at each site, transparently encrypting LAN-to-LAN traffic."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 49
    # -------------------------------------------------------------
    DayBlueprint(
        order=49,
        title="Day 49: AAA Framework (RADIUS & TACACS+)",
        concept="Centralized Identity and Access Management: Authentication, Authorization, Accounting, and protocol comparison",
        analogy="Imagine entering a high-security research laboratory: Authentication ('Who are you?') is the front guard inspecting your photo ID and fingerprint. Authorization ('What are you allowed to touch?') is your keycard opening Door 4B while prohibiting entry to the radioactive vault. Accounting ('What did you actually do?') is the surveillance log recording the exact second you unlocked the door, which buttons you pressed, and when you left.",
        theory_sections=[
            {
                "heading": "The AAA Security Architecture",
                "body": "In enterprise networks with hundreds of switches and routers, configuring local user accounts on every device is unmanageable and insecure. The **AAA framework** centralizes network device administration:\n- **Authentication**: Verifies credentials (username, password, MFA token, digital certificate).\n- **Authorization**: Determines what commands, privilege levels, or network resources the authenticated user is allowed to execute.\n- **Accounting**: Tracks and audits user activity, session durations, commands typed, and bandwidth consumed for compliance."
            },
            {
                "heading": "RADIUS vs TACACS+: Core Differences",
                "body": "Two major protocols implement AAA across enterprise infrastructure:\n1. **TACACS+ (Terminal Access Controller Access-Control System Plus)**:\n   - Cisco proprietary (now open RFC).\n   - **Separates Authentication, Authorization, and Accounting** into independent functions.\n   - Uses **TCP port 49** (reliable delivery).\n   - **Encrypts the entire packet payload** (only a standard header is cleartext).\n   - Gold standard for **Device Administration** (controlling CLI commands run by network engineers).\n2. **RADIUS (Remote Authentication Dial-In User Service)**:\n   - Open IETF standard (RFC 2865/2866).\n   - **Combines Authentication and Authorization** into a single request/response step.\n   - Uses **UDP ports 1812 (Auth) & 1813 (Accounting)** (or legacy 1645/1646).\n   - **Encrypts only the password field**; usernames and attributes remain unencrypted.\n   - Gold standard for **Network Access** (802.1X Wi-Fi, VPN logins, wired port authentication)."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: Configuring TACACS+ for Device Administration",
                "language": "cisco",
                "code": "# 1. Enable AAA subsystem\nRouter(config)# aaa new-model\n\n# 2. Define TACACS+ Server (Cisco ISE)\nRouter(config)# tacacs server ISE_PRIMARY\nRouter(config-server-tacacs)# address ipv4 10.1.10.50\nRouter(config-server-tacacs)# key CiscoTacacsKey123\n\n# 3. Configure AAA Authentication method list with local fallback\nRouter(config)# aaa authentication login default group tacacs+ local\n\n# 4. Configure Command Authorization (Privilege 15 commands)\nRouter(config)# aaa authorization exec default group tacacs+ local\nRouter(config)# aaa authorization commands 15 default group tacacs+ local\n\n# 5. Configure Command Accounting\nRouter(config)# aaa accounting commands 15 default start-stop group tacacs+",
                "explanation": "Forces CLI logins and privilege 15 commands to authenticate against an ISE TACACS+ server with local fallback."
            },
            {
                "title": "Cisco IOS: Configuring RADIUS for 802.1X Port Authentication",
                "language": "cisco",
                "code": "Switch(config)# aaa new-model\nSwitch(config)# radius server FREERADIUS_SRV\nSwitch(config-radius-server)# address ipv4 192.168.1.100 auth-port 1812 acct-port 1813\nSwitch(config-radius-server)# key RadiusSharedSecret99\n\nSwitch(config)# aaa authentication dot1x default group radius\nSwitch(config)# dot1x system-auth-control",
                "explanation": "Directs 802.1X switch port access requests to a central RADIUS authentication server."
            },
            {
                "title": "Verifying AAA Authentication Status on Cisco IOS",
                "language": "cisco",
                "code": "Router# show aaa servers\nRADIUS: id 1, priority 1, host 192.168.1.100, auth-port 1812, acct-port 1813\n     State: current UP, authen: count 452\nTACACS+: id 1, priority 1, host 10.1.10.50, port 49\n     State: current UP, authen: count 129, autor: count 820",
                "explanation": "Verifies connectivity and response times to configured TACACS+ and RADIUS servers."
            },
            {
                "title": "Python Script: Simulating AAA Access Request",
                "language": "python",
                "code": "def simulate_aaa_login(user: str, password: str, command: str) -> dict:\n    user_db = {'admin_alice': {'pw': 'Secr3t!', 'role': 'superadmin', 'priv': 15}}\n    if user not in user_db or user_db[user]['pw'] != password:\n        return {'authen': 'FAILED', 'authz': 'DENIED'}\n    user_info = user_db[user]\n    is_reload_allowed = user_info['priv'] >= 15\n    authz = 'ALLOWED' if (command != 'reload' or is_reload_allowed) else 'DENIED'\n    return {'authen': 'SUCCESS', 'authz': authz, 'accounting': f'USER={user} CMD={command}'}\n\nprint(simulate_aaa_login('admin_alice', 'Secr3t!', 'show running-config'))",
                "explanation": "Demonstrates the independent evaluation steps of the AAA framework."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="TACACS+ Command Authorization Simulator",
            description="Write a Python function `authorize_command(username: str, command: str, user_privileges: dict) -> bool`. `user_privileges` maps usernames to integer privilege levels (e.g., `{'alice': 15, 'bob': 7, 'carol': 1}`). If `command.startswith('show')`, allow for priv >= 1. If `command.startswith('configure')`, allow for priv >= 10. If `command.startswith('reload')`, allow only for priv == 15. Return `True` if authorized, otherwise `False`.",
            starter_code="def authorize_command(username: str, command: str, user_privileges: dict) -> bool:\n    # Return True if user has sufficient privilege level for the command\n    pass",
            solution_code="def authorize_command(username: str, command: str, user_privileges: dict) -> bool:\n    priv = user_privileges.get(username, 0)\n    if command.startswith('reload'):\n        return priv == 15\n    elif command.startswith('configure'):\n        return priv >= 10\n    elif command.startswith('show'):\n        return priv >= 1\n    return False",
            expected_output="True\nFalse\nTrue"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the 'AAA' security framework stand for?",
                options=[
                    "Authentication, Authorization, and Accounting",
                    "Automatic Address Allocation",
                    "Advanced Access Architecture",
                    "Application Acceleration Algorithm"
                ],
                correct_answer="Authentication, Authorization, and Accounting",
                explanation="AAA stands for Authentication (identity check), Authorization (permission check), and Accounting (activity tracking)."
            ),
            QuizQuestionBlueprint(
                question="Which protocol encrypts the ENTIRE packet payload and separates Authentication, Authorization, and Accounting into distinct functions?",
                options=[
                    "TACACS+",
                    "RADIUS",
                    "SNMPv1",
                    "Telnet"
                ],
                correct_answer="TACACS+",
                explanation="TACACS+ uses TCP port 49, completely encrypts the entire packet payload, and allows modular separation of authentication and per-command authorization."
            ),
            QuizQuestionBlueprint(
                question="What transport protocol and standard UDP ports are utilized by modern RADIUS implementations?",
                options=[
                    "UDP ports 1812 (Authentication) and 1813 (Accounting)",
                    "TCP port 22 and 23",
                    "UDP port 53 and 67",
                    "ICMP Protocol 1"
                ],
                correct_answer="UDP ports 1812 (Authentication) and 1813 (Accounting)",
                explanation="Standard RADIUS uses UDP 1812 for authentication/authorization and UDP 1813 for accounting messages."
            ),
            QuizQuestionBlueprint(
                question="Why is TACACS+ typically favored over RADIUS for network device administration (CLI access)?",
                options=[
                    "It allows granular command-by-command authorization (preventing unauthorized users from running destructive commands like 'reload')",
                    "It consumes 0% CPU on switches",
                    "It allows unencrypted passwords over Wi-Fi",
                    "It requires no server hardware to function"
                ],
                correct_answer="It allows granular command-by-command authorization (preventing unauthorized users from running destructive commands like 'reload')",
                explanation="TACACS+ queries the server before every single command entered in the CLI to verify if the user's role permits that specific command."
            ),
            QuizQuestionBlueprint(
                question="Why is 'local' fallback configuration (e.g. 'group tacacs+ local') critical in Cisco AAA?",
                options=[
                    "To prevent network administrators from being locked out of network devices if the central TACACS+ server goes offline",
                    "To bypass switch passwords during holidays",
                    "To convert the switch into an access point",
                    "To increase Ethernet port speed to 100 Gbps"
                ],
                correct_answer="To prevent network administrators from being locked out of network devices if the central TACACS+ server goes offline",
                explanation="If the AAA server is unreachable, the router falls back to local database accounts so administrators can still log in to repair the outage."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 50
    # -------------------------------------------------------------
    DayBlueprint(
        order=50,
        title="Day 50: Layer 2 Security (Port Security, DHCP Snooping, & DAI)",
        concept="Switchport Security and Layer 2 Attack Mitigation: CAM table overflows, rogue DHCP servers, and ARP spoofing prevention",
        analogy="An unhardened Layer 2 switch is like an open, trusting apartment building where anyone can slip on a fake delivery uniform, shout fake announcements, or plug in a rogue power generator. Port Security is like an electronic lock on each apartment door that only opens for registered residents' keycards. DHCP Snooping is like stationing a guard who inspects any lease contract: only leases signed by the certified landlord (trusted DHCP server) are recognized. Dynamic ARP Inspection (DAI) is like a notary public who checks every ID card against the official tenant directory before letting anyone claim they own an apartment.",
        theory_sections=[
            {
                "heading": "Layer 2 Vulnerabilities & Port Security",
                "body": "Because Layer 2 was designed for cooperative LANs, switches are vulnerable to malicious spoofing:\n- **MAC Flooding Attack**: An attacker uses tools (like `macof`) to flood a switch with thousands of bogus MAC addresses, overflowing the CAM table. The switch enters fail-open mode, acting like a hub and broadcasting all private frames to all ports.\n- **Port Security Solution**: Restricts the number of MAC addresses learned on an access switchport (e.g., maximum 1 or 2). It can dynamically learn MAC addresses or use `sticky` learning. Violation modes:\n  - `protect`: Drops unauthorized frames; no syslog message.\n  - `restrict`: Drops unauthorized frames, sends SNMP trap/syslog message, increments counter.\n  - `shutdown`: Disables port immediately into `err-disabled` state."
            },
            {
                "heading": "DHCP Snooping & Dynamic ARP Inspection (DAI)",
                "body": "- **DHCP Snooping**: Prevents rogue DHCP servers and DHCP starvation attacks. Switchports are classified as **Trusted** (facing genuine DHCP servers/uplinks) or **Untrusted** (facing regular end users). Untrusted ports are blocked from sending DHCP server messages (DHCPOFFER, DHCPACK). The switch monitors DHCP traffic to build the **DHCP Snooping Binding Database** (MAC, IP, Lease Time, VLAN, Port).\n\n- **Dynamic ARP Inspection (DAI)**: Mitigates ARP Spoofing / Man-In-The-Middle (MITM) poisoning. The switch intercepts all ARP requests/replies on untrusted ports and compares the sender MAC and IP against the trusted DHCP Snooping Binding Database. If the sender IP and MAC do not match, the forged ARP packet is dropped."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: Switchport Port Security Configuration",
                "language": "cisco",
                "code": "Switch(config)# interface range GigabitEthernet0/1 - 24\nSwitch(config-if-range)# switchport mode access\nSwitch(config-if-range)# switchport port-security\nSwitch(config-if-range)# switchport port-security maximum 2\nSwitch(config-if-range)# switchport port-security mac-address sticky\nSwitch(config-if-range)# switchport port-security violation shutdown",
                "explanation": "Configures sticky MAC learning and puts the port into err-disabled state upon security violation."
            },
            {
                "title": "Cisco IOS: Configuring DHCP Snooping & Trusting Uplink",
                "language": "cisco",
                "code": "# Enable DHCP snooping globally and for VLAN 10\nSwitch(config)# ip dhcp snooping\nSwitch(config)# ip dhcp snooping vlan 10\n\n# Trust the uplink port facing the authentic DHCP server\nSwitch(config)# interface GigabitEthernet0/24\nSwitch(config-if)# ip dhcp snooping trust\n\n# Rate-limit untrusted client access ports to prevent starvation\nSwitch(config)# interface GigabitEthernet0/1\nSwitch(config-if)# ip dhcp snooping limit rate 15",
                "explanation": "Allows DHCP offer messages strictly through Gi0/24 and blocks rogue DHCP servers on client access ports."
            },
            {
                "title": "Cisco IOS: Dynamic ARP Inspection (DAI) Configuration",
                "language": "cisco",
                "code": "# Enable DAI on VLAN 10 (requires DHCP Snooping)\nSwitch(config)# ip arp inspection vlan 10\n\n# Trust the core router uplink interface\nSwitch(config)# interface GigabitEthernet0/24\nSwitch(config-if)# ip arp inspection trust",
                "explanation": "Enforces hardware verification of ARP packets against the DHCP snooping table."
            },
            {
                "title": "Python Script: Simulating DAI Inspection Logic",
                "language": "python",
                "code": "snooping_binding = {'00:1A:2B:3C:4D:5E': '192.168.1.100'}\n\ndef dynamic_arp_inspection(sender_mac: str, sender_ip: str) -> str:\n    if sender_mac in snooping_binding:\n        if snooping_binding[sender_mac] == sender_ip:\n            return 'DAI: PERMIT - Valid ARP'\n        return f'DAI: DROP - IP Spoofing Detected! {sender_mac} claims {sender_ip}'\n    return f'DAI: DROP - Unregistered MAC {sender_mac}'\n\nprint(dynamic_arp_inspection('00:1A:2B:3C:4D:5E', '192.168.1.100'))\nprint(dynamic_arp_inspection('00:1A:2B:3C:4D:5E', '192.168.1.1'))",
                "explanation": "Demonstrates how DAI drops ARP poisoning packets that fail to match the binding table."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DHCP Snooping Message Filter",
            description="Write a Python function `validate_dhcp_response(interface_type: str, message_type: str) -> bool`. `interface_type` is either `'trusted'` or `'untrusted'`. `message_type` can be `'DISCOVER'`, `'REQUEST'`, `'OFFER'`, or `'ACK'`. Server messages (`OFFER` and `ACK`) are only allowed on `'trusted'` interfaces. Client messages are allowed on both. Return `True` if permitted, `False` if dropped.",
            starter_code="def validate_dhcp_response(interface_type: str, message_type: str) -> bool:\n    # Return True if message is allowed under DHCP snooping rules\n    pass",
            solution_code="def validate_dhcp_response(interface_type: str, message_type: str) -> bool:\n    server_msgs = {'OFFER', 'ACK'}\n    if message_type in server_msgs:\n        return interface_type == 'trusted'\n    return True",
            expected_output="False\nTrue\nTrue"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What security hazard does Cisco Port Security primarily prevent?",
                options=[
                    "MAC flooding attacks designed to overflow switch CAM memory and force unicast flooding",
                    "Physical copper corrosion inside RJ-45 jacks",
                    "Layer 3 OSPF route recalculations",
                    "Excessive screen brightness on client monitors"
                ],
                correct_answer="MAC flooding attacks designed to overflow switch CAM memory and force unicast flooding",
                explanation="Port Security restricts the number of MAC addresses learned per port, thwarting CAM overflow attacks."
            ),
            QuizQuestionBlueprint(
                question="What action does a switch take when a port security violation occurs under 'shutdown' mode?",
                options=[
                    "The port is immediately transitioned into an err-disabled state and shut down",
                    "The switch continues forwarding packets while rebooting itself",
                    "The switch uninstalls its operating system",
                    "The port changes its speed to 10 Gbps"
                ],
                correct_answer="The port is immediately transitioned into an err-disabled state and shut down",
                explanation="Under shutdown mode, the switch immediately disables the port (err-disabled) and sends an SNMP trap/syslog message."
            ),
            QuizQuestionBlueprint(
                question="What is the role of DHCP Snooping in a Layer 2 switched network?",
                options=[
                    "It blocks unauthorized (rogue) DHCP servers on untrusted ports and builds a binding database of IP-to-MAC assignments",
                    "It encrypts all DHCP payloads with 4096-bit RSA keys",
                    "It replaces Ethernet headers with Wi-Fi beacons",
                    "It shuts down the router when an IP address expires"
                ],
                correct_answer="It blocks unauthorized (rogue) DHCP servers on untrusted ports and builds a binding database of IP-to-MAC assignments",
                explanation="DHCP snooping drops DHCPOFFER/ACK messages from untrusted ports and records legitimate IP-MAC-Port leases in its binding table."
            ),
            QuizQuestionBlueprint(
                question="Which underlying database is utilized by Dynamic ARP Inspection (DAI) to validate ARP packets?",
                options=[
                    "The DHCP Snooping Binding Database",
                    "The OSPF Link-State Database",
                    "The BGP Routing Information Base",
                    "The Spanning Tree Bridge ID Table"
                ],
                correct_answer="The DHCP Snooping Binding Database",
                explanation="DAI checks ARP request/response IP-and-MAC bindings against the dynamic DHCP Snooping table to prevent ARP poisoning."
            ),
            QuizQuestionBlueprint(
                question="What is a 'sticky' MAC address in Cisco Port Security?",
                options=[
                    "A dynamically learned MAC address that is automatically converted and written into the switch's running configuration",
                    "A MAC address permanently glued to the physical cable",
                    "A broadcast MAC address (FF:FF:FF:FF:FF:FF)",
                    "A MAC address that belongs exclusively to virtual machines"
                ],
                correct_answer="A dynamically learned MAC address that is automatically converted and written into the switch's running configuration",
                explanation="'switchport port-security mac-address sticky' converts learned dynamic MACs into running-config entries, retaining them across reboots if saved."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 51
    # -------------------------------------------------------------
    DayBlueprint(
        order=51,
        title="Day 51: IDS & IPS (Intrusion Detection vs Intrusion Prevention)",
        concept="Network Intrusion Detection and Prevention Systems: In-line vs out-of-band, signature vs anomaly detection, and SPAN port mirroring",
        analogy="An IDS (Intrusion Detection System) is like a CCTV security camera monitored by a guard. If a burglar smashes a storefront window, the guard watches it happen on the screen, rings an alarm bell, and logs a report—but the thief has already grabbed the jewelry and fled. An IPS (Intrusion Prevention System) is like a bulletproof biometric turnstile placed directly in the doorway: the moment an unauthorized intruder attempts to step through, the mechanical gate locks instantly in real-time, physically stopping the intruder in his tracks before he touches anything inside.",
        theory_sections=[
            {
                "heading": "IDS vs IPS: In-Line Prevention vs Out-of-Band Detection",
                "body": "- **IDS (Out-of-Band / Promiscuous Mode)**: Connected via a switch SPAN/mirror port or network TAP. It receives a duplicate copy of traffic. Because it is out-of-band, it introduces zero network latency. However, it cannot stop an attack mid-stream; it can only generate alerts, send TCP Resets (RST), or trigger ACL updates after the fact.\n\n- **IPS (In-Line Deployment)**: Positioned directly in the physical traffic path (packets enter Port 1 and exit Port 2). Every packet is inspected before forwarding. An IPS can drop malicious packets in real-time, reset TCP sessions, and sanitize protocol anomalies. However, if the IPS CPU overloads or hardware fails without a bypass relay, it becomes a single point of failure and bottleneck."
            },
            {
                "heading": "Detection Methodologies: Signature vs Anomaly-Based",
                "body": "- **Signature-Based Detection**: Compares traffic patterns against a database of known exploit signatures (e.g., regex strings identifying SQL injection, specific malware byte sequences, or buffer overflow payloads). Highly accurate with low false positives, but completely blind to unknown Zero-Day vulnerabilities.\n- **Anomaly / Heuristic-Based Detection**: Establishes a baseline of normal network behavior (bandwidth, protocol distribution, connection rates). Flags any deviation (e.g., sudden burst of 10,000 SYN packets per second or an unusual outbound protocol) as potentially malicious. Detects novel attacks, but produces higher false positive rates."
            }
        ],
        code_snippets=[
            {
                "title": "Snort / Suricata Open-Source IDS/IPS Rule Syntax",
                "language": "bash",
                "code": "# Snort signature detecting SQL Injection in HTTP GET requests\ndrop tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (\n    msg:\"ATTACK [SQLi] - UNION SELECT attempt detected\";\n    flow:established,to_server;\n    content:\"UNION\"; nocase;\n    content:\"SELECT\"; nocase;\n    distance:1;\n    classtype:web-application-attack;\n    sid:1000001;\n    rev:1;\n)",
                "explanation": "Defines an in-line IPS rule that drops established TCP packets carrying a SQL injection payload."
            },
            {
                "title": "Cisco IOS: Switch Port Analyzer (SPAN) for IDS Monitoring",
                "language": "cisco",
                "code": "# Mirror traffic from server ports to an IDS sensor on Gi0/24\nSwitch(config)# monitor session 1 source interface GigabitEthernet0/1 - 4 both\nSwitch(config)# monitor session 1 destination interface GigabitEthernet0/24\n\n# Verify active SPAN session\nSwitch# show monitor session 1",
                "explanation": "Copies all RX and TX traffic from ports 1-4 and forwards it out port 24 to an out-of-band IDS sensor."
            },
            {
                "title": "Python Script: Simple Anomaly-Based Port Scan Detector",
                "language": "python",
                "code": "from collections import defaultdict\nimport time\n\nsyn_counter = defaultdict(list)\nTHRESHOLD = 15\n\ndef inspect_packet(src_ip: str, flag: str) -> str:\n    now = time.time()\n    if flag == 'SYN':\n        syn_counter[src_ip] = [t for t in syn_counter[src_ip] if now - t <= 5.0]\n        syn_counter[src_ip].append(now)\n        if len(syn_counter[src_ip]) > THRESHOLD:\n            return f'ALERT: Port scan from {src_ip}!'\n    return 'NORMAL'",
                "explanation": "Demonstrates behavioral anomaly detection identifying sudden spikes in TCP SYN packets."
            },
            {
                "title": "Viewing Suricata Fast Alert Logs",
                "language": "bash",
                "code": "# Tailing the Suricata fast log in Linux\nsudo tail -f /var/log/suricata/fast.log\n# 09/30-22:15:01 [**] [1:1000001:1] ATTACK [SQLi] - UNION SELECT attempt detected [**] {TCP} 203.0.113.88:49214 -> 192.168.1.10:80",
                "explanation": "Inspects real-time detection alert logs produced by the Suricata network engine."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Signature Matching Engine",
            description="Write a Python function `inspect_payload(payload: str, signatures: list) -> dict`. Each signature is a dict: `{'id': int, 'pattern': str, 'action': 'DROP'|'ALERT'}`. If any `'DROP'` pattern is found in `payload` (case-insensitive), return `{'action': 'DROP', 'matched_id': id}`. If only `'ALERT'` matches, return `{'action': 'ALERT', 'matched_id': id}`. Otherwise return `{'action': 'PASS', 'matched_id': None}`.",
            starter_code="def inspect_payload(payload: str, signatures: list) -> dict:\n    # Check payload against signatures and determine action\n    pass",
            solution_code="def inspect_payload(payload: str, signatures: list) -> dict:\n    lower_payload = payload.lower()\n    alert_match = None\n    for sig in signatures:\n        if sig['pattern'].lower() in lower_payload:\n            if sig['action'] == 'DROP':\n                return {'action': 'DROP', 'matched_id': sig['id']}\n            elif sig['action'] == 'ALERT' and alert_match is None:\n                alert_match = {'action': 'ALERT', 'matched_id': sig['id']}\n    if alert_match:\n        return alert_match\n    return {'action': 'PASS', 'matched_id': None}",
            expected_output="{'action': 'ALERT', 'matched_id': 102}\n{'action': 'DROP', 'matched_id': 101}\n{'action': 'PASS', 'matched_id': None}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the critical architectural difference between an IDS and an IPS?",
                options=[
                    "An IPS is deployed in-line to actively block/drop attacks in real-time, while an IDS is deployed out-of-band to monitor and alert passively",
                    "An IDS uses hardware while an IPS only runs on paper",
                    "An IDS only inspects UDP, while an IPS only inspects ARP",
                    "An IPS cannot be configured with rules"
                ],
                correct_answer="An IPS is deployed in-line to actively block/drop attacks in real-time, while an IDS is deployed out-of-band to monitor and alert passively",
                explanation="IPS sits in-line with the data path and drops malicious frames immediately; IDS sits out-of-band and only alerts."
            ),
            QuizQuestionBlueprint(
                question="Which detection technique is capable of detecting brand-new, previously unseen Zero-Day attacks?",
                options=[
                    "Anomaly-based (Heuristic / Behavioral) detection",
                    "Signature-based detection",
                    "MD5 checksum verification",
                    "Static port filtering"
                ],
                correct_answer="Anomaly-based (Heuristic / Behavioral) detection",
                explanation="Anomaly-based detection flags abnormal traffic behavior deviating from the established baseline, allowing it to catch zero-day attacks with no known signature."
            ),
            QuizQuestionBlueprint(
                question="What Cisco switch feature is used to copy packets from one or more switch ports to an out-of-band IDS sensor?",
                options=[
                    "SPAN (Switch Port Analyzer)",
                    "VLAN Trunking Protocol (VTP)",
                    "Dynamic Trunking Protocol (DTP)",
                    "Power over Ethernet (PoE)"
                ],
                correct_answer="SPAN (Switch Port Analyzer)",
                explanation="SPAN (port mirroring) duplicates traffic passing through designated ports or VLANs and mirrors it out a destination port to an IDS or packet analyzer."
            ),
            QuizQuestionBlueprint(
                question="What is a drawback of deploying an IPS directly in-line on a high-throughput network backbone?",
                options=[
                    "It introduces latency and can become a single point of failure or traffic bottleneck if hardware overloads",
                    "It deletes all IP addresses on the network",
                    "It converts fiber optic links into copper coaxial cables",
                    "It forces all users to change their passwords hourly"
                ],
                correct_answer="It introduces latency and can become a single point of failure or traffic bottleneck if hardware overloads",
                explanation="Because every single packet must be inspected before forwarding, overloaded in-line IPS devices can create throughput bottlenecks or drop valid traffic."
            ),
            QuizQuestionBlueprint(
                question="What is a 'False Positive' in the context of an intrusion detection or prevention system?",
                options=[
                    "The system incorrectly flags benign, harmless user traffic as a malicious attack",
                    "The system completely ignores a real ransomware attack",
                    "The system is powered off during an audit",
                    "The network connection is running at full gigabit speed"
                ],
                correct_answer="The system incorrectly flags benign, harmless user traffic as a malicious attack",
                explanation="A false positive occurs when legitimate, harmless traffic matches a detection rule and triggers a false security alert or unnecessary drop."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 52
    # -------------------------------------------------------------
    DayBlueprint(
        order=52,
        title="Day 52: QoS (Traffic Shaping, Policing, & Classification)",
        concept="Quality of Service: Classification, marking (CoS & DSCP), queuing (LLQ, CBWFQ), traffic policing, and traffic shaping",
        analogy="Imagine a crowded multi-lane highway leading into an international airport terminal during rush hour. Without traffic rules, city buses, heavy freight dump trucks, and screaming ambulances are stuck in the exact same bumper-to-bumper gridlock. QoS is like creating dedicated Priority HOV Lanes for Ambulances (Voice / VoIP) and Flight Crew Shuttles (Interactive Video), while placing Freight Trucks (Background BitTorrent & heavy backups) into slow crawling lanes with strict speed governors.",
        theory_sections=[
            {
                "heading": "QoS Mechanisms: Classification & Marking",
                "body": "When network links congest, routers must drop packets. **Quality of Service (QoS)** ensures critical traffic receives priority:\n- **Classification**: Identifying traffic types (VoIP, Video, Web, FTP) using ACLs or NBAR (Network Based Application Recognition).\n- **Marking**: Tagging packet headers as close to the ingress source as possible:\n  - **Layer 2 (802.1Q CoS)**: 3-bit **Class of Service (CoS)** in the 802.1Q tag (values 0-7, where 5 is Voice).\n  - **Layer 3 (IPv4 ToS / DSCP)**: 6-bit **Differentiated Services Code Point (DSCP)** in the IP header (values 0-63). Standard values include **EF (Expedited Forwarding - DSCP 46)** for low-latency Voice, **AF (Assured Forwarding)** for interactive video, and **CS0 / Best Effort** for standard web traffic."
            },
            {
                "heading": "Congestion Management: Shaping vs Policing & Queuing",
                "body": "- **Policing**: Enforces strict bandwidth limits. When traffic exceeds the configured rate (CIR - Committed Information Rate), excess packets are **immediately dropped** or remarked. Policing produces a jagged 'sawtooth' traffic graph and induces TCP retransmissions.\n\n- **Shaping**: Buffers excess packets in software queues and releases them smoothly over time at the target rate. Shaping smooths out bursty traffic without packet drops, but introduces queuing delay and memory usage.\n\n- **Queuing Algorithms**:\n  - **FIFO (First In, First Out)**: Default; no priority.\n  - **CBWFQ (Class-Based Weighted Fair Queuing)**: Allocates guaranteed bandwidth percentages to distinct traffic classes.\n  - **LLQ (Low Latency Queuing)**: Adds a strict Priority Queue (PQ) on top of CBWFQ specifically for VoIP jitter/delay guarantees."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: Modular QoS CLI (MQC) Configuration for VoIP",
                "language": "cisco",
                "code": "# Step 1: Class Map (Classification)\nRouter(config)# class-map match-any VOICE_TRAFFIC\nRouter(config-cmap)# match ip dscp ef\nRouter(config-cmap)# match protocol rtp audio\n\n# Step 2: Policy Map (Marking & Queuing)\nRouter(config)# policy-map WAN_EDGE_QOS\nRouter(config-pmap)# class VOICE_TRAFFIC\nRouter(config-pmap-c)# priority 500  # 500 Kbps Low Latency Priority Queue\nRouter(config-pmap-c)# exit\nRouter(config-pmap)# class class-default\nRouter(config-pmap-c)# fair-queue\n\n# Step 3: Service Policy (Application to WAN Interface)\nRouter(config)# interface Serial0/0/0\nRouter(config-if)# service-policy output WAN_EDGE_QOS",
                "explanation": "Implements Cisco MQC with Low Latency Queuing (LLQ) guaranteeing 500 Kbps for voice."
            },
            {
                "title": "Cisco IOS: Traffic Shaping vs Policing Example",
                "language": "cisco",
                "code": "# Traffic Policing (Drops bursts above 10 Mbps)\nRouter(config-pmap-c)# police 10000000 conform-action transmit exceed-action drop\n\n# Traffic Shaping (Buffers bursts to smooth to 10 Mbps)\nRouter(config-pmap-c)# shape average 10000000",
                "explanation": "Contrasts immediate packet dropping in policing vs smooth buffering in shaping."
            },
            {
                "title": "Verifying QoS Policy Drops and Matching on Cisco IOS",
                "language": "cisco",
                "code": "Router# show policy-map interface Serial0/0/0\n Serial0/0/0\n  Service-policy output: WAN_EDGE_QOS\n    Class-map: VOICE_TRAFFIC (match-any)\n      154200 packets, 12336000 bytes, drop 0 pkts\n      Priority: 500 kbps, burst bytes 12500\n    Class-map: class-default (match-any)\n      982100 packets, drop 421 pkts",
                "explanation": "Displays real-time packet counters, drop rates, and bandwidth utilization per QoS class."
            },
            {
                "title": "Python Script: Token Bucket Rate Limiter Simulator",
                "language": "python",
                "code": "import time\n\nclass TokenBucket:\n    def __init__(self, capacity: int, fill_rate: float):\n        self.capacity = capacity\n        self.fill_rate = fill_rate\n        self.tokens = capacity\n        self.last_check = time.time()\n\n    def consume(self, tokens_needed: int) -> bool:\n        now = time.time()\n        self.tokens = min(self.capacity, self.tokens + (now - self.last_check) * self.fill_rate)\n        self.last_check = now\n        if self.tokens >= tokens_needed:\n            self.tokens -= tokens_needed\n            return True\n        return False\n\nbucket = TokenBucket(capacity=1000, fill_rate=100.0)\nprint('Allowed?', bucket.consume(600))",
                "explanation": "Simulates the Token Bucket algorithm used inside routers for policing and shaping."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DSCP to CoS Priority Mapping",
            description="Write a Python function `dscp_to_cos(dscp_value: int) -> int` that maps standard DSCP values to 802.1p CoS (0-7): If `dscp_value == 46` (Expedited Forwarding / Voice), return CoS `5`. If `dscp_value in [34, 36, 38]` (Interactive Video), return CoS `4`. If `dscp_value in [26, 28]` (Call Signaling), return CoS `3`. If `dscp_value in [18, 20, 22]`, return CoS `2`. If `dscp_value in [10, 12, 14]`, return CoS `1`. Otherwise (Best Effort / CS0), return CoS `0`.",
            starter_code="def dscp_to_cos(dscp_value: int) -> int:\n    # Return mapped CoS value (0-7)\n    pass",
            solution_code="def dscp_to_cos(dscp_value: int) -> int:\n    if dscp_value == 46:\n        return 5\n    elif dscp_value in [34, 36, 38]:\n        return 4\n    elif dscp_value in [26, 28]:\n        return 3\n    elif dscp_value in [18, 20, 22]:\n        return 2\n    elif dscp_value in [10, 12, 14]:\n        return 1\n    return 0",
            expected_output="5\n4\n0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between Traffic Shaping and Traffic Policing?",
                options=[
                    "Policing immediately drops or remarks packets exceeding the rate limit, while shaping buffers excess packets to smooth egress flow",
                    "Shaping operates only at Layer 1, while policing operates at Layer 7",
                    "Policing requires fiber cables, while shaping requires satellite dishes",
                    "There is no difference; they are identical synonyms"
                ],
                correct_answer="Policing immediately drops or remarks packets exceeding the rate limit, while shaping buffers excess packets to smooth egress flow",
                explanation="Policing enforces hard limits by dropping excess bursts; shaping delays packets in memory buffers to transmit them at a steady rate."
            ),
            QuizQuestionBlueprint(
                question="Which DSCP value and binary standard represents Expedited Forwarding (EF) for voice traffic?",
                options=[
                    "DSCP 46 (101110)",
                    "DSCP 0 (000000)",
                    "DSCP 63 (111111)",
                    "DSCP 8 (001000)"
                ],
                correct_answer="DSCP 46 (101110)",
                explanation="DSCP 46 (Expedited Forwarding / EF) marks high-priority delay-sensitive Voice RTP traffic for strict priority queuing."
            ),
            QuizQuestionBlueprint(
                question="Where is the 3-bit Class of Service (CoS) field located?",
                options=[
                    "Inside the 802.1Q VLAN tag in an Ethernet frame",
                    "In the IPv4 ToS byte",
                    "Inside the TCP sequence number",
                    "In the DNS response record"
                ],
                correct_answer="Inside the 802.1Q VLAN tag in an Ethernet frame",
                explanation="CoS is a 3-bit field (values 0-7) residing within the 802.1Q Layer 2 frame tag."
            ),
            QuizQuestionBlueprint(
                question="Which queuing algorithm introduces a strict Priority Queue (PQ) to guarantee low latency and zero jitter for VoIP?",
                options=[
                    "LLQ (Low Latency Queuing)",
                    "FIFO (First In, First Out)",
                    "Round Robin",
                    "Random Early Detection (RED)"
                ],
                correct_answer="LLQ (Low Latency Queuing)",
                explanation="LLQ combines CBWFQ with a strict priority queue that is always serviced first before other queues, ensuring VoIP packets do not wait."
            ),
            QuizQuestionBlueprint(
                question="What are the three steps in the Cisco Modular QoS CLI (MQC) configuration model?",
                options=[
                    "Class Map (Define), Policy Map (Action), Service Policy (Apply to interface)",
                    "Install, Reboot, Format",
                    "Ping, Traceroute, Telnet",
                    "VLAN, Trunk, VTP"
                ],
                correct_answer="Class Map (Define), Policy Map (Action), Service Policy (Apply to interface)",
                explanation="Cisco MQC follows three steps: 1. Class-map identifies traffic; 2. Policy-map assigns actions/queues; 3. Service-policy binds the policy to an interface."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 53
    # -------------------------------------------------------------
    DayBlueprint(
        order=53,
        title="Day 53: FHRP (HSRP, VRRP, & GLBP)",
        concept="First Hop Redundancy Protocols: Virtual default gateways, preemption, active/standby state machines, and active-active forwarding",
        analogy="Imagine an office building with two receptionists sitting at Front Desk 1 and Front Desk 2. Employees are instructed to deliver letters strictly to 'The Head Receptionist'. Under an FHRP, both receptionists share a single virtual telephone number and uniform. As long as Receptionist 1 is healthy, she answers all incoming calls. If Receptionist 1 suddenly faints, Receptionist 2 immediately steps into her chair and answers that exact same phone number within seconds without any employee ever realizing an outage occurred.",
        theory_sections=[
            {
                "heading": "The Default Gateway Problem & FHRP Solutions",
                "body": "End hosts (PCs, printers, servers) are statically configured or assigned via DHCP a single Default Gateway IP address. If the physical router interface serving as that gateway fails, all hosts lose off-subnet and Internet connectivity. **First Hop Redundancy Protocols (FHRP)** solve this by clustering multiple physical routers into a single **Virtual Router**:\n- A shared **Virtual IP Address** and **Virtual MAC Address** are created.\n- End-user hosts point their default gateway to the Virtual IP.\n- The active physical router answers ARP requests for the Virtual IP and forwards traffic.\n- If the active router fails, the standby router takes over the Virtual IP and MAC transparently."
            },
            {
                "heading": "Protocol Comparison: HSRP vs VRRP vs GLBP",
                "body": "1. **HSRP (Hot Standby Router Protocol)**:\n   - Cisco proprietary (HSRPv1 uses multicast `224.0.0.2`, virtual MAC `0000.0c07.acXX`; HSRPv2 uses `224.0.0.102`, virtual MAC `0000.0c9f.fXXX`).\n   - Elects one **Active** router, one **Standby** router, and remaining routers are in 'Listen' state.\n   - `preempt` command allows a higher-priority router to reclaim the Active role after rebooting.\n2. **VRRP (Virtual Router Redundancy Protocol)**:\n   - Open IETF standard (RFC 5798); multicast `224.0.0.18`, virtual MAC `0000.5e00.01XX`.\n   - Elects one **Master** router and one or more **Backup** routers.\n   - Preemption is enabled by default.\n3. **GLBP (Gateway Load Balancing Protocol)**:\n   - Cisco proprietary.\n   - Elects an **Active Virtual Gateway (AVG)** that assigns distinct virtual MACs to up to 4 **Active Virtual Forwarders (AVFs)**.\n   - Provides true active-active load balancing by replying with different AVF MACs to client ARP queries."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: HSRP Configuration on Router 1 & Router 2",
                "language": "cisco",
                "code": "# Router 1 (Active)\nR1(config)# interface GigabitEthernet0/1\nR1(config-if)# ip address 192.168.1.2 255.255.255.0\nR1(config-if)# standby 1 ip 192.168.1.1\nR1(config-if)# standby 1 priority 110\nR1(config-if)# standby 1 preempt\n\n# Router 2 (Standby)\nR2(config)# interface GigabitEthernet0/1\nR2(config-if)# ip address 192.168.1.3 255.255.255.0\nR2(config-if)# standby 1 ip 192.168.1.1\nR2(config-if)# standby 1 priority 100\nR2(config-if)# standby 1 preempt",
                "explanation": "Configures HSRP Group 1 with Virtual IP 192.168.1.1. R1 has priority 110 and preempts R2."
            },
            {
                "title": "Cisco IOS: VRRPv3 Open Standard Configuration",
                "language": "cisco",
                "code": "# Configure open-standard VRRP on Router 1\nR1(config)# interface GigabitEthernet0/1\nR1(config-if)# vrrp 10 address-family ipv4\nR1(config-if-vrrp)# address 10.0.0.1 primary\nR1(config-if-vrrp)# priority 120",
                "explanation": "Sets up IETF standard VRRP Group 10 with primary virtual gateway 10.0.0.1."
            },
            {
                "title": "Verifying HSRP State and Virtual MAC on Cisco IOS",
                "language": "cisco",
                "code": "R1# show standby brief\nInterface   Grp  Pri P State   Active          Standby         Virtual IP\nGi0/1       1    110 P Active  local           192.168.1.3     192.168.1.1\n\nR1# show standby\nGigabitEthernet0/1 - Group 1 (version 2)\n  Virtual IP address is 192.168.1.1\n  Active virtual MAC address is 0000.0c9f.f001",
                "explanation": "Displays active HSRP group state, virtual MAC address, and standby peer IP."
            },
            {
                "title": "Python Script: Simulating FHRP Heartbeat & Failover",
                "language": "python",
                "code": "class FHRPCluster:\n    def __init__(self, vip: str):\n        self.vip = vip\n        self.active_router = 'R1'\n        self.standby_router = 'R2'\n\n    def send_heartbeat(self, r1_healthy: bool) -> str:\n        if r1_healthy:\n            self.active_router = 'R1'\n            return f'Cluster Stable: Active={self.active_router} forwarding for VIP {self.vip}'\n        else:\n            self.active_router = self.standby_router\n            return f'FAILOVER! R1 down. Standby {self.active_router} promoted to ACTIVE for VIP {self.vip}'\n\ncluster = FHRPCluster('192.168.1.1')\nprint(cluster.send_heartbeat(r1_healthy=True))\nprint(cluster.send_heartbeat(r1_healthy=False))",
                "explanation": "Simulates heartbeat loss and automatic failover of the virtual gateway IP address."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="HSRP Virtual MAC Calculator",
            description="Write a Python function `get_hsrp_v1_mac(group_number: int) -> str` that converts an HSRP group number (0-255) into its standard HSRP version 1 virtual MAC address: `00:00:0c:07:ac:XX` where `XX` is the 2-digit lowercase hex string.",
            starter_code="def get_hsrp_v1_mac(group_number: int) -> str:\n    # Return HSRPv1 virtual MAC address string\n    pass",
            solution_code="def get_hsrp_v1_mac(group_number: int) -> str:\n    hex_group = f'{group_number:02x}'\n    return f'00:00:0c:07:ac:{hex_group}'",
            expected_output="00:00:0c:07:ac:01\n00:00:0c:07:ac:0a\n00:00:0c:07:ac:ff"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What primary networking challenge do FHRP protocols (HSRP, VRRP, GLBP) solve?",
                options=[
                    "Eliminating the single point of failure when a default gateway router interface fails",
                    "Replacing BGP on global transit internet links",
                    "Encrypting Wi-Fi passwords with WPA3",
                    "Assigning public IP addresses to home laptops"
                ],
                correct_answer="Eliminating the single point of failure when a default gateway router interface fails",
                explanation="FHRP provides redundant physical routers backing a single virtual gateway IP so end devices never lose their default gateway."
            ),
            QuizQuestionBlueprint(
                question="What is the open IETF industry standard equivalent of Cisco's proprietary HSRP?",
                options=[
                    "VRRP (Virtual Router Redundancy Protocol)",
                    "GLBP (Gateway Load Balancing Protocol)",
                    "STP (Spanning Tree Protocol)",
                    "OSPF (Open Shortest Path First)"
                ],
                correct_answer="VRRP (Virtual Router Redundancy Protocol)",
                explanation="VRRP (RFC 5798) is the multivendor IETF open standard equivalent to Cisco's proprietary HSRP."
            ),
            QuizQuestionBlueprint(
                question="What happens when an HSRP-enabled router configured with the 'preempt' command reboots and comes back online?",
                options=[
                    "If its configured priority is higher than the currently active router, it immediately reclaims the Active role",
                    "It drops all routes from the routing table",
                    "It forces all workstations to reboot",
                    "It deletes its running configuration"
                ],
                correct_answer="If its configured priority is higher than the currently active router, it immediately reclaims the Active role",
                explanation="Without preempt, an active router remains active even if a higher priority router boots up; with preempt, the higher priority router takes back the active role."
            ),
            QuizQuestionBlueprint(
                question="Which FHRP protocol natively supports true active-active load balancing across up to 4 forwarders simultaneously?",
                options=[
                    "GLBP (Gateway Load Balancing Protocol)",
                    "HSRP version 1",
                    "VRRP version 2",
                    "Standard Static Routing"
                ],
                correct_answer="GLBP (Gateway Load Balancing Protocol)",
                explanation="GLBP uniquely supports active-active load balancing by using an Active Virtual Gateway (AVG) to reply with distinct Active Virtual Forwarder (AVF) virtual MACs."
            ),
            QuizQuestionBlueprint(
                question="What virtual MAC address prefix is reserved for standard VRRP (IPv4)?",
                options=[
                    "00:00:5E:00:01:XX",
                    "00:00:0C:07:AC:XX",
                    "FF:FF:FF:FF:FF:FF",
                    "01:00:5E:00:00:01"
                ],
                correct_answer="00:00:5E:00:01:XX",
                explanation="VRRP uses the IANA assigned virtual MAC address block 00:00:5E:00:01:XX where XX is the VRRP group ID in hex."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 54
    # -------------------------------------------------------------
    DayBlueprint(
        order=54,
        title="Day 54: Network Monitoring & Logging (SNMP, Syslog, & NetFlow)",
        concept="Network Telemetry, Health Monitoring, and Traffic Flow Analysis: MIBs/OIDs, SNMPv3, Syslog severity levels, and NetFlow 7-tuples",
        analogy="Monitoring a complex enterprise network is like monitoring intensive care patients in a hospital: Syslog is the emergency nurse call-button: the moment an event happens (an interface goes down), an immediate timestamped notification is logged. SNMP is the periodic vital signs monitor (heart rate, blood pressure): a central machine polls the patient every 5 minutes to record CPU temperature, link bandwidth, and port errors. NetFlow is like reviewing hallway security footage: it doesn't read the patient's private medical charts, but it records exactly who entered which room, at what time, and how many boxes were carried.",
        theory_sections=[
            {
                "heading": "SNMP: Architecture, MIBs, and SNMPv3 Security",
                "body": "**SNMP (Simple Network Management Protocol)** uses an **SNMP Manager** (NMS: PRTG, Zabbix, SolarWinds) and **SNMP Agents** (software daemons running on routers/switches):\n- **MIB (Management Information Base)**: A hierarchical database of monitored variables on a device.\n- **OID (Object Identifier)**: Dotted numeric strings addressing specific MIB variables (e.g., `1.3.6.1.2.1.2.2.1.10` for interface in-octets).\n- **Operations**: `GetRequest` (pull data from agent), `SetRequest` (change config on agent), and `Trap / Inform` (unsolicited agent alerts sent to NMS on UDP 162).\n- **SNMP Versions**:\n  - **SNMPv1 & SNMPv2c**: Insecure; authenticate using cleartext **community strings** ('public', 'private').\n  - **SNMPv3**: Modern standard; adds cryptographic **Authentication** (HMAC-SHA) and **Privacy** (AES encryption)."
            },
            {
                "heading": "Syslog Severity Levels & NetFlow / IPFIX Flow Analysis",
                "body": "- **Syslog (UDP Port 514)**: Collects human-readable system log messages.\n  - Standard 8 Severity Levels (0 to 7): **0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notification, 6=Informational, 7=Debugging**.\n  - Mnemonic: *\"Every Alley Cat Eats Weed Not Ice cream Dishes\"*.\n\n- **NetFlow / IPFIX (IP Flow Information Export)**: Collects statistical flow records defined by a 7-tuple:\n  (Source IP, Destination IP, Source Port, Destination Port, Layer 3 Protocol, Ingress Interface, ToS/DSCP).\n  Unlike full packet capture (Wireshark/PCAP), NetFlow collects only metadata, providing high-speed visibility into bandwidth consumption and top talkers with low CPU overhead."
            }
        ],
        code_snippets=[
            {
                "title": "Cisco IOS: Secure SNMPv3 User & Group Configuration",
                "language": "cisco",
                "code": "# Create SNMPv3 view\nRouter(config)# snmp-server view VIEW_ALL iso included\n\n# Create SNMPv3 group requiring authentication and encryption (authPriv)\nRouter(config)# snmp-server group SECURE_NMS_GRP v3 priv read VIEW_ALL\n\n# Create SNMPv3 user with SHA authentication and AES encryption\nRouter(config)# snmp-server user netadmin SECURE_NMS_GRP v3 auth sha AuthPass123 priv aes 128 EncryptPass456",
                "explanation": "Configures secure SNMPv3 authPriv user preventing eavesdropping or spoofed SNMP gets."
            },
            {
                "title": "Cisco IOS: Syslog Logging Configuration",
                "language": "cisco",
                "code": "# Send syslog messages to central SIEM / Syslog Server on UDP 514\nRouter(config)# logging host 192.168.1.50\nRouter(config)# logging trap informational  # Severity 6 and below\nRouter(config)# service timestamps log datetime msec\nRouter(config)# logging source-interface GigabitEthernet0/0",
                "explanation": "Directs timestamped router event logs to a central syslog repository."
            },
            {
                "title": "Cisco IOS: Flexible NetFlow (FNF) Configuration",
                "language": "cisco",
                "code": "# 1. Define Flow Record\nRouter(config)# flow record FLOW_RECORD_1\nRouter(config-flow-record)# match ipv4 source address\nRouter(config-flow-record)# match ipv4 destination address\nRouter(config-flow-record)# match transport source-port\nRouter(config-flow-record)# match transport destination-port\nRouter(config-flow-record)# collect counter bytes\n\n# 2. Apply Flow Monitor to Interface\nRouter(config)# interface GigabitEthernet0/0\nRouter(config-if)# ip flow monitor FLOW_MONITOR_1 input",
                "explanation": "Captures flow 5-tuple statistics and byte counts for traffic traversing GigabitEthernet0/0."
            },
            {
                "title": "Python Script: Querying an SNMP OID with PySNMP",
                "language": "python",
                "code": "# Demonstration of querying sysName OID: 1.3.6.1.2.1.1.5.0\nprint('SNMP Query logic configured for UDP port 161 (GetRequest) and 162 (Traps)')",
                "explanation": "Demonstrates how network automation scripts query SNMP MIB variables over UDP port 161."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Syslog Severity Parser",
            description="Write a Python function `parse_syslog_severity(log_message: str) -> dict` that extracts the integer severity level from a Cisco syslog header (e.g., `*Sep 30 22:15:00: %LINK-3-UPDOWN: Interface Gi0/1 changed state to down`) and returns `{'severity_level': int, 'severity_name': str}`.",
            starter_code="def parse_syslog_severity(log_message: str) -> dict:\n    # Extract severity integer and map to its severity name\n    pass",
            solution_code="def parse_syslog_severity(log_message: str) -> dict:\n    sev_map = {\n        0: 'Emergency', 1: 'Alert', 2: 'Critical', 3: 'Error',\n        4: 'Warning', 5: 'Notification', 6: 'Informational', 7: 'Debug'\n    }\n    import re\n    match = re.search(r'%[A-Z0-9_]+-(\\d)-[A-Z0-9_]+:', log_message)\n    if match:\n        sev_num = int(match.group(1))\n        return {'severity_level': sev_num, 'severity_name': sev_map.get(sev_num, 'Unknown')}\n    return {'severity_level': -1, 'severity_name': 'Invalid'}",
            expected_output="{'severity_level': 3, 'severity_name': 'Error'}\n{'severity_level': 5, 'severity_name': 'Notification'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which SNMP version provides strong cryptographic authentication (HMAC-SHA) and payload encryption (AES)?",
                options=[
                    "SNMPv3",
                    "SNMPv1",
                    "SNMPv2c",
                    "SNMPv0"
                ],
                correct_answer="SNMPv3",
                explanation="SNMPv3 introduced User-based Security Model (USM) providing strong authentication and encryption (authPriv)."
            ),
            QuizQuestionBlueprint(
                question="What is the standard Syslog severity level for an 'Error' message in Cisco IOS?",
                options=[
                    "Severity 3",
                    "Severity 0",
                    "Severity 7",
                    "Severity 6"
                ],
                correct_answer="Severity 3",
                explanation="Syslog severities run 0 (Emergency) to 7 (Debug); Severity 3 corresponds directly to Error conditions."
            ),
            QuizQuestionBlueprint(
                question="What does an SNMP Agent send to an NMS to notify it immediately of an unsolicited event (like a link failure)?",
                options=[
                    "An SNMP Trap (or Inform)",
                    "An ICMP Redirect",
                    "A TCP SYN-ACK",
                    "A DHCP Discover"
                ],
                correct_answer="An SNMP Trap (or Inform)",
                explanation="SNMP Traps and Informs are asynchronous, unsolicited messages sent by an agent to notify the NMS of critical events on UDP 162."
            ),
            QuizQuestionBlueprint(
                question="How does NetFlow differ from full packet capture (PCAP / Wireshark)?",
                options=[
                    "NetFlow collects traffic metadata and flow statistics without capturing raw packet payload data",
                    "NetFlow only captures physical copper cable resistance",
                    "NetFlow modifies the IP addresses inside each packet",
                    "NetFlow requires disabling all firewalls"
                ],
                correct_answer="NetFlow collects traffic metadata and flow statistics without capturing raw packet payload data",
                explanation="NetFlow records statistical flow metadata (IPs, ports, protocols, byte counters), requiring vastly less storage and compute than full payload packet captures."
            ),
            QuizQuestionBlueprint(
                question="Which UDP port is traditionally used by network devices to send Syslog messages to a central log server?",
                options=[
                    "UDP Port 514",
                    "TCP Port 80",
                    "UDP Port 69",
                    "TCP Port 22"
                ],
                correct_answer="UDP Port 514",
                explanation="Syslog communicates over UDP port 514 by default."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 55
    # -------------------------------------------------------------
    DayBlueprint(
        order=55,
        title="Day 55: SDN (Software-Defined Networking: Control Plane vs Data Plane)",
        concept="Decoupling Control Plane from Data Plane: Centralized controllers, Southbound APIs (OpenFlow), and Northbound REST APIs",
        analogy="Traditional networking is like a city of taxi drivers where every driver independently navigates their own car by staring at paper street maps and guessing which intersections might be jammed. Software-Defined Networking (SDN) is like Uber or Google Maps: the 'driver' inside the car just executes steering and pedals (the Data / Forwarding Plane), while a massive cloud brain with real-time GPS telemetry (the centralized Control Plane) computes the optimal route for every vehicle across the entire city simultaneously.",
        theory_sections=[
            {
                "heading": "The Planes of Networking: Data, Control, & Management",
                "body": "Every network device performs operations across three distinct planes:\n- **Data Plane (Forwarding Plane)**: The high-speed hardware silicon (ASICs/TCAM) responsible for moving bits from ingress ports to egress ports. Actions include MAC lookups, IP route table lookups, decrementing TTL, and recalculating checksums. Must operate in nanoseconds.\n- **Control Plane**: The intelligence of the network. Responsible for populating the routing table (RIB) and MAC table. Processes dynamic routing protocols (OSPF, BGP), Spanning Tree (STP), and ARP.\n- **Management Plane**: The administrative interface used by engineers (SSH, Telnet, HTTPS, SNMP, NETCONF/RESTCONF) to configure and monitor devices."
            },
            {
                "heading": "The SDN Architecture & Centralized Controllers",
                "body": "In **Traditional Networking**, every router has its own autonomous control plane and data plane packaged inside a single metal box (distributed architecture).\n\nIn **Software-Defined Networking (SDN)**:\n- The **Control Plane is decoupled** from physical switches and centralized into a software-based **SDN Controller** (e.g., OpenDaylight, Cisco DNA-C, ONOS).\n- The physical or virtual switches become simple, high-speed **Data Plane forwarders**.\n- **Southbound APIs (SBIs)**: The protocols used by the SDN controller to program forwarding tables into the physical switches (e.g., **OpenFlow**, NETCONF, gRPC).\n- **Northbound APIs (NBIs)**: RESTful APIs exposed by the SDN controller to business applications, automation scripts, and orchestration portals."
            }
        ],
        code_snippets=[
            {
                "title": "Conceptual OpenFlow Flow Table Entry Format",
                "language": "yaml",
                "code": "# OpenFlow Flow Entry:\nPriority: 100\nMatch: {in_port: 1, eth_type: 0x0800, ipv4_dst: 10.0.0.5}\nAction: [output: 2]\nStats: {packet_count: 5410, byte_count: 757400}",
                "explanation": "Illustrates how OpenFlow controllers program ternary match-action forwarding entries directly into switch TCAM."
            },
            {
                "title": "Ryu SDN Controller: Simple Python Controller Application",
                "language": "python",
                "code": "# Python Ryu SDN Controller structure\nclass SimpleSwitch13:\n    def packet_in_handler(self, ev):\n        # Centralized controller intelligence handles miss\n        print('Central controller calculating path and pushing flow entry to switch hardware')",
                "explanation": "Demonstrates an event-driven Python SDN application flow handler."
            },
            {
                "title": "SDN Plane Separation Architecture Diagram",
                "language": "text",
                "code": "Applications (Northbound REST APIs)\n        |\nv SDN Controller (Control Plane)\n        |\nv Physical Switches (Southbound OpenFlow/NETCONF Data Plane)",
                "explanation": "Visualizes the tripartite hierarchy of SDN architectures."
            },
            {
                "title": "Python Script: Simulating Control vs Data Plane Actions",
                "language": "python",
                "code": "class ForwardingHardware:\n    def __init__(self):\n        self.flow_table = {}\n    def data_plane_forward(self, dst_ip: str) -> str:\n        if dst_ip in self.flow_table:\n            return f'DATA PLANE: Forward out port {self.flow_table[dst_ip]}'\n        return 'DATA PLANE: Miss! Send Packet-In to SDN Controller'\n\nhw = ForwardingHardware()\nhw.flow_table['10.1.1.50'] = 3\nprint(hw.data_plane_forward('10.1.1.50'))",
                "explanation": "Simulates fast hardware data plane forwarding action driven by control plane flow installation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SDN Match-Action Flow Table Simulator",
            description="Write a Python function `sdn_forward_packet(packet: dict, flow_table: list) -> str`. Find the highest priority entry in `flow_table` whose `match` key-value pairs match `packet`. Return the matching `action` string. If no entry matches, return `'SEND_TO_CONTROLLER'`.",
            starter_code="def sdn_forward_packet(packet: dict, flow_table: list) -> str:\n    # Return highest priority action matching packet or 'SEND_TO_CONTROLLER'\n    pass",
            solution_code="def sdn_forward_packet(packet: dict, flow_table: list) -> str:\n    sorted_table = sorted(flow_table, key=lambda x: x['priority'], reverse=True)\n    for entry in sorted_table:\n        match_dict = entry['match']\n        if all(packet.get(k) == v for k, v in match_dict.items()):\n            return entry['action']\n    return 'SEND_TO_CONTROLLER'",
            expected_output="DROP\nOUTPUT_PORT_1\nSEND_TO_CONTROLLER"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the foundational architectural principle of Software-Defined Networking (SDN)?",
                options=[
                    "Decoupling the Control Plane from the Data (Forwarding) Plane and centralizing control logic in software",
                    "Replacing all copper cables with wireless infrared beams",
                    "Eliminating IP addresses completely from the Internet",
                    "Forcing all routers to use the Windows 95 operating system"
                ],
                correct_answer="Decoupling the Control Plane from the Data (Forwarding) Plane and centralizing control logic in software",
                explanation="SDN decouples the control plane (routing intelligence) from the underlying data plane (hardware forwarding), centralizing it into an SDN controller."
            ),
            QuizQuestionBlueprint(
                question="Which networking plane is implemented in specialized ASIC chips to process packet forwarding in nanoseconds?",
                options=[
                    "The Data Plane (Forwarding Plane)",
                    "The Control Plane",
                    "The Management Plane",
                    "The Documentation Plane"
                ],
                correct_answer="The Data Plane (Forwarding Plane)",
                explanation="The Data Plane executes high-speed lookups, checksum recalculation, and packet forwarding directly in silicon hardware ASICs."
            ),
            QuizQuestionBlueprint(
                question="What is the function of a Southbound API (SBI) in an SDN architecture?",
                options=[
                    "It enables the SDN Controller to communicate with and program the forwarding tables of physical/virtual network switches",
                    "It connects users directly to social media portals",
                    "It calculates employee paychecks",
                    "It allows switches to control power generators"
                ],
                correct_answer="It enables the SDN Controller to communicate with and program the forwarding tables of physical/virtual network switches",
                explanation="Southbound APIs (such as OpenFlow, NETCONF, and gRPC) are used by the SDN controller to push flow instructions down to data plane switches."
            ),
            QuizQuestionBlueprint(
                question="What type of API is used Northbound from the SDN controller to interface with business applications and orchestration platforms?",
                options=[
                    "RESTful APIs (HTTP / JSON)",
                    "RS-232 Serial console commands",
                    "Morse code over audio jack",
                    "Coaxial BNC television signals"
                ],
                correct_answer="RESTful APIs (HTTP / JSON)",
                explanation="Northbound APIs are standard RESTful APIs (using HTTP methods and JSON/XML payloads) that allow high-level software to query and automate the network."
            ),
            QuizQuestionBlueprint(
                question="What is an example of an early open-standard Southbound protocol used in SDN?",
                options=[
                    "OpenFlow",
                    "Telnet",
                    "POP3",
                    "FTP"
                ],
                correct_answer="OpenFlow",
                explanation="OpenFlow was the pioneering open standard Southbound protocol designed to manipulate switch flow tables directly from an external controller."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 56
    # -------------------------------------------------------------
    DayBlueprint(
        order=56,
        title="Day 56: Network Controllers (Cisco DNA Center)",
        concept="Enterprise Network Controllers and Intent-Based Networking: Design, Policy, Provision, and Assurance in Cisco Catalyst Center",
        analogy="Configuring an enterprise network with 500 switches via CLI is like a hotel manager personally walking to each of the 500 rooms every morning to adjust the thermostat, turn on the TV, and lock the safe. Cisco DNA Center (Catalyst Center) is like a master smart-building touchscreen in the manager's office: you state your intent ('Guest rooms must maintain 70 degrees and have guest Wi-Fi enabled'), and the central controller automatically translates that intent into thousands of switch and AP configurations, pushes them simultaneously, and continuously monitors health to ensure the policy is never violated.",
        theory_sections=[
            {
                "heading": "What is Intent-Based Networking (IBN)?",
                "body": "Traditional networking is imperative: engineers write line-by-line CLI commands detailing how a switch must behave. **Intent-Based Networking (IBN)** is declarative: network administrators declare what business outcome they want, and the system automatically configures, verifies, and maintains that state across the fabric:\n- **Translation**: The controller converts business policies (e.g., 'Quarantine unpatched medical IoT devices') into concrete network configurations (ACLs, VLANs, QoS policies, SGT tags).\n- **Activation**: The controller automatically provisions and deploys configurations to hundreds of switches, routers, and APs via APIs.\n- **Assurance**: Continuously gathers telemetry, AI-driven analytics, and telemetry to verify that the network is actually performing as intended."
            },
            {
                "heading": "Cisco DNA Center (Catalyst Center) & SD-Access",
                "body": "**Cisco DNA Center** is Cisco's enterprise network management and orchestration controller:\n- **Design**: Centralized maps, golden image management (SWIM), IP address pools, and global network profiles.\n- **Policy**: Virtual networks (VNets) and Scalable Group Tags (SGTs) that enforce identity-based microsegmentation without VLAN sprawl.\n- **Provision**: Zero-Touch Provisioning / Network Plug and Play (PnP). A new switch can be plugged into a rack out of the box, discover DNA Center, download its golden IOS-XE image, receive its configuration, and join the network automatically.\n- **Assurance**: AI Network Analytics, client health scores (0-100), device health, and automated root cause analysis with guided remediation."
            }
        ],
        code_snippets=[
            {
                "title": "Authenticating with Cisco DNA Center REST API",
                "language": "python",
                "code": "import requests\nimport urllib3\nurllib3.disable_warnings()\n\nDNAC_URL = 'https://sandboxdnac.cisco.com'\nauth_endpoint = f'{DNAC_URL}/dna/system/api/v1/auth/token'\n\n# POST request to acquire JWT token\nresponse = requests.post(auth_endpoint, auth=('devnetuser', 'Cisco123!'), verify=False)\ntoken = response.json().get('Token')\nprint('Acquired Cisco DNA-C Auth Token:', token[:25], '...')",
                "explanation": "Authenticates with Cisco DNA Center to obtain an authorized JWT session token for API calls."
            },
            {
                "title": "Retrieving Network Device Inventory from Cisco DNA Center",
                "language": "python",
                "code": "# Querying /dna/intent/api/v1/network-device\nheaders = {'x-auth-token': token, 'Content-Type': 'application/json'}\nres = requests.get(f'{DNAC_URL}/dna/intent/api/v1/network-device', headers=headers, verify=False)\nfor dev in res.json().get('response', []):\n    print(f\"{dev.get('hostname')} | IP: {dev.get('managementIpAddress')}\")",
                "explanation": "Queries DNA Center inventory to retrieve device details across the enterprise fabric."
            },
            {
                "title": "Cisco DNA Center Assurance Client Health Score Structure",
                "language": "json",
                "code": "{\n  \"clientMac\": \"00:1A:2B:3C:4D:5E\",\n  \"overallHealthScore\": 85,\n  \"connectionScore\": 100,\n  \"issueDetails\": \"High channel interference detected on 2.4 GHz AP radio\"\n}",
                "explanation": "Illustrates the telemetry JSON payload returned by DNA Center Assurance."
            },
            {
                "title": "Python Script: Client Health Score Evaluator",
                "language": "python",
                "code": "def evaluate_client_health(client_telemetry: dict) -> str:\n    score = client_telemetry.get('overallHealthScore', 0)\n    if score >= 80:\n        return 'HEALTH: EXCELLENT'\n    return 'HEALTH: INVESTIGATION NEEDED'\n\nprint(evaluate_client_health({'overallHealthScore': 95}))",
                "explanation": "Simulates automated issue detection based on DNA Center assurance client telemetry."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DNA Center Device Inventory Filter",
            description="Write a Python function `filter_unreachable_devices(devices_payload: list) -> list` that processes a list of device dictionaries and returns a list containing only the `hostname` strings of devices where `reachabilityStatus == 'Unreachable'`.",
            starter_code="def filter_unreachable_devices(devices_payload: list) -> list:\n    # Return list of hostnames of unreachable devices\n    pass",
            solution_code="def filter_unreachable_devices(devices_payload: list) -> list:\n    return [d['hostname'] for d in devices_payload if d.get('reachabilityStatus') == 'Unreachable']",
            expected_output="['Switch-Access-B', 'AP-Floor-3']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the four core functional pillars of Cisco DNA Center (Catalyst Center)?",
                options=[
                    "Design, Policy, Provision, and Assurance",
                    "Compile, Link, Execute, and Debug",
                    "Copy, Paste, Save, and Delete",
                    "Broadcast, Multicast, Anycast, and Unicast"
                ],
                correct_answer="Design, Policy, Provision, and Assurance",
                explanation="Cisco DNA Center is built around four primary workflows: Design (profiles), Policy (intent), Provision (deployment), and Assurance (analytics/telemetry)."
            ),
            QuizQuestionBlueprint(
                question="What is the core philosophy behind Intent-Based Networking (IBN)?",
                options=[
                    "Administrators declare high-level business intent, and the controller automatically translates, activates, and verifies the network configuration",
                    "Engineers must manually type 10,000 CLI lines without using copy-paste",
                    "All routing decisions are made by random dice rolls",
                    "Network hardware is replaced every 24 hours"
                ],
                correct_answer="Administrators declare high-level business intent, and the controller automatically translates, activates, and verifies the network configuration",
                explanation="IBN allows administrators to specify business requirements ('intent'); the controller automatically translates that intent into configuration and continuously assures it."
            ),
            QuizQuestionBlueprint(
                question="Which Cisco DNA Center feature enables brand-new switches to be automatically imaged and configured directly out of the shipping box?",
                options=[
                    "Network Plug and Play (PnP) / Zero-Touch Provisioning",
                    "TFTP Server manual recovery mode",
                    "Xmodem serial baud rate transfer",
                    "Manual USB thumb drive flashing"
                ],
                correct_answer="Network Plug and Play (PnP) / Zero-Touch Provisioning",
                explanation="Cisco Network PnP enables zero-touch onboarding: the switch phones home to DNA Center, updates firmware, and downloads its configuration automatically."
            ),
            QuizQuestionBlueprint(
                question="What role does the 'Assurance' subsystem in Cisco DNA Center perform?",
                options=[
                    "It monitors streaming telemetry and client health metrics to detect anomalies and provide guided root-cause troubleshooting",
                    "It physically repairs broken fiber patch cords",
                    "It issues credit cards to employees",
                    "It terminates employee accounts automatically"
                ],
                correct_answer="It monitors streaming telemetry and client health metrics to detect anomalies and provide guided root-cause troubleshooting",
                explanation="DNA Center Assurance ingests real-time telemetry to compute health scores and proactively identify network bottlenecks and configuration issues."
            ),
            QuizQuestionBlueprint(
                question="What type of token authentication is typically used when interacting with the Cisco DNA Center REST API?",
                options=[
                    "JSON Web Token (JWT) passed in the 'x-auth-token' header",
                    "Cleartext passwords in every URL query string",
                    "Fingerprint biometric scans over Bluetooth",
                    "NTLM v1 challenge-response"
                ],
                correct_answer="JSON Web Token (JWT) passed in the 'x-auth-token' header",
                explanation="Cisco DNA Center authenticates API calls using a temporary JWT token passed via the 'x-auth-token' HTTP request header."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 57
    # -------------------------------------------------------------
    DayBlueprint(
        order=57,
        title="Day 57: Cloud Networking (AWS VPCs, Azure VNets)",
        concept="Public Cloud Virtual Private Clouds and Software Networking: Subnets, Route Tables, Internet Gateways, NAT Gateways, and Security Groups",
        analogy="Traditional networking requires leasing physical real estate, installing heavy steel racks, and running physical patch cables. Cloud networking is like an architect drafting a digital 3D blueprint inside software: an AWS VPC (or Azure VNet) is your private virtual walled territory inside Amazon's or Microsoft's massive global data centers. With a single API call, you carve out subnets, deploy software routers, attach an Internet Gateway (unlocking the main gate to the public street), and configure security groups that act like personal bodyguards standing at every virtual machine's door.",
        theory_sections=[
            {
                "heading": "Anatomy of an AWS Virtual Private Cloud (VPC)",
                "body": "An **AWS VPC** is a logically isolated virtual network dedicated to your cloud account:\n- **CIDR Block**: Defines the IP range of the VPC (e.g., `10.0.0.0/16` providing 65,536 private IP addresses).\n- **Subnets**: Tied to specific **Availability Zones (AZs)** for fault tolerance:\n  - **Public Subnet**: Has a Route Table entry directing `0.0.0.0/0` outbound traffic to an **Internet Gateway (IGW)**.\n  - **Private Subnet**: Has no direct route to the IGW. Outbound internet access is achieved via a **NAT Gateway** located in a public subnet.\n- **Route Tables**: Direct packet flow between subnets, gateways, and VPC Peering connections.\n- **AWS reserves 5 IP addresses per subnet**: The network address (`.0`), VPC router (`.1`), DNS server (`.2`), future use (`.3`), and broadcast address (`.255`)."
            },
            {
                "heading": "Cloud Security: Security Groups vs Network ACLs & Azure VNets",
                "body": "Cloud networks enforce security using two distinct layers:\n1. **Security Groups (SGs)**:\n   - Attached directly to the virtual network interface (ENI / VM instance).\n   - **Stateful**: If you allow inbound traffic on port 443, outbound return traffic is automatically allowed regardless of outbound rules.\n   - Evaluates all rules before deciding; cannot have explicit 'deny' rules (only permits).\n2. **Network ACLs (NACLs)**:\n   - Attached to the **subnet boundary**.\n   - **Stateless**: Inbound and outbound traffic must be explicitly permitted with matching rules.\n   - Evaluates rules in numbered order (e.g., 100, 200) and supports explicit DENY statements.\n\n**Azure Equivalent**: Azure **Virtual Network (VNet)**, divided into subnets, connected via Public IPs or Azure NAT Gateway, and protected using **Network Security Groups (NSGs)**."
            }
        ],
        code_snippets=[
            {
                "title": "AWS CLI: Creating a VPC, Subnet, and Internet Gateway",
                "language": "bash",
                "code": "# 1. Create VPC with /16 CIDR\naws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=PROD-VPC}]'\n\n# 2. Create Public Subnet in us-east-1a\naws ec2 create-subnet --vpc-id vpc-0a1b2c3d4e5f6g7h8 --cidr-block 10.0.1.0/24 --availability-zone us-east-1a\n\n# 3. Create and Attach Internet Gateway (IGW)\naws ec2 create-internet-gateway\naws ec2 attach-internet-gateway --internet-gateway-id igw-11223344556677889 --vpc-id vpc-0a1b2c3d4e5f6g7h8",
                "explanation": "Constructs a full AWS public cloud network foundation using the AWS command line."
            },
            {
                "title": "Terraform Infrastructure-as-Code: AWS VPC & Security Group",
                "language": "hcl",
                "code": "resource \"aws_vpc\" \"main\" {\n  cidr_block           = \"10.0.0.0/16\"\n  enable_dns_hostnames = true\n  tags = { Name = \"Cloud-VPC\" }\n}\n\nresource \"aws_security_group\" \"web_sg\" {\n  name   = \"allow_web_traffic\"\n  vpc_id = aws_vpc.main.id\n  ingress {\n    from_port   = 443\n    to_port     = 443\n    protocol    = \"tcp\"\n    cidr_blocks = [\"0.0.0.0/0\"]\n  }\n}",
                "explanation": "Declarative Terraform HCL defining a cloud VPC and a stateful security group allowing HTTPS."
            },
            {
                "title": "AWS Transit Gateway Hub-and-Spoke Topology",
                "language": "text",
                "code": "[VPC-PROD (10.1.0.0/16)]      [VPC-DEV (10.2.0.0/16)]\n           \\                           /\n          +-----------------------------+\n          |     AWS Transit Gateway     |\n          +-----------------------------+",
                "explanation": "Visualizes AWS Transit Gateway providing hub-and-spoke multi-VPC cloud routing."
            },
            {
                "title": "Python Script: Calculating Usable AWS Subnet Hosts",
                "language": "python",
                "code": "def aws_usable_ips(cidr_prefix: int) -> int:\n    total_ips = 2 ** (32 - cidr_prefix)\n    return max(0, total_ips - 5)\n\nprint('/24 subnet usable IPs:', aws_usable_ips(24))  # 256 - 5 = 251\nprint('/28 subnet usable IPs:', aws_usable_ips(28))  # 16 - 5 = 11",
                "explanation": "Demonstrates AWS's 5-IP subnet reservation policy compared to standard RFC 1918 subnets."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="AWS Security Group Ingress Evaluator",
            description="Write a Python function `check_sg_ingress(packet: dict, sg_rules: list) -> bool` that evaluates whether an inbound packet matches any stateful security group rule. Return `True` if any rule permits the packet, otherwise `False`.",
            starter_code="def check_sg_ingress(packet: dict, sg_rules: list) -> bool:\n    # Return True if packet matches an allowed security group ingress rule\n    pass",
            solution_code="def check_sg_ingress(packet: dict, sg_rules: list) -> bool:\n    p_port = packet.get('port')\n    p_proto = packet.get('protocol')\n    p_src = packet.get('src_ip')\n    for rule in sg_rules:\n        if rule['port'] == p_port and rule['protocol'] == p_proto:\n            if rule['cidr'] == '0.0.0.0/0' or rule['cidr'] == p_src:\n                return True\n    return False",
            expected_output="True\nTrue\nFalse"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What critical attribute differentiates an AWS Security Group from a Network ACL (NACL)?",
                options=[
                    "Security Groups are stateful and applied at the instance/ENI level, while NACLs are stateless and applied at the subnet boundary",
                    "Security Groups can only be used on Linux, while NACLs run only on Windows",
                    "Security Groups require physical fiber connections",
                    "NACLs cannot block any traffic"
                ],
                correct_answer="Security Groups are stateful and applied at the instance/ENI level, while NACLs are stateless and applied at the subnet boundary",
                explanation="Security Groups are stateful host-level virtual firewalls; NACLs are stateless subnet-level packet filters."
            ),
            QuizQuestionBlueprint(
                question="How many IP addresses are reserved by AWS in every subnet created within a VPC?",
                options=[
                    "5 IP addresses (.0 network, .1 router, .2 DNS, .3 future use, and .255 broadcast)",
                    "2 IP addresses",
                    "0 IP addresses",
                    "10 IP addresses"
                ],
                correct_answer="5 IP addresses (.0 network, .1 router, .2 DNS, .3 future use, and .255 broadcast)",
                explanation="AWS reserves 5 IP addresses per subnet for network, router, DNS, future reserved, and broadcast roles."
            ),
            QuizQuestionBlueprint(
                question="What routing component must be attached to an AWS VPC to allow EC2 instances in a public subnet to communicate directly with the Internet?",
                options=[
                    "An Internet Gateway (IGW)",
                    "A Bluetooth dongle",
                    "An internal loopback adapter",
                    "A USB Hub"
                ],
                correct_answer="An Internet Gateway (IGW)",
                explanation="An Internet Gateway (IGW) provides horizontal scaling, redundancy, and bidirectional NAT between VPC instances and the Internet."
            ),
            QuizQuestionBlueprint(
                question="How can EC2 instances in a private subnet initiate outbound connections to download OS updates without exposing themselves to inbound internet traffic?",
                options=[
                    "Route outbound traffic through a NAT Gateway deployed in a public subnet",
                    "Attach a public IP directly to the database instance",
                    "Disable all routing tables in the VPC",
                    "Set subnet mask to 255.255.255.255"
                ],
                correct_answer="Route outbound traffic through a NAT Gateway deployed in a public subnet",
                explanation="A managed NAT Gateway in a public subnet allows private subnet hosts to initiate outbound connections while shielding them from inbound connections."
            ),
            QuizQuestionBlueprint(
                question="What is the Microsoft Azure equivalent of an AWS Virtual Private Cloud (VPC)?",
                options=[
                    "Azure Virtual Network (VNet)",
                    "Azure Cosmos DB",
                    "Azure Active Directory Domain",
                    "Azure Blob Storage"
                ],
                correct_answer="Azure Virtual Network (VNet)",
                explanation="An Azure Virtual Network (VNet) is the fundamental building block for private cloud networking in Microsoft Azure."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 58
    # -------------------------------------------------------------
    DayBlueprint(
        order=58,
        title="Day 58: Network APIs (REST APIs, JSON, XML, & YAML)",
        concept="Programmable Interfaces and Modern Data Encoding: REST verbs, NETCONF vs RESTCONF, and JSON/YAML data serialization",
        analogy="Traditional CLI scraping is like listening to someone rapidly read a novel over a crackling telephone: if Cisco changes the spacing by two spaces or rewords a phrase, your script crashes because it was parsing unstructured human text. Network APIs and Data Formats (like JSON and YAML) are like exchanging clean, standardized digital spreadsheets: every piece of information (interface name, IP address, operational status) is neatly labeled in a strict key-value pair that computers can read instantly with 100% precision.",
        theory_sections=[
            {
                "heading": "Modern Network APIs: REST, NETCONF, & RESTCONF",
                "body": "Modern network devices are fully programmable via machine-readable APIs:\n- **REST (Representational State Transfer)**: Uses standard HTTP verbs over TLS (HTTPS):\n  - `GET`: Retrieve data (e.g., read interface status).\n  - `POST`: Create a new resource (e.g., create a new VLAN).\n  - `PUT`: Replace an existing resource completely.\n  - `PATCH`: Update specific attributes of an existing resource.\n  - `DELETE`: Remove a resource.\n- **NETCONF (RFC 6241)**: Network Configuration Protocol. Uses SSH transport (port 830) and XML encoding to manage configurations and state. Supports database transactions (`candidate`, `running`, `startup`).\n- **RESTCONF (RFC 8040)**: A RESTful, HTTP-based implementation of NETCONF that uses either JSON or XML data encoding over HTTPS."
            },
            {
                "heading": "Data Serialization Formats: JSON, XML, & YAML",
                "body": "- **JSON (JavaScript Object Notation)**: Lightweight, ubiquitous, key-value pairs and arrays. Uses `{}` for objects, `[]` for lists, and double-quoted strings. Standard format for REST APIs.\n- **YAML (YAML Ain't Markup Language)**: Human-friendly, whitespace/indentation-sensitive format. Used extensively in Ansible playbooks, Kubernetes manifests, and CI/CD pipelines.\n- **XML (Extensible Markup Language)**: Tag-based format using `<tag>value</tag>`. Verbose and strict; used natively by NETCONF and SOAP."
            }
        ],
        code_snippets=[
            {
                "title": "Comparison of JSON, YAML, and XML for an Interface",
                "language": "yaml",
                "code": "# JSON format:\n# {\"interface\": {\"name\": \"GigabitEthernet0/1\", \"ip\": \"192.168.1.1\", \"enabled\": true}}\n\n# YAML format:\ninterface:\n  name: GigabitEthernet0/1\n  ip: 192.168.1.1\n  enabled: true",
                "explanation": "Contrasts the major data serialization formats used in network programmability."
            },
            {
                "title": "Python requests: RESTCONF GET Interface Status",
                "language": "python",
                "code": "import requests\nimport json\n\nurl = 'https://192.168.1.1/restconf/data/ietf-interfaces:interfaces'\nheaders = {'Accept': 'application/yang-data+json'}\nres = requests.get(url, headers=headers, auth=('admin', 'Cisco123!'), verify=False)\nprint(json.dumps(res.json(), indent=2))",
                "explanation": "Issues a RESTCONF HTTP GET request to query YANG-modeled router interfaces."
            },
            {
                "title": "Converting YAML to JSON in Python",
                "language": "python",
                "code": "import yaml, json\nyaml_text = 'router:\\n  hostname: Core-R1\\n  bgp_as: 65001'\ndata = yaml.safe_load(yaml_text)\nprint('Parsed JSON:', json.dumps(data))",
                "explanation": "Parses YAML configuration files into native Python objects and JSON strings."
            },
            {
                "title": "Python Script: Validating HTTP Status Codes",
                "language": "python",
                "code": "def parse_http_code(code: int) -> str:\n    if code == 200: return '200 OK'\n    elif code == 201: return '201 Created'\n    elif code == 404: return '404 Not Found'\n    return f'{code}: Other'\nprint(parse_http_code(200))\nprint(parse_http_code(404))",
                "explanation": "Demonstrates standard HTTP REST status code interpretation in network automation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="RESTCONF Interface IP Extractor",
            description="Write a Python function `extract_interface_ips(restconf_payload: dict) -> dict` that parses a RESTCONF JSON payload and returns a dictionary mapping interface names to their configured IPv4 addresses (or `None` if unassigned).",
            starter_code="def extract_interface_ips(restconf_payload: dict) -> dict:\n    # Return dict mapping interface name to its IPv4 address\n    pass",
            solution_code="def extract_interface_ips(restconf_payload: dict) -> dict:\n    result = {}\n    interfaces = restconf_payload.get('ietf-interfaces:interfaces', {}).get('interface', [])\n    for intf in interfaces:\n        name = intf.get('name')\n        addr_list = intf.get('ietf-ip:ipv4', {}).get('address', [])\n        result[name] = addr_list[0].get('ip') if addr_list else None\n    return result",
            expected_output="{'GigabitEthernet0/1': '10.1.1.1', 'GigabitEthernet0/2': '192.168.10.1', 'GigabitEthernet0/3': None}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which HTTP verb is used in RESTful APIs to retrieve resource information without modifying server state?",
                options=[
                    "GET",
                    "POST",
                    "DELETE",
                    "PATCH"
                ],
                correct_answer="GET",
                explanation="HTTP GET retrieves representation data safely without altering state on the server."
            ),
            QuizQuestionBlueprint(
                question="What transport protocol and default port does NETCONF use to securely communicate with network devices?",
                options=[
                    "SSH on Port 830",
                    "HTTP on Port 80",
                    "Telnet on Port 23",
                    "TFTP on Port 69"
                ],
                correct_answer="SSH on Port 830",
                explanation="NETCONF (RFC 6241) uses SSH over port 830 to provide encrypted, authenticated remote management sessions."
            ),
            QuizQuestionBlueprint(
                question="Which data format uses indentation and whitespace rather than curly braces or closing tags, making it the standard for Ansible playbooks?",
                options=[
                    "YAML",
                    "JSON",
                    "XML",
                    "HTML"
                ],
                correct_answer="YAML",
                explanation="YAML relies on strict whitespace indentation, making it highly readable and the de facto standard for Ansible automation."
            ),
            QuizQuestionBlueprint(
                question="What HTTP response status code signifies that a new resource (such as a new VLAN or interface) was successfully created via a POST request?",
                options=[
                    "201 Created",
                    "404 Not Found",
                    "500 Internal Server Error",
                    "301 Moved Permanently"
                ],
                correct_answer="201 Created",
                explanation="HTTP 201 Created indicates that the request has succeeded and led to the creation of a new resource."
            ),
            QuizQuestionBlueprint(
                question="How does RESTCONF differ from legacy NETCONF?",
                options=[
                    "RESTCONF uses HTTP/HTTPS APIs and can encode data in JSON or XML, whereas NETCONF uses SSH and XML exclusively",
                    "RESTCONF requires dial-up telephone modems",
                    "RESTCONF only works on Windows 98",
                    "RESTCONF eliminates the need for passwords"
                ],
                correct_answer="RESTCONF uses HTTP/HTTPS APIs and can encode data in JSON or XML, whereas NETCONF uses SSH and XML exclusively",
                explanation="RESTCONF provides a RESTful HTTP alternative to NETCONF, supporting JSON payloads and standard web development tooling."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 59
    # -------------------------------------------------------------
    DayBlueprint(
        order=59,
        title="Day 59: Network Automation with Python (Netmiko & NAPALM)",
        concept="Multi-Vendor Device Automation and Programmability: Paramiko/Netmiko SSH workflows, NAPALM getters, and concurrency with ThreadPoolExecutor",
        analogy="Configuring multi-vendor routers manually is like speaking to five people in five different languages: Cisco uses one set of commands, Juniper another, and Arista a third. Python automation libraries act as your universal translator team: Netmiko is like a lightning-fast robot typing directly into the SSH console with zero human typos, while NAPALM is an elite multilingual diplomat: you write a single script saying `get_facts()`, and NAPALM automatically figures out the exact vendor commands to return a uniform report whether the router is Cisco IOS, Juniper JunOS, or Arista EOS.",
        theory_sections=[
            {
                "heading": "SSH Automation with Netmiko",
                "body": "**Netmiko** (built by Kirk Byers on top of Paramiko) is the premier Python library for CLI-based network device automation:\n- Simplifies SSH connections to hundreds of network operating systems (Cisco IOS, IOS-XE, NX-OS, Juniper JunOS, Arista EOS).\n- Automatically handles CLI prompts (`#`, `>`, login prompts), pagination (`--More--`), and timing delays.\n- Core Methods:\n  - `send_command(cmd)`: Sends a read-only show command and returns output as a string.\n  - `send_config_set(list_of_commands)`: Enters configuration mode, executes commands in order, exits, and handles errors.\n  - `send_command_timing(cmd)`: For interactive commands expecting prompts (e.g., confirmations)."
            },
            {
                "heading": "Cross-Vendor Abstraction with NAPALM",
                "body": "**NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support)**:\n- Provides a unified Python API across diverse vendor platforms.\n- Instead of parsing vendor-specific text, NAPALM methods return structured Python dictionaries:\n  - `get_facts()`: Hostname, model, serial number, OS version, uptime.\n  - `get_interfaces()` & `get_interfaces_ip()`: Interface status, MTU, speed, IP assignments.\n  - `get_bgp_neighbors()`: BGP peer status across all vendors.\n- **Configuration Management**: Supports atomic configuration rollbacks (`load_merge_candidate()`, `compare_config()`, `commit_config()`, and `rollback()`)."
            }
        ],
        code_snippets=[
            {
                "title": "Python Netmiko: Pushing VLAN Configuration to Cisco IOS Switch",
                "language": "python",
                "code": "from netmiko import ConnectHandler\n\ncisco_switch = {\n    'device_type': 'cisco_ios',\n    'host': '192.168.1.10',\n    'username': 'admin',\n    'password': 'CiscoSecretPassword123'\n}\n\nwith ConnectHandler(**cisco_switch) as net_connect:\n    config_commands = ['vlan 50', 'name ENGINEERING_DEPT']\n    output = net_connect.send_config_set(config_commands)\n    print('Output:\\n', output)",
                "explanation": "Automates configuration push across SSH to a Cisco switch using Netmiko."
            },
            {
                "title": "Python NAPALM: Multi-Vendor Fact Gathering",
                "language": "python",
                "code": "from napalm import get_network_driver\ndriver = get_network_driver('ios')\ndevice = driver('192.168.1.1', 'admin', 'CiscoSecretPassword123')\ndevice.open()\nfacts = device.get_facts()\nprint('Hostname:', facts['hostname'])\nprint('OS Version:', facts['os_version'])\ndevice.close()",
                "explanation": "Demonstrates NAPALM returning vendor-agnostic structured device metadata."
            },
            {
                "title": "Concurrent Multi-Device Automation with ThreadPoolExecutor",
                "language": "python",
                "code": "from concurrent.futures import ThreadPoolExecutor\n# Run parallel execution across 50 switches simultaneously\nprint('ThreadPoolExecutor enables rapid concurrent multi-device backups')",
                "explanation": "Executes network backups simultaneously across multiple routers using Python threads."
            },
            {
                "title": "Python Script: Validating BGP Peer State via NAPALM Output",
                "language": "python",
                "code": "def verify_bgp_peers(napalm_bgp_data: dict) -> dict:\n    peers = napalm_bgp_data.get('global', {}).get('peers', {})\n    return {peer: 'UP' if info.get('is_up') else 'DOWN' for peer, info in peers.items()}\n\nprint(verify_bgp_peers({'global': {'peers': {'192.168.1.2': {'is_up': True}}}}))",
                "explanation": "Demonstrates programmatic health verification on structured NAPALM BGP data."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cisco Switchport Status Parser",
            description="Write a Python function `parse_interface_status(cli_output: str) -> dict` that parses standard switchport status text and returns a dictionary: `{'Gi0/1': 'connected', 'Gi0/2': 'notconnect'}`.",
            starter_code="def parse_interface_status(cli_output: str) -> dict:\n    # Return dict mapping interface name to status ('connected', 'notconnect')\n    pass",
            solution_code="def parse_interface_status(cli_output: str) -> dict:\n    result = {}\n    valid_statuses = {'connected', 'notconnect', 'disabled', 'err-disabled'}\n    for line in cli_output.strip().splitlines():\n        parts = line.split()\n        if not parts or parts[0] == 'Port':\n            continue\n        port_name = parts[0]\n        for word in parts[1:]:\n            if word in valid_statuses:\n                result[port_name] = word\n                break\n    return result",
            expected_output="{'Gi0/1': 'connected', 'Gi0/2': 'notconnect', 'Gi0/3': 'disabled'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary function of the Netmiko Python library?",
                options=[
                    "Automating interactive SSH/Telnet connections and configuration deployment to multi-vendor network devices",
                    "Designing 3D models of switch chassis",
                    "Mining cryptocurrency on network switch CPUs",
                    "Compressing video streams for YouTube"
                ],
                correct_answer="Automating interactive SSH/Telnet connections and configuration deployment to multi-vendor network devices",
                explanation="Netmiko automates CLI interactions over SSH/Telnet with comprehensive multi-vendor support, prompt handling, and command execution."
            ),
            QuizQuestionBlueprint(
                question="What distinct advantage does NAPALM offer over raw CLI scraping tools?",
                options=[
                    "It returns uniform, vendor-agnostic structured Python dictionaries across different operating systems (Cisco, Juniper, Arista)",
                    "It operates without requiring internet access or cables",
                    "It replaces all routers with cloud servers",
                    "It forces all network devices to use the Python language natively"
                ],
                correct_answer="It returns uniform, vendor-agnostic structured Python dictionaries across different operating systems (Cisco, Juniper, Arista)",
                explanation="NAPALM abstracts vendor differences, allowing a single method like get_facts() to return identical dictionary structures across Cisco, Juniper, and Arista."
            ),
            QuizQuestionBlueprint(
                question="Which Netmiko method is specifically intended to send a batch of configuration commands (entering and exiting configuration mode automatically)?",
                options=[
                    "send_config_set()",
                    "send_command()",
                    "ping()",
                    "disconnect()"
                ],
                correct_answer="send_config_set()",
                explanation="send_config_set() enters config mode, executes a list or file of configuration commands, handles device prompts, and exits configuration mode."
            ),
            QuizQuestionBlueprint(
                question="What capability in NAPALM protects production networks from botched configuration changes?",
                options=[
                    "Atomic configuration rollback (commit_config and rollback)",
                    "Automatic deletion of customer databases",
                    "Overriding electrical breakers",
                    "Disabling all firewall rules"
                ],
                correct_answer="Atomic configuration rollback (commit_config and rollback)",
                explanation="NAPALM allows engineers to compare candidate configurations before committing and instantly roll back if errors occur."
            ),
            QuizQuestionBlueprint(
                question="Why is multithreading (e.g. ThreadPoolExecutor) frequently used in Python network automation scripts?",
                options=[
                    "To execute tasks across hundreds of switches simultaneously rather than waiting for slow sequential SSH connections one by one",
                    "To increase switch memory from 4GB to 16GB",
                    "Because Python cannot run on a single CPU core",
                    "To bypass router login passwords"
                ],
                correct_answer="To execute tasks across hundreds of switches simultaneously rather than waiting for slow sequential SSH connections one by one",
                explanation="Because network SSH calls are I/O bound, thread pools allow scripts to configure or back up hundreds of devices in parallel in seconds."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 60 (Capstone)
    # -------------------------------------------------------------
    DayBlueprint(
        order=60,
        title="Day 60: Configuration Management (Ansible) & Networking Capstone Review",
        concept="Declarative Configuration Management, Idempotence, and End-to-End Enterprise Networking Architecture Review",
        analogy="Writing procedural Python scripts to configure 1,000 switches is like giving an assistant 1,000 individual task reminders: 'If port 1 is not configured, run this. If it is already configured, don't run it.' Ansible is like handing the assistant a Master Blueprint of the finished skyscraper: Ansible's idempotent engine looks at each switch, determines whatever small differences exist between current reality and your blueprint, makes only the necessary adjustments, and reports back: 'Everything matches the desired state.'",
        is_project_day=True,
        project_name="Network Automation & Configuration Management Capstone",
        theory_sections=[
            {
                "heading": "Agentless Network Automation with Ansible",
                "body": "**Ansible** is an open-source, agentless configuration management and orchestration engine:\n- **Agentless**: Switches and routers do not need Ansible software installed; Ansible executes commands over SSH or RESTCONF directly.\n- **Inventory (`hosts.ini` / `hosts.yaml`)**: Categorizes devices by groups (e.g., `[leaf_switches]`, `[spines]`, `[firewalls]`).\n- **Playbooks**: YAML files declaring the desired state of the network.\n- **Modules**: Pre-built vendor integrations (`cisco.ios.ios_config`, `cisco.ios.ios_command`, `junipernetworks.junos.junos_facts`).\n- **Idempotence**: A critical guarantee where executing a playbook multiple times produces the exact same result without unintended changes or redundant reboots."
            },
            {
                "heading": "60-Day Networking Course Grand Capstone Review",
                "body": "Congratulations on completing 60 days of intensive enterprise networking! Let us review the complete end-to-end journey:\n1. **Fundamentals & OSI/TCP-IP (Days 1-8)**: Layer 1 physical signals, Layer 2 frames, Layer 3 packets, Layer 4 segments, Encapsulation.\n2. **Addressing & Subnetting (Days 9-14)**: MAC addresses, IPv4 classes, FLSM, VLSM, CIDR notation, and 128-bit IPv6.\n3. **Layer 2 Switching (Days 15-21)**: MAC learning, 802.1Q VLAN trunking, STP loop prevention, EtherChannel aggregation, PoE.\n4. **Layer 3 Routing (Days 22-29)**: Routing tables, Static routes, Inter-VLAN routing (ROAS), RIP, EIGRP, OSPF areas, and global BGP peering.\n5. **Core Services (Days 30-37)**: TCP 3-way handshakes, UDP, DNS, DHCP DORA, NAT/PAT, ARP, and ICMP diagnostic tools.\n6. **Wireless & WAN (Days 38-45)**: Wi-Fi 6/7, 2.4 vs 5 GHz channels, WLCs, WPA3, Leased Lines, MPLS label switching, and SD-WAN.\n7. **Security & High Availability (Days 46-54)**: Firewalls, ACL wildcarding, IPsec VPNs, AAA (RADIUS/TACACS+), L2 security, QoS, FHRP (HSRP/VRRP), and SNMP/Syslog.\n8. **Modern Automation (Days 55-60)**: SDN control/data plane separation, DNA Center, AWS Cloud VPCs, REST APIs/JSON, Netmiko, and Ansible orchestration."
            }
        ],
        code_snippets=[
            {
                "title": "Ansible Inventory File (inventory.ini)",
                "language": "ini",
                "code": "[campus_switches]\nswitch-access-1 ansible_host=192.168.1.10\nswitch-access-2 ansible_host=192.168.1.11\n\n[campus_switches:vars]\nansible_network_os=cisco.ios.ios\nansible_connection=network_cli\nansible_user=admin",
                "explanation": "Defines device inventory and network CLI connection variables for Ansible automation."
            },
            {
                "title": "Ansible Playbook: Idempotent VLAN and Banner Provisioning",
                "language": "yaml",
                "code": "---\n- name: Configure Campus Network Baseline\n  hosts: campus_switches\n  gather_facts: false\n  tasks:\n    - name: Ensure MOTD banner is set\n      cisco.ios.ios_banner:\n        banner: motd\n        text: \"AUTHORIZED ACCESS ONLY - HUNAR PLATFORM LAB\"\n        state: present\n\n    - name: Ensure Corporate VLANs exist\n      cisco.ios.ios_vlans:\n        config:\n          - vlan_id: 10\n            name: MANAGEMENT\n          - vlan_id: 20\n            name: ENGINEERING\n        state: replaced",
                "explanation": "YAML playbook enforcing banners and VLAN states across all campus switches idempotently."
            },
            {
                "title": "Executing an Ansible Playbook from the Terminal",
                "language": "bash",
                "code": "ansible-playbook -i inventory.ini site.yaml\n# PLAY RECAP:\n# switch-access-1 : ok=2 changed=1 unreachable=0 failed=0\n# switch-access-2 : ok=2 changed=2 unreachable=0 failed=0",
                "explanation": "Executes playbook with real-time feedback detailing changes versus untouched states."
            },
            {
                "title": "Python Script: Capstone Course Completion Summary",
                "language": "python",
                "code": "print('=== 60-DAY COMPUTER NETWORKING BASICS COMPLETE ===')\nprint('Total Lessons: 60 | Total Quizzes: 300 | Mastery: 100%')",
                "explanation": "Summarizes the complete 10-module engineering curriculum mastered across the course."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Ansible Dynamic Inventory Generator",
            description="Write a Python function `generate_ansible_inventory(devices: list) -> dict` that converts a list of device dicts into an Ansible-compatible dynamic JSON inventory dictionary formatted as `{ 'routers': {'hosts': [ip, ...]}, 'switches': {'hosts': [ip, ...]} }`.",
            starter_code="def generate_ansible_inventory(devices: list) -> dict:\n    # Return dynamic inventory dictionary with 'routers' and 'switches' groups\n    pass",
            solution_code="def generate_ansible_inventory(devices: list) -> dict:\n    inventory = {'routers': {'hosts': []}, 'switches': {'hosts': []}}\n    for dev in devices:\n        role = dev.get('role')\n        ip = dev.get('ip')\n        if role == 'router':\n            inventory['routers']['hosts'].append(ip)\n        elif role == 'switch':\n            inventory['switches']['hosts'].append(ip)\n    return inventory",
            expected_output="{'routers': {'hosts': ['192.168.1.1']}, 'switches': {'hosts': ['192.168.1.10', '192.168.1.11']}}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does it mean that Ansible network modules are 'idempotent'?",
                options=[
                    "Running the playbook multiple times makes changes only if the device deviates from the declared state, avoiding duplicate actions",
                    "The playbook permanently erases router memory",
                    "The playbook only runs on leap years",
                    "The playbook requires manual approval for each character"
                ],
                correct_answer="Running the playbook multiple times makes changes only if the device deviates from the declared state, avoiding duplicate actions",
                explanation="Idempotence guarantees that applying an Ansible playbook repeatedly yields the same desired state without re-applying unchanged configurations."
            ),
            QuizQuestionBlueprint(
                question="Why is Ansible described as 'agentless' when managing enterprise routers and switches?",
                options=[
                    "It connects remotely using standard SSH or RESTCONF APIs without requiring specialized software daemons installed on the switch",
                    "It uses telepathy instead of cables",
                    "It does not require any computer or laptop to run",
                    "It cannot configure passwords"
                ],
                correct_answer="It connects remotely using standard SSH or RESTCONF APIs without requiring specialized software daemons installed on the switch",
                explanation="Unlike Puppet or Chef, Ansible requires no custom agents installed on target network gear; it manages devices directly through SSH or APIs."
            ),
            QuizQuestionBlueprint(
                question="What file format is strictly utilized to write Ansible Playbooks?",
                options=[
                    "YAML",
                    "HTML",
                    "CSV",
                    "Assembly language"
                ],
                correct_answer="YAML",
                explanation="Ansible playbooks are structured strictly in human-readable YAML format."
            ),
            QuizQuestionBlueprint(
                question="Which protocol stack layer is responsible for end-to-end reliable delivery and TCP 3-way handshakes?",
                options=[
                    "Layer 4 - Transport Layer",
                    "Layer 2 - Data Link Layer",
                    "Layer 1 - Physical Layer",
                    "Layer 7 - Application Layer"
                ],
                correct_answer="Layer 4 - Transport Layer",
                explanation="Layer 4 (Transport) is responsible for segmentation, port numbers, flow control, and reliable delivery (TCP)."
            ),
            QuizQuestionBlueprint(
                question="Across the complete 60-day networking course, what fundamental transition defines modern network engineering?",
                options=[
                    "Moving from manual, error-prone box-by-box CLI administration to automated, API-driven, intent-based software architectures",
                    "Replacing all routers with 56k dial-up modems",
                    "Abandoning the Internet in favor of printed mail",
                    "Converting all software back to binary punch cards"
                ],
                correct_answer="Moving from manual, error-prone box-by-box CLI administration to automated, API-driven, intent-based software architectures",
                explanation="Modern networking empowers engineers to move beyond manual CLI box configuration into scalable automation using Python, REST APIs, SDN controllers, and Ansible."
            )
        ]
    )
]
