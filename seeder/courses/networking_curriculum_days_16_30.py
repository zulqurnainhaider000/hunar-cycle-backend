"""
Computer Networking Basics 60-Day Curriculum - Part 2 (Days 16 to 30)
Module 4: Layer 2 - Switching Technologies (Days 16-21)
Module 5: Layer 3 - Routing Technologies (Days 22-29)
Module 6: Core Network Services & Protocols (Day 30)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_16_TO_30 = [
    # -------------------------------------------------------------
    # DAY 16
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: VLANs (Virtual LANs) & 802.1Q Trunking",
        concept="Segmenting broadcast domains at Layer 2: Access ports, Trunk ports, IEEE 802.1Q frame tagging, and Native VLANs",
        analogy="Think of a standard switch like an open-plan office building where 100 employees sit in the same giant noisy room. If anyone sneezes or shouts an announcement (**Broadcast Storm**), all 100 people are interrupted. A **VLAN** is like erecting soundproof drywall partitions dividing the room into Department 10 (Finance) and Department 20 (HR). A **Trunk link** is the private elevator shaft connecting floors with an employee badge scanner that stamps color-coded stickers (**802.1Q Tag**) on badges so everyone reaches their right room!",
        theory_sections=[
            {
                "heading": "Why VLANs? Segmenting Broadcast Domains",
                "body": "A Virtual LAN (VLAN) creates logically isolated Layer 2 broadcast domains on the same physical switch hardware. Traffic cannot cross from VLAN 10 to VLAN 20 without a Layer 3 routing device. VLANs enhance security, prevent broadcast propagation from degrading network performance, and allow organizing networks by function rather than physical geography."
            },
            {
                "heading": "Access Ports vs 802.1Q Trunking & Native VLAN",
                "body": "An **Access Port** belongs to exactly one VLAN and carries untagged standard Ethernet frames to end-user devices (PCs, printers). A **Trunk Port** connects switches together, carrying traffic for multiple VLANs simultaneously by injecting a 4-byte **IEEE 802.1Q tag** containing a 12-bit **VLAN ID (VID 1 to 4094)**. The **Native VLAN** (default VLAN 1) carries untagged legacy control traffic across the trunk."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring VLANs and Assigning Access Ports (Cisco IOS)",
                "language": "text",
                "code": "Switch(config)# vlan 10\nSwitch(config-vlan)# name Accounting\nSwitch(config-vlan)# exit\n\nSwitch(config)# interface range FastEthernet0/1 - 10\nSwitch(config-if-range)# switchport mode access\nSwitch(config-if-range)# switchport access vlan 10\nSwitch(config-if-range)# no shutdown",
                "explanation": "Creates VLAN 10 named Accounting and configures ports 1 through 10 as access members of that VLAN."
            },
            {
                "title": "Configuring an 802.1Q Trunk Link Between Switches",
                "language": "text",
                "code": "Switch(config)# interface GigabitEthernet0/1\nSwitch(config-if)# description Trunk-to-Core-Switch\nSwitch(config-if)# switchport trunk encapsulation dot1q\nSwitch(config-if)# switchport mode trunk\nSwitch(config-if)# switchport trunk allowed vlan 10,20,30\nSwitch(config-if)# switchport trunk native vlan 99",
                "explanation": "Configures an uplink as an 802.1Q trunk, allowing only specified VLANs and setting a secure native VLAN."
            },
            {
                "title": "Verifying VLAN Memberships and Active Trunk Ports",
                "language": "text",
                "code": "Switch# show vlan brief\nVLAN Name                             Status    Ports\n---- -------------------------------- --------- -------------------------------\n1    default                          active    Fa0/11, Fa0/12\n10   Accounting                       active    Fa0/1, Fa0/2, Fa0/3\n20   Engineering                      active    Fa0/4, Fa0/5\n\nSwitch# show interfaces trunk\nPort        Mode             Encapsulation  Status        Native vlan\nGi0/1       on               802.1q         trunking      99",
                "explanation": "Verifies that ports are correctly mapped to their respective broadcast domains and checks trunking status."
            },
            {
                "title": "IEEE 802.1Q 4-Byte Tag Structure Breakdown",
                "language": "text",
                "code": "Ethernet Frame with 802.1Q Tag:\n[ Dest MAC | Src MAC | 802.1Q Tag (4 Bytes) | EtherType | Payload | FCS ]\n                     │\n                     ├── TPID (2 Bytes): 0x8100 (Identifies 802.1Q frame)\n                     ├── Priority (3 Bits): 802.1p Quality of Service\n                     ├── DEI (1 Bit): Drop Eligible Indicator\n                     └── VLAN ID (12 Bits): 1 to 4094 (Identifies target VLAN)",
                "explanation": "Diagram detailing the 4-byte 802.1Q header inserted between the Source MAC and EtherType fields."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="802.1Q VLAN ID Range Validator",
            description="Write a Python function `is_valid_vlan_id(vid: int) -> bool` that verifies whether a VLAN ID falls within the standard 12-bit IEEE 802.1Q allocatable range (1 to 4094, with 0 and 4095 reserved).",
            starter_code="def is_valid_vlan_id(vid: int) -> bool:\n    # Return True if valid allocatable VLAN ID\n    pass",
            solution_code="def is_valid_vlan_id(vid: int) -> bool:\n    return isinstance(vid, int) and 1 <= vid <= 4094",
            expected_output="is_valid_vlan_id(10) == True, is_valid_vlan_id(4095) == False, is_valid_vlan_id(0) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary architectural purpose of configuring VLANs on an enterprise switch?",
                options=[
                    "To segment a single physical switch into multiple isolated Layer 2 broadcast domains for security and performance",
                    "To increase the physical voltage of Ethernet cables",
                    "To convert copper cables into wireless connections",
                    "To automatically back up files to the cloud"
                ],
                correct_answer="To segment a single physical switch into multiple isolated Layer 2 broadcast domains for security and performance",
                explanation="VLANs divide physical switches into isolated broadcast domains, containing broadcast storms."
            ),
            QuizQuestionBlueprint(
                question="What standard encapsulation protocol is used on trunk links to tag Ethernet frames with a 12-bit VLAN ID?",
                options=[
                    "IEEE 802.1Q (dot1q)",
                    "IEEE 802.11 (Wi-Fi)",
                    "IEEE 802.3u",
                    "ISL (Cisco proprietary only)"
                ],
                correct_answer="IEEE 802.1Q (dot1q)",
                explanation="IEEE 802.1Q is the industry-standard trunking protocol inserting a 4-byte tag into Ethernet headers."
            ),
            QuizQuestionBlueprint(
                question="Can two host computers connected to the same physical switch communicate directly at Layer 2 if they are on different VLANs (e.g. VLAN 10 and VLAN 20)?",
                options=[
                    "No, traffic cannot cross between different VLANs without a Layer 3 routing device",
                    "Yes, switches automatically bridge all VLANs without routers",
                    "Only on wireless connections",
                    "Only if both computers have the same IP address"
                ],
                correct_answer="No, traffic cannot cross between different VLANs without a Layer 3 routing device",
                explanation="VLANs are strictly separated at Layer 2; inter-VLAN communication requires Layer 3 routing."
            ),
            QuizQuestionBlueprint(
                question="How large is the VLAN ID (VID) field inside an IEEE 802.1Q header, and how many VLANs can it support?",
                options=[
                    "12 bits long, supporting up to 4094 usable VLANs",
                    "8 bits long, supporting 256 VLANs",
                    "32 bits long, supporting 4 billion VLANs",
                    "16 bits long, supporting 65,536 VLANs"
                ],
                correct_answer="12 bits long, supporting up to 4094 usable VLANs",
                explanation="12 bits (`2^12 = 4096`) minus reserved values 0 and 4095 yields 4094 usable VLAN IDs."
            ),
            QuizQuestionBlueprint(
                question="What is the role of the 'Native VLAN' on an 802.1Q trunk port?",
                options=[
                    "Frames belonging to the Native VLAN are transmitted across the trunk link without any 802.1Q tag header",
                    "It shuts down the switch during an attack",
                    "It charges money for each packet",
                    "It encrypts all voice calls"
                ],
                correct_answer="Frames belonging to the Native VLAN are transmitted across the trunk link without any 802.1Q tag header",
                explanation="802.1Q trunks transmit Native VLAN traffic untagged for backward compatibility with non-VLAN devices."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: DTP & VTP (Dynamic Trunking & VLAN Trunking Protocols)",
        concept="Automating trunk negotiation with DTP and centralizing VLAN database propagation with VTP (Server, Client, and Transparent modes)",
        analogy="Think of **DTP** like two diplomatic ambassadors meeting at a border checkpoint: they whisper to each other to negotiate whether their border should be an open multi-lane highway (**Trunk**) or a single tourist lane (**Access**). **VTP** is like a central university registrar sending a memo to all campus branch offices: when the head registrar (**VTP Server**) creates 'Classroom 501', the memo instantly updates the course books at all branch desks (**VTP Clients**) automatically!",
        theory_sections=[
            {
                "heading": "DTP (Dynamic Trunking Protocol) Modes",
                "body": "DTP is a proprietary Cisco protocol that negotiates trunk links between switch ports: (1) **Switchport mode access**: Permanently forces port into non-trunking mode; (2) **Switchport mode trunk**: Permanently forces port into trunking mode; (3) **Dynamic Desirable**: Actively asks neighbor to form a trunk; (4) **Dynamic Auto**: Passive, waits for neighbor to initiate trunking. If both sides are `dynamic auto`, the link remains an access port."
            },
            {
                "heading": "VTP (VLAN Trunking Protocol) Architecture & Risks",
                "body": "VTP allows network administrators to create, rename, or delete VLANs once on a **VTP Server**, which automatically synchronizes the VLAN database (`vlan.dat`) to all **VTP Clients** sharing the same VTP Domain and password using **Configuration Revision Numbers**. **VTP Transparent mode** ignores incoming VLAN updates and forwards them, maintaining its own local database. **Caution**: Connecting an old lab switch with a higher revision number can wipe out an entire company's VLAN database!"
            }
        ],
        code_snippets=[
            {
                "title": "Configuring DTP Port Modes on Cisco Switch",
                "language": "text",
                "code": "-- Best Practice: Disable DTP on user access ports to prevent VLAN hopping attacks!\nSwitch(config)# interface FastEthernet0/5\nSwitch(config-if)# switchport mode access\nSwitch(config-if)# switchport nonegotiate\n\n-- Best Practice on Inter-Switch Links: Force trunk mode and disable DTP\nSwitch(config)# interface GigabitEthernet0/1\nSwitch(config-if)# switchport mode trunk\nSwitch(config-if)# switchport nonegotiate",
                "explanation": "Disabling DTP with `switchport nonegotiate` is an enterprise security best practice against spoofing."
            },
            {
                "title": "Configuring VTP Domain, Mode, and Password",
                "language": "text",
                "code": "Switch-Core(config)# vtp domain HunarEnterprise\nSwitch-Core(config)# vtp mode server\nSwitch-Core(config)# vtp password SecretVtpKey2026\nSwitch-Core(config)# vtp version 2\n\n-- On Access Layer Switch:\nSwitch-Access(config)# vtp domain HunarEnterprise\nSwitch-Access(config)# vtp mode client\nSwitch-Access(config)# vtp password SecretVtpKey2026",
                "explanation": "Sets up a VTP server to propagate VLAN definitions to connected VTP client switches."
            },
            {
                "title": "Verifying VTP Status and Revision Number",
                "language": "text",
                "code": "Switch# show vtp status\nVTP Version capable             : 1 to 3\nVTP Operating Mode              : Client\nVTP Domain Name                 : HunarEnterprise\nVTP Pruning Mode                : Enabled\nVTP Configuration Revision      : 14\nNumber of existing VLANs        : 12",
                "explanation": "Displays VTP operating mode, domain name, pruning status, and the configuration revision counter."
            },
            {
                "title": "DTP Link Negotiation Matrix (Python Helper)",
                "language": "python",
                "code": "def negotiate_dtp(mode_a: str, mode_b: str) -> str:\n    a, b = mode_a.lower(), mode_b.lower()\n    if 'trunk' in [a, b]:\n        return 'Trunk'\n    if 'access' in [a, b]:\n        return 'Access'\n    if a == 'desirable' or b == 'desirable':\n        return 'Trunk'\n    # Both sides 'auto'\n    return 'Access (Both sides passive)'\n\nprint(negotiate_dtp('desirable', 'auto')) # Output: Trunk",
                "explanation": "Evaluates DTP mode combinations between neighbor switch ports."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DTP Negotiation Matrix Calculator",
            description="Write a Python function `calculate_dtp_outcome(port1: str, port2: str) -> str` that returns `'Trunk'` if a trunk is successfully negotiated, and `'Access'` otherwise. Valid modes are `'trunk'`, `'access'`, `'desirable'`, and `'auto'`.",
            starter_code="def calculate_dtp_outcome(port1: str, port2: str) -> str:\n    # Return 'Trunk' or 'Access'\n    pass",
            solution_code="def calculate_dtp_outcome(port1: str, port2: str) -> str:\n    p1, p2 = port1.strip().lower(), port2.strip().lower()\n    if p1 == 'access' or p2 == 'access':\n        return 'Access'\n    if p1 == 'trunk' or p2 == 'trunk':\n        return 'Trunk'\n    if p1 == 'desirable' or p2 == 'desirable':\n        return 'Trunk'\n    return 'Access'",
            expected_output="calculate_dtp_outcome('desirable', 'auto') == 'Trunk', calculate_dtp_outcome('auto', 'auto') == 'Access'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if two connected switch ports are both set to DTP `dynamic auto`?",
                options=[
                    "The link remains an Access port because neither side actively initiates trunk negotiation",
                    "The link forms a Trunk automatically",
                    "Both switch ports shut down with an error",
                    "The switches catch fire"
                ],
                correct_answer="The link remains an Access port because neither side actively initiates trunk negotiation",
                explanation="`dynamic auto` is passive; if neither side initiates (`desirable` or `trunk`), it stays an access link."
            ),
            QuizQuestionBlueprint(
                question="Why is `switchport nonegotiate` recommended on end-user access ports in secure networks?",
                options=[
                    "It turns off DTP packets, preventing rogue laptops from spoofing switch frames to form an unauthorized trunk (VLAN hopping)",
                    "It increases computer processor speed",
                    "It gives the user free administrative rights",
                    "It reduces power consumption to zero"
                ],
                correct_answer="It turns off DTP packets, preventing rogue laptops from spoofing switch frames to form an unauthorized trunk (VLAN hopping)",
                explanation="Disabling DTP prevents attackers from negotiating trunks and hopping into sensitive VLANs."
            ),
            QuizQuestionBlueprint(
                question="What VTP mode receives and forwards VTP advertisements across trunks but does NOT update its own local VLAN database?",
                options=[
                    "VTP Transparent Mode",
                    "VTP Server Mode",
                    "VTP Client Mode",
                    "VTP Off Mode"
                ],
                correct_answer="VTP Transparent Mode",
                explanation="Transparent mode maintains its own local VLANs while forwarding VTP frames to downstream switches."
            ),
            QuizQuestionBlueprint(
                question="What danger exists if a used switch with a higher VTP Configuration Revision Number is plugged into a production network?",
                options=[
                    "It will overwrite the production VLAN database across all VTP servers and clients, potentially wiping out all corporate VLANs",
                    "It causes the router to reformat its hard drive",
                    "It deletes all employee emails",
                    "The switches will run out of IP addresses"
                ],
                correct_answer="It will overwrite the production VLAN database across all VTP servers and clients, potentially wiping out all corporate VLANs",
                explanation="Switches blindly accept updates from devices with higher revision numbers in the same VTP domain."
            ),
            QuizQuestionBlueprint(
                question="What does 'VTP Pruning' achieve on trunk links?",
                options=[
                    "It prevents unnecessary broadcast traffic from traversing trunks to switches that have no active ports assigned to that VLAN",
                    "It deletes old switches from the server room",
                    "It cuts the physical cables",
                    "It shortens long passwords"
                ],
                correct_answer="It prevents unnecessary broadcast traffic from traversing trunks to switches that have no active ports assigned to that VLAN",
                explanation="VTP Pruning blocks broadcast and unknown unicast frames from traversing trunks where no receivers exist."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: STP, RSTP & MSTP (Loop Prevention & Spanning Tree)",
        concept="Preventing Layer 2 broadcast storms: Bridge Protocol Data Units (BPDUs), Root Bridge election, Port States, 802.1D STP vs 802.1w Rapid STP (RSTP)",
        analogy="Think of redundant switch cables like building multiple road bridges across a river. If an emergency siren vehicle (**Broadcast Frame**) drives onto Bridge A, crosses the river, sees Bridge B, crosses back, and loops in an infinite circle forever at 100 mph, the bridges jam and collapse (**Broadcast Storm**)! **Spanning Tree Protocol (STP)** is a traffic police officer who temporarily places a barricade on Bridge B (**Blocking State**). If Bridge A collapses, the officer instantly lifts the barricade (**Forwarding State**)!",
        theory_sections=[
            {
                "heading": "The Danger of Layer 2 Loops: Broadcast Storms",
                "body": "Because Ethernet frames lack a Time-To-Live (TTL) field (unlike Layer 3 IP packets), a broadcast frame caught in a redundant switching loop will circle endlessly at wire speed. This causes **Broadcast Storms** (consuming 100% bandwidth within seconds), MAC address table instability (flapping), and multiple frame transmission, freezing the entire LAN."
            },
            {
                "heading": "How STP Works: Root Bridge & Port Roles",
                "body": "IEEE **802.1D Spanning Tree Protocol (STP)** creates a loop-free logical tree: (1) Elect one **Root Bridge** (lowest Bridge ID = Priority + MAC); (2) Each non-root switch selects one **Root Port** (lowest path cost to root); (3) Each segment selects one **Designated Port**; (4) Redundant remaining ports enter **Blocking (Discarding)** state. Modern **802.1w RSTP** reduces convergence time from 50 seconds down to sub-second speeds."
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Spanning Tree Status on a Cisco Switch",
                "language": "text",
                "code": "Switch# show spanning-tree vlan 1\nVLAN0001\n  Spanning tree enabled protocol rstp\n  Root ID    Priority    24577\n             Address     0014.2201.1111\n             Cost        19\n             Port        1 (GigabitEthernet0/1)\n\n  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)\n             Address     0014.2201.2222\n\nInterface        Role Sts Cost      Prio.Nbr Type\n---------------- ---- --- --------- -------- --------------------------------\nGi0/1            Root FWD 19        128.1    P2p\nGi0/2            Altn BLK 19        128.2    P2p  # Blocking redundant loop!",
                "explanation": "Shows the active Root Bridge, local Bridge ID, path cost, Root Port (FWD), and Alternate Blocking port (BLK)."
            },
            {
                "title": "Configuring Switch as Root Bridge (Setting Bridge Priority)",
                "language": "text",
                "code": "-- Method 1: Set Bridge Priority directly (must be multiple of 4096)\nSwitch(config)# spanning-tree vlan 10 priority 4096\n\n-- Method 2: Use Cisco macro helper\nSwitch(config)# spanning-tree vlan 10 root primary\n# Lowers priority to guarantee winning the election against default 32768 switches",
                "explanation": "Forces the core switch to become the Root Bridge by assigning a low priority value."
            },
            {
                "title": "Enabling Rapid STP and PortFast on Edge Ports",
                "language": "text",
                "code": "-- Switch from legacy 802.1D to Rapid Spanning Tree (802.1w)\nSwitch(config)# spanning-tree mode rapid-pvst\n\n-- Enable PortFast on PC access ports (Bypasses 30s listening/learning delay)\nSwitch(config)# interface FastEthernet0/10\nSwitch(config-if)# spanning-tree portfast\nSwitch(config-if)# spanning-tree bpduguard enable",
                "explanation": "RSTP provides sub-second convergence, and PortFast brings edge user ports to forwarding instantly."
            },
            {
                "title": "Simulating Bridge ID Comparison in Python",
                "language": "python",
                "code": "def elect_root_bridge(switches: list[dict]) -> dict:\n    \"\"\"Bridge ID = (Priority * 10^12) + MAC_int. Lowest wins!\"\"\"\n    def bridge_key(s):\n        mac_int = int(s['mac'].replace(':', '').replace('.', ''), 16)\n        return (s['priority'], mac_int)\n        \n    return min(switches, key=bridge_key)\n\nsws = [\n    {'name': 'SW-Access', 'priority': 32768, 'mac': '00:11:22:33:44:55'},\n    {'name': 'SW-Core',   'priority': 4096,  'mac': '00:aa:bb:cc:dd:ee'}\n]\nprint('Elected Root Bridge:', elect_root_bridge(sws)['name'])",
                "explanation": "Calculates Root Bridge election by comparing Bridge Priority followed by lowest MAC address."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Root Bridge Election Simulator",
            description="Write a Python function `find_root_bridge(switches: list[tuple[str, int, str]]) -> str` where each tuple is `(switch_name, priority, mac_address)`. Return the name of the switch that wins the Root Bridge election (lowest priority, tie-breaker lowest MAC address).",
            starter_code="def find_root_bridge(switches: list[tuple[str, int, str]]) -> str:\n    # Return winning switch name\n    pass",
            solution_code="def find_root_bridge(switches: list[tuple[str, int, str]]) -> str:\n    if not switches:\n        return ''\n    sorted_sws = sorted(switches, key=lambda s: (s[1], s[2].replace(':', '').lower()))\n    return sorted_sws[0][0]",
            expected_output="find_root_bridge([('SW1', 32768, 'bb:bb'), ('SW2', 4096, 'aa:aa')]) == 'SW2'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why do Ethernet broadcast loops cause catastrophic network crashes if Spanning Tree Protocol (STP) is disabled?",
                options=[
                    "Because Ethernet frames lack a Time-To-Live (TTL) field, causing broadcast frames to circulate endlessly and consume 100% bandwidth (Broadcast Storm)",
                    "Because switches explode under high traffic",
                    "Because copper wires melt from excess electricity",
                    "Because passwords are broadcasted"
                ],
                correct_answer="Because Ethernet frames lack a Time-To-Live (TTL) field, causing broadcast frames to circulate endlessly and consume 100% bandwidth (Broadcast Storm)",
                explanation="Without an IP-style TTL, Layer 2 broadcast frames loop forever, overwhelming switch CPUs and links."
            ),
            QuizQuestionBlueprint(
                question="How is the Root Bridge elected in Spanning Tree Protocol?",
                options=[
                    "The switch with the lowest Bridge ID (lowest Priority value, broken by lowest MAC address)",
                    "The switch with the most physical cables plugged in",
                    "The switch with the newest serial number",
                    "The switch with the highest IP address"
                ],
                correct_answer="The switch with the lowest Bridge ID (lowest Priority value, broken by lowest MAC address)",
                explanation="Lowest Bridge ID wins the election: priority is evaluated first, then lowest MAC address as tie-breaker."
            ),
            QuizQuestionBlueprint(
                question="What is the default STP bridge priority on Cisco Catalyst switches?",
                options=[
                    "32768",
                    "4096",
                    "0",
                    "65535"
                ],
                correct_answer="32768",
                explanation="The default STP priority is 32768 (plus the VLAN system ID extension)."
            ),
            QuizQuestionBlueprint(
                question="What feature immediately transitions an access port from blocking to forwarding, bypassing the 30-second listening/learning delay for end-user computers?",
                options=[
                    "PortFast",
                    "FastSwitch",
                    "SpeedLink",
                    "TurboMode"
                ],
                correct_answer="PortFast",
                explanation="PortFast allows edge ports connected to hosts to skip listening and learning states, forwarding instantly."
            ),
            QuizQuestionBlueprint(
                question="What is the convergence speed advantage of Rapid Spanning Tree Protocol (RSTP - 802.1w) over legacy 802.1D STP?",
                options=[
                    "RSTP converges in a few milliseconds to seconds using proactive handshake proposals, whereas 802.1D takes 30 to 50 seconds",
                    "RSTP requires no electricity",
                    "RSTP only works on optical fiber",
                    "There is no difference in convergence speed"
                ],
                correct_answer="RSTP converges in a few milliseconds to seconds using proactive handshake proposals, whereas 802.1D takes 30 to 50 seconds",
                explanation="RSTP uses an active proposal-agreement handshake, converging topology changes in milliseconds."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 19
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: EtherChannel & Link Aggregation (LACP vs PAgP)",
        concept="Bundling physical links into logical high-throughput pipes: Bandwidth aggregation, redundancy, IEEE 802.3ad LACP vs Cisco PAgP, and hashing algorithms",
        analogy="Think of physical cables between two switches like lanes on a highway bridge. If you run two separate cables without Spanning Tree, you get a loop. If you run Spanning Tree, it blocks one cable (leaving you with only 1 Gbps). **EtherChannel** is like taking those 4 separate 1-Gbps lanes, wrapping a giant digital rope around them, and declaring them a single 4-Lane Superhighway (**4 Gbps pipe**)! Both switches treat the bundle as one logical link—doubling speed and providing failover!",
        theory_sections=[
            {
                "heading": "Why EtherChannel? Overcoming Spanning Tree Blocking",
                "body": "Normally, STP blocks redundant parallel links between switches to prevent loops, wasting expensive physical ports and bandwidth. **EtherChannel (Link Aggregation)** bundles up to 8 active parallel physical Ethernet links into a single logical interface (`Port-Channel`). Spanning Tree views the bundle as one link, keeping all physical cables forwarding simultaneously."
            },
            {
                "heading": "LACP (IEEE 802.3ad) vs PAgP (Cisco Proprietary)",
                "body": "(1) **LACP (Link Aggregation Control Protocol - IEEE 802.3ad/802.1ax)**: Open industry standard supported across Cisco, Juniper, Arista, and Linux bonding; modes are `Active` (initiates negotiation) and `Passive`. (2) **PAgP (Port Aggregation Protocol)**: Cisco proprietary; modes are `Desirable` and `Auto`. (3) **Static (On)**: Forces bundling without negotiation packets."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring LACP EtherChannel on Cisco Switch",
                "language": "text",
                "code": "Switch(config)# interface range GigabitEthernet0/1 - 2\nSwitch(config-if-range)# description Bundle-to-Core\nSwitch(config-if-range)# channel-group 1 mode active\nSwitch(config-if-range)# exit\n\n-- Configure the logical Port-Channel interface as a Trunk\nSwitch(config)# interface port-channel 1\nSwitch(config-if)# switchport mode trunk\nSwitch(config-if)# switchport trunk allowed vlan 10,20,30",
                "explanation": "Bundles physical ports Gi0/1 and Gi0/2 into logical Port-Channel 1 using standard LACP."
            },
            {
                "title": "Verifying EtherChannel Status and Member Ports",
                "language": "text",
                "code": "Switch# show etherchannel summary\nGroup  Port-channel  Protocol    Ports\n------+-------------+-----------+-----------------------------------------------\n1      Po1(SU)       LACP        Gi0/1(P)    Gi0/2(P)\n# Flags: (S) Layer 2, (U) In Use, (P) Bundled in port-channel\n# Result: 2 Gbps aggregated full duplex link operating normally!",
                "explanation": "Displays channel group state, active protocol, and flags proving ports are bundled in the channel."
            },
            {
                "title": "Configuring Load-Balancing Hashing Algorithm",
                "language": "text",
                "code": "-- Distribute packets across bundle using Source and Destination IP addresses\nSwitch(config)# port-channel load-balance src-dst-ip\n\nSwitch# show etherchannel load-balance\nEtherChannel Load-Balancing Configuration:\n        src-dst-ip",
                "explanation": "Configures hashing parameters (MAC, IP, or Port) to evenly balance flow traffic across member links."
            },
            {
                "title": "LACP Mode Negotiation Matrix (Python Helper)",
                "language": "python",
                "code": "def evaluate_lacp(mode_a: str, mode_b: str) -> bool:\n    a, b = mode_a.lower(), mode_b.lower()\n    if a == 'active' and b in ['active', 'passive']:\n        return True # Successful LACP channel\n    if b == 'active' and a in ['active', 'passive']:\n        return True\n    return False # Fails if both passive or incompatible",
                "explanation": "Verifies that at least one side is configured as Active for successful LACP bundle formation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="LACP Negotiation Validator",
            description="Write a Python function `is_lacp_bundled(mode1: str, mode2: str) -> bool` that takes two switch port LACP modes (`'active'`, `'passive'`, `'on'`) and returns `True` if a dynamic LACP bundle forms successfully (at least one is `'active'`, and both are either `'active'` or `'passive'`).",
            starter_code="def is_lacp_bundled(mode1: str, mode2: str) -> bool:\n    # Return True if LACP bundles successfully\n    pass",
            solution_code="def is_lacp_bundled(mode1: str, mode2: str) -> bool:\n    m1, m2 = mode1.strip().lower(), mode2.strip().lower()\n    valid = {'active', 'passive'}\n    if m1 in valid and m2 in valid:\n        return 'active' in (m1, m2)\n    return False",
            expected_output="is_lacp_bundled('active', 'passive') == True, is_lacp_bundled('passive', 'passive') == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary benefit of configuring an EtherChannel between two switches?",
                options=[
                    "It combines multiple physical Ethernet links into a single logical link, providing aggregated bandwidth and automatic link failover without Spanning Tree blocking",
                    "It eliminates the need for power cords",
                    "It doubles the length of cables to 200 meters",
                    "It converts switches into wireless access points"
                ],
                correct_answer="It combines multiple physical Ethernet links into a single logical link, providing aggregated bandwidth and automatic link failover without Spanning Tree blocking",
                explanation="EtherChannel bundles links into one logical Port-Channel, increasing bandwidth and providing redundancy."
            ),
            QuizQuestionBlueprint(
                question="What is the open industry-standard protocol for dynamic Link Aggregation defined by IEEE 802.3ad / 802.1ax?",
                options=[
                    "LACP (Link Aggregation Control Protocol)",
                    "PAgP (Port Aggregation Protocol)",
                    "DTP",
                    "STP"
                ],
                correct_answer="LACP (Link Aggregation Control Protocol)",
                explanation="LACP is the multi-vendor IEEE standard; PAgP is Cisco proprietary."
            ),
            QuizQuestionBlueprint(
                question="What happens if both ends of a prospective EtherChannel link are configured with LACP mode `passive`?",
                options=[
                    "The EtherChannel will fail to form because neither switch initiates the LACP negotiation handshake",
                    "The switches will form an EtherChannel in 1 microsecond",
                    "The switch ports will shut down permanently",
                    "The cables turn into fiber optics"
                ],
                correct_answer="The EtherChannel will fail to form because neither switch initiates the LACP negotiation handshake",
                explanation="If both ends are passive, neither transmits initial LACP negotiation packets; at least one must be active."
            ),
            QuizQuestionBlueprint(
                question="What prerequisite must all physical member interfaces share to successfully join an EtherChannel bundle?",
                options=[
                    "They must share identical speed, duplex, access VLAN (or allowed trunk VLANs), and native VLAN settings",
                    "They must have the same MAC address",
                    "They must be painted the same color",
                    "They must be connected to host PCs"
                ],
                correct_answer="They must share identical speed, duplex, access VLAN (or allowed trunk VLANs), and native VLAN settings",
                explanation="Member ports must match in speed, duplex, media type, and VLAN configuration."
            ),
            QuizQuestionBlueprint(
                question="Up to how many active physical Ethernet links can be bundled together in a standard LACP Port-Channel?",
                options=[
                    "Up to 8 active links (with up to 8 standby links)",
                    "Up to 2 links only",
                    "Up to 64 links",
                    "Unlimited links"
                ],
                correct_answer="Up to 8 active links (with up to 8 standby links)",
                explanation="Standard LACP supports bundling up to 8 active interfaces (yielding up to 8 Gbps or 80 Gbps)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Power over Ethernet (PoE - 802.3af, 802.3at, 802.3bt)",
        concept="Delivering DC electrical power and data over twisted-pair copper: PSE vs PD, PoE standards (PoE, PoE+, PoE++), power budgets, and remote device powering",
        analogy="Think of Power over Ethernet (PoE) like a single umbilical cord on a space station. An astronaut floating outside doesn't need two separate bulky cables—one for oxygen (**Data**) and one for electricity (**Power**). A single composite cable delivers both! A PoE switch feeds both gigabit network connectivity and electrical current over the exact same copper Ethernet cable to power security cameras and Wi-Fi access points on high ceilings with no AC wall outlets!",
        theory_sections=[
            {
                "heading": "PoE Architecture: PSE vs PD",
                "body": "Power over Ethernet (PoE) transmits direct current (DC) electrical power alongside standard Ethernet data over twisted-pair Cat5e/Cat6 cabling. The device supplying power is the **PSE (Power Sourcing Equipment)** (e.g. a PoE-capable switch or inline midspan injector). The device receiving power is the **PD (Powered Device)** (e.g. IP phones, PTZ security cameras, wireless APs, smart lighting)."
            },
            {
                "heading": "PoE Standards Evolution & Power Wattage",
                "body": "(1) **802.3af (PoE)**: Up to 15.4W at PSE (~12.95W at PD), powers basic VoIP phones and static cameras; (2) **802.3at (PoE+)**: Up to 30W at PSE (~25.5W at PD), powers dual-band Wi-Fi 6 APs and PTZ cameras; (3) **802.3bt (PoE++ / 4PPoE)**: Uses all 4 twisted pairs. Type 3 delivers up to 60W; Type 4 delivers up to 90W to 100W, powering digital signage displays, POS terminals, and thin clients."
            }
        ],
        code_snippets=[
            {
                "title": "IEEE PoE Standards Comparison Table",
                "language": "text",
                "code": "Standard     Common Name   Max Power at Switch (PSE)  Max Power at Device (PD)  Cable Wire Pairs Used\n802.3af      PoE           15.4 Watts                 12.95 Watts               2 Pairs (12 & 36 or 45 & 78)\n802.3at      PoE+          30.0 Watts                 25.5 Watts                2 Pairs\n802.3bt T3   PoE++ (4PPoE) 60.0 Watts                 51.0 Watts                4 Pairs (All 8 wires)\n802.3bt T4   PoE++ (High)  90.0 - 100.0 Watts         71.3 Watts                4 Pairs (All 8 wires)",
                "explanation": "Reference chart contrasting standard names, power deliveries, and physical wire utilization."
            },
            {
                "title": "Checking PoE Power Allocation and Budget on Cisco Switch",
                "language": "text",
                "code": "Switch# show power inline\nAvailable: 370.0(w)  Used: 46.2(w)  Remaining: 323.8(w)\n\nInterface Admin  Oper       Power(Watts) Device              Class\n--------- ------ ---------- ------------ ------------------- -----\nFa0/1     auto   on         15.4         Cisco IP Phone 7960 3\nFa0/2     auto   on         30.8         Meraki MR56 AP      4\nFa0/3     auto   off        0.0          n/a                 n/a",
                "explanation": "Displays total switch PoE budget, consumption per interface, device type, and power class."
            },
            {
                "title": "Disabling or Limiting PoE on a Switch Port",
                "language": "text",
                "code": "-- Disable electrical power on a specific port for security or power cycling\nSwitch(config)# interface FastEthernet0/1\nSwitch(config-if)# power inline never\n\n-- Restore automatic power detection\nSwitch(config-if)# power inline auto",
                "explanation": "Controls power delivery per port, enabling remote device reboots without visiting physical equipment."
            },
            {
                "title": "Python PoE Budget Overdraft Safety Checker",
                "language": "python",
                "code": "def check_poe_capacity(switch_budget_watts: float, connected_devices: list[float]) -> dict:\n    total_requested = sum(connected_devices)\n    remaining = switch_budget_watts - total_requested\n    return {\n        'budget_watts': switch_budget_watts,\n        'consumed_watts': total_requested,\n        'remaining_watts': round(remaining, 1),\n        'is_overdrawn': remaining < 0\n    }",
                "explanation": "Calculates power consumption against switch power supply limits to prevent brownouts."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="PoE Standard Classifier",
            description="Write a Python function `get_poe_standard_for_watts(device_watts: float) -> str` that returns `'802.3af (PoE)'` if `device_watts <= 12.95`, `'802.3at (PoE+)'` if `device_watts <= 25.5`, `'802.3bt (PoE++)'` if `device_watts <= 71.3`, and `'Exceeds Standard PoE'` otherwise.",
            starter_code="def get_poe_standard_for_watts(device_watts: float) -> str:\n    # Return required PoE standard\n    pass",
            solution_code="def get_poe_standard_for_watts(device_watts: float) -> str:\n    if device_watts <= 12.95:\n        return '802.3af (PoE)'\n    elif device_watts <= 25.5:\n        return '802.3at (PoE+)'\n    elif device_watts <= 71.3:\n        return '802.3bt (PoE++)'\n    return 'Exceeds Standard PoE'",
            expected_output="get_poe_standard_for_watts(10.0) == '802.3af (PoE)', get_poe_standard_for_watts(20.0) == '802.3at (PoE+)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary advantage of Power over Ethernet (PoE) in network engineering?",
                options=[
                    "It delivers both DC electrical power and data over a single standard Ethernet cable, eliminating the need for AC electrical outlets at device locations",
                    "It makes the internet connection wireless",
                    "It triples the CPU speed of laptops",
                    "It converts AC power into solar energy"
                ],
                correct_answer="It delivers both DC electrical power and data over a single standard Ethernet cable, eliminating the need for AC electrical outlets at device locations",
                explanation="PoE powers remote devices (cameras, APs, phones) through existing network cables without local wall outlets."
            ),
            QuizQuestionBlueprint(
                question="In PoE terminology, what is a 'PSE' (Power Sourcing Equipment)?",
                options=[
                    "The device (such as a PoE switch or midspan injector) that injects and supplies electrical power onto the cable",
                    "The battery inside an IP phone",
                    "The user's laptop screen",
                    "The network cable tester"
                ],
                correct_answer="The device (such as a PoE switch or midspan injector) that injects and supplies electrical power onto the cable",
                explanation="The PSE provides the DC power; the PD (Powered Device) consumes it."
            ),
            QuizQuestionBlueprint(
                question="What is the maximum power delivered by the IEEE 802.3at (PoE+) standard at the switch port (PSE)?",
                options=[
                    "30.0 Watts",
                    "15.4 Watts",
                    "90.0 Watts",
                    "5.0 Watts"
                ],
                correct_answer="30.0 Watts",
                explanation="802.3at (PoE+) supplies up to 30W at the PSE (~25.5W at the PD)."
            ),
            QuizQuestionBlueprint(
                question="Which modern PoE standard utilizes all 4 twisted pairs in an Ethernet cable to deliver up to 90W-100W for PTZ cameras and digital displays?",
                options=[
                    "IEEE 802.3bt (PoE++ / 4PPoE)",
                    "IEEE 802.3af",
                    "IEEE 802.3at",
                    "IEEE 802.11ax"
                ],
                correct_answer="IEEE 802.3bt (PoE++ / 4PPoE)",
                explanation="802.3bt uses all four pairs (4PPoE) to deliver high power up to 90W-100W."
            ),
            QuizQuestionBlueprint(
                question="What Cisco IOS command displays the total inline power budget and per-port power consumption on a switch?",
                options=[
                    "show power inline",
                    "show electricity status",
                    "display wattage all",
                    "show battery life"
                ],
                correct_answer="show power inline",
                explanation="`show power inline` displays the global switch power budget and wattage allocated per interface."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 21
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21 (Project): Campus Switching Lab (VLANs, STP & Trunking)",
        concept="Engineering a resilient campus access and distribution layer: Multi-VLAN configuration, 802.1Q Trunks, Rapid-PVST Root Bridge optimization, and PortFast security",
        analogy="Think of this project like architecting the entire internal communication and security framework for a modern university campus. You are laying out separate digital floors for Administration, Students, Faculty, and Voice/Video. You configure optical bridge highways between campus towers, set up automated flood barriers so network loops never cause blackouts, and test failover under live simulation!",
        theory_sections=[
            {
                "heading": "Module 4 Capstone Architecture",
                "body": "In this project, you construct a complete campus switching infrastructure uniting two distribution switches (Core-A, Core-B) and two access switches (Access-1, Access-2). You will implement: (1) Creating VLAN 10 (Faculty), VLAN 20 (Students), VLAN 30 (Management), and VLAN 99 (Native); (2) Configuring 802.1Q trunks with native VLAN protection; (3) Designing a predictable Spanning Tree root election using Rapid-PVST; (4) Hardening access ports with PortFast and BPDU Guard."
            },
            {
                "heading": "Spanning Tree Deterministic Engineering",
                "body": "Never leave Root Bridge election to random chance (default 32768 priority). In enterprise campus networks, Core-A is designated as Primary Root for odd VLANs and Secondary Root for even VLANs (VLAN load balancing), optimizing link utilization across redundant distribution trunks."
            }
        ],
        code_snippets=[
            {
                "title": "Campus Core Switch Configuration Script (Core-A.cfg)",
                "language": "text",
                "code": "-- Step 1: Create Campus VLANs\nSwitch(config)# hostname Core-A\nCore-A(config)# vlan 10,20,30,99\nCore-A(config-vlan)# exit\n\n-- Step 2: Configure Core-A as Primary Root for VLAN 10, Secondary for 20\nCore-A(config)# spanning-tree mode rapid-pvst\nCore-A(config)# spanning-tree vlan 10,30 priority 4096\nCore-A(config)# spanning-tree vlan 20 priority 8192\n\n-- Step 3: Configure Trunks to Access Switches\nCore-A(config)# interface range GigabitEthernet0/1 - 2\nCore-A(config-if-range)# switchport trunk encapsulation dot1q\nCore-A(config-if-range)# switchport mode trunk\nCore-A(config-if-range)# switchport trunk native vlan 99\nCore-A(config-if-range)# switchport trunk allowed vlan 10,20,30,99",
                "explanation": "Configures core campus VLANs, deterministic Spanning Tree root priorities, and 802.1Q distribution trunks."
            },
            {
                "title": "Campus Access Switch Hardening Script (Access-1.cfg)",
                "language": "text",
                "code": "Switch(config)# hostname Access-1\nAccess-1(config)# spanning-tree mode rapid-pvst\n\n-- Configure User Ports with PortFast & BPDU Guard Protection\nAccess-1(config)# interface range FastEthernet0/1 - 12\nAccess-1(config-if-range)# switchport mode access\nAccess-1(config-if-range)# switchport access vlan 20\nAccess-1(config-if-range)# spanning-tree portfast\nAccess-1(config-if-range)# spanning-tree bpduguard enable\nAccess-1(config-if-range)# no shutdown",
                "explanation": "Enforces port isolation on student ports and prevents unauthorized switch attachments using BPDU Guard."
            },
            {
                "title": "Comprehensive Campus Switching Verification Commands",
                "language": "text",
                "code": "Access-1# show vlan brief\nAccess-1# show interfaces trunk\nAccess-1# show spanning-tree vlan 20\n# Verifies that Access-1 Root Port points directly to Core-A with 0 blocked ports",
                "explanation": "Diagnostic suite confirming correct VLAN assignments, trunk active status, and loop-free topology."
            },
            {
                "title": "Python Campus Network Inventory Validator",
                "language": "python",
                "code": "def audit_campus_switch(vlan_dict: dict, trunk_allowed: list[int], native_vlan: int) -> list[str]:\n    warnings = []\n    if native_vlan == 1:\n        warnings.append('Security Risk: Native VLAN 1 in use! Change to unused VLAN (e.g. 99)')\n    for required in [10, 20, 30]:\n        if required not in trunk_allowed:\n            warnings.append(f'Missing required campus VLAN {required} on trunk!')\n    return warnings",
                "explanation": "Automated security audit script detecting misconfigured native VLANs or missing trunk allocations."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Campus Switch Configuration Auditor",
            description="Write a Python function `audit_trunk_security(native_vlan: int, allowed_vlans: list[int]) -> bool` that returns `True` if `native_vlan != 1` (default VLAN 1 changed for security) and `allowed_vlans` contains at least 3 distinct VLANs.",
            starter_code="def audit_trunk_security(native_vlan: int, allowed_vlans: list[int]) -> bool:\n    # Return True if trunk security configuration passes\n    pass",
            solution_code="def audit_trunk_security(native_vlan: int, allowed_vlans: list[int]) -> bool:\n    return native_vlan != 1 and len(set(allowed_vlans)) >= 3",
            expected_output="audit_trunk_security(99, [10, 20, 30]) == True, audit_trunk_security(1, [10, 20, 30]) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why should the default Native VLAN 1 be changed to an unused VLAN ID (like VLAN 99 or 999) on all trunk links?",
                options=[
                    "To prevent Double-Tagging VLAN Hopping security attacks where crafted frames bypass Layer 3 routing barriers",
                    "Because VLAN 1 consumes 10x more electricity",
                    "Because VLAN 1 is restricted to printers only",
                    "It is mandatory by international law"
                ],
                correct_answer="To prevent Double-Tagging VLAN Hopping security attacks where crafted frames bypass Layer 3 routing barriers",
                explanation="Changing the native VLAN mitigates double-tagging VLAN hopping attacks on 802.1Q trunks."
            ),
            QuizQuestionBlueprint(
                question="What happens if a user accidentally connects an unauthorized rogue switch into an edge port configured with `spanning-tree bpduguard enable`?",
                options=[
                    "The port immediately receives a BPDU, enters the `err-disable` state, and shuts down to protect the network from unauthorized loops",
                    "The rogue switch is promoted to network administrator",
                    "The entire campus loses power",
                    "The rogue switch is reformatted"
                ],
                correct_answer="The port immediately receives a BPDU, enters the `err-disable` state, and shuts down to protect the network from unauthorized loops",
                explanation="BPDU Guard puts access ports into err-disable if an unexpected BPDU frame arrives from a foreign switch."
            ),
            QuizQuestionBlueprint(
                question="In Spanning Tree engineering, why do network designers set Core-A to priority 4096 and Core-B to priority 8192?",
                options=[
                    "To deterministically ensure Core-A is Primary Root and Core-B smoothly assumes Root duties if Core-A fails",
                    "Because odd numbers are forbidden in Cisco IOS",
                    "To speed up hard drive access",
                    "To enable Wi-Fi on core switches"
                ],
                correct_answer="To deterministically ensure Core-A is Primary Root and Core-B smoothly assumes Root duties if Core-A fails",
                explanation="Explicit priorities guarantee deterministic primary and secondary Root Bridge placement."
            ),
            QuizQuestionBlueprint(
                question="What command on Cisco IOS configures an interface range to belong to VLAN 20?",
                options=[
                    "switchport access vlan 20",
                    "set vlan 20",
                    "vlan 20 activate",
                    "assign vlan 20"
                ],
                correct_answer="switchport access vlan 20",
                explanation="`switchport access vlan <id>` assigns static access interfaces to the designated VLAN."
            ),
            QuizQuestionBlueprint(
                question="What protocol should be enabled across all modern campus switches to replace legacy 802.1D STP for sub-second failover?",
                options=[
                    "Rapid-PVST+ (802.1w)",
                    "RIPv1",
                    "Telnet",
                    "TFTP"
                ],
                correct_answer="Rapid-PVST+ (802.1w)",
                explanation="Rapid-PVST+ provides sub-second spanning-tree convergence per VLAN."
            )
        ],
        is_project_day=True,
        project_name="Campus Switching Architecture Capstone Lab"
    ),

    # -------------------------------------------------------------
    # DAY 22
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Routing Fundamentals & The Routing Table",
        concept="The decision engine of Layer 3: Longest Prefix Match (LPM), Administrative Distance (AD), Routing Metrics, and the IP Routing Table structure",
        analogy="Think of a router like an air traffic controller at an international airport. Planes arrive with luggage tags indicating final destinations like 'Berlin, Germany' (**Destination IP**). The controller doesn't ask the plane 'how did you get here?'. The controller consults a flight destination ledger (**Routing Table**). If there are two routes to Germany, the controller picks the most specific airport route (**Longest Prefix Match**) and the most reputable airline (**Administrative Distance**)!",
        theory_sections=[
            {
                "heading": "How a Router Forwards Packets",
                "body": "When a router receives an Ethernet frame: (1) It decapsulates the Layer 2 frame, inspecting the destination MAC (which must match the router's own interface); (2) It verifies the IP header checksum and decrements the **Time-To-Live (TTL)** by 1 (dropping the packet if TTL=0 with an ICMP Time Exceeded); (3) It searches its **IP Routing Table** for the destination IP address; (4) It re-encapsulates the packet into a new Layer 2 frame with the next-hop MAC and transmits it out the exit interface."
            },
            {
                "heading": "Longest Prefix Match & Administrative Distance",
                "body": "**Longest Prefix Match (LPM)** is the universal routing decision rule: if an IP matches both `10.0.0.0/8` and `10.1.1.0/24`, the router ALWAYS selects `/24` because it is the most specific. When two different routing protocols advertise the exact same network prefix, the router uses **Administrative Distance (AD)** (the believability of the route source, lowest number wins): Connected (0), Static (1), eBGP (20), EIGRP (90), OSPF (110), RIP (120)."
            }
        ],
        code_snippets=[
            {
                "title": "Administrative Distance (AD) Hierarchy Reference Table",
                "language": "text",
                "code": "Route Source               Default Administrative Distance (AD)\nDirectly Connected (C)     0 (Most Trusted)\nStatic Route (S)           1\nExternal BGP (eBGP)        20\nEIGRP (Internal) (D)       90\nOSPF (O)                   110\nIS-IS                      115\nRIP (R)                    120\nInternal BGP (iBGP)        200\nUnknown / Unreachable      255 (Untrusted / Ignored)",
                "explanation": "Hierarchy of route trust: lower Administrative Distance takes precedence when identical prefixes are learned."
            },
            {
                "title": "Inspecting the IP Routing Table on a Cisco Router",
                "language": "text",
                "code": "Router# show ip route\nGateway of last resort is 198.51.100.1 to network 0.0.0.0\n\nC    192.168.1.0/24 is directly connected, GigabitEthernet0/0/0\nS    10.0.0.0/8 [1/0] via 172.16.1.1\nO    172.16.0.0/16 [110/2] via 192.168.1.254, 00:14:22, GigabitEthernet0/0/0\nS*   0.0.0.0/0 [1/0] via 198.51.100.1\n# [110/2] represents [Administrative Distance 110 / Metric Cost 2]",
                "explanation": "Decodes routing table entries, showing source code, prefix, AD, metric, next-hop, and exit interface."
            },
            {
                "title": "Inspecting Routing Table in Linux Kernel",
                "language": "bash",
                "code": "# Show IPv4 kernel routing table with metrics\nip route show\n# default via 192.168.1.1 dev eth0 proto dhcp metric 100\n# 192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.105 metric 100",
                "explanation": "Displays Linux kernel network routing table, default gateways, and metric weights."
            },
            {
                "title": "Longest Prefix Match Simulator in Python",
                "language": "python",
                "code": "import ipaddress\n\ndef longest_prefix_match(dest_ip_str: str, routes: list[str]) -> str:\n    dest_ip = ipaddress.ip_address(dest_ip_str)\n    matching_routes = []\n    for r in routes:\n        net = ipaddress.ip_network(r)\n        if dest_ip in net:\n            matching_routes.append(net)\n    if not matching_routes:\n        return 'No route to host (Drop)'\n    # LPM: Highest prefix length wins!\n    best_route = max(matching_routes, key=lambda n: n.prefixlen)\n    return str(best_route)\n\nprint(longest_prefix_match('10.1.1.5', ['10.0.0.0/8', '10.1.0.0/16', '10.1.1.0/24']))\n# Output: 10.1.1.0/24 (Most specific prefix wins!)",
                "explanation": "Implements the core Longest Prefix Match algorithm used by all hardware and software routers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Administrative Distance Comparator",
            description="Write a Python function `pick_preferred_route(protocol_a: str, protocol_b: str) -> str` that compares two routing protocol names from `['STATIC', 'EIGRP', 'OSPF', 'RIP']` and returns the name of the protocol with the lower (more preferred) Administrative Distance. ADs: Static=1, EIGRP=90, OSPF=110, RIP=120.",
            starter_code="def pick_preferred_route(protocol_a: str, protocol_b: str) -> str:\n    # Return preferred protocol name\n    pass",
            solution_code="def pick_preferred_route(protocol_a: str, protocol_b: str) -> str:\n    ad_map = {'STATIC': 1, 'EIGRP': 90, 'OSPF': 110, 'RIP': 120}\n    pa = protocol_a.strip().upper()\n    pb = protocol_b.strip().upper()\n    return pa if ad_map.get(pa, 255) <= ad_map.get(pb, 255) else pb",
            expected_output="pick_preferred_route('OSPF', 'EIGRP') == 'EIGRP', pick_preferred_route('RIP', 'STATIC') == 'STATIC'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the golden rule used by a router to select the winning path when a destination IP matches multiple routes in its routing table?",
                options=[
                    "Longest Prefix Match (LPM) - the route with the most specific (longest) prefix length is always chosen",
                    "Shortest subnet mask",
                    "Alphabetical order of interface names",
                    "Random selection"
                ],
                correct_answer="Longest Prefix Match (LPM) - the route with the most specific (longest) prefix length is always chosen",
                explanation="Longest Prefix Match dictates that the most specific subnet mask always wins packet routing decisions."
            ),
            QuizQuestionBlueprint(
                question="What does Administrative Distance (AD) measure in Cisco routing?",
                options=[
                    "The trustworthiness and believability of the route source (lowest number wins)",
                    "The physical length of the fiber optic cable in kilometers",
                    "The price of the router",
                    "The speed of the processor in megahertz"
                ],
                correct_answer="The trustworthiness and believability of the route source (lowest number wins)",
                explanation="AD ranks route sources by reliability (e.g. Connected=0, Static=1, OSPF=110)."
            ),
            QuizQuestionBlueprint(
                question="What action does a router take on the IP header of a packet before forwarding it out the next-hop interface?",
                options=[
                    "It decrements the Time-To-Live (TTL) field by 1 and recalculates the header checksum",
                    "It doubles the packet size",
                    "It converts IPv4 into IPv6",
                    "It erases the destination IP address"
                ],
                correct_answer="It decrements the Time-To-Live (TTL) field by 1 and recalculates the header checksum",
                explanation="Routers decrement TTL by 1 to prevent endless loops; if TTL reaches 0, the packet is discarded."
            ),
            QuizQuestionBlueprint(
                question="What is the default Administrative Distance of an Open Shortest Path First (OSPF) route?",
                options=[
                    "110",
                    "90",
                    "120",
                    "1"
                ],
                correct_answer="110",
                explanation="OSPF has a standard default Administrative Distance of 110."
            ),
            QuizQuestionBlueprint(
                question="What is the 'Gateway of Last Resort' (Default Route `0.0.0.0/0`) used for?",
                options=[
                    "Forwarding all packets whose destination IP addresses do not match any specific entry in the routing table (e.g. Internet traffic)",
                    "Shutting down the router",
                    "Erasing the flash memory",
                    "Sending emails"
                ],
                correct_answer="Forwarding all packets whose destination IP addresses do not match any specific entry in the routing table (e.g. Internet traffic)",
                explanation="The default route (0.0.0.0/0) matches all unlisted destination IPs, forwarding them toward the ISP."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Static Routing vs Dynamic Routing",
        concept="Engineering path selection: Standard static routes, Default static routes (`0.0.0.0/0`), Floating static routes (backup routes with higher AD), and Dynamic routing protocols",
        analogy="Think of routing like planning a road trip from Karachi to Lahore. A **Static Route** is printing out a fixed, unchanging paper map and writing: 'Always take Highway N-5 at Exit 12.' It requires zero brainpower from the car (**low CPU/bandwidth**), but if Highway N-5 collapses from a flood, your car stops dead and refuses to move. A **Dynamic Routing Protocol** is Google Maps with live GPS satellite updates: it talks to other cars, detects traffic jams in seconds, and automatically steers you around road closures!",
        theory_sections=[
            {
                "heading": "Static Routing: Precision & Low Overhead",
                "body": "Static routes are manually entered by network administrators using `ip route <prefix> <mask> <next-hop>`. They consume zero router CPU or network bandwidth because routers exchange no routing update packets. Static routing is ideal for small networks, stub networks with a single exit path, and default internet gateways. However, manual maintenance becomes unmanageable as networks scale, and static routes cannot automatically reroute around link outages unless floating routes are configured."
            },
            {
                "heading": "Floating Static Routes: Disaster Recovery",
                "body": "A **Floating Static Route** is an inactive backup static route configured with a higher Administrative Distance (e.g. `AD = 130`) than the primary route (e.g. OSPF with `AD = 110`). As long as the primary link is alive, the floating route stays hidden from the routing table. The instant the primary link fails, the floating static route immediately surfaces into the routing table, restoring connectivity."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Standard and Default Static Routes (Cisco IOS)",
                "language": "text",
                "code": "-- Standard Static Route to Remote Branch Subnet via Next-Hop IP\nRouter(config)# ip route 10.50.0.0 255.255.0.0 192.168.1.2\n\n-- Default Static Route (Gateway of Last Resort) to ISP\nRouter(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1",
                "explanation": "Configures a specific static route to a branch office and a default route (0.0.0.0/0) to the ISP gateway."
            },
            {
                "title": "Configuring a Floating Static Backup Route",
                "language": "text",
                "code": "-- Primary path is learned via OSPF (Administrative Distance 110)\n-- Floating backup route configured with AD 130 pointing to cellular 4G backup:\nRouter(config)# ip route 10.50.0.0 255.255.0.0 198.51.100.2 130\n\n-- Verifying: Route 130 will NOT appear in 'show ip route' until primary fails!",
                "explanation": "Assigns an administrative distance of 130, ensuring the route remains dormant until the primary link fails."
            },
            {
                "title": "Static vs Dynamic Routing Comparison Matrix",
                "language": "text",
                "code": "Feature                 Static Routing                   Dynamic Routing (OSPF/EIGRP/BGP)\nConfiguration           Manual per router                Automatic neighbor discovery\nTopology Scalability    Small networks (<10 routers)     Vast networks (thousands of routers)\nFailure Recovery        No automatic reroute             Sub-second automatic convergence\nRouter Resource Usage   Zero CPU/RAM overhead            Consumes CPU/RAM to compute trees\nNetwork Bandwidth       Zero overhead (No update msgs)   Exchanges periodic hello/LSA packets",
                "explanation": "Contrasts administrative overhead, failure convergence, resource utilization, and scalability."
            },
            {
                "title": "Python Script: Adding Persistent Static Route on Linux",
                "language": "python",
                "code": "import subprocess\n\ndef add_linux_static_route(subnet: str, gateway: str, interface: str):\n    cmd = f'ip route add {subnet} via {gateway} dev {interface}'\n    result = subprocess.run(cmd.split(), capture_output=True, text=True)\n    if result.returncode == 0:\n        print(f'Successfully installed static route: {subnet} via {gateway}')\n    else:\n        print(f'Error adding route: {result.stderr.strip()}')",
                "explanation": "Automates injection of static IP routes into the Linux kernel routing table."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Static Route CLI Generator",
            description="Write a Python function `build_cisco_static_route(network: str, mask: str, next_hop: str, ad: int = 1) -> str` that produces a valid Cisco IOS `ip route <network> <mask> <next_hop> [ad]` command string (omitting `ad` if `ad == 1`).",
            starter_code="def build_cisco_static_route(network: str, mask: str, next_hop: str, ad: int = 1) -> str:\n    # Generate Cisco static route command\n    pass",
            solution_code="def build_cisco_static_route(network: str, mask: str, next_hop: str, ad: int = 1) -> str:\n    if ad != 1:\n        return f\"ip route {network} {mask} {next_hop} {ad}\"\n    return f\"ip route {network} {mask} {next_hop}\"",
            expected_output="build_cisco_static_route('10.0.0.0', '255.0.0.0', '192.168.1.1') == 'ip route 10.0.0.0 255.0.0.0 192.168.1.1'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'Default Static Route' in IPv4 represented by in CIDR notation?",
                options=[
                    "0.0.0.0/0 (with mask 0.0.0.0)",
                    "255.255.255.255/32",
                    "127.0.0.1/8",
                    "192.168.1.1/24"
                ],
                correct_answer="0.0.0.0/0 (with mask 0.0.0.0)",
                explanation="0.0.0.0/0 matches any destination IP address with 0 matching bits required."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Floating Static Route'?",
                options=[
                    "A backup static route configured with a higher Administrative Distance than the primary route so it only becomes active if the primary route fails",
                    "A route used on cruise ships",
                    "A route that changes its IP address every 5 minutes",
                    "A route that floats in computer RAM"
                ],
                correct_answer="A backup static route configured with a higher Administrative Distance than the primary route so it only becomes active if the primary route fails",
                explanation="Floating static routes use elevated ADs to remain dormant until primary routes disappear."
            ),
            QuizQuestionBlueprint(
                question="What is a major advantage of Static Routing over Dynamic Routing protocols?",
                options=[
                    "It consumes zero router CPU/memory to calculate shortest paths and sends no periodic routing updates over the wire",
                    "It automatically reroutes around fiber optic cuts",
                    "It works without routers",
                    "It supports millions of routes automatically"
                ],
                correct_answer="It consumes zero router CPU/memory to calculate shortest paths and sends no periodic routing updates over the wire",
                explanation="Static routes require no CPU path calculations and generate zero routing protocol network traffic."
            ),
            QuizQuestionBlueprint(
                question="What is the default Administrative Distance of a standard static route in Cisco IOS?",
                options=[
                    "1",
                    "0",
                    "110",
                    "90"
                ],
                correct_answer="1",
                explanation="Static routes have an Administrative Distance of 1, second only to directly connected interfaces (0)."
            ),
            QuizQuestionBlueprint(
                question="What happens in a large enterprise network with 500 routers if administrators rely solely on static routing?",
                options=[
                    "Configuration complexity becomes unmanageable, and every single link failure requires manual administrative intervention to fix",
                    "The network runs 100x faster",
                    "The routers become self-healing",
                    "The switches stop using MAC addresses"
                ],
                correct_answer="Configuration complexity becomes unmanageable, and every single link failure requires manual administrative intervention to fix",
                explanation="Static routing cannot scale to large networks because manual adjustments are required for topology changes."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 24
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Inter-VLAN Routing (Router-on-a-Stick & Layer 3 Switches)",
        concept="Bridging isolated broadcast domains: Sub-interfaces, 802.1Q encapsulation on routers, Switched Virtual Interfaces (SVIs), and Layer 3 hardware routing",
        analogy="Think of VLANs like two separate islands separated by water (Island 10 and Island 20). If residents on Island 10 want to send letters to Island 20, they cannot walk across the water (**Layer 2 isolation**). In **Router-on-a-Stick (ROAS)**, a ferry boat (**single trunk cable**) picks up mail, travels to a mainland customs office (**Router**), checks tariffs, and ferries it back to Island 20. In a **Layer 3 Switch**, an underground supersonic tunnel (**hardware SVI**) connects the islands directly in 1 millisecond!",
        theory_sections=[
            {
                "heading": "Router-on-a-Stick (ROAS) Architecture",
                "body": "In small-to-medium networks, a single physical router interface connects to a switch trunk port. The router divides the physical interface into virtual **sub-interfaces** (e.g. `Gig0/0/0.10` and `Gig0/0/0.20`). Each sub-interface is bound to a specific VLAN using `encapsulation dot1Q <vlan_id>` and assigned an IP address that serves as the Default Gateway for that VLAN."
            },
            {
                "heading": "Layer 3 Switches & Switched Virtual Interfaces (SVIs)",
                "body": "In modern enterprise networks, routing all internal VLAN traffic through a single physical router creates an architectural bottleneck ('hairpinning'). **Multilayer / Layer 3 Switches** route traffic internally at hardware wire speeds (millions of packets per second using ASIC chips) via **Switched Virtual Interfaces (SVIs)** (`interface vlan 10`)."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Router-on-a-Stick (ROAS) Sub-Interfaces (Cisco IOS)",
                "language": "text",
                "code": "-- Bring up physical interface with NO IP address\nRouter(config)# interface GigabitEthernet0/0/0\nRouter(config-if)# no shutdown\n\n-- Sub-interface for VLAN 10 (Accounting Gateway)\nRouter(config)# interface GigabitEthernet0/0/0.10\nRouter(config-subif)# encapsulation dot1Q 10\nRouter(config-subif)# ip address 192.168.10.1 255.255.255.0\n\n-- Sub-interface for VLAN 20 (Engineering Gateway)\nRouter(config)# interface GigabitEthernet0/0/0.20\nRouter(config-subif)# encapsulation dot1Q 20\nRouter(config-subif)# ip address 192.168.20.1 255.255.255.0",
                "explanation": "Creates virtual sub-interfaces with 802.1Q tags that serve as default gateways for each VLAN."
            },
            {
                "title": "Configuring Layer 3 Switch Routing with SVIs (High Performance)",
                "language": "text",
                "code": "-- Enable IP routing engine in switch hardware\nSwitch(config)# ip routing\n\n-- Create Switched Virtual Interface (SVI) for VLAN 10\nSwitch(config)# interface vlan 10\nSwitch(config-if)# ip address 192.168.10.1 255.255.255.0\nSwitch(config-if)# no shutdown\n\n-- Create SVI for VLAN 20\nSwitch(config)# interface vlan 20\nSwitch(config-if)# ip address 192.168.20.1 255.255.255.0\nSwitch(config-if)# no shutdown",
                "explanation": "Enables hardware-accelerated wire-speed inter-VLAN routing directly on the multilayer switch."
            },
            {
                "title": "Converting a Switchport to a Routed Port (No VLANs)",
                "language": "text",
                "code": "-- Removes Layer 2 switching capabilities, turning port into a physical Layer 3 router port\nSwitch(config)# interface GigabitEthernet1/0/24\nSwitch(config-if)# no switchport\nSwitch(config-if)# ip address 10.1.1.2 255.255.255.252\nSwitch(config-if)# no shutdown",
                "explanation": "`no switchport` converts a switch port into a dedicated Layer 3 routed port connecting to upstream routers."
            },
            {
                "title": "Verifying Inter-VLAN Routing with Ping Across Subnets",
                "language": "text",
                "code": "PC-Accounting> ping 192.168.20.50\n# Pings from 192.168.10.50 (VLAN 10) to 192.168.20.50 (VLAN 20)\n# Packet flows: PC -> Switch Access -> Trunk -> Router Gateway -> Trunk -> Switch -> PC\nReply from 192.168.20.50: bytes=32 time=2ms TTL=127",
                "explanation": "Decremented TTL of 127 confirms that the packet traversed a Layer 3 routing hop between VLANs."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="ROAS Sub-Interface Command Builder",
            description="Write a Python function `build_roas_commands(parent_if: str, vlan_id: int, gateway_ip: str, mask: str) -> list[str]` that generates the 3 required Cisco IOS sub-interface commands (`interface <parent>.<vlan>`, `encapsulation dot1Q <vlan>`, `ip address <ip> <mask>`).",
            starter_code="def build_roas_commands(parent_if: str, vlan_id: int, gateway_ip: str, mask: str) -> list[str]:\n    # Generate sub-interface configuration lines\n    pass",
            solution_code="def build_roas_commands(parent_if: str, vlan_id: int, gateway_ip: str, mask: str) -> list[str]:\n    return [\n        f\"interface {parent_if}.{vlan_id}\",\n        f\"encapsulation dot1Q {vlan_id}\",\n        f\"ip address {gateway_ip} {mask}\"\n    ]",
            expected_output="build_roas_commands('Gig0/0', 10, '192.168.10.1', '255.255.255.0')[1] == 'encapsulation dot1Q 10'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is 'Router-on-a-Stick' (ROAS) in computer networking?",
                options=[
                    "A configuration where a single physical router interface connects to a switch trunk, routing inter-VLAN traffic via logical sub-interfaces",
                    "A router mounted on a wooden telephone pole",
                    "A wireless router with a single antenna",
                    "A router that only runs on battery power"
                ],
                correct_answer="A configuration where a single physical router interface connects to a switch trunk, routing inter-VLAN traffic via logical sub-interfaces",
                explanation="Router-on-a-Stick routes multiple VLANs across a single trunk link using sub-interfaces."
            ),
            QuizQuestionBlueprint(
                question="What command must be configured on a router sub-interface before an IP address can be assigned?",
                options=[
                    "encapsulation dot1Q <vlan_id>",
                    "switchport mode trunk",
                    "spanning-tree portfast",
                    "router ospf 1"
                ],
                correct_answer="encapsulation dot1Q <vlan_id>",
                explanation="Sub-interfaces require 802.1Q encapsulation mapping to bind them to a specific VLAN tag."
            ),
            QuizQuestionBlueprint(
                question="What is an SVI (Switched Virtual Interface) on a Layer 3 multilayer switch?",
                options=[
                    "A virtual Layer 3 routed interface tied to a specific VLAN (e.g. `interface vlan 10`) acting as that VLAN's default gateway",
                    "A virtual reality headset",
                    "A fake switch port that drops packets",
                    "A power supply emulator"
                ],
                correct_answer="A virtual Layer 3 routed interface tied to a specific VLAN (e.g. `interface vlan 10`) acting as that VLAN's default gateway",
                explanation="SVIs represent virtual router interfaces on multilayer switches, providing default gateways in hardware."
            ),
            QuizQuestionBlueprint(
                question="What command activates the Layer 3 routing engine on a Cisco Catalyst multilayer switch?",
                options=[
                    "ip routing",
                    "enable router",
                    "start layer3",
                    "routing on"
                ],
                correct_answer="ip routing",
                explanation="The global configuration command `ip routing` enables the IPv4 routing table engine on multilayer switches."
            ),
            QuizQuestionBlueprint(
                question="Why are Layer 3 switches preferred over Router-on-a-Stick in modern high-throughput campus networks?",
                options=[
                    "Layer 3 switches route packets directly in specialized ASIC hardware at wire speed, eliminating the single-cable ROAS bottleneck",
                    "Layer 3 switches are completely free",
                    "Router-on-a-Stick cannot support more than 2 computers",
                    "Layer 3 switches do not require cables"
                ],
                correct_answer="Layer 3 switches route packets directly in specialized ASIC hardware at wire speed, eliminating the single-cable ROAS bottleneck",
                explanation="Hardware ASIC switching eliminates the bandwidth bottleneck of funneling traffic through a single router trunk."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 25
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Distance Vector vs Link-State Routing Protocols",
        concept="Categorizing interior routing protocol algorithms: Routing by rumor vs Shortest Path First (Dijkstra), Bellman-Ford, metric calculations, and convergence behaviors",
        analogy="Think of routing algorithms like navigating a cross-country drive. **Distance Vector** is like asking people at roadside diners: 'Which way to Chicago?' The diner cook says: 'Drive east for 200 miles' (**Routing by Rumor**—you have no idea what roads look like beyond those 200 miles). **Link-State** is like having a complete satellite GPS roadmap of every single highway, bridge, and town in the entire country; your in-car computer runs Dijkstra's algorithm to calculate the perfect path yourself!",
        theory_sections=[
            {
                "heading": "Distance Vector: Routing by Rumor (Bellman-Ford)",
                "body": "Distance Vector protocols (e.g. RIP, IGRP) share their entire routing table only with directly connected immediate neighbors at periodic intervals. Routers learn paths 'by rumor' without possessing an end-to-end topological map of the entire autonomous system. Metrics are simple (e.g. Hop Count in RIP). Disadvantages: slow convergence, vulnerability to routing loops (count-to-infinity), and periodic broadcast overhead."
            },
            {
                "heading": "Link-State: Full Topological Awareness (Dijkstra SPF)",
                "body": "Link-State protocols (e.g. OSPF, IS-IS) flood **Link-State Advertisements (LSAs)** describing the state of their local interfaces. Every router builds an identical **Link-State Database (LSDB)** representing a complete map of the network. Each router independently executes **Dijkstra's Shortest Path First (SPF)** algorithm to construct a loop-free shortest path tree. Benefits: rapid convergence, scalable hierarchical areas, and zero count-to-infinity loops."
            }
        ],
        code_snippets=[
            {
                "title": "Distance Vector vs Link-State Comparison Matrix",
                "language": "text",
                "code": "Feature                 Distance Vector (RIPv2)          Link-State (OSPF / IS-IS)\nNetwork Knowledge       Knows only what neighbors say    Maintains complete topological map (LSDB)\nAlgorithm               Bellman-Ford                     Dijkstra's Shortest Path First (SPF)\nMetric                  Hop Count (Max 15 hops)          Cost (Bandwidth)\nConvergence Time        Slow (30 - 180 seconds)          Sub-second / instantaneous\nLoop Mitigation         Split Horizon, Poison Reverse    Inherently loop-free SPF tree\nMemory/CPU Overhead     Minimal                          Higher (calculates SPF tree in RAM)\nUpdate Mechanism        Periodic full table broadcasts   Triggered delta updates on link state change",
                "explanation": "Comprehensive reference contrasting architectural mechanics of Distance Vector and Link-State."
            },
            {
                "title": "Dijkstra's Shortest Path First (SPF) Algorithm in Python",
                "language": "python",
                "code": "import heapq\n\ndef dijkstra_spf(graph: dict, start_router: str) -> dict:\n    \"\"\"Calculates shortest cost path from start_router to all nodes\"\"\"\n    distances = {node: float('inf') for node in graph}\n    distances[start_router] = 0\n    queue = [(0, start_router)]\n    \n    while queue:\n        current_dist, current_node = heapq.heappop(queue)\n        if current_dist > distances[current_node]:\n            continue\n        for neighbor, weight in graph[current_node].items():\n            distance = current_dist + weight\n            if distance < distances[neighbor]:\n                distances[neighbor] = distance\n                heapq.heappush(queue, (distance, neighbor))\n    return distances\n\n# Network topology: R1 connected to R2 (cost 10) and R3 (cost 5)\ntopology = {\n    'R1': {'R2': 10, 'R3': 5},\n    'R2': {'R1': 10, 'R4': 1},\n    'R3': {'R1': 5,  'R4': 20},\n    'R4': {'R2': 1,  'R3': 20}\n}\nprint('Shortest Path from R1:', dijkstra_spf(topology, 'R1'))\n# Path R1 -> R2 -> R4 costs 11 (Beats R1 -> R3 -> R4 which costs 25!)",
                "explanation": "Demonstrates the exact Dijkstra shortest path tree calculation executed by OSPF routers."
            },
            {
                "title": "Split Horizon Rule (Loop Prevention in Distance Vector)",
                "language": "text",
                "code": "-- Split Horizon Rule:\n-- 'A router never advertises a route back out the same interface it learned it from.'\n-- Prevents two routers from bouncing unreachable route advertisements back and forth!",
                "explanation": "Explains Split Horizon, which prevents simple two-node routing loops in Distance Vector protocols."
            },
            {
                "title": "Triggered LSA Updates in Link-State Protocols",
                "language": "text",
                "code": "Router# debug ip ospf events\n# When a cable breaks, OSPF does NOT wait for a 30s timer!\n# It immediately floods a Link State Update (LSU) packet out all active interfaces,\n# prompting all routers to re-compute their SPF trees within milliseconds.",
                "explanation": "Illustrates how event-driven Link-State updates enable rapid convergence."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Routing Protocol Classifier",
            description="Write a Python function `classify_routing_protocol(proto: str) -> str` that maps `'RIP'` to `'Distance Vector'`, `'OSPF'` and `'IS-IS'` to `'Link-State'`, and `'BGP'` to `'Path Vector'`. Return `'Unknown'` for others.",
            starter_code="def classify_routing_protocol(proto: str) -> str:\n    # Return algorithm classification\n    pass",
            solution_code="def classify_routing_protocol(proto: str) -> str:\n    p = proto.strip().upper()\n    if p in ['RIP', 'RIPV1', 'RIPV2']:\n        return 'Distance Vector'\n    elif p in ['OSPF', 'IS-IS', 'ISIS']:\n        return 'Link-State'\n    elif p in ['BGP', 'EBGP', 'IBGP']:\n        return 'Path Vector'\n    return 'Unknown'",
            expected_output="classify_routing_protocol('OSPF') == 'Link-State', classify_routing_protocol('RIP') == 'Distance Vector'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What algorithm is used by Link-State routing protocols (such as OSPF and IS-IS) to calculate the shortest loop-free path?",
                options=[
                    "Dijkstra's Shortest Path First (SPF) algorithm",
                    "Bellman-Ford algorithm",
                    "Bubble Sort algorithm",
                    "RSA encryption algorithm"
                ],
                correct_answer="Dijkstra's Shortest Path First (SPF) algorithm",
                explanation="Link-state protocols build a full topological graph and run Dijkstra's algorithm to compute the best paths."
            ),
            QuizQuestionBlueprint(
                question="Why is Distance Vector routing often described as 'Routing by Rumor'?",
                options=[
                    "Because routers have no complete topological map; they only know what their immediate neighbors tell them about distances",
                    "Because it is an unverified conspiracy theory",
                    "Because it only runs on social media apps",
                    "Because it spreads computer viruses"
                ],
                correct_answer="Because routers have no complete topological map; they only know what their immediate neighbors tell them about distances",
                explanation="Routers learn second-hand distance and vector information without validating the full end-to-end topology."
            ),
            QuizQuestionBlueprint(
                question="What does the 'Split Horizon' loop-prevention rule state in Distance Vector routing?",
                options=[
                    "Information about a route should never be advertised back out the same interface through which it was learned",
                    "Routers must split packets into two halves",
                    "Routers can only operate during daylight hours",
                    "Subnets must be divided by two"
                ],
                correct_answer="Information about a route should never be advertised back out the same interface through which it was learned",
                explanation="Split Horizon prevents two routers from echoing unreachable route updates back and forth."
            ),
            QuizQuestionBlueprint(
                question="What metric does the Routing Information Protocol (RIP) use to measure distance?",
                options=[
                    "Hop Count (number of routers traversed, maximum 15)",
                    "Bandwidth / Link Speed",
                    "Cable thickness",
                    "Ping latency in milliseconds"
                ],
                correct_answer="Hop Count (number of routers traversed, maximum 15)",
                explanation="RIP measures route cost strictly by hop count; 16 hops is considered infinity (unreachable)."
            ),
            QuizQuestionBlueprint(
                question="What database is maintained by all OSPF routers in an area to represent an identical synchronized map of the network?",
                options=[
                    "LSDB (Link-State Database)",
                    "MAC Address Table",
                    "ARP Cache",
                    "DNS Registry"
                ],
                correct_answer="LSDB (Link-State Database)",
                explanation="The Link-State Database (LSDB) stores all Link-State Advertisements (LSAs), providing a map of the network."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: RIPv1 & RIPv2 (Routing Information Protocol)",
        concept="Deconstructing legacy Distance Vector: Hop count metric, 15-hop limit, 30-second periodic updates, Classful vs Classless (CIDR) differences, and Poison Reverse",
        analogy="Think of RIP like a town crier standing on a wooden box in the town square. Every 30 seconds, he rings a loud brass bell (**Periodic Update**) and shouts the entire town directory at the top of his lungs (**Full Table Broadcast**). He tells you: 'The blacksmith is 1 street away, the baker is 2 streets away.' But if a house is more than 15 streets away, the crier declares it in unreachable barbarian territory (**15 Hop Count Limit**)!",
        theory_sections=[
            {
                "heading": "RIP Mechanics & Hop Count Limitations",
                "body": "The Routing Information Protocol (RIP) is one of the oldest interior gateway routing protocols (RFC 1058 / RFC 2453). It uses **Hop Count** as its sole metric (each router crossed = 1 hop). The maximum allowed hop count is **15**; a metric of **16 is defined as unreachable (infinity)**. This strictly bounds RIP networks to small local implementations."
            },
            {
                "heading": "RIPv1 vs RIPv2: The Evolution to Classless Routing",
                "body": "**RIPv1** is classful: it does not send subnet masks in updates, broadcasts to `255.255.255.255`, and does not support VLSM or authentication. **RIPv2** is classless: it includes subnet masks in updates (enabling CIDR and VLSM), multicasts to `224.0.0.9` (reducing CPU interrupts on non-RIP hosts), and supports MD5 route authentication."
            }
        ],
        code_snippets=[
            {
                "title": "RIPv1 vs RIPv2 Key Architectural Differences",
                "language": "text",
                "code": "Feature                 RIPv1 (RFC 1058)             RIPv2 (RFC 2453)\nRouting Type            Classful                     Classless (Supports VLSM & CIDR)\nSubnet Mask in Update   NO (Assumes class A/B/C)     YES (Includes 32-bit mask)\nTransmission Method     Broadcast (255.255.255.255)  Multicast (224.0.0.9)\nAuthentication          None (Insecure)              Plaintext & MD5 Authentication\nRoute Summarization     Automatic at boundary only   Manual & Automatic Summarization",
                "explanation": "Summary matrix highlighting why RIPv2 replaced RIPv1 to support modern subnetting and security."
            },
            {
                "title": "Configuring RIPv2 on a Cisco Router",
                "language": "text",
                "code": "Router(config)# router rip\nRouter(config-router)# version 2\nRouter(config-router)# no auto-summary   -- CRITICAL: Disables classful boundary summarization!\nRouter(config-router)# network 192.168.1.0\nRouter(config-router)# network 10.0.0.0\nRouter(config-router)# passive-interface GigabitEthernet0/0/2 -- Suppresses updates on LAN ports",
                "explanation": "Enables RIPv2, disables legacy classful auto-summarization, and binds active networks."
            },
            {
                "title": "Verifying RIP Routes and Timers",
                "language": "text",
                "code": "Router# show ip route rip\nR    172.16.10.0/24 [120/2] via 192.168.1.2, 00:00:18, GigabitEthernet0/0/0\n# [120/2]: Administrative Distance 120, Metric is 2 Hops away\n\nRouter# show ip protocols\n  Routing Protocol is \"rip\"\n  Sending updates every 30 seconds, next due in 12 seconds\n  Invalid after 180 seconds, hold down 180, flushed after 240",
                "explanation": "Inspects learned RIP routes and verifies the 30-second update, 180-second invalid, and 240-second flush timers."
            },
            {
                "title": "Configuring MD5 Authentication for RIPv2",
                "language": "text",
                "code": "Router(config)# key chain RIP_KEY\nRouter(config-keychain)# key 1\nRouter(config-keychain-key)# key-string MySuperSecretKey\n\nRouter(config)# interface GigabitEthernet0/0/0\nRouter(config-if)# ip rip authentication mode md5\nRouter(config-if)# ip rip authentication key-chain RIP_KEY",
                "explanation": "Protects RIPv2 routing tables against rogue route injection using MD5 cryptographic hashes."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="RIP Metric Reachability Checker",
            description="Write a Python function `is_rip_reachable(current_hops: int) -> bool` that returns `True` if a route can be reached via RIP (`current_hops < 16`), and `False` if unreachable (`>= 16`).",
            starter_code="def is_rip_reachable(current_hops: int) -> bool:\n    # Return True if reachable in RIP\n    pass",
            solution_code="def is_rip_reachable(current_hops: int) -> bool:\n    return 0 <= current_hops < 16",
            expected_output="is_rip_reachable(14) == True, is_rip_reachable(15) == True, is_rip_reachable(16) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the maximum allowable hop count for a reachable route in the Routing Information Protocol (RIP)?",
                options=[
                    "15 hops (16 represents infinity / unreachable)",
                    "255 hops",
                    "100 hops",
                    "3 hops"
                ],
                correct_answer="15 hops (16 represents infinity / unreachable)",
                explanation="RIP defines 15 hops as the maximum valid diameter; a hop count of 16 indicates an unreachable network."
            ),
            QuizQuestionBlueprint(
                question="What multicast IPv4 address does RIPv2 use to send periodic routing updates to neighbor routers?",
                options=[
                    "224.0.0.9",
                    "224.0.0.5",
                    "255.255.255.255",
                    "192.168.1.255"
                ],
                correct_answer="224.0.0.9",
                explanation="RIPv2 uses dedicated multicast address 224.0.0.9, preventing non-RIP hosts from processing updates."
            ),
            QuizQuestionBlueprint(
                question="Why is `no auto-summary` an essential configuration command when configuring RIPv2 in modern networks?",
                options=[
                    "It stops the router from summarizing subnets back into classful Class A, B, or C boundaries, allowing VLSM to function properly",
                    "It disables passwords",
                    "It deletes all routes",
                    "It turns the router into a switch"
                ],
                correct_answer="It stops the router from summarizing subnets back into classful Class A, B, or C boundaries, allowing VLSM to function properly",
                explanation="`no auto-summary` prevents RIPv2 from collapsing discontiguous subnets to classful boundaries."
            ),
            QuizQuestionBlueprint(
                question="How often does a RIP router broadcast its full routing table to its neighbors by default?",
                options=[
                    "Every 30 seconds",
                    "Every 5 seconds",
                    "Every 24 hours",
                    "Only when links go down"
                ],
                correct_answer="Every 30 seconds",
                explanation="The default RIP periodic update timer transmits the full routing table every 30 seconds."
            ),
            QuizQuestionBlueprint(
                question="What is the Administrative Distance (AD) of RIP in the routing table?",
                options=[
                    "120",
                    "110",
                    "90",
                    "1"
                ],
                correct_answer="120",
                explanation="RIP routes are assigned an Administrative Distance of 120."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: EIGRP (Enhanced Interior Gateway Routing Protocol)",
        concept="Cisco's advanced distance vector protocol: DUAL algorithm, composite metric (Bandwidth & Delay), Feasible Distance vs Reported Distance, and unequal-cost load balancing",
        analogy="Think of EIGRP like an elite executive bodyguard escort team traveling in a presidential motorcade. Instead of waiting for a flat tire to happen and then searching the glovebox for a spare, the team designates an immediate backup vehicle driving right behind (**Feasible Successor**). The millisecond the lead car blows a tire, the bodyguard team instantly steps into the backup car with zero seconds of hesitation or delay (**DUAL zero-millisecond convergence**)!",
        theory_sections=[
            {
                "heading": "EIGRP: An Advanced Distance Vector Protocol",
                "body": "Originally proprietary to Cisco (now an open RFC), EIGRP combines the simplicity of Distance Vector with the fast convergence of Link-State. Instead of hop count, EIGRP calculates a **Composite Metric** based primarily on **Bandwidth** (slowest link along the path) and cumulative **Delay**. EIGRP does not send periodic full table dumps; it sends bounded, triggered updates only when network state changes."
            },
            {
                "heading": "The DUAL Finite State Machine (Successor vs Feasible Successor)",
                "body": "EIGRP uses the **Diffusing Update Algorithm (DUAL)** to guarantee loop-free convergence: (1) **Feasible Distance (FD)**: The lowest calculated metric to reach a destination; (2) **Reported/Advertised Distance (RD)**: The distance to destination as reported by an adjacent neighbor; (3) **Successor**: The primary best route installed in the routing table; (4) **Feasible Successor (FS)**: A pre-calculated backup path satisfying the **Feasibility Condition: `RD < FD`**. If the primary path dies, the FS is installed immediately with zero recalculation delay!"
            }
        ],
        code_snippets=[
            {
                "title": "EIGRP Composite Metric Formula Breakdown",
                "language": "text",
                "code": "Standard EIGRP Metric Formula (K1=1 Bandwidth, K3=1 Delay, K2=K4=K5=0):\nMetric = 256 * ( (10,000,000 / Least_Bandwidth_kbps) + (Cumulative_Delay_tens_of_usec) )\n\nExample:\nSlowest link in path = 100 Mbps (100,000 kbps)\nTotal delay = 2,000 microseconds (200 tens of usec)\nMetric = 256 * ( (10,000,000 / 100,000) + 200 ) = 256 * (100 + 200) = 76,800",
                "explanation": "Calculates EIGRP composite metric favoring high bandwidth and minimal cumulative delay."
            },
            {
                "title": "Configuring EIGRP on a Cisco Router",
                "language": "text",
                "code": "Router(config)# router eigrp 100          -- Autonomous System Number (Must match neighbors!)\nRouter(config-router)# no auto-summary\nRouter(config-router)# network 10.1.1.0 0.0.0.255   -- Wildcard mask\nRouter(config-router)# network 192.168.1.0 0.0.0.255\nRouter(config-router)# passive-interface GigabitEthernet0/0/2",
                "explanation": "Configures EIGRP with AS 100 using inverse wildcard masks to bind active interfaces."
            },
            {
                "title": "Inspecting EIGRP Topology Table and Feasible Successors",
                "language": "text",
                "code": "Router# show ip eigrp topology\nIP-EIGRP Topology Table for AS(100)/ID(10.1.1.1)\n\nP 10.2.2.0/24, 1 successors, FD is 30720\n        via 192.168.1.2 (30720/28160), GigabitEthernet0/0/0  -- Successor (Primary)\n        via 192.168.2.2 (35840/25600), GigabitEthernet0/0/1  -- Feasible Successor! (RD 25600 < FD 30720)",
                "explanation": "Validates the Feasibility Condition: Reported Distance 25600 is less than Feasible Distance 30720."
            },
            {
                "title": "Configuring Unequal-Cost Load Balancing with Variance",
                "language": "text",
                "code": "-- EIGRP is the ONLY routing protocol capable of unequal-cost load balancing!\nRouter(config-router)# variance 2\n# Installs routes whose metric is up to 2x the best metric into routing table simultaneously",
                "explanation": "Enables multi-path traffic balancing across links of varying bandwidth speeds."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="EIGRP Feasibility Condition Checker",
            description="Write a Python function `is_feasible_successor(fd: int, rd: int) -> bool` that verifies whether a backup route satisfies the EIGRP Feasibility Condition (`Reported Distance < Feasible Distance`).",
            starter_code="def is_feasible_successor(fd: int, rd: int) -> bool:\n    # Return True if RD < FD\n    pass",
            solution_code="def is_feasible_successor(fd: int, rd: int) -> bool:\n    return rd < fd",
            expected_output="is_feasible_successor(30720, 25600) == True, is_feasible_successor(30720, 35000) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What mathematical rule defines the EIGRP 'Feasibility Condition' to guarantee a backup route is completely loop-free?",
                options=[
                    "The neighbor's Reported Distance (RD) must be strictly less than the current Feasible Distance (FD): RD < FD",
                    "The hop count must be less than 15",
                    "The IP address must be an even number",
                    "The cable must be made of fiber optics"
                ],
                correct_answer="The neighbor's Reported Distance (RD) must be strictly less than the current Feasible Distance (FD): RD < FD",
                explanation="If RD < FD, the neighbor cannot possibly loop through you to reach the destination."
            ),
            QuizQuestionBlueprint(
                question="What is the default Administrative Distance (AD) of internal EIGRP routes?",
                options=[
                    "90",
                    "110",
                    "120",
                    "1"
                ],
                correct_answer="90",
                explanation="Internal EIGRP routes are assigned an Administrative Distance of 90."
            ),
            QuizQuestionBlueprint(
                question="What algorithm is executed by EIGRP to guarantee loop-free convergence and backup path calculations?",
                options=[
                    "DUAL (Diffusing Update Algorithm)",
                    "Dijkstra's SPF",
                    "Bellman-Ford",
                    "Kruskal's algorithm"
                ],
                correct_answer="DUAL (Diffusing Update Algorithm)",
                explanation="DUAL finite state machine tracks route calculations and ensures loop-free convergence."
            ),
            QuizQuestionBlueprint(
                question="Which unique routing capability is supported exclusively by EIGRP among all standard interior routing protocols?",
                options=[
                    "Unequal-cost load balancing (using the `variance` command)",
                    "Subnetting",
                    "Authentication",
                    "Dynamic route updates"
                ],
                correct_answer="Unequal-cost load balancing (using the `variance` command)",
                explanation="EIGRP can balance traffic across paths with different metrics using the variance multiplier."
            ),
            QuizQuestionBlueprint(
                question="What two primary link metrics are used by default in EIGRP's composite metric calculation?",
                options=[
                    "Bandwidth and Delay",
                    "Hop Count and Cost",
                    "Packet Loss and Jitter",
                    "Voltage and Temperature"
                ],
                correct_answer="Bandwidth and Delay",
                explanation="By default (K1=1, K3=1), EIGRP calculates metrics using minimum bandwidth and cumulative delay."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 28
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: OSPF (Open Shortest Path First - Single & Multi-Area)",
        concept="The enterprise link-state workhorse: OSPF neighbor adjacencies, Hello packets, DR/BDR election, Cost metric, Area 0 (Backbone), and LSA types",
        analogy="Think of multi-area OSPF like a multinational corporate enterprise. The global executive boardroom at headquarters is **Area 0 (The Backbone Area)**. Every regional branch office (Sales Area 1, Engineering Area 2) must have a direct liaison door plugged into the headquarters boardroom (**ABR - Area Border Router**). Regional offices resolve their own small local desk moves without bothering global headquarters, keeping the global executive boardroom calm and uncluttered!",
        theory_sections=[
            {
                "heading": "OSPF Adjacency States & DR/BDR Election",
                "body": "OSPF forms neighbor adjacencies via **Hello packets** sent to multicast `224.0.0.5`. On multi-access broadcast networks (Ethernet LANs with multiple routers), routers elect a **DR (Designated Router)** and **BDR (Backup Designated Router)** using highest OSPF Priority (default 1) broken by highest Router ID (RID). Non-DR routers (**DROTHERs**) form full adjacencies only with the DR/BDR (sending updates to `224.0.0.6`), reducing link adjacency meshes from `N*(N-1)/2` down to `2*(N-2)`."
            },
            {
                "heading": "Multi-Area Hierarchy & The Backbone (Area 0)",
                "body": "In large enterprise networks, running OSPF in a single area causes the Link-State Database (LSDB) to consume excessive RAM and forces every router to rerun Dijkstra's SPF on every minor link flap. Dividing the network into hierarchical **Areas** bounds SPF calculations. **The Golden Rule of Multi-Area OSPF: All non-backbone areas must connect directly to Area 0 (Backbone)** through an **ABR (Area Border Router)**."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Single-Area OSPFv2 (Cisco IOS)",
                "language": "text",
                "code": "Router(config)# router ospf 1\nRouter(config-router)# router-id 1.1.1.1       -- Best Practice: Assign explicit 32-bit Router ID\nRouter(config-router)# network 192.168.1.0 0.0.0.255 area 0\nRouter(config-router)# network 10.0.0.0 0.255.255.255 area 0\nRouter(config-router)# passive-interface GigabitEthernet0/0/2",
                "explanation": "Configures OSPF process 1, sets an explicit Router ID, and activates Area 0 with wildcard masks."
            },
            {
                "title": "Configuring Multi-Area OSPF on an Area Border Router (ABR)",
                "language": "text",
                "code": "ABR-Router(config)# router ospf 1\nABR-Router(config-router)# router-id 10.255.255.1\n-- Backbone link in Area 0:\nABR-Router(config-router)# network 10.0.0.0 0.0.0.3 area 0\n-- Branch office link in Area 10:\nABR-Router(config-router)# network 192.168.10.0 0.0.0.255 area 10",
                "explanation": "An Area Border Router (ABR) connects Area 10 directly into the core Backbone Area 0."
            },
            {
                "title": "Verifying OSPF Neighbor Adjacency States",
                "language": "text",
                "code": "Router# show ip ospf neighbor\nNeighbor ID     Pri   State           Dead Time   Address         Interface\n2.2.2.2           1   FULL/DR         00:00:36    192.168.1.2     GigabitEthernet0/0/0\n3.3.3.3           1   FULL/BDR        00:00:34    192.168.1.3     GigabitEthernet0/0/0\n# 'FULL/DR' confirms router formed a complete operational adjacency with the DR!",
                "explanation": "Confirms that OSPF neighbors successfully traversed Down -> Init -> 2-Way -> ExStart -> Exchange -> Loading -> Full."
            },
            {
                "title": "OSPF Cost Calculation Formula",
                "language": "python",
                "code": "def calculate_ospf_cost(interface_bandwidth_mbps: float, reference_bw_mbps: float = 100.0) -> int:\n    \"\"\"Cost = Reference Bandwidth / Interface Bandwidth (Minimum cost is 1)\"\"\"\n    cost = reference_bw_mbps / interface_bandwidth_mbps\n    return max(1, int(cost))\n\n# FastEthernet (100M) = cost 1; Gigabit (1000M) = cost 1 (unless ref-bw adjusted!)\nprint('Default Cost for 10M link:', calculate_ospf_cost(10.0)) # Cost 10",
                "explanation": "Calculates OSPF interface cost inversely proportional to link speed."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="OSPF Router ID Determinant",
            description="Write a Python function `determine_ospf_rid(manual_rid: str, loopbacks: list[str], physicals: list[str]) -> str` that follows the Cisco OSPF RID election rule: (1) Manual RID if present; (2) Highest IP on Loopback interfaces; (3) Highest IP on active physical interfaces.",
            starter_code="def determine_ospf_rid(manual_rid: str, loopbacks: list[str], physicals: list[str]) -> str:\n    # Determine elected OSPF Router ID\n    pass",
            solution_code="import ipaddress\n\ndef determine_ospf_rid(manual_rid: str, loopbacks: list[str], physicals: list[str]) -> str:\n    if manual_rid and manual_rid.strip():\n        return manual_rid.strip()\n    if loopbacks:\n        return str(max([ipaddress.ip_address(ip) for ip in loopbacks]))\n    if physicals:\n        return str(max([ipaddress.ip_address(ip) for ip in physicals]))\n    return '0.0.0.0'",
            expected_output="determine_ospf_rid('1.1.1.1', ['10.0.0.1'], ['192.168.1.1']) == '1.1.1.1', determine_ospf_rid('', ['10.0.0.1', '10.0.0.5'], ['192.168.1.1']) == '10.0.0.5'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the mandatory Backbone Area in a multi-area OSPF network that all other areas must connect to?",
                options=[
                    "Area 0 (or Area 0.0.0.0)",
                    "Area 1",
                    "Area 100",
                    "Area 255"
                ],
                correct_answer="Area 0 (or Area 0.0.0.0)",
                explanation="In multi-area OSPF, Area 0 is the designated core backbone through which inter-area traffic must pass."
            ),
            QuizQuestionBlueprint(
                question="What multicast IP addresses are used by OSPF routers on multi-access broadcast networks?",
                options=[
                    "224.0.0.5 (All OSPF Routers) and 224.0.0.6 (All Designated Routers - DR/BDR)",
                    "224.0.0.9 and 224.0.0.10",
                    "255.255.255.255 only",
                    "239.255.255.250"
                ],
                correct_answer="224.0.0.5 (All OSPF Routers) and 224.0.0.6 (All Designated Routers - DR/BDR)",
                explanation="224.0.0.5 addresses all OSPF routers; 224.0.0.6 targets the DR and BDR."
            ),
            QuizQuestionBlueprint(
                question="How does a router determine its OSPF Router ID (RID) if it was NOT manually configured?",
                options=[
                    "It elects the highest IPv4 address on any active Loopback interface; if none exist, the highest IPv4 address on any active physical interface",
                    "It generates a random number",
                    "It uses the MAC address of port 1",
                    "It asks the DHCP server"
                ],
                correct_answer="It elects the highest IPv4 address on any active Loopback interface; if none exist, the highest IPv4 address on any active physical interface",
                explanation="Highest loopback IP takes precedence, followed by highest active physical interface IP."
            ),
            QuizQuestionBlueprint(
                question="What OSPF neighbor state indicates that routers have achieved a complete, healthy database synchronization?",
                options=[
                    "FULL state",
                    "2-WAY state",
                    "INIT state",
                    "ATTEMPT state"
                ],
                correct_answer="FULL state",
                explanation="The FULL state signifies that neighbor LSDBs are fully synchronized."
            ),
            QuizQuestionBlueprint(
                question="What metric does OSPF use to determine the best path to a destination?",
                options=[
                    "Cost (inversely proportional to link Bandwidth: Reference_BW / Link_BW)",
                    "Hop Count",
                    "Cable length",
                    "Total number of computers"
                ],
                correct_answer="Cost (inversely proportional to link Bandwidth: Reference_BW / Link_BW)",
                explanation="OSPF calculates cost from bandwidth, favoring higher-speed links."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: BGP (Border Gateway Protocol - iBGP & eBGP)",
        concept="The protocol that connects the global Internet: Autonomous Systems (ASNs), Path Vector mechanics, BGP attributes (AS-Path, Next-Hop, Local Preference, MED), and peering",
        analogy="Think of interior routing protocols (OSPF/EIGRP) like the local traffic rules inside a sovereign country (e.g. driving on the right side of the road in Pakistan). **BGP (Border Gateway Protocol)** is international diplomacy and foreign border customs. Countries don't care how internal city streets are laid out; they negotiate border trade treaties (**BGP Peering Sessions**), checking passport stamps (**AS-Path**) to route cargo across sovereign nations!",
        theory_sections=[
            {
                "heading": "Autonomous Systems (AS) & The Path Vector Engine",
                "body": "The Internet is a federation of thousands of independent networks called **Autonomous Systems (ASNs)** (e.g. Google AS15169, Microsoft AS8075). BGP is a **Path Vector** protocol that glues these autonomous systems together. Rather than calculating raw link speeds, BGP makes routing decisions based on network policies, business relationships, and the sequence of Autonomous Systems a packet must traverse (**AS-Path**)."
            },
            {
                "heading": "eBGP vs iBGP & The AS-Path Loop Prevention Rule",
                "body": "**eBGP (External BGP)** connects routers in *different* Autonomous Systems (default AD 20); **iBGP (Internal BGP)** distributes BGP routes *within* the same AS (default AD 200). **Loop Prevention**: When an eBGP router advertises a route, it prepends its own ASN to the AS-Path attribute. If a router receives an advertisement where its own ASN is already listed in the AS-Path, it **immediately discards the route**, preventing inter-domain routing loops."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring eBGP Peering Between Two Autonomous Systems",
                "language": "text",
                "code": "-- Router in AS 65001 peering with ISP in AS 65002\nRouter-Enterprise(config)# router bgp 65001\nRouter-Enterprise(config-router)# bgp router-id 1.1.1.1\nRouter-Enterprise(config-router)# neighbor 203.0.113.2 remote-as 65002\nRouter-Enterprise(config-router)# network 198.51.100.0 mask 255.255.255.0\n# Establishes TCP port 179 peering session with neighbor",
                "explanation": "Establishes an eBGP peering session across Autonomous System boundaries over TCP port 179."
            },
            {
                "title": "BGP Path Selection Hierarchy Decision Matrix",
                "language": "text",
                "code": "Step   Attribute            Rule\n1      Weight               Highest wins (Cisco proprietary, local to router)\n2      Local Preference     Highest wins (Propagated across iBGP AS)\n3      Originate Locally    Locally originated routes preferred over learned\n4      AS-Path              Shortest AS-Path length wins (Fewer AS hops!)\n5      Origin Code          IGP (i) < EGP (e) < Incomplete (?)\n6      MED (Metric)         Lowest MED wins (Influences inbound traffic from neighbor)\n7      Path Type            eBGP paths preferred over iBGP paths\n8      Router ID            Lowest neighbor BGP Router ID as tie-breaker",
                "explanation": "Summary of BGP's path selection algorithm evaluating attributes in sequence."
            },
            {
                "title": "Verifying BGP Summary and Peering Table",
                "language": "text",
                "code": "Router# show ip bgp summary\nNeighbor        V    AS    MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd\n203.0.113.2     4  65002       142     140       12    0    0 02:14:15           5\n# 'State/PfxRcd: 5' indicates BGP session is ESTABLISHED and 5 prefixes were learned!",
                "explanation": "Verifies BGP state (Established) and count of active prefixes received from peer."
            },
            {
                "title": "Python BGP AS-Path Loop Detection Simulator",
                "language": "python",
                "code": "def check_bgp_as_loop(local_asn: int, as_path: list[int]) -> bool:\n    \"\"\"If local ASN is in AS-Path, drop route to prevent inter-domain loops!\"\"\"\n    if local_asn in as_path:\n        print(f'Rejecting route: Local ASN {local_asn} detected in AS-Path {as_path}!')\n        return True # Loop detected!\n    return False\n\nprint(check_bgp_as_loop(65001, [65002, 65003, 65001])) # Returns True (Loop!)",
                "explanation": "Demonstrates the BGP AS-Path loop detection mechanism."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="BGP AS-Path Loop Detector",
            description="Write a Python function `detect_as_loop(local_as: int, path: list[int]) -> bool` that returns `True` if `local_as` appears anywhere inside the `path` list.",
            starter_code="def detect_as_loop(local_as: int, path: list[int]) -> bool:\n    # Return True if local ASN is in path\n    pass",
            solution_code="def detect_as_loop(local_as: int, path: list[int]) -> bool:\n    return local_as in path",
            expected_output="detect_as_loop(100, [200, 300, 100]) == True, detect_as_loop(100, [200, 300, 400]) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What transport layer protocol and port number does BGP use to establish reliable peering sessions?",
                options=[
                    "TCP port 179",
                    "UDP port 53",
                    "IP protocol 89",
                    "UDP port 520"
                ],
                correct_answer="TCP port 179",
                explanation="BGP establishes reliable point-to-point connections over TCP port 179."
            ),
            QuizQuestionBlueprint(
                question="How does BGP prevent routing loops between different Autonomous Systems?",
                options=[
                    "A router automatically discards any incoming BGP route update if its own Autonomous System Number (ASN) is found inside the AS-Path attribute",
                    "By running Dijkstra's algorithm every 5 minutes",
                    "By limiting all networks to 15 hops",
                    "By blocking all TCP traffic"
                ],
                correct_answer="A router automatically discards any incoming BGP route update if its own Autonomous System Number (ASN) is found inside the AS-Path attribute",
                explanation="The AS-Path attribute lists traversed ASNs; finding one's own ASN indicates a routing loop."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between eBGP and iBGP?",
                options=[
                    "eBGP is used between routers in different Autonomous Systems; iBGP is used between routers within the same Autonomous System",
                    "eBGP is wireless; iBGP is wired",
                    "iBGP only works on Apple computers",
                    "There is no difference"
                ],
                correct_answer="eBGP is used between routers in different Autonomous Systems; iBGP is used between routers within the same Autonomous System",
                explanation="eBGP connects distinct Autonomous Systems; iBGP distributes BGP prefixes internally."
            ),
            QuizQuestionBlueprint(
                question="What BGP attribute is evaluated first in Cisco's standard BGP path selection algorithm?",
                options=[
                    "Weight (Highest weight wins)",
                    "AS-Path length",
                    "MED",
                    "Router ID"
                ],
                correct_answer="Weight (Highest weight wins)",
                explanation="Cisco routers evaluate Weight first (a proprietary, locally-configured integer)."
            ),
            QuizQuestionBlueprint(
                question="What is an Autonomous System (AS) in Internet architecture?",
                options=[
                    "A large connected network or collection of IP prefixes under the control of a single technical administrative organization (e.g. ISP or enterprise)",
                    "A computer that runs without human intervention",
                    "A server that generates free cryptocurrency",
                    "A robot that plugs in network cables"
                ],
                correct_answer="A large connected network or collection of IP prefixes under the control of a single technical administrative organization (e.g. ISP or enterprise)",
                explanation="An AS is a collection of connected routing prefixes managed by a single administrative domain."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: TCP vs UDP (Three-Way Handshake & Flow Control)",
        concept="Layer 4 transport mechanics: Connection-oriented TCP vs Connectionless UDP, SYN-SYN/ACK-ACK handshake, Sliding Windows, Flow Control, and Checksums",
        analogy="Think of **TCP** like certified postal mail with return-receipt tracking. You call the recipient on the phone: 'Are you ready?' (**SYN**). They say: 'Yes, send it!' (**SYN-ACK**). You say: 'Great, here it comes' (**ACK**). Every page is numbered; if page 4 gets wet, they request a retransmission. **UDP** is like a live radio broadcast or a quarterback throwing footballs into the endzone: the station broadcasts music continuously—if you drive under a bridge for 2 seconds, the station doesn't rewind the music; it just keeps playing!",
        theory_sections=[
            {
                "heading": "TCP: Reliable, Connection-Oriented Protocol",
                "body": "TCP (Transmission Control Protocol - RFC 793) guarantees reliable, in-order delivery of data streams. Before transmitting data, it establishes a session using the **Three-Way Handshake (SYN -> SYN-ACK -> ACK)**. TCP provides: (1) **Sequencing**: packets reassembled in correct order; (2) **Acknowledgments & Retransmission**: lost segments are detected and resent; (3) **Flow Control**: dynamic **Sliding Window** mechanism prevents overwhelming the receiver's buffer; (4) **Congestion Control**: throttles transmission during network bottlenecks."
            },
            {
                "heading": "UDP: Lightweight, Connectionless Datagrams",
                "body": "UDP (User Datagram Protocol - RFC 768) is a minimal, connectionless transport protocol with a tiny 8-byte header (compared to TCP's 20-byte minimum header). UDP provides zero guarantees: no handshake, no acknowledgments, no retransmissions, and no in-order ordering. It is optimal for real-time applications where low latency outweighs reliability: VoIP calls, live video streaming, online multiplayer gaming, and fast query protocols like DNS and DHCP."
            }
        ],
        code_snippets=[
            {
                "title": "TCP vs UDP Header Comparison Table",
                "language": "text",
                "code": "Feature                 TCP (Transmission Control Protocol)   UDP (User Datagram Protocol)\nConnection State        Connection-Oriented (3-Way Handshake) Connectionless (Fire and Forget)\nReliability             Guaranteed (Acks & Retransmissions)   Best-effort (Packets can drop)\nOrdering                Guaranteed via Sequence Numbers       No ordering guarantee\nHeader Size             20 Bytes minimum (up to 60 with opts) 8 Bytes fixed\nFlow & Congestion Ctrl  Yes (Sliding Window, AIMD)            None\nUse Cases               HTTP/HTTPS, SSH, FTP, Email, SQL DBs  VoIP, Video Streaming, Gaming, DNS",
                "explanation": "Contrasts structural differences and use cases of TCP and UDP."
            },
            {
                "title": "The TCP Three-Way Handshake Sequence Diagram",
                "language": "text",
                "code": "Client                                              Server\n  │                                                   │\n  │ ── 1. SYN (seq=100) ────────────────────────────> │ (Client requests connection)\n  │                                                   │\n  │ <── 2. SYN-ACK (seq=300, ack=101) ─────────────── │ (Server acknowledges & sends SYN)\n  │                                                   │\n  │ ── 3. ACK (ack=301) ────────────────────────────> │ (Client acknowledges)\n  │                                                   │\n  └─── [ TCP Connection Established / Data Flows ] ───┘",
                "explanation": "Step-by-step sequence diagram of the SYN, SYN-ACK, ACK connection establishment."
            },
            {
                "title": "Capturing TCP Three-Way Handshake with Tshark / Wireshark",
                "language": "bash",
                "code": "# Filter network traffic strictly for TCP control flags (SYN, ACK)\ntshark -i any -Y 'tcp.flags.syn == 1' -T fields -e ip.src -e ip.dst -e tcp.flags.str\n# 192.168.1.50 -> 142.250.190.46  ·······S· (SYN)\n# 142.250.190.46 -> 192.168.1.50  ···A···S· (SYN-ACK)",
                "explanation": "Filters live network packet captures for the initial TCP SYN and SYN-ACK handshake flags."
            },
            {
                "title": "Fast UDP Client vs Reliable TCP Client in Python",
                "language": "python",
                "code": "import socket\n\n# Fast, lightweight UDP message transmission (No handshake!)\ndef send_udp_telemetry(host: str, port: int, payload: bytes):\n    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM = UDP\n    sock.sendto(payload, (host, port))\n    sock.close()\n\n# Reliable TCP stream transmission (With Handshake!)\ndef send_tcp_transaction(host: str, port: int, payload: bytes):\n    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM = TCP\n    sock.connect((host, port))\n    sock.sendall(payload)\n    response = sock.recv(1024)\n    sock.close()\n    return response",
                "explanation": "Contrasts Python socket implementations of connectionless UDP versus stream-oriented TCP."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="TCP Handshake Next Sequence Number Calculator",
            description="Write a Python function `get_next_ack(received_seq: int, is_syn_or_fin: bool, payload_len: int = 0) -> int` that calculates the ACK number to return in TCP. If `is_syn_or_fin` is True, it consumes 1 sequence number (`seq + 1`). If carrying data, it consumes `seq + payload_len`.",
            starter_code="def get_next_ack(received_seq: int, is_syn_or_fin: bool, payload_len: int = 0) -> int:\n    # Calculate next expected ACK sequence number\n    pass",
            solution_code="def get_next_ack(received_seq: int, is_syn_or_fin: bool, payload_len: int = 0) -> int:\n    if is_syn_or_fin:\n        return received_seq + 1\n    return received_seq + payload_len",
            expected_output="get_next_ack(100, True, 0) == 101, get_next_ack(500, False, 200) == 700"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the exact sequence of packets exchanged during the TCP Three-Way Handshake?",
                options=[
                    "SYN -> SYN-ACK -> ACK",
                    "ACK -> SYN -> SYN-ACK",
                    "HELLO -> WELCOME -> CONNECTED",
                    "FIN -> ACK -> RST"
                ],
                correct_answer="SYN -> SYN-ACK -> ACK",
                explanation="The client sends SYN, the server responds with SYN-ACK, and the client returns ACK."
            ),
            QuizQuestionBlueprint(
                question="Why is UDP preferred over TCP for live video conferencing (Zoom) and online gaming?",
                options=[
                    "UDP has minimal latency with zero retransmission delays, prioritizing timely delivery over perfect packet recovery",
                    "UDP encrypts all video streams automatically",
                    "TCP cannot transmit audio",
                    "UDP cables are faster than TCP cables"
                ],
                correct_answer="UDP has minimal latency with zero retransmission delays, prioritizing timely delivery over perfect packet recovery",
                explanation="Retransmitting late video/audio packets is useless in live streams; low latency is paramount."
            ),
            QuizQuestionBlueprint(
                question="What is the size of a standard User Datagram Protocol (UDP) header?",
                options=[
                    "8 bytes",
                    "20 bytes",
                    "64 bytes",
                    "4 bytes"
                ],
                correct_answer="8 bytes",
                explanation="A UDP header is fixed at 8 bytes (Source Port, Dest Port, Length, Checksum)."
            ),
            QuizQuestionBlueprint(
                question="What mechanism does TCP use to dynamically control the flow of data so a fast sender does not overwhelm a slow receiver's memory buffer?",
                options=[
                    "Sliding Window (Windowing)",
                    "PortFast",
                    "Spanning Tree",
                    "Trunking"
                ],
                correct_answer="Sliding Window (Windowing)",
                explanation="The TCP Window Size field signals buffer capacity, allowing dynamic flow throttling."
            ),
            QuizQuestionBlueprint(
                question="What TCP flag is sent when a host wants to gracefully terminate an established connection?",
                options=[
                    "FIN (Finish)",
                    "RST (Reset)",
                    "SYN (Synchronize)",
                    "URG (Urgent)"
                ],
                correct_answer="FIN (Finish)",
                explanation="The FIN flag initiates graceful four-step connection teardown."
            )
        ]
    )
]
