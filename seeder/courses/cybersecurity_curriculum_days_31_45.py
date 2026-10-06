"""
Cybersecurity & IT Fundamentals Curriculum - Days 31 to 45
Module 6: Network & Infrastructure Security (Days 31-37)
Module 7: Cryptography & Data Protection (Days 38-44)
Module 8: Endpoint & Physical Security (Day 45)

Universal Standard Compliant:
- ELI5 markdown theory with beginner analogies
- Shell / Python / configuration snippets
- Daily hands-on coding or practical challenge
- Exactly 5 MCQs per day (75 total for Days 31-45)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_31_TO_45 = [
    # ---------------------------------------------------------
    # Day 31: Firewalls (Network-based, Host-based, WAF)
    # ---------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Firewalls (Network-based, Host-based, WAF)",
        concept="Mastering network perimeter defense: Packet-filtering firewalls, Stateful inspection firewalls, Next-Generation Firewalls (NGFW), Host-based firewalls, and Layer 7 Web Application Firewalls (WAF).",
        analogy="Think of building security: A Packet-Filtering firewall is a bouncer checking guest list names. A Stateful firewall is a bouncer who remembers which guests were already inside so they can return from the restroom without re-checking. A Next-Gen Firewall (NGFW) is an airport X-ray scanner examining what is inside every suitcase. A Web Application Firewall (WAF) is a translator who reads every spoken sentence to make sure nobody slips in a disguised magic spell.",
        theory_sections=[
            {
                "heading": "Firewall Evolution & Types",
                "content": (
                    "Firewalls isolate and protect networks by inspecting traffic against security rules:\n\n"
                    "1. **Packet-Filtering Firewalls (Stateless)**: Inspects Layer 3 and Layer 4 headers (Source/Destination IP and Port) in isolation. Very fast, but cannot track connection state.\n"
                    "2. **Stateful Inspection Firewalls**: Maintains a **State Table** tracking established TCP handshakes. Outbound requests automatically permit inbound response packets without opening static ports.\n"
                    "3. **Next-Generation Firewalls (NGFW)**: Operates up to Layer 7 with Deep Packet Inspection (DPI), integrated IDS/IPS, TLS/SSL decryption, and application awareness (e.g., blocking Facebook games while allowing corporate Facebook posts).\n"
                    "4. **Host-Based vs Network-Based**: Network firewalls are dedicated hardware appliances protecting the whole subnet; host-based firewalls (Windows Defender Firewall, `iptables`/`ufw`) run as software on individual endpoints.\n"
                    "5. **Web Application Firewall (WAF)**: Sits in front of web servers to inspect HTTP/HTTPS payloads for SQL injection, Cross-Site Scripting, and credential stuffing."
                )
            },
            {
                "heading": "The Golden Rule: Implicit Deny",
                "content": (
                    "Enterprise firewalls are strictly configured with an **Implicit Deny** rule at the very bottom of the rule list: *Any traffic not explicitly permitted by a higher rule is automatically dropped.*"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Firewall Rules (Linux UFW & Windows PowerShell)",
                "language": "bash",
                "code": (
                    "# Linux UFW (Uncomplicated Firewall):\n"
                    "sudo ufw default deny incoming       # Enforce implicit deny\n"
                    "sudo ufw default allow outgoing\n"
                    "sudo ufw allow 22/tcp                # Allow SSH\n"
                    "sudo ufw allow 443/tcp               # Allow HTTPS\n"
                    "sudo ufw enable\n\n"
                    "# Windows PowerShell Firewall Rule:\n"
                    "New-NetFirewallRule -DisplayName \"Block Port 23 Telnet\" -Direction Inbound -LocalPort 23 -Protocol TCP -Action Block"
                ),
                "explanation": "Sysadmins configure least-privilege firewall rule sets allowing only necessary ports while dropping unauthorized inbound traffic."
            },
            {
                "title": "Python: Simulating a Stateful Firewall Rule Engine",
                "language": "python",
                "code": (
                    "class StatefulFirewall:\n"
                    "    def __init__(self):\n"
                    "        self.state_table = set()  # (src_ip, dst_ip, src_port, dst_port)\n"
                    "        self.inbound_allow_rules = {(443, 'TCP'), (22, 'TCP')}\n"
                    "    \n"
                    "    def inspect_packet(self, direction: str, src: str, dst: str, port: int, proto: str) -> str:\n"
                    "        if direction == 'OUTBOUND':\n"
                    "            # Track outgoing connection in state table\n"
                    "            self.state_table.add((dst, src, port))  # Reverse mapping\n"
                    "            return 'ALLOW_OUTBOUND'\n"
                    "        \n"
                    "        # Inbound check: Is it an established response?\n"
                    "        if (src, dst, port) in self.state_table:\n"
                    "            return 'ALLOW_ESTABLISHED_RESPONSE'\n"
                    "        \n"
                    "        # Is it an approved new inbound service port?\n"
                    "        if (port, proto) in self.inbound_allow_rules:\n"
                    "            return 'ALLOW_NEW_SERVICE'\n"
                    "        return 'DROP (Implicit Deny)'\n\n"
                    "fw = StatefulFirewall()\n"
                    "fw.inspect_packet('OUTBOUND', '192.168.1.10', '93.184.216.34', 80, 'TCP')\n"
                    "print(fw.inspect_packet('INBOUND', '93.184.216.34', '192.168.1.10', 80, 'TCP'))\n"
                    "print(fw.inspect_packet('INBOUND', '1.2.3.4', '192.168.1.10', 23, 'TCP'))"
                ),
                "explanation": "Demonstrates state tracking: incoming response packets are recognized as part of an established conversation."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_firewall(direction: str, port: int, rule_list: list) -> str` that iterates through a list of rule dicts `[{'direction': str, 'port': int, 'action': 'ALLOW'/'BLOCK'}]` and returns the action of the first matching rule. If no rule matches, return 'BLOCK (Implicit Deny)'.",
            "starter_code": (
                "def evaluate_firewall(direction: str, port: int, rule_list: list) -> str:\n"
                "    # Return matching action or 'BLOCK (Implicit Deny)'\n"
                "    return ''\n\n"
                "rules = [\n"
                "    {'direction': 'INBOUND', 'port': 443, 'action': 'ALLOW'},\n"
                "    {'direction': 'INBOUND', 'port': 22, 'action': 'BLOCK'}\n"
                "]\n"
                "print(evaluate_firewall('INBOUND', 443, rules))\n"
                "print(evaluate_firewall('INBOUND', 22, rules))\n"
                "print(evaluate_firewall('INBOUND', 8080, rules))"
            ),
            "solution_code": (
                "def evaluate_firewall(direction: str, port: int, rule_list: list) -> str:\n"
                "    d_clean = direction.upper()\n"
                "    for rule in rule_list:\n"
                "        if rule.get('direction', '').upper() == d_clean and rule.get('port') == port:\n"
                "            return rule.get('action', 'BLOCK')\n"
                "    return 'BLOCK (Implicit Deny)'\n\n"
                "rules = [\n"
                "    {'direction': 'INBOUND', 'port': 443, 'action': 'ALLOW'},\n"
                "    {'direction': 'INBOUND', 'port': 22, 'action': 'BLOCK'}\n"
                "]\n"
                "print(evaluate_firewall('INBOUND', 443, rules))\n"
                "print(evaluate_firewall('INBOUND', 22, rules))\n"
                "print(evaluate_firewall('INBOUND', 8080, rules))"
            ),
            "expected_output": "ALLOW\nBLOCK\nBLOCK (Implicit Deny)"
        },
        quizzes=[
            {
                "question": "What is the primary operational advantage of a Stateful Inspection Firewall over a Stateless Packet-Filtering Firewall?",
                "options": [
                    "A stateful firewall tracks active connection sessions in a state table, automatically allowing return traffic for established outbound requests",
                    "A stateful firewall runs without electricity",
                    "A stateless firewall is immune to all DDoS attacks",
                    "A stateful firewall physically deletes bad hard drives"
                ],
                "correct_answer": "A stateful firewall tracks active connection sessions in a state table, automatically allowing return traffic for established outbound requests",
                "explanation": "Stateful firewalls remember outbound conversations, avoiding the need to open static wide-open inbound ports for response data."
            },
            {
                "question": "What does the 'Implicit Deny' rule at the bottom of a firewall access control list enforce?",
                "options": [
                    "Any network traffic that is not explicitly permitted by an earlier rule is automatically blocked and dropped",
                    "The firewall reboots every 10 minutes",
                    "All users must change passwords daily",
                    "Outbound web browsing is permanently disabled"
                ],
                "correct_answer": "Any network traffic that is not explicitly permitted by an earlier rule is automatically blocked and dropped",
                "explanation": "Implicit Deny is the foundational principle of least privilege in networking: silence and block everything unless explicitly whitelisted."
            },
            {
                "question": "Which type of firewall is specifically designed to inspect Layer 7 web traffic for SQL Injection, Cross-Site Scripting (XSS), and CSRF attacks?",
                "options": ["Web Application Firewall (WAF)", "Stateless Layer 3 Packet Filter", "Circuit-Level Gateway", "Ethernet Hub"],
                "correct_answer": "Web Application Firewall (WAF)",
                "explanation": "A WAF inspects HTTP/HTTPS application payloads, headers, cookies, and parameters to block web exploits before reaching the web server."
            },
            {
                "question": "What is the difference between a Host-Based Firewall and a Network-Based Firewall?",
                "options": [
                    "A host-based firewall runs as software directly on an individual computer protecting that single host, while a network firewall protects an entire subnet",
                    "Host-based firewalls only work on Linux",
                    "Network firewalls cannot block IP addresses",
                    "Host firewalls are installed in the cloud only"
                ],
                "correct_answer": "A host-based firewall runs as software directly on an individual computer protecting that single host, while a network firewall protects an entire subnet",
                "explanation": "Network firewalls protect perimeter boundaries, while host-based firewalls (like Windows Defender Firewall) enforce defense-in-depth on endpoints."
            },
            {
                "question": "What advanced capability distinguishes a Next-Generation Firewall (NGFW) from traditional stateful firewalls?",
                "options": [
                    "Deep Packet Inspection (DPI) capable of analyzing application layer data, detecting malware payloads, and decrypting TLS traffic",
                    "The ability to run without computer memory",
                    "Providing free internet to neighboring offices",
                    "Transmitting data faster than the speed of light"
                ],
                "correct_answer": "Deep Packet Inspection (DPI) capable of analyzing application layer data, detecting malware payloads, and decrypting TLS traffic",
                "explanation": "NGFWs integrate traditional firewalling with intrusion prevention (IPS), application-level control, and SSL inspection."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 32: IDS (Intrusion Detection System) vs IPS (Intrusion Prevention)
    # ---------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: IDS (Intrusion Detection System) vs IPS (Intrusion Prevention)",
        concept="Differentiating between passive detection (IDS) and active inline prevention (IPS), analyzing detection methodologies (Signature-based vs Heuristic/Anomaly-based), and managing false positives vs false negatives.",
        analogy="Think of bank security: An IDS (Intrusion Detection System) is a security camera watching the lobby—if a masked thief enters, it sounds an alarm buzzer and logs the video, but does not stop them from running away. An IPS (Intrusion Prevention System) is an armed guard stationed inside an airlock door—if someone draws a weapon, the guard physically locks the security doors and blocks their path immediately.",
        theory_sections=[
            {
                "heading": "IDS vs IPS: Passive vs Inline",
                "content": (
                    "Both appliances analyze network packets for malicious activity:\n\n"
                    "1. **IDS (Intrusion Detection System)**: Deployed **Out-of-Band (Passive)** via a Switch Port Analyzer (SPAN) or network TAP. It receives a copy of traffic. If malware is spotted, it generates an alert (syslog, email) and sends TCP Reset (RST) packets. Cannot stop the initial malicious packet.\n"
                    "2. **IPS (Intrusion Prevention System)**: Deployed **Inline** directly in the network traffic path (all packets must physically pass through the IPS). If an exploit is detected, the IPS drops the malicious packets in real time before reaching the destination."
                )
            },
            {
                "heading": "Detection Methodologies: Signatures vs Anomalies",
                "content": (
                    "- **Signature-Based**: Matches packets against a database of known exploit byte sequences (Snort/Suricata rules). Ultra-fast, low false positives, but completely blind to brand-new zero-days.\n"
                    "- **Anomaly / Heuristic-Based**: Establishes a baseline of normal traffic behavior (e.g., standard bandwidth, normal port usage). Flags any statistically abnormal deviations (e.g., a workstation suddenly sending 10 GB of data to an IP in Russia at 3:00 AM)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Writing a Snort / Suricata IDS/IPS Detection Rule",
                "language": "bash",
                "code": (
                    "# Snort Rule format:\n"
                    "# action proto src_ip src_port -> dst_ip dst_port (rule_options)\n"
                    "alert tcp any any -> $HOME_NET 80 (\n"
                    "    msg:\"ATTACK [SQLi] - Classic 'or 1=1' Attempt\";\n"
                    "    content:\"or+1%3D1\"; nocase;\n"
                    "    sid:1000001;\n"
                    "    rev:1;\n"
                    ")"
                ),
                "explanation": "Snort signatures inspect packet payloads for specific hexadecimal or ASCII exploit patterns."
            },
            {
                "title": "Python: Simulating an Inline IPS Packet Dropper",
                "language": "python",
                "code": (
                    "class NetworkIPS:\n"
                    "    def __init__(self):\n"
                    "        # Known exploit signatures\n"
                    "        self.signatures = ['/etc/passwd', 'cmd.exe', 'UNION SELECT']\n"
                    "    \n"
                    "    def process_packet_inline(self, packet_payload: str) -> str:\n"
                    "        for sig in self.signatures:\n"
                    "            if sig.lower() in packet_payload.lower():\n"
                    "                # IPS DROPS packet and terminates connection\n"
                    "                return f'IPS_ACTION: PACKET_DROPPED (Matched Signature: {sig})'\n"
                    "        return 'IPS_ACTION: PACKET_FORWARDED'\n\n"
                    "ips = NetworkIPS()\n"
                    "print(ips.process_packet_inline('GET /index.html HTTP/1.1'))\n"
                    "print(ips.process_packet_inline('GET /view?file=../../etc/passwd HTTP/1.1'))"
                ),
                "explanation": "Inline IPS evaluates packets before forwarding them, dropping malicious traffic before it reaches target servers."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `ips_inspect(payload: str, known_signatures: list) -> dict` that returns a dict `{'status': 'FORWARDED' or 'DROPPED', 'matched_rule': str or None}`. Drop if any signature is found in payload (case-insensitive).",
            "starter_code": (
                "def ips_inspect(payload: str, known_signatures: list) -> dict:\n"
                "    # Return {'status': 'FORWARDED' or 'DROPPED', 'matched_rule': str/None}\n"
                "    return {}\n\n"
                "sigs = ['malicious_payload', 'bash_reverse_shell']\n"
                "print(ips_inspect('GET /home HTTP/1.1', sigs))\n"
                "print(ips_inspect('POST /api data=bash_reverse_shell', sigs))"
            ),
            "solution_code": (
                "def ips_inspect(payload: str, known_signatures: list) -> dict:\n"
                "    clean = payload.lower()\n"
                "    for sig in known_signatures:\n"
                "        if sig.lower() in clean:\n"
                "            return {'status': 'DROPPED', 'matched_rule': sig}\n"
                "    return {'status': 'FORWARDED', 'matched_rule': None}\n\n"
                "sigs = ['malicious_payload', 'bash_reverse_shell']\n"
                "print(ips_inspect('GET /home HTTP/1.1', sigs))\n"
                "print(ips_inspect('POST /api data=bash_reverse_shell', sigs))"
            ),
            "expected_output": "{'status': 'FORWARDED', 'matched_rule': None}\n{'status': 'DROPPED', 'matched_rule': 'bash_reverse_shell'}"
        },
        quizzes=[
            {
                "question": "What is the critical deployment difference between an IDS and an IPS?",
                "options": [
                    "An IDS is deployed passively out-of-band to monitor and alert, while an IPS is deployed inline directly in the traffic flow to actively block attacks",
                    "An IDS is for Windows, while an IPS is for macOS",
                    "An IDS runs without computer hardware",
                    "An IPS can only inspect Wi-Fi networks"
                ],
                "correct_answer": "An IDS is deployed passively out-of-band to monitor and alert, while an IPS is deployed inline directly in the traffic flow to actively block attacks",
                "explanation": "IDS detects and alerts on traffic copies (passive); IPS sits inline on the physical wire and drops malicious packets in real time."
            },
            {
                "question": "What is the main limitation of Signature-Based detection systems in modern cybersecurity?",
                "options": [
                    "They cannot detect zero-day exploits or newly modified malware whose signatures are not yet in the database",
                    "They produce too many false alarms on known viruses",
                    "They take days to inspect a single network packet",
                    "They require dial-up internet connections"
                ],
                "correct_answer": "They cannot detect zero-day exploits or newly modified malware whose signatures are not yet in the database",
                "explanation": "Signature detection requires prior knowledge of the attack pattern. An attacker with a novel zero-day will bypass signature filters."
            },
            {
                "question": "What is a 'False Positive' in the context of an Intrusion Detection System?",
                "options": [
                    "The system generates a security alert on legitimate, harmless user traffic",
                    "An actual attack occurred but the system failed to detect it",
                    "The server crashed due to a power outage",
                    "A user forgot their password"
                ],
                "correct_answer": "The system generates a security alert on legitimate, harmless user traffic",
                "explanation": "A False Positive is a false alarm: benign traffic triggers an alert, wasting analyst triage time."
            },
            {
                "question": "Which detection methodology establishes a statistical baseline of normal network behavior and flags abnormal deviations?",
                "options": ["Anomaly / Heuristic-Based Detection", "Signature-Based Detection", "Static String Matching", "CRC32 Checksumming"],
                "correct_answer": "Anomaly / Heuristic-Based Detection",
                "explanation": "Anomaly detection models normal traffic metrics and generates alerts when unusual spikes or unseen behaviors emerge."
            },
            {
                "question": "What network switch feature is used to send a mirrored copy of all network traffic to a passive IDS sensor?",
                "options": ["SPAN (Port Mirroring)", "Spanning Tree Protocol", "Trunk Port VLAN Tagging", "DHCP Snooping"],
                "correct_answer": "SPAN (Port Mirroring)",
                "explanation": "Switch Port Analyzer (SPAN) mirrors traffic from designated switch ports to a monitoring port connected to the IDS sensor."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 33: VPNs (Virtual Private Networks) and IPsec
    # ---------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: VPNs (Virtual Private Networks) and IPsec",
        concept="Understanding encrypted network tunnels: Site-to-Site vs Remote Access VPNs, IPsec architecture (AH vs ESP, Tunnel mode vs Transport mode), and modern TLS/SSL VPNs (OpenVPN, WireGuard).",
        analogy="Using the public internet without a VPN is like driving an open-air convertible along a public highway where every bystander can look inside and photograph what you are carrying. A VPN is building a private underground bulletproof tunnel straight from your garage directly into the corporate headquarters vault.",
        theory_sections=[
            {
                "heading": "VPN Topologies: Remote Access vs Site-to-Site",
                "content": (
                    "Virtual Private Networks create encrypted tunnels over untrusted networks (the public internet):\n\n"
                    "1. **Remote Access VPN**: Connects individual remote workers to the corporate network via VPN client software (Cisco AnyConnect, OpenVPN, WireGuard).\n"
                    "2. **Site-to-Site VPN**: Interconnects two entire geographically separated branch office networks across the internet. Handled automatically by routers or firewalls without individual desktop client software."
                )
            },
            {
                "heading": "The IPsec Protocol Suite Architecture",
                "content": (
                    "IPsec operates at Layer 3 (Network Layer) to secure IP communications:\n"
                    "- **AH (Authentication Header - IP Protocol 51)**: Provides integrity and authentication, but **NO ENCRYPTION** (data remains visible in cleartext!). Rarely used alone.\n"
                    "- **ESP (Encapsulating Security Payload - IP Protocol 50)**: Provides **CONFIDENTIALITY (ENCRYPTION)**, integrity, and anti-replay protection.\n"
                    "- **Transport Mode**: Only the payload is encrypted; original IP headers remain exposed. Used for direct host-to-host links.\n"
                    "- **Tunnel Mode**: The ENTIRE original IP packet (header and payload) is encrypted and wrapped inside a brand-new outer IP header. Standard for site-to-site VPNs."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Active WireGuard and OpenVPN Tunnel Interfaces",
                "language": "bash",
                "code": (
                    "# Linux WireGuard VPN interface status and cryptographic handshakes:\n"
                    "sudo wg show\n"
                    "# Output: interface: wg0, public key: ..., latest handshake: 1 minute ago, transfer: 50MB\n\n"
                    "# Verifying default routing goes through the VPN tunnel (tun0 / wg0):\n"
                    "ip route show | grep -E 'tun|wg'"
                ),
                "explanation": "Sysadmins verify that all default egress traffic routes across the virtual tunnel adapter rather than the local gateway."
            },
            {
                "title": "Python: Simulating VPN Packet Tunnel Encapsulation",
                "language": "python",
                "code": (
                    "def ipsec_tunnel_encapsulate(original_ip_packet: dict, vpn_gateway_ip: str) -> dict:\n"
                    "    # In Tunnel Mode, the entire original packet is encrypted and nested\n"
                    "    ciphertext_payload = f\"ENCRYPTED_ESP_DATA[{original_ip_packet}]\"\n"
                    "    outer_packet = {\n"
                    "        'src_ip': '198.51.100.1',           # Local VPN Appliance Public IP\n"
                    "        'dst_ip': vpn_gateway_ip,            # Remote Corporate Gateway Public IP\n"
                    "        'protocol': 'ESP (50)',\n"
                    "        'payload': ciphertext_payload\n"
                    "    }\n"
                    "    return outer_packet\n\n"
                    "inner = {'src': '10.0.1.5', 'dst': '10.0.2.80', 'data': 'confidential_finance.xlsx'}\n"
                    "print(ipsec_tunnel_encapsulate(inner, '203.0.113.1'))"
                ),
                "explanation": "Demonstrates IPsec tunnel mode where private internal IP addresses are completely hidden inside an outer routable packet."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_ipsec_security(protocol: str, mode: str) -> dict` that evaluates whether confidentiality (encryption) is provided. Protocol 'ESP' provides encryption; 'AH' does NOT provide encryption. Return dict `{'protocol': protocol, 'mode': mode, 'encryption_enabled': bool}`.",
            "starter_code": (
                "def evaluate_ipsec_security(protocol: str, mode: str) -> dict:\n"
                "    # Return {'protocol': protocol, 'mode': mode, 'encryption_enabled': True/False}\n"
                "    return {}\n\n"
                "print(evaluate_ipsec_security('ESP', 'Tunnel'))\n"
                "print(evaluate_ipsec_security('AH', 'Transport'))"
            ),
            "solution_code": (
                "def evaluate_ipsec_security(protocol: str, mode: str) -> dict:\n"
                "    p_clean = protocol.upper()\n"
                "    has_encryption = (p_clean == 'ESP')\n"
                "    return {\n"
                "        'protocol': p_clean,\n"
                "        'mode': mode.capitalize(),\n"
                "        'encryption_enabled': has_encryption\n"
                "    }\n\n"
                "print(evaluate_ipsec_security('ESP', 'Tunnel'))\n"
                "print(evaluate_ipsec_security('AH', 'Transport'))"
            ),
            "expected_output": "{'protocol': 'ESP', 'mode': 'Tunnel', 'encryption_enabled': True}\n{'protocol': 'AH', 'mode': 'Transport', 'encryption_enabled': False}"
        },
        quizzes=[
            {
                "question": "Which protocol within the IPsec suite is responsible for providing data confidentiality through encryption?",
                "options": ["ESP (Encapsulating Security Payload)", "AH (Authentication Header)", "ICMP", "ARP"],
                "correct_answer": "ESP (Encapsulating Security Payload)",
                "explanation": "ESP encrypts the payload to provide confidentiality. AH only provides integrity and authentication without encrypting data."
            },
            {
                "question": "What is the difference between IPsec 'Transport Mode' and 'Tunnel Mode'?",
                "options": [
                    "Transport mode encrypts only the payload, leaving original IP headers visible; Tunnel mode encrypts the ENTIRE original packet inside a brand-new IP header",
                    "Transport mode is for airplanes; Tunnel mode is for trains",
                    "Tunnel mode does not use encryption",
                    "Transport mode is only supported on mobile phones"
                ],
                "correct_answer": "Transport mode encrypts only the payload, leaving original IP headers visible; Tunnel mode encrypts the ENTIRE original packet inside a brand-new IP header",
                "explanation": "Tunnel mode wraps the original packet (including private internal headers) inside an outer header, shielding network topology."
            },
            {
                "question": "What type of VPN connection permanently links two separate branch offices across the public internet without requiring individual software on user laptops?",
                "options": ["Site-to-Site VPN", "Remote Access VPN", "Dial-Up VPN", "Point-to-Point Bluetooth"],
                "correct_answer": "Site-to-Site VPN",
                "explanation": "Site-to-site VPNs connect two network gateways (routers/firewalls), transparently routing traffic between corporate subnets."
            },
            {
                "question": "Why is using a public Wi-Fi network at an airport or coffee shop dangerous without a VPN?",
                "options": [
                    "Attackers on the same unencrypted Wi-Fi network can capture unencrypted packets, perform ARP poisoning, or launch Evil Twin attacks",
                    "Airport Wi-Fi burns out the laptop battery",
                    "Coffee shop routers delete all Word documents",
                    "Laptops automatically download viruses from airplanes"
                ],
                "correct_answer": "Attackers on the same unencrypted Wi-Fi network can capture unencrypted packets, perform ARP poisoning, or launch Evil Twin attacks",
                "explanation": "Open Wi-Fi lacks peer isolation. A VPN wraps all endpoint traffic in an encrypted tunnel, rendering sniffed frames unreadable."
            },
            {
                "question": "Which modern, lightweight open-source VPN protocol has gained massive adoption due to its small codebase (~4,000 lines of code) and state-of-the-art cryptography?",
                "options": ["WireGuard", "PPTP", "Telnet", "FTP"],
                "correct_answer": "WireGuard",
                "explanation": "WireGuard uses modern cryptography (ChaCha20, Curve25519) with a radically smaller codebase than legacy IPsec or OpenVPN, dramatically reducing attack surface."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 34: Wi-Fi Security Protocols (WEP, WPA, WPA2, WPA3)
    # ---------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Wi-Fi Security Protocols (WEP, WPA, WPA2, WPA3)",
        concept="Tracing the evolution of wireless encryption: WEP (broken RC4), WPA (TKIP band-aid), WPA2 (AES-CCMP, 4-way handshake, KRACK vulnerability), and WPA3 (SAE Dragonfly handshake, Protected Management Frames).",
        analogy="Think of wireless deadbolts: WEP was a paper padlock that anyone could pick with a paperclip in 60 seconds. WPA was a slightly thicker cardboard lock. WPA2 was a heavy steel padlock, but if someone recorded you locking it (4-way handshake), they could take that recording home and guess combinations offline. WPA3 is a biometric titanium vault with an anti-tamper lock that resists offline guessing.",
        theory_sections=[
            {
                "heading": "The Evolution of Wi-Fi Encryption Standards",
                "content": (
                    "Wireless 802.11 transmissions broadcast across open air, requiring cryptographic shielding:\n\n"
                    "1. **WEP (Wired Equivalent Privacy - 1999)**: Uses RC4 stream cipher with a tiny 24-bit **Initialization Vector (IV)**. IVs collide and repeat after capturing a few thousand packets. Can be cracked in under 2 minutes. Completely obsolete.\n"
                    "2. **WPA (Wi-Fi Protected Access - 2003)**: Interim fix using **TKIP (Temporal Key Integrity Protocol)**. Dynamically rotates keys per packet, but still relies on vulnerable RC4.\n"
                    "3. **WPA2 (802.11i - 2004)**: Mandatory **AES-CCMP** encryption. Standard for two decades. Pre-Shared Key (PSK) mode uses a **4-Way Handshake**; attackers capture the handshake and crack the password offline using dictionary attacks. Vulnerable to **KRACK (Key Reinstallation Attack)**.\n"
                    "4. **WPA3 (2018)**: Replaces PSK with **SAE (Simultaneous Authentication of Equals)** using the Dragonfly handshake. Provides **Forward Secrecy**, rendering offline dictionary attacks mathematically impossible. Mandates 192-bit encryption for Enterprise and Protected Management Frames (PMF) to block deauthentication attacks."
                )
            },
            {
                "heading": "Deauthentication Attacks",
                "content": (
                    "In WPA2, Layer 2 management frames are unencrypted. Attackers spoof the AP's MAC address and broadcast **Deauth packets**, instantly kicking victims off the Wi-Fi network to capture their 4-way handshake when they reconnect. WPA3 mandates **PMF (802.11w)**, preventing rogue deauth frames."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Auditing Wi-Fi Encryption Protocols via Command Line",
                "language": "bash",
                "code": (
                    "# Windows PowerShell command to inspect local Wi-Fi encryption:\n"
                    "netsh wlan show interfaces\n"
                    "# Expected Output: Authentication: WPA3-Personal | Cipher: CCMP\n\n"
                    "# Linux Aircrack-ng suite monitoring wireless frames (Ethical Lab):\n"
                    "sudo airodump-ng wlan0mon\n"
                    "# Shows BSSID, Channel, Encryption (WEP, WPA2, WPA3), and ESSID"
                ),
                "explanation": "Security assessments verify that corporate wireless networks do not support legacy WEP or TKIP fallbacks."
            },
            {
                "title": "Python: Classifying Wi-Fi Protocol Security Strength",
                "language": "python",
                "code": (
                    "def audit_wifi_security(protocol: str) -> dict:\n"
                    "    p = protocol.upper()\n"
                    "    ratings = {\n"
                    "        'WEP': ('BROKEN / INSECURE', 'Cracked in minutes via IV collisions', False),\n"
                    "        'WPA': ('DEPRECATED', 'Uses vulnerable TKIP stream cipher', False),\n"
                    "        'WPA2': ('ACCEPTABLE', 'Vulnerable to 4-way handshake capture & offline cracking', True),\n"
                    "        'WPA3': ('EXCELLENT', 'Uses SAE Dragonfly handshake with Forward Secrecy', True)\n"
                    "    }\n"
                    "    status, desc, is_approved = ratings.get(p, ('UNKNOWN', 'Invalid protocol', False))\n"
                    "    return {'protocol': p, 'status': status, 'analysis': desc, 'approved': is_approved}\n\n"
                    "print(audit_wifi_security('WEP'))\n"
                    "print(audit_wifi_security('WPA3'))"
                ),
                "explanation": "Triage logic used in automated compliance scanners to flag legacy wireless configurations."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `is_wifi_secure(protocol: str, cipher: str) -> bool` that returns True only if protocol is 'WPA3' or ('WPA2' with cipher 'AES'/'CCMP'). Return False for 'WEP', 'TKIP', or any other combination.",
            "starter_code": (
                "def is_wifi_secure(protocol: str, cipher: str) -> bool:\n"
                "    # Return True if secure, False otherwise\n"
                "    return False\n\n"
                "print(is_wifi_secure('WPA3', 'AES'))\n"
                "print(is_wifi_secure('WPA2', 'CCMP'))\n"
                "print(is_wifi_secure('WPA2', 'TKIP'))\n"
                "print(is_wifi_secure('WEP', 'RC4'))"
            ),
            "solution_code": (
                "def is_wifi_secure(protocol: str, cipher: str) -> bool:\n"
                "    p = protocol.upper()\n"
                "    c = cipher.upper()\n"
                "    if p == 'WPA3':\n"
                "        return True\n"
                "    if p == 'WPA2' and c in ['AES', 'CCMP']:\n"
                "        return True\n"
                "    return False\n\n"
                "print(is_wifi_secure('WPA3', 'AES'))\n"
                "print(is_wifi_secure('WPA2', 'CCMP'))\n"
                "print(is_wifi_secure('WPA2', 'TKIP'))\n"
                "print(is_wifi_secure('WEP', 'RC4'))"
            ),
            "expected_output": "True\nTrue\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "Why is WEP (Wired Equivalent Privacy) considered completely broken and unsafe to use?",
                "options": [
                    "It uses a weak 24-bit Initialization Vector (IV) with the RC4 cipher, causing key reuse that allows attackers to crack the password in minutes",
                    "WEP only works on desktop computers",
                    "WEP was invented by cybercriminals",
                    "WEP shuts down internet access after 100 megabytes"
                ],
                "correct_answer": "It uses a weak 24-bit Initialization Vector (IV) with the RC4 cipher, causing key reuse that allows attackers to crack the password in minutes",
                "explanation": "WEP's short 24-bit IV results in frequent key collisions. Capturing sufficient IV traffic allows instant key derivation."
            },
            {
                "question": "Which robust symmetric encryption algorithm is utilized by the WPA2 wireless standard?",
                "options": ["AES (Advanced Encryption Standard) with CCMP", "RC4", "DES", "MD5"],
                "correct_answer": "AES (Advanced Encryption Standard) with CCMP",
                "explanation": "WPA2 mandated the replacement of legacy RC4 with military-grade AES encryption operating in CCMP mode."
            },
            {
                "question": "What major vulnerability in WPA2-Personal (PSK) networks allows attackers to crack passwords offline without actively connecting to the router?",
                "options": [
                    "Capturing the 4-Way Handshake frames transmitted when a client connects to the AP, then brute-forcing the hash offline using dictionaries",
                    "Unplugging the router power cord",
                    "Looking at the router's plastic antenna",
                    "Changing the computer screen resolution"
                ],
                "correct_answer": "Capturing the 4-Way Handshake frames transmitted when a client connects to the AP, then brute-forcing the hash offline using dictionaries",
                "explanation": "In WPA2-PSK, an attacker sniffs the 4-way handshake exchange and uses GPU clusters to test billions of dictionary passwords offline."
            },
            {
                "question": "What key cryptographic mechanism does WPA3 introduce to eliminate offline dictionary attacks and provide Forward Secrecy?",
                "options": ["SAE (Simultaneous Authentication of Equals) Dragonfly Handshake", "TKIP", "Cleartext HTTP", "Static WEP Keys"],
                "correct_answer": "SAE (Simultaneous Authentication of Equals) Dragonfly Handshake",
                "explanation": "WPA3 uses the SAE Dragonfly handshake: even if an attacker captures the wireless handshake, offline dictionary guessing is mathematically prevented."
            },
            {
                "question": "What is a 'Deauthentication Attack' on an unhardened WPA2 Wi-Fi network?",
                "options": [
                    "Spoofing the router's MAC address and sending fake disconnect frames to forcefully disconnect a victim, capturing their handshake upon reconnection",
                    "Calling the internet service provider to cancel the account",
                    "Physically cutting the Ethernet cables",
                    "Resetting the router to factory settings"
                ],
                "correct_answer": "Spoofing the router's MAC address and sending fake disconnect frames to forcefully disconnect a victim, capturing their handshake upon reconnection",
                "explanation": "Because 802.11 management frames were unencrypted in WPA2, attackers send spoofed deauth frames to force handshakes for cracking."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 35: Network Segmentation & DMZ (Demilitarized Zone)
    # ---------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Network Segmentation & DMZ (Demilitarized Zone)",
        concept="Mastering enterprise network architecture: VLANs (Virtual LANs), Subnetting, DMZs (Demilitarized Zones), Micro-segmentation, and Zero-Trust lateral movement prevention.",
        analogy="Think of a cruise ship: If the ship's hull was one single open hollow room, a single rock tear would flood the whole vessel and sink it. Instead, naval engineers build watertight steel bulkheads (VLANs & Firewalls) dividing the hull into 20 sealed compartments. If Compartment 3 floods, the watertight doors seal it off, and the ship stays afloat.",
        theory_sections=[
            {
                "heading": "Network Segmentation & VLANs",
                "content": (
                    "Placing all corporate devices (receptionists, finance, IoT printers, guest smartphones, domain controllers) on a single flat network is disastrous:\n\n"
                    "1. **Flat Network Hazard**: If a guest phone or printer is infected, malware uses ARP scanning to discover and compromise domain servers within seconds.\n"
                    "2. **VLANs (Virtual LANs - 802.1Q)**: Logical Layer 2 boundaries created inside network switches. Traffic between VLANs CANNOT pass without going through a Layer 3 firewall.\n"
                    "3. **Micro-segmentation**: Cloud security model where security policies are applied down to individual workloads/containers (e.g., Database container only accepts traffic from Backend App container on port 5432)."
                )
            },
            {
                "heading": "The DMZ (Demilitarized Zone) Architecture",
                "content": (
                    "A **DMZ** is a physical or logical buffer subnetwork that exposes external-facing public services (Web servers, DNS servers, Email relays) to the untrusted internet:\n"
                    "- Internet clients can talk to the DMZ.\n"
                    "- DMZ servers **CANNOT initiate connections into the private internal corporate network**.\n"
                    "- If an attacker exploits a zero-day on the public web server, they are trapped inside the DMZ and cannot access the internal database holding credit cards."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Cisco Switch VLAN Configuration & Routing Boundary",
                "language": "bash",
                "code": (
                    "# Cisco IOS Switch VLAN Segmentation:\n"
                    "Switch(config)# vlan 10\n"
                    "Switch(config-vlan)# name CORPORATE_WORKSTATIONS\n"
                    "Switch(config)# vlan 20\n"
                    "Switch(config-vlan)# name IOT_CAMERAS_PRINTERS\n"
                    "Switch(config)# vlan 30\n"
                    "Switch(config-vlan)# name PUBLIC_DMZ_SERVERS\n\n"
                    "# Assigning physical switch port 1 to VLAN 20:\n"
                    "Switch(config)# interface gigabitethernet 0/1\n"
                    "Switch(config-if)# switchport mode access\n"
                    "Switch(config-if)# switchport access vlan 20"
                ),
                "explanation": "Isolating untrusted IoT hardware on VLAN 20 prevents infected printers from sniffing corporate workstation frames."
            },
            {
                "title": "Python: Simulating DMZ Firewall Traffic Enforcement",
                "language": "python",
                "code": (
                    "def dmz_firewall_rule(src_zone: str, dst_zone: str, port: int) -> str:\n"
                    "    # INTERNET -> DMZ (Allowed for public web port 443)\n"
                    "    if src_zone == 'INTERNET' and dst_zone == 'DMZ' and port == 443:\n"
                    "        return 'ALLOW_PUBLIC_WEB'\n"
                    "    \n"
                    "    # DMZ -> INTERNAL_LAN (STRICTLY FORBIDDEN to prevent pivot attacks!)\n"
                    "    if src_zone == 'DMZ' and dst_zone == 'INTERNAL_LAN':\n"
                    "        return 'CRITICAL_BLOCK: DMZ cannot initiate connection into Internal LAN!'\n"
                    "        \n"
                    "    # INTERNAL_LAN -> DMZ (Allowed for database updates)\n"
                    "    if src_zone == 'INTERNAL_LAN' and dst_zone == 'DMZ':\n"
                    "        return 'ALLOW_INTERNAL_MANAGEMENT'\n"
                    "    return 'BLOCK_DEFAULT'\n\n"
                    "print(dmz_firewall_rule('INTERNET', 'DMZ', 443))\n"
                    "print(dmz_firewall_rule('DMZ', 'INTERNAL_LAN', 1433))"
                ),
                "explanation": "Illustrates DMZ boundary isolation preventing compromised internet-facing servers from pivoting into internal network assets."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str` that returns 'PERMITTED' if src_vlan == dst_vlan or is_firewall_rule_present is True, and 'BLOCKED (Isolated VLAN)' otherwise.",
            "starter_code": (
                "def check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str:\n"
                "    # Return 'PERMITTED' or 'BLOCKED (Isolated VLAN)'\n"
                "    return ''\n\n"
                "print(check_lateral_movement(10, 10, False))\n"
                "print(check_lateral_movement(10, 20, False))\n"
                "print(check_lateral_movement(10, 20, True))"
            ),
            "solution_code": (
                "def check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str:\n"
                "    if src_vlan == dst_vlan:\n"
                "        return 'PERMITTED'\n"
                "    if is_firewall_rule_present:\n"
                "        return 'PERMITTED'\n"
                "    return 'BLOCKED (Isolated VLAN)'\n\n"
                "print(check_lateral_movement(10, 10, False))\n"
                "print(check_lateral_movement(10, 20, False))\n"
                "print(check_lateral_movement(10, 20, True))"
            ),
            "expected_output": "PERMITTED\nBLOCKED (Isolated VLAN)\nPERMITTED"
        },
        quizzes=[
            {
                "question": "What is the primary security goal of a Demilitarized Zone (DMZ) in enterprise network design?",
                "options": [
                    "To isolate publicly accessible servers (like web and email) in a perimeter buffer network so that if compromised, the attacker cannot easily pivot into the internal network",
                    "To provide free Wi-Fi to military personnel",
                    "To turn off all firewalls on holidays",
                    "To double the download speed of video files"
                ],
                "correct_answer": "To isolate publicly accessible servers (like web and email) in a perimeter buffer network so that if compromised, the attacker cannot easily pivot into the internal network",
                "explanation": "DMZs host public services in an isolated zone. Strict firewall rules prevent DMZ servers from initiating inbound sessions into internal LANs."
            },
            {
                "question": "What is a 'Flat Network' and why is it considered a major cybersecurity risk?",
                "options": [
                    "A network where all devices share a single broadcast domain without segmentation; if any single device is infected, malware can easily spread laterally to all others",
                    "A network running on flat fiber optic cables",
                    "A network that has run out of IP addresses",
                    "A website that has no 3D graphics"
                ],
                "correct_answer": "A network where all devices share a single broadcast domain without segmentation; if any single device is infected, malware can easily spread laterally to all others",
                "explanation": "Flat networks lack internal barriers. A compromised guest laptop or IoT thermostat can freely attack internal payroll servers."
            },
            {
                "question": "What network technology logically divides a physical network switch into separate, isolated broadcast domains at Layer 2?",
                "options": ["VLAN (Virtual Local Area Network - 802.1Q)", "NAT", "DNS", "BGP"],
                "correct_answer": "VLAN (Virtual Local Area Network - 802.1Q)",
                "explanation": "VLANs partition physical switch hardware into distinct logical networks. Traffic cannot jump between VLANs without routing through a firewall."
            },
            {
                "question": "What is 'Lateral Movement' in cyber attack lifecycle terminology?",
                "options": [
                    "The techniques an attacker uses to progressively navigate through a network from an initial compromised endpoint to other high-value target systems",
                    "Typing on a keyboard with your left hand",
                    "Moving servers from one physical rack to another",
                    "A mouse moving sideways across the desk"
                ],
                "correct_answer": "The techniques an attacker uses to progressively navigate through a network from an initial compromised endpoint to other high-value target systems",
                "explanation": "After gaining initial entry, adversaries probe internal networks and pivot laterally toward domain controllers and databases."
            },
            {
                "question": "What is 'Micro-segmentation' in cloud and zero-trust environments?",
                "options": [
                    "Enforcing granular security policies and isolation rules directly at the individual workload, virtual machine, or container level",
                    "Cutting network cables into very short pieces",
                    "Using tiny microchip routers",
                    "Dividing passwords into 2-letter chunks"
                ],
                "correct_answer": "Enforcing granular security policies and isolation rules directly at the individual workload, virtual machine, or container level",
                "explanation": "Micro-segmentation creates individual micro-perimeters around workloads, preventing lateral movement even between servers in the same subnet."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 36: Honeypots and Honeynets
    # ---------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: Honeypots and Honeynets",
        concept="Mastering active cyber deception: Low-interaction vs High-interaction Honeypots, Honeynets, Honeytokens (canary credentials), and adversary intelligence gathering.",
        analogy="A Honeypot is a counterfeit bank vault with unlocked glass doors placed deliberately in the middle of a city alleyway, filled with fake gold bars. It has no real money and zero legitimate business customers. Therefore, the second anyone opens the door or steps inside, an alarm bells ring—because there is 100% certainty that anyone touching it is an intruder.",
        theory_sections=[
            {
                "heading": "The Purpose of Honeypots & Deception Technology",
                "content": (
                    "A **Honeypot** is a decoy computer system explicitly configured to be attacked, probed, and compromised:\n\n"
                    "1. **Zero Legitimate Traffic**: Because the honeypot has no real business function, **any interaction is inherently malicious**, yielding zero false positives.\n"
                    "2. **Adversary Early Warning**: Alerts the SOC the instant an attacker initiates internal reconnaissance.\n"
                    "3. **Threat Intelligence Gathering**: Researchers study attacker tactics, exploits, and toolkits in a controlled environment.\n"
                    "4. **Low-Interaction Honeypots**: Emulates specific services (e.g., fake SSH banner on port 22). Low risk, low resource usage, but cannot observe full exploit detonation.\n"
                    "5. **High-Interaction Honeypots**: Real operating systems and real databases heavily monitored and sandboxed. High intelligence value, but carries risk if the attacker attempts to pivot."
                )
            },
            {
                "heading": "Honeynets and Honeytokens (Canary Artifacts)",
                "content": (
                    "- **Honeynet**: An entire network of interconnected honeypots simulating a fake enterprise domain.\n"
                    "- **Honeytokens / Canary Tokens**: Fake credentials, fake API keys (e.g., dummy AWS access keys planted in GitHub repos), or bogus database records. If that canary key is ever used, alerts immediately reveal who stole it."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Deploying an Open-Source Cowrie SSH/Telnet Honeypot",
                "language": "bash",
                "code": (
                    "# Cowrie is a medium/high interaction SSH and Telnet honeypot:\n"
                    "# 1. Clone and launch via Docker container:\n"
                    "docker run -p 2222:2222 cowrie/cowrie\n\n"
                    "# 2. Inspecting live attacker login attempts logged as JSON:\n"
                    "tail -f cowrie/var/log/cowrie/cowrie.json | jq '{src_ip: .src_ip, user: .username, pass: .password}'"
                ),
                "explanation": "Honeypots log attacker credentials and downloaded malware samples directly into threat intelligence pipelines."
            },
            {
                "title": "Python: Building a Simple Port Trap Honeypot",
                "language": "python",
                "code": (
                    "import socket\n"
                    "import time\n\n"
                    "def run_honey_listener(trap_port: int):\n"
                    "    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
                    "    s.bind(('0.0.0.0', trap_port))\n"
                    "    s.listen(1)\n"
                    "    print(f'[*] Honeypot listening on trap port {trap_port}...')\n"
                    "    \n"
                    "    # Simulating connection trigger\n"
                    "    # In production, this runs in a loop logging attacker IPs\n"
                    "    # s.accept() -> Triggers critical SOC alert\n"
                    "    return 'HONEYPOT_ACTIVE'\n\n"
                    "print(run_honey_listener(23)) # Telnet trap"
                ),
                "explanation": "Trap listeners detect reconnaissance port sweeps across corporate subnets."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `inspect_honeytoken(used_token: str, canary_tokens: set) -> dict` that returns `{'is_honeypot_triggered': True, 'alert_level': 'CRITICAL'}` if the token is in canary_tokens, otherwise `{'is_honeypot_triggered': False, 'alert_level': 'NONE'}`.",
            "starter_code": (
                "def inspect_honeytoken(used_token: str, canary_tokens: set) -> dict:\n"
                "    # Return alert dict\n"
                "    return {}\n\n"
                "canaries = {'AKIA_CANARY_FAKE_KEY_123', 'fake_admin_pass'}\n"
                "print(inspect_honeytoken('AKIA_CANARY_FAKE_KEY_123', canaries))\n"
                "print(inspect_honeytoken('LEGIT_PROD_KEY_456', canaries))"
            ),
            "solution_code": (
                "def inspect_honeytoken(used_token: str, canary_tokens: set) -> dict:\n"
                "    is_hit = used_token in canary_tokens\n"
                "    return {\n"
                "        'is_honeypot_triggered': is_hit,\n"
                "        'alert_level': 'CRITICAL' if is_hit else 'NONE'\n"
                "    }\n\n"
                "canaries = {'AKIA_CANARY_FAKE_KEY_123', 'fake_admin_pass'}\n"
                "print(inspect_honeytoken('AKIA_CANARY_FAKE_KEY_123', canaries))\n"
                "print(inspect_honeytoken('LEGIT_PROD_KEY_456', canaries))"
            ),
            "expected_output": "{'is_honeypot_triggered': True, 'alert_level': 'CRITICAL'}\n{'is_honeypot_triggered': False, 'alert_level': 'NONE'}"
        },
        quizzes=[
            {
                "question": "What is the primary purpose of deploying a 'Honeypot' in an enterprise network?",
                "options": [
                    "To serve as a decoy system designed to lure, detect, and study malicious activity without hosting any legitimate business data or traffic",
                    "To produce honey in the office kitchen",
                    "To store company customer backup databases",
                    "To boost wireless internet signals"
                ],
                "correct_answer": "To serve as a decoy system designed to lure, detect, and study malicious activity without hosting any legitimate business data or traffic",
                "explanation": "Honeypots act as traps: because no legitimate employee has a reason to contact them, any connection represents an attacker or malware."
            },
            {
                "question": "Why do alerts generated by honeypots have an exceptionally low False Positive rate?",
                "options": [
                    "Because honeypots have zero legitimate production users, meaning virtually any interaction is inherently unauthorized or malicious",
                    "Because honeypots are written in Python",
                    "Because honeypots cannot connect to routers",
                    "Because honeypots only operate during business hours"
                ],
                "correct_answer": "Because honeypots have zero legitimate production users, meaning virtually any interaction is inherently unauthorized or malicious",
                "explanation": "With no authorized users or scheduled tasks contacting the decoy, almost all alerts represent legitimate adversary activity."
            },
            {
                "question": "What is a 'Honeytoken' (or Canary Token)?",
                "options": [
                    "A bogus piece of data (such as a fake database record, fake password, or fake API key) planted deliberately to detect unauthorized data theft",
                    "A cryptocurrency coin given to employees",
                    "A physical gold medal awarded to programmers",
                    "A discount coupon for antivirus software"
                ],
                "correct_answer": "A bogus piece of data (such as a fake database record, fake password, or fake API key) planted deliberately to detect unauthorized data theft",
                "explanation": "Honeytokens are boobytrapped digital assets. If someone attempts to use a planted fake AWS key, automated alarms fire immediately."
            },
            {
                "question": "What is the main risk associated with deploying a High-Interaction Honeypot (a real, fully functional operating system)?",
                "options": [
                    "If not properly isolated and contained, an attacker could compromise the honeypot and use it as a launchpad to attack real internal production systems",
                    "It consumes too much paper",
                    "It makes coffee machines malfunction",
                    "It changes all computer desktop wallpapers"
                ],
                "correct_answer": "If not properly isolated and contained, an attacker could compromise the honeypot and use it as a launchpad to attack real internal production systems",
                "explanation": "High-interaction honeypots run real OS software; if containment controls fail, the attacker can use the decoy as an internal pivot point."
            },
            {
                "question": "What is a 'Honeynet'?",
                "options": [
                    "A network composed of multiple honeypots designed to simulate an entire corporate network environment",
                    "A fishing net made of fiber optic cables",
                    "A Wi-Fi network that only works on laptops",
                    "An internet connection provided by the city"
                ],
                "correct_answer": "A network composed of multiple honeypots designed to simulate an entire corporate network environment",
                "explanation": "A honeynet scales honeypots into a full decoy network with multiple servers, routers, and simulated workstations to observe complex attack chains."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 37: Proxy Servers
    # ---------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Proxy Servers",
        concept="Differentiating between Forward Proxies (client-side privacy, content filtering, caching) and Reverse Proxies (server-side load balancing, SSL termination, DDoS protection).",
        analogy="Think of intermediaries: A Forward Proxy is an attorney you hire to make purchases for you—the seller never knows your identity because your attorney speaks on your behalf. A Reverse Proxy is the grand reception desk of a skyscraper—visitors never wander into the CEO's office directly; the receptionist verifies credentials, balances elevator loads, and delivers packages to the right floor.",
        theory_sections=[
            {
                "heading": "Forward Proxy vs Reverse Proxy",
                "content": (
                    "Proxies act as intermediaries for network requests:\n\n"
                    "1. **Forward Proxy**: Sits in front of internal **clients** reaching out to the internet.\n"
                    "   - *Functions*: Hides client IP addresses, filters objectionable or malicious websites, caches frequently requested web assets to save bandwidth, and performs outbound SSL/TLS decryption inspection.\n"
                    "2. **Reverse Proxy**: Sits in front of internal **servers** receiving inbound traffic from the internet.\n"
                    "   - *Functions*: Conceals backend server IP addresses, provides **Load Balancing** across server pools, handles **SSL/TLS Termination** (decrypting HTTPS so backend servers focus purely on compute), and blocks web application attacks."
                )
            },
            {
                "heading": "Transparent vs Explicit Proxies",
                "content": (
                    "- **Explicit Proxy**: Client web browsers must be configured with the proxy's IP and port (or via a PAC auto-config file).\n"
                    "- **Transparent Proxy**: Operates at the network gateway without requiring any client-side software configuration. All outbound port 80/443 traffic is invisibly redirected into the proxy via router policy."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reverse Proxy Configuration (NGINX Load Balancing & SSL Termination)",
                "language": "bash",
                "code": (
                    "# NGINX Reverse Proxy configuration block:\n"
                    "server {\n"
                    "    listen 443 ssl;\n"
                    "    server_name api.company.com;\n"
                    "    ssl_certificate /etc/ssl/cert.pem;\n"
                    "    ssl_certificate_key /etc/ssl/privkey.pem;\n\n"
                    "    location / {\n"
                    "        # Forward traffic to internal private server pool:\n"
                    "        proxy_pass http://internal_backend_servers;\n"
                    "        proxy_set_header X-Forwarded-For $remote_addr;\n"
                    "    }\n"
                    "}"
                ),
                "explanation": "The reverse proxy terminates HTTPS publicly and forwards requests to private internal cluster nodes."
            },
            {
                "title": "Python: Querying Web Resources Through a Forward Proxy",
                "language": "python",
                "code": (
                    "import requests\n\n"
                    "def fetch_via_proxy(target_url: str, proxy_url: str) -> dict:\n"
                    "    proxies = {'http': proxy_url, 'https': proxy_url}\n"
                    "    try:\n"
                    "        # Request exits via proxy IP rather than local machine IP\n"
                    "        r = requests.get(target_url, proxies=proxies, timeout=5)\n"
                    "        return {'status_code': r.status_code, 'proxied': True}\n"
                    "    except Exception as e:\n"
                    "        return {'error': str(e), 'proxied': False}\n\n"
                    "print(fetch_via_proxy('https://httpbin.org/ip', 'http://10.10.1.1:8080'))"
                ),
                "explanation": "Demonstrates programmatic routing of client traffic through an outbound enterprise forward proxy."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_proxy_role(protects: str) -> str` that returns 'FORWARD_PROXY' if protects == 'CLIENTS', 'REVERSE_PROXY' if protects == 'SERVERS', and 'UNKNOWN' otherwise.",
            "starter_code": (
                "def classify_proxy_role(protects: str) -> str:\n"
                "    # Return 'FORWARD_PROXY', 'REVERSE_PROXY', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_proxy_role('CLIENTS'))\n"
                "print(classify_proxy_role('SERVERS'))"
            ),
            "solution_code": (
                "def classify_proxy_role(protects: str) -> str:\n"
                "    p = protects.strip().upper()\n"
                "    if p == 'CLIENTS':\n"
                "        return 'FORWARD_PROXY'\n"
                "    if p == 'SERVERS':\n"
                "        return 'REVERSE_PROXY'\n"
                "    return 'UNKNOWN'\n\n"
                "print(classify_proxy_role('CLIENTS'))\n"
                "print(classify_proxy_role('SERVERS'))"
            ),
            "expected_output": "FORWARD_PROXY\nREVERSE_PROXY"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a Forward Proxy and a Reverse Proxy?",
                "options": [
                    "A Forward Proxy protects internal clients reaching out to the internet, while a Reverse Proxy protects internal servers receiving traffic from the internet",
                    "A Forward Proxy is for sending emails; a Reverse Proxy is for reading documents",
                    "Reverse proxies only work in reverse alphabetical order",
                    "There is no difference; both are exact synonyms"
                ],
                "correct_answer": "A Forward Proxy protects internal clients reaching out to the internet, while a Reverse Proxy protects internal servers receiving traffic from the internet",
                "explanation": "Forward proxies manage outbound client traffic (anonymity, filtering); reverse proxies manage inbound server traffic (load balancing, SSL termination)."
            },
            {
                "question": "What is 'SSL/TLS Termination' on a Reverse Proxy?",
                "options": [
                    "The reverse proxy decrypts incoming HTTPS traffic at the perimeter, forwarding unencrypted HTTP requests to backend cluster servers to relieve their CPU load",
                    "Deleting all digital certificates from the web server",
                    "Canceling the company's domain name registration",
                    "Shutting down the web browser permanently"
                ],
                "correct_answer": "The reverse proxy decrypts incoming HTTPS traffic at the perimeter, forwarding unencrypted HTTP requests to backend cluster servers to relieve their CPU load",
                "explanation": "Offloading SSL/TLS decryption to the reverse proxy centralizes certificate management and frees backend servers from cryptographic overhead."
            },
            {
                "question": "Why do corporate enterprise networks force employee web browsers to connect through an outbound Forward Proxy?",
                "options": [
                    "To enforce URL filtering (blocking gambling or malware sites), inspect traffic for data loss (DLP), and cache web content to save bandwidth",
                    "To make videos play in slow motion",
                    "To charge employees per megabyte of data",
                    "To prevent keyboards from wearing out"
                ],
                "correct_answer": "To enforce URL filtering (blocking gambling or malware sites), inspect traffic for data loss (DLP), and cache web content to save bandwidth",
                "explanation": "Forward proxies provide visibility and control over outbound enterprise web traffic, stopping malware downloads and data exfiltration."
            },
            {
                "question": "What is a 'Transparent Proxy'?",
                "options": [
                    "A proxy that intercepts network traffic at the gateway without requiring any manual proxy configuration changes on client computers",
                    "A computer monitor made of transparent glass",
                    "A proxy server that publishes all passwords online",
                    "A software program that has no code"
                ],
                "correct_answer": "A proxy that intercepts network traffic at the gateway without requiring any manual proxy configuration changes on client computers",
                "explanation": "Transparent proxies invisibly divert client traffic using router redirect rules without end-user awareness or device configuration."
            },
            {
                "question": "Which HTTP header is typically added by a reverse proxy to inform backend servers of the true original client IP address?",
                "options": ["X-Forwarded-For", "Authorization", "User-Agent", "Set-Cookie"],
                "correct_answer": "X-Forwarded-For",
                "explanation": "Because backend servers see the reverse proxy's IP as the direct source, the proxy inserts the `X-Forwarded-For` header containing the client's original IP."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 38: Basics of Cryptography (Plaintext vs Ciphertext)
    # ---------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Basics of Cryptography (Plaintext vs Ciphertext)",
        concept="Mastering foundational cryptography: Plaintext (readable data), Ciphertext (encrypted scrambled data), Ciphers (mathematical algorithms), Keys (secret entropy), Kerckhoffs's Principle, and the Caesar cipher.",
        analogy="Think of locking a handwritten diary: The readable English words are **Plaintext**. The mechanical lock mechanism is the **Cipher** (the mathematical algorithm). The unique physical metal key is the **Key**. The scrambled, completely unreadable mess of ink inside is the **Ciphertext**. Anyone who finds the diary cannot read a word without having the matching metal key.",
        theory_sections=[
            {
                "heading": "Core Cryptographic Terminology",
                "content": (
                    "Cryptography transforms readable information into unreadable formats to ensure confidentiality and integrity:\n\n"
                    "1. **Plaintext (Cleartext)**: Unencrypted, human-readable data (e.g., `'Meet at noon'`, credit card numbers, passwords).\n"
                    "2. **Ciphertext**: Scrambled data produced by an encryption algorithm, appearing completely random and indecipherable without the decryption key.\n"
                    "3. **Cipher (Algorithm)**: The mathematical function or steps used to perform encryption and decryption (e.g., AES, RSA, Caesar substitution).\n"
                    "4. **Key**: A secret value (string of bits) that feeds into the cipher. The security of the ciphertext depends entirely on keeping the key secret.\n"
                    "5. **Cryptanalysis**: The art and science of analyzing and breaking cryptographic systems without knowing the key."
                )
            },
            {
                "heading": "Kerckhoffs's Principle: Security Through Obscurity is Dead",
                "content": (
                    "Formulated in the 19th century by Auguste Kerckhoffs:\n"
                    "*'A cryptosystem should be secure even if everything about the system, except the key, is public knowledge.'*\n"
                    "Never design a secret proprietary algorithm. Modern ciphers like AES-256 are completely open source and mathematically analyzed by the world's top mathematicians. True security rests entirely in the secrecy and entropy of the **Key**, not the algorithm."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Python: Demonstrating the Historic Caesar Substitution Cipher",
                "language": "python",
                "code": (
                    "def caesar_encrypt(plaintext: str, shift: int) -> str:\n"
                    "    ciphertext = []\n"
                    "    for char in plaintext:\n"
                    "        if char.isalpha():\n"
                    "            base = ord('A') if char.isupper() else ord('a')\n"
                    "            shifted = (ord(char) - base + shift) % 26 + base\n"
                    "            ciphertext.append(chr(shifted))\n"
                    "        else:\n"
                    "            ciphertext.append(char)\n"
                    "    return ''.join(ciphertext)\n\n"
                    "secret = 'ATTACK AT DAWN'\n"
                    "cipher = caesar_encrypt(secret, shift=3)\n"
                    "print(f'Plaintext:  {secret}')\n"
                    "print(f'Ciphertext: {cipher}') # 'DZZDFN DW GDZQ'"
                ),
                "explanation": "Illustrates how simple substitution transforms plaintext into ciphertext using a numerical key shift."
            },
            {
                "title": "Generating Cryptographically Secure Random Keys via Python",
                "language": "python",
                "code": (
                    "import secrets\n\n"
                    "# Generating high-entropy 256-bit (32 byte) encryption key:\n"
                    "aes_256_key = secrets.token_bytes(32)\n"
                    "hex_key = aes_256_key.hex()\n"
                    "print('Cryptographic Key (Hex):', hex_key)\n"
                    "print('Key Length in Bits:     ', len(aes_256_key) * 8)"
                ),
                "explanation": "Standard random libraries like `random.randint` are predictable; cryptographic security mandates OS entropy via `secrets`."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `caesar_decrypt(ciphertext: str, shift: int) -> str` that reverses the Caesar cipher shift to recover the original plaintext string.",
            "starter_code": (
                "def caesar_decrypt(ciphertext: str, shift: int) -> str:\n"
                "    # Return original decrypted plaintext\n"
                "    return ''\n\n"
                "print(caesar_decrypt('DZZDFN DW GDZQ', 3))\n"
                "print(caesar_decrypt('KHOOR', 3))"
            ),
            "solution_code": (
                "def caesar_decrypt(ciphertext: str, shift: int) -> str:\n"
                "    plaintext = []\n"
                "    for char in ciphertext:\n"
                "        if char.isalpha():\n"
                "            base = ord('A') if char.isupper() else ord('a')\n"
                "            shifted = (ord(char) - base - shift) % 26 + base\n"
                "            plaintext.append(chr(shifted))\n"
                "        else:\n"
                "            plaintext.append(char)\n"
                "    return ''.join(plaintext)\n\n"
                "print(caesar_decrypt('DZZDFN DW GDZQ', 3))\n"
                "print(caesar_decrypt('KHOOR', 3))"
            ),
            "expected_output": "ATTACK AT DAWN\nHELLO"
        },
        quizzes=[
            {
                "question": "What is the term for original, readable, unencrypted information in cryptography?",
                "options": ["Plaintext (or Cleartext)", "Ciphertext", "Hash Digest", "Entropy"],
                "correct_answer": "Plaintext (or Cleartext)",
                "explanation": "Plaintext is raw, human-readable data before an encryption algorithm converts it into ciphertext."
            },
            {
                "question": "What is 'Ciphertext'?",
                "options": [
                    "The scrambled, unreadable output produced by an encryption algorithm that can only be deciphered with the matching key",
                    "A computer programming language",
                    "A font style in Microsoft Word",
                    "A deleted text file"
                ],
                "correct_answer": "The scrambled, unreadable output produced by an encryption algorithm that can only be deciphered with the matching key",
                "explanation": "Ciphertext is the encrypted result of running plaintext through a cipher with a secret key."
            },
            {
                "question": "What is 'Kerckhoffs's Principle' in cryptographic engineering?",
                "options": [
                    "A cryptographic system should be secure even if everything about the algorithm is publicly known, as long as the key remains secret",
                    "All encryption algorithms must be kept top secret from the public",
                    "Passwords must be changed every 3 days",
                    "Computers should never be connected to the internet"
                ],
                "correct_answer": "A cryptographic system should be secure even if everything about the algorithm is publicly known, as long as the key remains secret",
                "explanation": "Kerckhoffs established that security should rely solely on key secrecy, rejecting 'security through obscurity' of algorithms."
            },
            {
                "question": "Why is 'Security Through Obscurity' (keeping an algorithm secret rather than using tested public algorithms) considered poor security practice?",
                "options": [
                    "Proprietary secret algorithms almost always contain severe hidden mathematical flaws that attackers quickly discover through reverse engineering",
                    "Secret algorithms cost too much money to print",
                    "Secret algorithms are illegal under international copyright law",
                    "Secret algorithms cannot run on Intel CPUs"
                ],
                "correct_answer": "Proprietary secret algorithms almost always contain severe hidden mathematical flaws that attackers quickly discover through reverse engineering",
                "explanation": "Public algorithms like AES have withstood decades of global peer review; homegrown secret algorithms inevitably fail."
            },
            {
                "question": "In modern cryptography, what determines the ultimate strength and resistance of an encrypted message against brute-force attacks?",
                "options": [
                    "The length (entropy) and unpredictability of the secret cryptographic Key",
                    "The physical weight of the computer hard drive",
                    "Whether the computer is connected via Wi-Fi or Ethernet",
                    "The number of monitors on the desk"
                ],
                "correct_answer": "The length (entropy) and unpredictability of the secret cryptographic Key",
                "explanation": "Key size dictates brute-force complexity: an AES-256 key has 2^256 combinations, taking supercomputers billions of years to exhaust."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 39: Symmetric Encryption
    # ---------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Symmetric Encryption",
        concept="Mastering symmetric-key cryptography: Shared secret keys, Block ciphers vs Stream ciphers, DES/3DES legacy vulnerabilities, and the modern AES (Advanced Encryption Standard) gold standard.",
        analogy="Think of a locked metal toolbox: Symmetric encryption uses **one single physical key** to both lock AND unlock the toolbox. If Alice wants to send a secret tool to Bob, she locks the box with her key. But Bob can only open it if Alice also gives him a duplicate copy of that EXACT same key. The big challenge: how does Alice get the key to Bob safely without a thief stealing it in transit?",
        theory_sections=[
            {
                "heading": "Symmetric Encryption Mechanics",
                "content": (
                    "In symmetric cryptography, a **single shared secret key** is used for both encryption and decryption:\n"
                    "- **Extreme Speed**: Symmetric algorithms rely on rapid mathematical permutations and substitutions, making them 1,000x faster than asymmetric algorithms. Ideal for bulk data (hard drives, streaming video, database files).\n"
                    "- **Block Ciphers**: Encrypt data in fixed-size blocks (e.g., 128-bit chunks). Examples: AES, DES, Blowfish.\n"
                    "- **Stream Ciphers**: Encrypt data bit-by-bit or byte-by-byte continuously. Examples: RC4 (deprecated), ChaCha20."
                )
            },
            {
                "heading": "Evolution: From DES to AES",
                "content": (
                    "1. **DES (Data Encryption Standard - 1977)**: 56-bit key length. Obsolete; can be brute-forced in under 24 hours.\n"
                    "2. **3DES (Triple DES)**: Encrypts data with DES three times. Secure, but slow and being phased out.\n"
                    "3. **AES (Advanced Encryption Standard - 2001 / Rijndael)**: The global standard. Fixed block size of 128 bits with key lengths of **128, 192, or 256 bits**. Zero practical attacks exist against full AES-256."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Encrypting Files with OpenSSL AES-256-CBC via Terminal",
                "language": "bash",
                "code": (
                    "# Encrypting a confidential text document using AES-256 with a password:\n"
                    "openssl enc -aes-256-cbc -salt -in confidential.txt -out confidential.enc\n\n"
                    "# Decrypting the encrypted file back to plaintext:\n"
                    "openssl enc -d -aes-256-cbc -in confidential.enc -out decrypted.txt"
                ),
                "explanation": "Standard OpenSSL CLI commands used by system administrators to encrypt sensitive archives with AES-256."
            },
            {
                "title": "Python: Demonstrating Symmetric AES-GCM Encryption (Authenticated Encryption)",
                "language": "python",
                "code": (
                    "# Note: In production use the 'cryptography' library (AESGCM)\n"
                    "import secrets\n\n"
                    "def simulate_symmetric_key_exchange():\n"
                    "    # Shared secret key known to both Alice and Bob\n"
                    "    shared_key = secrets.token_bytes(32)  # 256 bits\n"
                    "    print(f'Shared Secret Key: {shared_key.hex()[:16]}... (Must be kept secret!)')\n"
                    "    return shared_key\n\n"
                    "key = simulate_symmetric_key_exchange()\n"
                    "print('Key length in bytes:', len(key))"
                ),
                "explanation": "Demonstrates generation of a 256-bit symmetric key that must be pre-shared between communicating parties."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `symmetric_key_pairs(num_users: int) -> int` that calculates how many unique shared secret keys are required for `num_users` individuals to all communicate securely with each other using symmetric encryption (Formula: `n * (n - 1) / 2`).",
            "starter_code": (
                "def symmetric_key_pairs(num_users: int) -> int:\n"
                "    # Return total unique symmetric keys required\n"
                "    return 0\n\n"
                "print(symmetric_key_pairs(2))\n"
                "print(symmetric_key_pairs(10))\n"
                "print(symmetric_key_pairs(100))"
            ),
            "solution_code": (
                "def symmetric_key_pairs(num_users: int) -> int:\n"
                "    if num_users < 2:\n"
                "        return 0\n"
                "    return (num_users * (num_users - 1)) // 2\n\n"
                "print(symmetric_key_pairs(2))\n"
                "print(symmetric_key_pairs(10))\n"
                "print(symmetric_key_pairs(100))"
            ),
            "expected_output": "1\n45\n4950"
        },
        quizzes=[
            {
                "question": "What is the defining characteristic of Symmetric Encryption?",
                "options": [
                    "A single, identical secret key is used for both encrypting the plaintext and decrypting the ciphertext",
                    "Two different keys are used: one public and one private",
                    "No keys are needed to decrypt data",
                    "It only encrypts numbers, not letters"
                ],
                "correct_answer": "A single, identical secret key is used for both encrypting the plaintext and decrypting the ciphertext",
                "explanation": "In symmetric systems (like AES), both sender and receiver must possess the exact same shared secret key."
            },
            {
                "question": "What is the primary operational advantage of Symmetric Encryption over Asymmetric Encryption?",
                "options": [
                    "Symmetric encryption is computationally lightweight and dramatically faster, making it suitable for bulk data transfers",
                    "Symmetric keys can be published openly on the internet",
                    "Symmetric algorithms do not require electricity",
                    "Symmetric encryption never uses mathematical formulas"
                ],
                "correct_answer": "Symmetric encryption is computationally lightweight and dramatically faster, making it suitable for bulk data transfers",
                "explanation": "Symmetric ciphers use fast hardware-accelerated bitwise operations, encrypting gigabytes of data in seconds."
            },
            {
                "question": "Which symmetric cipher is universally adopted as the modern gold standard by governments, banks, and cybersecurity frameworks?",
                "options": ["AES (Advanced Encryption Standard)", "DES (Data Encryption Standard)", "Caesar Cipher", "RC4"],
                "correct_answer": "AES (Advanced Encryption Standard)",
                "explanation": "AES was selected by NIST in 2001, providing impenetrable security at 128, 192, and 256-bit key sizes."
            },
            {
                "question": "What is the 'Key Distribution Problem' inherent to symmetric cryptography?",
                "options": [
                    "Securely delivering the shared secret key to the recipient over an untrusted network without an eavesdropper intercepting it",
                    "Keys taking up too much hard drive storage",
                    "Key generation wearing out the computer CPU",
                    "Forgetting where the physical key was placed"
                ],
                "correct_answer": "Securely delivering the shared secret key to the recipient over an untrusted network without an eavesdropper intercepting it",
                "explanation": "If Alice and Bob have never met, sending the symmetric key over the internet risks interception, which led to the invention of asymmetric cryptography."
            },
            {
                "question": "Why is the original 56-bit DES (Data Encryption Standard) considered completely insecure today?",
                "options": [
                    "Its 56-bit key size is so small that modern computers can brute-force all possible keys in just a few hours",
                    "DES was deleted from the internet",
                    "DES cannot encrypt vowels",
                    "DES requires an analog dial-up telephone"
                ],
                "correct_answer": "Its 56-bit key size is so small that modern computers can brute-force all possible keys in just a few hours",
                "explanation": "56 bits yields only 72 quadrillion combinations, easily brute-forced by modern cloud compute clusters."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 40: Asymmetric Encryption (Public Key & Private Key)
    # ---------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Asymmetric Encryption (Public Key & Private Key)",
        concept="Mastering public-key cryptography: Mathematically paired keys (Public Key to encrypt, Private Key to decrypt), Diffie-Hellman key exchange, RSA, and Elliptic Curve Cryptography (ECC).",
        analogy="Think of a public post office drop box: The mail drop slot is the **Public Key**—anyone in the entire world can drop a sealed letter into the box. But once the letter falls inside, only the mail carrier who owns the physical brass key (**Private Key**) can open the door and retrieve the letter. Anyone can deposit (encrypt), but only the owner can unlock (decrypt).",
        theory_sections=[
            {
                "heading": "Asymmetric Cryptography Architecture",
                "content": (
                    "Invented to solve the symmetric key distribution problem, asymmetric encryption uses a **mathematically linked keypair**:\n\n"
                    "1. **Public Key**: Distributed freely and openly to the entire world. Anyone can use your public key to encrypt a secret message addressed to you.\n"
                    "2. **Private Key**: Kept strictly secret by the owner and **NEVER SHARED**. Only your private key can decrypt messages encrypted with your matching public key.\n"
                    "3. **Mathematical Foundations**: Relies on 'one-way trapdoor functions'—math that is easy to compute in one direction, but computationally impossible to reverse without a secret trapdoor:\n"
                    "   - **RSA (Rivest-Shamir-Adleman)**: Relies on the extreme difficulty of factoring the product of two massive prime numbers (2048 to 4096 bits).\n"
                    "   - **ECC (Elliptic Curve Cryptography)**: Relies on the discrete logarithm problem over elliptic curves. Provides equivalent security to RSA at dramatically smaller key sizes (e.g., 256-bit ECC matches 3072-bit RSA), saving CPU and battery on mobile devices."
                )
            },
            {
                "heading": "Hybrid Cryptography: The Best of Both Worlds",
                "content": (
                    "Asymmetric encryption is computationally slow and cannot encrypt large gigabyte files. Real-world protocols (HTTPS, SSH, PGP) use **Hybrid Encryption**:\n"
                    "1. Use Asymmetric crypto (RSA/ECC/Diffie-Hellman) to safely negotiate a temporary random symmetric session key.\n"
                    "2. Use fast Symmetric crypto (AES-256) with that session key to encrypt the actual web traffic or file."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Generating RSA and ECC Keypairs via OpenSSL CLI",
                "language": "bash",
                "code": (
                    "# Generating a 2048-bit RSA private key:\n"
                    "openssl genrsa -out private_key.pem 2048\n\n"
                    "# Extracting the matching public key to share with the world:\n"
                    "openssl rsa -in private_key.pem -pubout -out public_key.pem\n\n"
                    "# Generating modern Elliptic Curve (ECC - prime256v1) private key:\n"
                    "openssl ecparam -name prime256v1 -genkey -noout -out ecc_private.pem"
                ),
                "explanation": "Standard commands used to generate public/private key pairs for SSH servers and SSL certificates."
            },
            {
                "title": "Python: Demonstrating Asymmetric Hybrid Key Exchange Concept",
                "language": "python",
                "code": (
                    "def simulate_hybrid_handshake():\n"
                    "    # Step 1: Server sends Public Key to Client\n"
                    "    server_public_key = 'SERVER_PUB_KEY_RSA_4096'\n"
                    "    \n"
                    "    # Step 2: Client generates high-speed symmetric AES session key\n"
                    "    session_key = 'AES_SESSION_SECRET_987654'\n"
                    "    \n"
                    "    # Step 3: Client encrypts session key with server's public key\n"
                    "    encrypted_session_key = f'RSA_ENCRYPTED({session_key})_BY_{server_public_key}'\n"
                    "    \n"
                    "    # Step 4: Server decrypts using its Private Key\n"
                    "    print('[Client] Transmitting encrypted session key over internet...')\n"
                    "    print(f'[Server] Decrypted session key using Private Key: {session_key}')\n"
                    "    print('[Both] Subsequent gigabytes of data encrypted via fast AES-256!')\n\n"
                    "simulate_hybrid_handshake()"
                ),
                "explanation": "Demonstrates the hybrid encryption model utilized in HTTPS (TLS) handshakes."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool` that verifies asymmetric confidentiality: data encrypted with 'PUBLIC' must be decrypted with 'PRIVATE' to return True. Any other combination returns False.",
            "starter_code": (
                "def check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool:\n"
                "    # Return True if valid asymmetric encryption/decryption pair\n"
                "    return False\n\n"
                "print(check_asymmetric_rule('PUBLIC', 'PRIVATE'))\n"
                "print(check_asymmetric_rule('PUBLIC', 'PUBLIC'))\n"
                "print(check_asymmetric_rule('PRIVATE', 'PRIVATE'))"
            ),
            "solution_code": (
                "def check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool:\n"
                "    e = encrypt_key_type.upper()\n"
                "    d = decrypt_key_type.upper()\n"
                "    return (e == 'PUBLIC' and d == 'PRIVATE')\n\n"
                "print(check_asymmetric_rule('PUBLIC', 'PRIVATE'))\n"
                "print(check_asymmetric_rule('PUBLIC', 'PUBLIC'))\n"
                "print(check_asymmetric_rule('PRIVATE', 'PRIVATE'))"
            ),
            "expected_output": "True\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "If Alice wants to send a confidential encrypted message to Bob using Asymmetric Cryptography, which key must Alice use to encrypt the message?",
                "options": ["Bob's Public Key", "Bob's Private Key", "Alice's Private Key", "Alice's Public Key"],
                "correct_answer": "Bob's Public Key",
                "explanation": "To send confidential data to Bob, Alice encrypts it using Bob's freely available Public Key. Only Bob's matching Private Key can decrypt it."
            },
            {
                "question": "What is the primary operational advantage of Elliptic Curve Cryptography (ECC) over traditional RSA?",
                "options": [
                    "ECC provides equivalent cryptographic security with significantly smaller key sizes, reducing compute overhead and power consumption",
                    "ECC can only be broken by aliens",
                    "ECC eliminates the need for private keys",
                    "ECC does not use math"
                ],
                "correct_answer": "ECC provides equivalent cryptographic security with significantly smaller key sizes, reducing compute overhead and power consumption",
                "explanation": "A 256-bit ECC key offers comparable security to a 3072-bit RSA key, providing high speed and low memory footprints ideal for mobile and IoT devices."
            },
            {
                "question": "What is 'Hybrid Cryptography' as used in HTTPS (TLS)?",
                "options": [
                    "Using asymmetric cryptography to securely exchange a temporary symmetric session key, then using fast symmetric AES to encrypt the actual data stream",
                    "Using both gasoline and electric batteries to power servers",
                    "Switching between Windows and Linux every hour",
                    "Using two passwords instead of one"
                ],
                "correct_answer": "Using asymmetric cryptography to securely exchange a temporary symmetric session key, then using fast symmetric AES to encrypt the actual data stream",
                "explanation": "Hybrid encryption combines the key-distribution solution of asymmetric crypto with the raw processing speed of symmetric ciphers."
            },
            {
                "question": "What happens if someone accidentally publishes or shares their Asymmetric Private Key online?",
                "options": [
                    "Anyone who obtains the private key can now decrypt all past and future confidential messages addressed to that entity and impersonate their digital signature",
                    "The public key automatically deletes itself",
                    "The internet service provider shuts off power",
                    "Nothing, because public keys protect private keys"
                ],
                "correct_answer": "Anyone who obtains the private key can now decrypt all past and future confidential messages addressed to that entity and impersonate their digital signature",
                "explanation": "The private key is the foundation of identity and decryption. Compromising it completely breaks confidentiality and authenticity."
            },
            {
                "question": "Can an Asymmetric Public Key be used to decrypt a message that was encrypted using that exact same Public Key?",
                "options": [
                    "No, only the mathematically paired Private Key can decrypt messages encrypted by the Public Key",
                    "Yes, public keys work in both directions",
                    "Yes, but only within 5 minutes of encryption",
                    "Only if the computer is connected to the internet"
                ],
                "correct_answer": "No, only the mathematically paired Private Key can decrypt messages encrypted by the Public Key",
                "explanation": "Asymmetric cryptography is asymmetric: one key encrypts, but only the other paired key can reverse the mathematical trapdoor."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 41: Hashing (MD5, SHA-1, SHA-256)
    # ---------------------------------------------------------
    DayBlueprint(
        order=41,
        title="Day 41: Hashing (MD5, SHA-1, SHA-256)",
        concept="Mastering cryptographic hash functions: One-way directionality, fixed-length digests, collision resistance, the avalanche effect, obsolete algorithms (MD5, SHA-1), and modern standards (SHA-2, SHA-3, bcrypt).",
        analogy="Think of a food blender making a strawberry-banana fruit smoothie: Turning whole strawberries and bananas into a smoothie is trivial (hashing). But taking a glass of smoothie and un-blending it back into intact, whole, fresh strawberries is physically impossible (one-way property). And if you change even one seed, the color of the smoothie completely changes (avalanche effect).",
        theory_sections=[
            {
                "heading": "Properties of Cryptographic Hash Functions",
                "content": (
                    "A cryptographic hash function takes an arbitrary-sized input string/file and produces a **fixed-size alphanumeric output (Digest)**:\n\n"
                    "1. **One-Way (Pre-image Resistance)**: Computationally infeasible to reverse a hash digest back into the original input (`Hash(X) = Y`, cannot calculate `X` from `Y`).\n"
                    "2. **Deterministic**: The exact same input will ALWAYS produce the exact same hash output every single time.\n"
                    "3. **Fixed Output Length**: A 5-letter word and a 500-page encyclopedia both produce an identical 256-bit (64 hex characters) digest under SHA-256.\n"
                    "4. **Avalanche Effect**: Changing a single comma or bit in the input radically scrambles over 50% of the output digest characters.\n"
                    "5. **Collision Resistance**: Computationally impossible to find two different inputs `A` and `B` where `Hash(A) == Hash(B)`."
                )
            },
            {
                "heading": "Broken Hashes vs Modern Standards",
                "content": (
                    "- **MD5 (128-bit) & SHA-1 (160-bit)**: **BROKEN**. Practical collision attacks exist (SHAttered attack in 2017 created two different PDFs with the identical SHA-1 hash). Never use for digital certificates or signatures.\n"
                    "- **SHA-2 (SHA-256, SHA-512)**: Modern secure standard. Robust against collisions.\n"
                    "- **Password Hashing (bcrypt, Argon2, PBKDF2)**: General hashes (SHA-256) are too fast, allowing GPUs to guess billions of passwords per second. Password storage requires **slow, salted, memory-hard algorithms** like Argon2."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Downloaded File Integrity with SHA-256 (CLI)",
                "language": "bash",
                "code": (
                    "# Linux / macOS: Calculating SHA-256 checksum:\n"
                    "sha256sum ubuntu-24.04-desktop-amd64.iso\n\n"
                    "# Windows PowerShell Checksum:\n"
                    "Get-FileHash -Algorithm SHA256 .\\installer.exe"
                ),
                "explanation": "Comparing calculated file hashes against vendor-published hashes verifies files were not corrupted or backdoored in transit."
            },
            {
                "title": "Python: Demonstrating the Avalanche Effect in SHA-256",
                "language": "python",
                "code": (
                    "import hashlib\n\n"
                    "def hash_str(text: str) -> str:\n"
                    "    return hashlib.sha256(text.encode()).hexdigest()\n\n"
                    "input1 = 'The quick brown fox jumps over the lazy dog.'\n"
                    "input2 = 'The quick brown fox jumps over the lazy dog?' # Single character change!\n\n"
                    "h1 = hash_str(input1)\n"
                    "h2 = hash_str(input2)\n\n"
                    "print('Hash 1:', h1)\n"
                    "print('Hash 2:', h2)\n"
                    "print('Hashes Match:', h1 == h2)"
                ),
                "explanation": "Illustrates how altering a single punctuation mark completely randomizes the entire resulting 256-bit hexadecimal digest."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `verify_file_integrity(calculated_hash: str, published_hash: str) -> bool` that returns True if the hashes match (case-insensitive and stripping whitespace), otherwise False.",
            "starter_code": (
                "def verify_file_integrity(calculated_hash: str, published_hash: str) -> bool:\n"
                "    # Return True if hashes match\n"
                "    return False\n\n"
                "print(verify_file_integrity('a1b2c3d4', 'A1B2C3D4'))\n"
                "print(verify_file_integrity('a1b2c3d4 ', 'a1b2c3d5'))"
            ),
            "solution_code": (
                "def verify_file_integrity(calculated_hash: str, published_hash: str) -> bool:\n"
                "    clean_calc = calculated_hash.strip().lower()\n"
                "    clean_pub = published_hash.strip().lower()\n"
                "    return clean_calc == clean_pub\n\n"
                "print(verify_file_integrity('a1b2c3d4', 'A1B2C3D4'))\n"
                "print(verify_file_integrity('a1b2c3d4 ', 'a1b2c3d5'))"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary difference between Encryption and Hashing?",
                "options": [
                    "Encryption is a two-way process designed to be decrypted with a key; Hashing is a one-way mathematical function that can never be decrypted",
                    "Encryption is for numbers; Hashing is for letters",
                    "Hashing requires a password to read",
                    "There is no difference"
                ],
                "correct_answer": "Encryption is a two-way process designed to be decrypted with a key; Hashing is a one-way mathematical function that can never be decrypted",
                "explanation": "Encryption preserves the ability to reverse data back to plaintext; hashing destroys the original data to create a permanent one-way fingerprint."
            },
            {
                "question": "What is a 'Hash Collision' in cryptographic systems?",
                "options": [
                    "When two completely different input strings or files produce the exact same hash output digest",
                    "When a computer hard drive crashes while hashing",
                    "When two computers download the same file at once",
                    "When a password is longer than 256 characters"
                ],
                "correct_answer": "When two completely different input strings or files produce the exact same hash output digest",
                "explanation": "A collision occurs when `Hash(A) == Hash(B)` for distinct inputs A and B, breaking the fundamental integrity guarantee of the cipher."
            },
            {
                "question": "Why are MD5 and SHA-1 no longer considered secure for digital signatures and certificates?",
                "options": [
                    "Researchers have demonstrated practical collision attacks where two different files can be crafted with identical hash values",
                    "They can only run on Windows 98",
                    "The US government deleted the source code",
                    "They take days to calculate"
                ],
                "correct_answer": "Researchers have demonstrated practical collision attacks where two different files can be crafted with identical hash values",
                "explanation": "Both MD5 and SHA-1 suffer from collision vulnerabilities, allowing attackers to forge digital certificates with matching hashes."
            },
            {
                "question": "What is the 'Avalanche Effect' in cryptographic hashing?",
                "options": [
                    "Changing even a single bit of the input data results in a radically different, unpredictable hash digest",
                    "A virus that deletes files like an avalanche of snow",
                    "A computer cooling fan running at maximum speed",
                    "Hashing thousands of files simultaneously"
                ],
                "correct_answer": "Changing even a single bit of the input data results in a radically different, unpredictable hash digest",
                "explanation": "The avalanche effect ensures that small input modifications completely scramble the output, preventing attackers from guessing input patterns."
            },
            {
                "question": "Why should passwords stored in a database be hashed using slow, memory-hard algorithms like Argon2 or bcrypt rather than fast SHA-256?",
                "options": [
                    "Fast algorithms like SHA-256 allow attackers with modern GPUs to compute billions of guesses per second during offline dictionary attacks",
                    "SHA-256 cannot hash letters",
                    "Argon2 uses less database storage space",
                    "bcrypt automatically sends passwords to users via SMS"
                ],
                "correct_answer": "Fast algorithms like SHA-256 allow attackers with modern GPUs to compute billions of guesses per second during offline dictionary attacks",
                "explanation": "SHA-256 is designed for fast file verification; password hashes must be intentionally slow and resource-intensive to resist GPU brute-forcing."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 42: Digital Signatures & Non-repudiation
    # ---------------------------------------------------------
    DayBlueprint(
        order=42,
        title="Day 42: Digital Signatures & Non-repudiation",
        concept="Mastering cryptographic identity verification: Digital Signatures (Hashing + Asymmetric encryption), Non-repudiation (legal accountability), Integrity verification, and code signing.",
        analogy="Think of signing an important paper legal contract: A handwritten signature is easy to photocopy or forge. A Digital Signature is like dipping the document into a high-tech wax that locks the ink forever (Integrity), stamped with your personal unique wax seal (Authenticity). If someone changes even one comma on page 4, the wax shatters instantly, proving the document was tampered with.",
        theory_sections=[
            {
                "heading": "How Digital Signatures Work",
                "content": (
                    "A Digital Signature provides three vital security guarantees:\n"
                    "1. **Authenticity**: Proves the sender's true identity.\n"
                    "2. **Integrity**: Proves the message was not modified in transit.\n"
                    "3. **Non-repudiation**: The signer cannot claim 'I never sent this!' because only their private key could have created the signature.\n\n"
                    "Signing and Verification Workflow:\n"
                    "- **Sender (Signer)**:\n"
                    "  1. Takes the document and computes a cryptographic hash (e.g., SHA-256).\n"
                    "  2. Encrypts that hash with their **PRIVATE KEY**. The resulting encrypted hash is the **Digital Signature**.\n"
                    "- **Recipient (Verifier)**:\n"
                    "  1. Decrypts the signature using the sender's **PUBLIC KEY** to reveal Hash A.\n"
                    "  2. Independently hashes the received document to calculate Hash B.\n"
                    "  3. If `Hash A == Hash B`, the signature is 100% valid!"
                )
            },
            {
                "heading": "Code Signing",
                "content": (
                    "Software developers digitally sign executables (.exe, .pkg) using a code-signing certificate. When Windows SmartScreen or macOS Gatekeeper runs the installer, it verifies the signature to ensure malware has not infected the binary."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Signing and Verifying a File Using OpenSSL CLI",
                "language": "bash",
                "code": (
                    "# Step 1: Sign the document using the private key (SHA-256):\n"
                    "openssl dgst -sha256 -sign signer_private.pem -out contract.sig contract.pdf\n\n"
                    "# Step 2: Verify the digital signature using the signer's public key:\n"
                    "openssl dgst -sha256 -verify signer_public.pem -signature contract.sig contract.pdf\n"
                    "# Output: Verified OK"
                ),
                "explanation": "Standard cryptographic workflow used to sign legal contracts and software releases."
            },
            {
                "title": "Python: Simulating Digital Signature Verification Logic",
                "language": "python",
                "code": (
                    "import hashlib\n\n"
                    "def simulate_digital_signature(message: str, private_key_id: str) -> dict:\n"
                    "    msg_hash = hashlib.sha256(message.encode()).hexdigest()\n"
                    "    # Simulating signature = hash encrypted by private key\n"
                    "    signature = f'SIG_SIGNED_BY_{private_key_id}[{msg_hash}]'\n"
                    "    return {'message': message, 'signature': signature}\n\n"
                    "def verify_signature(package: dict, expected_signer: str) -> bool:\n"
                    "    msg = package['message']\n"
                    "    sig = package['signature']\n"
                    "    calc_hash = hashlib.sha256(msg.encode()).hexdigest()\n"
                    "    expected_sig = f'SIG_SIGNED_BY_{expected_signer}[{calc_hash}]'\n"
                    "    return sig == expected_sig\n\n"
                    "pkg = simulate_digital_signature('Transfer $10,000 to Bob', 'ALICE_PRIV')\n"
                    "print('Valid Signature:', verify_signature(pkg, 'ALICE_PRIV'))\n"
                    "pkg['message'] = 'Transfer $99,000 to Bob' # Tampered!\n"
                    "print('Tampered Signature Valid:', verify_signature(pkg, 'ALICE_PRIV'))"
                ),
                "explanation": "Demonstrates why tampering with a signed message invalidates the signature."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_signature_keys(action: str, key_type: str) -> bool` that returns True if action == 'SIGN' and key_type == 'PRIVATE', or if action == 'VERIFY' and key_type == 'PUBLIC'. Otherwise return False.",
            "starter_code": (
                "def check_signature_keys(action: str, key_type: str) -> bool:\n"
                "    # Return True for valid signature key roles\n"
                "    return False\n\n"
                "print(check_signature_keys('SIGN', 'PRIVATE'))\n"
                "print(check_signature_keys('VERIFY', 'PUBLIC'))\n"
                "print(check_signature_keys('SIGN', 'PUBLIC'))"
            ),
            "solution_code": (
                "def check_signature_keys(action: str, key_type: str) -> bool:\n"
                "    act = action.upper()\n"
                "    k = key_type.upper()\n"
                "    if act == 'SIGN' and k == 'PRIVATE':\n"
                "        return True\n"
                "    if act == 'VERIFY' and k == 'PUBLIC':\n"
                "        return True\n"
                "    return False\n\n"
                "print(check_signature_keys('SIGN', 'PRIVATE'))\n"
                "print(check_signature_keys('VERIFY', 'PUBLIC'))\n"
                "print(check_signature_keys('SIGN', 'PUBLIC'))"
            ),
            "expected_output": "True\nTrue\nFalse"
        },
        quizzes=[
            {
                "question": "Which key is used by the SENDER to create a Digital Signature on a document?",
                "options": ["The Sender's Private Key", "The Sender's Public Key", "The Recipient's Public Key", "The Recipient's Private Key"],
                "correct_answer": "The Sender's Private Key",
                "explanation": "The sender encrypts the document hash with their own Private Key. Because only the sender possesses this key, it proves authenticity."
            },
            {
                "question": "What is 'Non-repudiation' in information security?",
                "options": [
                    "A legal and technical assurance that the sender cannot deny having created and sent a specific message or transaction",
                    "Refusing to pay a credit card bill",
                    "A firewall blocking spam emails",
                    "A software license agreement"
                ],
                "correct_answer": "A legal and technical assurance that the sender cannot deny having created and sent a specific message or transaction",
                "explanation": "Non-repudiation provides indisputable proof of origin: since only the sender holds the private key, they cannot claim someone else signed it."
            },
            {
                "question": "Which key is used by the RECIPIENT to verify that a digital signature is genuine and unaltered?",
                "options": ["The Sender's Public Key", "The Sender's Private Key", "The Recipient's Private Key", "A shared symmetric password"],
                "correct_answer": "The Sender's Public Key",
                "explanation": "Anyone can use the sender's freely available Public Key to decrypt the signature and verify that the decrypted hash matches the document."
            },
            {
                "question": "If an attacker modifies even a single letter in a digitally signed legal PDF, what happens during signature verification?",
                "options": [
                    "Verification fails immediately because the recalculated hash will not match the hash decrypted from the signature",
                    "The signature automatically updates to match the new text",
                    "The recipient's computer shuts down",
                    "The PDF turns black and white"
                ],
                "correct_answer": "Verification fails immediately because the recalculated hash will not match the hash decrypted from the signature",
                "explanation": "Due to the avalanche effect of hashing, any alteration produces a completely different hash, failing verification."
            },
            {
                "question": "What is 'Code Signing' in software distribution?",
                "options": [
                    "Developers digitally sign application executable files to prove the code comes from a legitimate publisher and has not been infected with malware",
                    "Writing comments in computer code",
                    "Translating code into another language",
                    "Formatting code with automated linters"
                ],
                "correct_answer": "Developers digitally sign application executable files to prove the code comes from a legitimate publisher and has not been infected with malware",
                "explanation": "Code signing certificates allow operating systems (Windows SmartScreen, macOS Gatekeeper) to trust the software author."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 43: PKI (Public Key Infrastructure) & Digital Certificates (SSL/TLS)
    # ---------------------------------------------------------
    DayBlueprint(
        order=43,
        title="Day 43: PKI (Public Key Infrastructure) & Digital Certificates (SSL/TLS)",
        concept="Mastering digital trust: Public Key Infrastructure (PKI), Certificate Authorities (CA), X.509 certificate fields, the TLS handshake, Certificate Revocation Lists (CRL), and OCSP stapling.",
        analogy="Think of a government passport office: Anyone can print a piece of paper claiming 'I am the King of England' (a self-signed key). But border customs officers won't trust it. Instead, you go to a recognized, trusted government passport agency (Certificate Authority). The agency verifies your birth certificate, prints your passport (Digital Certificate) with holographic seals and digital chips, and stamps it. When you travel, border agents trust you because they trust the passport agency.",
        theory_sections=[
            {
                "heading": "The Components of Public Key Infrastructure (PKI)",
                "content": (
                    "PKI provides the framework that binds public keys to human or corporate identities:\n\n"
                    "1. **Certificate Authority (CA)**: A trusted third-party organization (DigiCert, Let's Encrypt, Sectigo) that issues and digitally signs certificates.\n"
                    "2. **Digital Certificate (X.509)**: An electronic credential containing:\n"
                    "   - Subject Common Name (e.g., `*.google.com`)\n"
                    "   - The Subject's Public Key\n"
                    "   - Validity period (Not Before / Not After)\n"
                    "   - Digital Signature of the issuing CA.\n"
                    "3. **Trust Chains**: Operating systems and browsers come pre-installed with a **Root CA Certificate Store**. A website certificate is trusted if it chains back through intermediate CAs to a trusted Root CA."
                )
            },
            {
                "heading": "Certificate Revocation: CRL vs OCSP",
                "content": (
                    "When a private key is leaked or an employee leaves, the certificate must be revoked immediately:\n"
                    "- **CRL (Certificate Revocation List)**: A periodically published list of revoked certificate serial numbers. Large and slow.\n"
                    "- **OCSP (Online Certificate Status Protocol)**: Real-time query to the CA asking 'Is certificate #1234 valid right now?'.\n"
                    "- **OCSP Stapling**: The web server queries the CA periodically and 'staples' a timestamped, signed OCSP response to the TLS handshake, saving browser latency."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting TLS Certificates and Expiration via OpenSSL CLI",
                "language": "bash",
                "code": (
                    "# Querying live SSL/TLS certificate from a web server:\n"
                    "openssl s_client -connect google.com:443 -servername google.com </dev/null |\n"
                    "openssl x509 -noout -issuer -subject -dates\n\n"
                    "# Output:\n"
                    "# issuer=C = US, O = Google Trust Services, CN = WR2\n"
                    "# subject=CN = *.google.com\n"
                    "# notBefore=Aug 12 08:35:10 2024 GMT\n"
                    "# notAfter=Nov  4 08:35:09 2024 GMT"
                ),
                "explanation": "Security teams monitor certificate expiration dates to prevent service outages caused by expired SSL certificates."
            },
            {
                "title": "Python: Checking Certificate Expiration Date Programmatically",
                "language": "python",
                "code": (
                    "import ssl\n"
                    "import socket\n"
                    "import datetime\n\n"
                    "def check_cert_expiry(hostname: str) -> dict:\n"
                    "    ctx = ssl.create_default_context()\n"
                    "    with socket.create_connection((hostname, 443), timeout=5) as sock:\n"
                    "        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:\n"
                    "            cert = ssock.getpeercert()\n"
                    "            exp_str = cert['notAfter']\n"
                    "            exp_date = datetime.datetime.strptime(exp_str, '%b %d %H:%M:%S %Y %Z')\n"
                    "            days_left = (exp_date - datetime.datetime.utcnow()).days\n"
                    "            return {'hostname': hostname, 'days_until_expiry': days_left, 'is_expired': days_left <= 0}\n\n"
                    "print(check_cert_expiry('google.com'))"
                ),
                "explanation": "Automated monitoring script alerting sysadmins when SSL certificates have fewer than 30 days remaining."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `validate_cert_status(days_left: int, is_revoked: bool) -> str` that returns 'REVOKED' if is_revoked is True, 'EXPIRED' if days_left <= 0, 'EXPIRING_SOON' if 0 < days_left <= 30, and 'VALID' if days_left > 30.",
            "starter_code": (
                "def validate_cert_status(days_left: int, is_revoked: bool) -> str:\n"
                "    # Return certificate status string\n"
                "    return ''\n\n"
                "print(validate_cert_status(90, False))\n"
                "print(validate_cert_status(15, False))\n"
                "print(validate_cert_status(-2, False))\n"
                "print(validate_cert_status(90, True))"
            ),
            "solution_code": (
                "def validate_cert_status(days_left: int, is_revoked: bool) -> str:\n"
                "    if is_revoked:\n"
                "        return 'REVOKED'\n"
                "    if days_left <= 0:\n"
                "        return 'EXPIRED'\n"
                "    if days_left <= 30:\n"
                "        return 'EXPIRING_SOON'\n"
                "    return 'VALID'\n\n"
                "print(validate_cert_status(90, False))\n"
                "print(validate_cert_status(15, False))\n"
                "print(validate_cert_status(-2, False))\n"
                "print(validate_cert_status(90, True))"
            ),
            "expected_output": "VALID\nEXPIRING_SOON\nEXPIRED\nREVOKED"
        },
        quizzes=[
            {
                "question": "What is the primary role of a Certificate Authority (CA) in Public Key Infrastructure (PKI)?",
                "options": [
                    "A trusted third party that verifies an entity's identity and issues a cryptographically signed digital certificate binding their public key to their identity",
                    "A company that sells hard drives",
                    "A government agency that monitors text messages",
                    "A web browser extension that blocks advertisements"
                ],
                "correct_answer": "A trusted third party that verifies an entity's identity and issues a cryptographically signed digital certificate binding their public key to their identity",
                "explanation": "CAs act as the root of digital trust, confirming that a public key belongs to the real domain owner (e.g., google.com)."
            },
            {
                "question": "Why does a web browser display a 'Your Connection is Not Private' warning when encountering a Self-Signed certificate?",
                "options": [
                    "The certificate was not signed by a trusted Root Certificate Authority present in the operating system's root store",
                    "The website is written in an unsupported programming language",
                    "The user's Wi-Fi router is out of range",
                    "The website has too many images"
                ],
                "correct_answer": "The certificate was not signed by a trusted Root Certificate Authority present in the operating system's root store",
                "explanation": "Anyone can create a self-signed certificate. Browsers only trust certificates that chain back to recognized Root CAs."
            },
            {
                "question": "What is the purpose of the Online Certificate Status Protocol (OCSP)?",
                "options": [
                    "To check in real-time whether a specific digital certificate has been revoked prior to its scheduled expiration date",
                    "To renew domain registrations automatically",
                    "To generate passwords for web browsers",
                    "To calculate download speeds"
                ],
                "correct_answer": "To check in real-time whether a specific digital certificate has been revoked prior to its scheduled expiration date",
                "explanation": "OCSP provides real-time revocation status queries, replacing large, slow Certificate Revocation Lists (CRLs)."
            },
            {
                "question": "What is 'OCSP Stapling'?",
                "options": [
                    "The web server regularly queries the CA and 'staples' a timestamped, signed OCSP validity proof directly into the TLS handshake, improving speed and privacy",
                    "Physically stapling printouts of digital certificates",
                    "Combining two different domain names into one",
                    "Pinning a certificate to the browser toolbar"
                ],
                "correct_answer": "The web server regularly queries the CA and 'staples' a timestamped, signed OCSP validity proof directly into the TLS handshake, improving speed and privacy",
                "explanation": "OCSP stapling removes the need for each individual browser to contact the CA, enhancing privacy and speeding up handshakes."
            },
            {
                "question": "What standard format defines the structure of modern digital certificates used across the internet?",
                "options": ["X.509", "RFC 1918", "IEEE 802.3", "ASCII 128"],
                "correct_answer": "X.509",
                "explanation": "ITU-T X.509 is the universal standard specifying public key certificates, certificate revocation lists, and attribute authorities."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 44: Data States (Data at Rest, in Transit, in Use)
    # ---------------------------------------------------------
    DayBlueprint(
        order=44,
        title="Day 44: Data States (Data at Rest, in Transit, in Use)",
        concept="Mastering data protection across the three fundamental states: Data at Rest (storage encryption), Data in Transit (network wire encryption), and Data in Use (active memory & confidential computing).",
        analogy="Think of gold bullion coins: Data at Rest is gold locked inside a steel bank vault (encrypted SSD). Data in Transit is gold moving between cities inside an armored security truck escorted by guards (TLS tunnel). Data in Use is gold sitting out on the jeweler's workbench being melted and weighed—at that exact second, the gold is vulnerable to someone grabbing it off the table (RAM scraping).",
        theory_sections=[
            {
                "heading": "The Three States of Digital Data",
                "content": (
                    "Security controls must protect data throughout its entire lifecycle:\n\n"
                    "1. **Data at Rest**: Inactive data stored persistently on physical media (hard drives, flash storage, SANs, cloud S3 buckets, tape backups).\n"
                    "   - *Controls*: Full Disk Encryption (**BitLocker**, LUKS, FileVault), database column-level encryption (TDE), self-encrypting drives (SEDs).\n"
                    "2. **Data in Transit (Data in Motion)**: Data traversing an internal or external network (between clients and servers, or server-to-server).\n"
                    "   - *Controls*: Transport Layer Security (**TLS 1.3**), IPsec VPNs, SSH, HTTPS. Prevents eavesdropping and MitM packet sniffing.\n"
                    "3. **Data in Use**: Data actively loaded into volatile system memory (**RAM**, CPU registers, cache) being processed by an application.\n"
                    "   - *Vulnerabilities*: RAM scraping malware (e.g., BlackPOS attacking Target retail registers), memory dumps, cold boot attacks.\n"
                    "   - *Emerging Controls*: **Confidential Computing** using hardware-enforced memory encryption enclaves (Intel SGX, AMD SEV)."
                )
            },
            {
                "heading": "Data Loss Prevention (DLP)",
                "content": (
                    "DLP software monitors all three states: scanning stored network drives (Rest), inspecting outbound emails and web uploads (Transit), and blocking clipboard copying or USB transfers (Use)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Full Disk Encryption Status (Windows & Linux)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Auditing BitLocker full-disk encryption:\n"
                    "Get-BitLockerVolume -MountPoint \"C:\" | Select-Object MountPoint, VolumeStatus, EncryptionMethod\n"
                    "# Output: Protection Status: On, Encryption Method: XtsAes256\n\n"
                    "# Linux: Auditing LUKS (Linux Unified Key Setup) partition encryption:\n"
                    "sudo cryptsetup status /dev/mapper/cryptroot"
                ),
                "explanation": "Audits confirm that laptops leaving the building have full-disk encryption active, protecting lost or stolen hardware."
            },
            {
                "title": "Python: DLP Scanner Identifying Sensitive PII (Credit Cards)",
                "language": "python",
                "code": (
                    "import re\n\n"
                    "def dlp_scan_text(content: str) -> dict:\n"
                    "    # Regex for standard 16-digit credit card pattern\n"
                    "    cc_pattern = r'\\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\\b'\n"
                    "    matches = re.findall(cc_pattern, content)\n"
                    "    if matches:\n"
                    "        return {'dlp_alert': 'BLOCKED', 'reason': f'Exposed Credit Card detected ({len(matches)} matches)'}\n"
                    "    return {'dlp_alert': 'PERMITTED', 'reason': 'Clean'}\n\n"
                    "print(dlp_scan_text('Patient summary: All vitals normal.'))\n"
                    "print(dlp_scan_text('Client payment: Card 4111222233334444 approved.'))"
                ),
                "explanation": "DLP engines inspect network packets and clipboard buffers for sensitive regex patterns (credit cards, SSNs)."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_data_state(scenario: str) -> str` that maps 'LAPTOP_HARD_DRIVE' -> 'DATA_AT_REST', 'WIFI_TRANSMISSION' -> 'DATA_IN_TRANSIT', 'RAM_BUFFER' -> 'DATA_IN_USE', and 'S3_BUCKET' -> 'DATA_AT_REST'. Return 'UNKNOWN' for any other string.",
            "starter_code": (
                "def classify_data_state(scenario: str) -> str:\n"
                "    # Return 'DATA_AT_REST', 'DATA_IN_TRANSIT', 'DATA_IN_USE', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_data_state('LAPTOP_HARD_DRIVE'))\n"
                "print(classify_data_state('WIFI_TRANSMISSION'))\n"
                "print(classify_data_state('RAM_BUFFER'))"
            ),
            "solution_code": (
                "def classify_data_state(scenario: str) -> str:\n"
                "    mapping = {\n"
                "        'laptop_hard_drive': 'DATA_AT_REST',\n"
                "        's3_bucket': 'DATA_AT_REST',\n"
                "        'database_file': 'DATA_AT_REST',\n"
                "        'backup_tape': 'DATA_AT_REST',\n"
                "        'wifi_transmission': 'DATA_IN_TRANSIT',\n"
                "        'https_request': 'DATA_IN_TRANSIT',\n"
                "        'ethernet_cable': 'DATA_IN_TRANSIT',\n"
                "        'ram_buffer': 'DATA_IN_USE',\n"
                "        'cpu_register': 'DATA_IN_USE'\n"
                "    }\n"
                "    return mapping.get(scenario.lower(), 'UNKNOWN')\n\n"
                "print(classify_data_state('LAPTOP_HARD_DRIVE'))\n"
                "print(classify_data_state('WIFI_TRANSMISSION'))\n"
                "print(classify_data_state('RAM_BUFFER'))"
            ),
            "expected_output": "DATA_AT_REST\nDATA_IN_TRANSIT\nDATA_IN_USE"
        },
        quizzes=[
            {
                "question": "What is the primary security control used to protect 'Data at Rest' stored on employee laptops?",
                "options": [
                    "Full Disk Encryption (such as BitLocker, FileVault, or LUKS)",
                    "Using HTTPS web browsers",
                    "Screen brightness filters",
                    "Changing the desktop wallpaper"
                ],
                "correct_answer": "Full Disk Encryption (such as BitLocker, FileVault, or LUKS)",
                "explanation": "Full Disk Encryption (FDE) protects data at rest: if a laptop is lost or stolen, the hard drive cannot be read without the decryption key."
            },
            {
                "question": "Data moving across an Ethernet cable or public Wi-Fi network is classified as which state of data?",
                "options": ["Data in Transit (Data in Motion)", "Data at Rest", "Data in Use", "Data in Quarantine"],
                "correct_answer": "Data in Transit (Data in Motion)",
                "explanation": "Data traveling across any network connection is in transit, protected by transport encryption protocols like TLS and IPsec."
            },
            {
                "question": "Why is 'Data in Use' historically considered the most vulnerable state of data?",
                "options": [
                    "Data must be decrypted in system RAM and CPU registers for software to process it, leaving it exposed to RAM-scraping malware and memory dumps",
                    "RAM cannot store numbers",
                    "Data in use is automatically uploaded to Facebook",
                    "Processors delete data every 10 seconds"
                ],
                "correct_answer": "Data must be decrypted in system RAM and CPU registers for software to process it, leaving it exposed to RAM-scraping malware and memory dumps",
                "explanation": "CPUs must read cleartext data to compute. Attackers with root access can dump process memory to steal unencrypted credentials and keys."
            },
            {
                "question": "What is the purpose of Data Loss Prevention (DLP) systems?",
                "options": [
                    "To detect, monitor, and block unauthorized transfers or exfiltration of sensitive data (like credit cards or PII) across all data states",
                    "To defragment mechanical hard drives",
                    "To speed up database search queries",
                    "To download software updates faster"
                ],
                "correct_answer": "To detect, monitor, and block unauthorized transfers or exfiltration of sensitive data (like credit cards or PII) across all data states",
                "explanation": "DLP systems scan networks, endpoints, and storage for sensitive patterns (SSNs, medical records), blocking unauthorized leaks."
            },
            {
                "question": "What hardware technology provides cryptographic protection for Data in Use by isolating execution inside encrypted CPU memory enclaves?",
                "options": ["Confidential Computing (e.g., Intel SGX, AMD SEV)", "RAID 5 Disk Arrays", "Bluetooth Low Energy", "Dynamic DNS"],
                "correct_answer": "Confidential Computing (e.g., Intel SGX, AMD SEV)",
                "explanation": "Confidential computing encrypts memory in hardware enclaves so that even the hypervisor or host OS root administrator cannot read the data in use."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 45: Endpoint Protection (Antivirus, Anti-malware, EDR)
    # ---------------------------------------------------------
    DayBlueprint(
        order=45,
        title="Day 45: Endpoint Protection (Antivirus, Anti-malware, EDR)",
        concept="Tracing endpoint security evolution: Legacy signature Antivirus (AV), Next-Generation Antivirus (NGAV), Endpoint Detection and Response (EDR), and Extended Detection and Response (XDR).",
        analogy="Think of personal health defense: Legacy Antivirus is a vaccine catalog that only protects against last year's exact flu strains. Next-Gen Antivirus (NGAV) is an active immune system that detects unfamiliar infections based on high body fever and coughs. EDR (Endpoint Detection and Response) is a flight data black box flight recorder tracking every heart valve, with an onboard paramedic capable of instantly freezing the patient and pumping antitoxins into their bloodstream.",
        theory_sections=[
            {
                "heading": "The Evolution from Legacy AV to EDR",
                "content": (
                    "Endpoints (workstations, servers, mobile devices) are the primary entry targets for cyber attacks:\n\n"
                    "1. **Legacy Antivirus (AV)**: Relies on static file hashing and known virus signatures. Completely ineffective against modern fileless malware, script-based PowerShell attacks, and polymorphic malware.\n"
                    "2. **Next-Generation Antivirus (NGAV)**: Uses machine learning, behavioral heuristics, and script inspection (AMSI) to spot malicious actions (e.g., Excel spawning PowerShell).\n"
                    "3. **EDR (Endpoint Detection and Response - CrowdStrike, SentinelOne, Defender for Endpoint)**:\n"
                    "   - Continuously records process executions, registry edits, network sockets, and file modifications in real time.\n"
                    "   - Visualizes complete **Process Trees** (attack lineage).\n"
                    "   - Provides active remediation: remote shell, process killing, and **Network Host Isolation** (severing all network traffic except management to stop lateral spread).\n"
                    "4. **XDR (Extended Detection and Response)**: Correlates telemetry beyond endpoints, pulling in cloud, identity, email, and firewall logs."
                )
            },
            {
                "heading": "Network Host Isolation",
                "content": (
                    "When EDR detects active ransomware detonating on an endpoint, the SOC analyst clicks **Isolate Host**. The EDR agent immediately manipulates local kernel packet filters to drop all inbound and outbound network connections, stopping ransomware from spreading to network file shares while maintaining a secure telemetry channel to the management console."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Auditing Endpoint Antivirus & Threat Status via PowerShell",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Querying Defender real-time protection and definitions:\n"
                    "Get-MpComputerStatus | Select-Object AMServiceEnabled, AntispywareSignatureVersion, RealTimeProtectionEnabled\n\n"
                    "# Querying active detected threats on endpoint:\n"
                    "Get-MpThreatDetection | Select-Object ThreatName, InitialDetectionTime, Resources"
                ),
                "explanation": "Sysadmins verify endpoint agent health and query local infection alerts."
            },
            {
                "title": "Python: Simulating EDR Behavioral Process Tree Analysis",
                "language": "python",
                "code": (
                    "def edr_analyze_process_tree(parent_proc: str, child_proc: str, cmd_line: str) -> dict:\n"
                    "    # Detecting Living-off-the-Land (LotL) execution patterns\n"
                    "    suspicious_parents = {'winword.exe', 'excel.exe', 'powerpnt.exe', 'outlook.exe'}\n"
                    "    suspicious_children = {'powershell.exe', 'cmd.exe', 'wscript.exe', 'mshta.exe'}\n"
                    "    \n"
                    "    if parent_proc.lower() in suspicious_parents and child_proc.lower() in suspicious_children:\n"
                    "        return {\n"
                    "            'severity': 'CRITICAL',\n"
                    "            'action': 'KILL_PROCESS_AND_ISOLATE_HOST',\n"
                    "            'reason': f'Office document {parent_proc} spawned shell binary {child_proc}!'\n"
                    "        }\n"
                    "    return {'severity': 'INFO', 'action': 'ALLOW', 'reason': 'Standard process execution'}\n\n"
                    "print(edr_analyze_process_tree('excel.exe', 'powershell.exe', '-Enc BAB4...'))\n"
                    "print(edr_analyze_process_tree('explorer.exe', 'chrome.exe', ''))"
                ),
                "explanation": "EDR engines evaluate process parentage relationships to identify malicious code execution."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `edr_response_action(threat_severity: str) -> str` that maps 'CRITICAL' -> 'ISOLATE_HOST_AND_KILL', 'HIGH' -> 'KILL_PROCESS', 'MEDIUM' -> 'ALERT_SOC', and 'LOW' -> 'LOG_EVENT'. Return 'UNKNOWN' for any other string.",
            "starter_code": (
                "def edr_response_action(threat_severity: str) -> str:\n"
                "    # Return automated EDR response action string\n"
                "    return ''\n\n"
                "print(edr_response_action('CRITICAL'))\n"
                "print(edr_response_action('HIGH'))\n"
                "print(edr_response_action('LOW'))"
            ),
            "solution_code": (
                "def edr_response_action(threat_severity: str) -> str:\n"
                "    mapping = {\n"
                "        'critical': 'ISOLATE_HOST_AND_KILL',\n"
                "        'high': 'KILL_PROCESS',\n"
                "        'medium': 'ALERT_SOC',\n"
                "        'low': 'LOG_EVENT'\n"
                "    }\n"
                "    return mapping.get(threat_severity.lower(), 'UNKNOWN')\n\n"
                "print(edr_response_action('CRITICAL'))\n"
                "print(edr_response_action('HIGH'))\n"
                "print(edr_response_action('LOW'))"
            ),
            "expected_output": "ISOLATE_HOST_AND_KILL\nKILL_PROCESS\nLOG_EVENT"
        },
        quizzes=[
            {
                "question": "What is the primary limitation of traditional legacy Antivirus (AV) that led to the development of EDR (Endpoint Detection and Response)?",
                "options": [
                    "Legacy AV relies on known file signatures and cannot detect fileless memory attacks, living-off-the-land scripts, or novel zero-days",
                    "Legacy AV only works on desktop printers",
                    "Legacy AV uses too much paper",
                    "Legacy AV requires dial-up internet"
                ],
                "correct_answer": "Legacy AV relies on known file signatures and cannot detect fileless memory attacks, living-off-the-land scripts, or novel zero-days",
                "explanation": "Attackers bypass static signatures using fileless PowerShell scripts and in-memory execution; EDR monitors real-time behavioral telemetry."
            },
            {
                "question": "What does an EDR agent do during a 'Host Isolation' action?",
                "options": [
                    "It cuts all network communication to and from the infected endpoint, except for the secure management channel, preventing lateral spread of malware",
                    "It physically ejects the hard drive from the computer",
                    "It turns off the building's electrical power",
                    "It formats the operating system immediately"
                ],
                "correct_answer": "It cuts all network communication to and from the infected endpoint, except for the secure management channel, preventing lateral spread of malware",
                "explanation": "Host isolation quarantines the compromised computer from the rest of the company network while keeping the SOC connected for forensic investigation."
            },
            {
                "question": "What is a 'Process Tree' in EDR forensics?",
                "options": [
                    "A hierarchical visual mapping showing which parent process spawned child processes, revealing the exact lineage of an infection",
                    "A diagram of trees planted outside the office",
                    "A list of all CPU cooling fans",
                    "The operating system file directory folder list"
                ],
                "correct_answer": "A hierarchical visual mapping showing which parent process spawned child processes, revealing the exact lineage of an infection",
                "explanation": "Process trees allow analysts to trace attacks back to the initial infection vector (e.g., `outlook.exe` -> `word.exe` -> `powershell.exe`)."
            },
            {
                "question": "What is 'XDR' (Extended Detection and Response)?",
                "options": [
                    "A platform that unifies security telemetry across endpoints, cloud workloads, email, network firewalls, and identity providers for holistic threat correlation",
                    "An extra-large computer monitor",
                    "A faster version of Wi-Fi",
                    "An external USB hard drive"
                ],
                "correct_answer": "A platform that unifies security telemetry across endpoints, cloud workloads, email, network firewalls, and identity providers for holistic threat correlation",
                "explanation": "XDR expands beyond endpoint boundaries to correlate data from email gateways, cloud environments, and firewalls in one console."
            },
            {
                "question": "What is 'Living off the Land' (LotL) in cyber attacks?",
                "options": [
                    "Attackers utilizing legitimate, pre-installed administrative operating system tools (like PowerShell, WMI, Certutil) to conduct attacks without dropping executable files",
                    "Working remotely from a rural farm",
                    "Installing open-source solar panels on servers",
                    "Surviving in the forest without computers"
                ],
                "correct_answer": "Attackers utilizing legitimate, pre-installed administrative operating system tools (like PowerShell, WMI, Certutil) to conduct attacks without dropping executable files",
                "explanation": "LotL allows adversaries to evade signature antivirus by weaponizing built-in system administration utilities."
            }
        ]
    )
]
