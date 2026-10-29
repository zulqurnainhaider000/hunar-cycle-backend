"""
Instructor Manual data-com (2) Curriculum Seeder
Faculty of Engineering Sciences & Technology (FEST), Hamdard University Islamabad Campus.

100% VERBATIM transcription from "Instructor Manual data-com (2).pdf".
Complete 12-Lab Curriculum Covering:
- Day 1 (Lab # 2 in manual): Network Components (UTP, STP, Coax, Fiber Optics, Connectors, NIC)
- Day 2 (Lab # 3 in manual): Cable Construction (Straight-Through, Crossover, Rollover, Tools, Hubs, Switches, MAC, Routers)
- Day 3 (Lab # 4 in manual): Building a Peer-to-Peer Network (IPv4 format, Classes A-E, NetID/HostID, Loopback, Private ranges, Subnet masks)
- Day 4 (Lab # 5 in manual): Building a Switched Network 1 (TCP/IP protocols, Switch cabling, LED status lamps, ipconfig, ping, tracert)
- Day 5 (Lab # 6 in manual): Building an advanced Switched Network and controlling an unauthorized access (Windows Firewall ICMP, APIPA 169.254, ARP, Static Class A/B/C)
- Day 6 (Lab # 7 in manual): Sharing and Remote Access (Simple File Sharing, RDP client/server, System properties, mstsc)
- Day 7 (Lab # 8 in manual): Address Resolution Protocol (ARP / RARP concepts, Layer 2-3 mapping, Dynamic vs Static, arp -a/-d/-s)
- Day 8 (Lab # 9 in manual): Wireshark (Packet sniffer, 3 panes, Capture preferences promiscuous mode, pcap filters)
- Day 9 (Lab # 10 in manual): Introduction to the Cisco IOS (Console, Aux, Telnet, POST/Boot sequence, NVRAM, User/Privileged EXEC, copy run start)
- Day 10 (Lab # 11 in manual): Cisco Routers- Basic Configurations (Hostnames, MOTD banners, Passwords, service password-encryption, FastEthernet, Serial DCE clock rate, show int)
- Day 11 (Lab # 12 in manual): IP Routing (Routed vs Routing protocols, Static routes, Default routes 0.0.0.0, RIP distance-vector hop count max 15, show ip route)
- Day 12 (Lab # 13 in manual): VLAN (Virtual LAN) (Flat network, Broadcast domains, Access vs Trunk 802.1Q/ISL, Router-on-a-Stick subinterfaces, switchport access vlan, show vlan brief)

Assessments:
- EXACTLY 5 high-quality Quizzes per Lab (60 Quizzes total)
- EXACTLY 4 Flashcards per Lab (48 Flashcards total)
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

# Ensure environment variables from backend/.env are loaded
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(backend_dir, ".env"))

from prisma import Prisma

COURSE_DATA = {
    "title": "Instructor Manual data-com (2)",
    "category": "University",
    "description": "Official Academic Curriculum for Instructor Manual data-com (2), Faculty of Engineering Sciences & Technology (FEST), Hamdard University Islamabad Campus. Comprehensive laboratory manual covering Network Transmission Media (UTP, STP, Coaxial, Fiber Optics, NICs), Cable Construction & Pinouts (Straight-Through, Crossover, Rollover Console), Peer-to-Peer Networking, IPv4 Addressing & Subnetting, Switched LAN Architecture & Switch Diagnostics, Advanced Switched Networks, Windows Firewall Security & ICMP, Network Sharing & Remote Desktop Protocol (RDP), Address Resolution Protocol (ARP), Wireshark Packet Inspection, Cisco IOS Command-Line Operation, Router Configurations, Static/Dynamic IP Routing (RIP), and Virtual Local Area Networks (VLANs & Router-on-a-Stick).",
    "color": "#059669",
    "thumbnail": "assets/images/university/ccn/datacom2_logo.png"
}

DAYS_PART1 = [   {   'codeSnippet': '# Network Transmission Media & Cable Specifications Reference\n'
                       '\n'
                       '# 1. Twisted-Pair Specifications:\n'
                       '# Category: Cat 5 / Cat 5e / Cat 6 (100 Mbps - 1 Gbps, 100m segment limit)\n'
                       '# Connector: RJ-45 (8P8C modular connector)\n'
                       '# Shielding: UTP (Unshielded) vs STP (Shielded with metallic foil/braid)\n'
                       '\n'
                       '# 2. Coaxial Cable Specifications:\n'
                       '# Thicknet (RG-11): 50-ohm, connects up to 100 devices, max distance 5000 m (expensive)\n'
                       '# Thinnet (RG-58): 50-ohm, connects up to 30 devices, max distance 185 m (cheaper)\n'
                       '# Connector: BNC (Bayonet Neill-Concelman) connector, T-connector, 50-ohm terminator\n'
                       '\n'
                       '# 3. Optical Fiber Specifications:\n'
                       '# Single-mode (SMF): 8-10 micron core, 1310/1550 nm laser, single direct light path, '
                       'long-haul\n'
                       '# Multimode (MMF): 50/62.5 micron core, 850/1300 nm LED/laser, multiple angles, local campus\n'
                       '# Connectors: ST (Straight Tip - bayonet lock), SC (Subscriber Connector - push-pull square)',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 2: Network Components (Day 1)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand some basic information about networks.\n'
                   '* Focusing on network transmission media and its types.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Data Communications:\n'
                   'The exchange of data between two devices via some form of transmission medium such as a wire '
                   'cable. A data communications system must transmit data to the correct destination in an accurate '
                   'and timely manner.\n'
                   '\n'
                   '#### A Network:\n'
                   'A network is a set of devices (often referred to as nodes) connected together by communication '
                   'links to transmit information and for sharing resources.\n'
                   '\n'
                   '#### Network Components:\n'
                   'A data communications system has **five components**:\n'
                   '1. **The Message**: The information or data communicated (text, numbers, pictures, audio, video).\n'
                   '2. **The Sender**: The device that sends the data message (computer, workstation, telephone '
                   'handset, video camera).\n'
                   '3. **The Receiver**: The device that receives the message (computer, workstation, television, '
                   'printer).\n'
                   '4. **The Medium**: The physical path by which a message travels from sender to receiver.\n'
                   '5. **The Protocol**: A set of rules that govern data communications. It represents an agreement '
                   'between the communicating devices.\n'
                   '\n'
                   '![Data Communications Components](assets/images/university/ccn/lab1_data_comm_components.png)\n'
                   '*Figure 1.0: Five components of a data communications system (Message, Sender, Receiver, Medium, '
                   'Protocol).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Transmission Media:\n'
                   '\n'
                   'A transmission media is defined as **anything that can carry information from a source to a '
                   'destination**.\n'
                   '\n'
                   '![Transmission Media Overview](assets/images/university/ccn/lab1_media.png)\n'
                   '*Figure 1: Transmission Media classification.*\n'
                   '\n'
                   '#### Types of Transmission Media:\n'
                   '\n'
                   'Transmission media are broadly classified into **Guided Media** (wired/bounded) and **Unguided '
                   'Media** (wireless/unbounded):\n'
                   '\n'
                   '![Transmission Media Categories](assets/images/university/ccn/lab1_transmission_media.png)\n'
                   '*Figure 2: Transmission media categories (Guided: Twisted-pair, Coaxial, Fiber-optic; Unguided: '
                   'Free space radio/microwave).*\n'
                   '\n'
                   '**Guided media**, which are those that provide a physical conduit from one device to another, '
                   'include:\n'
                   '* Twisted-pair cable\n'
                   '* Coaxial cable\n'
                   '* Fiber-optic cable\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 1. Twisted-Pair Cable\n'
                   '\n'
                   '* Consists of two or more pairs of single conductor wires that have been twisted around each '
                   'other.\n'
                   '* **Twisting the cables helps to eliminate electromagnetic interference (EMI) and crosstalk** '
                   'between the two wires.\n'
                   '* Shielding can further help to eliminate external noise and interference.\n'
                   '\n'
                   '#### 1.1 Unshielded Twisted-Pair (UTP):\n'
                   'The most common cable used in local area networking. It consists of color-coded copper conductors '
                   'insulated in plastic sheath without metallic shielding.\n'
                   '\n'
                   '![UTP Cable](assets/images/university/ccn/lab1_utp_cable.png)\n'
                   '*Figure 3: Unshielded twisted-pair (UTP) cable.*\n'
                   '\n'
                   'UTP cable terminates in a standard **RJ-45 (Registered Jack 45)** modular connector:\n'
                   '\n'
                   '![RJ-45 Connector](assets/images/university/ccn/lab1_rj45_connector.png)\n'
                   '*Figure 4: RJ-45 Connector (8-pin modular connector for UTP cabling).*\n'
                   '\n'
                   '#### 1.2 Shielded Twisted-Pair (STP):\n'
                   'Contains a protective metal foil or braided mesh shield encasing each pair or all pairs together.\n'
                   '* More expensive than UTP.\n'
                   '* Much less susceptible to electromagnetic interference and noise.\n'
                   '\n'
                   '![STP Cable](assets/images/university/ccn/lab1_stp_cable.png)\n'
                   '*Figure 5: Shielded twisted-pair (STP) cable.*\n'
                   '\n'
                   '#### Twisted-Pair Cable Applications:\n'
                   '* Telephone lines\n'
                   '* **Local loop**: The physical line that connects subscribers to the central telephone office\n'
                   '* DSL (Digital Subscriber Line) broadband lines\n'
                   '* Local Area Networks (LANs - 10BASE-T, 100BASE-TX, 1000BASE-T)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 2. Coaxial Cable\n'
                   '\n'
                   '* Carries signals of higher frequency ranges than those in twisted-pair cable.\n'
                   '* **Central core conductor** of solid or stranded wire (usually copper).\n'
                   '* Insulating plastic dielectric layer.\n'
                   '* **Outer conductor** of metal foil, braided copper wire, or a combination of the two, acting as a '
                   'shield against noise and ground return.\n'
                   '* Outer protective plastic jacket.\n'
                   '\n'
                   '![Coaxial Cable Construction](assets/images/university/ccn/lab1_coaxial_cable.png)\n'
                   '*Figure 6: Coaxial cable construction.*\n'
                   '\n'
                   '#### Coaxial cable has two main kinds:\n'
                   '1. **Thick (RG-11)**: Connects up to 100 devices with a maximum segment range of 5000 m (more '
                   'expensive, heavy and rigid).\n'
                   '2. **Thin (RG-58)**: Connects up to 30 devices within a maximum range of 185 m (cheaper, flexible, '
                   'popular in legacy 10BASE2).\n'
                   '\n'
                   'To connect coaxial cable to network devices, we need **BNC (Bayonet Neill-Concelman)** '
                   'connectors:\n'
                   '\n'
                   '![BNC Connectors](assets/images/university/ccn/lab1_bnc_connectors.png)\n'
                   '*Figure 7: BNC Connectors (BNC cable connector, BNC T-connector, and BNC terminator).*\n'
                   '\n'
                   '#### Coaxial cable applications:\n'
                   '* Analog telephone networks\n'
                   '* Digital telephone networks (largely replaced today with fiber-optic cable)\n'
                   '* Cable TV (CATV) distribution networks (near consumer premises)\n'
                   '* Traditional legacy Ethernet LANs (10BASE2 and 10BASE5)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 3. Fiber-Optic Cable\n'
                   '\n'
                   '* A fiber-optic cable is made of ultra-pure glass or plastic and **transmits signals in the form '
                   'of light pulses**.\n'
                   '* A glass or plastic **core** is surrounded by a **cladding** of less dense optical material '
                   '(lower refractive index) to ensure total internal reflection.\n'
                   '* Outer buffer coating and protective jacket prevent physical damage and moisture ingress.\n'
                   '\n'
                   '![Fiber Optics Cable](assets/images/university/ccn/lab1_fiber_optic.png)\n'
                   '*Figure 8: Fiber Optics cable structure.*\n'
                   '\n'
                   '#### Fiber Optic Cable Modes:\n'
                   '1. **Single-mode fiber (SMF)**: Features an extremely narrow core (8-10 microns). Carries light '
                   'pulses along a single direct path with zero intermodal dispersion; used for long-distance '
                   'backbones.\n'
                   '2. **Multimode fiber (MMF)**: Features a larger core (50-62.5 microns). Many pulses of light '
                   'travel simultaneously at different reflection angles; used for shorter campus LANs.\n'
                   '\n'
                   '![Fiber Optic Propagation Modes](assets/images/university/ccn/lab1_fiber_modes.png)\n'
                   '*Figure 9: Propagation modes (Single-mode step index vs Multimode step index and graded index).*\n'
                   '\n'
                   '#### Popular Connectors Used with Fiber-Optic Cable:\n'
                   '* **ST (Straight Tip) connectors**: Bayonet twist-lock cylindrical connector.\n'
                   '* **SC (Subscriber Connector)**: Square push-pull latching connector.\n'
                   '\n'
                   '![Fiber Optic Connectors](assets/images/university/ccn/lab1_fiber_connectors.png)\n'
                   '*Figure 10: Fiber optic connectors (ST and SC connectors).*\n'
                   '\n'
                   '#### Fiber Optic Cable Applications:\n'
                   '* High-speed telecommunication backbone networks\n'
                   '* Cable TV distribution backbones\n'
                   '* High-bandwidth campus Local Area Networks (LANs)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 4. Network Interface Card (NIC)\n'
                   '\n'
                   'In computer networking, a **NIC** provides the hardware interface between a computer and a '
                   'physical network medium. A NIC technically is network adapter hardware installed in an expansion '
                   'slot (PCI/PCIe) or integrated on the motherboard.\n'
                   '\n'
                   '![Network Interface Card](assets/images/university/ccn/lab1_nic.png)\n'
                   '*Figure 11: 10/100 Ethernet network LAN Adapter with RJ-45 port.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Guided media provide distinct transmission capabilities: Twisted-pair is cost-effective for '
                   'desktop LANs, Coaxial delivers legacy broadband, and Fiber-Optic offers high bandwidth and noise '
                   'immunity.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '1. The student should inspect and handle all network lab transmission media samples (UTP Cat 5/6, '
                   'STP, Thinnet RG-58, Thicknet RG-11, Single-mode and Multimode fiber samples).\n'
                   '2. Identify the connector types (RJ-45, BNC, ST, SC) and match each connector to its proper cable '
                   'and NIC port.\n',
        'flashcards': [   {   'answer': 'Message (the data communicated), Sender (device sending data), Receiver '
                                        '(device receiving data), Medium (physical transmission path), and Protocol '
                                        '(rules governing communication).',
                              'question': 'What are the 5 essential components of a data communications system?'},
                          {   'answer': 'UTP (Unshielded Twisted-Pair) lacks metallic shielding around wire pairs, '
                                        'while STP (Shielded Twisted-Pair) encases pairs in protective metal foil or '
                                        'braid to resist electromagnetic interference.',
                              'question': 'What is the key difference between UTP and STP cabling?'},
                          {   'answer': 'RG-11 (Thicknet) supports up to 100 devices across a 5000 m segment '
                                        '(expensive/heavy), while RG-58 (Thinnet) supports up to 30 devices over a 185 '
                                        'm segment (cheaper/flexible).',
                              'question': 'What are the key technical differences between RG-11 and RG-58 coaxial '
                                          'cables?'},
                          {   'answer': 'ST (Straight Tip - round bayonet twist-lock connector) and SC (Subscriber '
                                        'Connector - square push-pull latching connector).',
                              'question': 'What are the two common connector types used for fiber-optic cabling?'}],
        'order': 1,
        'quizzes': [   {   'correctAnswer': 'Message, Sender, Receiver, Medium, and Protocol',
                           'explanation': 'According to the manual, a data communications system has five components: '
                                          'the message, sender, receiver, medium, and protocol.',
                           'options': [   'Message, Sender, Receiver, Medium, and Protocol',
                                          'Hardware, Software, Firmware, User, and Data',
                                          'Server, Client, Router, Switch, and Hub',
                                          'Input, Processing, Output, Storage, and Control'],
                           'question': 'What are the five fundamental components of a data communications system?'},
                       {   'correctAnswer': 'To eliminate electromagnetic interference and crosstalk between the two '
                                            'wires',
                           'explanation': 'Twisting the cables cancels out electromagnetic interference and crosstalk '
                                          'between the two wires, and shielding provides additional external noise '
                                          'protection.',
                           'options': [   'To increase the overall physical breaking tension of the wire',
                                          'To eliminate electromagnetic interference and crosstalk between the two '
                                          'wires',
                                          'To allow high-voltage AC electric current transmission',
                                          'To separate data transmission channels into distinct colors'],
                           'question': 'What is the primary technical reason for twisting conductor pairs in a '
                                       'Twisted-Pair cable?'},
                       {   'correctAnswer': 'Thin coaxial cable (RG-58)',
                           'explanation': 'Thin (RG-58) connects up to 30 devices within 185 m (cheaper), whereas '
                                          'Thick (RG-11) connects up to 100 devices over a range of 5000 m.',
                           'options': [   'Thick coaxial cable (RG-11)',
                                          'Thin coaxial cable (RG-58)',
                                          'Shielded Twisted Pair (STP)',
                                          'Single-mode fiber optic cable'],
                           'question': 'Which coaxial cable specification connects up to 30 devices within a maximum '
                                       'segment distance of 185 meters?'},
                       {   'correctAnswer': 'Single-mode carries light pulses along a single direct path, whereas '
                                            'multimode allows many light pulses to travel at different angles',
                           'explanation': 'Single-mode fiber features a tiny core carrying light pulses along a single '
                                          'path with minimal dispersion, while Multimode fiber allows multiple light '
                                          'rays to propagate at different angles.',
                           'options': [   'Single-mode carries light pulses along a single direct path, whereas '
                                          'multimode allows many light pulses to travel at different angles',
                                          'Single-mode uses copper core reflection, whereas multimode uses glass '
                                          'refraction',
                                          'Single-mode is limited to short patch cords, whereas multimode spans '
                                          'intercontinental subsea cables',
                                          'Single-mode transmits radio frequency, whereas multimode transmits infrared '
                                          'light'],
                           'question': 'How does Single-mode optical fiber differ from Multimode optical fiber in '
                                       'light propagation?'},
                       {   'correctAnswer': 'RJ-45 connector',
                           'explanation': 'Unshielded Twisted-Pair (UTP) network cables terminate in an 8-pin RJ-45 '
                                          '(Registered Jack 45) connector.',
                           'options': ['BNC connector', 'RJ-45 connector', 'ST connector', 'SC connector'],
                           'question': 'Which modular connector type is standard for terminating 8-conductor '
                                       'Unshielded Twisted-Pair (UTP) network cables?'}],
        'title': 'Day 1 (Lab # 2): Network Components'},
    {   'codeSnippet': '# Cable Pinout Wiring Color Codes Reference\n'
                       '\n'
                       '# EIA/TIA-568A Standard:\n'
                       '# Pin 1: White-Green\n'
                       '# Pin 2: Green\n'
                       '# Pin 3: White-Orange\n'
                       '# Pin 4: Blue\n'
                       '# Pin 5: White-Blue\n'
                       '# Pin 6: Orange\n'
                       '# Pin 7: White-Brown\n'
                       '# Pin 8: Brown\n'
                       '\n'
                       '# EIA/TIA-568B Standard (Most Popular):\n'
                       '# Pin 1: White-Orange\n'
                       '# Pin 2: Orange\n'
                       '# Pin 3: White-Green\n'
                       '# Pin 4: Blue\n'
                       '# Pin 5: White-Blue\n'
                       '# Pin 6: Green\n'
                       '# Pin 7: White-Brown\n'
                       '# Pin 8: Brown\n'
                       '\n'
                       '# Crossover Cable Pin Swaps (568A to 568B):\n'
                       '# Pin 1 (Tx+) <---> Pin 3 (Rx+)\n'
                       '# Pin 2 (Tx-) <---> Pin 6 (Rx-)\n'
                       '# Pin 3 (Rx+) <---> Pin 1 (Tx+)\n'
                       '# Pin 6 (Rx-) <---> Pin 2 (Tx-)',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 3: Cable Construction (Day 2)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding the inner details for UTP and STP cables.\n'
                   '* Make different types of cables: **Straight-Through**, **Crossover**, and **Rollover**.\n'
                   '* The student should take a demonstration on the network lab devices and tools.\n'
                   '* Understanding the main function for the network lab devices and tools.\n'
                   '* Understanding the main differences between MAC and IP addresses.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   'In Lab 1, there were many types of network cables used in real-world applications, such as UTP, '
                   'STP, and Coax cables. In Lab 2, we will continue with the most common cables (UTP and STP) to '
                   'learn their inner technical details. The inner colored wires in UTP or STP must follow a precise '
                   'order to perform their designed functions.\n'
                   '\n'
                   'According to the arrangement of the inner colored wires, network cables are categorized as:\n'
                   '1. **Straight-Through cable**\n'
                   '2. **Crossover cable**\n'
                   '3. **Rollover cable (Console cable)**\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Straight-Through Cable\n'
                   '\n'
                   'Here, the connections are **identical on both ends** of the cable. This type of cable is used when '
                   'connecting **dissimilar devices**:\n'
                   '* Switch to Router\n'
                   '* Router to Hub\n'
                   '* Switch to PC\n'
                   '* Hub to PC\n'
                   '\n'
                   'The colors of the wires and their respective pin numbers are:\n'
                   '\n'
                   '| Pin # | Side 1 Color | Side 2 Color |\n'
                   '|:---:|:---|:---|\n'
                   '| **Pin 1** | White-Orange | White-Orange |\n'
                   '| **Pin 2** | Orange | Orange |\n'
                   '| **Pin 3** | White-Green | White-Green |\n'
                   '| **Pin 4** | Blue | Blue |\n'
                   '| **Pin 5** | White-Blue | White-Blue |\n'
                   '| **Pin 6** | Green | Green |\n'
                   '| **Pin 7** | White-Brown | White-Brown |\n'
                   '| **Pin 8** | Brown | Brown |\n'
                   '\n'
                   '![Straight-Through Cable](assets/images/university/ccn/lab2_straight_through.png)\n'
                   '*Figure 1: Straight-through cable pinouts (T568B on both ends).*\n'
                   '\n'
                   '![Cable Summary](assets/images/university/ccn/lab2_cables.png)\n'
                   '*Figure 1.1: Ethernet cable wiring color coding comparison.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Crossover Cable\n'
                   '\n'
                   'Here, the connections are different with a specific pattern. This type of cable is used when '
                   'connecting **similar devices**:\n'
                   '* Router to Router\n'
                   '* Switch to Switch\n'
                   '* PC to PC\n'
                   '* Hub to Hub\n'
                   '\n'
                   'And with specific exceptions:\n'
                   '* Switch to Hub\n'
                   '* Router to PC (since both transmit on pins 1 & 2 and receive on pins 3 & 6)\n'
                   '\n'
                   'The colors of the wires and their respective pin numbers are:\n'
                   '\n'
                   '| Pin # | Side 1 (T568B) | Side 2 (T568A) |\n'
                   '|:---:|:---|:---|\n'
                   '| **Pin 1** | White-Orange | White-Green |\n'
                   '| **Pin 2** | Orange | Green |\n'
                   '| **Pin 3** | White-Green | White-Orange |\n'
                   '| **Pin 4** | Blue | Blue |\n'
                   '| **Pin 5** | White-Blue | White-Blue |\n'
                   '| **Pin 6** | Green | Orange |\n'
                   '| **Pin 7** | White-Brown | White-Brown |\n'
                   '| **Pin 8** | Brown | Brown |\n'
                   '\n'
                   '![Crossover Cable](assets/images/university/ccn/lab2_crossover.png)\n'
                   '*Figure 2: Crossover cable pinouts (T568B swapped to T568A).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Rollover Cable (Console Cable)\n'
                   '\n'
                   'Here, the connections are made in **completely reverse order**:\n'
                   '* Pin 1 connects to Pin 8\n'
                   '* Pin 2 connects to Pin 7\n'
                   '* Pin 3 connects to Pin 6\n'
                   '* Pin 4 connects to Pin 5\n'
                   '* Pin 5 connects to Pin 4\n'
                   '* Pin 6 connects to Pin 3\n'
                   '* Pin 7 connects to Pin 2\n'
                   '* Pin 8 connects to Pin 1\n'
                   '\n'
                   "This type of cable is used to connect a PC's serial/COM port (or USB-serial adapter) to the "
                   '**Console port** of a Cisco router or switch for out-of-band management and configuration.\n'
                   '\n'
                   '![Rollover Cable](assets/images/university/ccn/lab2_rollover.png)\n'
                   '*Figure 3: Rollover cable pinouts.*\n'
                   '\n'
                   '![Cisco Console Connection](assets/images/university/ccn/lab2_cisco_console.png)\n'
                   '*Figure 3.1: Cisco router console rollover cable with RJ-45 to DB-9 adapter.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Networking Tools:\n'
                   '\n'
                   '#### 1. Cable Crimping Tool:\n'
                   'A specialized handheld mechanical tool used to crimp or connect an RJ-45 modular connector to the '
                   'prepared ends of a twisted-pair cable. It strips cable jackets, cuts individual conductors flush, '
                   'and presses metallic contact blades into the wire cores.\n'
                   '\n'
                   '![Crimping Tool](assets/images/university/ccn/lab2_crimping_tool.png)\n'
                   '*Figure 4: Cable crimping tool.*\n'
                   '\n'
                   '#### 2. Network Cable Tester:\n'
                   'An electronic test instrument used to verify the electrical continuity and pinout correctness in a '
                   'cable assembly. It sequentially illuminates LEDs for pins 1 through 8 to reveal open circuits, '
                   'short circuits, crossed pairs, or split pairs.\n'
                   '\n'
                   '![Cable Tester](assets/images/university/ccn/lab2_cable_tester.png)\n'
                   '*Figure 5: Network cable tester.*\n'
                   '\n'
                   '#### 3. Rack & Patch Panel:\n'
                   'A mounted hardware unit containing rows of RJ-45 ports used to terminate, organize, and patch '
                   'horizontal structured cabling runs coming from wall jacks throughout a building into central '
                   'network switches.\n'
                   '\n'
                   '![Patch Panel](assets/images/university/ccn/lab2_patch_panel.png)\n'
                   '*Figure 6: Rack and Patch Panel.*\n'
                   '\n'
                   '#### 4. Cable Tray:\n'
                   'A structural cable tray system used to support insulated electrical and data cables used for power '
                   'distribution and communication. Cable trays are used for overhead and raised-floor cable '
                   'management in commercial construction. They are especially useful when wiring modifications are '
                   'anticipated, allowing new cables to be laid in the tray rather than pulled through rigid conduit '
                   'pipes.\n'
                   '\n'
                   '![Cable Tray](assets/images/university/ccn/lab2_cable_tray.png)\n'
                   '*Figure 7: Cable tray overhead management system.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Network Devices:\n'
                   '\n'
                   '#### 1. HUB:\n'
                   'In computer networking, a hub is a simple Layer 1 (Physical Layer) multiport device that joins '
                   'multiple computers together. Packets arriving at any port are broadcast/repeated out all other '
                   'ports, creating a single collision domain and sharing bandwidth.\n'
                   '\n'
                   '![Network Hub](assets/images/university/ccn/lab2_network_hub.png)\n'
                   '*Figure 8: Ethernet Hub.*\n'
                   '\n'
                   '#### 2. SWITCH:\n'
                   'A network switch is a hardware device that connects multiple computers together within one local '
                   'area network (LAN). Technically, network switches operate at **Layer 2 (Data Link Layer)** of the '
                   'OSI model. Switches inspect incoming frames, learn connected devices, and forward traffic unicast '
                   'directly to the destination port based on **MAC (Media Access Control)** addresses, creating '
                   'isolated collision domains on every port.\n'
                   '\n'
                   '![Network Switch](assets/images/university/ccn/lab2_network_switch.png)\n'
                   '*Figure 9: Network Switch.*\n'
                   '\n'
                   '#### MAC Address Architecture:\n'
                   'The MAC address uniquely identifies network adapters on a LAN. MAC addresses are **12-digit '
                   'hexadecimal numbers (48 bits in length)**, represented as six pairs of hex digits:\n'
                   '\n'
                   '`00:A0:C9:14:C8:29`\n'
                   '\n'
                   '* **First 24 bits (3 bytes)**: The **Organizationally Unique Identifier (OUI)** representing the '
                   'adapter manufacturer, regulated by the IEEE standards body. In the example `00:A0:C9`, it '
                   'identifies **Intel Corporation**.\n'
                   '* **Second 24 bits (3 bytes)**: The unique serial number assigned to the adapter by the '
                   'manufacturer.\n'
                   '\n'
                   '![MAC Address Structure](assets/images/university/ccn/lab2_mac_address.png)\n'
                   '*Figure 10: 48-bit MAC address format (OUI Vendor ID vs Device Serial Number).*\n'
                   '\n'
                   '#### 3. ROUTER:\n'
                   'A router is a Layer 3 (Network Layer) device that forwards data packets between computer networks, '
                   'creating an interconnected overlay internetwork. Routers connect distinct IP subnets and WANs.\n'
                   '\n'
                   '![Network Router](assets/images/university/ccn/lab2_router.png)\n'
                   '*Figure 11: Network Router.*\n'
                   '\n'
                   'Routers manage traffic based on logical **IP (Internet Protocol) addresses**. An IP address '
                   'consists of 4 octets that represent the host on an intranet or the Internet. Each IP address has '
                   'two parts:\n'
                   '* **Network ID (NetID)**\n'
                   '* **Host ID (HostID)**\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Preparation:\n'
                   '* Prepare all needed equipment before making cables (bulk UTP cable roll, RJ-45 connectors, '
                   'crimping tool, cable tester).\n'
                   '* Each student should cut and assemble their own cable.\n'
                   '\n'
                   '#### Main Steps to Make a Crossover Cable:\n'
                   '1. Cut the UTP cable to the desired length using the cutting blade on the crimping tool.\n'
                   '2. Strip approximately 1.5 to 2 cm of the outer plastic jacket using the stripper blade.\n'
                   '3. Untwist and straighten the colored wire pairs.\n'
                   '4. Align the wires according to the **T568B** color sequence on Side 1:\n'
                   '   *(White-Orange, Orange, White-Green, Blue, White-Blue, Green, White-Brown, Brown)*\n'
                   '5. Trim the aligned wires flat and push them firmly into an RJ-45 connector until each wire '
                   'touches the front of the plug.\n'
                   '6. Insert the connector into the crimper socket and squeeze the handles firmly until the gold pins '
                   'lock into the wires.\n'
                   '7. Prepare Side 2 using the **T568A** color sequence:\n'
                   '   *(White-Green, Green, White-Orange, Blue, White-Blue, Orange, White-Brown, Brown)*\n'
                   '8. Insert both ends into the network cable tester and power it on. Verify that LEDs 1-3, 2-6, 3-1, '
                   '4-4, 5-5, 6-2, 7-7, 8-8 illuminate in correct crossover sequence.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Straight-Through cables connect dissimilar devices (PC to Switch), Crossover cables connect '
                   'similar devices (PC to PC), and Rollover cables enable console management.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '1. Make a verified Straight-Through cable (T568B on both ends).\n'
                   '2. Make a verified Rollover console cable (Pin 1 reversed to Pin 8).\n',
        'flashcards': [   {   'answer': 'Straight-Through connects dissimilar devices (e.g. Switch to PC, Switch to '
                                        'Router). Crossover connects similar devices (e.g. PC to PC, Switch to Switch, '
                                        'Router to Router) and exceptions (Router to PC).',
                              'question': 'When do you use a Straight-Through vs Crossover cable?'},
                          {   'answer': 'Pins 1 and 2 swap with Pins 3 and 6: Pin 1 (Tx+) <-> Pin 3 (Rx+), and Pin 2 '
                                        '(Tx-) <-> Pin 6 (Rx-). Pins 4, 5, 7, and 8 remain unchanged.',
                              'question': 'What is the specific pin-swap pattern in a Crossover cable?'},
                          {   'answer': 'A console cable where pin connections are completely inverted (Pin 1 to Pin '
                                        '8, Pin 2 to Pin 7, etc.), used to configure Cisco switches and routers via '
                                        'console port.',
                              'question': 'What is a Rollover cable and what are its pin connections?'},
                          {   'answer': 'The first 24 bits are the Organizationally Unique Identifier (OUI) assigned '
                                        'to the manufacturer, and the last 24 bits are the vendor-assigned unique '
                                        'adapter serial number.',
                              'question': 'What are the two components of a 48-bit MAC address?'}],
        'order': 2,
        'quizzes': [   {   'correctAnswer': 'When connecting dissimilar devices such as switch to PC or switch to '
                                            'router',
                           'explanation': 'Straight-Through cables are used when connecting dissimilar devices (switch '
                                          'and router, router and hub, switch and PC, etc.).',
                           'options': [   'When connecting similar devices such as switch to switch or PC to PC',
                                          'When connecting dissimilar devices such as switch to PC or switch to router',
                                          "When connecting a computer directly to a router's console port",
                                          'When connecting two standalone network hubs together'],
                           'question': 'When should a Straight-Through UTP cable be used instead of a Crossover '
                                       'cable?'},
                       {   'correctAnswer': 'Pin 1',
                           'explanation': 'In crossover cabling, Pin 1 (Tx+) on Side 1 connects to Pin 3 (Rx+) on Side '
                                          '2, and Pin 2 (Tx-) connects to Pin 6 (Rx-).',
                           'options': ['Pin 1', 'Pin 2', 'Pin 4', 'Pin 6'],
                           'question': 'In a standard Ethernet Crossover cable, which pin on Side 1 connects to Pin 3 '
                                       'on Side 2?'},
                       {   'correctAnswer': 'To connect a PC to a router or switch console port for management '
                                            'purposes',
                           'explanation': "A rollover cable has reversed pinouts and connects a computer's serial port "
                                          'to a router or switch console port for administrative management.',
                           'options': [   'To interconnect two gigabit switches for VLAN trunking',
                                          'To connect a PC to a router or switch console port for management purposes',
                                          'To supply Power over Ethernet (PoE) to an IP telephone',
                                          'To connect an analog dial-up modem to a telephone wall jack'],
                           'question': 'What is the primary function of a Rollover (console) cable?'},
                       {   'correctAnswer': '48 bits; the first 24 bits represent the Organizationally Unique '
                                            'Identifier (OUI manufacturer ID)',
                           'explanation': 'MAC addresses are 48 bits (12 hexadecimal digits). The first 24 bits are '
                                          'the IEEE-regulated OUI identifying the manufacturer (e.g. 00A0C9 for '
                                          'Intel), and the remaining 24 bits are the serial number.',
                           'options': [   '32 bits; the first 16 bits represent the Network ID',
                                          '48 bits; the first 24 bits represent the Organizationally Unique Identifier '
                                          '(OUI manufacturer ID)',
                                          '64 bits; the first 32 bits represent the IPv4 translation prefix',
                                          '128 bits; the first 64 bits represent the interface identifier'],
                           'question': 'How many total bits make up a standard MAC address, and what do the first 24 '
                                       'bits represent?'},
                       {   'correctAnswer': 'Layer 2 (Data Link Layer)',
                           'explanation': 'Network switches operate at Layer 2 (Data Link Layer) of the OSI model and '
                                          'forward frames between ports based on hardware MAC addresses.',
                           'options': [   'Layer 1 (Physical Layer)',
                                          'Layer 2 (Data Link Layer)',
                                          'Layer 3 (Network Layer)',
                                          'Layer 4 (Transport Layer)'],
                           'question': 'At which layer of the OSI model do network switches operate to make forwarding '
                                       'decisions based on MAC addresses?'}],
        'title': 'Day 2 (Lab # 3): Cable Construction'},
    {   'codeSnippet': '# Windows Command Prompt: Network Diagnostic Commands\n'
                       '\n'
                       '# 1. Check local TCP/IP stack integrity:\n'
                       'ping 127.0.0.1\n'
                       '\n'
                       '# 2. Test connectivity with peer workstation (Workstation 2):\n'
                       'ping 192.168.230.2\n'
                       '\n'
                       '# 3. Continuous ping for cable testing:\n'
                       'ping 192.168.230.2 -t\n'
                       '\n'
                       '# 4. View active IP configuration:\n'
                       'ipconfig\n'
                       'ipconfig /all',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 4: Building a Peer-to-Peer Network (Day 3)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding the concept behind a peer-to-peer network.\n'
                   '* Understanding the IP address structure.\n'
                   '* Understanding masking concepts and subnet mask address structure.\n'
                   '* Create a simple LAN with two PCs (simple peer-to-peer network) using a single crossover cable to '
                   'connect the two workstations.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Peer-to-Peer (P2P) Network:\n'
                   'A peer-to-peer (abbreviated to P2P) computer network is one in which **each computer in the '
                   'network can act as both a client or server** for the other computers in the network. This '
                   'architecture allows shared access to various resources such as files, printers, peripherals, and '
                   'sensors without requiring a central dedicated server.\n'
                   '\n'
                   'P2P networks can be set up within the home, a small business, or over the Internet. Each computer '
                   'must use a compatible protocol and network configuration to communicate. Each PC must have a '
                   '**unique IP address** on the same subnet to communicate.\n'
                   '\n'
                   '![Peer-to-Peer Topology](assets/images/university/ccn/lab3_p2p_topology.png)\n'
                   '*Figure 1: Simple peer-to-peer network between two workstations connected via crossover cable.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### IP Address Architecture:\n'
                   '\n'
                   'An IP address is a logical address assigned to a network adapter. Computers and devices acquire IP '
                   'addresses to join Internet Protocol networks.\n'
                   '\n'
                   '* Logical address used in TCP/IP networking.\n'
                   '* **Unique 32-bit binary number**.\n'
                   '* Divided into **four groups of octets (8-bit bytes)** separated by periods (dotted decimal '
                   'notation):\n'
                   '  `217.29.240.5`\n'
                   '* Total IPv4 address space: **2^32 = 4,294,967,296 addresses**.\n'
                   '* Addresses can be assigned statically by an administrator or dynamically via DHCP.\n'
                   '* **ICANN (Internet Corporation for Assigned Names and Numbers)**: A non-profit organization that '
                   'maintains and allocates global IP address space.\n'
                   '\n'
                   '![IPv4 Address Format](assets/images/university/ccn/lab3_ipv4_format.png)\n'
                   '*Figure 2: IPv4 32-bit dotted-decimal address structure.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### IP Address Classes:\n'
                   '\n'
                   'IPv4 divides unicast addresses into classes based on the high-order bits of the first octet:\n'
                   '\n'
                   '| Class | 1st Octet Range | High-Order Bits | Default Subnet Mask | Purpose / Scale |\n'
                   '|:---:|:---:|:---:|:---:|:---|\n'
                   '| **Class A** | 1 – 126 | `0xxxxxxx` | `255.0.0.0` | Very large networks (16.7M hosts/net) |\n'
                   '| **Class B** | 128 – 191 | `10xxxxxx` | `255.255.0.0` | Medium-sized networks (65,534 hosts/net) '
                   '|\n'
                   '| **Class C** | 192 – 223 | `110xxxxx` | `255.255.255.0` | Small local networks (254 hosts/net) |\n'
                   '| **Class D** | 224 – 239 | `1110xxxx` | N/A | Multicast groups |\n'
                   '| **Class E** | 240 – 255 | `1111xxxx` | N/A | Experimental and research |\n'
                   '\n'
                   '![IP Classes Table](assets/images/university/ccn/lab3_ip_classes.png)\n'
                   '*Figure 3: IP address classes and network division.*\n'
                   '\n'
                   '#### NetID vs HostID:\n'
                   'Every IP address consists of two parts:\n'
                   '1. **Network ID (NetID)**: Identifies the specific network to which the host belongs.\n'
                   '2. **Host ID (HostID)**: Uniquely identifies the individual workstation or node on that network.\n'
                   '\n'
                   '![NetID and HostID](assets/images/university/ccn/lab3_netid_hostid.png)\n'
                   '*Figure 4: NetID and HostID division across Class A, Class B, and Class C.*\n'
                   '\n'
                   '#### Number of Addresses per Class:\n'
                   '* **Class A**: 128 networks, 16,777,216 addresses per network.\n'
                   '* **Class B**: 16,384 networks, 65,536 addresses per network.\n'
                   '* **Class C**: 2,097,152 networks, 256 addresses per network.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Loopback Address:\n'
                   'The IP address **`127.0.0.1`** is a special-purpose address reserved on every computer:\n'
                   '* Reserved for communicating from a node to itself (**localhost**).\n'
                   "* Allows testing whether the local computer's TCP/IP software stack is installed and operational "
                   'without transmitting packets onto the wire.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Private and Public IP Addresses:\n'
                   '\n'
                   '* **Public IP Addresses**: Globally unique routable addresses assigned for use over the Internet.\n'
                   '* **Private IP Addresses**: Non-routable addresses reserved for internal use within private Local '
                   'Area Networks (LANs), defined in RFC 1918:\n'
                   '\n'
                   '| Class | Private Address Range | Default Subnet Mask |\n'
                   '|:---:|:---|:---:|\n'
                   '| **Class A** | `10.0.0.0` to `10.255.255.255` | `255.0.0.0` |\n'
                   '| **Class B** | `172.16.0.0` to `172.31.255.255` | `255.255.0.0` |\n'
                   '| **Class C** | `192.168.0.0` to `192.168.255.255` | `255.255.255.0` |\n'
                   '\n'
                   '![Private IP Ranges](assets/images/university/ccn/lab3_private_ip.png)\n'
                   '*Figure 5: Private IP address ranges (RFC 1918).*\n'
                   '\n'
                   '![Private IP Table](assets/images/university/ccn/lab3_private_table.png)\n'
                   '*Figure 5.1: Private IP address space allocation.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Masking Concept & The Network Address:\n'
                   '\n'
                   'A **subnet mask** is a 32-bit number that distinguishes the Network ID from the Host ID. It '
                   'contains 1s in the network bits and 0s in the host bits.\n'
                   '\n'
                   '![Masking Concept](assets/images/university/ccn/lab3_masking_concept.png)\n'
                   '*Figure 6: Masking concept via bitwise AND operation.*\n'
                   '\n'
                   '#### The Network Address:\n'
                   'The network address is the beginning address of each address block:\n'
                   '* Found by performing a bitwise AND operation between any IP address in the block and its subnet '
                   'mask.\n'
                   '* Retains the NetID and sets all HostID bits to zero.\n'
                   '* E.g., IP `192.168.230.1` AND Mask `255.255.255.0` = Network Address `192.168.230.0`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Preparation:\n'
                   '* Work in pairs as a team to construct the peer-to-peer network.\n'
                   '* Each team uses two PCs and one verified crossover cable.\n'
                   '\n'
                   '#### Step 1: Physical Cabling:\n'
                   'Plug the crossover cable into the RJ-45 NIC ports of both workstations. Verify that the link light '
                   'on each NIC illuminates green.\n'
                   '\n'
                   '#### Step 2: Check Network Adapters in Device Manager:\n'
                   'Open `Control Panel` -> `System` -> `Device Manager`. Expand `Network Adapters` and right-click '
                   'your NIC:\n'
                   '* A green/normal icon indicates proper functioning.\n'
                   '* A **yellow circle with an exclamation mark** indicates a resource conflict or driver issue.\n'
                   '* A **red X** indicates the device is disabled or has a serious failure.\n'
                   '\n'
                   '#### Step 3: Configure TCP/IP Protocol Settings:\n'
                   '1. Open `Control Panel` -> `Network Connections`.\n'
                   '2. Right-click `Local Area Connection` and select `Properties`.\n'
                   '\n'
                   '![Network Connections Window](assets/images/university/ccn/lab3_network_connections.png)\n'
                   '*Figure 7: Network Connections Window.*\n'
                   '\n'
                   '3. Under the `General` tab, select `Internet Protocol (TCP/IP)` and click `Properties`.\n'
                   '\n'
                   '![TCP/IP Properties Window](assets/images/university/ccn/lab3_tcpip_properties.png)\n'
                   '*Figure 8: TCP/IP Properties configuration window.*\n'
                   '\n'
                   '4. Select `Use the following IP address` and configure static addresses on the `192.168.230.0` '
                   'network:\n'
                   '   * **Workstation 1**: IP `192.168.230.1`, Subnet Mask `255.255.255.0`\n'
                   '   * **Workstation 2**: IP `192.168.230.2`, Subnet Mask `255.255.255.0`\n'
                   '   * Leave Default Gateway and DNS blank for an isolated peer-to-peer lab.\n'
                   '\n'
                   '#### Step 4: Verify Connectivity with PING:\n'
                   'Open Command Prompt (`cmd`) and test connectivity:\n'
                   '```bat\n'
                   'ping 192.168.230.2\n'
                   '```\n'
                   '\n'
                   '#### Understanding Ping Output:\n'
                   '* **Reply from 192.168.230.2: bytes=32 time<1ms TTL=128**: Successful physical and network layer '
                   'communication.\n'
                   '* **Request timed out**: Indicates a physical cable break, incorrect IP configuration, host '
                   'powered off, or Windows Firewall blocking incoming ICMP packets.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Peer-to-peer networking enables direct resource sharing between two computers without servers '
                   'using a crossover cable and static IP configuration.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   "1. For each team, test connectivity with your neighbor team's PCs using the `ping` utility.\n"
                   '2. Troubleshoot and resolve any "Request timed out" responses by verifying cable pinouts and '
                   'firewall exceptions.\n',
        'flashcards': [   {   'answer': 'A network in which every connected computer can act as both a client and a '
                                        'server, sharing resources without requiring a central dedicated server.',
                              'question': 'What is the core definition of a Peer-to-Peer (P2P) network?'},
                          {   'answer': 'Class A: 1-126 (Mask 255.0.0.0); Class B: 128-191 (Mask 255.255.0.0); Class '
                                        'C: 192-223 (Mask 255.255.255.0).',
                              'question': 'What are the first-octet ranges and default subnet masks for Classes A, B, '
                                          'and C?'},
                          {   'answer': 'Class A: 10.0.0.0 – 10.255.255.255; Class B: 172.16.0.0 – 172.31.255.255; '
                                        'Class C: 192.168.0.0 – 192.168.255.255.',
                              'question': 'What are the private IP address ranges specified in RFC 1918 for Classes A, '
                                          'B, and C?'},
                          {   'answer': 'By performing a bitwise logical AND operation between the 32-bit IP address '
                                        'and the 32-bit subnet mask, preserving the NetID and setting all HostID bits '
                                        'to 0.',
                              'question': 'How is the Network Address calculated from an IP address and its subnet '
                                          'mask?'}],
        'order': 3,
        'quizzes': [   {   'correctAnswer': '4,294,967,296',
                           'explanation': 'IPv4 uses 32-bit addresses divided into four octets, yielding 2^32 = '
                                          '4,294,967,296 unique possible addresses.',
                           'options': [   '65,536',
                                          '16,777,216',
                                          '4,294,967,296',
                                          '340,282,366,920,938,463,463,374,607,431,768,211,456'],
                           'question': 'What is the theoretical total number of unique IPv4 addresses supported by its '
                                       '32-bit address space?'},
                       {   'correctAnswer': 'Range 192 – 223; Default mask 255.255.255.0',
                           'explanation': 'Class C addresses span from 192 to 223 in the first octet (binary prefix '
                                          '110) with a default subnet mask of 255.255.255.0.',
                           'options': [   'Range 1 – 126; Default mask 255.0.0.0',
                                          'Range 128 – 191; Default mask 255.255.0.0',
                                          'Range 192 – 223; Default mask 255.255.255.0',
                                          'Range 224 – 239; Default mask 255.255.255.255'],
                           'question': 'What is the first octet range and default subnet mask for Class C IPv4 '
                                       'addresses?'},
                       {   'correctAnswer': '127.0.0.1',
                           'explanation': '127.0.0.1 is the reserved loopback address, used to verify that the local '
                                          "computer's TCP/IP stack is functioning correctly.",
                           'options': ['0.0.0.0', '127.0.0.1', '192.168.1.1', '255.255.255.255'],
                           'question': 'Which special-purpose IP address is designated as the loopback address for '
                                       'communicating from a node to itself (localhost)?'},
                       {   'correctAnswer': '172.16.0.0 to 172.31.255.255',
                           'explanation': 'Class B private address space spans 172.16.0.0 through 172.31.255.255, '
                                          'containing 16 contiguous Class B network blocks.',
                           'options': [   '10.0.0.0 to 10.255.255.255',
                                          '172.16.0.0 to 172.31.255.255',
                                          '192.168.0.0 to 192.168.255.255',
                                          '169.254.0.0 to 169.254.255.255'],
                           'question': 'What is the designated private IP address range for Class B networks according '
                                       'to RFC 1918?'},
                       {   'correctAnswer': 'A physical cable failure, incorrect IP addressing, host offline, or '
                                            'blocking by a firewall',
                           'explanation': "The manual notes that 'Request time out' results from physical cable "
                                          'errors, host not found, or blocking by Windows Firewall.',
                           'options': [   'The remote host answered with duplicate ARP packets',
                                          'A physical cable failure, incorrect IP addressing, host offline, or '
                                          'blocking by a firewall',
                                          'The local DNS cache needs to be flushed',
                                          'The NIC has negotiated half-duplex communication'],
                           'question': "When testing network connectivity with the ping utility, what does a 'Request "
                                       "timed out' response typically indicate?"}],
        'title': 'Day 3 (Lab # 4): Building a Peer-to-Peer Network'},
    {   'codeSnippet': '# Windows Command Prompt: Network Diagnostic Commands\n'
                       '\n'
                       '# 1. View detailed TCP/IP settings for all network adapters:\n'
                       'ipconfig /all\n'
                       '\n'
                       '# 2. Release and renew dynamic DHCP IP address:\n'
                       'ipconfig /release\n'
                       'ipconfig /renew\n'
                       '\n'
                       '# 3. Test reachability with continuous ping:\n'
                       'ping 192.168.230.2 -t\n'
                       '\n'
                       '# 4. Trace route and hop count to external domain:\n'
                       'tracert www.yahoo.com\n'
                       'tracert -h 5 www.yahoo.com',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 5: Building a Switched Network 1 (Day 4)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding the concept behind a switched network.\n'
                   '* The student should be familiar with TCP/IP.\n'
                   '* Learn to create a simple LAN with two PCs using an Ethernet switch (Switched Network).\n'
                   '* Learn to configure and verify network connectivity.\n'
                   '* Learn to deal with the switch device and examine its LED lamp colors.\n'
                   '* Learn about various network-related commands: **Ping**, **Ipconfig**, and **Tracert**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Switched Network:\n'
                   'A switched network consists of a series of interlinked nodes called **switches**. Switches are '
                   'hardware devices capable of creating temporary dedicated point-to-point connections between two or '
                   'more devices. In a switched network, some nodes connect to end systems (workstations, servers), '
                   'while others connect to other switches for routing.\n'
                   '\n'
                   'In this lab, we build a simple switched network consisting of one central switch and multiple '
                   'workstations.\n'
                   '\n'
                   '![Switched Network Topology](assets/images/university/ccn/lab4_switched_net.png)\n'
                   '*Figure 1: Example of a switched local area network.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### What is TCP/IP?\n'
                   '\n'
                   '**TCP/IP** is the Internet Communication Protocol suite. It stands for **Transmission Control '
                   'Protocol / Internet Protocol**.\n'
                   '* A communication protocol is a formal description of the rules computers must follow to '
                   'communicate with each other.\n'
                   '* The Internet communication protocol defines rules for computer communication across local and '
                   'global networks.\n'
                   '* Web browsers access web servers using TCP/IP, and servers send HTML back over TCP/IP.\n'
                   '* E-mail applications use TCP/IP to send and receive e-mails over SMTP, POP3, and IMAP.\n'
                   '* Your IP address and domain name are essential parts of the TCP/IP protocol suite.\n'
                   '\n'
                   '#### Inside TCP/IP:\n'
                   'Inside the TCP/IP standard, several protocols handle specific aspects of data communications:\n'
                   '1. **TCP (Transmission Control Protocol)**: Reliable, connection-oriented communication between '
                   'applications with error recovery and flow control.\n'
                   '2. **UDP (User Datagram Protocol)**: Simple, lightweight, connectionless communication between '
                   'applications without delivery guarantees.\n'
                   '3. **IP (Internet Protocol)**: Logical addressing and packet routing between computers.\n'
                   '4. **ICMP (Internet Control Message Protocol)**: Diagnostic error reporting and statistical '
                   'messages (used by `ping` and `tracert`).\n'
                   '5. **DHCP (Dynamic Host Configuration Protocol)**: Application layer protocol for automated IP '
                   'address assignment. DHCP maintains an address pool, pulling the next available address and leasing '
                   'it to the requesting client for a negotiable lease duration.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Preparation:\n'
                   '* Workstations with functioning NICs and installed device drivers.\n'
                   '* An Ethernet Switch (4 to 32 ports) and two CAT5 **straight-through** cables.\n'
                   '\n'
                   '#### Step 1: Setting up a Simple Switched Network:\n'
                   'Connect the two PCs to the switch using straight-through cables. The switch permits multiple '
                   'workstations to communicate concurrently without collisions:\n'
                   '1. Plug the straight-through cable from Workstation 1 into **Port 1** of the switch.\n'
                   '2. Plug the cable from Workstation 2 into **Port 2** of the switch.\n'
                   '3. Turn on the switch and computers.\n'
                   '\n'
                   '#### Step 2: Checking Switch LED Status Lamps:\n'
                   'Check the green link LED on the back of each NIC and the port LEDs on the front of the switch:\n'
                   '* Verifies good physical Layer 1 and Layer 2 connectivity.\n'
                   '* If a link LED is unlit, it indicates a bad cable connection, incorrect pinout wiring, or a '
                   'hardware fault.\n'
                   '\n'
                   'You can monitor switch activity and operational status by checking its port LEDs. The switch port '
                   'LEDs indicate the following states:\n'
                   '\n'
                   '| Port LED State | Meaning |\n'
                   '|:---|:---|\n'
                   '| **Solid green** | Link is up (healthy connection). |\n'
                   '| **Steady flashing green** | Link is up. |\n'
                   '| **Flashing green** | Link is up (active traffic traversing the port). |\n'
                   '| **Solid amber** | Link is disabled by administrative software. |\n'
                   '| **Flashing amber** | A fault condition exists on the port. |\n'
                   '| **Off** | No physical link detected. |\n'
                   '\n'
                   '*Note: The LEDs flash various colors during POST (Power-On Self-Test) boot diagnostics. This is '
                   'normal. A healthy operational state is indicated by a steady green light.*\n'
                   '\n'
                   '#### Step 3: Network Adapters and TCP/IP Settings:\n'
                   '1. In `Network Connections`, verify the NIC is active without resource conflicts.\n'
                   '2. Configure static IP addresses:\n'
                   '   * **Workstation 1**: IP `192.168.230.1`, Subnet Mask `255.255.255.0`\n'
                   '   * **Workstation 2**: IP `192.168.230.2`, Subnet Mask `255.255.255.0`\n'
                   '   * Gateway and DNS can remain blank.\n'
                   '\n'
                   '#### Step 4: The IPCONFIG Command-Line Utility:\n'
                   '`ipconfig` is a command-line tool available on Microsoft Windows NT and later. It displays network '
                   'configuration and provides control over active TCP/IP connections.\n'
                   '\n'
                   'Run the command to display complete network adapter details:\n'
                   '```bat\n'
                   'ipconfig /all\n'
                   '```\n'
                   '\n'
                   '#### Step 5: Verify Connectivity with Ping:\n'
                   'From Workstation 1, ping Workstation 2:\n'
                   '```bat\n'
                   'ping 192.168.230.2\n'
                   '```\n'
                   '\n'
                   'To test an external Internet address:\n'
                   '```bat\n'
                   'ping www.yahoo.com\n'
                   '```\n'
                   '\n'
                   '#### Step 6: Path Discovery with TRACERT:\n'
                   '`tracert` traces the route packets take to reach a destination host:\n'
                   '```bat\n'
                   'tracert www.yahoo.com\n'
                   '```\n'
                   '\n'
                   '* The output displays each intermediate router (hop) and round-trip delay.\n'
                   '* The number of hops varies depending on dynamic routing paths across the Internet.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Switches provide dedicated bandwidth per port and isolate collisions. Switch diagnostic LEDs, '
                   '`ipconfig`, `ping`, and `tracert` provide comprehensive Layer 1 through Layer 3 verification.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks:\n'
                   '1. Run `ipconfig /?` to display all command-line parameters.\n'
                   '2. Try `ipconfig /renew` on a dynamic DHCP connection and record the results.\n'
                   '3. Run `ping /?` to inspect available flags.\n'
                   '4. Try continuous ping `ping <IP_Address> -t` and observe ping responses until interrupted with '
                   '`Ctrl+C`.\n'
                   '5. Run `tracert /?` and perform a trace with max hops limited to 5: `tracert -h 5 '
                   'www.yahoo.com`.\n',
        'flashcards': [   {   'answer': 'No light (Off), steady light (Solid Green = Link up, Solid Amber = Disabled), '
                                        'and flashing light (Flashing Green = Traffic, Flashing Amber = Fault).',
                              'question': 'What are the three primary LED status states on a network switch port?'},
                          {   'answer': 'ICMP handles error and diagnostic reporting (ping/tracert); DHCP '
                                        'automatically assigns IP addresses from a pool to client hosts for a leased '
                                        'duration.',
                              'question': 'What roles do ICMP and DHCP play in TCP/IP networking?'},
                          {   'answer': 'Host name, adapter MAC address, IP address, subnet mask, default gateway, '
                                        'DHCP server, lease dates, and DNS server addresses.',
                              'question': "What information does the 'ipconfig /all' command display?"},
                          {   'answer': 'It sends packets with incrementing TTL values to elicit ICMP Time Exceeded '
                                        'messages, discovering each router hop and round-trip latency along the path.',
                              'question': "How does the 'tracert' command measure the path to a remote computer?"}],
        'order': 4,
        'quizzes': [   {   'correctAnswer': 'Link is up (healthy physical connection)',
                           'explanation': "According to the manual's Switch Port LED table, Solid Green indicates that "
                                          'the physical link is up and operational.',
                           'options': [   'A fault condition exists on the port',
                                          'Link is up (healthy physical connection)',
                                          'Link has been administratively disabled by software',
                                          'Active traffic is causing packet collisions'],
                           'question': 'What does a Solid Green Port LED on an Ethernet network switch indicate?'},
                       {   'correctAnswer': 'A fault condition exists on the port or cable',
                           'explanation': 'A flashing amber LED indicates that a hardware, cable, or network fault '
                                          'condition exists.',
                           'options': [   'The port is operating in 1000 Mbps gigabit mode',
                                          'A fault condition exists on the port or cable',
                                          'The port is transmitting broadcast packets',
                                          'The switch is successfully executing an STP bridge election'],
                           'question': 'What does a Flashing Amber Port LED on a network switch signify?'},
                       {   'correctAnswer': 'ICMP',
                           'explanation': 'ICMP (Internet Control Message Protocol) is specifically designated within '
                                          'the TCP/IP stack for diagnostic error reporting and statistics.',
                           'options': ['TCP', 'UDP', 'ICMP', 'DHCP'],
                           'question': 'Which protocol in the TCP/IP suite is responsible for reporting network errors '
                                       'and diagnostic statistics?'},
                       {   'correctAnswer': 'ipconfig /all',
                           'explanation': "The 'ipconfig /all' command outputs detailed configuration settings for "
                                          'every network interface on a Windows computer.',
                           'options': ['ping -a', 'ipconfig /all', 'tracert -d', 'netstat -r'],
                           'question': 'Which Windows command-line utility displays all TCP/IP adapter parameters '
                                       'including MAC addresses and DNS servers?'},
                       {   'correctAnswer': 'An intermediate router or gateway along the path to the destination',
                           'explanation': 'Each hop in a tracert trace represents an intermediate Layer 3 router '
                                          'traversed by the packet on its path to the destination.',
                           'options': [   'A single byte of data transferred across the local bus',
                                          'An intermediate router or gateway along the path to the destination',
                                          'A local DNS cache record lookup',
                                          'A physical Ethernet switch port'],
                           'question': 'What does each hop reported by the tracert utility represent during path '
                                       'analysis?'}],
        'title': 'Day 4 (Lab # 5): Building a Switched Network 1'},
    {   'codeSnippet': '# Windows Command Prompt: Network & Firewall Management\n'
                       '\n'
                       '# 1. Inspect APIPA or DHCP assigned IP addresses:\n'
                       'ipconfig\n'
                       'ipconfig /all\n'
                       '\n'
                       '# 2. Ping local loopback to verify TCP/IP stack integrity:\n'
                       'ping 127.0.0.1\n'
                       '\n'
                       '# 3. Ping peer hosts across the advanced switched LAN:\n'
                       'ping 192.168.9.2\n'
                       'ping 192.168.9.3\n'
                       '\n'
                       '# 4. Access shared folder via UNC syntax:\n'
                       'start \\\\192.168.9.2\n'
                       'start \\\\PC2\n'
                       '\n'
                       '# 5. Verify ARP cache table:\n'
                       'arp -a',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 6: Building an advanced Switched Network and controlling an unauthorized access (Day 5)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Building a switched network using static and dynamic addressing.\n'
                   '* The student should be familiar with Windows Firewall settings and security controls.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Windows Firewall & Unauthorized Access:\n'
                   'When someone on the Internet or an external network tries to connect to your computer, Windows '
                   'calls that attempt an **"unsolicited request."** When your computer receives an unsolicited '
                   'request, Windows Firewall blocks the connection by default.\n'
                   '\n'
                   'If you run an application (such as an instant messaging program, file transfer, or network game) '
                   'that needs to receive information from the network, Windows Firewall prompts you to either '
                   '**block** or **unblock (allow)** the connection:\n'
                   '* Choosing to unblock creates an **Exception rule** so the firewall will permit that traffic in '
                   'the future.\n'
                   '* Although you can turn off Windows Firewall for specific connections, doing so increases the risk '
                   'of system compromise.\n'
                   '\n'
                   '![Windows Firewall Settings](assets/images/university/ccn/lab5_firewall_settings.png)\n'
                   "*Figure 1: Windows Firewall General tab (On, Off, Don't allow exceptions).*\n"
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Step 1: Setting up the Group LAN:\n'
                   '* Students work in groups of **4 to 7 workstations** connected to a single central switch.\n'
                   '* The lab switch is a **26-port Cisco switch** with 24 normal 10/100 Mbps ports and 2 Gigabit '
                   'ports (used for high-speed uplink backbones).\n'
                   "* Connect each PC's 3COM NIC to one of the 24 normal switch ports using standard UTP "
                   'straight-through cables.\n'
                   '\n'
                   '#### Step 2: Preparing Windows Firewall & ICMP Echo Requests:\n'
                   '1. Open `Control Panel` -> `Windows Firewall`.\n'
                   '\n'
                   '![Windows Firewall Exceptions](assets/images/university/ccn/lab5_firewall_rules.png)\n'
                   '*Figure 2: Windows Firewall Exceptions tab.*\n'
                   '\n'
                   '2. Navigate to the `Advanced` tab, highlight your network adapter, and click `Settings` under '
                   '**ICMP**.\n'
                   '3. Check the box for **`Allow incoming echo request`**.\n'
                   '   * By default, Windows Firewall blocks incoming ping requests.\n'
                   '   * Enabling incoming echo requests allows other computers to ping your workstation while '
                   'maintaining firewall protection against unauthorized access.\n'
                   '\n'
                   '![ICMP Echo Settings](assets/images/university/ccn/lab5_port_blocking.png)\n'
                   '*Figure 3: Windows Firewall ICMP Settings (Allow incoming echo request).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 3: Automatic IP Failover & APIPA (Automatic Private IP Addressing):\n'
                   '1. Configure all PCs to **Obtain an IP address automatically** in TCP/IP properties.\n'
                   '2. When connected to a reset or non-configured switch without an active DHCP server, the PCs will '
                   'fail to acquire a standard DHCP address.\n'
                   '3. Run `ipconfig /all`. The PCs receive an **APIPA** address in the **`169.254.x.x`** range with '
                   'subnet mask `255.255.0.0`:\n'
                   '   * APIPA range spans `169.254.0.1` to `169.254.255.254` (NetID `169.254.0.0/16`).\n'
                   '   * Windows displays a "Limited or no connectivity" warning (yellow triangle with an exclamation '
                   'mark).\n'
                   '4. **ARP (Address Resolution Protocol) Conflict Prevention**:\n'
                   '   * During failover, each host uses ARP to broadcast probe packets before binding an address.\n'
                   '   * This guarantees that no two PCs on the LAN select the same APIPA address.\n'
                   '\n'
                   '#### Sample APIPA Group Address Table:\n'
                   '| Student Name | PC Name | Assigned APIPA IP | Subnet Mask |\n'
                   '|:---|:---:|:---:|:---:|\n'
                   '| Ali | PC1 | `169.254.159.208` | `255.255.0.0` |\n'
                   '| Salem | PC2 | `169.254.155.235` | `255.255.0.0` |\n'
                   '| Maha | PC3 | `169.254.121.211` | `255.255.0.0` |\n'
                   '| Saud | PC4 | `169.254.150.134` | `255.255.0.0` |\n'
                   '| Mohd | PC5 | `169.254.105.212` | `255.255.0.0` |\n'
                   '| Zaid | PC6 | `169.254.110.113` | `255.255.0.0` |\n'
                   '\n'
                   'Test APIPA connectivity between workstations using `ping`:\n'
                   '```bat\n'
                   'ping 169.254.155.235\n'
                   'ping 169.254.150.134\n'
                   '```\n'
                   '*Both return successful replies, proving that APIPA allows local peer-to-peer communication even '
                   'when DHCP fails.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 4: Configuring the LAN Using Static Private Addresses:\n'
                   '\n'
                   'When DHCP is absent, static addressing provides predictable network organization.\n'
                   '\n'
                   '##### A. Class C Static Addressing:\n'
                   'Assign each PC an address on `192.168.9.0/24`:\n'
                   '* PC1 (Ali): `192.168.9.1` (Mask `255.255.255.0`)\n'
                   '* PC2 (Salem): `192.168.9.2` (Mask `255.255.255.0`)\n'
                   '* PC3 (Maha): `192.168.9.3` (Mask `255.255.255.0`)\n'
                   '* PC4 (Saud): `192.168.9.4` (Mask `255.255.255.0`)\n'
                   '* PC5 (Mohd): `192.168.9.5` (Mask `255.255.255.0`)\n'
                   '* PC6 (Zaid): `192.168.9.6` (Mask `255.255.255.0`)\n'
                   '\n'
                   '1. Test local stack: `ping 127.0.0.1` (verifies TCP/IP is intact).\n'
                   '2. Test group connectivity: `ping 192.168.9.2`, `ping 192.168.9.3`, `ping 192.168.9.4`.\n'
                   '\n'
                   '##### B. Class B Static Addressing:\n'
                   'Reconfigure all PCs with private Class B addresses (`172.16.0.0` through `172.31.255.255`):\n'
                   '* PC1: `172.25.10.101` (Mask `255.255.0.0`)\n'
                   '* PC2: `172.25.10.102` (Mask `255.255.0.0`)\n'
                   '* PC3: `172.25.10.103` (Mask `255.255.0.0`)\n'
                   '* PC4: `172.25.10.104` (Mask `255.255.0.0`)\n'
                   '* PC5: `172.25.10.105` (Mask `255.255.0.0`)\n'
                   '* PC6: `172.25.10.106` (Mask `255.255.0.0`)\n'
                   '\n'
                   'Verify connectivity: `ping 172.25.10.102` and `ping 172.25.10.104`.\n'
                   '\n'
                   '##### C. Class A Static Addressing:\n'
                   'Reconfigure all PCs with private Class A addresses (`10.0.0.0` through `10.255.255.255`):\n'
                   '* PC1: `10.10.10.101` (Mask `255.0.0.0`)\n'
                   '* PC2: `10.10.10.102` (Mask `255.0.0.0`)\n'
                   '* PC3: `10.10.10.103` (Mask `255.0.0.0`)\n'
                   '* PC4: `10.10.10.104` (Mask `255.0.0.0`)\n'
                   '* PC5: `10.10.10.105` (Mask `255.0.0.0`)\n'
                   '* PC6: `10.10.10.106` (Mask `255.0.0.0`)\n'
                   '\n'
                   'Verify connectivity: `ping 10.10.10.102` and `ping 10.10.10.104`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 5: Connecting to the Internet & DHCP:\n'
                   'Connect the external network line to an open switch port. Re-enable **Obtain an IP address '
                   'automatically** in TCP/IP settings. The lab DHCP server assigns live routable addresses and '
                   'default gateway/DNS parameters.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 6: Resource & File Sharing:\n'
                   '1. Create a folder in `My Documents` labeled with your name.\n'
                   '2. Right-click the folder and choose `Sharing and Security`.\n'
                   '3. Check **Share this folder on the network**.\n'
                   "4. To access a peer's shared folder over the LAN:\n"
                   '   * Click `Start` -> `Run`.\n'
                   '   * Type `\\<IP_Address>` (e.g., `\\192.168.9.2`) and press Enter.\n'
                   '5. In addition to IP addressing, test accessing shares using NetBIOS computer names:\n'
                   '   * Type `\\PC4` in the Run dialog.\n'
                   '   * Ping by computer name: `ping PC4`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'APIPA provides automatic fallback on isolated LANs, ARP prevents address collisions, and Windows '
                   'Firewall ICMP rules regulate diagnostic echo requests.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks:\n'
                   '1. Verify APIPA addressing and test inter-workstation ping across 6 PCs.\n'
                   '2. Reconfigure workstations sequentially across Class C, Class B, and Class A private subnets and '
                   'verify connectivity.\n'
                   '3. Test file sharing by IP address (`\\<IP>`) and by host name (`\\<HostName>`).\n',
        'flashcards': [   {   'answer': 'Automatic Private IP Addressing (APIPA) assigns an IP from 169.254.0.1 to '
                                        '169.254.255.254 with mask 255.255.0.0 when a PC cannot contact a DHCP server.',
                              'question': 'What is APIPA and when does Windows use it?'},
                          {   'answer': 'A host broadcasts an ARP query for the chosen address; if another host '
                                        'responds, it picks a different random address, ensuring all LAN hosts remain '
                                        'distinct.',
                              'question': 'How does ARP prevent duplicate IP collisions during APIPA '
                                          'autoconfiguration?'},
                          {   'answer': "Under Windows Firewall -> Advanced Tab -> ICMP Settings, check 'Allow "
                                        "incoming echo request'.",
                              'question': 'Which Windows Firewall setting is required for ping to function?'},
                          {   'answer': "Open Start -> Run and type '\\\\<IP_Address>' (e.g. \\\\192.168.9.2) or "
                                        "'\\\\<PC_Name>' (e.g. \\\\PC4) to browse shared folders.",
                              'question': 'How do you access shared resources on a peer workstation by IP or host '
                                          'name?'}],
        'order': 5,
        'quizzes': [   {   'correctAnswer': '169.254.0.1 to 169.254.255.254',
                           'explanation': 'When DHCP fails, Windows APIPA assigns a link-local address in the '
                                          '169.254.0.1 to 169.254.255.254 range (NetID 169.254.0.0/16).',
                           'options': [   '10.0.0.1 to 10.255.255.254',
                                          '169.254.0.1 to 169.254.255.254',
                                          '172.16.0.1 to 172.31.255.254',
                                          '192.168.1.1 to 192.168.1.254'],
                           'question': 'When a Windows PC fails to contact a DHCP server on an unconfigured switch, '
                                       'which IP address range is automatically assigned by APIPA?'},
                       {   'correctAnswer': 'ARP (Address Resolution Protocol) probe broadcasts',
                           'explanation': 'Hosts use ARP probe packets to ensure no duplicate IP address exists on the '
                                          'local link before binding an APIPA address.',
                           'options': [   'DNS dynamic zone updates',
                                          'ARP (Address Resolution Protocol) probe broadcasts',
                                          'ICMP Router Discovery',
                                          'IGMP membership reports'],
                           'question': 'What mechanism prevents multiple workstations from assigning themselves the '
                                       'same IP address during APIPA failover?'},
                       {   'correctAnswer': "'Allow incoming echo request'",
                           'explanation': "Enabling 'Allow incoming echo request' in Windows Firewall ICMP settings "
                                          'allows the PC to respond to ping packets without exposing other ports.',
                           'options': [   "'Allow incoming echo request'",
                                          "'Allow outgoing redirect'",
                                          "'Allow incoming timestamp request'",
                                          "'Allow subnet mask broadcast'"],
                           'question': 'In Windows Firewall, which specific ICMP setting must be enabled to allow '
                                       'other workstations to ping your PC?'},
                       {   'correctAnswer': '10.0.0.0 through 10.255.255.255',
                           'explanation': 'Class A private IP space spans 10.0.0.0 through 10.255.255.255 (with '
                                          'default subnet mask 255.0.0.0).',
                           'options': [   '1.0.0.0 through 1.255.255.255',
                                          '10.0.0.0 through 10.255.255.255',
                                          '172.16.0.0 through 172.31.255.255',
                                          '192.168.0.0 through 192.168.255.255'],
                           'question': 'What is the private IP address range for Class A networks used during static '
                                       'LAN reconfiguration?'},
                       {   'correctAnswer': '\\\\<IP_Address>',
                           'explanation': "Windows Universal Naming Convention (UNC) syntax uses '\\\\<IP_Address>' or "
                                          "'\\\\<HostName>' to open shared network resources.",
                           'options': [   'http://<IP_Address>/shares',
                                          '\\\\<IP_Address>',
                                          'ftp://<IP_Address>',
                                          'rdp://<IP_Address>'],
                           'question': 'In Windows, what syntax is typed into the Run dialog to access a shared '
                                       'network folder on another computer by IP address?'}],
        'title': 'Day 5 (Lab # 6): Building an advanced Switched Network and controlling an unauthorized access'},
    {   'codeSnippet': '# Windows Remote Desktop & Resource Sharing Commands\n'
                       '\n'
                       '# 1. Launch Remote Desktop Connection client:\n'
                       'mstsc\n'
                       '\n'
                       '# 2. Launch Remote Desktop directly to target IP:\n'
                       'mstsc /v:192.168.9.2\n'
                       '\n'
                       '# 3. Check active IPv4 address on target host:\n'
                       'ipconfig\n'
                       '\n'
                       '# 4. View active local file shares:\n'
                       'net share\n'
                       '\n'
                       '# 5. Connect network drive via command line:\n'
                       'net use Z: \\\\192.168.9.2\\SharedFolder',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 7: Sharing and Remote Access (Day 6)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding the concept behind remote desktop access.\n'
                   '* The student should be familiar with remote desktop access settings and file sharing security.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Shared Resources (Network Shares):\n'
                   'A shared resource or network share is a device or piece of information on a computer that can be '
                   'remotely accessed from another computer, typically via a Local Area Network (LAN) or enterprise '
                   'Intranet, as if it were a resource on the local machine.\n'
                   '\n'
                   '#### Simple File Sharing:\n'
                   "Windows operating systems let you share a computer's disks and folders with other computers on the "
                   'network using **Simple File Sharing**:\n'
                   '* If a disk or folder is shared under Simple File Sharing, everyone on the network can access it.\n'
                   '* By default, there are no individualized user permissions and no passwords.\n'
                   '* Because sharing in this way is wide open, Windows provides built-in warnings to protect against '
                   'potential security risks.\n'
                   '\n'
                   '#### Remote Desktop Services (RDP):\n'
                   'Remote Desktop Services is a core component of Microsoft Windows that allows a user to access '
                   'applications and data on a remote computer over a network using the **Remote Desktop Protocol '
                   '(RDP)**:\n'
                   '* Connect to your office/lab computer from another computer with full access to programs, files, '
                   'and resources.\n'
                   '* Applications continue running on the host machine even after disconnecting.\n'
                   '* **Session Limits**:\n'
                   '  * **Client Windows OS (XP, Vista, 7)**: Allows **only 1 session** at a time.\n'
                   '  * **Server Windows OS (2000, 2003, 2008)**: Allows **2 concurrent remote sessions plus 1 local '
                   'console session**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Part 1: Setting up File and Disk Sharing\n'
                   '\n'
                   '1. Right-click the disk or folder you want to share and select **Sharing and Security**.\n'
                   '\n'
                   '![Sharing and Security Dialog](assets/images/university/ccn/lab6_share_properties.png)\n'
                   '*Figure 1: Folder Sharing and Security properties dialog.*\n'
                   '\n'
                   '2. **Entire Disk vs. Specific Folder Warning**:\n'
                   '   * If sharing an entire drive (e.g. C:), Windows displays a warning that the entire disk and all '
                   'contained subfolders will be exposed.\n'
                   '   * **Best Practice**: Share a specific folder rather than an entire disk volume.\n'
                   '\n'
                   '![Folder Sharing Warning](assets/images/university/ccn/lab6_share_folder.png)\n'
                   '*Figure 2: Windows XP warning regarding disk sharing security.*\n'
                   '\n'
                   '3. **Network Setup Wizard Warning**:\n'
                   '   * The first time you configure sharing, Windows urges you to use the Network Setup Wizard.\n'
                   '   * The Wizard automatically enables the **Internet Connection Firewall (ICF)** / Windows '
                   'Firewall to block unauthorized Internet access while permitting LAN file sharing.\n'
                   '\n'
                   '![Network Sharing Security](assets/images/university/ccn/lab6_share_permissions.png)\n'
                   '*Figure 3: Windows file sharing enablement prompt.*\n'
                   '\n'
                   '![Firewall Sharing Warning](assets/images/university/ccn/lab6_firewall_warning.png)\n'
                   '*Figure 4: Windows Firewall file sharing security alert.*\n'
                   '\n'
                   '4. **Configuring Permissions**:\n'
                   '   * Specify a **Share name** (1-12 characters recommended for compatibility).\n'
                   '   * Check **Share this folder on the network**.\n'
                   '   * By default, network users have full access (read, write, delete).\n'
                   '   * To prevent users from modifying or deleting files, uncheck **Allow network users to change my '
                   'files**.\n'
                   '   * > **Critical Warning**: When users have full access, deleting a shared file does NOT send it '
                   'to the Recycle Bin. Once deleted over the network, it is permanently lost!\n'
                   '\n'
                   '![Network Sharing Configuration](assets/images/university/ccn/lab6_network_sharing.png)\n'
                   '*Figure 5: Setting Share name and file alteration permissions.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Part 2: Setting up the Host Computer for Remote Desktop\n'
                   '\n'
                   'Before connecting to a remote computer, you must prepare the target machine:\n'
                   '1. You must have a **user account with a password** on the host.\n'
                   '2. The computer must be configured to **accept remote connections**.\n'
                   '3. You must know the **IPv4 address** of the host.\n'
                   '\n'
                   '##### Step 1: User Accounts in Control Panel:\n'
                   '1. Open `Control Panel` -> switch to `Classic View` -> select `User Accounts`.\n'
                   '\n'
                   '![Control Panel User Accounts](assets/images/university/ccn/lab6_control_panel.png)\n'
                   '*Figure 6: Windows Control Panel User Accounts.*\n'
                   '\n'
                   '2. Ensure your user account has a password assigned (Remote Desktop will reject blank password '
                   'logins by default).\n'
                   '3. Open `Control Panel` -> `System` -> `Advanced System Settings` -> select the **`Remote`** tab.\n'
                   '4. Check **`Allow connections from computers running Remote Desktop`**.\n'
                   '5. Click `Select Users` and ensure your user account is authorized.\n'
                   '\n'
                   '![Remote Tab Settings](assets/images/university/ccn/lab6_remote_desktop.png)\n'
                   '*Figure 7: System Properties Remote tab configuration.*\n'
                   '\n'
                   '##### Step 2: Determine Host IPv4 Address:\n'
                   '1. Open Command Prompt (`cmd`) and type:\n'
                   '```bat\n'
                   'ipconfig\n'
                   '```\n'
                   '\n'
                   '![IPCONFIG Output](assets/images/university/ccn/lab6_cmd_ipconfig.png)\n'
                   '*Figure 8: Finding the host IPv4 address in ipconfig.*\n'
                   '\n'
                   '2. Record the IPv4 address (e.g. `192.168.9.2`).\n'
                   '3. Log out of the account, but **do not shut down or turn off** the computer.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Part 3: Connecting via Remote Desktop Client\n'
                   '\n'
                   '1. On the client PC, go to `Start` -> `All Programs` -> `Accessories` -> **`Remote Desktop '
                   'Connection`** (or run `mstsc`).\n'
                   '\n'
                   '![Remote Desktop Connection Dialog](assets/images/university/ccn/lab6_rdp_connect.png)\n'
                   '*Figure 9: Remote Desktop Connection login window.*\n'
                   '\n'
                   "2. Enter the host's IP address and click `Connect`.\n"
                   '3. If prompted with a security/certificate trust alert, click `Yes` / `Connect`.\n'
                   '\n'
                   '![RDP Security Credentials](assets/images/university/ccn/lab6_rdp_credentials.png)\n'
                   '*Figure 10: Remote connection credentials entry.*\n'
                   '\n'
                   '4. Enter the authorized username and password and press Enter.\n'
                   '\n'
                   '![Remote Desktop Active Session](assets/images/university/ccn/lab6_rdp_session.png)\n'
                   '*Figure 11: Active Remote Desktop session window.*\n'
                   '\n'
                   '5. You are now controlling the remote computer. To exit, click the connection bar X at the top or '
                   'choose `Start` -> `Log Off`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Part 4: Remote Desktop Advanced Options\n'
                   '\n'
                   'Click **Options** in the Remote Desktop client to configure advanced features:\n'
                   '* **Display**: Choose full-screen or custom window resolution and display color depth.\n'
                   '* **Local Resources**: Redirect and mount local printers, clipboard, and local disk drives to the '
                   'remote session for easy file copying and printing.\n'
                   '* **Programs**: Configure an application to start automatically upon login.\n'
                   '* **Experience**: Optimize performance settings based on connection bandwidth (LAN, Broadband, '
                   'Modem).\n'
                   '* **Advanced**: Configure server authentication and Remote Desktop Gateway settings.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Simple File Sharing provides open local resource sharing, while Remote Desktop Protocol (RDP) '
                   'allows full interactive graphical control of remote systems with encrypted authentication.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks:\n'
                   '1. Create and share a folder with read-only permissions, and attempt to delete a file from a peer '
                   'computer.\n'
                   '2. Enable Remote Desktop on your PC and establish an RDP session from a peer workstation.\n'
                   '3. Test local resource redirection by copying and pasting a file across the RDP clipboard.\n',
        'flashcards': [   {   'answer': 'A Windows feature that shares folders across the LAN without user permissions '
                                        'or passwords; everyone on the network has open access unless restricted.',
                              'question': 'What is Simple File Sharing and its main security risk?'},
                          {   'answer': 'Windows client editions (XP, Vista, 7) allow 1 remote session. Windows Server '
                                        'editions allow 2 concurrent remote sessions plus 1 console session.',
                              'question': 'What is the concurrent RDP session limit for Windows client vs server '
                                          'editions?'},
                          {   'answer': 'The file is permanently deleted immediately and is NOT placed into either '
                                        "computer's Recycle Bin.",
                              'question': 'What happens to a file deleted over a network share by a user with write '
                                          'permissions?'},
                          {   'answer': "A user account with a password, enabling 'Allow connections from computers "
                                        "running Remote Desktop' in System Properties -> Remote, and knowing the "
                                        "host's IPv4 address.",
                              'question': 'What are the configuration requirements to enable Remote Desktop access on '
                                          'a host PC?'}],
        'order': 6,
        'quizzes': [   {   'correctAnswer': 'One session',
                           'explanation': 'Windows client operating systems allow only one active Remote Desktop '
                                          'session at a time, whereas Windows Server editions support 2 concurrent '
                                          'remote sessions plus 1 console session.',
                           'options': [   'One session',
                                          'Two remote sessions plus one console session',
                                          'Up to five sessions',
                                          'Unlimited sessions'],
                           'question': 'How many concurrent Remote Desktop sessions are permitted on Windows client '
                                       'operating systems (XP, Vista, 7)?'},
                       {   'correctAnswer': 'Because all files and system folders on the drive become accessible to '
                                            'all network users',
                           'explanation': 'Sharing an entire disk drive exposes all files, operating system folders, '
                                          'and user directories to anyone on the network without restriction.',
                           'options': [   'Because sharing a disk disables all physical network adapters',
                                          'Because all files and system folders on the drive become accessible to all '
                                          'network users',
                                          'Because hard drives cannot format partitions while shared',
                                          'Because Windows does not support NTFS file systems over a LAN'],
                           'question': 'Why does Windows display a security warning when sharing an entire hard disk '
                                       'drive rather than a specific folder?'},
                       {   'correctAnswer': 'The file is permanently deleted and bypassed from the Recycle Bin',
                           'explanation': "The manual specifically warns: 'If a user has full access, deleting a file "
                                          "doesn't put it in the Recycle Bin. Once it's deleted, it's gone for good.'",
                           'options': [   "The file is sent to the client computer's local Recycle Bin",
                                          "The file is sent to the host computer's Recycle Bin",
                                          'The file is permanently deleted and bypassed from the Recycle Bin',
                                          'The file is quarantined by Windows Defender for 30 days'],
                           'question': 'What happens when a network user with write permissions deletes a file from a '
                                       'shared network folder?'},
                       {   'correctAnswer': 'The user account must have a password set',
                           'explanation': 'Remote Desktop requires that the user account on the target machine have a '
                                          'password configured; blank passwords are blocked by default for security.',
                           'options': [   'The account must be configured with a blank password',
                                          'The user account must have a password set',
                                          'The account must have a public static IP address registered with ICANN',
                                          'The account must belong to the anonymous IIS web group'],
                           'question': 'What prerequisite user account setting is mandatory before a host PC can '
                                       'accept incoming Remote Desktop connections?'},
                       {   'correctAnswer': 'Local Resources',
                           'explanation': "The 'Local Resources' tab configures redirection of local printers, "
                                          'clipboard, audio, and disk drives into the remote session.',
                           'options': ['Display', 'Local Resources', 'Experience', 'Programs'],
                           'question': 'In the Remote Desktop Connection client options, which tab allows redirecting '
                                       'local printers, clipboard, and drives into the remote session?'}],
        'title': 'Day 6 (Lab # 7): Sharing and Remote Access'}]



DAYS_PART2 = [   {   'codeSnippet': '# Windows Command Prompt: ARP Management Commands\n'
                       '\n'
                       '# 1. Display the current ARP table entries:\n'
                       'arp -a\n'
                       '\n'
                       '# 2. Display the ARP table for a specific network interface:\n'
                       'arp -a -N 192.168.9.1\n'
                       '\n'
                       '# 3. Delete all entries from the ARP table:\n'
                       'arp -d\n'
                       '\n'
                       '# 4. Delete the ARP entry with a specific IP address:\n'
                       'arp -d 19.100.85.209\n'
                       '\n'
                       '# 5. Add a static ARP mapping (IP to MAC):\n'
                       'arp -s 19.100.85.209 00-aa-bb-62-11-06',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 8: Address Resolution Protocol (ARP) (Day 7)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding the function of **ARP** and **RARP**.\n'
                   '* Knows how the ARP protocol works.\n'
                   '* Deals with essential ARP utility commands.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Logical vs. Physical Addressing:\n'
                   'Delivery of a packet to a host or a router requires two levels of addressing: **logical** (Layer 3 '
                   'IP address) and **physical** (Layer 2 MAC hardware address). We need to be able to map a logical '
                   'address to its corresponding physical address and vice versa.\n'
                   '\n'
                   '* **ARP (Address Resolution Protocol)**: Used to find the physical address (MAC) of the next hop '
                   'on the network given a known logical address (IP).\n'
                   '* **RARP (Reverse Address Resolution Protocol)**: Finds the logical address (IP) for a machine '
                   'that only knows its physical address (MAC) (e.g. diskless workstations).\n'
                   '\n'
                   '![ARP & RARP Concept](assets/images/university/ccn/lab7_arp_concept.png)\n'
                   '*Figure 1: Layer 2 to Layer 3 address mapping concept (ARP vs. RARP).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### ARP Table Architecture:\n'
                   'The ARP table is a local cache database that lists associated MAC and IP addresses on a host or '
                   'router:\n'
                   '* **Layer 2 to Layer 3 mapping**: Connects hardware adapters with network layer destinations.\n'
                   '* **Contains two types of entries**:\n'
                   '  1. **Dynamic ARP table entries**: Created automatically when a device sends or receives an ARP '
                   'broadcast; entries time out and expire after an aging timer.\n'
                   '  2. **Static ARP table entries**: Created manually by an administrator using the `arp -s` '
                   'command; entries remain permanently in the table until reboot or manual deletion.\n'
                   '\n'
                   "The **ARP utility** provides a way of obtaining information from and manipulating a device\\'s ARP "
                   'table.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### How Does ARP Work?\n'
                   '\n'
                   'When a host wants to send an IP datagram to another host on the same local network:\n'
                   '1. It first checks its local ARP cache table to see if the physical address is already known.\n'
                   '2. If the physical address is found, the frame is encapsulated and sent directly.\n'
                   '3. If the physical address is not found in the table, an **ARP Request** is initiated.\n'
                   '\n'
                   '![ARP Request Broadcast](assets/images/university/ccn/lab7_arp_request.png)\n'
                   '*Figure 2: ARP Request (Broadcast to `FF:FF:FF:FF:FF:FF`).*\n'
                   '\n'
                   '#### ARP Request:\n'
                   '* The source host generates an ARP Request packet containing its own IP, its own MAC, and the '
                   "destination host\\'s IP address.\n"
                   '* The frame is sent as a **broadcast** to physical address **`FF-FF-FF-FF-FF-FF`**.\n'
                   '* Every machine on the local network segment receives and processes the request.\n'
                   '* All machines whose IP does not match discard the packet silently.\n'
                   '\n'
                   '![ARP Reply Unicast](assets/images/university/ccn/lab7_arp_reply.png)\n'
                   '*Figure 3: ARP Reply (Unicast direct response).*\n'
                   '\n'
                   '#### ARP Reply:\n'
                   '* The machine that owns the queried IP address creates an ARP Reply packet.\n'
                   '* It fills in its physical MAC address and sends the reply as a **unicast** frame directly back to '
                   'the requesting source.\n'
                   '* The source host receives the reply, updates its local ARP table cache, and transmits the '
                   'buffered data packet.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Inspecting and Manipulating the ARP Table:\n'
                   '\n'
                   'Open the Windows Command Prompt (`cmd`) and execute the following commands:\n'
                   '\n'
                   '![ARP Table Output](assets/images/university/ccn/lab7_arp_table.png)\n'
                   '*Figure 4: Windows ARP cache table output.*\n'
                   '\n'
                   '1. **Display Active Entries**:\n'
                   '```bat\n'
                   'arp -a\n'
                   '```\n'
                   '* Displays the current active ARP cache entries, showing:\n'
                   '  * **Internet Address**: The target logical IPv4 address.\n'
                   '  * **Physical Address**: The corresponding 48-bit MAC address.\n'
                   '  * **Type**: `dynamic` (learned automatically) or `static` (broadcast/manually set).\n'
                   '\n'
                   '2. **Delete All Entries**:\n'
                   '```bat\n'
                   'arp -d\n'
                   '```\n'
                   '* Clears all dynamic entries from the ARP table cache.\n'
                   '\n'
                   '3. **Delete a Specific Entry**:\n'
                   '```bat\n'
                   'arp -d 19.100.85.209\n'
                   '```\n'
                   '* Deletes the specific ARP mapping for IP `19.100.85.209`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'ARP provides essential glue between Layer 3 logical IP routing and Layer 2 physical frame delivery '
                   'on Ethernet LANs using dynamic broadcast requests and unicast replies.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '1. Try adding a static ARP entry:\n'
                   '```bat\n'
                   'arp -s 19.100.85.209 00-aa-bb-62-11-06\n'
                   '```\n'
                   '*What is its function? (It binds the IP permanently to the given MAC address, bypassing broadcast '
                   'discovery).*\n'
                   '\n'
                   '2. When you enter `arp -a`, what is the meaning of the entry:\n'
                   '```text\n'
                   'Internet Address: 255.255.255.255\n'
                   'Physical Address: ff-ff-ff-ff-ff-ff\n'
                   'Type:             static\n'
                   '```\n'
                   '*What is its significance? (It represents the local broadcast address; any packet destined for '
                   '`255.255.255.255` is transmitted as an Ethernet broadcast to all network nodes).*',
        'flashcards': [   {   'answer': 'ARP (Address Resolution Protocol) resolves a known logical IP address into a '
                                        'physical MAC address. RARP (Reverse ARP) resolves a known physical MAC '
                                        'address into a logical IP address.',
                              'question': 'What is the primary difference between ARP and RARP?'},
                          {   'answer': 'Dynamic entries (learned automatically through network broadcast queries and '
                                        "aged out over time) and Static entries (manually configured with 'arp -s' and "
                                        'persistent until reboot).',
                              'question': 'What are the two types of ARP table entries?'},
                          {   'answer': 'ARP Request is a broadcast packet sent to MAC address FF:FF:FF:FF:FF:FF '
                                        'asking who owns an IP; ARP Reply is a unicast packet sent directly back to '
                                        "the requester containing the target's MAC address.",
                              'question': 'What happens during an ARP Request versus an ARP Reply?'},
                          {   'answer': "'arp -a' displays all ARP cache entries; 'arp -d' clears/deletes ARP entries; "
                                        "'arp -s <ip> <mac>' creates a permanent static ARP mapping.",
                              'question': 'What do the commands arp -a, arp -d, and arp -s do?'}],
        'order': 7,
        'quizzes': [   {   'correctAnswer': 'To resolve a known logical IP address into its corresponding physical MAC '
                                            'address',
                           'explanation': 'ARP maps a known Layer 3 logical IP address to its corresponding Layer 2 '
                                          'physical MAC address on a local area network.',
                           'options': [   'To resolve a known logical IP address into its corresponding physical MAC '
                                          'address',
                                          'To assign dynamic IP addresses to client workstations',
                                          'To route packets across autonomous system boundaries',
                                          'To translate domain names into IP addresses'],
                           'question': 'What is the primary function of the Address Resolution Protocol (ARP)?'},
                       {   'correctAnswer': 'FF:FF:FF:FF:FF:FF',
                           'explanation': 'ARP requests are broadcast to all hosts on the local network segment using '
                                          'the layer 2 broadcast address FF:FF:FF:FF:FF:FF.',
                           'options': [   '00:00:00:00:00:00',
                                          'FF:FF:FF:FF:FF:FF',
                                          '01:00:5E:00:00:01',
                                          "The default gateway's MAC address"],
                           'question': 'Which destination MAC address is used by an ARP Request packet when querying '
                                       'the local network?'},
                       {   'correctAnswer': 'arp -a',
                           'explanation': "The 'arp -a' command displays current active ARP table entries, showing "
                                          'mapped IP addresses, physical MAC addresses, and entry types.',
                           'options': ['arp -d', 'arp -a', 'arp -s', 'arp -v'],
                           'question': 'Which command displays the contents of the local ARP cache table in Windows?'},
                       {   'correctAnswer': 'Deletes all dynamic entries from the ARP table',
                           'explanation': "The command 'arp -d' deletes all dynamic entries from the ARP cache table.",
                           'options': [   'Displays detailed packet statistics for the ARP daemon',
                                          'Deletes all dynamic entries from the ARP table',
                                          'Disables ARP address resolution on all interfaces',
                                          'Drops incoming broadcast packets'],
                           'question': "What is the function of the command 'arp -d' without additional parameters?"},
                       {   'correctAnswer': 'Dynamic entries are learned automatically and age out, whereas static '
                                            'entries are manually entered and persist until reboot',
                           'explanation': 'Dynamic ARP entries are automatically added via ARP broadcast requests and '
                                          'replies and time out after an aging timer, while static entries are entered '
                                          'manually and do not expire.',
                           'options': [   'Dynamic entries are learned automatically and age out, whereas static '
                                          'entries are manually entered and persist until reboot',
                                          'Dynamic entries are stored in ROM, while static entries are stored in NVRAM',
                                          'Dynamic entries are used for multicast, while static entries are used for '
                                          'unicast',
                                          'Dynamic entries require an external DNS server'],
                           'question': 'What is the primary difference between dynamic and static entries in an ARP '
                                       'table?'}],
        'title': 'Day 7 (Lab # 8): Address Resolution Protocol (ARP)'},
    {   'codeSnippet': '# Wireshark Capture Filter Syntax (pcap / tcpdump)\n'
                       '\n'
                       '# 1. Capture all traffic to and from specific MAC address:\n'
                       'ether host 08:00:08:15:ca:fe\n'
                       '\n'
                       '# 2. Capture all traffic to and from specific IP address:\n'
                       'host 192.168.0.10\n'
                       '\n'
                       '# 3. Capture HTTP traffic on TCP port 80:\n'
                       'tcp port 80\n'
                       '\n'
                       '# 4. Compound filter (traffic to/from 192.168.0.10 except HTTP):\n'
                       'host 192.168.0.10 and not port 80\n'
                       '\n'
                       '# 5. Capture only traffic between two specific subnets:\n'
                       'src net 192.168.10.0/24 and dst net 192.168.20.0/24',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 9: Wireshark (Day 8)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Using Wireshark to monitor and capture traffic on the LAN.\n'
                   '* Browse and analyze packets from a live network or from a previously saved capture file.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '**Wireshark** is a free packet sniffer computer application. It is used for network '
                   'troubleshooting, analysis, software and communications protocol development, and education.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Step 1: Starting Wireshark & Interface Overview\n'
                   '\n'
                   'When Wireshark launches, it provides three main panes:\n'
                   '\n'
                   '![Wireshark Main Interface](assets/images/university/ccn/lab8_wireshark.png)\n'
                   '*Figure 1: Wireshark packet capture main window.*\n'
                   '\n'
                   '1. **Top Pane (Packet List Pane)**: Displays a summary of each captured packet (Packet number, '
                   'Time offset, Source IP, Destination IP, Protocol, Length, and Info summary).\n'
                   '2. **Middle Pane (Packet Details Pane)**: Displays the hierarchical protocol tree breakdown '
                   '(Frame, Ethernet II, IPv4, TCP/UDP, Application data) for the packet selected in the top pane.\n'
                   '3. **Bottom Pane (Packet Bytes Pane)**: Displays the raw hexadecimal and ASCII dump of the packet '
                   'selected in the top pane, highlighting selected fields.\n'
                   '\n'
                   '![Packet List Pane](assets/images/university/ccn/lab8_packet_list.png)\n'
                   '*Figure 2: Wireshark Packet List pane.*\n'
                   '\n'
                   '![Packet Details Pane](assets/images/university/ccn/lab8_packet_details.png)\n'
                   '*Figure 3: Wireshark Packet Details hierarchical tree pane.*\n'
                   '\n'
                   '#### Toolbars of Interest:\n'
                   '* **Menu Items**: Drop-down menus for all operations.\n'
                   '* **Main Toolbar**: Shortcut icons to start, stop, restart, save, and reload captures.\n'
                   '* **Filter Toolbar**: Contains the "Filter:" dialog button, text box for filter strings, and the '
                   '"Clear" button.\n'
                   '* **Status Bar**: Displays interface capture statistics and file details.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 2: Capturing Packets in Wireshark\n'
                   '\n'
                   'Before capturing, the capture interface must be specified:\n'
                   '1. Navigate to `Capture` -> `Interfaces` to display active network adapters.\n'
                   '2. Click `Options` next to your active adapter to open the **Capture Preferences** dialog.\n'
                   '\n'
                   '![Capture Preferences](assets/images/university/ccn/lab8_capture_preferences.png)\n'
                   '*Figure 4: Wireshark Capture Preferences configuration dialog.*\n'
                   '\n'
                   '#### Key Capture Preferences Options:\n'
                   '\n'
                   '##### Filtering Options:\n'
                   '* **Capture packets in promiscuous mode**: Usually a network card only captures traffic addressed '
                   'to its own MAC address. Enabling promiscuous mode allows the NIC to capture all traffic visible on '
                   'the physical wire.\n'
                   '* **Limit each packet to xy bytes**: Limits the maximum captured size per packet (useful to save '
                   'disk space if only headers are needed).\n'
                   '* **Capture Filter**: Pre-filters incoming frames using pcap syntax to reduce capture file size.\n'
                   '\n'
                   '##### Storing Options:\n'
                   '* **File**: Specifies the disk file to which captured data is written.\n'
                   '* **Use multiple files**: Creates multiple sequential files with timestamped names (e.g. '
                   '`/foo_00001_20040205110102.cap`) for long-term captures.\n'
                   '\n'
                   '##### Stop Condition Options:\n'
                   '* Allows automatically stopping the capture after a specified number of packets, megabytes, or '
                   'seconds.\n'
                   '\n'
                   '##### Display While Capturing Options:\n'
                   '* **Update list of packets in real time**: Immediately displays packets in the main window as they '
                   'are received.\n'
                   '\n'
                   '![Capture Progress](assets/images/university/ccn/lab8_capture_progress.png)\n'
                   '*Figure 5: Wireshark live packet capture progress dialog.*\n'
                   '\n'
                   '![Capture Results](assets/images/university/ccn/lab8_capture_results.png)\n'
                   '*Figure 6: Live capture results overview.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 3: Viewing and Saving Captured Packets\n'
                   '\n'
                   '* To view packet details, click any row in the packet list pane.\n'
                   '* To save captures, select `File` -> `Save As...`.\n'
                   '* The standard file extension for capture files is **`.cap`** or **`.pcap`** (or `.cap.gz` for '
                   'compressed files).\n'
                   '* Open saved files via `File` -> `Open...`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 4: Packet Filtering in Wireshark\n'
                   '\n'
                   'Wireshark provides two distinct filtering mechanisms:\n'
                   '1. **Capture Filters**: Applied *during capture* using **pcap (libpcap / WinPcap)** filter syntax. '
                   'Reduces capture file size on high-traffic networks.\n'
                   '2. **Display Filters**: Applied *after capture* using Wireshark display syntax to show or hide '
                   'packets without altering the captured file.\n'
                   '\n'
                   '#### Capture Filter Syntax & Examples:\n'
                   '\n'
                   'A capture filter takes the form of primitive expressions connected by conjunctions (`and`, `or`, '
                   '`not`):\n'
                   '\n'
                   '##### 1. Filter by MAC Address:\n'
                   'Capture all traffic to and from Ethernet MAC address `08:00:08:15:ca:fe`:\n'
                   '```text\n'
                   'ether host 08:00:08:15:ca:fe\n'
                   '```\n'
                   '\n'
                   '![Filter by MAC](assets/images/university/ccn/lab8_filter_mac.png)\n'
                   '*Figure 7: Capture filter for specific Ethernet MAC address.*\n'
                   '\n'
                   '##### 2. Filter by IP Address:\n'
                   'Capture all traffic to and from IP address `192.168.0.10`:\n'
                   '```text\n'
                   'host 192.168.0.10\n'
                   '```\n'
                   '\n'
                   '![Filter by IP](assets/images/university/ccn/lab8_filter_ip.png)\n'
                   '*Figure 8: Capture filter for specific IP address.*\n'
                   '\n'
                   '##### 3. Filter by TCP Port:\n'
                   'Capture all traffic to and from TCP port 80 (HTTP):\n'
                   '```text\n'
                   'tcp port 80\n'
                   '```\n'
                   '\n'
                   '![Filter by Port 80](assets/images/university/ccn/lab8_filter_port80.png)\n'
                   '*Figure 9: Capture filter for TCP port 80.*\n'
                   '\n'
                   '##### 4. Combined Filter:\n'
                   'Capture all traffic to and from `192.168.0.10` except HTTP:\n'
                   '```text\n'
                   'host 192.168.0.10 and not port 80\n'
                   '```\n'
                   '\n'
                   '![Combined Filter](assets/images/university/ccn/lab8_filter_combined.png)\n'
                   '*Figure 10: Compound capture filter.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Wireshark provides deep packet inspection across all OSI layers. Using promiscuous mode and pcap '
                   'capture filters enables precise network troubleshooting and protocol analysis.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks:\n'
                   '1. Capture packets for 2-3 minutes while browsing websites, and identify DNS queries and HTTP GET '
                   'requests.\n'
                   '2. Configure a capture filter to capture only ICMP echo traffic: `icmp`.\n'
                   '3. Save the capture session as a `.cap` file and reload it in Wireshark.',
        'flashcards': [   {   'answer': 'Top Pane (Packet List - summary of all captured packets), Middle Pane (Packet '
                                        'Details - protocol header tree view), and Bottom Pane (Packet Bytes - '
                                        'hexadecimal and ASCII payload dump).',
                              'question': 'What are the three primary viewing panes in Wireshark?'},
                          {   'answer': 'It configures the network adapter to capture and inspect all packets passing '
                                        'across the physical transmission medium, rather than discarding packets '
                                        'addressed to other MAC addresses.',
                              'question': "What does 'promiscuous mode' do in packet sniffing?"},
                          {   'answer': 'Capture Filters use libpcap syntax and filter packets before writing to disk '
                                        'during capture; Display Filters use Wireshark display syntax and filter '
                                        'previously captured packets on screen without deleting them.',
                              'question': 'How does a Capture Filter differ from a Display Filter?'},
                          {   'answer': "'host 192.168.0.10' (traffic to/from IP), 'ether host 08:00:08:15:ca:fe' "
                                        "(traffic to/from MAC), 'tcp port 80' (HTTP traffic), 'host 192.168.0.10 and "
                                        "not port 80' (compound filter).",
                              'question': 'What are common examples of Wireshark capture filters?'}],
        'order': 8,
        'quizzes': [   {   'correctAnswer': 'Middle pane (Packet Details pane)',
                           'explanation': "Wireshark's middle pane is the Packet Details pane, displaying protocol "
                                          'headers (Ethernet, IP, TCP/UDP) in an expandable tree view.',
                           'options': [   'Top pane (Packet List pane)',
                                          'Middle pane (Packet Details pane)',
                                          'Bottom pane (Packet Bytes pane)',
                                          'Status Toolbar pane'],
                           'question': 'In the Wireshark packet analysis interface, which pane displays the '
                                       'hierarchical protocol tree breakdown of the selected packet?'},
                       {   'correctAnswer': 'To allow the network card to capture all traffic visible on the wire, not '
                                            'just packets addressed to its own MAC address',
                           'explanation': 'In promiscuous mode, the NIC passes all incoming network frames to the '
                                          'operating system rather than discarding frames not addressed to its own MAC '
                                          'address.',
                           'options': [   'To limit packet capture to encrypted SSL/TLS traffic only',
                                          'To allow the network card to capture all traffic visible on the wire, not '
                                          'just packets addressed to its own MAC address',
                                          'To compress the captured packets before saving to disk',
                                          'To prevent packet collisions on the local switch port'],
                           'question': "What is the purpose of enabling 'Capture packets in promiscuous mode' in "
                                       'Wireshark Capture Preferences?'},
                       {   'correctAnswer': 'host 192.168.0.10',
                           'explanation': "Wireshark capture filters use libpcap/tcpdump syntax where 'host "
                                          "192.168.0.10' matches all traffic to and from the specified IP address.",
                           'options': [   'ip.addr == 192.168.0.10',
                                          'host 192.168.0.10',
                                          'filter ip 192.168.0.10',
                                          'tcp.port == 192.168.0.10'],
                           'question': 'Which capture filter expression in Wireshark captures all traffic to and from '
                                       'the IP address 192.168.0.10?'},
                       {   'correctAnswer': 'Capture filters are applied before capture using pcap syntax to reduce '
                                            'file size, while display filters are applied after capture using '
                                            'Wireshark syntax',
                           'explanation': 'Capture filters use libpcap syntax and filter incoming frames before they '
                                          'are written to disk, whereas display filters filter which packets are '
                                          'visible on screen without deleting collected packets.',
                           'options': [   'Capture filters are applied before capture using pcap syntax to reduce file '
                                          'size, while display filters are applied after capture using Wireshark '
                                          'syntax',
                                          'Capture filters only work with wireless interfaces, while display filters '
                                          'work with Ethernet',
                                          'Capture filters cannot filter IP addresses',
                                          'Display filters permanently discard filtered packets from the capture file'],
                           'question': 'How does a Capture Filter differ technically from a Display Filter in '
                                       'Wireshark?'},
                       {   'correctAnswer': '.pcap / .cap',
                           'explanation': "The common file format for Wireshark packet capture files is '.cap' or "
                                          "'.pcap' (packet capture format).",
                           'options': ['.log', '.pcap / .cap', '.txt', '.xml'],
                           'question': 'What is the standard file extension used by Wireshark for saving raw captured '
                                       'packet data?'}],
        'title': 'Day 8 (Lab # 9): Wireshark'},
    {   'codeSnippet': '# Cisco IOS: EXEC Modes & Configuration Commands\n'
                       '\n'
                       '# 1. Enter Privileged EXEC mode:\n'
                       'Router> enable\n'
                       'Router#\n'
                       '\n'
                       '# 2. Return to User EXEC mode:\n'
                       'Router# disable\n'
                       'Router>\n'
                       '\n'
                       '# 3. View running configuration in RAM:\n'
                       'Router# show running-config\n'
                       '\n'
                       '# 4. View startup configuration in NVRAM:\n'
                       'Router# show startup-config\n'
                       '\n'
                       '# 5. Save running configuration to NVRAM:\n'
                       'Router# copy running-config startup-config\n'
                       '\n'
                       '# 6. Backup configuration to a TFTP server:\n'
                       'Router# copy running-config tftp\n'
                       '\n'
                       '# 7. Erase startup configuration from NVRAM:\n'
                       'Router# erase startup-config',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 10: Introduction to the Cisco IOS (Day 9)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding and configuring the Cisco Internetwork Operating System (IOS).\n'
                   '* Connecting to a router.\n'
                   '* Bringing up a router and observing the boot sequence.\n'
                   '* Logging into a router.\n'
                   '* Understanding router CLI prompts and EXEC modes.\n'
                   '* Performing CLI editing and contextual help features.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   'The **IOS (Internetwork Operating System)** is the proprietary operating system that runs Cisco '
                   'routers and switches. It provides the command-line interface (CLI) used to configure, verify, and '
                   'troubleshoot network devices.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Connecting to a Cisco Router:\n'
                   '\n'
                   'There are three primary ways to connect to a Cisco router for configuration:\n'
                   '1. **Console Port (Out-of-Band)**:\n'
                   '   * An RJ-45 (8-pin modular) port located on the back panel of the router.\n'
                   "   * Connected using a rollover cable with an RJ-45 to DB-9 adapter to a computer\\'s serial COM "
                   'port.\n'
                   '   * By default, there is no password set.\n'
                   '2. **Auxiliary (AUX) Port (Out-of-Band)**:\n'
                   '   * An RJ-45 port allowing modem dial-up connection to configure a remote router if the network '
                   'is down.\n'
                   '3. **Telnet / SSH (In-Band)**:\n'
                   '   * A terminal program that connects over an active network interface (Ethernet or Serial) once '
                   'IP addressing is configured.\n'
                   '\n'
                   '![Cisco 2600 External Ports](assets/images/university/ccn/lab9_router_ports.png)\n'
                   '*Figure 1: External connections and interfaces on a Cisco 2600 Series router.*\n'
                   '\n'
                   '![Console Connection](assets/images/university/ccn/lab9_router_console.png)\n'
                   '*Figure 2: Computer terminal console connection using rollover cable.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Bringing Up a Router (The Boot Sequence):\n'
                   '\n'
                   'When a Cisco router powers on, it executes the following initialization steps:\n'
                   '1. **Power-On Self-Test (POST)**: Runs diagnostic code stored in ROM to verify CPU, memory, and '
                   'interface circuitry.\n'
                   '2. **Bootstrap Loader**: Finds and loads the Cisco IOS from **Flash memory** (electronically '
                   'erasable programmable read-only memory - EEPROM).\n'
                   '3. **Decompression**: The IOS image is decompressed into volatile **RAM** and starts running.\n'
                   '4. **Configuration Loading**: The IOS searches **Non-Volatile RAM (NVRAM)** for a valid '
                   '`startup-config` file.\n'
                   '5. **Setup Mode**: If no configuration is found in NVRAM, the router enters interactive **Setup '
                   'Mode**.\n'
                   '\n'
                   '![Router Boot Sequence](assets/images/university/ccn/lab9_router_boot.png)\n'
                   '*Figure 3: Cisco IOS boot stages (ROM -> Flash -> NVRAM -> RAM).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Step 1: Connecting Console Interfaces & Terminal Configuration:\n'
                   "1. Connect the rollover cable to the router\\'s console port.\n"
                   "2. Attach the DB-9 female adapter to the PC\\'s COM port.\n"
                   '3. Open HyperTerminal or PuTTY and configure the serial communication settings:\n'
                   '   * **Bits per second (Baud rate)**: `9600`\n'
                   '   * **Data bits**: `8`\n'
                   '   * **Parity**: `None`\n'
                   '   * **Stop bits**: `1`\n'
                   '   * **Flow control**: `None`\n'
                   '   *(9600-8-N-1)*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 2: Logging into the Router & CLI Prompts:\n'
                   '\n'
                   'Press Enter to display the CLI prompt:\n'
                   '```text\n'
                   'Router>\n'
                   '```\n'
                   '* **User EXEC Mode (`Router>`)**: Used primarily to view statistics and status messages. Does not '
                   'permit configuration changes.\n'
                   '\n'
                   'To enter **Privileged EXEC Mode**, issue the `enable` command:\n'
                   '```text\n'
                   'Router> enable\n'
                   'Router#\n'
                   '```\n'
                   '* **Privileged EXEC Mode (`Router#`)**: Allows full configuration changes, debugging, and viewing '
                   'sensitive system files.\n'
                   '\n'
                   'To return to User EXEC mode:\n'
                   '```text\n'
                   'Router# disable\n'
                   'Router>\n'
                   '```\n'
                   '\n'
                   'To exit the console session:\n'
                   '```text\n'
                   'Router> logout\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 3: Verifying Configuration Files:\n'
                   '\n'
                   '1. **Verify Active Configuration in RAM**:\n'
                   '```text\n'
                   'Router# show running-config\n'
                   '```\n'
                   '*(Displays the current running configuration stored in volatile RAM).*\n'
                   '\n'
                   '![Show Version Output](assets/images/university/ccn/lab9_show_version.png)\n'
                   '*Figure 4: Cisco IOS show version output detailing system specs and memory.*\n'
                   '\n'
                   '2. **Verify Stored Configuration in NVRAM**:\n'
                   '```text\n'
                   'Router# show startup-config\n'
                   '```\n'
                   '*(Displays the configuration stored in NVRAM that loads on system boot).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 4: Configuration File Management:\n'
                   '\n'
                   '1. **Save Running Configuration to NVRAM**:\n'
                   '```text\n'
                   'Router# copy running-config startup-config\n'
                   'Destination filename [startup-config]? [Enter]\n'
                   'Building configuration...\n'
                   '[OK]\n'
                   '```\n'
                   '\n'
                   '2. **Backup Configuration to a TFTP Server**:\n'
                   '```text\n'
                   'Router# copy running-config tftp\n'
                   'Address or name of remote host []? 192.168.0.120\n'
                   'Destination filename [router-confg]? todd1-confg\n'
                   '!!\n'
                   '487 bytes copied in 12.236 secs (40 bytes/sec)\n'
                   '```\n'
                   '\n'
                   '3. **Erase Configuration from NVRAM**:\n'
                   '```text\n'
                   'Router# erase startup-config\n'
                   'Erasing the nvram filesystem will remove all files!\n'
                   'Continue? [confirm] [Enter]\n'
                   '[OK]\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 5: Essential CLI Editing & Shortcut Keys:\n'
                   '\n'
                   '| Shortcut Key | Function |\n'
                   '|:---|:---|\n'
                   '| **`Backspace`** | Deletes a single character behind the cursor. |\n'
                   '| **`Ctrl + U`** | Erases the entire current line. |\n'
                   '| **`Ctrl + Z`** | Immediately exits configuration mode and returns to Privileged EXEC '
                   '(`Router#`). |\n'
                   '| **`Tab`** | Auto-completes a partially typed command. |\n'
                   '| **`Up Arrow`** | Recalls previously executed commands from history. |\n'
                   '| **`?`** | Provides context-sensitive command help. |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'The Cisco IOS provides hierarchical EXEC modes for device security. Configurations active in RAM '
                   'must be committed to NVRAM via `copy run start` to survive device restarts.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '1. Establish a console connection to the lab router using 9600-8-N-1 settings.\n'
                   '2. Enter privileged mode, inspect `show running-config` and `show version`, and determine the '
                   'exact IOS version and NVRAM size.\n'
                   '3. Save the running configuration to NVRAM with `copy run start`.',
        'flashcards': [   {   'answer': 'Console port (out-of-band via rollover cable and serial terminal), Auxiliary '
                                        'port (out-of-band dial-up modem access), and Telnet/SSH (in-band network '
                                        'access over active interfaces).',
                              'question': 'What are the three primary methods for connecting to a Cisco router?'},
                          {   'answer': '1. POST runs from ROM; 2. Bootstrap loads IOS from Flash EEPROM into RAM; 3. '
                                        'IOS searches NVRAM for startup-config; 4. If no configuration exists in '
                                        'NVRAM, router enters Setup mode.',
                              'question': "What is the sequence of steps in a Cisco router's boot process?"},
                          {   'answer': '9600 baud, 8 data bits, 1 stop bit, no parity, no flow control (9600-8-N-1).',
                              'question': 'What are the standard HyperTerminal connection parameters for Cisco console '
                                          'ports?'},
                          {   'answer': 'User EXEC mode (Router>) allows basic monitoring and viewing statistics; '
                                        'Privileged EXEC mode (Router#, entered with enable) allows full '
                                        'configuration, testing, and debugging.',
                              'question': 'What is the difference between User EXEC mode and Privileged EXEC mode?'}],
        'order': 9,
        'quizzes': [   {   'correctAnswer': 'Console port',
                           'explanation': 'The console port is an RJ-45 connection on the router used for direct local '
                                          'out-of-band management via a rollover cable and terminal emulator.',
                           'options': ['FastEthernet 0/0 port', 'Console port', 'Auxiliary port', 'Serial 0/0 port'],
                           'question': 'What type of port on a Cisco router is used for local out-of-band management '
                                       'using a rollover cable with no default password?'},
                       {   'correctAnswer': '9600 baud, 8 data bits, no parity, 1 stop bit, no flow control '
                                            '(9600-8-N-1)',
                           'explanation': 'Standard Cisco console serial parameters are 9600 bits per second, 8 data '
                                          'bits, no parity, 1 stop bit, and no flow control.',
                           'options': [   '9600 baud, 8 data bits, no parity, 1 stop bit, no flow control (9600-8-N-1)',
                                          '115200 baud, 7 data bits, even parity, 2 stop bits, hardware flow control',
                                          '2400 baud, 8 data bits, odd parity, 1 stop bit, XON/XOFF',
                                          '4800 baud, 7 data bits, no parity, 1 stop bit, RTS/CTS'],
                           'question': 'What is the correct baud rate and serial communication parameter setting in '
                                       'HyperTerminal for connecting to a Cisco router console?'},
                       {   'correctAnswer': 'Non-Volatile RAM (NVRAM)',
                           'explanation': 'The router loads the Cisco IOS from Flash memory and the startup-config '
                                          'configuration file from NVRAM.',
                           'options': [   'Flash memory (EEPROM)',
                                          'Non-Volatile RAM (NVRAM)',
                                          'Dynamic RAM (RAM)',
                                          'Boot ROM'],
                           'question': 'In the Cisco router initialization sequence, where does the router load its '
                                       'startup configuration file from?'},
                       {   'correctAnswer': 'Router#',
                           'explanation': 'Router> represents User EXEC mode, while Router# represents Privileged EXEC '
                                          'mode (entered via the enable command).',
                           'options': ['Router>', 'Router#', 'Router(config)#', 'Router(config-if)#'],
                           'question': 'Which Cisco IOS prompt indicates that the router is in Privileged EXEC mode?'},
                       {   'correctAnswer': 'copy running-config startup-config',
                           'explanation': "The command 'copy running-config startup-config' (or 'copy run start') "
                                          'saves the active RAM configuration to NVRAM so it persists across reboots.',
                           'options': [   'copy startup-config running-config',
                                          'copy running-config startup-config',
                                          'save config nvram',
                                          'write memory erase'],
                           'question': 'Which command saves the active running configuration from RAM into NVRAM as '
                                       'the backup startup configuration?'}],
        'title': 'Day 9 (Lab # 10): Introduction to the Cisco IOS'},
    {   'codeSnippet': '# Cisco Router: Basic Administrative & Interface Configuration\n'
                       '\n'
                       '# 1. Hostname and MOTD Banner:\n'
                       'Router# config t\n'
                       'Router(config)# hostname Lab_A\n'
                       'Lab_A(config)# banner motd # Authorized Access Only! #\n'
                       '\n'
                       '# 2. Securing Privileged EXEC Mode:\n'
                       'Lab_A(config)# enable secret cisco123\n'
                       '\n'
                       '# 3. Securing Console and VTY Lines:\n'
                       'Lab_A(config)# line console 0\n'
                       'Lab_A(config-line)# password ciscocon\n'
                       'Lab_A(config-line)# login\n'
                       'Lab_A(config-line)# line vty 0 4\n'
                       'Lab_A(config-line)# password ciscovty\n'
                       'Lab_A(config-line)# login\n'
                       '\n'
                       '# 4. Encrypt Plaintext Passwords:\n'
                       'Lab_A(config)# service password-encryption\n'
                       '\n'
                       '# 5. Configuring FastEthernet LAN Interface:\n'
                       'Lab_A(config)# interface FastEthernet 0/0\n'
                       'Lab_A(config-if)# ip address 192.168.10.1 255.255.255.0\n'
                       'Lab_A(config-if)# no shutdown\n'
                       '\n'
                       '# 6. Configuring Serial DCE WAN Interface:\n'
                       'Lab_A(config)# interface Serial 0/0\n'
                       'Lab_A(config-if)# ip address 192.168.20.1 255.255.255.0\n'
                       'Lab_A(config-if)# clock rate 64000\n'
                       'Lab_A(config-if)# no shutdown',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 11: Cisco Routers- Basic Configurations (Day 10)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Administrative configurations: hostnames, banners, and descriptions.\n'
                   '* Securing the router with console, auxiliary, Telnet (VTY), and enable passwords.\n'
                   '* Encrypting passwords using `service password-encryption`.\n'
                   '* Interface configuration: FastEthernet LAN and Serial WAN.\n'
                   '* Clock rate configuration on DCE serial interfaces.\n'
                   '* Verifying interfaces and troubleshooting with `show interfaces`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Router Administrative Configuration:\n'
                   'A Cisco router requires basic administrative settings to establish its identity on the '
                   'internetwork:\n'
                   '* **Hostname**: Uniquely identifies the router at the CLI prompt (`hostname <name>`).\n'
                   '* **Banner MOTD (Message of the Day)**: Displays a legal or informational warning to anyone '
                   'connecting via console, aux, or Telnet.\n'
                   '\n'
                   '```text\n'
                   'Router(config)# hostname Mohammad\n'
                   'Mohammad(config)# banner motd #\n'
                   "Enter TEXT message. End with the character '#'.\n"
                   'This network is for SALES department.\n'
                   '#\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Setting Passwords on Cisco Routers:\n'
                   '\n'
                   'Five passwords are used to secure a Cisco router:\n'
                   '1. **Enable Password**: Secures access to Privileged EXEC mode (`Router#`). Stored in plaintext by '
                   'default.\n'
                   '```text\n'
                   'Router(config)# enable password todd\n'
                   '```\n'
                   '2. **Enable Secret**: Secures access to Privileged EXEC mode with automatic strong **MD5 '
                   'encryption**. Overrides `enable password`.\n'
                   '```text\n'
                   'Router(config)# enable secret todd\n'
                   '```\n'
                   '3. **Auxiliary Password**: Secures the modem auxiliary port (`line aux 0`).\n'
                   '```text\n'
                   'Router(config)# line aux 0\n'
                   'Router(config-line)# login\n'
                   'Router(config-line)# password todd\n'
                   '```\n'
                   '4. **Console Password**: Secures direct console cable access (`line console 0`).\n'
                   '```text\n'
                   'Router(config)# line console 0\n'
                   'Router(config-line)# login\n'
                   'Router(config-line)# password todd1\n'
                   '```\n'
                   '5. **Telnet (VTY) Password**: Secures in-band virtual terminal access (`line vty 0 4`).\n'
                   '```text\n'
                   'Router(config)# line vty 0 4\n'
                   'Router(config-line)# login\n'
                   'Router(config-line)# password todd2\n'
                   '```\n'
                   '*Note: If no VTY password is set, the router will refuse Telnet connections with the error '
                   '"Password required, but none set". To allow Telnet without passwords, issue `no login` under `line '
                   'vty 0 4`.*\n'
                   '\n'
                   '#### Encrypting Passwords:\n'
                   'To prevent plaintext passwords from being read in `show running-config`, enable encryption:\n'
                   '```text\n'
                   'Router(config)# service password-encryption\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Router Interfaces & Configuration:\n'
                   '\n'
                   'A Cisco router features two primary communication interface types:\n'
                   '1. **Ethernet / FastEthernet**: Connects to the local LAN.\n'
                   '2. **Serial Interfaces**: Connects to wide area networks (WANs) or other routers.\n'
                   '\n'
                   '#### Bringing Up an Interface:\n'
                   'All interfaces on Cisco routers are in an **administratively down** state by default.\n'
                   '* To turn an interface on: `no shutdown` (or `no shut`).\n'
                   '* To turn an interface off: `shutdown`.\n'
                   '\n'
                   '```text\n'
                   'Router(config)# interface FastEthernet 0/0\n'
                   'Router(config-if)# ip address 172.16.10.2 255.255.255.0\n'
                   'Router(config-if)# no shutdown\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Serial Interface Commands & Clock Rate:\n'
                   '\n'
                   '* In production WANs, serial interfaces connect to external CSU/DSU devices that provide network '
                   'synchronization clocking.\n'
                   "* In a back-to-back lab environment, one router\\'s serial cable end is **DCE (Data Communication "
                   'Equipment)**, and the other is **DTE (Data Terminal Equipment)**.\n'
                   '* **The DCE interface must provide clocking** using the `clock rate` command:\n'
                   '```text\n'
                   'Router(config)# interface Serial 0/0\n'
                   'Router(config-if)# clock rate 64000\n'
                   'Router(config-if)# ip address 172.16.20.1 255.255.255.0\n'
                   'Router(config-if)# no shutdown\n'
                   '```\n'
                   '*If you enter `clock rate` on a DTE interface, the IOS will output: `%Error: This command applies '
                   'only to DCE interfaces`.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Verifying Interfaces with `show interfaces`:\n'
                   '\n'
                   'The `show interfaces` command outputs physical and data link status:\n'
                   '\n'
                   '```text\n'
                   'Router# show interfaces FastEthernet 0/0\n'
                   'FastEthernet0/0 is up, line protocol is up\n'
                   '  Hardware is AmdFE, address is 00b0.6483.2320\n'
                   '  Internet address is 192.168.1.33/27\n'
                   '  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec\n'
                   '```\n'
                   '\n'
                   '#### Diagnostic State Analysis:\n'
                   '\n'
                   '| Interface Status | Line Protocol Status | Meaning & Troubleshooting |\n'
                   '|:---|:---|:---|\n'
                   '| **up** | **up** | **Operational**: Layer 1 carrier detected and Layer 2 keepalives functioning. '
                   '|\n'
                   '| **up** | **down** | **Data Link Layer Problem**: Clock rate missing on DCE, keepalive mismatch, '
                   'or framing/encapsulation mismatch. |\n'
                   '| **down** | **down** | **Physical Layer Problem**: Cable disconnected, damaged pins, or remote '
                   'interface powered off. |\n'
                   '| **administratively down** | **down** | **Disabled by Software**: Interface was shut down using '
                   'the `shutdown` command. Enable with `no shutdown`. |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Basic router configuration establishes hostnames, MOTD legal banners, encrypted passwords, and '
                   'Layer 3 IP addressing on LAN and WAN interfaces.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '1. Configure hostname `Lab_A`, an MOTD banner, and `enable secret`.\n'
                   '2. Secure line console 0 and line vty 0 4 with passwords and enable `service '
                   'password-encryption`.\n'
                   '3. Configure FastEthernet 0/0 with IP `192.168.10.1/24` and Serial 0/0 with IP `192.168.20.1/24` '
                   'and clock rate 64000.\n'
                   '4. Verify with `show interfaces` that both interfaces display `up/up`.',
        'flashcards': [   {   'answer': 'enable secret is encrypted automatically using MD5 hashing in the '
                                        'configuration, whereas enable password is stored in cleartext unless '
                                        'encrypted by service password-encryption.',
                              'question': 'Why is enable secret preferred over enable password?'},
                          {   'answer': 'On the DCE (Data Communication Equipment) end of a back-to-back serial '
                                        'connection without an external CSU/DSU, to supply synchronization clocking to '
                                        'the DTE end.',
                              'question': 'When is the clock rate command required on a Cisco router serial '
                                          'interface?'},
                          {   'answer': 'Layer 1 (Physical) has carrier signal, but Layer 2 (Data Link) has failed due '
                                        'to clock rate absence, keepalive mismatch, or incompatible '
                                        'framing/encapsulation.',
                              'question': "What does 'Serial0/0 is up, line protocol is down' mean?"},
                          {   'answer': "The 'no shutdown' (or 'no shut') command entered within interface "
                                        'configuration mode.',
                              'question': "What command enables an interface that is 'administratively down'?"}],
        'order': 10,
        'quizzes': [   {   'correctAnswer': 'enable password is stored in cleartext by default, whereas enable secret '
                                            'is automatically encrypted using MD5 hashing',
                           'explanation': 'The manual notes that enable password is unencrypted in configuration files '
                                          'by default, while enable secret is automatically encrypted and takes '
                                          'precedence.',
                           'options': [   'enable password is stored in cleartext by default, whereas enable secret is '
                                          'automatically encrypted using MD5 hashing',
                                          'enable secret only applies to console connections',
                                          'enable password permits alphanumeric passwords, whereas enable secret '
                                          'requires numbers only',
                                          'enable secret is stored on an external TFTP server'],
                           'question': 'What is the critical security difference between enable password and enable '
                                       'secret on a Cisco router?'},
                       {   'correctAnswer': 'The DCE (Data Communication Equipment) interface',
                           'explanation': 'In a back-to-back connection without an external CSU/DSU, the DCE end of '
                                          'the cable must supply clocking using the clock rate command (e.g. clock '
                                          'rate 64000).',
                           'options': [   'The DTE (Data Terminal Equipment) interface',
                                          'The DCE (Data Communication Equipment) interface',
                                          'Both DTE and DCE interfaces',
                                          'Neither interface (clocking is automatically derived from the FastEthernet '
                                          'port)'],
                           'question': 'In a back-to-back router serial lab connection, which end of the serial cable '
                                       'must have the clock rate command configured?'},
                       {   'correctAnswer': 'A Data Link layer framing, clock rate, keepalive, or encapsulation '
                                            'mismatch',
                           'explanation': "'Line up, protocol down' indicates physical carrier detection is present "
                                          '(Layer 1 is up), but Layer 2 keepalives or clocking failed, representing a '
                                          'Data Link layer problem.',
                           'options': [   'A physical cable disconnection or damaged pin',
                                          'A Data Link layer framing, clock rate, keepalive, or encapsulation mismatch',
                                          'The interface has been shut down with the administrative shutdown command',
                                          'Normal operational status with zero packet drops'],
                           'question': "When inspecting 'show interfaces serial 0/0', what does the status 'Serial0/0 "
                                       "is up, line protocol is down' indicate?"},
                       {   'correctAnswer': 'service password-encryption',
                           'explanation': 'service password-encryption applies Cisco Type 7 encryption to all '
                                          'plaintext passwords in the active configuration.',
                           'options': [   'encrypt all passwords',
                                          'service password-encryption',
                                          'crypto key generate rsa',
                                          'security passwords enable'],
                           'question': 'Which global configuration command manually encrypts all plaintext passwords '
                                       '(including console, aux, and vty passwords) in the running-config?'},
                       {   'correctAnswer': 'no shutdown',
                           'explanation': "All interfaces are shut down by default on Cisco routers; issuing 'no "
                                          "shutdown' (or 'no shut') from interface configuration mode brings the "
                                          'interface up.',
                           'options': ['enable interface', 'no shutdown', 'interface start', 'restart port'],
                           'question': "How do you bring up an interface that is in the 'administratively down' "
                                       'state?'}],
        'title': 'Day 10 (Lab # 11): Cisco Routers- Basic Configurations'},
    {   'codeSnippet': '# Cisco IOS: IP Routing Configurations (Static, Default, RIP)\n'
                       '\n'
                       '# 1. Static Routes on Lab_A to reach networks 30, 40, and 50 via Lab_B:\n'
                       'Lab_A(config)# ip route 192.168.30.0 255.255.255.0 192.168.20.2\n'
                       'Lab_A(config)# ip route 192.168.40.0 255.255.255.0 192.168.20.2\n'
                       'Lab_A(config)# ip route 192.168.50.0 255.255.255.0 192.168.20.2\n'
                       '\n'
                       '# 2. Default Route on Stub Router Lab_C:\n'
                       'Lab_C(config)# ip route 0.0.0.0 0.0.0.0 192.168.40.1\n'
                       '\n'
                       '# 3. Dynamic RIP Routing on Lab_A:\n'
                       'Lab_A(config)# router rip\n'
                       'Lab_A(config-router)# network 192.168.10.0\n'
                       'Lab_A(config-router)# network 192.168.20.0\n'
                       '\n'
                       '# 4. View Routing Table:\n'
                       'Lab_A# show ip route',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 12: IP Routing (Day 11)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understanding IP routing concepts and routing table decisions.\n'
                   '* Understanding routed protocols vs. routing protocols.\n'
                   '* Configuring and verifying **Static Routing**.\n'
                   '* Configuring and verifying **Default Routing** on stub networks.\n'
                   '* Configuring and verifying dynamic routing using **Routing Information Protocol (RIP)**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### What is IP Routing?\n'
                   'IP routing is the process of forwarding packets from a host on one network across an internetwork '
                   'to another host on a remote network.\n'
                   '* **Routed Protocols**: Protocols that contain network layer addressing and can be routed across '
                   'an internetwork (e.g. IP, IPX).\n'
                   '* **Routing Protocols**: Protocols used by routers to dynamically communicate, share routing '
                   'tables, and select best paths (e.g. RIP, OSPF, EIGRP).\n'
                   '\n'
                   '![Simple Two-Router Routing Example](assets/images/university/ccn/lab11_two_router_topology.png)\n'
                   '*Figure 1: Simple two-router network example.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### How Routers Make Forwarding Decisions:\n'
                   '\n'
                   'Routers look up the destination IP address of an incoming packet in their **routing table** (`show '
                   'ip route`):\n'
                   '\n'
                   '```text\n'
                   'Lab_A# show ip route\n'
                   'Gateway of last resort is not set\n'
                   '\n'
                   'C    10.10.10.0/24 is directly connected, FastEthernet0/0\n'
                   'C    10.10.20.0/24 is directly connected, FastEthernet0/1\n'
                   'C    10.10.30.0/24 is directly connected, FastEthernet0/2\n'
                   'C    10.10.40.0/24 is directly connected, Serial0/0\n'
                   '```\n'
                   '\n'
                   '* The **`C`** indicates that the network is **directly connected**.\n'
                   '* If a packet arrives for `10.10.10.10`, the router packet-switches it out interface '
                   '`FastEthernet0/0`.\n'
                   '* By default, routers only know about directly connected networks. To reach remote networks, '
                   'routing must be configured.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### IP Routing in a Multi-Router Internetwork:\n'
                   '\n'
                   '![Three Router WAN Internetwork](assets/images/university/ccn/lab11_routing_topology.png)\n'
                   '*Figure 2: Three-router internetwork topology (Lab_A, Lab_B, Lab_C).*\n'
                   '\n'
                   '#### Network Addressing Scheme:\n'
                   '\n'
                   '| Router | Network Address | Interface | IP Address | Subnet Mask |\n'
                   '|:---:|:---:|:---:|:---:|:---:|\n'
                   '| **Lab_A** | `192.168.10.0` | `fa0/0` | `192.168.10.1` | `255.255.255.0` |\n'
                   '| **Lab_A** | `192.168.20.0` | `s0/0` | `192.168.20.1` | `255.255.255.0` |\n'
                   '| **Lab_B** | `192.168.20.0` | `s0/0` | `192.168.20.2` | `255.255.255.0` |\n'
                   '| **Lab_B** | `192.168.40.0` | `s0/1` | `192.168.40.1` | `255.255.255.0` |\n'
                   '| **Lab_B** | `192.168.30.0` | `fa0/0` | `192.168.30.1` | `255.255.255.0` |\n'
                   '| **Lab_C** | `192.168.40.0` | `s0/0` | `192.168.40.2` | `255.255.255.0` |\n'
                   '| **Lab_C** | `192.168.50.0` | `fa0/0` | `192.168.50.1` | `255.255.255.0` |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 1. Static Routing\n'
                   '\n'
                   "Static routing occurs when an administrator manually enters routes into each router\\'s routing "
                   'table.\n'
                   '\n'
                   '#### Syntax:\n'
                   '```text\n'
                   'ip route <destination-network> <subnet-mask> <next-hop-ip | exit-interface>\n'
                   '```\n'
                   '\n'
                   '#### Benefits of Static Routing:\n'
                   '* **No CPU overhead** on the router.\n'
                   '* **No bandwidth consumed** on WAN links for routing protocol updates.\n'
                   '* **Security**: Administrators selectively control access to specific networks.\n'
                   '\n'
                   '#### Disadvantages of Static Routing:\n'
                   '* High administrative overhead in large or growing networks.\n'
                   '* Does not dynamically adapt to link failures.\n'
                   '\n'
                   '#### Configuring Static Routes on Lab_A:\n'
                   'To reach remote networks `192.168.30.0`, `192.168.40.0`, and `192.168.50.0` via Lab_B '
                   '(`192.168.20.2`):\n'
                   '```text\n'
                   'Lab_A(config)# ip route 192.168.30.0 255.255.255.0 192.168.20.2\n'
                   'Lab_A(config)# ip route 192.168.40.0 255.255.255.0 192.168.20.2\n'
                   'Lab_A(config)# ip route 192.168.50.0 255.255.255.0 192.168.20.2\n'
                   '```\n'
                   '\n'
                   'The resulting routing table displays:\n'
                   '```text\n'
                   'Lab_A# show ip route\n'
                   'S    192.168.50.0 [1/0] via 192.168.20.2\n'
                   'S    192.168.40.0 [1/0] via 192.168.20.2\n'
                   'S    192.168.30.0 [1/0] via 192.168.20.2\n'
                   'C    192.168.20.0 is directly connected, Serial0/0\n'
                   'C    192.168.10.0 is directly connected, FastEthernet0/0\n'
                   '```\n'
                   '*(Code **`S`** stands for Static Route with default Administrative Distance 1).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 2. Default Routing\n'
                   '\n'
                   'Default routing sends packets with a remote destination network not listed in the routing table to '
                   'a designated next-hop router.\n'
                   '* Can only be used on **stub networks** (networks with only one exit path).\n'
                   '* In our topology, **Lab_A** and **Lab_C** are stub routers.\n'
                   '\n'
                   '#### Configuring a Default Route on Lab_C:\n'
                   'Instead of configuring multiple static routes, configure one default route using quad-zero '
                   'wildcards:\n'
                   '```text\n'
                   'Lab_C(config)# ip route 0.0.0.0 0.0.0.0 192.168.40.1\n'
                   '```\n'
                   '\n'
                   'Routing table output:\n'
                   '```text\n'
                   'Lab_C# show ip route\n'
                   'Gateway of last resort is 192.168.40.1 to network 0.0.0.0\n'
                   '\n'
                   'C    192.168.50.0 is directly connected, FastEthernet0/0\n'
                   'C    192.168.40.0 is directly connected, Serial0/0\n'
                   'S*   0.0.0.0/0 [1/0] via 192.168.40.1\n'
                   '```\n'
                   '*`S*` indicates a candidate default route.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 3. Dynamic Routing: Routing Information Protocol (RIP)\n'
                   '\n'
                   'Dynamic routing protocols automatically discover remote networks and maintain routing tables.\n'
                   '* **RIP (Routing Information Protocol)**: A true **distance-vector** routing protocol.\n'
                   '* **Metric**: Hop count (each router traversed is 1 hop).\n'
                   '* **Maximum Hop Count**: **15 hops** (16 is deemed unreachable).\n'
                   '* **Update Frequency**: Broadcasts its complete routing table every **30 seconds**.\n'
                   '* **Administrative Distance**: **120**.\n'
                   '\n'
                   '#### Configuring RIP on Lab_A:\n'
                   "1. Delete existing static routes (since static routes have AD 1 and override RIP\\'s AD 120):\n"
                   '```text\n'
                   'Lab_A(config)# no ip route 192.168.30.0 255.255.255.0 192.168.20.2\n'
                   'Lab_A(config)# no ip route 192.168.40.0 255.255.255.0 192.168.20.2\n'
                   'Lab_A(config)# no ip route 192.168.50.0 255.255.255.0 192.168.20.2\n'
                   '```\n'
                   '2. Enable RIP and advertise directly connected networks:\n'
                   '```text\n'
                   'Lab_A(config)# router rip\n'
                   'Lab_A(config-router)# network 192.168.10.0\n'
                   'Lab_A(config-router)# network 192.168.20.0\n'
                   '```\n'
                   '\n'
                   'Routing table after RIP convergence:\n'
                   '```text\n'
                   'Lab_A# show ip route\n'
                   'R    192.168.50.0 [120/2] via 192.168.20.2, 00:00:23, Serial0/0\n'
                   'R    192.168.40.0 [120/1] via 192.168.20.2, 00:00:23, Serial0/0\n'
                   'R    192.168.30.0 [120/1] via 192.168.20.2, 00:00:23, Serial0/0\n'
                   'C    192.168.20.0 is directly connected, Serial0/0\n'
                   'C    192.168.10.0 is directly connected, FastEthernet0/0\n'
                   '```\n'
                   '*(Code **`R`** stands for RIP route; `[120/2]` denotes Administrative Distance 120 and hop count '
                   '2).*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'Static routing gives administrators total bandwidth and path control, default routing simplifies '
                   'stub networks, and RIP dynamic routing automates route discovery across multi-router '
                   'internetworks.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Task:\n'
                   '\n'
                   '![Hands-on Internetwork Topology](assets/images/university/ccn/lab11_routing_task.png)\n'
                   '*Figure 4: Hands-on lab internetwork (Routers 2621, 2501A, 2501B, 2501C).*\n'
                   '\n'
                   'Configure the 4-router lab network using static routing first, and then reconfigure using RIP '
                   'dynamic routing:\n'
                   '* **Router 2621**: F0/0 = `172.16.10.1/24`\n'
                   '* **Router 2501A**: E0 = `172.16.10.2/24`, S0 = `172.16.20.1/24`\n'
                   '* **Router 2501B**: E0 = `172.16.30.1/24`, S0 = `172.16.20.2/24`, S1 = `172.16.40.1/24`\n'
                   '* **Router 2501C**: E0 = `172.16.50.1/24`, S0 = `172.16.40.2/24`',
        'flashcards': [   {   'answer': 'Advantages: No CPU processing overhead, zero bandwidth consumed on links, '
                                        'enhanced security. Disadvantages: Requires manual entry and maintenance, '
                                        'prone to administrative error, does not adapt to network outages.',
                              'question': 'What are the advantages and disadvantages of Static Routing?'},
                          {   'answer': "A route ('ip route 0.0.0.0 0.0.0.0 <next-hop>') that forwards all packets "
                                        'destined for unknown remote networks to a next-hop router, used primarily on '
                                        'stub networks with a single exit path.',
                              'question': 'What is a Default Route and when is it configured?'},
                          {   'answer': 'A distance-vector dynamic routing protocol that uses hop count as its metric '
                                        '(maximum 15 hops; 16 = unreachable), advertising complete routing tables '
                                        'every 30 seconds with an Administrative Distance of 120.',
                              'question': 'What is the Routing Information Protocol (RIP) and what is its metric?'},
                          {   'answer': "'C' = Directly Connected network; 'S' = Static route; 'R' = Route learned "
                                        'dynamically via RIP.',
                              'question': 'What do the codes C, S, and R represent in a Cisco routing table (show ip '
                                          'route)?'}],
        'order': 11,
        'quizzes': [   {   'correctAnswer': 'C',
                           'explanation': "In 'show ip route', the code C stands for directly connected networks.",
                           'options': ['S', 'C', 'R', 'D'],
                           'question': "In a Cisco router routing table ('show ip route'), which letter code indicates "
                                       'a directly connected network?'},
                       {   'correctAnswer': '1',
                           'explanation': 'Static routes have a default administrative distance of 1.',
                           'options': ['0', '1', '90', '120'],
                           'question': 'What is the default Administrative Distance (AD) for a manually configured '
                                       'static route on a Cisco router?'},
                       {   'correctAnswer': 'ip route 0.0.0.0 0.0.0.0 192.168.40.1',
                           'explanation': "A default route uses wildcard quad-zeros for both network and mask: 'ip "
                                          "route 0.0.0.0 0.0.0.0 <next-hop-ip>'.",
                           'options': [   'ip default-gateway 192.168.40.1',
                                          'ip route 0.0.0.0 0.0.0.0 192.168.40.1',
                                          'ip route 255.255.255.255 255.255.255.255 192.168.40.1',
                                          'router default 192.168.40.1'],
                           'question': 'Which command correctly configures a Default Route pointing to next-hop IP '
                                       'address 192.168.40.1?'},
                       {   'correctAnswer': 'Hop count; max 15 hops (16 is deemed unreachable)',
                           'explanation': 'RIP uses hop count as its sole metric, with a maximum allowable hop count '
                                          'of 15; a hop count of 16 indicates an unreachable destination.',
                           'options': [   'Bandwidth; max 100 hops',
                                          'Hop count; max 15 hops (16 is deemed unreachable)',
                                          'Delay; max 255 hops',
                                          'Cost; max 64 hops'],
                           'question': 'What is the metric used by the Routing Information Protocol (RIP), and what is '
                                       'its maximum allowable hop count?'},
                       {   'correctAnswer': 'Every 30 seconds',
                           'explanation': 'RIP is a distance-vector routing protocol that broadcasts its complete '
                                          'routing table every 30 seconds by default.',
                           'options': [   'Every 10 seconds',
                                          'Every 30 seconds',
                                          'Every 60 seconds',
                                          'Only triggered upon topology change'],
                           'question': 'How frequently does RIP broadcast its complete routing table out of all active '
                                       'participating interfaces?'}],
        'title': 'Day 11 (Lab # 12): IP Routing'},
    {   'codeSnippet': '# Cisco Catalyst 2950 & 1900 Switch: VLAN & Trunking Configuration\n'
                       '\n'
                       '# 1. Create VLANs on Cisco 2950:\n'
                       'Switch(config)# vlan 2\n'
                       'Switch(config-vlan)# name Sales\n'
                       'Switch(config-vlan)# vlan 3\n'
                       'Switch(config-vlan)# name Marketing\n'
                       'Switch(config-vlan)# vlan 4\n'
                       'Switch(config-vlan)# name Finance\n'
                       '\n'
                       '# 2. Assign Access Ports to VLANs on 2950:\n'
                       'Switch(config)# interface FastEthernet 0/2\n'
                       'Switch(config-if)# switchport access vlan 2\n'
                       'Switch(config)# interface FastEthernet 0/3\n'
                       'Switch(config-if)# switchport access vlan 3\n'
                       '\n'
                       '# 3. Configure Trunk Port on 2950:\n'
                       'Switch(config)# interface FastEthernet 0/12\n'
                       'Switch(config-if)# switchport mode trunk\n'
                       '\n'
                       '# 4. Inter-VLAN Routing (Router-on-a-Stick on Cisco 2600):\n'
                       'Router(config)# interface FastEthernet 0/0.2\n'
                       'Router(config-subif)# encapsulation dot1q 2\n'
                       'Router(config-subif)# ip address 192.168.2.1 255.255.255.0\n'
                       'Router(config)# interface FastEthernet 0/0.3\n'
                       'Router(config-subif)# encapsulation dot1q 3\n'
                       'Router(config-subif)# ip address 192.168.3.1 255.255.255.0',
        'content': '![Hamdard University FEST Crest](assets/images/university/ccn/datacom2_logo.png)\n'
                   '\n'
                   '# LAB # 13: VLAN (Virtual LAN) (Day 12)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the concept and architecture of Virtual Local Area Networks (VLANs).\n'
                   '* Implement a multi-VLAN switched network.\n'
                   '* Customize a switch configuration to meet specified network requirements.\n'
                   '* Configure trunk links using IEEE 802.1Q.\n'
                   '* Configure Inter-VLAN routing using **Router-on-a-Stick** with subinterfaces.\n'
                   '* Perform LAN and VLAN troubleshooting.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '#### Flat Networks vs. VLANs:\n'
                   'Traditional Layer 2 switched networks are designed as **flat networks**:\n'
                   '* Every broadcast packet transmitted is received by every device on the network segment.\n'
                   '* A flat network is a **single broadcast domain**, which can lead to broadcast storms and degraded '
                   'performance.\n'
                   '\n'
                   '![Flat Network Structure](assets/images/university/ccn/lab12_flat_network.png)\n'
                   '*Figure 1: Traditional flat network structure (single large broadcast domain).*\n'
                   '\n'
                   '#### What is a VLAN?\n'
                   'A **VLAN (Virtual Local Area Network)** is a logical grouping of network users and resources '
                   'connected to administratively defined ports on a switch:\n'
                   '* Creates **smaller broadcast domains** within a Layer 2 switched internetwork.\n'
                   '* Broadcast frames are switched *only* between ports logically assigned to the same VLAN.\n'
                   '\n'
                   '#### Benefits of VLANs:\n'
                   '1. **Broadcast Control**: Decreases the size while increasing the number of broadcast domains.\n'
                   '2. **Enhanced Security**: Users needing confidential data can be isolated into dedicated VLANs '
                   'where outside users cannot communicate without passing through a router.\n'
                   '3. **Flexibility and Scalability**: Moves, adds, and changes are handled by software port '
                   'reassignment without physical recabling. Independent of physical geography.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### VLAN Membership Types:\n'
                   '1. **Static VLANs**: Switch ports are manually assigned to a VLAN by an administrator. This is the '
                   'most common and secure configuration.\n'
                   '2. **Dynamic VLANs**: Switch ports are assigned automatically based on host MAC addresses, '
                   'protocols, or network applications using a **VLAN Management Policy Server (VMPS)**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Switched Link Types:\n'
                   '\n'
                   'There are two types of links in a switched VLAN environment:\n'
                   '1. **Access Links**:\n'
                   '   * Belongs to **only one VLAN** (the native/access VLAN of the port).\n'
                   '   * Attached end devices (PCs, printers) are completely unaware of VLAN tags.\n'
                   '2. **Trunk Links**:\n'
                   '   * Carries traffic for **multiple VLANs simultaneously** between switches or between a switch '
                   'and a router.\n'
                   '   * Frame tagging protocols:\n'
                   '     * **IEEE 802.1Q (dot1q)**: Standard open tagging protocol (inserts a 4-byte tag into the '
                   'Ethernet frame).\n'
                   '     * **Cisco ISL (Inter-Switch Link)**: Cisco proprietary encapsulation protocol.\n'
                   '\n'
                   '![VLAN Topology and Inter-VLAN Routing](assets/images/university/ccn/lab12_vlan_topology.png)\n'
                   '*Figure 2: Multi-VLAN topology with 802.1Q trunking and Inter-VLAN router.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Inter-VLAN Routing:\n'
                   '\n'
                   'Because each VLAN is a separate Layer 3 subnet, communication between VLANs requires a **Layer 3 '
                   'router** or Layer 3 switch:\n'
                   '* **Router-on-a-Stick**: A single physical FastEthernet connection between the switch and router '
                   'is configured as a trunk.\n'
                   "* The router\\'s physical interface is divided into logical **subinterfaces** (e.g. `fa0/0.1`, "
                   '`fa0/0.2`), each configured with 802.1Q encapsulation for its respective VLAN.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Steps:\n'
                   '\n'
                   '#### Step 1: Configuring VLANs on Cisco Catalyst 2950 Switch\n'
                   '\n'
                   '1. Create VLANs in global configuration mode:\n'
                   '```text\n'
                   'Switch# config t\n'
                   'Switch(config)# vlan 2\n'
                   'Switch(config-vlan)# name Sales\n'
                   'Switch(config-vlan)# vlan 3\n'
                   'Switch(config-vlan)# name Marketing\n'
                   'Switch(config-vlan)# vlan 4\n'
                   'Switch(config-vlan)# name Finance\n'
                   'Switch(config-vlan)# end\n'
                   '```\n'
                   '\n'
                   '*Note: VLAN 1 is the default native VLAN and administrative VLAN on all Cisco switches. It cannot '
                   'be deleted or renamed.*\n'
                   '\n'
                   '2. Verify created VLANs:\n'
                   '```text\n'
                   'Switch# show vlan brief\n'
                   '```\n'
                   '\n'
                   '3. Assign Switch Ports to VLANs:\n'
                   '```text\n'
                   'Switch(config)# interface FastEthernet 0/2\n'
                   'Switch(config-if)# switchport access vlan 2\n'
                   'Switch(config)# interface FastEthernet 0/3\n'
                   'Switch(config-if)# switchport access vlan 3\n'
                   'Switch(config)# interface FastEthernet 0/4\n'
                   'Switch(config-if)# switchport access vlan 4\n'
                   '```\n'
                   '\n'
                   '4. Configure Trunk Port on Switch:\n'
                   '```text\n'
                   'Switch(config)# interface FastEthernet 0/12\n'
                   'Switch(config-if)# switchport mode trunk\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 2: Configuring VLANs on Cisco 1900 Switch (Reference)\n'
                   '\n'
                   '1. Create VLANs:\n'
                   '```text\n'
                   '1900(config)# vlan 2 name sales\n'
                   '1900(config)# vlan 3 name marketing\n'
                   '1900(config)# vlan 4 name mis\n'
                   '```\n'
                   '2. Assign static port membership:\n'
                   '```text\n'
                   '1900(config-if)# vlan-membership static 2\n'
                   '```\n'
                   '3. Enable DISL trunking:\n'
                   '```text\n'
                   '1900(config-if)# trunk on\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '#### Step 3: Configuring Inter-VLAN Routing on Cisco 2600 Router (Router-on-a-Stick)\n'
                   '\n'
                   '1. Bring up physical interface without assigning an IP address:\n'
                   '```text\n'
                   'Router(config)# interface FastEthernet 0/0\n'
                   'Router(config-if)# no shutdown\n'
                   '```\n'
                   '\n'
                   '2. Create subinterfaces with 802.1Q encapsulation:\n'
                   '```text\n'
                   'Router(config)# interface FastEthernet 0/0.2\n'
                   'Router(config-subif)# encapsulation dot1q 2\n'
                   'Router(config-subif)# ip address 192.168.2.1 255.255.255.0\n'
                   '\n'
                   'Router(config)# interface FastEthernet 0/0.3\n'
                   'Router(config-subif)# encapsulation dot1q 3\n'
                   'Router(config-subif)# ip address 192.168.3.1 255.255.255.0\n'
                   '\n'
                   'Router(config)# interface FastEthernet 0/0.4\n'
                   'Router(config-subif)# encapsulation dot1q 4\n'
                   'Router(config-subif)# ip address 192.168.4.1 255.255.255.0\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Conclusion:-\n'
                   'VLANs segment broadcast traffic at Layer 2, enhancing security and bandwidth efficiency. '
                   'Inter-VLAN communication is seamlessly accomplished using 802.1Q trunking and router '
                   'subinterfaces.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks:\n'
                   '1. Configure VLANs 2, 3, and 4 on the lab switch and assign ports accordingly.\n'
                   '2. Verify with `show vlan brief` that each port is in its assigned VLAN.\n'
                   '3. Configure an 802.1Q trunk port and configure Router-on-a-Stick subinterfaces on the connected '
                   'router to enable full inter-VLAN pinging.',
        'flashcards': [   {   'answer': 'A Virtual LAN is a logical broadcast domain created on Layer 2 switches. '
                                        'Benefits: Broadcast containment, improved security, departmental '
                                        'organization, and flexibility independent of physical location.',
                              'question': 'What is a VLAN and what are its primary network benefits?'},
                          {   'answer': 'Static VLANs are configured manually by assigning switch ports to a VLAN; '
                                        'Dynamic VLANs assign ports automatically based on MAC addresses using a VLAN '
                                        'Management Policy Server (VMPS).',
                              'question': 'What is the difference between Static and Dynamic VLANs?'},
                          {   'answer': 'Access links carry untagged frames for a single VLAN to end-user devices; '
                                        'Trunk links carry multiplexed frames for multiple VLANs using 802.1Q tags '
                                        'between switches or to a router.',
                              'question': 'What are Access links versus Trunk links?'},
                          {   'answer': 'A router architecture where a single physical FastEthernet/Gigabit port is '
                                        'divided into virtual subinterfaces (e.g. fa0/0.1), each configured with '
                                        "'encapsulation dot1q <vlan#>' and an IP gateway address.",
                              'question': "What is 'Router-on-a-Stick' inter-VLAN routing?"}],
        'order': 12,
        'quizzes': [   {   'correctAnswer': 'Because it constitutes a single broadcast domain where all broadcast '
                                            'frames are received by every device',
                           'explanation': 'The manual explains that a network is called flat because it is one '
                                          'broadcast domain where all broadcast packets are seen by every device, not '
                                          'because of its physical layout.',
                           'options': [   'Because all switches must be mounted in the same physical equipment rack',
                                          'Because it constitutes a single broadcast domain where all broadcast frames '
                                          'are received by every device',
                                          'Because it uses unshielded flat telephone cabling',
                                          'Because it does not support TCP/IP routing'],
                           'question': "Why is a traditional Layer 2 switched network referred to as a 'flat "
                                       "network'?"},
                       {   'correctAnswer': 'An Access link belongs to only one VLAN, whereas a Trunk link can carry '
                                            'traffic for multiple VLANs simultaneously',
                           'explanation': 'An Access link is assigned to a single VLAN and connects end-user devices, '
                                          'whereas a Trunk link carries multiplexed traffic for multiple VLANs between '
                                          'switches or to a router.',
                           'options': [   'An Access link belongs to only one VLAN, whereas a Trunk link can carry '
                                          'traffic for multiple VLANs simultaneously',
                                          'Access links operate at 10 Gbps, while Trunk links operate at 10 Mbps',
                                          'Access links connect routers, while Trunk links connect end-user PCs',
                                          'Access links tag packets with 802.1Q headers, while Trunk links do not'],
                           'question': 'What is the difference between an Access Link and a Trunk Link in a switched '
                                       'VLAN environment?'},
                       {   'correctAnswer': 'IEEE 802.1Q (dot1q)',
                           'explanation': 'IEEE 802.1Q (dot1q) is the open industry standard for frame tagging on VLAN '
                                          'trunks, supported by all modern switches and routers.',
                           'options': ['Cisco ISL', 'IEEE 802.1Q (dot1q)', 'IEEE 802.3u', 'IEEE 802.11ac'],
                           'question': 'Which IEEE industry standard protocol is used for VLAN tagging and '
                                       'encapsulation on Ethernet trunk links?'},
                       {   'correctAnswer': 'By creating logical subinterfaces (e.g. fa0/0.1, fa0/0.2) on the router, '
                                            'each configured with 802.1Q encapsulation for a distinct VLAN',
                           'explanation': 'Router-on-a-stick divides a single physical FastEthernet port into virtual '
                                          'subinterfaces, assigning each subinterface an 802.1Q VLAN tag and default '
                                          'gateway IP address.',
                           'options': [   'By creating logical subinterfaces (e.g. fa0/0.1, fa0/0.2) on the router, '
                                          'each configured with 802.1Q encapsulation for a distinct VLAN',
                                          'By disabling Layer 3 IP routing on the router',
                                          'By converting the FastEthernet port into an analog serial interface',
                                          'By installing a wireless bridge between the switch and router'],
                           'question': "How does a router perform 'Router-on-a-Stick' inter-VLAN routing across a "
                                       'single FastEthernet physical link?'},
                       {   'correctAnswer': 'switchport access vlan 2',
                           'explanation': 'On Cisco 2950 (and modern Catalyst) switches, ports are assigned to a VLAN '
                                          "using 'switchport access vlan <vlan-id>' under interface configuration "
                                          'mode.',
                           'options': [   'vlan-membership static 2',
                                          'switchport access vlan 2',
                                          'set vlan 2 port 0/2',
                                          'vlan 2 assign f0/2'],
                           'question': 'On a Cisco Catalyst 2950 switch, which command assigns FastEthernet port 0/2 '
                                       'to VLAN 2?'}],
        'title': 'Day 12 (Lab # 13): VLAN (Virtual LAN)'}]

DAYS_DATA = DAYS_PART1 + DAYS_PART2


def seed_datacom2_curriculum(verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds Days 1 to 6 (Labs 2 to 7) of Instructor Manual data-com (2) into Neon PostgreSQL via Prisma.
    Non-destructive: Touches ONLY this specific course, preserving all other courses and user accounts.
    """
    db = None
    owns_connection = False

    try:
        # Connect to database with retry mechanism using fresh Prisma client instances
        for attempt in range(5):
            try:
                db = Prisma()
                db.connect()
                owns_connection = True
                break
            except Exception as e:
                if db:
                    try:
                        db.disconnect()
                    except Exception:
                        pass
                print(f"[!] Connection attempt {attempt + 1} failed: {e}. Retrying in 2 seconds...", flush=True)
                time.sleep(2)
        else:
            raise RuntimeError("Failed to connect to Neon PostgreSQL after 5 attempts.")

        if verbose:
            print("=" * 85)
            print("[*] Connected to Neon PostgreSQL Database via Prisma.")
            print(f"[*] Target Course: '{COURSE_DATA['title']}' (Category: {COURSE_DATA['category']})")
            print("=" * 85)

        # 1. Non-destructive lookup or creation of Course/Lesson record
        lesson = db.lesson.find_first(
            where={
                "title": COURSE_DATA["title"],
                "category": COURSE_DATA["category"]
            }
        )

        if not lesson:
            lesson = db.lesson.create(
                data={
                    "title": COURSE_DATA["title"],
                    "category": COURSE_DATA["category"],
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[+] Created Course record: ID={lesson.id} | Title='{lesson.title}'")
        else:
            lesson = db.lesson.update(
                where={"id": lesson.id},
                data={
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[*] Found existing Course record: ID={lesson.id} | Title='{lesson.title}'")

        # 2. Idempotent cleanup of old steps, quizzes, and flashcards for ONLY THIS COURSE
        del_q = db.quiz.delete_many(where={"lessonId": lesson.id})
        del_f = db.flashcard.delete_many(where={"lessonId": lesson.id})
        del_s = db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"[*] Cleared previous records for datacom2 course: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

        # 3. Insert Labs LessonSteps, Quizzes, and Flashcards
        summary_rows = []
        total_quizzes = 0
        total_flashcards = 0

        def safe_op(op_func, max_retries=5, delay=0.8):
            for attempt in range(max_retries):
                try:
                    return op_func()
                except Exception as ex:
                    if attempt == max_retries - 1:
                        raise ex
                    time.sleep(delay)

        for day in DAYS_DATA:
            step = safe_op(lambda day=day: db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": day["order"],
                    "title": day["title"],
                    "content": day["content"],
                    "codeSnippet": day.get("codeSnippet", "")
                }
            ))
            time.sleep(0.05)

            # Insert Quizzes linked to both lessonId and lessonStepId
            for q in day["quizzes"]:
                safe_op(lambda q=q, step_id=step.id: db.quiz.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step_id,
                        "question": q["question"],
                        "options": q["options"],
                        "correctAnswer": q["correctAnswer"],
                        "explanation": q.get("explanation", "")
                    }
                ))
                total_quizzes += 1
                time.sleep(0.05)

            # Insert Flashcards linked to both lessonId and lessonStepId
            for fc in day["flashcards"]:
                safe_op(lambda fc=fc, step_id=step.id: db.flashcard.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step_id,
                        "question": fc["question"],
                        "answer": fc["answer"]
                    }
                ))
                total_flashcards += 1
                time.sleep(0.05)

            summary_rows.append({
                "day_num": f"Day {day['order']}",
                "title": day["title"][:50],
                "quizzes_count": len(day["quizzes"]),
                "flashcards_count": len(day["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 85)
            print("SUMMARY TABLE: UNIVERSITY DATA-COM (2) COMPLETE 12-LAB CURRICULUM SEEDED")
            print("=" * 85)
            print(f"{'Day #':<8} | {'Title':<52} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 85)
            for row in summary_rows:
                print(f"{row['day_num']:<8} | {row['title']:<52} | {row['quizzes_count']:<8} | {row['flashcards_count']:<10}")
            print("=" * 85)
            print(f"Total LessonSteps: {len(DAYS_DATA)}")
            print(f"Total Quizzes:     {total_quizzes}")
            print(f"Total Flashcards:  {total_flashcards}")
            print(f"Category:          {COURSE_DATA['category']}")
            print("=" * 85)

        return {
            "lessonId": lesson.id,
            "title": lesson.title,
            "category": lesson.category,
            "stepsCount": len(DAYS_DATA),
            "quizzesCount": total_quizzes,
            "flashcardsCount": total_flashcards
        }

    finally:
        if owns_connection and db.is_connected():
            db.disconnect()

if __name__ == "__main__":
    seed_datacom2_curriculum()