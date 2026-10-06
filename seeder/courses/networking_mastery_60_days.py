"""
Complete Computer Networking Basics 60-Day Curriculum Blueprint
Assembles all 60 days of topic-per-day lessons, deep ELI5 analogies,
progressive CLI/code snippets, daily networking labs/challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.networking_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.networking_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.networking_curriculum_days_31_45 import DAYS_31_TO_45
from seeder.courses.networking_curriculum_days_46_60 import DAYS_46_TO_60

# Consolidate all 60 days in strict sequential order
ALL_60_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_45 + DAYS_46_TO_60

NETWORKING_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Computer Networking Basics",
    category="TECH",
    description=(
        "The comprehensive 60-Day Computer Networking Roadmap. "
        "Enforced universal topic-per-day architecture: Networking Fundamentals (LAN/WAN/MAN/PAN/CAN, Topologies, Transmission Media, Devices), "
        "Network Architectures (OSI 7 Layers, TCP/IP 4 Layers, Encapsulation/PDU), "
        "IP Addressing & Subnetting (MAC, IPv4 Classes, RFC 1918, FLSM, VLSM/CIDR, IPv6 & SLAAC), "
        "Layer 2 Switching (CAM Tables, VLANs, 802.1Q, DTP, VTP, STP/RSTP/MSTP, EtherChannel LACP, PoE, Campus Switching Lab), "
        "Layer 3 Routing (Static, Inter-VLAN ROAS, RIP, EIGRP, OSPF Single/Multi-Area, BGP iBGP/eBGP), "
        "Core Services & Protocols (TCP/UDP, Ports, DHCP DORA, DNS, NAT/PAT, ARP, ICMP, Core Services Lab), "
        "Wireless & WAN (Wi-Fi 4/5/6/7, Frequencies, Autonomous vs WLC, WEP/WPA2/WPA3, Leased Lines, MPLS, PPPoE, SD-WAN), "
        "Network Security (Stateful/Stateless/NGFW Firewalls, Standard & Extended ACLs, IPsec & SSL VPNs, AAA RADIUS/TACACS+, Port Security, DHCP Snooping, DAI, IDS/IPS), "
        "Optimization & High Availability (QoS LLQ/CBWFQ, FHRP HSRP/VRRP/GLBP, SNMPv3, Syslog, NetFlow), and "
        "Modern Networking & Automation (SDN OpenFlow, Cisco DNA Center / Catalyst Center, AWS VPCs / Azure VNets, REST APIs, JSON/YAML, Netmiko, NAPALM, Ansible Capstone). "
        "Features 60 hands-on networking labs/challenges and 300 knowledge verification quizzes."
    ),
    color="#2563EB",
    days=ALL_60_DAYS
)
