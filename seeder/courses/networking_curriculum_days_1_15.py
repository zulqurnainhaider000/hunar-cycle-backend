"""
Computer Networking Basics 60-Day Curriculum - Part 1 (Days 1 to 15)
Module 1: Networking Fundamentals (Days 1-5)
Module 2: Network Architectures & Models (Days 6-8)
Module 3: IP Addressing & Subnetting (Days 9-14)
Module 4: Layer 2 - Switching Technologies (Day 15)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_15 = [
    # -------------------------------------------------------------
    # DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Introduction to Networks (LAN, WAN, MAN, PAN, CAN)",
        concept="Understanding network scale and geographic classification: Personal Area Networks, Local Area Networks, Campus Area Networks, Metropolitan Area Networks, and Wide Area Networks",
        analogy="Think of computer networks like different types of transportation systems. A PAN is your personal bicycle helmet and smartwatch talking via Bluetooth. A LAN is the internal hallway inside your house connecting rooms. A CAN is a university shuttle bus connecting faculties. A MAN is the municipal city metro connecting entire neighborhoods. A WAN is an international commercial airline fleet connecting continents across the entire globe!",
        theory_sections=[
            {
                "heading": "What is a Computer Network?",
                "body": "A computer network is an interconnected collection of autonomous computing devices (nodes) that exchange data and share resources via transmission media. Networks enable file transfer, remote application access, video conferencing, and resource sharing (such as network-attached printers and storage)."
            },
            {
                "heading": "Geographical Scale Classifications (PAN to WAN)",
                "body": "Networks are categorized primarily by physical scope: (1) **PAN (Personal Area Network)**: within 10 meters, typically Bluetooth/Zigbee; (2) **LAN (Local Area Network)**: high-speed connectivity within a single room, home, or office building; (3) **CAN (Campus Area Network)**: connects multiple LANs across a university or corporate park; (4) **MAN (Metropolitan Area Network)**: spans a town or city, often managed by telco fiber rings; (5) **WAN (Wide Area Network)**: spans countries and continents, typified by the public Internet."
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Local Network Interfaces on Linux / macOS",
                "language": "bash",
                "code": "# View all local network adapters, IP addresses, and MAC addresses\nip addr show\n\n# Or using standard tool\nifconfig",
                "explanation": "Displays active physical and virtual network interfaces, revealing whether the device is bound to a LAN or loopback adapter."
            },
            {
                "title": "Inspecting Network Adapters on Windows (PowerShell / CMD)",
                "language": "powershell",
                "code": "# Retrieve detailed IPv4, subnet mask, and default gateway info\nipconfig /all\n\n# Inspect specific adapter configuration\nGet-NetIPConfiguration",
                "explanation": "Windows commands displaying IP configuration, MAC hardware address, and active DHCP/DNS lease servers."
            },
            {
                "title": "Testing LAN vs WAN Reachability with Ping",
                "language": "bash",
                "code": "# Test local LAN gateway reachability (sub-millisecond latency)\nping -c 4 192.168.1.1\n\n# Test global WAN reachability to public DNS\nping -c 4 8.8.8.8",
                "explanation": "LAN roundtrip latency is typically under 1ms, whereas WAN roundtrip times vary from 15ms to 200ms across continents."
            },
            {
                "title": "Python Script: Classifying Network Type by Geographic Radius",
                "language": "python",
                "code": "def classify_network_by_radius(radius_meters: float) -> str:\n    if radius_meters <= 10:\n        return 'PAN (Personal Area Network)'\n    elif radius_meters <= 1000:\n        return 'LAN (Local Area Network)'\n    elif radius_meters <= 5000:\n        return 'CAN (Campus Area Network)'\n    elif radius_meters <= 50000:\n        return 'MAN (Metropolitan Area Network)'\n    else:\n        return 'WAN (Wide Area Network)'",
                "explanation": "Demonstrates algorithmic classification of computer networks based on physical geographic coverage."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Network Scale Classifier",
            description="Write a Python function `get_network_scope(acronym: str) -> str` that maps `'PAN'`, `'LAN'`, `'CAN'`, `'MAN'`, and `'WAN'` to their descriptive scope: `'Personal'`, `'Local'`, `'Campus'`, `'Metropolitan'`, and `'Wide Area'`. Return `'Unknown'` for unrecognized acronyms.",
            starter_code="def get_network_scope(acronym: str) -> str:\n    # Map acronym to scope description\n    pass",
            solution_code="def get_network_scope(acronym: str) -> str:\n    mapping = {\n        'PAN': 'Personal',\n        'LAN': 'Local',\n        'CAN': 'Campus',\n        'MAN': 'Metropolitan',\n        'WAN': 'Wide Area'\n    }\n    return mapping.get(acronym.strip().upper(), 'Unknown')",
            expected_output="get_network_scope('LAN') == 'Local', get_network_scope('WAN') == 'Wide Area'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What type of network connects smartwatches, wireless earbuds, and smartphones within a 10-meter range?",
                options=[
                    "PAN (Personal Area Network)",
                    "WAN (Wide Area Network)",
                    "MAN (Metropolitan Area Network)",
                    "CAN (Campus Area Network)"
                ],
                correct_answer="PAN (Personal Area Network)",
                explanation="PAN covers the personal space around an individual (typically under 10 meters) via Bluetooth or Zigbee."
            ),
            QuizQuestionBlueprint(
                question="What is the world's largest, most well-known example of a Wide Area Network (WAN)?",
                options=[
                    "The Global Internet",
                    "A home Wi-Fi router",
                    "A university computer lab",
                    "A Bluetooth car stereo connection"
                ],
                correct_answer="The Global Internet",
                explanation="The public Internet is the quintessential global WAN, connecting millions of private, public, and enterprise networks."
            ),
            QuizQuestionBlueprint(
                question="Which network category connects multiple distinct building LANs across a college campus or military base?",
                options=[
                    "CAN (Campus Area Network)",
                    "PAN (Personal Area Network)",
                    "SAN (Storage Area Network)",
                    "HAN (Home Area Network)"
                ],
                correct_answer="CAN (Campus Area Network)",
                explanation="CAN interconnects localized LANs across a defined geographic property, such as a university or hospital campus."
            ),
            QuizQuestionBlueprint(
                question="How does typical data transmission latency in a LAN compare to that of a WAN?",
                options=[
                    "LAN latency is much lower (often sub-millisecond) because physical cable distances are short and privately controlled",
                    "WAN latency is always 100x lower than LAN",
                    "LANs cannot transmit data faster than 1 bit per second",
                    "Latency is identical regardless of distance"
                ],
                correct_answer="LAN latency is much lower (often sub-millisecond) because physical cable distances are short and privately controlled",
                explanation="Local Area Networks experience minimal latency (<1ms) compared to WAN circuits traversing thousands of kilometers."
            ),
            QuizQuestionBlueprint(
                question="What CLI command on Windows displays the IP address, subnet mask, and default gateway of all network adapters?",
                options=[
                    "ipconfig",
                    "show_network",
                    "net_adapter_scan",
                    "get_my_internet"
                ],
                correct_answer="ipconfig",
                explanation="`ipconfig` (or `ipconfig /all`) is the standard Windows command for viewing TCP/IP adapter configurations."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Network Topologies (Star, Mesh, Bus, Ring, Tree)",
        concept="Architecting physical and logical layouts: Bus, Ring, Star, Extended Star, Mesh, and Hybrid topologies with redundancy trade-offs",
        analogy="Think of network topologies like floor plans for school classroom desks. In a **Bus topology**, all student desks are chained to a single long wire running down the center aisle (if the wire breaks, everyone loses connection). In a **Star topology**, every desk has a direct cord plugged into the teacher's central podium (if one student's cord snaps, only they are affected). In a **Full Mesh**, every student has a direct string connected to every single other classmate in the room!",
        theory_sections=[
            {
                "heading": "Physical vs Logical Topology",
                "body": "The **Physical Topology** describes how cables, nodes, and devices are physically arranged and wired in the real world. The **Logical Topology** describes the path data signals take through the physical layout. For example, a legacy coaxial hub physically resembles a Star, but logically behaves as a shared Bus where all packets collide."
            },
            {
                "heading": "Comparison of Standard Topologies",
                "body": "(1) **Star**: Central switch/hub connected to each device; dominant today due to ease of troubleshooting and fault isolation. (2) **Bus**: Single backbone cable with terminators at both ends; susceptible to single-point total failure. (3) **Ring**: Token-based ring; token travels unidirectionally. (4) **Full Mesh**: Every node connects to every other node with `N*(N-1)/2` links; supreme redundancy at high cabling cost. (5) **Partial Mesh**: Balance of redundancy and cost."
            }
        ],
        code_snippets=[
            {
                "title": "Calculating Physical Cable Links in a Full Mesh Topology (Python)",
                "language": "python",
                "code": "def calculate_mesh_links(num_nodes: int) -> int:\n    \"\"\"Formula: N * (N - 1) / 2\"\"\"\n    if num_nodes < 2:\n        return 0\n    return (num_nodes * (num_nodes - 1)) // 2\n\n# 10 routers in a full mesh require 45 individual point-to-point links!\nprint('Links for 10 routers:', calculate_mesh_links(10))",
                "explanation": "Calculates the exponential cabling overhead required by full mesh network designs."
            },
            {
                "title": "Simulating a Star Topology in Python NetworkX",
                "language": "python",
                "code": "import networkx as nx\n\n# Create a Star Graph with 1 central switch (node 0) and 4 host PCs\nstar_net = nx.star_graph(4)\nprint('Nodes:', star_net.nodes())\nprint('Edges connecting to central switch:', star_net.edges(0))",
                "explanation": "Models the central switch dependency in Star topologies using Python graph modeling."
            },
            {
                "title": "Inspecting Neighbor Links on Cisco Switch (CDP / LLDP)",
                "language": "text",
                "code": "Switch# show cdp neighbors\nCapability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n                  S - Switch, H - Host, I - IGMP, r - Repeater\n\nDevice ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\nRouter-Core      Gig 0/1           142        R S         ISR4331   Gig 0/0/0\nSwitch-Floor2    Gig 0/2           165        S           WS-C2960  Gig 0/1",
                "explanation": "Cisco Discovery Protocol (CDP) maps out physical star and tree topologies by discovering directly connected neighbors."
            },
            {
                "title": "Verifying Cable Fault Detection via Switch Port Status",
                "language": "text",
                "code": "Switch# show interfaces status\nPort      Name               Status       Vlan       Duplex  Speed Type\nFa0/1     Finance-PC1        connected    10         a-full  a-100 10/100BaseTX\nFa0/2     Finance-PC2        notconnect   10         auto    auto  10/100BaseTX\n# Port Fa0/2 indicates severed cable without impacting Fa0/1 (Star topology benefit!)",
                "explanation": "Star topologies isolate physical link failures to individual switch ports without interrupting the broader LAN."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Mesh Cable Link Calculator",
            description="Write a Python function `full_mesh_cable_count(nodes: int) -> int` that returns the exact number of physical cables needed for a full mesh topology with `nodes` devices using formula `n * (n - 1) // 2`. Return 0 if nodes < 2.",
            starter_code="def full_mesh_cable_count(nodes: int) -> int:\n    # Return required physical links\n    pass",
            solution_code="def full_mesh_cable_count(nodes: int) -> int:\n    if nodes < 2:\n        return 0\n    return (nodes * (nodes - 1)) // 2",
            expected_output="full_mesh_cable_count(5) == 10, full_mesh_cable_count(1) == 0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is the Star topology the most widely used physical topology in modern enterprise Ethernet LANs?",
                options=[
                    "A failure of a single device cable only disconnects that specific host, leaving the rest of the network operational",
                    "It requires no switches or cables",
                    "It works without any electrical power",
                    "It guarantees infinite internet bandwidth"
                ],
                correct_answer="A failure of a single device cable only disconnects that specific host, leaving the rest of the network operational",
                explanation="In a star topology, link breaks are isolated to individual peripheral drops without bringing down the LAN."
            ),
            QuizQuestionBlueprint(
                question="How many physical point-to-point links are required to connect 6 routers in a Full Mesh topology?",
                options=[
                    "15 links",
                    "6 links",
                    "30 links",
                    "36 links"
                ],
                correct_answer="15 links",
                explanation="Formula `N*(N-1)/2` = `6 * 5 / 2` = 15 physical links."
            ),
            QuizQuestionBlueprint(
                question="What critical component must be placed at both ends of a Bus topology trunk cable to prevent signal reflection?",
                options=[
                    "Terminators (Resistors)",
                    "Amplifiers",
                    "Batteries",
                    "Mirrors"
                ],
                correct_answer="Terminators (Resistors)",
                explanation="50-ohm terminating resistors absorb electrical signals at bus cable ends, preventing signal bounce/reflection."
            ),
            QuizQuestionBlueprint(
                question="What happens if the central switch in a Star topology experiences a complete hardware power outage?",
                options=[
                    "The entire network goes down because the central switch is a single point of failure for all connected nodes",
                    "The nodes automatically connect using satellite signals",
                    "Only host #1 loses connection",
                    "The cables turn into fiber optics"
                ],
                correct_answer="The entire network goes down because the central switch is a single point of failure for all connected nodes",
                explanation="The central device in a star topology is a single point of failure for the entire segment."
            ),
            QuizQuestionBlueprint(
                question="Which topology offers the highest fault tolerance and redundancy at the cost of maximum cabling expense?",
                options=[
                    "Full Mesh topology",
                    "Linear Bus topology",
                    "Token Ring topology",
                    "Daisy Chain topology"
                ],
                correct_answer="Full Mesh topology",
                explanation="Full mesh provides alternate routes between all node pairs, yielding fault tolerance."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Network Models (Client-Server vs Peer-to-Peer)",
        concept="Architectural paradigms of data communication: Centralized Client-Server architecture vs Decentralized Peer-to-Peer (P2P) systems",
        analogy="Think of communication models like shopping for bread. **Client-Server** is like walking into a commercial bakery store: the bakery (Server) bakes bread, manages the inventory, and serves 500 customers (Clients) walking through the front door. **Peer-to-Peer (P2P)** is like a neighborhood potluck picnic in a park: everyone brings a dish, everyone shares directly with each other, and there is no single store owner or central kitchen in charge!",
        theory_sections=[
            {
                "heading": "Client-Server Architecture: Centralized Control",
                "body": "In a **Client-Server** model, specialized computers (Servers) provide shared services, files, authentication, or web resources, while user devices (Clients) request and consume those services. Administration, security policies, and backups are centralized. If the server fails or becomes overloaded, clients cannot access the service unless redundant clusters exist."
            },
            {
                "heading": "Peer-to-Peer (P2P): Distributed Equal Nodes",
                "body": "In a **Peer-to-Peer (P2P)** network, there are no dedicated servers or hierarchical nodes. Every host (Peer) can act simultaneously as both a client (requesting data) and a server (sharing data). P2P is highly scalable and resilient against single points of failure (exemplified by BitTorrent, Bitcoin, and local ad-hoc file transfers), but decentralized administration and security are challenging."
            }
        ],
        code_snippets=[
            {
                "title": "Minimal Client-Server Architecture in Python (Server.py)",
                "language": "python",
                "code": "import socket\n\n# Server binds to port and listens for client connections\nserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nserver.bind(('0.0.0.0', 9000))\nserver.listen(5)\nprint('Server listening on port 9000...')\n\nwhile True:\n    client_sock, client_addr = server.accept()\n    print(f'Connection from {client_addr}')\n    client_sock.sendall(b'HTTP/1.1 200 OK\\r\\n\\r\\nHello from Centralized Server!')\n    client_sock.close()",
                "explanation": "Implements the server side of client-server communication, listening on a dedicated port."
            },
            {
                "title": "Minimal Client Connection in Python (Client.py)",
                "language": "python",
                "code": "import socket\n\n# Client connects to server to request data\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(('127.0.0.1', 9000))\nresponse = client.recv(1024)\nprint('Received from Server:', response.decode())\nclient.close()",
                "explanation": "Clients initiate outbound TCP handshakes to dedicated server addresses to consume resources."
            },
            {
                "title": "Inspecting Server Listening Ports with Netstat / SS",
                "language": "bash",
                "code": "# Show all active TCP server listening ports and process IDs\nss -tulnp\n\n# Or on Windows\nnetstat -ano | findstr LISTENING",
                "explanation": "Reveals whether a device is currently behaving as a server listening for inbound client sockets."
            },
            {
                "title": "Decentralized Peer Node Concept (Dual Client + Server Role)",
                "language": "python",
                "code": "class PeerNode:\n    def __init__(self, node_id, port):\n        self.node_id = node_id\n        self.port = port\n        self.shared_blocks = {}\n        \n    def serve_chunk(self, chunk_id):\n        \"\"\"Acting as a Server\"\"\"\n        return self.shared_blocks.get(chunk_id)\n        \n    def request_chunk(self, remote_peer, chunk_id):\n        \"\"\"Acting as a Client\"\"\"\n        return remote_peer.serve_chunk(chunk_id)",
                "explanation": "Demonstrates how P2P nodes transition interchangeably between serving and consuming data blocks."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Architecture Model Decision Engine",
            description="Write a Python function `recommend_network_model(requires_central_auth: bool, max_budget_usd: int) -> str` that returns `'Client-Server'` if centralized authentication is required, `'Peer-to-Peer'` if no central auth is needed and budget is under 500, and `'Hybrid'` otherwise.",
            starter_code="def recommend_network_model(requires_central_auth: bool, max_budget_usd: int) -> str:\n    # Recommend network architectural model\n    pass",
            solution_code="def recommend_network_model(requires_central_auth: bool, max_budget_usd: int) -> str:\n    if requires_central_auth:\n        return 'Client-Server'\n    elif max_budget_usd < 500:\n        return 'Peer-to-Peer'\n    return 'Hybrid'",
            expected_output="recommend_network_model(True, 1000) == 'Client-Server', recommend_network_model(False, 200) == 'Peer-to-Peer'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the defining characteristic of a Peer-to-Peer (P2P) network model?",
                options=[
                    "Each computer can act simultaneously as both a client and a server, with no central administrator required",
                    "There are no cables permitted",
                    "Only one computer can send data per day",
                    "It is strictly used for printing documents"
                ],
                correct_answer="Each computer can act simultaneously as both a client and a server, with no central administrator required",
                explanation="In P2P, peers share resources directly with equivalent privileges and capabilities."
            ),
            QuizQuestionBlueprint(
                question="What is a major advantage of the Client-Server model in enterprise corporate IT?",
                options=[
                    "Centralized administration, security access controls, and unified data backup management",
                    "It requires no software licenses",
                    "It completely eliminates the need for power supplies",
                    "It works without computer hardware"
                ],
                correct_answer="Centralized administration, security access controls, and unified data backup management",
                explanation="Client-server architectures provide centralized control over security policies, credentials, and backups."
            ),
            QuizQuestionBlueprint(
                question="Which protocol is an example of a decentralized Peer-to-Peer (P2P) architecture?",
                options=[
                    "BitTorrent",
                    "HTTP / Web browsing",
                    "Standard DNS resolution",
                    "Telnet"
                ],
                correct_answer="BitTorrent",
                explanation="BitTorrent is a distributed P2P file-sharing protocol where swarm peers exchange piece blocks directly."
            ),
            QuizQuestionBlueprint(
                question="What happens in a single-server Client-Server network if the central database server hardware crashes?",
                options=[
                    "All clients lose access to the central service until the server is repaired or restored from backup",
                    "Clients automatically convert their laptops into mainframe supercomputers",
                    "The client data is automatically printed on paper",
                    "The network switches to radio frequencies"
                ],
                correct_answer="All clients lose access to the central service until the server is repaired or restored from backup",
                explanation="Centralized servers present a single point of failure if high availability clustering is not configured."
            ),
            QuizQuestionBlueprint(
                question="What network CLI tool identifies whether a device is currently acting as a server listening on open TCP/UDP ports?",
                options=[
                    "netstat or ss",
                    "traceroute",
                    "ping",
                    "nslookup"
                ],
                correct_answer="netstat or ss",
                explanation="`netstat -ano` or `ss -tuln` inspects listening sockets to show services waiting for inbound client traffic."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Transmission Media (Copper UTP, Fiber Optic, Wireless RF)",
        concept="Physics and properties of physical layer media: Unshielded Twisted Pair (UTP Categories), Fiber Optic (Single-Mode vs Multi-Mode), and Radio Frequencies (RF)",
        analogy="Think of network cables like plumbing pipes carrying messages across a city. **Copper cables** are like copper water pipes carrying pulses of electricity (cheap and flexible, but susceptible to lightning and magnetic interference, limited to 100 meters). **Fiber Optic cables** are like microscopic glass laser pipes carrying pulses of pure light (immune to lightning and electro-magnetic noise, spanning 40 kilometers across ocean beds!). **Wireless** is shouting through the airwaves with a megaphone!",
        theory_sections=[
            {
                "heading": "Copper Cabling: UTP vs STP",
                "body": "Twisted-pair copper cables cancel electromagnetic interference (EMI) and crosstalk through wire twisting. **UTP (Unshielded Twisted Pair)** is standard indoors. Modern categories: Cat5e (1 Gbps up to 100m), Cat6 (10 Gbps up to 55m), Cat6a (10 Gbps up to 100m). **The maximum certified distance for horizontal Ethernet copper cabling is strictly 100 meters** (90m solid + 10m patch)."
            },
            {
                "heading": "Fiber Optics: Single-Mode (SMF) vs Multi-Mode (MMF)",
                "body": "Fiber optic cables transmit pulses of photons through silica glass cores with total internal reflection, providing complete immunity to EMI. **Single-Mode Fiber (SMF)** uses a tiny 9-micron core with lasers, transmitting light in a straight single ray over 10 to 40+ kilometers (WAN backbones). **Multi-Mode Fiber (MMF)** uses a larger 50-micron core with LEDs/VCSELs, bouncing multiple light angles over shorter campus distances up to 550 meters."
            }
        ],
        code_snippets=[
            {
                "title": "Summary Matrix: Ethernet Cable Categories & Specifications",
                "language": "text",
                "code": "Category    Max Bandwidth    Max Speed         Max Distance    Use Case\nCat5e       100 MHz          1 Gbps (1000BaseT)  100 meters      Standard Home/Office\nCat6        250 MHz          10 Gbps (10GBaseT)  55 meters       Gigabit LANs / Small Server\nCat6a       500 MHz          10 Gbps (10GBaseT)  100 meters      Modern Enterprise Backbones\nCat8        2000 MHz         40 Gbps (40GBaseT)  30 meters       Data Center Switch-to-Server",
                "explanation": "Reference specifications showing frequency, bandwidth throughput, and physical distance limitations."
            },
            {
                "title": "Inspecting Physical Link Speed and Duplex in Linux",
                "language": "bash",
                "code": "# Using ethtool to inspect physical copper/fiber transceivers\nethtool eth0\n# Outputs:\n# Speed: 1000Mb/s\n# Duplex: Full\n# Auto-negotiation: on\n# Link detected: yes",
                "explanation": "ethtool queries the physical network interface controller (NIC) to verify media link speed and duplex status."
            },
            {
                "title": "Cisco Switch Optical Transceiver Diagnostics (DOM)",
                "language": "text",
                "code": "Switch# show interfaces transceiver detail\nOptical Transceiver Diagnostics for TenGigabitEthernet1/0/1:\nTransceiver Type  : 10Gbase-LR (Single-Mode Fiber)\nTx Power          : -2.4 dBm (Normal laser output)\nRx Power          : -5.1 dBm (Strong optical light received)\nTemperature       : 31.4 C",
                "explanation": "Digital Optical Monitoring (DOM) measures laser light transmission levels in fiber optic SFP transceivers."
            },
            {
                "title": "Python Cable Distance & Attenuation Safety Checker",
                "language": "python",
                "code": "def check_copper_distance(distance_meters: float, cable_cat: str) -> bool:\n    if distance_meters > 100:\n        return False # Violates 100-meter IEEE 802.3 standard!\n    if cable_cat.upper() == 'CAT6' and distance_meters > 55:\n        print('Warning: Cat6 falls back from 10G to 1G between 55m and 100m')\n    return True",
                "explanation": "Enforces 100-meter physical layer distance constraints for Ethernet twisted-pair cabling."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Fiber Optic Transceiver Selector",
            description="Write a Python function `select_fiber_type(distance_km: float) -> str` that returns `'Multi-Mode (MMF)'` for distances <= 0.5 km (500m), and `'Single-Mode (SMF)'` for distances > 0.5 km up to 40 km. Return `'Exceeds Standard Reach'` for distances > 40 km.",
            starter_code="def select_fiber_type(distance_km: float) -> str:\n    # Select appropriate fiber type\n    pass",
            solution_code="def select_fiber_type(distance_km: float) -> str:\n    if distance_km <= 0.5:\n        return 'Multi-Mode (MMF)'\n    elif distance_km <= 40.0:\n        return 'Single-Mode (SMF)'\n    return 'Exceeds Standard Reach'",
            expected_output="select_fiber_type(0.3) == 'Multi-Mode (MMF)', select_fiber_type(15.0) == 'Single-Mode (SMF)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the maximum certified physical run distance for standard Ethernet twisted-pair copper cable (Cat5e/Cat6/Cat6a)?",
                options=[
                    "100 meters (approx. 328 feet)",
                    "1,000 meters",
                    "50 meters",
                    "500 meters"
                ],
                correct_answer="100 meters (approx. 328 feet)",
                explanation="The TIA/EIA and IEEE standards define a strict 100-meter limit for twisted-pair copper runs."
            ),
            QuizQuestionBlueprint(
                question="Why is Fiber Optic cabling immune to Electromagnetic Interference (EMI) and Radio Frequency Interference (RFI)?",
                options=[
                    "Because it transmits data as pulses of light (photons) through glass rather than electrical currents through metal",
                    "Because the cable is made of rubber",
                    "Because it is coated in gold",
                    "Because it only works underwater"
                ],
                correct_answer="Because it transmits data as pulses of light (photons) through glass rather than electrical currents through metal",
                explanation="Light signals traveling through non-conductive glass cores are entirely impervious to magnetic or electrical fields."
            ),
            QuizQuestionBlueprint(
                question="What is the primary difference between Single-Mode Fiber (SMF) and Multi-Mode Fiber (MMF)?",
                options=[
                    "SMF has a tiny core (9 microns) using lasers for long distances (10-40km); MMF has a larger core (50-62.5 microns) using LEDs for shorter building runs",
                    "SMF only transmits text; MMF only transmits pictures",
                    "MMF is made of copper wire",
                    "SMF requires no power"
                ],
                correct_answer="SMF has a tiny core (9 microns) using lasers for long distances (10-40km); MMF has a larger core (50-62.5 microns) using LEDs for shorter building runs",
                explanation="Single-mode has a tiny core allowing only one light path for long hauls; multi-mode allows multiple dispersion paths."
            ),
            QuizQuestionBlueprint(
                question="Why are the internal wire pairs in a UTP cable twisted together at varying twist rates?",
                options=[
                    "To cancel out Electromagnetic Interference (EMI) and reduce crosstalk between adjacent pairs",
                    "To make the cable look thicker",
                    "To prevent users from cutting the cable",
                    "To generate extra electricity"
                ],
                correct_answer="To cancel out Electromagnetic Interference (EMI) and reduce crosstalk between adjacent pairs",
                explanation="Twisting equalizes external magnetic interference on both wires so receiver circuits cancel out the noise."
            ),
            QuizQuestionBlueprint(
                question="What registered jack connector is universally used terminated at the ends of RJ-45 copper patch cables?",
                options=[
                    "RJ-45 (8P8C)",
                    "RJ-11 (Phone)",
                    "USB Type-C",
                    "HDMI 2.1"
                ],
                correct_answer="RJ-45 (8P8C)",
                explanation="RJ-45 (8 positions, 8 contacts) is the ubiquitous connector for Category twisted-pair Ethernet cables."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Basic Network Devices (Hub, Switch, Router, Modem, AP)",
        concept="Understanding the roles, operating layers, and broadcast/collision boundaries of Hubs, Switches, Routers, Modems, and Access Points",
        analogy="Think of network devices like postal sorting workers. A **Hub** is a megaphone: when someone speaks, it screams the message to every room in the building. A **Switch** is an intelligent mailroom sorter inside an office: it looks at the name on the envelope (MAC address) and drops it into that exact desk box. A **Router** is the international airport sorting facility: it inspects country codes (IP addresses) and routes planes across cities. A **Modem** is the translator converting electrical light pulses into phone wires!",
        theory_sections=[
            {
                "heading": "Hub vs Switch: Collision Domains",
                "body": "A legacy **Hub** operates at Layer 1 (Physical). It possesses zero intelligence: bits received on one port are blindly repeated out all other ports, creating a single shared **Collision Domain** where only one device can transmit at a time. A **Switch** operates at Layer 2 (Data Link). It learns MAC addresses and creates micro-segmented, dedicated point-to-point connections, giving **each switch port its own separate collision domain** in full duplex."
            },
            {
                "heading": "Router vs Switch: Broadcast Domains",
                "body": "Switches forward broadcast frames (`FF:FF:FF:FF:FF:FF`) out all ports within a LAN. A **Router** operates at Layer 3 (Network), making forwarding decisions based on logical IP addresses. Crucially, **Routers do NOT forward Layer 2 broadcast packets by default**, thereby creating separate **Broadcast Domains** that contain broadcast traffic within distinct subnets."
            }
        ],
        code_snippets=[
            {
                "title": "Summary Comparison: Network Devices, OSI Layers & Domains",
                "language": "text",
                "code": "Device          OSI Layer     Addressing Used   Collision Domains     Broadcast Domains\nHub             Layer 1       None (Raw Bits)   1 (Shared across all) 1 (Shared)\nBridge          Layer 2       MAC Address       1 per port            1 (Shared)\nSwitch          Layer 2       MAC Address       1 per port (Dedicated) 1 (Per VLAN)\nRouter          Layer 3       IP Address        1 per interface       1 per interface (Breaks BC domains)\nWireless AP     Layer 2       MAC Address       1 (Shared RF medium)  1 (Shared)",
                "explanation": "Essential architectural comparison detailing OSI operational layer and domain boundaries."
            },
            {
                "title": "Viewing the MAC Address Table on a Managed Cisco Switch",
                "language": "text",
                "code": "Switch# show mac address-table\n          Mac Address Table\n-------------------------------------------\nVlan    Mac Address       Type        Ports\n----    -----------       --------    -----\n   1    0050.7966.6801    DYNAMIC     Fa0/1\n   1    0050.7966.6802    DYNAMIC     Fa0/2\n# Switch intelligently forwards frames destined to 0050.7966.6801 ONLY out port Fa0/1!",
                "explanation": "Switches use MAC address forwarding tables to deliver frames only to the designated recipient port."
            },
            {
                "title": "Viewing the IP Routing Table on a Cisco Router",
                "language": "text",
                "code": "Router# show ip route\nGateway of last resort is 198.51.100.1 to network 0.0.0.0\n\nC    192.168.1.0/24 is directly connected, GigabitEthernet0/0\nC    10.0.0.0/8 is directly connected, GigabitEthernet0/1\nS*   0.0.0.0/0 [1/0] via 198.51.100.1\n# Router determines path across subnets using IP destination routes",
                "explanation": "Routers use Layer 3 routing tables to forward packets between different IP subnets."
            },
            {
                "title": "Python Device Operational Layer Classifier",
                "language": "python",
                "code": "def get_device_layer(device_name: str) -> int:\n    device = device_name.lower().strip()\n    if 'hub' in device or 'repeater' in device:\n        return 1\n    elif 'switch' in device or 'bridge' in device or 'access point' in device:\n        return 2\n    elif 'router' in device or 'layer 3 switch' in device:\n        return 3\n    return 0",
                "explanation": "Demonstrates mapping of core network hardware devices to their respective OSI operational layers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Collision and Broadcast Domain Counter",
            description="Write a Python function `count_domains(num_switch_ports: int, num_router_interfaces: int) -> dict[str, int]` that returns a dictionary `{'collision_domains': int, 'broadcast_domains': int}`. Each switch port is 1 collision domain; each router interface is 1 broadcast domain and 1 collision domain.",
            starter_code="def count_domains(num_switch_ports: int, num_router_interfaces: int) -> dict[str, int]:\n    # Return {'collision_domains': ..., 'broadcast_domains': ...}\n    pass",
            solution_code="def count_domains(num_switch_ports: int, num_router_interfaces: int) -> dict[str, int]:\n    return {\n        'collision_domains': max(0, num_switch_ports) + max(0, num_router_interfaces),\n        'broadcast_domains': max(0, num_router_interfaces)\n    }",
            expected_output="count_domains(24, 2) == {'collision_domains': 26, 'broadcast_domains': 2}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="At which layer of the OSI model does a standard network Switch operate?",
                options=[
                    "Layer 2 (Data Link Layer)",
                    "Layer 1 (Physical Layer)",
                    "Layer 3 (Network Layer)",
                    "Layer 7 (Application Layer)"
                ],
                correct_answer="Layer 2 (Data Link Layer)",
                explanation="Standard switches make forwarding decisions based on Layer 2 MAC addresses."
            ),
            QuizQuestionBlueprint(
                question="Why is an Ethernet Switch vastly superior to a legacy Ethernet Hub?",
                options=[
                    "A switch gives each port its own dedicated collision domain by inspecting MAC addresses, preventing packet collisions",
                    "A hub is more expensive and requires optical fiber",
                    "A switch only works on wireless signals",
                    "A hub encrypts all passwords"
                ],
                correct_answer="A switch gives each port its own dedicated collision domain by inspecting MAC addresses, preventing packet collisions",
                explanation="Switches isolate collision domains per port; hubs broadcast all electrical signals to every port simultaneously."
            ),
            QuizQuestionBlueprint(
                question="What device is required to interconnect different IP subnets and route packets across diverse networks?",
                options=[
                    "Router",
                    "Hub",
                    "Modem only",
                    "Unmanaged Layer 2 Switch"
                ],
                correct_answer="Router",
                explanation="Routers operate at Layer 3 to route packets across separate IP subnets and broadcast domains."
            ),
            QuizQuestionBlueprint(
                question="Do Routers forward Layer 2 broadcast frames (`FF:FF:FF:FF:FF:FF`) across interfaces by default?",
                options=[
                    "No, routers break broadcast domains and do not forward Layer 2 broadcasts by default",
                    "Yes, routers repeat broadcasts to the entire global internet",
                    "Only on Monday mornings",
                    "Only if the cable is under 10 meters"
                ],
                correct_answer="No, routers break broadcast domains and do not forward Layer 2 broadcasts by default",
                explanation="Routers terminate and boundary Layer 2 broadcast domains, containing local broadcasts within the subnet."
            ),
            QuizQuestionBlueprint(
                question="What is the primary role of a Modem (Modulator-Demodulator)?",
                options=[
                    "To convert digital signals from a computer into analog signals suitable for telephone/cable lines, and vice versa",
                    "To assign IP addresses to printers",
                    "To boost computer monitor brightness",
                    "To store user passwords"
                ],
                correct_answer="To convert digital signals from a computer into analog signals suitable for telephone/cable lines, and vice versa",
                explanation="Modems modulate digital data into analog carrier waves for transmission over telco media and demodulate upon reception."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 6
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: The OSI Reference Model (All 7 Layers in Depth)",
        concept="Mastering the 7-layer Open Systems Interconnection model: Physical, Data Link, Network, Transport, Session, Presentation, and Application",
        analogy="Think of the OSI model like sending an expensive porcelain vase to a customer overseas. **Application (Layer 7)**: You decide to sell the vase. **Presentation (6)**: You pack it with bubble wrap and translate the receipt into German. **Session (5)**: You agree on the shipping appointment window. **Transport (4)**: You attach tracking and insurance numbers (guaranteed delivery). **Network (3)**: The delivery company writes the postal address. **Data Link (2)**: A local mail truck takes it to the sorting facility. **Physical (1)**: The asphalt road and truck tires carrying the package!",
        theory_sections=[
            {
                "heading": "The 7 Layers from Top to Bottom (APSTNDP)",
                "body": "Developed by the ISO, the OSI model provides a vendor-neutral conceptual framework: (7) **Application**: user interaction, HTTP, DNS, SSH; (6) **Presentation**: data formatting, encryption (TLS), compression; (5) **Session**: session establishment, checkpoints, dialogues; (4) **Transport**: end-to-end delivery, ports, TCP/UDP; (3) **Network**: logical IP addressing, routing paths; (2) **Data Link**: physical MAC addressing, framing, switches; (1) **Physical**: raw bit transmission over copper, fiber, or air."
            },
            {
                "heading": "Mnemonic Aid & Layer Protocol Data Units (PDUs)",
                "body": "A popular mnemonic from top to bottom is: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (Application, Presentation, Session, Transport, Network, Data Link, Physical). Conversely, bottom-up is: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way."
            }
        ],
        code_snippets=[
            {
                "title": "Complete OSI 7-Layer Architecture Reference Chart",
                "language": "text",
                "code": "Layer #   Name           PDU Name     Key Protocols / Standards           Hardware\n7         Application    Data         HTTP, HTTPS, DNS, DHCP, SSH, FTP   Gateways, Firewalls\n6         Presentation   Data         TLS/SSL, JPEG, ASCII, JSON, gzip    OS / App Runtime\n5         Session        Data         RPC, NetBIOS, Sockets               OS APIs\n4         Transport      Segment      TCP, UDP                            Load Balancers\n3         Network        Packet       IPv4, IPv6, ICMP, OSPF, BGP         Routers, L3 Switches\n2         Data Link      Frame        Ethernet 802.3, Wi-Fi 802.11, ARP   Switches, Bridges\n1         Physical       Bit          Voltage, Photons, RJ-45, Cat6       Hubs, Cables, NICs",
                "explanation": "Reference chart summarizing layer number, official PDU designation, protocols, and hardware."
            },
            {
                "title": "Inspecting Layer 4 & Layer 7 Data with cURL & Verbose Flag",
                "language": "bash",
                "code": "# Connects to Web Server showing Layer 4 TCP handshake and Layer 7 HTTP headers\ncurl -v https://api.github.com\n# * Connected to api.github.com (140.82.113.6) port 443 (Layer 3 & 4)\n# * TLS 1.3 connection established (Layer 6 Presentation Encryption)\n# > GET / HTTP/2 (Layer 7 Application Request)",
                "explanation": "cURL verbose trace demonstrates how lower layers connect before upper application data exchanges."
            },
            {
                "title": "Capturing Layer 2, 3, and 4 Headers with Tshark / Wireshark",
                "language": "bash",
                "code": "# Capture 1 packet and display OSI headers layer-by-layer\ntshark -c 1 -V -i any\n# Frame 1: 74 bytes on wire (Layer 1 & 2)\n# Ethernet II, Src: 00:0c:29:4f:8e:1a, Dst: 00:50:56:e8:11:02 (Layer 2 Data Link)\n# Internet Protocol Version 4, Src: 192.168.1.50, Dst: 8.8.8.8 (Layer 3 Network)\n# Transmission Control Protocol, Src Port: 54321, Dst Port: 443 (Layer 4 Transport)",
                "explanation": "Wireshark packet dissections visually demonstrate the layered protocol headers stacked inside network frames."
            },
            {
                "title": "Python OSI Layer Lookup Function",
                "language": "python",
                "code": "OSI_LAYERS = {\n    1: ('Physical', 'Bits'),\n    2: ('Data Link', 'Frames'),\n    3: ('Network', 'Packets'),\n    4: ('Transport', 'Segments'),\n    5: ('Session', 'Data'),\n    6: ('Presentation', 'Data'),\n    7: ('Application', 'Data')\n}\n\ndef get_layer_pdu(layer_num: int) -> str:\n    return OSI_LAYERS.get(layer_num, ('Unknown', 'Unknown'))[1]",
                "explanation": "Demonstrates mapping of layer numbers to their formal Protocol Data Unit (PDU) nomenclature."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="OSI Layer Protocol Matcher",
            description="Write a Python function `get_osi_layer_for_protocol(protocol: str) -> int` that maps `'HTTP'`, `'TCP'`, `'IP'`, and `'ETHERNET'` to their respective OSI layer numbers (7, 4, 3, 2). Return 0 for unknown protocols.",
            starter_code="def get_osi_layer_for_protocol(protocol: str) -> int:\n    # Map protocol to OSI layer number\n    pass",
            solution_code="def get_osi_layer_for_protocol(protocol: str) -> int:\n    mapping = {\n        'HTTP': 7,\n        'HTTPS': 7,\n        'DNS': 7,\n        'TCP': 4,\n        'UDP': 4,\n        'IP': 3,\n        'IPV4': 3,\n        'IPV6': 3,\n        'ETHERNET': 2,\n        'ARP': 2\n    }\n    return mapping.get(protocol.strip().upper(), 0)",
            expected_output="get_osi_layer_for_protocol('TCP') == 4, get_osi_layer_for_protocol('IP') == 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which layer of the OSI model is responsible for logical IP addressing and end-to-end packet routing across networks?",
                options=[
                    "Layer 3 (Network Layer)",
                    "Layer 2 (Data Link Layer)",
                    "Layer 4 (Transport Layer)",
                    "Layer 1 (Physical Layer)"
                ],
                correct_answer="Layer 3 (Network Layer)",
                explanation="Layer 3 handles logical addressing (IPv4/IPv6) and path determination (routing)."
            ),
            QuizQuestionBlueprint(
                question="What is the formal Protocol Data Unit (PDU) name at Layer 4 (Transport Layer)?",
                options=[
                    "Segment (or Datagram for UDP)",
                    "Packet",
                    "Frame",
                    "Bit"
                ],
                correct_answer="Segment (or Datagram for UDP)",
                explanation="Transport Layer PDUs are termed Segments (in TCP) or Datagrams (in UDP)."
            ),
            QuizQuestionBlueprint(
                question="Which layer of the OSI model handles data formatting, compression, and TLS/SSL encryption?",
                options=[
                    "Layer 6 (Presentation Layer)",
                    "Layer 7 (Application Layer)",
                    "Layer 5 (Session Layer)",
                    "Layer 3 (Network Layer)"
                ],
                correct_answer="Layer 6 (Presentation Layer)",
                explanation="The Presentation layer translates syntax, formats data (JPEG, JSON, ASCII), and manages encryption/decryption."
            ),
            QuizQuestionBlueprint(
                question="What is the PDU name used at Layer 2 (Data Link Layer)?",
                options=[
                    "Frame",
                    "Packet",
                    "Segment",
                    "Bit"
                ],
                correct_answer="Frame",
                explanation="Layer 2 bundles bits into Frames containing source and destination MAC hardware addresses."
            ),
            QuizQuestionBlueprint(
                question="At which layer of the OSI model do end-user protocols like HTTP, DNS, SSH, and SMTP operate?",
                options=[
                    "Layer 7 (Application Layer)",
                    "Layer 4 (Transport Layer)",
                    "Layer 1 (Physical Layer)",
                    "Layer 5 (Session Layer)"
                ],
                correct_answer="Layer 7 (Application Layer)",
                explanation="Layer 7 provides services directly to user-facing applications (web browsers, email clients, SSH terminals)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: The TCP/IP Model (DoD 4-Layer Architecture)",
        concept="Contrasting practical implementation against theoretical models: The 4-Layer TCP/IP protocol suite vs 7-Layer OSI",
        analogy="Think of the OSI model like an idealized 7-step recipe in a Michelin-star culinary book with separate steps for washing hands, drying hands, selecting plates, and aligning silverware. The **TCP/IP Model** is how the bustling restaurant kitchen actually cooks food in 4 practical steps: Network Access, Internet, Transport, and Application! It was forged in battle by DARPA and became the living language of the global Internet.",
        theory_sections=[
            {
                "heading": "The 4-Layer DoD Architecture",
                "body": "Created by the US Department of Defense (DoD), the TCP/IP stack condensed the 7 OSI layers into 4 practical functional layers: (4) **Application** (combines OSI Application, Presentation, and Session); (3) **Transport** (corresponds directly to OSI Transport, managing TCP/UDP); (2) **Internet** (corresponds to OSI Network, managing IP, ICMP, ARP); (1) **Network Access** (or Link layer, combining OSI Data Link and Physical)."
            },
            {
                "heading": "Why TCP/IP Won the Protocol Wars",
                "body": "While OSI was developed by international committees as a theoretical reference model, TCP/IP was implemented in functional UNIX code (BSD sockets) and deployed across ARPANET. The pragmatism, open RFC documentation, and resilience of TCP/IP made it the universal foundation of modern computer networking."
            }
        ],
        code_snippets=[
            {
                "title": "OSI 7-Layer vs TCP/IP 4-Layer Direct Mapping",
                "language": "text",
                "code": "OSI 7-Layer Model           TCP/IP 4-Layer Suite        Key Protocol Examples\n7. Application   ─┐\n6. Presentation  ─┼──────────> 4. Application           HTTP, HTTPS, DNS, SSH, FTP\n5. Session       ─┘\n4. Transport     ────────────> 3. Transport             TCP, UDP\n3. Network       ────────────> 2. Internet              IPv4, IPv6, ICMP, ARP\n2. Data Link     ─┐\n1. Physical      ─┴──────────> 1. Network Access (Link) Ethernet (802.3), Wi-Fi (802.11)",
                "explanation": "Visual comparison illustrating how the 7 OSI layers collapse into the 4 practical TCP/IP layers."
            },
            {
                "title": "Verifying TCP/IP Stack Protocols in Linux /etc/protocols",
                "language": "bash",
                "code": "# Inspect official protocol numbers registered in the Internet layer\ncat /etc/protocols | grep -E \"(tcp|udp|icmp)\"\n# icmp    1    ICMP    # internet control message protocol\n# tcp     6    TCP     # transmission control protocol\n# udp     17   UDP     # user datagram protocol",
                "explanation": "Shows the standard protocol numbers embedded in IP packet headers at the Internet layer."
            },
            {
                "title": "Verifying TCP/IP Application Services in /etc/services",
                "language": "bash",
                "code": "# Inspect standard Application layer port numbers\ncat /etc/services | grep -E \"^(http|ssh|domain|https)\\s\"\n# ssh        22/tcp\n# domain     53/tcp\n# http       80/tcp\n# https      443/tcp",
                "explanation": "Maps Application-layer protocol names to their designated Transport-layer TCP/UDP port bindings."
            },
            {
                "title": "Python TCP/IP Layer Classifier",
                "language": "python",
                "code": "TCPIP_LAYERS = {\n    4: 'Application Layer',\n    3: 'Transport Layer',\n    2: 'Internet Layer',\n    1: 'Network Access Layer'\n}\n\ndef get_tcpip_layer_name(layer: int) -> str:\n    return TCPIP_LAYERS.get(layer, 'Invalid Layer Number')",
                "explanation": "Encapsulates the 4-layer DoD network model classification into clean programmatic definitions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="TCP/IP Layer Mapper",
            description="Write a Python function `map_osi_to_tcpip(osi_layer: int) -> int` that maps an OSI layer number (1 to 7) to its corresponding TCP/IP layer number (1 to 4). Return 0 for invalid inputs.",
            starter_code="def map_osi_to_tcpip(osi_layer: int) -> int:\n    # Map OSI layer number (1-7) to TCP/IP layer (1-4)\n    pass",
            solution_code="def map_osi_to_tcpip(osi_layer: int) -> int:\n    if osi_layer in [5, 6, 7]:\n        return 4  # Application\n    elif osi_layer == 4:\n        return 3  # Transport\n    elif osi_layer == 3:\n        return 2  # Internet\n    elif osi_layer in [1, 2]:\n        return 1  # Network Access\n    return 0",
            expected_output="map_osi_to_tcpip(7) == 4, map_osi_to_tcpip(3) == 2, map_osi_to_tcpip(1) == 1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How many layers are defined in the standard TCP/IP (DoD) network architecture model?",
                options=[
                    "4 layers",
                    "7 layers",
                    "5 layers",
                    "3 layers"
                ],
                correct_answer="4 layers",
                explanation="The classic TCP/IP model has 4 layers: Network Access, Internet, Transport, and Application."
            ),
            QuizQuestionBlueprint(
                question="Which three OSI layers are combined into the single 'Application Layer' in the TCP/IP model?",
                options=[
                    "Application, Presentation, and Session layers",
                    "Transport, Network, and Data Link layers",
                    "Physical, Data Link, and Network layers",
                    "Application, Transport, and Internet layers"
                ],
                correct_answer="Application, Presentation, and Session layers",
                explanation="TCP/IP merges OSI layers 5, 6, and 7 into a single unified Application layer."
            ),
            QuizQuestionBlueprint(
                question="What is the equivalent layer in the TCP/IP model to the OSI 'Network Layer'?",
                options=[
                    "Internet Layer",
                    "Transport Layer",
                    "Network Access Layer",
                    "Link Layer"
                ],
                correct_answer="Internet Layer",
                explanation="The Internet Layer (housing IP, ICMP, and ARP) corresponds directly to the OSI Network Layer."
            ),
            QuizQuestionBlueprint(
                question="What are the two primary Transport Layer protocols used in the TCP/IP suite?",
                options=[
                    "TCP and UDP",
                    "HTTP and DNS",
                    "IP and ICMP",
                    "Ethernet and Wi-Fi"
                ],
                correct_answer="TCP and UDP",
                explanation="TCP (connection-oriented) and UDP (connectionless) are the core Transport layer workhorses."
            ),
            QuizQuestionBlueprint(
                question="Which organization originally funded and guided the development of the TCP/IP protocol suite?",
                options=[
                    "DARPA (U.S. Department of Defense)",
                    "Microsoft",
                    "Apple",
                    "United Nations"
                ],
                correct_answer="DARPA (U.S. Department of Defense)",
                explanation="DARPA developed TCP/IP for ARPANET to create a fault-tolerant military communication network."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 8
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Data Encapsulation & Decapsulation (PDU Life Cycle)",
        concept="Tracing packets from keyboard to wire: Headers, Trailers, PDU transitions (Data -> Segment -> Packet -> Frame -> Bits), and MTU",
        analogy="Think of Data Encapsulation like nesting Russian Matryoshka dolls or preparing an official letter for courier shipping. You write a letter (**Data**). You stuff it into a numbered envelope with port numbers (**Segment**). You stuff that into a cardboard shipping box with recipient city and country IP addresses (**Packet**). You put the box into a steel delivery van with local tire barcodes and a padlock checksum (**Frame**). The van drives along the physical road (**Bits**). When received, the process is reversed (**Decapsulation**)!",
        theory_sections=[
            {
                "heading": "The Encapsulation Process (Top-Down)",
                "body": "When a computer sends data, it travels down the protocol stack: (1) Application generates raw user payload (Data); (2) Transport layer prepends a TCP/UDP header containing source and destination port numbers (creating a **Segment**); (3) Network layer prepends an IP header containing source and destination IP addresses (creating a **Packet**); (4) Data Link layer wraps the packet with a MAC header and an FCS checksum trailer (creating a **Frame**); (5) Physical layer converts the frame into electrical pulses or light rays (**Bits**)."
            },
            {
                "heading": "Decapsulation & Maximum Transmission Unit (MTU)",
                "body": "Upon receiving bits, the destination machine reverses this process (**Decapsulation**), stripping headers layer by layer after verifying checksum integrity. Standard Ethernet has a **Maximum Transmission Unit (MTU)** of 1500 bytes. Payloads exceeding MTU must be fragmented into multiple IP packets."
            }
        ],
        code_snippets=[
            {
                "title": "PDU Transformation Pipeline Diagram",
                "language": "text",
                "code": "Layer               Operation                 Resulting PDU\nApplication         User Input / Payload  ──> [ Data ]\nTransport           + TCP Port Header     ──> [ TCP Header | Data ]                (Segment)\nNetwork             + IP Address Header   ──> [ IP Header | TCP | Data ]           (Packet)\nData Link           + MAC Header & FCS    ──> [ MAC Header | IP | TCP | Data | FCS] (Frame)\nPhysical            Encoding onto Wire    ──> 011010010110001001110011...          (Bits)",
                "explanation": "Illustrates how each layer wraps lower layers with metadata headers and checksum trailers."
            },
            {
                "title": "Verifying Network Interface MTU in Linux",
                "language": "bash",
                "code": "# Check interface MTU (Default is 1500 bytes for standard Ethernet)\nip link show eth0\n# 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP",
                "explanation": "Displays the Maximum Transmission Unit allowed on the network interface before packet fragmentation occurs."
            },
            {
                "title": "Testing Path MTU and Prohibiting Fragmentation with Ping",
                "language": "bash",
                "code": "# Send 1472-byte payload with Don't Fragment (DF) flag set\n# 1472 payload + 20 byte IP header + 8 byte ICMP header = exactly 1500 MTU!\nping -c 2 -M do -s 1472 8.8.8.8\n\n# Attempting 1500 byte payload fails with 'Message too long, mtu=1500'\nping -c 1 -M do -s 1500 8.8.8.8",
                "explanation": "Tests Maximum Transmission Unit boundaries using ICMP ping with the Don't Fragment bit enabled."
            },
            {
                "title": "Python PDU Overhead Calculator",
                "language": "python",
                "code": "def calculate_packet_overhead(payload_bytes: int) -> dict:\n    tcp_header = 20\n    ip_header = 20\n    ethernet_header_trailer = 14 + 4  # 14 byte header + 4 byte FCS trailer\n    total_frame_size = payload_bytes + tcp_header + ip_header + ethernet_header_trailer\n    \n    return {\n        'payload': payload_bytes,\n        'headers_total': tcp_header + ip_header + ethernet_header_trailer,\n        'total_on_wire': total_frame_size,\n        'efficiency_percent': round((payload_bytes / total_frame_size) * 100, 2)\n    }",
                "explanation": "Calculates byte overhead introduced by TCP, IP, and Ethernet framing during encapsulation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="PDU Name by Layer Resolver",
            description="Write a Python function `get_pdu_name(layer_level: str) -> str` that maps `'TRANSPORT'`, `'NETWORK'`, `'DATALINK'`, and `'PHYSICAL'` to their PDU name: `'Segment'`, `'Packet'`, `'Frame'`, and `'Bits'`. Return `'Data'` for any other layer.",
            starter_code="def get_pdu_name(layer_level: str) -> str:\n    # Return official PDU name\n    pass",
            solution_code="def get_pdu_name(layer_level: str) -> str:\n    mapping = {\n        'TRANSPORT': 'Segment',\n        'NETWORK': 'Packet',\n        'DATALINK': 'Frame',\n        'DATA LINK': 'Frame',\n        'PHYSICAL': 'Bits'\n    }\n    return mapping.get(layer_level.strip().upper(), 'Data')",
            expected_output="get_pdu_name('Network') == 'Packet', get_pdu_name('DataLink') == 'Frame'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the term for the process where each layer in the protocol stack adds its own control header to data as it moves down?",
                options=[
                    "Encapsulation",
                    "Decapsulation",
                    "Subnetting",
                    "Modulation"
                ],
                correct_answer="Encapsulation",
                explanation="Encapsulation wraps data payloads with headers and trailers as information moves down the stack."
            ),
            QuizQuestionBlueprint(
                question="What is the standard Maximum Transmission Unit (MTU) size for standard Ethernet frames?",
                options=[
                    "1500 bytes",
                    "64 bytes",
                    "9000 bytes",
                    "256 bytes"
                ],
                correct_answer="1500 bytes",
                explanation="Standard IEEE 802.3 Ethernet defines a default MTU of 1500 bytes for the IP payload."
            ),
            QuizQuestionBlueprint(
                question="Which PDU has both a header at the front and a trailer (Frame Check Sequence - FCS) at the rear?",
                options=[
                    "Layer 2 Frame",
                    "Layer 3 Packet",
                    "Layer 4 Segment",
                    "Layer 7 Message"
                ],
                correct_answer="Layer 2 Frame",
                explanation="Layer 2 frames include a trailing Frame Check Sequence (FCS) containing a CRC checksum."
            ),
            QuizQuestionBlueprint(
                question="What happens during 'Decapsulation' when a web server receives an Ethernet frame from a client?",
                options=[
                    "The server strips the headers layer-by-layer as the payload ascends the stack, delivering raw data to the application",
                    "The server compresses the packet into a zip archive",
                    "The frame is deleted and forgotten",
                    "The server reboots"
                ],
                correct_answer="The server strips the headers layer-by-layer as the payload ascends the stack, delivering raw data to the application",
                explanation="Decapsulation unpacks and verifies headers progressively as data ascends up to the application."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Jumbo Frame' in modern enterprise data centers?",
                options=[
                    "An Ethernet frame with an MTU configured up to 9000 bytes to reduce CPU packet-processing overhead on storage networks",
                    "A cable that is 500 meters long",
                    "A picture sent via email",
                    "A frame sent across satellite"
                ],
                correct_answer="An Ethernet frame with an MTU configured up to 9000 bytes to reduce CPU packet-processing overhead on storage networks",
                explanation="Jumbo frames (up to 9000 bytes MTU) allow storage networks (SAN/iSCSI) to transfer large payloads with fewer interrupts."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: MAC Addressing & Ethernet Frame Structure",
        concept="Mastering Layer 2 hardware addressing: 48-bit MAC address format, OUI vs NIC identifier, unicast/multicast/broadcast addresses, and Ethernet II frames",
        analogy="Think of a MAC address like the Vehicle Identification Number (VIN) stamped permanently into the steel engine block of your car at the manufacturing plant. No matter what city you drive through, what license plate you screw onto the bumper (**IP Address**), or what paint color you use, your car's physical steel VIN number (**MAC Address**) never changes! A police officer standing on the local street corner identifies your exact car by that VIN.",
        theory_sections=[
            {
                "heading": "Anatomy of a 48-bit MAC Address",
                "body": "A Media Access Control (MAC) address is a 48-bit (6-byte) physical hardware address expressed as 12 hexadecimal characters (e.g. `00:1A:2B:3C:4D:5E` or `001a.2b3c.4d5e`). The first 24 bits (3 bytes) represent the **OUI (Organizationally Unique Identifier)** assigned by IEEE to the manufacturer (e.g. Cisco, Apple, Intel). The remaining 24 bits are assigned uniquely by the vendor."
            },
            {
                "heading": "Unicast, Multicast & Broadcast MACs",
                "body": "(1) **Unicast**: Targeted to one specific NIC (least significant bit of first octet is 0). (2) **Multicast**: Targeted to a group of subscribed devices (starts with `01:00:5E:...` for IPv4 multicast). (3) **Broadcast**: Targeted to all hosts on the local segment, expressed as `FF:FF:FF:FF:FF:FF`."
            }
        ],
        code_snippets=[
            {
                "title": "Ethernet II Frame Structure Breakdown",
                "language": "text",
                "code": "Field               Size        Purpose\nPreamble            7 Bytes     Clock synchronization (10101010...)\nSFD                 1 Byte      Start Frame Delimiter (10101011)\nDestination MAC     6 Bytes     Target hardware address (Unicast/Broadcast)\nSource MAC          6 Bytes     Sender hardware address\nEtherType           2 Bytes     Identifies payload protocol (0x0800=IPv4, 0x86DD=IPv6, 0x0806=ARP)\nPayload / Data      46-1500 B   Layer 3 Packet (Padded to 46 bytes if needed)\nFCS (CRC-32)        4 Bytes     Frame Check Sequence error detection",
                "explanation": "Standard 802.3 / Ethernet II framing specifications detailing header fields and payload bounds."
            },
            {
                "title": "Inspecting Physical MAC Address in Linux and Windows",
                "language": "bash",
                "code": "# Linux: Displays link/ether 48-bit hex MAC\nip link show eth0\n# link/ether 52:54:00:12:34:56 brd ff:ff:ff:ff:ff:ff\n\n# Windows: Displays Physical Address\ngetmac /v",
                "explanation": "CLI commands to view physical Layer 2 MAC addresses on local network interface cards."
            },
            {
                "title": "Extracting OUI Vendor from MAC Address in Python",
                "language": "python",
                "code": "def parse_mac_address(mac_str: str) -> dict:\n    # Normalize separators (: or - or .)\n    clean_mac = mac_str.replace(':', '').replace('-', '').replace('.', '').upper()\n    if len(clean_mac) != 12:\n        raise ValueError('Invalid MAC format')\n        \n    oui = clean_mac[:6]       # First 24 bits (Manufacturer)\n    nic_id = clean_mac[6:]    # Last 24 bits (Device)\n    return {'OUI': oui, 'NIC_ID': nic_id, 'is_broadcast': clean_mac == 'FFFFFFFFFFFF'}",
                "explanation": "Splits 48-bit MAC addresses into the 24-bit OUI vendor block and the 24-bit NIC device ID."
            },
            {
                "title": "Inspecting ARP Table Linking IP Addresses to MAC Addresses",
                "language": "bash",
                "code": "# Inspect local ARP cache resolving IP addresses to physical MAC hardware addresses\narp -a\n# Internet Address      Physical Address      Type\n# 192.168.1.1           00-50-56-e8-11-02     dynamic\n# 192.168.1.254         ff-ff-ff-ff-ff-ff     static",
                "explanation": "Shows the device's local Address Resolution Protocol (ARP) mapping table."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="MAC Address Validator",
            description="Write a Python function `is_valid_mac(mac: str) -> bool` that verifies whether a string is a valid 48-bit MAC address in colon-separated format (e.g. `'00:1A:2B:3C:4D:5E'`, 6 groups of 2 hexadecimal digits).",
            starter_code="def is_valid_mac(mac: str) -> bool:\n    # Validate colon-separated MAC address\n    pass",
            solution_code="import re\n\ndef is_valid_mac(mac: str) -> bool:\n    pattern = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'\n    return bool(re.match(pattern, mac.strip()))",
            expected_output="is_valid_mac('00:1A:2B:3C:4D:5E') == True, is_valid_mac('00:1G:2B:3C:4D:5E') == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How many bits (and bytes) long is a standard Ethernet MAC address?",
                options=[
                    "48 bits (6 bytes)",
                    "32 bits (4 bytes)",
                    "128 bits (16 bytes)",
                    "64 bits (8 bytes)"
                ],
                correct_answer="48 bits (6 bytes)",
                explanation="Standard MAC addresses are 48 bits (6 octets) represented as 12 hexadecimal characters."
            ),
            QuizQuestionBlueprint(
                question="What do the first 24 bits (3 bytes) of a MAC address represent?",
                options=[
                    "The OUI (Organizationally Unique Identifier) assigned to the NIC manufacturer by IEEE",
                    "The user's home postal code",
                    "The IP address in binary",
                    "The battery serial number"
                ],
                correct_answer="The OUI (Organizationally Unique Identifier) assigned to the NIC manufacturer by IEEE",
                explanation="The first 24 bits comprise the OUI identifying the hardware manufacturer (e.g., Cisco, Intel)."
            ),
            QuizQuestionBlueprint(
                question="What is the universal Layer 2 Broadcast MAC address used to send frames to all hosts on a local LAN?",
                options=[
                    "FF:FF:FF:FF:FF:FF",
                    "00:00:00:00:00:00",
                    "255.255.255.255",
                    "AA:BB:CC:DD:EE:FF"
                ],
                correct_answer="FF:FF:FF:FF:FF:FF",
                explanation="FF:FF:FF:FF:FF:FF represents all 48 bits set to 1, signifying a Layer 2 broadcast."
            ),
            QuizQuestionBlueprint(
                question="What is the role of the Frame Check Sequence (FCS) located at the tail of an Ethernet frame?",
                options=[
                    "To detect data corruption using a 32-bit Cyclic Redundancy Check (CRC-32) algorithm",
                    "To encrypt the payload",
                    "To compress video data",
                    "To store user passwords"
                ],
                correct_answer="To detect data corruption using a 32-bit Cyclic Redundancy Check (CRC-32) algorithm",
                explanation="The FCS field holds a CRC-32 checksum; frames arriving with mismatched FCS values are dropped."
            ),
            QuizQuestionBlueprint(
                question="What EtherType hex value in an Ethernet II frame header indicates that the enclosed payload is an IPv4 packet?",
                options=[
                    "0x0800",
                    "0x86DD (IPv6)",
                    "0x0806 (ARP)",
                    "0xFFFF"
                ],
                correct_answer="0x0800",
                explanation="EtherType 0x0800 designates an IPv4 payload; 0x86DD is IPv6; 0x0806 is ARP."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 10
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: IPv4 Addressing & Classes (A, B, C, D, E)",
        concept="Mastering 32-bit logical addressing: Dotted-decimal notation, Network ID vs Host ID portions, and legacy Classful addressing (Classes A, B, C, D, E)",
        analogy="Think of an IPv4 address like a traditional mailing address: 'Street Name (Network ID)' + 'House Number (Host ID)'. Everyone living on the same street shares the same Street Name so the postal truck can find the neighborhood. Class A addresses were like giant countries with few streets but millions of houses; Class C addresses were like tiny rural villages with thousands of short streets but only 254 houses each!",
        theory_sections=[
            {
                "heading": "Structure of an IPv4 Address",
                "body": "An IPv4 address is a 32-bit binary number divided into four 8-bit octets separated by dots (e.g. `192.168.1.1`). Because 1 byte ranges from 0 to 255 (`2^8 - 1`), each octet is a decimal between 0 and 255. The total theoretical IPv4 address space is `2^32` (approx. 4.29 billion addresses)."
            },
            {
                "heading": "Legacy Classful Addressing Rules",
                "body": "Historically (before CIDR), addresses were partitioned into 5 classes based on leading bits: (1) **Class A**: `1.0.0.0` - `126.255.255.255` (/8 mask, 16M hosts/net); (2) **Class B**: `128.0.0.0` - `191.255.255.255` (/16 mask, 65,534 hosts/net); (3) **Class C**: `192.0.0.0` - `223.255.255.255` (/24 mask, 254 hosts/net); (4) **Class D**: `224.0.0.0` - `239.255.255.255` (Multicast); (5) **Class E**: `240.0.0.0` - `255.255.255.254` (Experimental). Note: `127.0.0.0/8` is reserved for loopback."
            }
        ],
        code_snippets=[
            {
                "title": "Converting Dotted Decimal IPv4 into 32-Bit Binary",
                "language": "python",
                "code": "def ip_to_binary(ip_str: str) -> str:\n    octets = [int(o) for o in ip_str.split('.')]\n    # Format each octet as an 8-bit binary string\n    bin_octets = [f'{o:08b}' for o in octets]\n    return '.'.join(bin_octets)\n\nprint('192.168.1.1 in Binary:')\nprint(ip_to_binary('192.168.1.1'))\n# Output: 11000000.10101000.00000001.00000001",
                "explanation": "Converts dotted decimal notation into raw 32-bit binary representation."
            },
            {
                "title": "Legacy Classful IPv4 Range Summary Table",
                "language": "text",
                "code": "Class   Leading Bits   First Octet Range   Default Mask     Usable Hosts per Network\nA       0              1.0.0.0 - 126.x.x.x 255.0.0.0 (/8)   16,777,214 hosts\nB       10             128.0.0.0 - 191.x   255.255.0.0 (/16) 65,534 hosts\nC       110            192.0.0.0 - 223.x   255.255.255.0(/24)254 hosts\nD       1110           224.0.0.0 - 239.x   None (Multicast) Not Applicable\nE       1111           240.0.0.0 - 255.x   None (Research)  Not Applicable\n* 127.0.0.0/8 is reserved for internal host Loopback (localhost)",
                "explanation": "Summary table of class ranges, default subnet masks, and host capacities."
            },
            {
                "title": "Testing Local Host Loopback Adapter Reachability",
                "language": "bash",
                "code": "# Tests that local TCP/IP protocol stack software is functioning properly\nping 127.0.0.1\n\n# Ping localhost hostname\nping localhost",
                "explanation": "Pinging 127.0.0.1 tests the internal software stack without generating traffic on physical wires."
            },
            {
                "title": "Python Classful Address Classifier",
                "language": "python",
                "code": "def get_ipv4_class(ip_str: str) -> str:\n    first_octet = int(ip_str.split('.')[0])\n    if 1 <= first_octet <= 126:\n        return 'Class A'\n    elif first_octet == 127:\n        return 'Loopback Address'\n    elif 128 <= first_octet <= 191:\n        return 'Class B'\n    elif 192 <= first_octet <= 223:\n        return 'Class C'\n    elif 224 <= first_octet <= 239:\n        return 'Class D (Multicast)'\n    elif 240 <= first_octet <= 255:\n        return 'Class E (Experimental)'\n    return 'Invalid IP'",
                "explanation": "Inspects the first octet of an IPv4 address to determine its class under classful rules."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="IPv4 Class Classifier",
            description="Write a Python function `classify_ip_class(ip: str) -> str` that inspects an IPv4 string and returns `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, or `'Loopback'` based on standard first-octet ranges. Return `'Invalid'` if first octet is not between 1 and 255.",
            starter_code="def classify_ip_class(ip: str) -> str:\n    # Return IPv4 class letter\n    pass",
            solution_code="def classify_ip_class(ip: str) -> str:\n    try:\n        first = int(ip.split('.')[0])\n        if 1 <= first <= 126:\n            return 'A'\n        elif first == 127:\n            return 'Loopback'\n        elif 128 <= first <= 191:\n            return 'B'\n        elif 192 <= first <= 223:\n            return 'C'\n        elif 224 <= first <= 239:\n            return 'D'\n        elif 240 <= first <= 255:\n            return 'E'\n        return 'Invalid'\n    except:\n        return 'Invalid'",
            expected_output="classify_ip_class('10.0.0.1') == 'A', classify_ip_class('192.168.1.1') == 'C'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How many total bits are in a single standard IPv4 address?",
                options=[
                    "32 bits",
                    "48 bits",
                    "128 bits",
                    "64 bits"
                ],
                correct_answer="32 bits",
                explanation="IPv4 addresses are 32 bits long, formatted into four 8-bit octets."
            ),
            QuizQuestionBlueprint(
                question="What is the default subnet mask for a legacy Class B IPv4 network?",
                options=[
                    "255.255.0.0 (/16)",
                    "255.0.0.0 (/8)",
                    "255.255.255.0 (/24)",
                    "255.255.255.255 (/32)"
                ],
                correct_answer="255.255.0.0 (/16)",
                explanation="Class B networks allocate 16 bits to the Network ID (255.255.0.0) and 16 bits to hosts."
            ),
            QuizQuestionBlueprint(
                question="What is the entire `127.0.0.0/8` address block reserved for in IPv4?",
                options=[
                    "Loopback testing of the local computer TCP/IP stack (e.g. 127.0.0.1)",
                    "Public military websites",
                    "Satellite communications",
                    "Wireless printers"
                ],
                correct_answer="Loopback testing of the local computer TCP/IP stack (e.g. 127.0.0.1)",
                explanation="127.0.0.0/8 is reserved for loopback, routing packets directly within the local operating system."
            ),
            QuizQuestionBlueprint(
                question="What is the first octet range for Class C IPv4 addresses?",
                options=[
                    "192 to 223",
                    "1 to 126",
                    "128 to 191",
                    "224 to 239"
                ],
                correct_answer="192 to 223",
                explanation="Class C spans 192.0.0.0 through 223.255.255.255 (binary leading bits 110)."
            ),
            QuizQuestionBlueprint(
                question="What is Class D (`224.0.0.0` - `239.255.255.255`) reserved for in networking?",
                options=[
                    "Multicast groups",
                    "Government servers",
                    "Home Wi-Fi routers",
                    "Experimental research only"
                ],
                correct_answer="Multicast groups",
                explanation="Class D addresses are reserved for one-to-many multicast transmission groups (e.g. OSPF, RIPv2)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 11
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Private vs Public IP Addresses (RFC 1918 & CGNAT)",
        concept="Preserving address space with RFC 1918 private scopes: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, APIPA (169.254.0.0/16), and Carrier-Grade NAT",
        analogy="Think of IP addresses like telephone extension numbers inside a massive corporate skyscraper. The outside world knows the skyscraper by its single official public telephone number (**Public IP**). Inside the building, each employee has a private 3-digit desk extension like '101' or '102' (**Private IP**). You can't dial '101' directly from a payphone in London—the receptionist (**NAT Gateway**) must bridge your call to that desk!",
        theory_sections=[
            {
                "heading": "The IPv4 Exhaustion Crisis & RFC 1918",
                "body": "Because 4.29 billion IPv4 addresses could not support every smartphone, computer, and smart toaster on Earth, the IETF published **RFC 1918**, setting aside three private ranges that are **NOT routable on the public Internet**: (1) `10.0.0.0 - 10.255.255.255` (10.0.0.0/8); (2) `172.16.0.0 - 172.31.255.255` (172.16.0.0/12); (3) `192.168.0.0 - 192.168.255.255` (192.168.0.0/16). Millions of homes and businesses reuse these identical addresses concurrently."
            },
            {
                "heading": "APIPA (169.254.0.0/16) & Carrier-Grade NAT (CGNAT)",
                "body": "If a host is configured for DHCP but fails to reach a DHCP server, modern operating systems automatically assign an **APIPA (Automatic Private IP Addressing)** address in the `169.254.0.0/16` range. Internet Service Providers facing public IP scarcity use **CGNAT (Carrier-Grade NAT)** in `100.64.0.0/10` (RFC 6598) to nest multiple residential customer routers behind shared public addresses."
            }
        ],
        code_snippets=[
            {
                "title": "RFC 1918 Private IPv4 Address Ranges Summary",
                "language": "text",
                "code": "Class    CIDR Prefix     IP Range                          Total Addresses    Common Usage\nClass A  10.0.0.0/8      10.0.0.0 - 10.255.255.255         16,777,216         Large Enterprises / Clouds\nClass B  172.16.0.0/12   172.16.0.0 - 172.31.255.255       1,048,576          Mid-size Networks / Docker\nClass C  192.168.0.0/16  192.168.0.0 - 192.168.255.255     65,536             Home & SOHO Wi-Fi Routers\nAPIPA    169.254.0.0/16  169.254.0.0 - 169.254.255.255     65,536             DHCP Failure Fallback\nCGNAT    100.64.0.0/10   100.64.0.0 - 100.127.255.255      4,194,304          ISP Shared Carrier NAT",
                "explanation": "Comprehensive reference of reserved non-routable private address allocations."
            },
            {
                "title": "Determining Local Private IP vs WAN Public IP via CLI",
                "language": "bash",
                "code": "# View local private IP assigned by home router\nhostname -I | awk '{print $1}'\n# Output: 192.168.1.105 (RFC 1918 Private IP)\n\n# Query public external WAN IP as seen by global Internet\ncurl https://api.ipify.org\n# Output: 203.135.42.18 (Publicly Routable IP)",
                "explanation": "Contrasts the internal private address assigned by a local router with the external public IP seen by web servers."
            },
            {
                "title": "Recognizing APIPA DHCP Failure in Windows / Linux",
                "language": "text",
                "code": "Ethernet adapter Local Area Connection:\n   IPv4 Address. . . . . . . . . . . : 169.254.88.142\n   Subnet Mask . . . . . . . . . . . : 255.255.0.0\n   Default Gateway . . . . . . . . . : <blank>\n# A 169.254.x.x IP indicates device cannot communicate with DHCP server!",
                "explanation": "An APIPA address indicates that the client could not obtain a valid DHCP lease from the network."
            },
            {
                "title": "Python RFC 1918 Address Checker (using ipaddress module)",
                "language": "python",
                "code": "import ipaddress\n\ndef inspect_ip_scope(ip_str: str) -> dict:\n    ip_obj = ipaddress.ip_address(ip_str)\n    return {\n        'ip': ip_str,\n        'is_private': ip_obj.is_private,\n        'is_global': ip_obj.is_global,\n        'is_loopback': ip_obj.is_loopback,\n        'is_link_local_apipa': ip_obj.is_link_local\n    }\n\nprint(inspect_ip_scope('192.168.1.50'))",
                "explanation": "Uses Python's standard library to inspect IPv4 private, global, loopback, and link-local scope."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Private IP Address Detector",
            description="Write a Python function `is_rfc1918_private(ip: str) -> bool` that returns `True` if an IPv4 address falls within `10.0.0.0/8`, `172.16.0.0/12` (172.16-172.31), or `192.168.0.0/16`. Return `False` otherwise.",
            starter_code="def is_rfc1918_private(ip: str) -> bool:\n    # Return True if RFC 1918 private address\n    pass",
            solution_code="def is_rfc1918_private(ip: str) -> bool:\n    try:\n        parts = [int(p) for p in ip.split('.')]\n        if len(parts) != 4:\n            return False\n        if parts[0] == 10:\n            return True\n        if parts[0] == 172 and 16 <= parts[1] <= 31:\n            return True\n        if parts[0] == 192 and parts[1] == 168:\n            return True\n        return False\n    except:\n        return False",
            expected_output="is_rfc1918_private('10.50.1.1') == True, is_rfc1918_private('8.8.8.8') == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if a router attempts to forward a packet with a destination IP of `192.168.1.50` onto the public Internet?",
                options=[
                    "Public Internet routers immediately drop the packet because RFC 1918 addresses are non-routable on the public web",
                    "The packet is broadcast to every computer on Earth",
                    "The router charges money to the ISP",
                    "The destination is converted to Google"
                ],
                correct_answer="Public Internet routers immediately drop the packet because RFC 1918 addresses are non-routable on the public web",
                explanation="RFC 1918 private addresses are strictly blocked and dropped by Internet core routers."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is a valid RFC 1918 private Class B IP range?",
                options=[
                    "172.16.0.0 to 172.31.255.255 (/12 prefix)",
                    "172.0.0.0 to 172.255.255.255",
                    "192.168.0.0 to 192.168.255.255",
                    "10.0.0.0 to 10.255.255.255"
                ],
                correct_answer="172.16.0.0 to 172.31.255.255 (/12 prefix)",
                explanation="The RFC 1918 Class B scope covers 16 continuous Class B network numbers: 172.16.0.0 to 172.31.255.255."
            ),
            QuizQuestionBlueprint(
                question="What does seeing an IP address starting with `169.254.x.x` on a Windows or Mac computer signify?",
                options=[
                    "The computer failed to obtain an IP lease from a DHCP server and assigned an APIPA fallback address",
                    "The computer has connected to high-speed fiber internet",
                    "The network card is permanently broken",
                    "The computer has joined the FBI network"
                ],
                correct_answer="The computer failed to obtain an IP lease from a DHCP server and assigned an APIPA fallback address",
                explanation="169.254.0.0/16 is APIPA (Link-Local), self-assigned when DHCP discovery broadcasts go unanswered."
            ),
            QuizQuestionBlueprint(
                question="Why can millions of homes around the world all use `192.168.1.1` simultaneously without IP address conflicts?",
                options=[
                    "Because private IP spaces are isolated within independent LANs and translated into unique public IPs via NAT at the router gateway",
                    "Because all home routers share the same physical cable",
                    "Because Wi-Fi ignores IP addresses",
                    "Because computers change their IP address every second"
                ],
                correct_answer="Because private IP spaces are isolated within independent LANs and translated into unique public IPs via NAT at the router gateway",
                explanation="Private networks are separate local namespaces; Network Address Translation (NAT) translates them to public IPs."
            ),
            QuizQuestionBlueprint(
                question="What is the Carrier-Grade NAT (CGNAT) address space designated by RFC 6598 for ISPs?",
                options=[
                    "100.64.0.0/10",
                    "10.0.0.0/8",
                    "192.168.1.0/24",
                    "224.0.0.0/4"
                ],
                correct_answer="100.64.0.0/10",
                explanation="100.64.0.0/10 is specifically reserved for Carrier-Grade NAT infrastructure between ISPs and consumer routers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 12
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Subnetting & FLSM (Fixed Length Subnet Mask)",
        concept="Mastering binary subnet division: Borrowing host bits, calculating subnets, Network Address, Broadcast Address, and Usable Host formulas (2^H - 2)",
        analogy="Think of a standard pizza cut into large slices. A Class C network (`/24`) is one giant 256-slice pizza pie for a single room. But what if you have 4 separate small departments (Sales, Marketing, HR, Finance) and you don't want them overhearing each other's conversations? By **subnetting**, you cut that single pizza into 4 equal mini-pizzas of 64 slices each (**FLSM**). Each department gets its own secure table and room number!",
        theory_sections=[
            {
                "heading": "Why Subnet? Broadcast Control & Security",
                "body": "Subnetting divides a large physical network into smaller, logical sub-networks. This achieves three vital goals: (1) **Contains Broadcast Traffic**: Broadcast storms are restricted to their local subnet; (2) **Enhances Security**: Firewalls and Access Control Lists (ACLs) can filter traffic moving between subnets; (3) **Conserves Addresses**: Eliminates wasted host addresses."
            },
            {
                "heading": "The Core Subnetting Math Formulas",
                "body": "Subnetting operates by **borrowing bits from the Host portion** and giving them to the Network portion: (1) Number of created subnets = `2^S` (where `S` is borrowed subnet bits); (2) Total IP addresses per subnet = `2^H` (where `H` is remaining host bits); (3) **Usable hosts per subnet = `2^H - 2`**. Why minus 2? Because the **First address** is reserved as the Network ID, and the **Last address** is reserved as the Directed Broadcast Address."
            }
        ],
        code_snippets=[
            {
                "title": "FLSM Subnetting Example: Splitting /24 into 4 Subnets (/26)",
                "language": "text",
                "code": "Original Network: 192.168.1.0/24 (Mask: 255.255.255.0, 256 IPs)\nBorrow 2 bits: 11000000 -> /26 (Mask: 255.255.255.192, Block Size = 256 - 192 = 64)\nCreated Subnets: 2^2 = 4 Subnets. Usable hosts per subnet: 2^6 - 2 = 62 hosts.\n\nSubnet #  Network ID       Usable Host Range             Broadcast Address\nSubnet 1  192.168.1.0/26   192.168.1.1   - 192.168.1.62   192.168.1.63\nSubnet 2  192.168.1.64/26  192.168.1.65  - 192.168.1.126  192.168.1.127\nSubnet 3  192.168.1.128/26 192.168.1.129 - 192.168.1.190  192.168.1.191\nSubnet 4  192.168.1.192/26 192.168.1.193 - 192.168.1.254  192.168.1.255",
                "explanation": "Complete breakdown of a /24 split into four equal /26 subnets showing block sizes, ranges, and broadcasts."
            },
            {
                "title": "Subnet Mask Magic Number / Block Size Calculator in Python",
                "language": "python",
                "code": "def calculate_flsm_subnets(network_ip: str, prefix_len: int, borrow_bits: int):\n    new_prefix = prefix_len + borrow_bits\n    host_bits = 32 - new_prefix\n    block_size = 2 ** host_bits\n    num_subnets = 2 ** borrow_bits\n    usable_hosts = (2 ** host_bits) - 2\n    \n    print(f'New Prefix: /{new_prefix} | Subnets Created: {num_subnets}')\n    print(f'Block Size: {block_size} | Usable Hosts per Subnet: {usable_hosts}')\n\ncalculate_flsm_subnets('192.168.1.0', 24, 2)",
                "explanation": "Calculates block size, total subnets, and usable hosts when borrowing bits."
            },
            {
                "title": "Configuring Subnetted Interface on a Cisco Router",
                "language": "text",
                "code": "Router(config)# interface GigabitEthernet0/0/1\nRouter(config-if)# description Accounting-Subnet\nRouter(config-if)# ip address 192.168.1.65 255.255.255.192\nRouter(config-if)# no shutdown\n# Configures router gateway using first usable host of Subnet 2 (/26)",
                "explanation": "Assigns a subnetted IP address and custom 255.255.255.192 mask to a router interface."
            },
            {
                "title": "Verifying Subnet Mask Application with Linux ipcalc",
                "language": "bash",
                "code": "# Using ipcalc utility to inspect subnet boundaries\nipcalc 192.168.1.65/26\n# Address:   192.168.1.65\n# Netmask:   255.255.255.192 = 26\n# Network:   192.168.1.64/26\n# HostMin:   192.168.1.65\n# HostMax:   192.168.1.126\n# Broadcast: 192.168.1.127\n# Hosts/Net: 62",
                "explanation": "Calculates network address, usable host boundaries, and broadcast targets via ipcalc."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Usable Host Capacity Calculator",
            description="Write a Python function `get_usable_host_count(prefix: int) -> int` that calculates usable host count `(2 ** (32 - prefix)) - 2` for prefixes 1 to 30. For /31 and /32, return 0 (or 2 for /31 RFC 3021, but standard formula is 0).",
            starter_code="def get_usable_host_count(prefix: int) -> int:\n    # Calculate usable IPv4 host capacity\n    pass",
            solution_code="def get_usable_host_count(prefix: int) -> int:\n    if prefix >= 31 or prefix <= 0:\n        return 0\n    host_bits = 32 - prefix\n    return (2 ** host_bits) - 2",
            expected_output="get_usable_host_count(24) == 254, get_usable_host_count(26) == 62, get_usable_host_count(30) == 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why must you subtract 2 from total addresses (`2^H - 2`) when calculating usable hosts in a subnet?",
                options=[
                    "Because the very first address is reserved as the Network ID and the very last address is reserved as the Directed Broadcast",
                    "To account for the router's battery power",
                    "Because 2 is an unlucky number in computer science",
                    "To reserve space for the website domain name"
                ],
                correct_answer="Because the very first address is reserved as the Network ID and the very last address is reserved as the Directed Broadcast",
                explanation="The first address identifies the wire network itself; the last address is the broadcast address."
            ),
            QuizQuestionBlueprint(
                question="How many usable host IP addresses are provided by a `/26` subnet mask (255.255.255.192)?",
                options=[
                    "62 usable hosts",
                    "64 usable hosts",
                    "254 usable hosts",
                    "30 usable hosts"
                ],
                correct_answer="62 usable hosts",
                explanation="32 - 26 = 6 host bits; `2^6 - 2` = 64 - 2 = 62 usable host addresses."
            ),
            QuizQuestionBlueprint(
                question="If you borrow 3 bits from a `/24` network, how many new equal-sized subnets are created?",
                options=[
                    "8 subnets (2^3 = 8)",
                    "3 subnets",
                    "6 subnets",
                    "16 subnets"
                ],
                correct_answer="8 subnets (2^3 = 8)",
                explanation="Formula `2^S` where S is borrowed bits: `2^3` = 8 equal subnets."
            ),
            QuizQuestionBlueprint(
                question="What is the Broadcast Address for the subnet `192.168.1.0/26`?",
                options=[
                    "192.168.1.63",
                    "192.168.1.64",
                    "192.168.1.255",
                    "192.168.1.1"
                ],
                correct_answer="192.168.1.63",
                explanation="The block size for /26 is 64; the range is 0 to 63, making 192.168.1.63 the broadcast address."
            ),
            QuizQuestionBlueprint(
                question="Which subnet mask prefix length is traditionally used for point-to-point router links to conserve addresses with exactly 2 usable hosts?",
                options=[
                    "/30 (255.255.255.252)",
                    "/24 (255.255.255.0)",
                    "/28 (255.255.255.240)",
                    "/16 (255.255.0.0)"
                ],
                correct_answer="/30 (255.255.255.252)",
                explanation="A /30 provides 4 total IPs: 1 network, 2 usable hosts (perfect for router-to-router links), and 1 broadcast."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: VLSM & CIDR (Variable Length Subnet Masking)",
        concept="Engineering custom subnet hierarchies: VLSM optimization, CIDR slash notation, route summarization (supernetting), and zero waste IP designs",
        analogy="Think of Fixed Length Subnetting (FLSM) like baking only large 16-inch pizzas: whether a customer is a hungry family of 6 or a tiny toddler wanting 1 slice, you are forced to give everyone an identical giant pizza (massive waste of food!). **VLSM (Variable Length)** is like a custom artisan bakery: you bake an 8-slice pie for Engineering (50 hosts), a 4-slice pie for HR (20 hosts), and a tiny 2-bite snack for point-to-point router links (2 hosts). Zero waste!",
        theory_sections=[
            {
                "heading": "FLSM Inefficiency vs VLSM Elegance",
                "body": "In Fixed-Length Subnet Masking (FLSM), all subnets share the exact same mask, which wastes enormous address space when subnets have disparate host counts. **VLSM (Variable Length Subnet Masking)** allows engineers to subnet an already subnetted space, assigning tailored prefix lengths (e.g. `/25` for 100 hosts, `/27` for 25 hosts, `/30` for router links) without address overlap."
            },
            {
                "heading": "CIDR (Classless Inter-Domain Routing) & Supernetting",
                "body": "Introduced in 1993 by RFC 1519, **CIDR** abolished rigid A/B/C classes in favor of arbitrary prefix lengths expressed with slash notation (`/prefix`). CIDR also enables **Route Summarization (Supernetting)**: combining multiple contiguous subnets into a single advertised route (e.g. summarizing four `/24` subnets into one `/22` route), shrinking global routing tables."
            }
        ],
        code_snippets=[
            {
                "title": "VLSM Design Example (Subnetting Largest to Smallest)",
                "language": "text",
                "code": "Base Block: 192.168.10.0/24 (256 Total IPs)\nRequirement: Branch A (100 hosts), Branch B (50 hosts), WAN Link (2 hosts)\n\nStep 1: Always allocate LARGEST requirement first!\n- Branch A (Need 100 hosts) -> Need 128 block (/25)\n  Subnet A: 192.168.10.0/25 (Usable: .1 - .126, Broadcast: .127)\n\nStep 2: Take remaining block (192.168.10.128/25) and subdivide:\n- Branch B (Need 50 hosts)  -> Need 64 block (/26)\n  Subnet B: 192.168.10.128/26 (Usable: .129 - .190, Broadcast: .191)\n\nStep 3: Subdivide remaining space (192.168.10.192/26):\n- WAN Link (Need 2 hosts)   -> Need 4 block (/30)\n  Subnet C: 192.168.10.192/30 (Usable: .193 - .194, Broadcast: .195)",
                "explanation": "Demonstrates the golden rule of VLSM: order requirements from largest to smallest to avoid address fragmentation."
            },
            {
                "title": "Python Standard Library ipaddress VLSM Subnetter",
                "language": "python",
                "code": "import ipaddress\n\nnet = ipaddress.ip_network('192.168.10.0/24')\n\n# Carve out subnets dynamically\nsubnets_26 = list(net.subnets(prefixlen_diff=2)) # Generates four /26 subnets\nfor s in subnets_26:\n    print(f'Subnet: {s} | Netmask: {s.netmask} | Usable: {s.num_addresses - 2}')",
                "explanation": "Uses Python's ipaddress module to divide network blocks dynamically."
            },
            {
                "title": "CIDR Route Summarization (Supernetting) Calculation",
                "language": "text",
                "code": "Subnets to Summarize:\n192.168.0.0/24  -> 11000000.10101000.000000 00.00000000\n192.168.1.0/24  -> 11000000.10101000.000000 01.00000000\n192.168.2.0/24  -> 11000000.10101000.000000 10.00000000\n192.168.3.0/24  -> 11000000.10101000.000000 11.00000000\nMatching common prefix bits: 22 bits identical!\nSummary Supernet Route: 192.168.0.0/22 (Covers all 4 subnets in 1 routing table entry)",
                "explanation": "Calculates common matching binary prefix bits to summarize four /24 networks into one /22 route."
            },
            {
                "title": "Configuring CIDR Supernet Route on Cisco Router",
                "language": "text",
                "code": "Router(config)# ip route 192.168.0.0 255.255.252.0 10.1.1.2\n# Advertises single /22 summary route instead of four individual /24 routes",
                "explanation": "Applies a summarized supernet static route to reduce routing table size."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Smallest CIDR Prefix Finder",
            description="Write a Python function `find_min_prefix_for_hosts(hosts_needed: int) -> int` that determines the smallest CIDR prefix length (1 to 30) capable of accommodating `hosts_needed` usable hosts.",
            starter_code="def find_min_prefix_for_hosts(hosts_needed: int) -> int:\n    # Find CIDR prefix length for host requirement\n    pass",
            solution_code="def find_min_prefix_for_hosts(hosts_needed: int) -> int:\n    for prefix in range(30, 0, -1):\n        usable = (2 ** (32 - prefix)) - 2\n        if usable >= hosts_needed:\n            return prefix\n    return 0",
            expected_output="find_min_prefix_for_hosts(50) == 26, find_min_prefix_for_hosts(100) == 25, find_min_prefix_for_hosts(2) == 30"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the golden rule when designing a Variable Length Subnet Mask (VLSM) addressing scheme?",
                options=[
                    "Always allocate and subnet the largest host requirements first, descending to the smallest",
                    "Always allocate point-to-point links first",
                    "Never use numbers ending in zero",
                    "All subnets must have identical masks"
                ],
                correct_answer="Always allocate and subnet the largest host requirements first, descending to the smallest",
                explanation="Designing from largest to smallest prevents address overlap and contiguous block fragmentation."
            ),
            QuizQuestionBlueprint(
                question="What is 'Route Summarization' (Supernetting) in CIDR?",
                options=[
                    "Combining multiple contiguous subnets into a single advertised route with a shorter prefix length to shrink routing tables",
                    "Encrypting router passwords",
                    "Deleting old routes from memory",
                    "Converting IPv4 into IPv6 automatically"
                ],
                correct_answer="Combining multiple contiguous subnets into a single advertised route with a shorter prefix length to shrink routing tables",
                explanation="Supernetting condenses multiple route advertisements into a single summary prefix, saving router memory."
            ),
            QuizQuestionBlueprint(
                question="What single summarized CIDR route covers `192.168.0.0/24`, `192.168.1.0/24`, `192.168.2.0/24`, and `192.168.3.0/24`?",
                options=[
                    "192.168.0.0/22",
                    "192.168.0.0/20",
                    "192.168.0.0/23",
                    "192.168.0.0/16"
                ],
                correct_answer="192.168.0.0/22",
                explanation="The first 22 bits are identical across all four /24 networks; 24 - 2 bits = /22."
            ),
            QuizQuestionBlueprint(
                question="What prefix length provides exactly 2 usable host addresses for point-to-point WAN router links without wasting addresses?",
                options=[
                    "/30",
                    "/24",
                    "/28",
                    "/29"
                ],
                correct_answer="/30",
                explanation="A /30 prefix provides 4 total IPs (2^2), yielding exactly 2 usable host addresses."
            ),
            QuizQuestionBlueprint(
                question="Why was CIDR (Classless Inter-Domain Routing) introduced to replace legacy Class A, B, and C networks?",
                options=[
                    "To prevent global IPv4 exhaustion and stop the explosion of Internet backbone routing table sizes",
                    "Because classes were banned by international law",
                    "To make computers run faster",
                    "To enable color displays"
                ],
                correct_answer="To prevent global IPv4 exhaustion and stop the explosion of Internet backbone routing table sizes",
                explanation="CIDR allowed flexible prefix sizing, preventing IPv4 depletion and curbing routing table bloat."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: IPv6 Addressing (Structure, Types & SLAAC)",
        concept="The next-generation 128-bit Internet protocol: Hexadecimal format, zero compression rules, Unicast types (Global, Link-Local, Unique Local), and SLAAC autoconfiguration",
        analogy="Think of IPv4 like an old 7-digit town phonebook from 1950. As the city grew into a sprawling metropolis with smartphones and IoT gadgets, the phone company ran completely out of numbers. **IPv6** didn't just add one extra digit—it created a phone number long enough to assign a unique IP address to every single grain of sand on planet Earth (`3.4 x 10^38` addresses)! We will never run out again.",
        theory_sections=[
            {
                "heading": "128-Bit Hexadecimal Format & Compression Rules",
                "body": "IPv6 addresses are 128 bits long (4 times larger than IPv4), written as eight groups of four hexadecimal digits separated by colons (e.g. `2001:0db8:85a3:0000:0000:8a2e:0370:7334`). Two compression rules simplify notation: (1) **Omit Leading Zeros** in any hextet (`:0042:` -> `:42:`); (2) **Double Colon (`::`) Rule**: Contiguous groups of all-zero hextets can be compressed to `::` **exactly once per address**."
            },
            {
                "heading": "IPv6 Address Types & SLAAC",
                "body": "IPv6 eliminates broadcast completely, using Unicast, Anycast, and Multicast: (1) **Global Unicast (2000::/3)**: Publicly routable on the global Internet; (2) **Link-Local (FE80::/10)**: Non-routable local communication required on every active interface; (3) **Unique Local (FC00::/7)**: Private enterprise scope. Through **SLAAC (Stateless Address Autoconfiguration)**, hosts discover routers via ICMPv6 Router Advertisements and configure their own IPv6 addresses with zero DHCP server needed!"
            }
        ],
        code_snippets=[
            {
                "title": "IPv6 Compression Rules Step-by-Step",
                "language": "text",
                "code": "Original Uncompressed: \n2001:0db8:0000:0000:0000:0000:1428:57ab\n\nStep 1: Omit Leading Zeros in each hextet:\n2001:db8:0:0:0:0:1428:57ab\n\nStep 2: Compress consecutive all-zero hextets with '::' (once only!):\n2001:db8::1428:57ab (Final Compressed Canonical IPv6 Address)",
                "explanation": "Demonstrates applying leading zero omission and the double-colon rule to compress IPv6 strings."
            },
            {
                "title": "Inspecting IPv6 Link-Local and Global Addresses in Linux",
                "language": "bash",
                "code": "# View IPv6 addresses (look for inet6)\nip -6 addr show\n# inet6 fe80::5054:ff:fe12:3456/64 scope link (Link-Local - FE80::)\n# inet6 2001:db8:1::10/64 scope global (Global Unicast - 2000::/3)",
                "explanation": "Displays local IPv6 link-local addresses (fe80::) and globally routable unicast IPs."
            },
            {
                "title": "Configuring IPv6 and SLAAC on a Cisco Router Interface",
                "language": "text",
                "code": "Router(config)# ipv6 unicast-routing\nRouter(config)# interface GigabitEthernet0/0\nRouter(config-if)# ipv6 address 2001:db8:acad:1::1/64\nRouter(config-if)# ipv6 address fe80::1 link-local\nRouter(config-if)# no shutdown\n# Router immediately begins sending ICMPv6 Router Advertisements (RA) for SLAAC",
                "explanation": "Enables IPv6 routing, sets global and link-local addresses, and initiates SLAAC router advertisements."
            },
            {
                "title": "Testing IPv6 Connectivity with Ping6",
                "language": "bash",
                "code": "# Ping IPv6 local loopback (::1, equivalent of 127.0.0.1 in IPv4)\nping -6 ::1\n\n# Ping Google Public IPv6 DNS server\nping -6 2001:4860:4860::8888",
                "explanation": "Validates IPv6 protocol stack functionality and global reachability using native IPv6 ping."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="IPv6 Address Expander",
            description="Write a Python function `expand_ipv6(ip_str: str) -> str` using the standard `ipaddress` module that expands a compressed IPv6 string into its full 32-hex-character uncompressed representation.",
            starter_code="def expand_ipv6(ip_str: str) -> str:\n    # Return fully expanded IPv6 string\n    pass",
            solution_code="import ipaddress\n\ndef expand_ipv6(ip_str: str) -> str:\n    try:\n        return ipaddress.IPv6Address(ip_str.strip()).exploded\n    except:\n        return 'Invalid IPv6'",
            expected_output="expand_ipv6('2001:db8::1') == '2001:0db8:0000:0000:0000:0000:0000:0001'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How many bits long is an IPv6 address compared to an IPv4 address?",
                options=[
                    "128 bits (IPv6) vs 32 bits (IPv4)",
                    "64 bits vs 32 bits",
                    "256 bits vs 128 bits",
                    "48 bits vs 32 bits"
                ],
                correct_answer="128 bits (IPv6) vs 32 bits (IPv4)",
                explanation="IPv6 uses 128-bit addresses, offering 340 undecillion (`3.4 * 10^38`) unique addresses."
            ),
            QuizQuestionBlueprint(
                question="What prefix denotes an IPv6 Link-Local address automatically assigned to every active interface?",
                options=[
                    "FE80::/10",
                    "2001::/16",
                    "FC00::/7",
                    "::1/128"
                ],
                correct_answer="FE80::/10",
                explanation="Link-Local addresses always begin with `FE80::/10` and operate only within the local segment."
            ),
            QuizQuestionBlueprint(
                question="What is the equivalent IPv6 loopback address to IPv4's `127.0.0.1`?",
                options=[
                    "::1",
                    "::0",
                    "FE80::1",
                    "2001::1"
                ],
                correct_answer="::1",
                explanation="`::1` (or `0000:...:0001`) is the designated IPv6 loopback address."
            ),
            QuizQuestionBlueprint(
                question="How many times can the double-colon (`::`) compression shortcut be used within a single IPv6 address?",
                options=[
                    "Exactly once, to prevent ambiguity about how many zero hextets are omitted",
                    "Unlimited times",
                    "Up to 4 times",
                    "Twice per address"
                ],
                correct_answer="Exactly once, to prevent ambiguity about how many zero hextets are omitted",
                explanation="`::` can only appear once in an address; multiple occurrences would make parsing ambiguous."
            ),
            QuizQuestionBlueprint(
                question="What is SLAAC (Stateless Address Autoconfiguration) in IPv6?",
                options=[
                    "A mechanism where client devices discover local routers and configure their own global IPv6 address without needing a stateful DHCPv6 server",
                    "An encryption algorithm",
                    "A cable testing standard",
                    "A tool for deleting old routes"
                ],
                correct_answer="A mechanism where client devices discover local routers and configure their own global IPv6 address without needing a stateful DHCPv6 server",
                explanation="SLAAC allows hosts to listen to ICMPv6 Router Advertisements and auto-generate their own address."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 15
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: How a Switch Works (MAC Address Table & Frame Forwarding)",
        concept="Mastering Layer 2 forwarding logic: The 3 core switch functions (Learning, Forwarding/Filtering, and Flooding), CAM table aging, and unknown unicast handling",
        analogy="Think of an Ethernet switch like a receptionist at an office building with 24 individual tenant mailboxes. When the switch first powers on, its directory notebook (**MAC Address Table / CAM Table**) is completely empty. When letter arrives from Port 1 stamped 'From Alice' (**Learning**), the switch writes: 'Alice sits at Port 1'. If the letter is addressed to Bob and the switch has never seen Bob before, it runs to all 23 other doors shouting: 'Is Bob here?!' (**Unknown Unicast Flooding**). The moment Bob replies from Port 5, the switch writes down Bob's location and will never shout for Bob again (**Filtering & Direct Forwarding**)!",
        theory_sections=[
            {
                "heading": "The Three Core Switch Operations",
                "body": "A Layer 2 switch operates autonomously using three simple rules: (1) **Learning**: The switch inspects the **Source MAC address** of every incoming frame and records it in its CAM (Content Addressable Memory) table alongside the receiving port and VLAN with an aging timer (typically 300 seconds); (2) **Forwarding & Filtering**: If the **Destination MAC address** is already in the table on a different port, the frame is forwarded *only* out that specific port; (3) **Flooding**: If the Destination MAC is unknown, or if it is a Broadcast (`FF:FF:FF:FF:FF:FF`) or Multicast, the switch floods the frame out all ports except the receiving port."
            },
            {
                "heading": "MAC Table Aging & Unknown Unicast Flooding",
                "body": "If an idle host does not transmit for 300 seconds, its entry is purged from the CAM table to free memory. If another host attempts to communicate with that idle host, the switch performs **Unknown Unicast Flooding**, broadcasting the frame to re-learn the location as soon as the recipient responds."
            }
        ],
        code_snippets=[
            {
                "title": "Switch Forwarding Decision Logic (Python Simulation)",
                "language": "python",
                "code": "class EthernetSwitch:\n    def __init__(self, ports_count=8):\n        self.ports = list(range(1, ports_count + 1))\n        self.mac_table = {}  # {mac_address: port}\n        \n    def process_frame(self, in_port: int, src_mac: str, dst_mac: str):\n        # 1. LEARN: Always record source MAC on receiving port\n        self.mac_table[src_mac] = in_port\n        \n        # 2. FORWARD or FLOOD\n        if dst_mac == 'FF:FF:FF:FF:FF:FF' or dst_mac not in self.mac_table:\n            # Flood out all ports except arrival port\n            out_ports = [p for p in self.ports if p != in_port]\n            return {'action': 'FLOOD', 'ports': out_ports}\n        else:\n            target_port = self.mac_table[dst_mac]\n            if target_port == in_port:\n                return {'action': 'FILTER_DROP', 'ports': []}\n            return {'action': 'FORWARD', 'ports': [target_port]}",
                "explanation": "Implements the foundational Learning, Forwarding, Filtering, and Flooding algorithms of a Layer 2 switch."
            },
            {
                "title": "Inspecting the MAC Table on a Cisco Catalyst Switch",
                "language": "text",
                "code": "Switch# show mac address-table dynamic\n          Mac Address Table\n-------------------------------------------\nVlan    Mac Address       Type        Ports\n----    -----------       --------    -----\n  10    0014.2201.2345    DYNAMIC     Gi0/1\n  10    0014.2201.8899    DYNAMIC     Gi0/2\nTotal Mac Addresses for this criterion: 2",
                "explanation": "Displays dynamic entries learned from frame source addresses and mapped to switch interfaces."
            },
            {
                "title": "Clearing the MAC Address Table Manually",
                "language": "text",
                "code": "Switch# clear mac address-table dynamic\n# Erases learned entries to verify learning and flooding behavior during testing",
                "explanation": "Flushes the dynamic CAM table, forcing the switch to re-learn active device locations."
            },
            {
                "title": "Configuring CAM Table Aging Time on Cisco Switch",
                "language": "text",
                "code": "Switch(config)# mac address-table aging-time 600\n# Extends default aging time from 300 seconds to 600 seconds",
                "explanation": "Adjusts how long idle MAC address table entries are retained before eviction."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Switch Forwarding Action Predictor",
            description="Write a Python function `predict_switch_action(known_macs: dict[str, int], in_port: int, dst_mac: str) -> str` that returns `'FORWARD'` if `dst_mac` is in `known_macs` and its port != `in_port`, `'FILTER'` if `dst_mac` port == `in_port`, and `'FLOOD'` otherwise.",
            starter_code="def predict_switch_action(known_macs: dict[str, int], in_port: int, dst_mac: str) -> str:\n    # Return 'FORWARD', 'FILTER', or 'FLOOD'\n    pass",
            solution_code="def predict_switch_action(known_macs: dict[str, int], in_port: int, dst_mac: str) -> str:\n    if dst_mac == 'FF:FF:FF:FF:FF:FF' or dst_mac not in known_macs:\n        return 'FLOOD'\n    out_port = known_macs[dst_mac]\n    if out_port == in_port:\n        return 'FILTER'\n    return 'FORWARD'",
            expected_output="predict_switch_action({'AA': 2}, 1, 'AA') == 'FORWARD', predict_switch_action({}, 1, 'BB') == 'FLOOD'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which field of an incoming Ethernet frame does a switch inspect to populate its MAC Address (CAM) Table?",
                options=[
                    "Source MAC Address",
                    "Destination MAC Address",
                    "IP Header Checksum",
                    "EtherType field"
                ],
                correct_answer="Source MAC Address",
                explanation="Switches learn device locations by recording the frame's Source MAC address and arrival port."
            ),
            QuizQuestionBlueprint(
                question="What action does an Ethernet switch take when receiving a frame destined for a MAC address that is NOT in its CAM table?",
                options=[
                    "It floods the frame out all ports belonging to that VLAN except the receiving port (Unknown Unicast Flooding)",
                    "It drops the frame and shuts down the port",
                    "It sends an email alert to the network administrator",
                    "It converts the frame into an IPv6 packet"
                ],
                correct_answer="It floods the frame out all ports belonging to that VLAN except the receiving port (Unknown Unicast Flooding)",
                explanation="Unknown unicast frames are flooded to all ports within the VLAN except the ingress port."
            ),
            QuizQuestionBlueprint(
                question="What is the default aging time for dynamic MAC address table entries on most enterprise switches (such as Cisco)?",
                options=[
                    "300 seconds (5 minutes)",
                    "60 seconds (1 minute)",
                    "24 hours",
                    "Infinite (entries never age out)"
                ],
                correct_answer="300 seconds (5 minutes)",
                explanation="Dynamic CAM entries age out after 300 seconds of inactivity to keep tables accurate."
            ),
            QuizQuestionBlueprint(
                question="What memory technology allows enterprise switches to perform MAC address lookups in hardware within nanoseconds?",
                options=[
                    "CAM (Content Addressable Memory) / TCAM",
                    "Standard SATA Hard Drives",
                    "USB Flash Drives",
                    "Optical CDs"
                ],
                correct_answer="CAM (Content Addressable Memory) / TCAM",
                explanation="CAM/TCAM hardware searches entire memory spaces in a single clock cycle, powering wire-speed switching."
            ),
            QuizQuestionBlueprint(
                question="What happens if a switch receives a frame where the Destination MAC is known to reside on the EXACT same port it arrived on?",
                options=[
                    "The switch filters (drops) the frame because the destination already received it on the local shared segment",
                    "The switch duplicates the frame 1,000 times",
                    "The switch triggers an alarm",
                    "The switch restarts itself"
                ],
                correct_answer="The switch filters (drops) the frame because the destination already received it on the local shared segment",
                explanation="Filtering drops frames that do not need cross-port traversal, preventing unnecessary traffic propagation."
            )
        ]
    )
]
