"""
ITC University Curriculum Seeder (CS-111 Introduction to Computing & ITC Lab)
100% Verbatim text transcription from 'Lab Manual ITC Update 2021 (1).docx' for Hamdard Institute of Engineering & Technology.
Populates all 14 University Laboratory Modules (Labs 1 to 14) with zero data loss, exact paragraphs, complete shortcut tables, Japanese car data, formulas, inline assets, quizzes, and flashcards.
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from prisma import Prisma

COURSE_DATA = {
    "title": "Introduction to Computing & ITC Lab (CS-111)",
    "category": "University",
    "description": "Official Academic Curriculum for CS-111 Introduction to Computing & ITC Lab. Comprehensive university laboratory manual covering Computer Architecture, Windows OS internals, TCP/IP Networking, Microsoft Office Productivity Suite (Word, Excel, Access), and Programming Foundations.",
    "color": "#4F46E5",
    "thumbnail": "assets/images/university/itc/lab0_hamdard_logo.png"
}

LABS_DATA = [
    {
        "order": 1,
        "title": "Lab 1: Computer Hardware, CPU, Motherboard & Peripheral Architecture",
        "codeSnippet": "# Diagnostic command to view hardware architecture in Windows\nsysteminfo | findstr /B /C:\"OS Name\" /C:\"System Type\" /C:\"Processor\"",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 1\n\nComputer Hardware\n\n\n## Objective\n\n\nTo learn about different parts of computer hardware\n\n\n## Theory\n\n\nComponents of a Computer:\n\nComputer consists of two main components:\n\nHardware\n\nSoftware\n\nSoftware:\n\nComputer software, or just software, is a collection of computer programs and related data that provides the instructions for telling a computer what to do and how to do it. In other words, software is a set of programs, procedures, algorithms and its documentation concerned with the operation of a data processing system. Program software performs the function of the program it implements, either by directly providing instructions to the computer hardware or by serving as input to another piece of software. The term was coined to contrast to the old term hardware (meaning physical devices). In contrast to hardware, software \"cannot be touched\".\n\nOperating System:\n\nAn operating system (OS) is a collection of software that manages computer hardware resources and provides common services for computer programs. The operating system is a vital component of the system software in a computer system. Application programs require an operating system to function.\n\n\n### Examples:\n\n\nMicrosoft Windows\n\nLinux\n\n\n![Diagram](assets/images/university/itc/lab1_os_windows_linux.png)\n\n\nMacintosh\n\n\n![Diagram](assets/images/university/itc/lab1_os_macintosh.png)\n\n\nHardware:\n\nComputer hardware is the collection of physical elements that comprise a computer system. Computer hardware refers to the physical parts or components of computer such as monitor, keyboard, hard disk, mouse, etc., refers to objects that you can actually touch, like disks, disk drives, display screens, keyboards, printers, boards, and chips. In contrast, software is untouchable. Software exists as ideas, application, concepts, and symbols, but it has no substance. A combination of hardware and software forms a usable computing system. This allows it for computer run better than normally faster.\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_hardware.png)\n\n\nProcessor:\n\n\n![Diagram](assets/images/university/itc/lab1_cpu.png)\n\n\nA central processing unit (CPU), also referred to as a central processor unit, is the hardware within a computer system which carries out the instructions of a computer program by performing the basic arithmetical, logical, and input/output operations of the system. The form, design, and implementation of CPUs have changed over the course of their history, but their fundamental operation remains much the same.\n\nTwo typical components of a CPU are the arithmetic logic unit (ALU), which performs arithmetic and logical operations, and the control unit (CU), which extracts instructions from memory and decodes and executes them, calling on the ALU when necessary.\n\nMotherboard:\n\n\n![Diagram](assets/images/university/itc/lab1_motherboard.png)\n\n\nThe motherboard serves to connect all of the parts of a computer together. The CPU, memory, hard drives, optical drives, video card, sound card and other ports and expansion cards all connect to the motherboard directly or via cables.\n\nThe motherboard can be thought of as the \"back bone\" of the computer.\n\nMotherboards, cases and power supplies all come in different sizes called form factors. All three must be compatible to work properly together.\n\nMotherboards vary greatly in respect to the types of components they support. For example, each motherboard supports a single type of CPU and a short list of memory types.\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_hdd.png)\n\n\nHard Disk Drives:\n\nA hard disk drive (HDDalso hard drive, hard disk, or disk drive) is a device for storing and retrieving digital information. It consists of one or more rigid (\"hard\") rapidly rotating discs (platters) coated with magnetic material, with magnetic heads arranged to read and write data to the surfaces.\n\nRAM [Random Access Memory]:\n\n\n![Diagram](assets/images/university/itc/lab1_ram.png)\n\n\nRAM (random access memory) is the place in a computer where the operating system, application programs, and data in current use are kept so that they can be quickly reached by the computer's processor. RAM is much faster to read from and write to than the other kinds of storage in a computer, the hard disk, floppy disk, and CD-ROM. However, the data in RAM stays there only as long as your computer is running. When you turn the computer off, RAM loses its data. When you turn your computer on again, your operating system and other files are once again loaded into RAM, usually from your hard disk.\n\nInput Devices:\n\nThe devices that use to enter data and instructions in a computer.\n\nFor Example:\n\n\n\n| Keyboard | 40640102235 |\n\n| --- | --- |\n\nKeyboard\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_keyboard.png)\n\n\n\n\n| Mouse / Touchpad | 88902755901510665346075 |\n\n| --- | --- |\n\nMouse / Touchpad\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_mouse.png)\n\n\n\n![Diagram](assets/images/university/itc/lab1_touchpad.png)\n\n\n\n\n| Scanner | 779780157480 |\n\n| --- | --- |\n\nScanner\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_scanner.png)\n\n\n\n\n| Microphone | 1017270179070 |\n\n| --- | --- |\n\nMicrophone\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_microphone.png)\n\n\nOutput Devices:\n\nThe devices that allow information to be represented (that is, given out) to the user.\n\nFor Example:\n\n\n\n| Monitor / LCD | 2072640274955-10795199390 |\n\n| --- | --- |\n\nMonitor / LCD\n\n-10795199390\n\n\n![Diagram](assets/images/university/itc/lab1_monitor_crt.png)\n\n\n\n![Diagram](assets/images/university/itc/lab1_monitor_lcd.png)\n\n\n\n\n| Printer | 96456585090 |\n\n| --- | --- |\n\nPrinter\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_printer.png)\n\n\n\n\n| Speakers | centercenter |\n\n| --- | --- |\n\nSpeakers\n\ncentercenter\n\n\n![Diagram](assets/images/university/itc/lab1_speakers.png)\n\n\nPorts:\n\nPorts are the socket at the back of the computer that allows different peripheral devices to connect to the computer\n\nPS/2 Port [Keyboard]USB PortsSerial Port[Dial-up Modem]VGA Port [Monitor]SpeakersLine InMicrophonePS/2 Port [Mouse]Ethernet Port [Network]LPT1 Printer Port [Printer]Game Port [Joystick]\n\n\n![Diagram](assets/images/university/itc/lab1_ports.png)\n\n\nPS/2 Port [Keyboard]\n\nUSB Ports\n\nSerial Port\n\n[Dial-up Modem]\n\nVGA Port [Monitor]\n\nSpeakers\n\nLine In\n\nMicrophone\n\nPS/2 Port [Mouse]\n\nEthernet Port [Network]\n\nLPT1 Printer Port [Printer]\n\nGame Port [Joystick]\n\n\n## Tasks:\n\n\n\n### Q.)Label the diagram of the motherboard\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab1_motherboard_components.png)\n\n\n\n### Q.)Where is OS stored and installed on a computer?\n",
        "quizzes": [
            {
                        "question": "Which two internal units comprise the core functional architecture of a Central Processing Unit (CPU)?",
                        "options": [
                                    "Arithmetic Logic Unit (ALU) and Control Unit (CU)",
                                    "Hard Disk Drive (HDD) and Random Access Memory (RAM)",
                                    "Basic Input Output System (BIOS) and Northbridge",
                                    "Expansion Bus and Direct Memory Access (DMA)"
                        ],
                        "correctAnswer": "Arithmetic Logic Unit (ALU) and Control Unit (CU)",
                        "explanation": "The ALU handles mathematical operations and logical evaluations, while the Control Unit fetches, decodes, and manages the execution of instructions."
            },
            {
                        "question": "What is the primary physical characteristic that distinguishes RAM from secondary storage such as an HDD?",
                        "options": [
                                    "RAM is volatile and loses its data immediately when electrical power is removed.",
                                    "RAM retains all operating system files even when the system is unplugged.",
                                    "RAM utilizes rapidly rotating magnetic platters with mechanical actuator arms.",
                                    "RAM is much slower to read and write than optical discs and magnetic tapes."
                        ],
                        "correctAnswer": "RAM is volatile and loses its data immediately when electrical power is removed.",
                        "explanation": "RAM is high-speed semiconductor volatile memory; power disruption clears its entire contents, requiring the OS to reload from the non-volatile HDD/SSD on boot."
            },
            {
                        "question": "What term designates the physical dimensions, mounting hole locations, and casing compatibility of motherboards, power supplies, and cases?",
                        "options": [
                                    "Form Factor",
                                    "Clock Multiplier",
                                    "Bandwidth Protocol",
                                    "Thermal Design Power (TDP)"
                        ],
                        "correctAnswer": "Form Factor",
                        "explanation": "Form factor (such as ATX, Micro-ATX, Mini-ITX) specifies the physical geometry and compatibility standards across motherboards, cases, and power supplies."
            },
            {
                        "question": "Which peripheral port utilizes a 15-pin 3-row D-sub miniature connector to transmit analog video signals to a monitor?",
                        "options": [
                                    "VGA Port",
                                    "Serial RS-232 Port",
                                    "LPT1 Parallel Port",
                                    "PS/2 Mini-DIN Port"
                        ],
                        "correctAnswer": "VGA Port",
                        "explanation": "The Video Graphics Array (VGA) port is a 15-pin analog connector historically standardized for computer displays and monitors."
            },
            {
                        "question": "Where does the Operating System reside before the computer is turned on, and where is it loaded during the boot sequence?",
                        "options": [
                                    "Stored in non-volatile secondary storage (HDD/SSD); loaded into volatile RAM upon boot",
                                    "Stored exclusively in the CPU cache; loaded into the BIOS ROM upon boot",
                                    "Stored in the CMOS battery; loaded into the VGA card upon boot",
                                    "Stored in external network routers; loaded into the power supply upon boot"
                        ],
                        "correctAnswer": "Stored in non-volatile secondary storage (HDD/SSD); loaded into volatile RAM upon boot",
                        "explanation": "Secondary storage retains the installed OS files permanently without electricity. Upon boot, the bootloader copies the operating system kernel into RAM for rapid execution."
            }
],
        "flashcards": [
            {
                        "question": "What does the Arithmetic Logic Unit (ALU) perform within the CPU?",
                        "answer": "Arithmetic calculations (+, -, *, /) and logical comparison decisions (AND, OR, NOT, comparisons)."
            },
            {
                        "question": "What is the function of the Control Unit (CU)?",
                        "answer": "It extracts instructions from memory, decodes them, and directs the flow of data across the CPU and peripherals."
            },
            {
                        "question": "Why is the motherboard termed the 'backbone' of the computer?",
                        "answer": "Because it physically and electrically interconnects all system components: CPU, RAM, storage drives, GPU, and ports."
            },
            {
                        "question": "What happens to data residing in RAM when you turn off the computer?",
                        "answer": "All data in RAM is completely lost because RAM is volatile semiconductor memory."
            },
            {
                        "question": "What peripheral port was historically designated for dot-matrix and laser printers?",
                        "answer": "The 25-pin LPT1 Parallel Printer Port."
            }
]
    },
    {
        "order": 2,
        "title": "Lab 2: Windows Operating System Environment, Device Manager & Permissions",
        "codeSnippet": "# Inspect device hardware and security permissions in Windows command line\ndevmgmt.msc\nicacls \"C:\\Users\\Public\" /t",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 2\n\nWindows Operating System and its Components\n\n\n## Objective\n\n\nTo become familiar with the Windows OS environment\n\n\n## Introduction:\n\n\nWindows is the most common operating system used for PCs. It is essential that you familiarize yourself with the basic functionality of this OS.\n\nIt is necessary that you are aware of the hardware in your computer. While the operating system usually takes care of the complexity of managing the hardware of your computer system, knowing the hardware helps when you have to:\n\nInstall an operating system\n\nUpgrade your computer system\n\nDiagnose and repair problems in your computer system\n\n\n## Preparation:\n\n\nStart computer and try to explore its functionalities.\n\n\n### PROBLEM #1:\n\n\nFamiliarize yourself with the following basic tasks specific to Windows operating systems:\n\nCopying/ pasting a file. (Using Shift and Ctrl Keys also)\n\nCreating a new file\n\nCreating a new folder\n\nDeleting a file\n\nFinding how to find Windows help\n\n\n## Equipment:\n\n\nPersonal Computer with Windows Operating System\n\n\n## Procedure:\n\n\nCopying/ pasting a file [select a file, right click> copy; go to the directory to paste into, right click > paste]\n\nCreating a new file [hint: right click > new > file type]\n\nCreating a new folder [hint: right click > new > folder]\n\nDeleting a file [hint: select a file, right click > delete]\n\nFinding how to find Windows help [hint: click on Windows Start button, and then on Help and Support, explore what kind of help is available]\n\n\n### PROBLEM #2:\n\n\nTo check the hardware present in your computer\n\n\n## Equipment:\n\n\n1.Personal Computer with Windows Operating System\n\n\n## Procedure:\n\n\nTo check the hardware present in your computer, Right click on My Computer and then click on Properties , note down the specifications of the PC you are working on in the General tab (shown by default).\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_system_general.png)\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_computer_name.png)\n\n\nClick on the Computer Name tab.\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_devicemanager.png)\n\n\nClick on the Hardware tab and then on Device Manager, note all information about hardware devices here?\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_system_properties.png)\n\n\n(Hint: you can right-click on any device and see further properties)\n\n\n### PROBLEM #3:\n\n\nTo check the Sharing and Security feature of Folders\n\n\n## Equipment:\n\n\n1.Personal Computer with Windows Operating System\n\n\n## Procedure:\n\n\nTo check the Sharing and Security, Right click on My Computer and then click on Properties , Select Sharing or Security tab.\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_system_general.png)\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab2_permissions.png)\n\n\n\n## Tasks:\n\n\nWhere to find Operating System being used? (write complete details)\n\nWhere to find installed Service Pack?\n\nWhere to find System\u2019s name?\n\nWhere to find clock speed of the computer\u201fs CPU?\n\nWhere to find amount of RAM present?\n\nWhere to find size the disk drive?\n\nDoes the computer have a Bluetooth radio?\n\nDoes the computer have a network adapter?\n\nWhat is the name of the monitor? Is the proper driver of the monitor installed? What is the name of the provider of the driver for the monitor?\n\nList down different permissions applied to folders",
        "quizzes": [
            {
                        "question": "What is the crucial difference between the 'Full Control' and 'Modify' NTFS permissions?",
                        "options": [
                                    "Full Control allows a user to change permissions and take ownership; Modify does not.",
                                    "Modify allows deleting files; Full Control does not.",
                                    "Full Control only applies to text files; Modify applies to executable programs.",
                                    "Modify grants administrative access across the entire network domain."
                        ],
                        "correctAnswer": "Full Control allows a user to change permissions and take ownership; Modify does not.",
                        "explanation": "Both Full Control and Modify permit editing and deleting, but only Full Control grants the administrative rights to alter ACL permissions and seize ownership."
            },
            {
                        "question": "In Windows Device Manager, what does a yellow exclamation mark icon next to a hardware device signify?",
                        "options": [
                                    "The device has a hardware conflict, missing driver, or operational error.",
                                    "The device is operating at maximum gigabit speed.",
                                    "The device has been successfully encrypted with BitLocker.",
                                    "The hardware device is permanently powered off."
                        ],
                        "correctAnswer": "The device has a hardware conflict, missing driver, or operational error.",
                        "explanation": "A yellow exclamation mark indicates that Windows detects the physical device but cannot communicate with it properly due to a missing or incompatible driver."
            },
            {
                        "question": "Which keyboard shortcut permanently deletes a selected file immediately without sending it to the Windows Recycle Bin?",
                        "options": [
                                    "Shift + Delete",
                                    "Ctrl + Delete",
                                    "Alt + Delete",
                                    "Ctrl + Shift + D"
                        ],
                        "correctAnswer": "Shift + Delete",
                        "explanation": "Holding Shift while pressing Delete bypasses the Recycle Bin staging area and requests immediate permanent file deletion."
            },
            {
                        "question": "Where in the Windows operating system can you verify whether a PC is part of a peer-to-peer Workgroup or an Active Directory Domain?",
                        "options": [
                                    "In System Properties under the Computer Name tab",
                                    "In Disk Management under Volume Properties",
                                    "In the Recycle Bin properties dialog",
                                    "In the Screen Resolution settings"
                        ],
                        "correctAnswer": "In System Properties under the Computer Name tab",
                        "explanation": "The Computer Name tab in System Properties explicitly declares the full computer name and whether the machine belongs to a Workgroup or Domain."
            },
            {
                        "question": "Which NTFS permission allows a user to see the names of files inside a directory without granting access to open or read the files themselves?",
                        "options": [
                                    "List Folder Contents",
                                    "Read & Execute",
                                    "Modify",
                                    "Write Only"
                        ],
                        "correctAnswer": "List Folder Contents",
                        "explanation": "'List Folder Contents' enables viewing directory inventory and file listings without granting permission to view file contents."
            }
],
        "flashcards": [
            {
                        "question": "What utility can you run from Windows Run prompt to open Device Manager directly?",
                        "answer": "devmgmt.msc"
            },
            {
                        "question": "What are the 6 standard NTFS folder permissions in Windows?",
                        "answer": "Full Control, Modify, Read & Execute, List Folder Contents, Read, and Write."
            },
            {
                        "question": "What information does the General tab of System Properties show?",
                        "answer": "Windows OS edition, Service Pack, CPU model and clock frequency, and total installed RAM."
            },
            {
                        "question": "What does a red 'X' indicate on a device in Device Manager?",
                        "answer": "It indicates that the device is currently disabled."
            },
            {
                        "question": "What is the function of the NetBIOS computer name?",
                        "answer": "It serves as the unique human-readable identifier for a computer on a Local Area Network."
            }
]
    },
    {
        "order": 3,
        "title": "Lab 3: Networking Fundamentals, TCP/IP Configuration & Diagnostic Commands",
        "codeSnippet": "# Essential TCP/IP diagnostic suite\nipconfig /all\nping 127.0.0.1\ntracert espn.com\narp -a\nnetstat -s\nnslookup www.google.com",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 3\n\nIntroduction to Networking and Routing\n\n\n## Objective\n\n\nTo become familiar with basics of computer networking\n\nTo become familiar with basic TCP/IP configuration\n\n\n## Theory\n\n\nThe Internet is a network of computers that links many different types of computers all over the world. Computers are uniquely identified by the IP addresses.\n\nTo check the TCP/IP configuration, right click on the LAN icon on your taskbar . Next, click on Open Network and sharing Center .\n\n\n![Diagram](assets/images/university/itc/lab3_networking.png)\n\n\n\n![Diagram](assets/images/university/itc/lab3_lan_icon.png)\n\n\nNext, click on the Local Area Connection 2.\n\nNext click on Details.\n\n-38103175\n\n\n![Diagram](assets/images/university/itc/lab3_taskbar_network.png)\n\n\n-888365187960-3840480294640\n\n\n![Diagram](assets/images/university/itc/lab3_tcp_ip_config.png)\n\n\n\n![Diagram](assets/images/university/itc/lab3_ip_details.png)\n\n\nIP Address :An Internet Protocol\u00a0address\u00a0(IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. ... Internet Protocol version 4 (IPv4) defines an\u00a0IP address\u00a0as a 32-bit number. Ex 192.168.0.2\n\nA\u00a0subnet mask\u00a0is a number that defines a range of IP addresses available within a\u00a0network.\u00a0A single\u00a0subnet mask\u00a0limits the number of valid IPs for a specific\u00a0network.\u00a0Multiple\u00a0subnet masks\u00a0can organize a single\u00a0network\u00a0into smaller networks (called subnetworks or\u00a0subnets). Ex 255.255.255.0\n\nA\u00a0default gateway\u00a0is the node in a computer network using the internet protocol suite that serves as the forwarding host (router) to other networks when no other route specification matches the destination IP address of a packet. Ex 192.168.0.1\n\nDNS\u00a0is the name service for Internet\u00a0addresses\u00a0that translates friendly domain names to numeric Internet Protocol (IP)\u00a0addresses. For example, \"www.microsoft.com\" translates to 198.105.232.6. ... In a domain name system, the client requests network\u00a0addressing\u00a0information from the name\u00a0servers.\n\nA media access control\u00a0address\u00a0(MAC address) of a device is a unique identifier assigned to a network interface controller (NIC). For communications within a network segment, it is used as a network\u00a0address\u00a0for most IEEE 802 network technologies, including Ethernet, Wi-Fi, and Bluetooth.\n\n\n\n\n![Diagram](assets/images/university/itc/lab3_mac_address.png)\n\n\n\n## Basic IP Commands:\n\n\n1. Ping\n\nThe PING utility tests connectivity between two hosts. PING uses a special protocol called the\u00a0Internet Control Message Protocol (ICMP)\u00a0to determine whether the remote machine (website, server, etc.) can receive the test packet and reply.\n\nAlso a great way to verify whether you have TCP/IP installed and your Network Card is working.\n\nWe'll start by Pinging the loopback address (127.0.0.1) to verify that TCP/IP is installed and configured correctly on the local computer.\n\nType:\u00a0PING 127.0.0.1\n\nThis tells me that TCP/IP is working as well as my Network Card.\n\nTo test out connectivity to a website all you have to do is type:\u00a0ping espn.com\n\nThe results should tell you if the connection was successful or if you had any lost packets.\n\nPacket loss describes a condition in which data packets appear to be transmitted correctly at one end of a connection, but never arrive at the other. Why? Well, there are a few possibilities.\n\nThe network connection might be poor and packets get damaged in transit or the packet was dropped at a router because of internet congestion. Some Internet Web servers may be configured to disregard ping requests for security purposes.\n\nNote the IP address of espn.com -- 199.181.132.250. You can also ping this address and get the same result.\n\nHowever, Ping is not just used to test websites. It can also test connectivity to various servers: DNS, DHCP, your Print server, etc. As you get more into networking you'll realize just how handy the Ping utility can be.\n\n2. Tracert\n\nTracert is very similar to Ping, except that Tracert identifies pathways taken along each hop, rather than the time it takes for each packet to return (ping).\n\nIf I have trouble connecting to a remote host I will use Tracert to see where that connection fails. Any information sent from a source computer must travel through many computers / servers / routers (they're all the same thing, essentially) before it reaches a destination.\n\nIt may not be your computer but something that is down along the way. It can also tell you if communication is slow because a link has gone down between you and the destination.\n\nIf you know there are normally 4 routers but Tracert returns 8 responses, you know your packets are taking an indirect route due to a link being down.\n\n3. ARP\n\nThe ARP utility helps diagnose problems associated with the\u00a0Address Resolution Protocol (ARP).\n\nTCP/IP hosts use ARP to determine the physical (MAC) address that corresponds with a specific IP address. Type\u00a0arp\u00a0with the\u00a0\u2013 a\u00a0option to display IP addresses that have been resolved to MAC addresses recently.\n\n4. Netstat\n\nNetstat (Network Statistics) displays network connections (both incoming and outgoing), routing tables, and a number of network interface statistics.\n\nIt is an important part of the\u00a0Network + exam\u00a0but it's a helpful tool in finding problems and determining the amount of traffic on the network as a performance measurement.\n\nNetstat \u2013s\u00a0provides statistics about incoming and outgoing traffic.\n\n5. Nbtstat\n\nNbtstat (NetBios over TCP/IP) enables you to check information about NetBios names.\n\nIt helps us view the NetBios name cache (nbtstat -c) which shows the NetBios names and the corresponding IP address that has been resolved (nbtstat -r) by a particular host as well as the names that have been registered by the local system (nbtstat \u2013n).\n\n6. NSLookup\n\nNSLookup provides a command-line utility for diagnosing DNS problems. In its most basic usage, NSLookup returns the IP address with the matching host name.\n\n7. IPConfig\n\nNot part of the TCP/IP utilities but it is useful to show current TCP/IP settings.\n\nThe IPConfig command line utility will show detailed information about the network you are connected to. It also helps with reconfiguration of your IP address through release and renew.\n\nLet's say you want to know what you're IP address is --\u00a0ipconfig\u00a0is what you type in the command prompt.\n\nipconfig\u00a0will give a quick view of you IP address, your subnet mask and default gateway.\n\nipconfig /all\u00a0will give you more detailed information.\n\nThrough\u00a0ipconfig /all\u00a0we can find DNS severs, if we have DHCP enabled, MAC Address, along with other helpful information. All good things to know if we have trouble getting connected to the internet.\n\nOther IPConfig tools that are helpful include\u00a0ipconfig /release\u00a0and\u00a0ipconfig /renew. But before I get into this let's discuss how we actually get an IP Address.\n\nThere are two ways to obtain an IP address. One way is to have a static IP address which we manually assign. The second one is to have a dynamic IP address obtained through a DHCP server.\n\nIf you were to right click on Network Connects, go to Properties, right click on Local Area Connection, scroll down to Internet Protocol (TCP/IP), and select Properties -- you'll see two options:\n\nObtain an IP address automatically\n\nUse the following IP address\n\nUnless you know your static IP address you'll want to stick to the option for automatically obtaining the IP address. If you have it set to automatic your computer will be issued an IP through a DHCP server.\n\nAnd just in case you're wondering,\u00a0Dynamic Host Configuration Protocol (DHCP)\u00a0is a network protocol that enables a server to automatically assign an IP address to a computer from a defined range of numbers (i.e., a scope) configured for a given network.\n\nIn laymen's terms: I have a cable modem at home and I have that modem connected to a wireless router that issues out IP address to anyone that connects to that router. That is DHCP that is issuing out IP addresses.\n\nYour company probably has a server dedicated to this. Understanding this is definitely important for any networking exam.\n\nLet's look at what happens when we release our IP address.\n\nI've just lost internet connection and my IP address is 0.0.0.0. If I type ipconfig /renew this option re-establishes TCP/IP connections on all network adapters and I can resume my internet surfing.\n\nNote:\u00a0ipconfig /release renew won't work if you manually assigned your IP addresses.\n\nTask:\n\nWhat is the IP address of the machine you are working?\n\nWhat is the subnet mask?\n\nNote down the IP address of the default gateway. Is the default gateway on the same LAN as the machine? Explain why or why not?\n\nWhat is the physical address or MAC address of the machine?\n\nCan you configure the MAC address of the machine?\n\nWhat is the name of the DNS server?\n\nWhat is name of default DNS server for your machine? What is the IP address of the default DNS server?\n\nResolve the address www.google.com; do you get the same IPs as above?\n\nWhat is the IP address of the first hop router?\n\nCan you trace the route of the packet and determine until which hop the packets are in Pakistan, when do they exit Pakistan?\n\nUsing the link http://www.net.berkeley.edu/cgi-bin/traceroute  (which will run and output the traceroute command in University of California, Berkeley), trace the route to the web server at Hamdard www.hamdard.edu.pk/.\n\nDated: ____________",
        "quizzes": [
            {
                        "question": "What diagnostic network protocol is utilized by the PING utility to test end-to-end host reachability?",
                        "options": [
                                    "Internet Control Message Protocol (ICMP)",
                                    "Hypertext Transfer Protocol (HTTP)",
                                    "Simple Mail Transfer Protocol (SMTP)",
                                    "Network Time Protocol (NTP)"
                        ],
                        "correctAnswer": "Internet Control Message Protocol (ICMP)",
                        "explanation": "PING transmits ICMP Echo Request datagrams and awaits ICMP Echo Reply packets to verify connectivity and latency."
            },
            {
                        "question": "Which command-line command displays the physical MAC address corresponding to recently resolved local IP addresses?",
                        "options": [
                                    "arp -a",
                                    "netstat -s",
                                    "tracert -d",
                                    "nslookup -all"
                        ],
                        "correctAnswer": "arp -a",
                        "explanation": "'arp -a' outputs the Address Resolution Protocol table mapping IP network addresses to physical MAC hardware addresses."
            },
            {
                        "question": "What is the primary function of a Default Gateway in a Local Area Network?",
                        "options": [
                                    "It acts as the forwarding router to route packets destined for external networks outside the local subnet.",
                                    "It acts as a physical uninterruptible power supply for the workstation.",
                                    "It translates alphanumeric passwords into binary numbers.",
                                    "It encrypts local hard disk files automatically."
                        ],
                        "correctAnswer": "It acts as the forwarding router to route packets destined for external networks outside the local subnet.",
                        "explanation": "When an IP destination does not match the local subnet mask range, packets are forwarded to the Default Gateway router for internet routing."
            },
            {
                        "question": "What occurs when the command 'ipconfig /release' is executed on a workstation with dynamic IP addressing?",
                        "options": [
                                    "The workstation releases its leased IP address back to the DHCP server and its IP becomes 0.0.0.0.",
                                    "The workstation formats its hard drive.",
                                    "The workstation permanently locks its MAC address.",
                                    "The workstation converts its network cable to fiber optic."
                        ],
                        "correctAnswer": "The workstation releases its leased IP address back to the DHCP server and its IP becomes 0.0.0.0.",
                        "explanation": "'ipconfig /release' discards the active DHCP lease, dropping the local adapter's IP to 0.0.0.0 until 'ipconfig /renew' is invoked."
            },
            {
                        "question": "Which diagnostic utility identifies intermediate router hops along the packet transmission path by evaluating TTL expired responses?",
                        "options": [
                                    "tracert",
                                    "nbtstat",
                                    "nslookup",
                                    "getmac"
                        ],
                        "correctAnswer": "tracert",
                        "explanation": "'tracert' (Trace Route) sends packets with incrementing TTL values to identify every intermediate router between source and destination."
            }
],
        "flashcards": [
            {
                        "question": "What is the loopback IP address used to test the local TCP/IP stack?",
                        "answer": "127.0.0.1"
            },
            {
                        "question": "How many bits are in an IPv4 address and a MAC address respectively?",
                        "answer": "An IPv4 address contains 32 bits; a MAC physical address contains 48 bits."
            },
            {
                        "question": "What does DNS stand for and what is its primary function?",
                        "answer": "Domain Name System; it translates human-readable domain names into numeric IP addresses."
            },
            {
                        "question": "What protocol dynamically assigns IP addresses to devices connecting to a network?",
                        "answer": "Dynamic Host Configuration Protocol (DHCP)."
            },
            {
                        "question": "Which command command displays complete network adapter details including DNS and MAC addresses?",
                        "answer": "ipconfig /all"
            }
]
    },
    {
        "order": 4,
        "title": "Lab 4: Microsoft Word Document Processing, Page Setup & Complete Shortcut Table",
        "codeSnippet": "# Microsoft Word Mail Merge & Document formatting standards\n# Verbatim Shortcut Range: Ctrl+0 to Shift+Alt+T",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 4\n\nIntroduction to Microsoft Word\n\n\n## Objective\n\n\nLearn to create a word document using different features of MS Word\n\n\n## Theory\n\n\nMicrosoft Word:\n\nMicrosoft Word is a powerful tool to create professional documents.\n\nTo begin, open Microsoft Word. Your screen will look like the one shown here.\n\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_ribbon.png)\n\n\n\n## Document Views:\n\n\nIn Word, you can display your document in one of five views: Normal, Web Layout, Print Layout, Reading Layout, or Online Layout. To change the view of a document, use the view tab.\n\nPrint Layout\n\nThe Print Layout view shows the document as it will look when it is printed.\n\nWeb Layout\n\nWeb layout view enables you to view your document as it would appear in a browser such as Internet Explorer.\n\nFull Screen Reading Layout\n\nReading Layout view formats your screen to make reading your document more comfortable.\n\nOutline view\n\nThe outline view displays the document in outline form. Headings can be displayed without the text. If you move a heading, the accompanying text moves with it.\n\n\n## Paragraph Group:\n\n\nWhen you type information in Microsoft Word, each time you press the Enter key Word creates a new paragraph. You can format paragraphs. For example, you can indent the first line of a paragraph, you can set the amount of space that separates paragraphs, and you can align a paragraph left, right, center, or flush with both margins. Styles are a set of formats you can quickly apply to a paragraph. For example, by applying a style, you can set the font, set the font size, and align a paragraph all at once. In this lesson, you will learn about the various formats you can apply to a paragraph and about styles.\n\n\n![Diagram](assets/images/university/itc/lab4_word_margins.png)\n\n\nWhen you are formatting a paragraph, you do not need to select the entire paragraph. Placing the cursor anywhere in the paragraph enables you to format it. After you format a paragraph, pressing the Enter key creates a new paragraph in the same format.\n\n\n## Indent Paragraphs:\n\n\nIndentation allows you to indent your paragraph from the left and/or right margin. You may find this necessary when you are quoting a large block of text. Try using the first line indent and hanging indent.\n\n\n![Diagram](assets/images/university/itc/lab4_word_orientation.png)\n\n\n\n## Align Paragraphs\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_portrait_landscape.png)\n\n\nMicrosoft Word gives you a choice of several types of alignments. Left-aligned text is flush with the left margin of your document and is the default setting. Right-aligned text is flush with the right margin of your document, centered text is centered between the left and right margins, and justified text is flush with both the left and right margins.\n\n\n## Change Line Spacing\n\n\nLine spacing sets the amount of space between lines within a paragraph. The spacing for each line is set to accommodate the largest font on that line. If the lines include smaller fonts, there will appear to be extra space between lines where the smaller fonts are located. At 1.5, the line spacing is set to one-and-a-half times the single-space amount. At 2.0, the line spacing is set to two times the single-space amount (double space).\n\n\n![Diagram](assets/images/university/itc/lab4_word_page_size.png)\n\n\n\n## Bullets and Numbers:\n\n\nIf you have lists of data, you may want to bullet or number them. When using Microsoft Word, bulleting and numbering are easy.\n\n\n![Diagram](assets/images/university/itc/lab4_word_paragraph_group.png)\n\n\nIn Microsoft Word, you can easily create bulleted or numbered lists of items. Several bulleting and numbering styles are available, as shown in the examples. You can select the one you wish to use.\n\nBulleting:\n\nType the list as shown\n\nSelect the words you just typed.\n\nChoose the Home tab.\n\nIn the Paragraph group, click the down arrow next to the Bullets button. The Bullet Library appears.\n\nClick to select the type of bullet you want to use. Word adds bullets to your list.\n\nNote: As you move your cursor over the various bullet styles, Word displays the bullet style onscreen.\n\n\n![Diagram](assets/images/university/itc/lab4_word_alignment.png)\n\n\nNumbers7620000\n\n\n![Diagram](assets/images/university/itc/lab4_word_indent.png)\n\n\nNumbers\n\nBullets\n\n\n## Set the Orientation:\n\n\nBefore you print your document, you may want to change the orientation of your pages. There are two orientations you can use: portrait and landscape. Paper, such as paper sized 8.5 x 11in, is longer on one edge than it is on the other. If you print in Portrait, the shortest edge of the paper becomes the top of the page. Portrait is the default option. If you print Landscape, the longest edge of the paper becomes the top of the page.\n\n\n![Diagram](assets/images/university/itc/lab4_word_line_spacing.png)\n\n\nChoose the Page Layout tab.\n\nClick Orientation in the Page Setup group. A menu appears.\n\nClick Portrait. Word sets your page orientation to Portrait.\n\nPage Size:\n\n\n![Diagram](assets/images/university/itc/lab4_word_bullet_library.png)\n\n\nPaper comes in a variety of sizes. Most business correspondence uses 8.5 x 11in paper which is the default page size in Word. If you are not using 8.5 x 11in paper, you can use the Size option in the Page Setup group of the Page Layout tab to change the Size setting.\n\nChoose the Page Layout tab.\n\nClick Size in the Page Setup group. A menu appears.\n\nClick Letter 8.5 x 11in. Word sets your page size.\n\n\n## Set the Margins:\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_bullets_numbers.png)\n\n\nMargins define the amount of white space that appears at the top, bottom, left, and right edges of your document. The Margin option in the Page Setup group of the Page Layout tab provides several standard margin sizes from which you can choose.\n\nChoose the Page Layout tab.\n\nClick Margins in the Page Setup group. A menu appears.\n\nClick Moderate. Word sets your margins to the Moderate settings.\n\n\n## Inserting Picture:\n\n\n3305175-211455Copy the picture from any source and paste in MS word. Pictures can be placed in different forms in MS- Word. MS- Word also allows pictures to be inserted from clip art.\n\n\n![Diagram](assets/images/university/itc/lab4_word_numbering_library.png)\n\n\nSearch the picture in clip art here\n\nPicture layout options\n\n\n![Diagram](assets/images/university/itc/lab4_word_insert_picture.png)\n\n\n\n## Saving a Word file:\n\n\nIn the File menu, select Save As. A pop \u2013 up window appears, select the destination to save the file and press Save button.\n\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_picture_layout.png)\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_save_dialog.png)\n\n\n\n## Printing a Word file:\n\n\nIn the File menu, select Print option, a pop-up window appears. Set the page setting, select the printer and press Print button.\n\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_save_as.png)\n\n\n\n![Diagram](assets/images/university/itc/lab4_word_print_dialog.png)\n\n\nPrint PreviewDifferent shortcut keys used in a Word file:\n\nPrint Preview\n\n\n\n| Shortcut | Description |\n\n| --- | --- |\n\nShortcut\n\nDescription\n\n\n\n| Ctrl+0 | Toggles 6pts of spacing above the\u00a0paragraph. |\n\n| --- | --- |\n\nCtrl+0\n\nToggles 6pts of spacing above the\u00a0paragraph.\n\n\n\n| Ctrl+A | Select all contents of the page. |\n\n| --- | --- |\n\nCtrl+A\n\nSelect all contents of the page.\n\n\n\n| Ctrl+B | Bold\u00a0highlighted selection. |\n\n| --- | --- |\n\nCtrl+B\n\nBold\u00a0highlighted selection.\n\n\n\n| Ctrl+C | Copy\u00a0selected text. |\n\n| --- | --- |\n\nCtrl+C\n\nCopy\u00a0selected text.\n\n\n\n| Ctrl+D | Open the\u00a0font\u00a0preferences window. |\n\n| --- | --- |\n\nCtrl+D\n\nOpen the\u00a0font\u00a0preferences window.\n\n\n\n| Ctrl+E | Aligns the line or selected text to the center of the screen. |\n\n| --- | --- |\n\nCtrl+E\n\nAligns the line or selected text to the center of the screen.\n\n\n\n| Ctrl+F | Open find box. |\n\n| --- | --- |\n\nCtrl+F\n\nOpen find box.\n\n\n\n| Ctrl+I | Italic\u00a0highlighted selection. |\n\n| --- | --- |\n\nCtrl+I\n\nItalic\u00a0highlighted selection.\n\n\n\n| Ctrl+J | Aligns\u00a0the selected text or line to justify the screen. |\n\n| --- | --- |\n\nCtrl+J\n\nAligns\u00a0the selected text or line to justify the screen.\n\n\n\n| Ctrl+K | Insert a\u00a0hyperlink. |\n\n| --- | --- |\n\nCtrl+K\n\nInsert a\u00a0hyperlink.\n\n\n\n| Ctrl+L | Aligns the line or selected text to the left of the screen. |\n\n| --- | --- |\n\nCtrl+L\n\nAligns the line or selected text to the left of the screen.\n\n\n\n| Ctrl+M | Indent the paragraph. |\n\n| --- | --- |\n\nCtrl+M\n\nIndent the paragraph.\n\n\n\n| Ctrl+N | Opens new, blank document window. |\n\n| --- | --- |\n\nCtrl+N\n\nOpens new, blank document window.\n\n\n\n| Ctrl+O | Opens the dialog box or page for selecting a file to open. |\n\n| --- | --- |\n\nCtrl+O\n\nOpens the dialog box or page for selecting a file to open.\n\n\n\n| Ctrl+P | Open the print window. |\n\n| --- | --- |\n\nCtrl+P\n\nOpen the print window.\n\n\n\n| Ctrl+R | Aligns the line or selected text to the right of the screen. |\n\n| --- | --- |\n\nCtrl+R\n\nAligns the line or selected text to the right of the screen.\n\n\n\n| Ctrl+S | Save the open document. Like Shift+F12. |\n\n| --- | --- |\n\nCtrl+S\n\nSave the open document. Like Shift+F12.\n\n\n\n| Alt+F, A | Save the document under a different file name. |\n\n| --- | --- |\n\nAlt+F, A\n\nSave the document under a different file name.\n\n\n\n| Alt+X | Show the\u00a0Unicode\u00a0code of a highlighted character. |\n\n| --- | --- |\n\nAlt+X\n\nShow the\u00a0Unicode\u00a0code of a highlighted character.\n\n\n\n| Ctrl+T | Create a\u00a0hanging indent. |\n\n| --- | --- |\n\nCtrl+T\n\nCreate a\u00a0hanging indent.\n\n\n\n| Ctrl+U | Underline the selected text. |\n\n| --- | --- |\n\nCtrl+U\n\nUnderline the selected text.\n\n\n\n| Ctrl+V | Paste. |\n\n| --- | --- |\n\nCtrl+V\n\nPaste.\n\n\n\n| Ctrl+W | Close the currently open document. |\n\n| --- | --- |\n\nCtrl+W\n\nClose the currently open document.\n\n\n\n| Ctrl+X | Cut\u00a0selected text. |\n\n| --- | --- |\n\nCtrl+X\n\nCut\u00a0selected text.\n\n\n\n| Ctrl+Y | Redo the last action performed. |\n\n| --- | --- |\n\nCtrl+Y\n\nRedo the last action performed.\n\n\n\n| Ctrl+Z | Undo last action. |\n\n| --- | --- |\n\nCtrl+Z\n\nUndo last action.\n\n\n\n| Ctrl+Shift+L | Quickly create a\u00a0bullet point. |\n\n| --- | --- |\n\nCtrl+Shift+L\n\nQuickly create a\u00a0bullet point.\n\n\n\n| Ctrl+Shift+F | Change the font. |\n\n| --- | --- |\n\nCtrl+Shift+F\n\nChange the font.\n\n\n\n| Ctrl+Shift+> | Increase selected font +1pts up to 12pt and then increase font +2pts. |\n\n| --- | --- |\n\nCtrl+Shift+>\n\nIncrease selected font +1pts up to 12pt and then increase font +2pts.\n\n\n\n| Ctrl+] | Increase selected font +1pts. |\n\n| --- | --- |\n\nCtrl+]\n\nIncrease selected font +1pts.\n\n\n\n| Ctrl+Shift+< | Decrease selected font -1pts if 12pt or lower; if above 12, decreases font by +2pt. |\n\n| --- | --- |\n\nCtrl+Shift+<\n\nDecrease selected font -1pts if 12pt or lower; if above 12, decreases font by +2pt.\n\n\n\n| Ctrl+[ | Decrease selected font -1pts. |\n\n| --- | --- |\n\nCtrl+[\n\nDecrease selected font -1pts.\n\n\n\n| Ctrl+/+c | Insert a cent sign (\u00a2). |\n\n| --- | --- |\n\nCtrl+/+c\n\nInsert a cent sign (\u00a2).\n\n\n\n| Ctrl+'+<char> | Insert a character with an accent (acute) mark, where <char> is the character you want. For example, if you wanted an accented \u00e9 you would use\u00a0Ctrl+'+e\u00a0as your shortcut key. To reverse the accent mark, use the opposite accent mark, often found on the\u00a0tilde key. |\n\n| --- | --- |\n\nCtrl+'+<char>\n\nInsert a character with an accent (acute) mark, where <char> is the character you want. For example, if you wanted an accented \u00e9 you would use\u00a0Ctrl+'+e\u00a0as your shortcut key. To reverse the accent mark, use the opposite accent mark, often found on the\u00a0tilde key.\n\n\n\n| Ctrl+Shift+* | View or hide non printing characters. |\n\n| --- | --- |\n\nCtrl+Shift+*\n\nView or hide non printing characters.\n\n\n\n| Ctrl+<left arrow> | Moves one word to the left. |\n\n| --- | --- |\n\nCtrl+<left arrow>\n\nMoves one word to the left.\n\n\n\n| Ctrl+<right arrow> | Moves one word to the right. |\n\n| --- | --- |\n\nCtrl+<right arrow>\n\nMoves one word to the right.\n\n\n\n| Ctrl+<up arrow> | Moves to the beginning of the line or paragraph. |\n\n| --- | --- |\n\nCtrl+<up arrow>\n\nMoves to the beginning of the line or paragraph.\n\n\n\n| Ctrl+<down arrow> | Moves to the end of the paragraph. |\n\n| --- | --- |\n\nCtrl+<down arrow>\n\nMoves to the end of the paragraph.\n\n\n\n| Ctrl+Del | Deletes word to right of cursor. |\n\n| --- | --- |\n\nCtrl+Del\n\nDeletes word to right of cursor.\n\n\n\n| Ctrl+Backspace | Deletes word to left of cursor. |\n\n| --- | --- |\n\nCtrl+Backspace\n\nDeletes word to left of cursor.\n\n\n\n| Ctrl+End | Moves the cursor to the end of the document. |\n\n| --- | --- |\n\nCtrl+End\n\nMoves the cursor to the end of the document.\n\n\n\n| Ctrl+Home | Moves the cursor to the beginning of the document. |\n\n| --- | --- |\n\nCtrl+Home\n\nMoves the cursor to the beginning of the document.\n\n\n\n| Ctrl+Spacebar | Reset highlighted text to the default font. |\n\n| --- | --- |\n\nCtrl+Spacebar\n\nReset highlighted text to the default font.\n\n\n\n| Ctrl+1 | Single-space lines. |\n\n| --- | --- |\n\nCtrl+1\n\nSingle-space lines.\n\n\n\n| Ctrl+2 | Double-space lines. |\n\n| --- | --- |\n\nCtrl+2\n\nDouble-space lines.\n\n\n\n| Ctrl+5 | 1.5-line spacing. |\n\n| --- | --- |\n\nCtrl+5\n\n1.5-line spacing.\n\n\n\n| Ctrl+Alt+1 | Changes text to heading 1. |\n\n| --- | --- |\n\nCtrl+Alt+1\n\nChanges text to heading 1.\n\n\n\n| Ctrl+Alt+2 | Changes text to heading 2. |\n\n| --- | --- |\n\nCtrl+Alt+2\n\nChanges text to heading 2.\n\n\n\n| Ctrl+Alt+3 | Changes text to heading 3. |\n\n| --- | --- |\n\nCtrl+Alt+3\n\nChanges text to heading 3.\n\n\n\n| Alt+Ctrl+F2 | Open new document. |\n\n| --- | --- |\n\nAlt+Ctrl+F2\n\nOpen new document.\n\n\n\n| Ctrl+F1 | Open the\u00a0Task Pane. |\n\n| --- | --- |\n\nCtrl+F1\n\nOpen the\u00a0Task Pane.\n\n\n\n| Ctrl+F2 | Display the\u00a0print preview. |\n\n| --- | --- |\n\nCtrl+F2\n\nDisplay the\u00a0print preview.\n\n\n\n| Ctrl+Shift+> | Increases the selected text size by one font size. |\n\n| --- | --- |\n\nCtrl+Shift+>\n\nIncreases the selected text size by one font size.\n\n\n\n| Ctrl+Shift+< | Decreases the selected text size by one font size. |\n\n| --- | --- |\n\nCtrl+Shift+<\n\nDecreases the selected text size by one font size.\n\n\n\n| Ctrl+Shift+F6 | Switches to another open Microsoft Word document. |\n\n| --- | --- |\n\nCtrl+Shift+F6\n\nSwitches to another open Microsoft Word document.\n\n\n\n| Ctrl+Shift+F12 | Prints the document. |\n\n| --- | --- |\n\nCtrl+Shift+F12\n\nPrints the document.\n\n\n\n| F1 | Open help. |\n\n| --- | --- |\n\nF1\n\nOpen help.\n\n\n\n| F4 | Repeat the last action performed (Word 2000+). |\n\n| --- | --- |\n\nF4\n\nRepeat the last action performed (Word 2000+).\n\n\n\n| F5 | Open the\u00a0Find,\u00a0Replace, and\u00a0Go To\u00a0window in Microsoft Word. |\n\n| --- | --- |\n\nF5\n\nOpen the\u00a0Find,\u00a0Replace, and\u00a0Go To\u00a0window in Microsoft Word.\n\n\n\n| F7 | Spellcheck and grammar check selected text or document. |\n\n| --- | --- |\n\nF7\n\nSpellcheck and grammar check selected text or document.\n\n\n\n| F12 | Save As. |\n\n| --- | --- |\n\nF12\n\nSave As.\n\n\n\n| Shift+F3 | Change the text in Microsoft Word from\u00a0uppercase\u00a0to\u00a0lowercase\u00a0or a capital letter at the beginning of every word. |\n\n| --- | --- |\n\nShift+F3\n\nChange the text in Microsoft Word from\u00a0uppercase\u00a0to\u00a0lowercase\u00a0or a capital letter at the beginning of every word.\n\n\n\n| Shift+F7 | Runs a Thesaurus check on the selected word. |\n\n| --- | --- |\n\nShift+F7\n\nRuns a Thesaurus check on the selected word.\n\n\n\n| Shift+F12 | Save the open document. Like Ctrl+S. |\n\n| --- | --- |\n\nShift+F12\n\nSave the open document. Like Ctrl+S.\n\n\n\n| Shift+Enter | Create a\u00a0soft break\u00a0instead of a new paragraph. |\n\n| --- | --- |\n\nShift+Enter\n\nCreate a\u00a0soft break\u00a0instead of a new paragraph.\n\n\n\n| Shift+Insert | Paste. |\n\n| --- | --- |\n\nShift+Insert\n\nPaste.\n\n\n\n| Shift+Alt+D | Insert the current date. |\n\n| --- | --- |\n\nShift+Alt+D\n\nInsert the current date.\n\n\n\n| Shift+Alt+T | Insert the current time. |\n\n| --- | --- |\n\nShift+Alt+T\n\nInsert the current time.\n\n\n## Lab Task\n\n\nWrite a  newspaper article on any topic comprising of 3-4 paragraphs. Use the following MS Word features:\n\nBold, Italic, Underline, Highlight, Small Caps.\n\nDifferent Line Spacing\n\nBulletin or Numbering\n\nParagraph Alignment\n\nTwo-columns on a page\n\nInsert a picture relevant to your topic on the right side of your paragraph\n\nPlace your name and student id at the top right in font size 10 as Header\n\nAttach a print out of this article with your manual.\n\nCreate a Mail Merge Document to send Cricket MatchInvitation to your Friends. Write steps and attach a sample page(s).\n\nUse table of Contents option create a table of Contents of a document. Write down its steps.\n\nConvert Text to table and Table to Text of following text:\n\nAttendance Date 19 09 2 26 09 2 03 10 2 67 34 100 100 100 100 67 2 2 P P A A P A P P P P P P P P P P P P A P P Att % Anas Saeed Hafiz Osama Bin Haleem Muhammad Usama Shahzaib Zahidi Usama Ali Wajahatullah Khan Shinwari Zain Ali Sno Std ID Student Name 1 2 3 4 5 6 7 6 1 2 1 A 2 1 3 3 3 3 2",
        "quizzes": [
            {
                        "question": "Which Microsoft Word shortcut key creates a hanging indent where the second and subsequent lines of a paragraph are indented?",
                        "options": [
                                    "Ctrl + T",
                                    "Ctrl + M",
                                    "Ctrl + Shift + H",
                                    "Alt + H"
                        ],
                        "correctAnswer": "Ctrl + T",
                        "explanation": "Ctrl + T creates a hanging indent in Word, commonly utilized in APA and MLA bibliography citations."
            },
            {
                        "question": "What keyboard shortcut toggles text case between uppercase, lowercase, and title case capitalization?",
                        "options": [
                                    "Shift + F3",
                                    "Ctrl + Shift + C",
                                    "Alt + F4",
                                    "Ctrl + F12"
                        ],
                        "correctAnswer": "Shift + F3",
                        "explanation": "Shift + F3 cycles highlighted text through UPPERCASE, lowercase, and Title Case capitalization."
            },
            {
                        "question": "Which shortcut key combination immediately inserts the dynamic current time into a Microsoft Word document?",
                        "options": [
                                    "Shift + Alt + T",
                                    "Ctrl + Shift + ;",
                                    "Alt + T",
                                    "Ctrl + Alt + T"
                        ],
                        "correctAnswer": "Shift + Alt + T",
                        "explanation": "Shift + Alt + T inserts the current time field; Shift + Alt + D inserts the current date field."
            },
            {
                        "question": "What is the function of the shortcut key combination 'Ctrl + 5' in Microsoft Word?",
                        "options": [
                                    "Sets 1.5-line spacing on the active paragraph",
                                    "Increases font size by 5 points",
                                    "Applies heading style 5",
                                    "Inserts 5 blank pages"
                        ],
                        "correctAnswer": "Sets 1.5-line spacing on the active paragraph",
                        "explanation": "In Word: Ctrl+1 sets single space, Ctrl+2 sets double space, and Ctrl+5 sets 1.5-line spacing."
            },
            {
                        "question": "How does pressing 'Shift + Enter' differ from pressing the standard 'Enter' key in Microsoft Word?",
                        "options": [
                                    "Shift + Enter creates a soft break (line break) without starting a new paragraph.",
                                    "Shift + Enter deletes the current sentence.",
                                    "Shift + Enter saves the file automatically.",
                                    "Shift + Enter opens the Font preferences dialog."
                        ],
                        "correctAnswer": "Shift + Enter creates a soft break (line break) without starting a new paragraph.",
                        "explanation": "Shift + Enter inserts an inline soft break, continuing on the next line within the same paragraph formatting block."
            }
],
        "flashcards": [
            {
                        "question": "What is the shortcut to reset highlighted text back to the default font in Word?",
                        "answer": "Ctrl + Spacebar"
            },
            {
                        "question": "What shortcut key executes Save As in Microsoft Word?",
                        "answer": "F12 (or Alt + F, A)"
            },
            {
                        "question": "What does Ctrl + Shift + * do in Word?",
                        "answer": "It toggles the display of non-printing characters (spaces, tabs, paragraph marks)."
            },
            {
                        "question": "What shortcut key runs a Thesaurus check on a selected word?",
                        "answer": "Shift + F7"
            },
            {
                        "question": "What shortcut opens the Font preferences dialog window?",
                        "answer": "Ctrl + D"
            }
]
    },
    {
        "order": 5,
        "title": "Lab 5: Microsoft Excel Spreadsheet Design, Formulas & Japanese Car Dataset",
        "codeSnippet": "# Excel Formulas for Sum, Average, Percentage and Scaling\n=SUM(B4:C4)\n=D4/SUM($D$4:$D$9)\n=AVERAGE(B4:B9)\n=IF(E18>=3.0, \"A\", \"B\")",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 5\n\nIntroduction to MS Excel\n\n\n## Objective\n\n\nLearn to create spreadsheets using Microsoft excel\n\n\n## Theory\n\n\nMicrosoft Excel:\n\nMicrosoft Excel is the most widespread program for creating spreadsheets on the market today. Spreadsheets allow you to organize information in rows and tables (which create cells), with the added bonus of automatic mathematics. Spreadsheets have been used for many, many years in business to keep track of expenses and other calculations. Excel will keep track of numbers you place in cells, and if you define cells to refer to each other, any changes made in one cell will be reflected in these referring cells. It sounds a bit complicated, but Excel makes it all a breeze.\n\nOpening Microsoft Excel:\n\nStart >> Programs >> Microsoft Office >> Microsoft Office Excel 2010\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_grid.png)\n\n\nMicrosoft Excel will automatically open with a blank spreadsheet spanning many columns and rows. You will notice a number of toolbars with many more options included.\n\nPresentation of Data in Tables\n\nIn all aspects of your university study and professional career, good, clear presentation of data and information is essential to the success with which your audience receives your information. Simple features within Excel can really enhance how your data looks and improve comparability of data sets.\n\nAfter entering the following data set into Excel we will use features, to improve the presentation of the data.\n\nFrom this....\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_unformatted_cells.png)\n\n\n\u2026to this\u2026\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_margins.png)\n\n\nEntering Data\n\nWhen you open a workbook, by default, Excel selects cell A1 as the active cell.\n\nBegin typing your data into the active cell.\n\nPress the Enter key to move the active cell down (e.g. A2) OR Press the Tab key to move the active cell to the right (e.g. B1)\n\nTo activate a random cell, move the cursor to that cell with the mouse and click on the mouse button.\n\nTo select a group of adjacent cells, click on the first cell and drag the cursor across the adjoining cells.\n\nTo select a group of random cells, click the first cell, hold down the CTRL key and click the additional cells.\n\nColumn Widths / Row Widths\n\nTo change the column width to display all the data clearly,\n\nMove the cursor with the mouse to the right of the column heading of the column you want to widen (i.e. A B C D, etc). The cursor will turn into a cross symbol.\n\nDouble click the mouse and the column will automatically widen to the width of the contents. OR Click and drag the column to widen manually.\n\nRow widths are adjusted the same way, except you place the cursor between the row headings.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_orientation.png)\n\n\nTo insert Columns or Row\n\nTo insert a column within a data set:\n\nSelect the column to the right of where you want to position the new column, by clicking on the column heading (i.e. A B C D, etc).\n\n\n![Diagram](assets/images/university/itc/lab5_excel_header_footer.png)\n\n\nRight click your mouse while your cursor is over the column heading.\n\nClick on Insert.\n\nTo insert a row within a data set:\n\nSelect the row below where you want to position the new row, by clicking on the row heading (i.e. 1 2 3 4, etc).\n\nRight click your mouse while your cursor is over the row heading.\n\nClick on Insert.\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_page_setup.png)\n\n\nMerging Cells\n\nTo centre a heading across the width of the data set\n\nSelect the cell that contains the heading and drag the cursor across the columns that represent the data set.\n\nClick on the Merge and Center button on the toolbar.\n\nAutoFill:\n\nExcel has an AutoFill facility that is very useful. You can read all about this in the built-in Help\n\nFor now, try the following:\n\nOn a new worksheet, click in A1 and type Jan\n\nPoint precisely to the fill handle (small black +) in the bottom right-hand corner of the cell.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_column_width.png)\n\n\nDrag this down to the A12 and then release the button\n\nExcel should have filled in the months of the year\n\nNow try days of the week (type mon or monday)\n\nFill two adjacent cells with 0 and 5, select both cells and drag the fill handle to generate 10, 15, 20\u2026\u2026\n\nFilling Cells with the same data:\n\nThere is a quick way of entering the same data into a range of cells.\n\nHighlight an area of cells (for example, A1:A6)\n\nType some characters or a number\n\nPress the Ctrl and Enter keys at the same time\n\nRemove the highlighting by clicking in any cell\n\nWord Wrap:\n\nA long string of text can be made to wrap onto several lines within a cell using this facility.\n\nClick in a cell and then select Cells from the Format menu\n\nClick on the Alignment tab\n\nClick in the wrap text box, so that it is ticked\n\n\n![Diagram](assets/images/university/itc/lab5_excel_insert_menu.png)\n\n\nClick OK\n\nType some text and note how it wraps\n\nPress the Enter Key\n\nPage Setup:\n\n\n![Diagram](assets/images/university/itc/lab5_excel_insert_column.png)\n\n\nThe page setup allows you to format the page, set margins, and add headers and footers. To view the Page Setup select Windows Button > Print > Print Preview >Page Setup.\n\nSelect the Orientation under the Page tab in the Page Setup dialog box to make the page Landscape or Portrait. The size of the worksheet on the page can also be formatted under the Scaling title. To force a worksheet to be printed on one page, select Fit to 1 page(s).\n\n4124325-271145\n\n\n![Diagram](assets/images/university/itc/lab5_excel_wrap_text.png)\n\n\nMargins:\n\nChange the top, bottom, left, and right margins under the Margins tab. Enter values in the Header/Footer fields to indicate how far from the edge of the page this text should appear. Check the boxes for centering Horizontally or Vertically to center the page.\n\nHeader/Footer:\n\n\n![Diagram](assets/images/university/itc/lab5_excel_percentage_button.png)\n\n\nAdd preset Headers and Footers to the page by clicking the drop-down menus under the Header/Footer tab.\n\nTo modify a preset Header or Footer, or to make your own, click the Custom Header or Custom Footer buttons.\n\nA new window will open allowing you to enter text in the left, center, or right on the page.\n\nFormat Text \u2013 After highlighting the text click this button to change the Font, Size, and Style.\n\nPage Number - Insert the page number of each page.\n\nTotal Number of Pages - Use this feature along with the page number to create strings such as \"page 1 of 15\".\n\n\n![Diagram](assets/images/university/itc/lab5_excel_percent_style.png)\n\n\nDate - Add the current date.\n\nTime - Add the current time.\n\nFile Name - Add the name of the workbook file.\n\nSheet Name - Add the name of worksheet.\n\nPicture - Add a picture.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_rounding.png)\n\n\nSheet:\n\nClick the Sheet tab and check Gridlines box under the Print section if you wantthe gridlines dividing the cells to appearon the page. If the worksheet is severalpages long and only the first page includes titles for the columns, select Rows to repeat at the topof the Print titles section to choose a title row that will be printed at the top of each page.\n\nAutoSum Function\n\nTo automatically total a row or column of numbers\n\n\n![Diagram](assets/images/university/itc/lab5_excel_autosum_button.png)\n\n\nFor a row of numbers, select the empty cell directly to the right of the numbers, then:\n\nClick the AutoSum button on the right hand side of the Home ribbon\n\nThe SUM formula including the range of numbers selected will appear in the formula bar\n\nCheck you have the correct range and then press the Enter button.\n\nOR\n\nFor a column of numbers, select the empty cell directly below the numbers, then continue with steps 1 to 3 above.\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_autosum_formula.png)\n\n\nRounding\n\nTo round a decimal value to a whole number or simply increase or decrease the number of decimal places a value has:\n\n\n![Diagram](assets/images/university/itc/lab5_excel_custom_sort.png)\n\n\nSelect the cell/s containing the value/s you want to alter\n\nClick on the Decrease Decimal button to remove decimal places\n\nOR\n\nClick on the Increase Decimal button to add decimal places\n\nSimple calculations\n\nTo carry out simple calculations:\n\nThink about how you would do the problem in your head or on your calculator.\n\nThink about how Excel may carry this out and get Excel to do it by clicking on the relevant cell/s and using the appropriate combination of:\n\naddition +\n\nsubtraction -\n\nmultiplication *\n\ndivision /\n\nbrackets ()\n\nto the power of ^\n\nRound appropriately using the \u201cDecrease Decimal\u201d button or the \u201cIncrease Decimal\u201d button as per Rounding instructions above.\n\nPercentages\n\nTo create a percentage from a proportion (decimal), simply use the Percent Style button. This will automatically display the proportion (decimal) to the nearest whole percent, so:\n\n\n![Diagram](assets/images/university/itc/lab5_excel_custom_sort.png)\n\n\n0.003will become 0%\n\n0.03will become 3%\n\n0.3will become 30%\n\n3will become 300%\n\nSelect the cell/s containing the number/s you want to alter\n\nClick on the Percent Style button to round to the nearest whole percentage\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_borders_menu.png)\n\n\nBorders\n\nBorders can be applied individually to each of the 4 sides of a cell or applied to a group of cells. Borders allow you to separate data groups and highlight specific sections of data. To add a border to a cell or group of cells\n\nSelect the cell(s) that you want to place a border around\n\nClick on the down arrow  of the Borders button on the toolbar. A range of different border buttons will be displayed.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_borders_grid.png)\n\n\nClick on the Borders button you want for the selected cells.\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_sample_sheet.png)\n\n\nSorting Data\n\n\n![Diagram](assets/images/university/itc/lab5_excel_formatted_cells.png)\n\n\nTo sort data numerically or alphabetically\n\nSelect the rows of data you want to sort\n\nClick on the Sort and Filter button on the Home ribbon.\n\nClick on Custom Sort.\n\nNext to the Sort By heading, click on the down arrow  to select the column on which you want to sort the data\n\n\n![Diagram](assets/images/university/itc/lab5_excel_borders_grid.png)\n\n\nSelect either Smallest to Largest or Largest to Smallest.\n\nClick OK.\n\nCharts\n\nCharts make data visual. With a chart you can transform spreadsheet data to show comparisons, patterns, and trends.\n\nIn Excel 2007, you just select data in your worksheet, choose a chart type that best suits your purpose, and click. That\u2019s it! You can also use the new Chart Tools to customize the design, layout, and formatting of your chart. Just like the preview capability you saw in Word 2007 and PowerPoint 2007, you can see how various options would look just by pointing at them in the dialog box, even before you make a choice.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_autofill.png)\n\n\n4 Clicks to create a simple chart in Excel 2007\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_insert_elements.png)\n\n\nLet\u2019s say we want to see graphically the sales of beverages in our caf\u00e9 in the first 3 months of the year.\n\nSelect the cells containing the sales data, including cells with text (e.g. column and row headings for the data.)\n\nSelect Insert tab.\n\nSelect Column icon from Charts group\n\nSelect Clustered Column chart from 2-D Column type\n\nThe chart shows the sales of the 4 different beverages grouped together for each month. What if we want to see what happened in the sales of each beverage month over month?\n\nSelect the chart, Chart Tools -> Design -> Data -> Switch Row/Column.\n\nChart Elements\n\nA chart has many elements. Some of these elements are displayed by default; others can be added as needed. You can change the display of the chart elements by moving them to other locations in the chart, resizing them, or by changing the format. You can also remove chart elements that you do not want to display.\n\nHere are some standard chart elements.\n\nThe chart area encompasses the entire chart and all its elements.\n\n\n![Diagram](assets/images/university/itc/lab5_excel_charts.png)\n\n\nThe plot area is that area bounded by the axes, including all data series, category names, axis titles, and all markers that represent data points.\n\nThe data points are the individual values plotted in a chart and represented by bars, columns, lines, pie or doughnut slices, dots, and various other shapes called data markers. Data markers of the same color constitute a data series (i.e. related data points. You can plot one or more data series in a chart, but pie charts have only one data series.\n\nThe horizontal (category) or vertical (value) axis is a line bordering the chart plot area used as a frame of reference for measurement. The y-axis is usually the vertical axis and contains data. The x-axis is usually the horizontal axis and contains the categories.\n\nA legend is a box that identifies the patterns or colors that are assigned to the data series or categories in a chart.\n\nA chart title is the descriptive text for a chart. Note that horizontal and vertical axes usually have titles too.\n\nModifying charts\n\nAfter you create a chart, you can modify it. For example, you may want to change the way that axes are displayed, add a chart title, move or hide the legend, or display additional chart elements.\n\nTo modify an element in the chart, you can right-click on it and choose the appropriate (format) option. Or, you can use the appropriate tabs, groups and options under Chart Tools.\n\nAdd titles to a chart: Chart Tools -> Layout -> Labels -> Chart Title\n\nAdd axis titles to a chart: Chart Tools -> Layout -> Labels -> Axis Title\n\nAdd legend to a chart: Chart Tools -> Layout -> Labels -> Legend\n\nAdd data labels to a chart: Chart Tools -> Layout -> Labels -> Data Labels\n\nAdd data table to a chart: Chart Tools -> Layout -> Labels -> Data Table\n\nTo change formatting and layout of each axes: Chart Tools -> Layout -> Axes ->Axes\n\nTo turn gridlines on or off: Chart Tools -> Layout -> Axes -> Gridlines\n\nTo format the plot area: Chart Tools -> Background -> Plot Area\n\nTo format the chart wall (for 3-D charts): Chart Tools -> Background -> Chart Wall\n\nTo format the chart floor (for 3-D charts): Chart Tools -> Background -> Chart Floor\n\nTo change 3D viewpoint of a chart: Chart Tools -> Background -> 3-D Rotation\n\nTo move chart to a different sheet: Chart Tools -> Design -> Location -> Move Chart\n\nExcel Shortcut Keys\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_chart_steps.png)\n\n\nLab Task____________________________________________________________\n\nCreate a marks sheet on Microsoft excel, which calculates the marks, Gpa and Grade of 5 courses of a student. Also create a chart to display the result in graphical form.\n\nAttach a printout with your lab manual\n\nSample__________________________________________________________________________\n\n\n\n\n![Diagram](assets/images/university/itc/lab5_excel_chart_elements.png)\n",
        "quizzes": [
            {
                        "question": "Which Excel keyboard shortcut automatically generates the '=SUM(...)' formula to total adjacent numbers above the active cell?",
                        "options": [
                                    "Alt + =",
                                    "Ctrl + S",
                                    "Shift + F11",
                                    "Ctrl + Shift + A"
                        ],
                        "correctAnswer": "Alt + =",
                        "explanation": "Alt + = is the universal Excel shortcut to automatically insert the AutoSum formula for adjacent rows or columns."
            },
            {
                        "question": "What happens in Excel when a user enters a decimal value of 0.30 and applies the Percent Style shortcut (Ctrl + Shift + %)?",
                        "options": [
                                    "The cell displays 30%",
                                    "The cell displays 0.3%",
                                    "The cell displays 300%",
                                    "The cell displays an invalid formula error #VALUE!"
                        ],
                        "correctAnswer": "The cell displays 30%",
                        "explanation": "Excel multiplies decimal proportions by 100 and appends the % symbol: 0.30 becomes 30%."
            },
            {
                        "question": "Which keyboard shortcut selects an entire column in Microsoft Excel?",
                        "options": [
                                    "Ctrl + Space",
                                    "Shift + Space",
                                    "Alt + Space",
                                    "Ctrl + Shift + C"
                        ],
                        "correctAnswer": "Ctrl + Space",
                        "explanation": "Ctrl + Space selects the entire active column; Shift + Space selects the entire active row."
            },
            {
                        "question": "In the Japanese Car dataset, if cell B4 contains Trouble-free cars (44) and D4 contains Total cars (85), which formula calculates Trouble-free percentage?",
                        "options": [
                                    "=B4/D4",
                                    "=B4*D4",
                                    "=SUM(B4:D4)",
                                    "=AVERAGE(B4-D4)"
                        ],
                        "correctAnswer": "=B4/D4",
                        "explanation": "Percentage proportion is calculated as Part divided by Total: =B4/D4."
            },
            {
                        "question": "What keyboard shortcut allows editing the contents of the currently selected cell directly in the formula bar?",
                        "options": [
                                    "F2",
                                    "F5",
                                    "F7",
                                    "F12"
                        ],
                        "correctAnswer": "F2",
                        "explanation": "Pressing F2 activates the in-cell edit mode in Excel without overwriting existing data."
            }
],
        "flashcards": [
            {
                        "question": "What shortcut key creates a chart from selected data in Excel immediately?",
                        "answer": "F11"
            },
            {
                        "question": "What shortcut selects an entire row in Microsoft Excel?",
                        "answer": "Shift + Space"
            },
            {
                        "question": "What shortcut enters the current dynamic date in an Excel cell?",
                        "answer": "Ctrl + ;"
            },
            {
                        "question": "What feature forces multi-line text to display inside a single cell?",
                        "answer": "Wrap Text (Format Cells -> Alignment -> Wrap text)."
            },
            {
                        "question": "What is the function of the AutoFill Fill Handle in Excel?",
                        "answer": "It detects sequences and automatically extends dates, days, numbers, and formulas when dragged."
            }
]
    },
    {
        "order": 6,
        "title": "Lab 6: Microsoft Excel Applied Analysis - Ohm's Law Calculations & Advanced Charts",
        "codeSnippet": "# Excel Engineering Formulas for Ohm's Law (V = I * R)\n# In Cell C2: =A2 * $B$1 (Current * Fixed Resistance)\n# Linear Trendline slope represents resistance: R = dV / dI",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 6\n\nIntroduction to MS Excel (continued)\n\n\n## Objective\n\n\nLearn to create spreadsheets using Microsoft excel\n\nLab Task____________________________________________________________\n\nUsing Excel formula to calculate value of voltage, when a list of current and resistance is given.\n\nUsing Excel Chart feature, create Line and XY Graph to draw graph of voltage vs current.\n\nUsing Excel Chart feature, create Bar graph for a cricket team Match vs its scores.",
        "quizzes": [
            {
                        "question": "In an Excel XY Scatter plot of Ohm's Law (Voltage vs Current), what physical parameter does the slope of the linear trendline represent?",
                        "options": [
                                    "Resistance (R)",
                                    "Electrical Power (P)",
                                    "Capacitance (C)",
                                    "Inductance (L)"
                        ],
                        "correctAnswer": "Resistance (R)",
                        "explanation": "Because V = I * R, the graph of V (y-axis) vs I (x-axis) has the equation y = mx, where slope m = V/I = R (Resistance)."
            },
            {
                        "question": "Which Excel formula syntax ensures that cell reference '$B$1' remains fixed when dragging the formula down multiple rows?",
                        "options": [
                                    "Absolute Cell Reference ($B$1)",
                                    "Relative Cell Reference (B1)",
                                    "Mixed Cell Reference (B$1 only for column)",
                                    "Circular Reference"
                        ],
                        "correctAnswer": "Absolute Cell Reference ($B$1)",
                        "explanation": "The dollar signs ($) lock both the column letter and row number, preventing Excel from shifting the reference during fill operations."
            },
            {
                        "question": "Which chart type in Microsoft Excel is specifically designed to plot numeric coordinates against numeric coordinates for scientific data?",
                        "options": [
                                    "XY (Scatter) Chart",
                                    "Pie Chart",
                                    "Radar Chart",
                                    "Doughnut Chart"
                        ],
                        "correctAnswer": "XY (Scatter) Chart",
                        "explanation": "XY Scatter charts treat both axes as numerical value scales, making them the standard choice for scientific and engineering data."
            }
],
        "flashcards": [
            {
                        "question": "What is the formula for Ohm's Law?",
                        "answer": "V = I * R (Voltage = Current * Resistance)."
            },
            {
                        "question": "Why use an XY Scatter chart instead of a Line chart for experimental physics data?",
                        "answer": "An XY Scatter chart plots true numerical scales along both X and Y axes, whereas a Line chart treats the X axis as categorical text labels."
            },
            {
                        "question": "How do you display the mathematical equation of a line on an Excel chart?",
                        "answer": "Right-click the data series -> Add Trendline -> Check 'Display Equation on chart'."
            }
]
    },
    {
        "order": 7,
        "title": "Lab 7: Microsoft Access Relational Database Design, Data Types & Relationships",
        "codeSnippet": "-- Relational schema matching Lab 7 specification\nCREATE TABLE Student (\n    StudentID VARCHAR(20) PRIMARY KEY,\n    FirstName VARCHAR(50) NOT NULL,\n    LastName VARCHAR(50) NOT NULL,\n    Department VARCHAR(50),\n    Semester INT\n);\n\nCREATE TABLE Marks (\n    StudentID VARCHAR(20) PRIMARY KEY,\n    ITC INT CHECK (ITC BETWEEN 0 AND 100),\n    Mathematics INT,\n    English INT,\n    Electronics INT,\n    Physics INT,\n    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON DELETE CASCADE\n);",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 7\n\nMicrosoft Access\n\n\n## Objective\n\n\nLearn to create databases using Microsoft access\n\n\n## Theory\n\n\nFamiliarization With Some Basic Database Related Terms:\n\nA record is a row in a datasheet and is a set of values defined by fields. In a mailing list table, each record would contain the data for one person as specified by the intersecting fields.\n\nA field is a column in a datasheet and defines a data type for a set of values in a table.\n\nFor a mailing list table might include fields for first name, last name, address, city, state, zip code, and telephone number.\n\nA table is a grouping of related data organized in fields (columns) and records (rows) on a datasheet. By using a common field in two tables, the data can be combined. Many tables can be stored in a single database.\n\nA database is a collection of related information.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_welcome.png)\n\n\n\n## GETTING STARTED\n\n\nAfter opening Access, you will be presented with two major options as shown in the figure above.  First, if you are creating a new database or the second if  you want to  open and  edit an existing database. Details about both of these choices are given below:\n\nOpen an existing database\n\nIf the database was opened recently on the computer, it will be listed in the File Menu either directly or inside Recent  option. Highlight the database name and click OK.\n\nOtherwise, click Open (Ctrl + O) from the File Menu, navigate to the proper folder location, highlight the database name in the listing and click OK.\n\nCreating a new database\n\nClick New (Ctrl + N) option inside the File Menu. You will be presented with MS Access available database templates both offline and online and then you are required to select any one of them to create your new database. Some of the example offline database templates include Blank Database, Blank Web database, sample database, etc. Some of the example online database templates include Assets, Contacts, Issues and Tasks etc.  Unlike Word documents, Excel worksheets, and Power Point presentations, you must save an Access database before you start working on it. After selecting \"Blank Access database\" for example, you will first be prompted to specify a location and a name for the database.\n\nNavigating Access Window\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_database_window.png)\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_object_pane.png)\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_ribbon.png)\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_navigation.png)\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_toolbar.png)\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_view_selector.png)\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_design_view.png)\n\n\n\n## SCREEN LAYOUTS\n\n\nDatabase Window\n\nThe Database Window organizes all of the objects in the database, e.g. Tables, Queries, Forms, etc. The default table listing provides links for creating or modifying tables and will list all of the tables in the database when they have been added.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_datasheet_view.png)\n\n\nDesign View\n\nDesign View customizes the fields in the database so that data can be entered.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_field_properties.png)\n\n\nDatasheet View\n\nThe datasheet view allows you to enter data into the database.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_add_field.png)\n\n\n\n## CREATING TABLES\n\n\nIntroduction to Tables\n\n\n![Diagram](assets/images/university/itc/lab7_access_rename_field.png)\n\n\nTables are grids that store information in a database similar to the way an Excel worksheet stores information in a workbook, to create a table Click Create from Main Menu. Access provides two ways to create a table for which there are icons  Table and Table design.\n\nClick on any icon to create a table. Create table in Design view will allow you to create the fields of the table. This is the most common way of creating a table and is explained in detail below.\n\nCreate table by entering data will give you a blank datasheet with just ID field and the rest  with unlabeled columns that looks much like an Excel worksheet. Enter data into the cells and click the Save button. After the table is saved, the empty cells of the datasheet are trimmed. The fields are given generic names such as \"Field1\", \"Field2\", etc. To rename them with more descriptive titles that reflect the content of the fields, change the view to Design view again and modify names as per requirements.\n\nCreate a Table in Design View\n\n4432414Top Pane174307528575Design View will allow you to define the fields in the table before adding any data to the datasheet. The window is divided into two parts: a top pane for entering the field name, data type, and an option description of the field, and a bottom pane for specifying field properties\n\n\n![Diagram](assets/images/university/itc/lab7_access_delete_record.png)\n\n\n44\n\n3\n\n24\n\n14\n\nTop Pane\n\nBottom PaneField Name - This is the name of the field and should represent the contents of the field such as \"Name\", \"Address\", \"Final Grade\", etc. The name cannot exceed 64 characters in length and may include spaces.\n\nBottom Pane\n\nData Type - is the type of value that will be entered into the fields.\n\nText  -  The default type, text type allows any combination of letters and numbers up to a maximum of 255 characters per field record.\n\nMemo - A text type that stores up to 64,000 characters.\n\nNumber - Any number can be stored.\n\nDate/Time - A date, time, or combination of both.\n\nCurrency - Monetary values that can be set up to automatically include a dollar sign ($) and correct decimal and comma positions.\n\nAutoNumber - When a new record is created, Access will automatically assign a unique integer to the record in this field. From the General options, select Increment if the numbers should be assigned in order or random if any random number should be chosen. Since every record in a datasheet must include at least one field that distinguishes it from all others, this is a useful data type to use if the existing data will not produce such values.\n\nYes/No  -  Use this option for True/False, Yes/No, On/Off, or other values that must be only one of two.\n\nOLE Object  -  An OLE (Object Linking and Embedding) object is a sound, picture, or other object such as a Word document or Excel spreadsheet that is created in another program. Use this data type to embed an OLE object or link to the object in the database.\n\nHyperlink  -  A hyperlink will link to an Internet or Intranet site, or another location in the database. The data consists of up to four parts each separated by the pound sign (#): DisplayText#Address#SubAddress#ScreenTip. The Address is the only required part of the string. Examples:\n\nInternet hyperlink example:  FGCU Home Page#http://www.fgcu.edu#\n\nDatabase link example:  #c:\\My Documents\\database.mdb#MyTable\n\nDescription (optional) - Enter a brief description of what the contents of the field are.\n\nField Properties - Select any pertinent properties for the field from the bottom pane.\n\nProperties for each field are set from the bottom pane of the Design View window.\n\nField Size is used to set the number of characters needed in a text or number field. The default field size for the text type is 50 characters. If the records in the field will only have two or three characters, you can change the size of the field to save disk space or prevent entry errors by limiting the number of characters allowed. Likewise, if the field will require more than 50 characters, enter a number up to 255. The field size is set in exact characters for Text type, but options are given for numbers:\n\nByte - Positive integers between 1 and 255\n\nInteger - Positive and negative integers between -32,768 and 32,768\n\nLong Integer (default)  -  Larger positive and negative integers between -2 billion and 2 billion.\n\nSingle - Single-precision floating-point number\n\nDouble - Double-precision floating-point number\n\nDecimal - Allows for Precision and Scale property control\n\nFormat confirms the data in the field to the same format when it is entered into the datasheet. For text and memo fields, this property has two parts that are separated by a semicolon. The first part of the property is used to apply to the field and the second applies to empty fields.\n\nPrimary Key\n\nEvery record in a table must have a primary key that differentiates it from every other record in the table. In some cases, it is only necessary to designate an existing field as the primary key if you are certain that every record in the table will have a different value for that particular field. A social security number is an example of a record whose values will only appear once in a database table.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_primary_key.png)\n\n\nDesignate the primary key field by right-clicking on the record and selection Primary Key from the shortcut menu or select Primary Key from the  Quick Access Toolbar .\n\nThe primary key field will be noted with a key image to the left. To remove a primary key, repeat one of these steps.\n\nIndexes\n\nCreating indexes allows Access to query and sort records faster. To set an indexed field, select a field that is commonly searched and change the Indexed property to Yes\n\n(Duplicates OK) if multiple entries of the same data value are allowed or Yes (No Duplicates) to prevent duplicates.\n\nField Validation Rules\n\nValidation Rules specify requirements (change word) for the data entered in the worksheet.\n\nA customized message can be displayed to the user when data that violates the rule setting is entered. Click the expression builder (\"...\") button at the end of the Validation Rule box to write the validation rule. Examples of field validation rules include <> 0  to not allow zero values in the record, and ??? to only all data strings three characters in length.\n\nInput Masks\n\nAn input mask controls the value of a record and sets it in a specific format. They are similar  to the Format property, but instead display the format on the datasheet before the data is entered. For example, a telephone number field can formatted with an input mask to accept ten digits that are automatically formatted as \"(555) 123-4567\". The blank field would look like (___) ___-____. Add an input mask to a field by following these steps:\n\nIn design view, place the cursor in the field that the input mask will be applied to.\n\nClick in the white space following Input Mask under the General tab.\n\nClick the \"...\" button to use the wizard or enter the mask, (@@@) @@@-@@@@, into the field provided.\n\nDATASHEET RECORDS\n\nAdding Records\n\n\n![Diagram](assets/images/university/itc/lab7_access_table_fields.png)\n\n\nAdd new records to the table in datasheet view by typing in the record beside the asterisk\n\n(*) that marks the new record.\n\nEditing Records\n\n\n![Diagram](assets/images/university/itc/lab7_access_create_table.png)\n\n\nTo edit records, simply place the cursor in the record that is to be edited and make the necessary changes. Use the arrow keys to move through the record grid. The previous, next, first, and last record buttons at the bottom of the datasheet are helpful in maneuvering through the datasheet.\n\nDeleting Records\n\n\n![Diagram](assets/images/university/itc/lab7_access_add_record.png)\n\n\nDelete a record on a datasheet by placing the cursor in any field of the record row and\n\nselect Delete Record  from the menu bar or click the  Delete  button on the  Quick Access toolbar.\n\nAdding and Deleting Columns\n\nAlthough it is best to add new fields (displayed as columns in the datasheet) in design view because more options are available, they can also be quickly added in datasheet view.\n\n2428875-114300Highlight the column that the new column should appear to the left of by clicking its label at the top of the datasheet and press right click then select  Insert field  from the  dropdown menu.  Entire columns can be deleted by placing the cursor in the column and selecting Delete field from the dropdown menu.\n\n\n![Diagram](assets/images/university/itc/lab7_access_new_record_indicator.png)\n\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_sort_records.png)\n\n\nFreezing and unfreezing Columns\n\nSimilar to freezing panes in Excel, columns on an Access table can be frozen. This is helpful if the datasheet has many columns and relevant data would otherwise not appear on the screen at the same time. Freeze a column by placing the cursor in any record in the column and select Freeze fields from the right click dropdown men. Select the same option to unfreeze a single column or select Unfreeze All fields\n\n\n![Diagram](assets/images/university/itc/lab7_access_filter_selection.png)\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_filter_options.png)\n\n\nFinding Data in a Table\n\nOpen the table in datasheet view. Place the cursor in any record in the field that you want to search and select Home|Find  (Ctrl + F)...  from the  Quick Access  toolbar. Enter the value criteria in the Find What:  box. From the Look In:  drop-down menu, define the area of the search by selecting the entire table or just the field in the table you placed your cursor in during step 2. Select the matching criteria from Match: to and click the More >> button for additional search parameters. When all of the search criteria are set, click the Find Nextbutton. If more than one record meets the criteria, keep clicking Find Next until you reach the correct record.\n\n\n### Table Relationships\n\n\nTo prevent the duplication of information in a database by repeating fields in more than one table, table relationships can be established to link fields of tables together. Once you are in Design view or in datasheet view of a table, Table Tools Menu is automatically highlighted then click the Relationships  button on the toolbar.  . From the Show Table window (click the Show Table button on the toolbar to make it appear), double click on the names of the tables or queries you would like to include in the relationships.\n\n\n![Diagram](assets/images/university/itc/lab7_access_toggle_filter.png)\n\n\nWhen you have finished adding tables or queries, click Close. To link fields in two different tables, click and drag a field from one table to the corresponding field on the other table and release the mouse button. The Edit Relationships window will appear. From this window, select different fields if necessary and select an option from Enforce Referential Integrity if necessary. These options give Access permission to automatically make changes to referential tables if key-records in one of the tales is deleted or updated. Check the Enforce Referential Integrity box to ensure that the relationships are valid and that the data is not accidentally deleted when data is added, edited, or deleted. Click Create to create the link. A line now connects the two fields in the Relationships window. The datasheet of a relational table will provide expand and collapse indicators to view sub-datasheets containing matching information from the other table.\n\nSORTING & FILTERING\n\nSorting and filtering allow you to view records in a table in a different way either by reordering all of the records in the table or view only those records in a table that meet certain criteria that you specify.\n\nSorting\n\n\n![Diagram](assets/images/university/itc/lab7_access_freeze_columns.png)\n\n\nIn table datasheet view, place the cursor in the column that you want to sort by. Select\n\nAscending or Descending  from the  Quick Access toolbar  under Home main menu  or click the Sort A to Z or Sort Z to A from the dropdown menu.\n\nTo sort by more than one column (such as sorting by date and then sorting records with the same date alphabetically), highlight the columns by clicking and dragging the mouse over the field labels and select one of the sort methods stated above\n\nFilter by Selection\n\nThis feature will filter records that contain identical data values in a given field such as filtering out all of the records that have the value \"Smith\" in a name field. To Filter by\n\n\n![Diagram](assets/images/university/itc/lab7_access_unfreeze_columns.png)\n\n\nSelection, place the cursors in the field that you want to filter the other records by and click the  Selection  button  inside Home main menu  on the toolbar or  directly select the criteria from right click dropdown menu.\n\n\n![Diagram](assets/images/university/itc/lab7_access_relationships_view.png)\n\n\nFilter by Form\n\nIf the table is large, it may be difficult to find the record that contains the value you would like to filter by so using Filter by Form may be advantageous instead. This method creates\n\na blank version of the table with drop-down menus for each field that each contains the values found in the records of that field.\n\nThe following methods can be used to select records based on the record selected by that do not have exactly the same value. Type these formats into the field where the drop-down menu appears instead of selecting an absolute value.\n\nSaving a Filter\n\nThe filtered contents of a table can be saved as a query by selecting  Advanced|Save As\n\nQuery. Enter a name for the query and click OK.  The query is now saved within the database.\n\nRemove a Filter\n\nTo view all records in a table again, click the depressed toggle Filter button.\n\n\n\n\n![Diagram](assets/images/university/itc/lab7_access_table_relationships.png)\n\n\n\n## Lab Task\n\n\nCreate the following tables in Microsoft Access:\n\nTable1:  Student (containing fields:  Student ID,  First Name, Last Name, Department  and Semester).\n\nTable2:  Marks (containing fields: Student ID,  ITC, Mathematics, English, Electronics, Physics)\n\nSelect appropriate primary keys and define the appropriate relationship for these two tables. Add some sample data to the tables and make a hard copy of the tables created. Attach the printout with your manual.",
        "quizzes": [
            {
                        "question": "What primary constraint distinguishes a table's Primary Key field in Microsoft Access?",
                        "options": [
                                    "It uniquely identifies every record in the table and cannot contain NULL or duplicate values.",
                                    "It must always contain decimal currency amounts.",
                                    "It automatically hides the table from unauthorized users.",
                                    "It can only be edited using SQL command scripts."
                        ],
                        "correctAnswer": "It uniquely identifies every record in the table and cannot contain NULL or duplicate values.",
                        "explanation": "A Primary Key uniquely distinguishes each entity record and strictly prohibits duplicate entries and NULL values."
            },
            {
                        "question": "Which Microsoft Access data type should be selected when a field needs to store narrative descriptions exceeding 255 characters?",
                        "options": [
                                    "Memo",
                                    "Text",
                                    "OLE Object",
                                    "Hyperlink"
                        ],
                        "correctAnswer": "Memo",
                        "explanation": "Standard Text fields cap at 255 characters; Memo fields store up to 64,000 characters."
            },
            {
                        "question": "What is the key benefit of checking 'Enforce Referential Integrity' when linking two database tables in Access?",
                        "options": [
                                    "It prevents orphan records by ensuring foreign key values correspond to valid primary keys in the parent table.",
                                    "It doubles the maximum disk storage capacity of the database file.",
                                    "It automatically converts all numbers to Roman numerals.",
                                    "It turns off all validation rule checks."
                        ],
                        "correctAnswer": "It prevents orphan records by ensuring foreign key values correspond to valid primary keys in the parent table.",
                        "explanation": "Referential integrity guarantees relationship consistency, forbidding child records with non-existent parent IDs and managing cascading deletes."
            },
            {
                        "question": "What symbol marks the empty row ready for data entry at the bottom of a table in Access Datasheet View?",
                        "options": [
                                    "An asterisk (*)",
                                    "A question mark (?)",
                                    "A pound sign (#)",
                                    "A dollar sign ($)"
                        ],
                        "correctAnswer": "An asterisk (*)",
                        "explanation": "In Access Datasheet View, an asterisk (*) marks the new blank row waiting for record insertion."
            },
            {
                        "question": "How does Microsoft Access differ from Word and Excel regarding when the file must be saved?",
                        "options": [
                                    "Access requires you to name and save the database file before creating tables or entering data.",
                                    "Access cannot save files to local hard disks.",
                                    "Access only saves files when the computer is turned off.",
                                    "Access never saves data automatically."
                        ],
                        "correctAnswer": "Access requires you to name and save the database file before creating tables or entering data.",
                        "explanation": "Access manages real-time disk persistence; you must establish the database file container before designing objects."
            }
],
        "flashcards": [
            {
                        "question": "What is a Record in an Access database table?",
                        "answer": "A horizontal row in a datasheet containing a complete set of attribute values for a single entity."
            },
            {
                        "question": "What is a Field in an Access database table?",
                        "answer": "A vertical column defining a specific attribute and data type."
            },
            {
                        "question": "What does AutoNumber data type do?",
                        "answer": "It automatically assigns a unique sequential or random integer to each newly created record."
            },
            {
                        "question": "What is the maximum character limit for an Access standard Text data type?",
                        "answer": "255 characters."
            },
            {
                        "question": "What is an Input Mask in Microsoft Access?",
                        "answer": "A property that dictates and displays the required formatting pattern on screen before data is entered (e.g. phone numbers)."
            }
]
    },
    {
        "order": 8,
        "title": "Lab 8: Introduction to HTML  -  Document Structure, Headings & Paragraphs",
        "codeSnippet": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Heading Example</title>\n</head>\n<body>\n    <h1>This is heading 1</h1>\n    <h2>This is heading 2</h2>\n    <h3>This is heading 3</h3>\n    <h4>This is heading 4</h4>\n    <h5>This is heading 5</h5>\n    <h6>This is heading 6</h6>\n    <p>Here is a first paragraph of text.</p>\n    <p>Here is a second paragraph of text.</p>\n</body>\n</html>",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 8\n\nHTML\n\nDated: _______________\n\n\n## Objective\n\n\nLearn to create web page using HTML\n\n\n## Theory\n\n\nHTML stands for\u00a0Hypertext\u00a0Markup\u00a0Language, and it is the most widely used language to write Web Pages.\n\nHypertext\u00a0refers to the way in which Web pages (HTML documents) are linked together. Thus, the link available on a webpage is called Hypertext.\n\nAs its name suggests, HTML is a\u00a0Markup Language\u00a0which means you use HTML to simply \"mark-up\" a text document with tags that tell a Web browser how to structure it to display.\n\nOriginally, HTML was developed with the intent of defining the structure of documents like headings, paragraphs, lists, and so forth to facilitate the sharing of scientific information between researchers.\n\nNow, HTML is being widely used to format web pages with the help of different tags available in HTML language.\n\nBasic HTML Document\n\nIn its simplest form, following is an example of an HTML document \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<title>This is document title</title><head>\n\nHi there !\n\n</head>\n\n<body>\n\n<h1>This is a heading</h1>\n\n<p>Document content goes here.....</p>\n\n</body>\n\n<   /   html>\n\nHTML Tags\n\nAs told earlier, HTML is a markup language and makes use of various tags to format the content. These tags are enclosed within angle braces\u00a0<Tag Name>. Except few tags, most of the tags have their corresponding closing tags. For example,\u00a0<html>\u00a0has its closing tag\u00a0</html>\u00a0and\u00a0<body>\u00a0tag has its closing tag\u00a0</body>\u00a0tag etc.\n\nAbove example of HTML document uses the following tags \u2212\n\n\n\n| Sr.No | Tag & Description |\n\n| --- | --- |\n\nSr.No\n\nTag & Description\n\n\n\n| 1 | <!DOCTYPE...> This tag defines the document type and HTML version. |\n\n| --- | --- |\n\n1\n\n<!DOCTYPE...>\n\nThis tag defines the document type and HTML version.\n\n\n\n| 2 | <html> This tag encloses the complete HTML document and mainly comprises of document header which is represented by <head>...</head> and document body which is represented by <body>...</body> tags. |\n\n| --- | --- |\n\n2\n\n<html>\n\nThis tag encloses the complete HTML document and mainly comprises of document header which is represented by <head>...</head> and document body which is represented by <body>...</body> tags.\n\n\n\n| 3 | <head> This tag represents the document's header which can keep other HTML tags like <title>, <link> etc. |\n\n| --- | --- |\n\n3\n\n<head>\n\nThis tag represents the document's header which can keep other HTML tags like <title>, <link> etc.\n\n\n\n| 4 | <title> The <title> tag is used inside the <head> tag to mention the document title. |\n\n| --- | --- |\n\n4\n\n<title>\n\nThe <title> tag is used inside the <head> tag to mention the document title.\n\n\n\n| 5 | <body> This tag represents the document's body which keeps other HTML tags like <h1>, <div>, <p> etc. |\n\n| --- | --- |\n\n5\n\n<body>\n\nThis tag represents the document's body which keeps other HTML tags like <h1>, <div>, <p> etc.\n\n\n\n| 6 | <h1> T.his tag represents the heading. |\n\n| --- | --- |\n\n6\n\n<h1>\n\nT.his tag represents the heading.\n\n\n\n| 7 | <p></p> This tag represents a paragraph. |\n\n| --- | --- |\n\n7\n\n<p></p>\n\nThis tag represents a paragraph.\n\nTo learn HTML, you will need to study various tags and understand how they behave, while formatting a textual document. Learning HTML is simple as users have to learn the usage of different tags in order to format the text or images to make a beautiful webpage.\n\nWorld Wide Web Consortium (W3C) recommends to use lowercase tags starting from HTML 4.\n\nHTML Document Structure\n\nA typical HTML document will have the following structure \u2212\n\n<html>\n\n<head>\n\nDocument header related tags\n\n</head>\n\n<body>\n\nDocument body related tags\n\n</body>\n\n</html>\n\nThe <!DOCTYPE> Declaration\n\nThe <!DOCTYPE> declaration tag is used by the web browser to understand the version of the HTML used in the document. Current version of HTML is 5 and it makes use of the following declaration \u2212\n\n<!DOCTYPE html>\n\nThere are many other declaration types which can be used in HTML document depending on what version of HTML is being used. We will see more details on this while discussing <!DOCTYPE...> tag along with other HTML tags.\n\n\n## Heading Tags\n\n\nAny document starts with a heading. You can use different sizes for your headings. HTML also has six levels of headings, which use the elements\u00a0<h1>, <h2>, <h3>, <h4>, <h5>,\u00a0and\u00a0<h6>. While displaying any heading, browser adds one line before and one line after that heading.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Heading Example</title>\n\n</head>\n\n<body>\n\n<h1>This is heading 1</h1>\n\n<h2>This is heading 2</h2>\n\n<h3>This is heading 3</h3>\n\n<h4>This is heading 4</h4>\n\n<h5>This is heading 5</h5>\n\n<h6>This is heading 6</h6>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\n\n## Paragraph Tag\n\n\nThe\u00a0<p>\u00a0tag offers a way to structure your text into different paragraphs. Each paragraph of text should go in between an opening <p> and a closing </p> tag as shown below in the example \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Paragraph Example</title>\n\n</head>\n\n<body>\n\n<p>Here is a first paragraph of text.</p>\n\n<p>Here is a second paragraph of text.</p>\n\n<p>Here is a third paragraph of text.</p>\n\n</body>\n\n</html>\n\n\n## Lab Task\n\n\nCreate a webpage that prints your name to the screen.\n\nCreate a webpage that prints the numbers 1 - 10 to the screen.\n\nCreate a webpage and set its title to \"This is a webpage\".\n\nCreate a webpage that prints the message to the screen, and set the title of the page to the current date.",
        "quizzes": [
            {
                        "question": "What does the abbreviation HTML stand for?",
                        "options": [
                                    "Hypertext Markup Language",
                                    "High-Tech Modern Language",
                                    "Hyper Transfer Module Layout",
                                    "Home Tool Markup Link"
                        ],
                        "correctAnswer": "Hypertext Markup Language",
                        "explanation": "HTML stands for Hypertext Markup Language. Hypertext refers to clickable links between pages, and Markup refers to tagging text with structural formatting."
            },
            {
                        "question": "Which declaration informs the web browser that the document is written in modern HTML5?",
                        "options": [
                                    "<!DOCTYPE html>",
                                    "<doctype html5>",
                                    "<?xml version='1.0'?>",
                                    "<html version='5.0'>"
                        ],
                        "correctAnswer": "<!DOCTYPE html>",
                        "explanation": "In HTML5, the standard doctype declaration is simply <!DOCTYPE html>, which is placed at the very top of the document."
            },
            {
                        "question": "How many levels of headings does HTML provide natively?",
                        "options": [
                                    "6 levels (<h1> to <h6>)",
                                    "3 levels (<h1> to <h3>)",
                                    "8 levels (<h1> to <h8>)",
                                    "10 levels (<h1> to <h10>)"
                        ],
                        "correctAnswer": "6 levels (<h1> to <h6>)",
                        "explanation": "HTML defines six heading levels, ranging from <h1> (the largest, top-level heading) down to <h6> (the smallest subheading)."
            }
],
        "flashcards": [
            {
                        "question": "What is the purpose of the <title> tag in an HTML document?",
                        "answer": "It specifies the title of the webpage, which appears in the browser's title bar or tab, and is placed inside the <head> element."
            },
            {
                        "question": "What does W3C recommend regarding HTML tag case starting from HTML 4?",
                        "answer": "The World Wide Web Consortium (W3C) recommends writing all HTML tags and attributes in lowercase."
            },
            {
                        "question": "What automatic spacing does a web browser add around HTML heading tags?",
                        "answer": "The browser automatically adds one empty line of vertical margin before and after every heading element."
            },
            {
                        "question": "Which HTML element encloses all visible contents of a webpage displayed in the browser window?",
                        "answer": "The <body> element."
            }
]
    },
    {
        "order": 9,
        "title": "Lab 9: HTML Continued  -  Attributes, Text Formatting & Hyperlinks",
        "codeSnippet": "<!DOCTYPE html>\n<html>\n<head>\n    <title>HTML Formatting and Hyperlinks</title>\n</head>\n<body bgcolor=\"green\">\n    <p align=\"center\" id=\"html\">This para explains what is <b>HTML</b></p>\n    <p align=\"left\" id=\"css\">The following word uses <i>italicized</i>, <u>underlined</u>, and <strike>strikethrough</strike> typeface.</p>\n    <p>Polynomial: 2x<sup>3</sup> + 5x<sup>2</sup> + 3x + 9 = 0</p>\n    <p>Logarithm: log<sub>10</sub>(x + 2Y)</p>\n    <p>I want to drink <del>cola</del> <ins>wine</ins></p>\n    <p>Comparing <big>big</big> and <small>small</small> text with <tt>monospaced</tt> font.</p>\n    <a href=\"contact_us.html\">CONTACT</a> | <a href=\"http://www.yahoo.com/\">ABOUT</a>\n</body>\n</html>",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 9\n\nHTML (continued)\n\nDated: _______________\n\n\n## Objective\n\n\n\\\n\nLearn to create web page using HTML\n\n\n## Theory\n\n\nHTML Attributes:\n\nAn attribute is used to define the characteristics of an HTML element and is placed inside the element's opening tag. All attributes are made up of two parts \u2212 a\u00a0name\u00a0and a\u00a0value\n\nThe\u00a0name\u00a0is the property you want to set. For example, the paragraph\u00a0<p>\u00a0element in the example carries an attribute whose name is\u00a0align, which you can use to indicate the alignment of paragraph on the page.\n\nThe\u00a0value\u00a0is what you want the value of the property to be set and always put within quotations. The below example shows three possible values of align attribute:\u00a0left, center\u00a0and\u00a0right.\n\nAttribute names and attribute values are case-insensitive. However, the World Wide Web Consortium (W3C) recommends lowercase attributes/attribute values in their HTML 4 recommendation.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>write anything you want </title>\n\n</head>\n\n<body>\n\n<p align=\"left\">This is left aligned</p>\n\n<p align=\"center\">This is center aligned</p>\n\n<p align=\"right\">This is right aligned</p>\n\n</body>\n\n</html>\n\n\n## Core Attributes\n\n\nThe four core attributes that can be used on the majority of HTML elements (although not all) are \u2212\n\nId\n\nTitle\n\nClass\n\nStyle\n\nThe Id Attribute\n\nThe\u00a0id\u00a0attribute of an HTML tag can be used to uniquely identify any element within an HTML page. There are two primary reasons that you might want to use an id attribute on an element \u2212\n\nIf an element carries an id attribute as a unique identifier, it is possible to identify just that element and its content.\n\nIf you have two elements of the same name within a Web page (or style sheet), you can use the id attribute to distinguish between elements that have the same name.\n\nWe will discuss style sheet in separate tutorial. For now, let's use the id attribute to distinguish between two paragraph elements as shown below.\n\n\n### Example\n\n\n<p id = \"html\">This para explains what is HTML</p>\n\n<p id = \"css\">This para explains what is Cascading Style Sheet</p>\n\nThe bgcolor Attribute\n\nPlaces a background color behind an element. Like <body>\n\nIt can have three types of values: numeric, hexidecimal, RGB values\n\n\n### Example\n\n\n<body bgcolor = \"green\">This para explains what is HTML</body>\n\n<body bgcolor = (0,255,0)>This para explains what is HTML</body>\n\nBold Text\n\nAnything that appears within\u00a0<b>...</b>\u00a0element, is displayed in bold as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Bold Text Example</title>\n\n</head>\n\n<body>\n\n<b>The following word uses a bold typeface</b>|The following word uses a bold typeface\n\n</body>\n\n</html>\n\nItalic Text\n\nAnything that appears within\u00a0<i>...</i>\u00a0element is displayed in italicized as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Italic Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses an <i>italicized</i> typeface.</p>\n\n</body>\n\n</html>\n\nUnderlined Text\n\nAnything that appears within\u00a0<u>...</u>\u00a0element, is displayed with underline as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Underlined Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses an <u>underlined</u> typeface.</p>\n\n</body>\n\n</html>\n\nStrike Text\n\nAnything that appears within\u00a0<strike>...</strike>\u00a0element is displayed with strikethrough, which is a thin line through the text as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Strike Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <strike>strikethrough</strike> typeface.</p>\n\n</body>\n\n</html>\n\nMonospaced Font\n\nThe content of a\u00a0<tt>...</tt>\u00a0element is written in monospaced font. Most of the fonts are known as variable-width fonts because different letters are of different widths (for example, the letter 'm' is wider than the letter 'i'). In a monospaced font, however, each letter has the same width.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Monospaced Font Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <tt>monospaced</tt> typeface.</p>\n\n</body>\n\n</html>\n\nSuperscript Text\n\nThe content of a\u00a0<sup>...</sup>\u00a0element is written in superscript; the font size used is the same size as the characters surrounding it but is displayed half a character's height above the other characters.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Superscript Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <sup>superscript</sup> typeface.</p>\n\n<p>2x<sup>3</sup>+5x<sup>2</sup>+3x+9=0</p>\n\n</body>\n\n</html>\n\nSubscript Text\n\nThe content of a\u00a0<sub>...</sub>\u00a0element is written in subscript; the font size used is the same as the characters surrounding it, but is displayed half a character's height beneath the other characters.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Subscript Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <sub>subscript</sub> typeface.</p>\n\n<p>Following is general formulae: log<sub>10</sub>(x+2Y)\n\n</body>\n\n</html>\n\nInserted Text\n\nAnything that appears within\u00a0<ins>...</ins>\u00a0element is displayed as inserted text.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Inserted Text Example</title>\n\n</head>\n\n<body>\n\n<p>I want to drink <del>cola</del><ins>wine</ins></p>\n\n</body>\n\n</html>\n\nDeleted Text\n\nAnything that appears within\u00a0<del>...</del>\u00a0element, is displayed as deleted text.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Deleted Text Example</title>\n\n</head>\n\n<body>\n\n<p>I want to drink <del>cola</del><ins>wine</ins></p>\n\n</body>\n\n</html>\n\nLarger Text\n\nThe content of the\u00a0<big>...</big>\u00a0element is displayed one font size larger than the rest of the text surrounding it as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Larger Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <big>big</big> typeface.</p>\n\n</body>\n\n</html>\n\nSmaller Text\n\nThe content of the\u00a0<small>...</small>\u00a0element is displayed one font size smaller than the rest of the text surrounding it as shown below \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Smaller Text Example</title>\n\n</head>\n\n<body>\n\n<p>The following word uses a <small>small</small> typeface.</p>\n\n</body>\n\n</html>\n\nHyper Text\n\nThe hyper text of a text uses\u00a0<a>...</a>\u00a0element. You can refer/link your page to some other web page as well as some other web site.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Div Tag Example</title>\n\n</head>\n\n<body>\n\n<a href=\u201dcontact_us.html\">CONTACT</a> |\n\n<a href=\"http://www.yahoo.com/\">ABOUT</a>\n\n</body>\n\n</html>\n\n\n## Lab Task\n\n\nCreate a webpage that displays a table of contents page of Chapter 1 -4\n\nCreate hyper link on each chapter that refers to separate web page for each chapter.\n\nInclude link on each chapter to go back to main page.\n\nIn each chapter use all tags and attributes studies in this lab.",
        "quizzes": [
            {
                        "question": "Which two parts make up every HTML attribute?",
                        "options": [
                                    "A name and a value (name=\"value\")",
                                    "A tag and a closing bracket",
                                    "A class and an ID",
                                    "A source and a destination"
                        ],
                        "correctAnswer": "A name and a value (name=\"value\")",
                        "explanation": "All HTML attributes consist of a name (the property being configured) and a value (the assigned setting inside quotes)."
            },
            {
                        "question": "Which HTML tag is used to write mathematical powers like x\u00b2 in superscript?",
                        "options": [
                                    "<sup>",
                                    "<sub>",
                                    "<power>",
                                    "<up>"
                        ],
                        "correctAnswer": "<sup>",
                        "explanation": "The <sup> tag renders superscript text positioned half a character's height above the standard baseline."
            },
            {
                        "question": "How does a monospaced font (<tt>) differ from standard variable-width fonts?",
                        "options": [
                                    "Every letter in a monospaced font has the exact same horizontal width",
                                    "Monospaced fonts are always italicized and bold",
                                    "Letters are drawn with double pixel borders",
                                    "It only displays numerical digits"
                        ],
                        "correctAnswer": "Every letter in a monospaced font has the exact same horizontal width",
                        "explanation": "In a monospaced font, all characters (including narrow letters like 'i' and wide letters like 'm') occupy identical horizontal spacing."
            }
],
        "flashcards": [
            {
                        "question": "What are the four core attributes usable across most HTML elements?",
                        "answer": "id, title, class, and style."
            },
            {
                        "question": "What is the difference between <del> and <ins> tags?",
                        "answer": "<del> displays text as deleted (with a strikethrough), while <ins> displays text as inserted (underlined)."
            },
            {
                        "question": "What tag is used to create hyperlinks in HTML?",
                        "answer": "The anchor tag: <a href=\"URL\">Link Text</a>."
            },
            {
                        "question": "What are three valid formats for values assigned to the bgcolor attribute?",
                        "answer": "Color names ('green'), hexadecimal codes ('#00FF00'), and RGB values ('(0,255,0)')."
            }
]
    },
    {
        "order": 10,
        "title": "Lab 10: HTML Continued (Advanced)  -  Grouping, Images, Tables, Lists & Forms",
        "codeSnippet": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Educational Consultancy Portal</title>\n</head>\n<body>\n    <!-- Header Section -->\n    <div style=\"background-color:#eee; padding:10px;\">\n        <h1>Global Education Consultancy</h1>\n        <a href=\"#feedback\">Skip to Feedback Form</a>\n    </div>\n\n    <!-- Course Table -->\n    <h2>Available Programs & Fees</h2>\n    <table border=\"1\" cellpadding=\"5\" cellspacing=\"5\">\n        <tr>\n            <th>Program Name</th>\n            <th>Duration</th>\n            <th>Tuition Fee</th>\n        </tr>\n        <tr>\n            <td>Computer Science (BSCS)</td>\n            <td>4 Years</td>\n            <td>$5000 / year</td>\n        </tr>\n        <tr>\n            <td>Software Engineering</td>\n            <td>4 Years</td>\n            <td>$5200 / year</td>\n        </tr>\n    </table>\n\n    <!-- Services List -->\n    <h2>Services Offered</h2>\n    <ul type=\"square\">\n        <li>University Admissions Guidance</li>\n        <li>Visa Documentation & Filing</li>\n        <li>IELTS / TOEFL Preparation</li>\n    </ul>\n\n    <!-- Order / Consultation Form -->\n    <h2 id=\"feedback\">Book Consultation</h2>\n    <form action=\"process.php\" method=\"POST\" enctype=\"multipart/form-data\">\n        First name: <input type=\"text\" name=\"first_name\"/><br/><br/>\n        User ID: <input type=\"text\" name=\"user_id\"/><br/><br/>\n        Password: <input type=\"password\" name=\"password\"/><br/><br/>\n        \n        Subjects of Interest:<br/>\n        <input type=\"checkbox\" name=\"maths\" value=\"on\"> Mathematics\n        <input type=\"checkbox\" name=\"cs\" value=\"on\" checked> Computer Science<br/><br/>\n        \n        Degree Level:<br/>\n        <input type=\"radio\" name=\"level\" value=\"undergrad\" checked> Undergraduate\n        <input type=\"radio\" name=\"level\" value=\"grad\"> Postgraduate<br/><br/>\n        \n        Country Destination:<br/>\n        <select name=\"country\">\n            <option value=\"UK\" selected>United Kingdom</option>\n            <option value=\"USA\">United States</option>\n            <option value=\"Canada\">Canada</option>\n        </select><br/><br/>\n        \n        Statement of Purpose:<br/>\n        <textarea rows=\"5\" cols=\"40\" name=\"sop\">Enter details...</textarea><br/><br/>\n        \n        Upload Academic Transcript:<br/>\n        <input type=\"file\" name=\"transcript\" accept=\"application/pdf,image/*\"/><br/><br/>\n        \n        <input type=\"hidden\" name=\"portal_version\" value=\"1.0\"/>\n        <input type=\"submit\" name=\"submit\" value=\"Submit Application\"/>\n        <input type=\"reset\" name=\"reset\" value=\"Reset Form\"/>\n    </form>\n</body>\n</html>",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 10\n\nHTML (continued)\n\nDated: _______________\n\n\n## Objective\n\n\nLearn to create web page using HTML\n\n\n## Theory\n\n\nGrouping Content\n\nThe\u00a0<div>\u00a0and\u00a0<span>\u00a0elements allow you to group together several elements to create sections or subsections of a page.\n\nFor example, you might want to put all of the footnotes on a page within a <div> element to indicate that all of the elements within that <div> element relate to the footnotes. You might then attach a style to this <div> element so that they appear using a special set of style rules.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\nThe <span> element, on the other hand, can be used to group inline elements only. So, if you have a part of a sentence or paragraph which you want to group together, you could use the <span> element as follows.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Span Tag Example</title>\n\n</head>\n\n<body>\n\n<p>This is the example of <spanstyle=\"color:green\">span tag</span>\n\nand the <spanstyle=\"color:red\">div tag</span> alongwith CSS</p>\n\n</body>\n\n</html>\n\nHTML - Comments\n\nComment is a piece of code which is ignored by any web browser. It is a good practice to add comments into your HTML code, especially in complex documents, to indicate sections of a document, and any other notes to anyone looking at the code. Comments help you and others understand your code and increases code readability.\n\nHTML comments are placed in between\u00a0<!-- ... -->\u00a0tags. So, any content placed with-in <!-- ... --> tags will be treated as comment and will be completely ignored by the browser.\n\nHTML - Images\n\nImages are very important to beautify as well as to depict many complex concepts in simple way on your web page. This tutorial will take you through simple steps to use images in your web pages.\n\nInsert Image\n\nYou can insert any image in your web page by using\u00a0<img>\u00a0tag. Following is the simple syntax to use this tag.\n\n<img src = \"Image URL\" ... attributes-list/>\n\nThe <img> tag is an empty tag, which means that, it can contain only list of attributes and it has no closing tag.\n\n\n### Example\n\n\n<img src=\"/html/images/test.png\"alt=\"Test Image\"/>\n\nYou can use PNG, JPEG or GIF image file based on your comfort but make sure you specify correct image file name in\u00a0src\u00a0attribute. Image name is always case sensitive.\n\nThe\u00a0alt\u00a0attribute is a mandatory attribute which specifies an alternate text for an image, if the image cannot be displayed.\n\nSet Image Location\n\nUsually we keep all the images in a separate directory. So let's keep HTML file test.htm in our home directory and create a subdirectory\u00a0images\u00a0inside the home directory where we will keep our image test.png.\n\n\n### Example\n\n\n<img src=\"/html/images/test.png\" alt=\"Test Image\"/>\n\nSet Image Width/Height\n\nYou can set image width and height based on your requirement using\u00a0width\u00a0and\u00a0height\u00a0attributes. You can specify width and height of the image in terms of either pixels or percentage of its actual size.\n\n\n### Example\n\n\n<img src=\"/html/images/test.png\" alt=\"Test Image\" width=\"150\" height=\"100\"/>\n\nSet Image Border\n\nBy default, image will have a border around it, you can specify border thickness in terms of pixels using border attribute. A thickness of 0 means, no border around the picture.\n\n\n### Example\n\n\n<img src=\"/html/images/test.png\" alt=\"Test Image\"\n\nSet Image Alignment\n\nBy default, image will align at the left side of the page, but you can use\u00a0align\u00a0attribute to set it in the center or right.\n\n\n### Example\n\n\n<imgsrc=\"/html/images/test.png\"alt=\"Test Image\"border=\"3\"align=\"right\"/>\n\nFree Web Graphics\n\nFor Free Web Graphics including patterns you can look into\u00a0Free Web Graphicshttps://www.tutorialspoint.com/free_web_graphics.htm\n\nHTML - Text Links\n\nA webpage can contain various links that take you directly to other pages and even specific parts of a given page. These links are known as hyperlinks.\n\nHyperlinks allow visitors to navigate between Web sites by clicking on words, phrases, and images. Thus you can create hyperlinks using text or images available on a webpage.\n\nNote\u00a0\u2212 I recommend you to go through a short tutorial on\u00a0Understanding URL\n\nLinking Documents\n\nA link is specified using HTML tag <a>. This tag is called\u00a0anchor tag\u00a0and anything between the opening <a> tag and the closing </a> tag becomes part of the link and a user can click that part to reach to the linked document. Following is the simple syntax to use <a> tag.\n\n<a href = \"Document URL\" ... attributes-list>Link Text</a>\n\n\n### Example\n\n\nLet's try following example which links http://www.tutorialspoint.com at your page \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Hyperlink Example</title>\n\n</head>\n\n<body>\n\n<p>Click following link</p>\n\n<ahref=\"https://www.tutorialspoint.com\"target=\"_self\">Tutorials Point</a>\n\n</body>\n\n</html>\n\nThis will produce the following result, where you can click on the link generated to reach to the home page of Tutorials Point (in this example).\n\nThe target Attribute\n\nWe have used\u00a0target\u00a0attribute in our previous example. This attribute is used to specify the location where linked document is opened. Following are the possible options \u2212\n\n\n\n| Sr.No | Option & Description |\n\n| --- | --- |\n\nSr.No\n\nOption & Description\n\n\n\n| 1 | _blank: Opens the linked document in a new window or tab. |\n\n| --- | --- |\n\n1\n\n_blank: Opens the linked document in a new window or tab.\n\n\n\n| 2 | _self:Opens the linked document in the same frame. |\n\n| --- | --- |\n\n2\n\n_self:Opens the linked document in the same frame.\n\n\n\n| 3 | _parent:Opens the linked document in the parent frame. |\n\n| --- | --- |\n\n3\n\n_parent:Opens the linked document in the parent frame.\n\n\n\n| 4 | _top:Opens the linked document in the full body of the window. |\n\n| --- | --- |\n\n4\n\n_top:Opens the linked document in the full body of the window.\n\n\n\n| 5 | Targetframe:Opens the linked document in a named\u00a0targetframe. |\n\n| --- | --- |\n\n5\n\nTargetframe:Opens the linked document in a named\u00a0targetframe.\n\n\n### Example\n\n\nTry following example to understand basic difference in few options given for target attribute.\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Hyperlink Example</title>\n\n<basehref=\"https://www.tutorialspoint.com/\">\n\n</head>\n\n<body>\n\n<p>Click any of the following links</p>\n\n<ahref=\"/html/index.htm\"target=\"_blank\">Opens in New</a> |\n\n<ahref=\"/html/index.htm\"target=\"_self\">Opens in Self</a> |\n\n<ahref=\"/html/index.htm\"target=\"_parent\">Opens in Parent</a> |\n\n<ahref=\"/html/index.htm\"target=\"_top\">Opens in Body</a>\n\n</body>\n\n</html>\n\nThis will produce the following result, where you can click on different links to understand the difference between various options given for target attribute.\n\nLinking to a Page Section\n\nYou can create a link to a particular section of a given webpage by using\u00a0name\u00a0attribute. This is a two-step process.\n\nNote\u00a0\u2212 The\u00a0name\u00a0attribute deprecated in HTML5. Do not use this attribute. Use\u00a0id\u00a0and\u00a0title\u00a0attribute instead.\n\nFirst create a link to the place where you want to reach with-in a webpage and name it using <a...> tag as follows \u2212\n\n<h1>HTML Text Links <a name = \"top\"></a></h1>\n\nSecond step is to create a hyperlink to link the document and place where you want to reach \u2212\n\n<a href = \"/html/html_text_links.htm#top\">Go to the Top</a>\n\nThis will produce following link, where you can click on the link generated\u00a0Go to the Top\u00a0to reach to the top of the HTML Text Link tutorial.\n\nGo to the Top\n\nHTML - Image Links\n\nWe have seen how to create hypertext link using text and we also learnt how to use images in our webpages. Now, we will learn how to use images to create hyperlinks.\n\n\n### Example\n\n\nIt's simple to use an image as hyperlink. We just need to use an image inside hyperlink at the place of text as shown below \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Image Hyperlink Example</title>\n\n</head>\n\n<body>\n\n<p>Click following link</p>\n\n<a href=\"https://www.tutorialspoint.com\"target=\"_self\">\n\n<imgsrc=\"/images/logo.png\"alt=\"Tutorials Point\"border=\"0\"/>\n\n</a>\n\n</body>\n\n</html>\n\nThis will produce the following result, where you can click on the images to reach to the home page of Tutorials Point.\n\nThis was the simplest way of creating hyperlinks using images. Next we will see how we can create Mouse-Sensitive Image Links.\n\nHTML - Tables\n\nThe HTML tables allow web authors to arrange data like text, images, links, other tables, etc. into rows and columns of cells.\n\nThe HTML tables are created using the\u00a0<table>\u00a0tag in which the\u00a0<tr>\u00a0tag is used to create table rows and\u00a0<td>\u00a0tag is used to create data cells. The elements under <td> are regular and left aligned by default\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Tables</title>\n\n</head>\n\n<body>\n\n<table border=\"2\">\n\n<tr>\n\n<td>Row 1, Column 1</td>\n\n<td>Row 1, Column 2</td><td>Row 1, Column 3</td>\n\n</tr>\n\n<tr>\n\n<td>Row 2, Column 1</td>\n\n<td>Row 2, Column 2</td>\n\n</tr>\n\n</table>\n\n</body>\n\n</html>\n\nHere, the\u00a0border\u00a0is an attribute of <table> tag and it is used to put a border across all the cells. If you do not need a border, then you can use border = \"0\".\n\n\n### Table Heading\n\n\n\n### Table heading can be defined using\u00a0<th>\u00a0tag. This tag will be put to replace <td> tag, which is used to represent actual data cell. Normally you will put your top row as table heading as shown below, otherwise you can use <th> element in any row. Headings, which are defined in <th> tag are centered and bold by default.\n\n\nCellpadding and Cellspacing Attributes\n\nThere are two attributes called\u00a0cellpadding\u00a0and\u00a0cellspacing\u00a0which you will use to adjust the white space in your table cells. The cellspacing attribute defines space between table cells, while cellpadding represents the distance between cell borders and the content within a cell.\n\nThis will produce the following result \u2212\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Table Cellpadding</title>\n\n</head>\n\n<body>\n\n<tableborder=\"1\"cellpadding=\"5\"cellspacing=\"5\">\n\n<tr>\n\n<th>Name</th>\n\n<th>Salary</th>\n\n</tr>\n\n<tr>\n\n<td>Ramesh Raman</td>\n\n<td>5000</td>\n\n</tr>\n\n<tr>\n\n<td>Shabbir Hussein</td>\n\n<td>7000</td>\n\n</tr>\n\n</table>\n\n</body>\n\n</html>\n\nHTML - Lists\n\nHTML offers web authors three ways for specifying lists of information. All lists must contain one or more list elements. Lists may contain \u2212\n\n<ul>\u00a0\u2212 An unordered list. This will list items using plain bullets.\n\n<ol>\u00a0\u2212 An ordered list. This will use different schemes of numbers to list your items.\n\n<dl>\u00a0\u2212 A definition list. This arranges your items in the same way as they are arranged in a dictionary.\n\nHTML Unordered Lists\n\nAn unordered list is a collection of related items that have no special order or sequence. This list is created by using HTML\u00a0<ul>\u00a0tag. Each item in the list is marked with a bullet.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Unordered List</title>\n\n</head>\n\n<body>\n\n<ul>\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ul>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\nThe type Attribute\n\nYou can use\u00a0type\u00a0attribute for <ul> tag to specify the type of bullet you like. By default, it is a disc. Following are the possible options \u2212\n\n<ul type = \"square\">\n\n<ul type = \"disc\">\n\n<ul type = \"circle\">\n\n\n### Example\n\n\nFollowing is an example where we used <ul type = \"square\">\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Unordered List</title>\n\n</head>\n\n<body>\n\n<ultype=\"square\">\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ul>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\n\n### Example\n\n\nFollowing is an example where we used <ul type = \"disc\"> \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Unordered List</title>\n\n</head>\n\n<body>\n\n<ultype=\"disc\">\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ul>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\n\n### Example\n\n\nFollowing is an example where we used <ul type = \"circle\"> \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Unordered List</title>\n\n</head>\n\n<body>\n\n<ultype=\"circle\">\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ul>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\nHTML Ordered Lists\n\nIf you are required to put your items in a numbered list instead of bulleted, then HTML ordered list will be used. This list is created by using\u00a0<ol>\u00a0tag. The numbering starts at one and is incremented by one for each successive ordered list element tagged with <li>.\n\n\n### Example\n\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Ordered List</title>\n\n</head>\n\n<body>\n\n<ol>\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ol>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\nThe type Attribute\n\nYou can use\u00a0type\u00a0attribute for <ol> tag to specify the type of numbering you like. By default, it is a number. Following are the possible options \u2212\n\n<ol type = \"1\"> - Default-Case Numerals.\n\n<ol type = \"I\"> - Upper-Case Numerals.\n\n<ol type = \"i\"> - Lower-Case Numerals.\n\n<ol type = \"A\"> - Upper-Case Letters.\n\n<ol type = \"a\"> - Lower-Case Letters.\n\n\n### Example\n\n\nFollowing is an example where we used <ol type = \"1\">\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>HTML Ordered List</title>\n\n</head>\n\n<body>\n\n<ol type=\"1\">\n\n<li>Beetroot</li>\n\n<li>Ginger</li>\n\n<li>Potato</li>\n\n<li>Radish</li>\n\n</ol>\n\n</body>\n\n</html>\n\nHTML - Forms\n\nHTML Forms are required, when you want to collect some data from the site visitor. For example, during user registration you would like to collect information such as name, email address, credit card, etc.\n\nA form will take input from the site visitor and then will post it to a back-end application such as CGI, ASP Script or PHP script etc. The back-end application will perform required processing on the passed data based on defined business logic inside the application.\n\nThere are various form elements available like text fields, textarea fields, drop-down menus, radio buttons, checkboxes, etc.\n\nThe HTML\u00a0<form>\u00a0tag is used to create an HTML form and it has following syntax \u2212\n\n<form action = \"Script URL\" method = \"GET|POST\">\n\nform elements like input, textarea etc.\n\n</form>\n\nForm Attributes\n\nApart from common attributes, following is a list of the most frequently used form attributes \u2212\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Action:Backend script ready to process your passed data. |\n\n| --- | --- |\n\n1\n\nAction:Backend script ready to process your passed data.\n\n\n\n| 2 | Method:Method to be used to upload data. The most frequently used are GET and POST methods. |\n\n| --- | --- |\n\n2\n\nMethod:Method to be used to upload data. The most frequently used are GET and POST methods.\n\n\n\n| 3 | Target:Specify the target window or frame where the result of the script will be displayed. It takes values like _blank, _self, _parent etc. |\n\n| --- | --- |\n\n3\n\nTarget:Specify the target window or frame where the result of the script will be displayed. It takes values like _blank, _self, _parent etc.\n\n\n\n| 4 | Enctype:You can use the enctype attribute to specify how the browser encodes the data before it sends it to the server. Possible values are \u2212 application/x-www-form-urlencoded\u00a0\u2212 This is the standard method most forms use in simple scenarios. mutlipart/form-data\u00a0\u2212 This is used when you want to upload binary data in the form of files like image, word file etc. |\n\n| --- | --- |\n\n4\n\nEnctype:You can use the enctype attribute to specify how the browser encodes the data before it sends it to the server. Possible values are \u2212\n\napplication/x-www-form-urlencoded\u00a0\u2212 This is the standard method most forms use in simple scenarios.\n\nmutlipart/form-data\u00a0\u2212 This is used when you want to upload binary data in the form of files like image, word file etc.\n\nNote\u00a0\u2212 You can refer to\u00a0Perl & CGI\u00a0for a detail on how form data upload works.\n\nHTML Form Controls\n\nThere are different types of form controls that you can use to collect data using HTML form \u2212\n\nText Input Controls\n\nCheckboxes Controls\n\nRadio Box Controls\n\nSelect Box Controls\n\nFile Select boxes\n\nHidden Controls\n\nClickable Buttons\n\nSubmit and Reset Button\n\nText Input Controls\n\nThere are three types of text input used on forms \u2212\n\nSingle-line text input controls\u00a0\u2212 This control is used for items that require only one line of user input, such as search boxes or names. They are created using HTML\u00a0<input>\u00a0tag.\n\nPassword input controls\u00a0\u2212 This is also a single-line text input but it masks the character as soon as a user enters it. They are also created using HTMl <input> tag.\n\nMulti-line text input controls\u00a0\u2212 This is used when the user is required to give details that may be longer than a single sentence. Multi-line input controls are created using HTML\u00a0<textarea>\u00a0tag.\n\nSingle-line text input controls\n\nThis control is used for items that require only one line of user input, such as search boxes or names. They are created using HTML <input> tag.\n\n\n### Example\n\n\nHere is a basic example of a single-line text input used to take first name and last name \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<body>\n\n<form>\n\nFirst name: <input type=\"text\"name=\"first_name\"/>\n\nLast name: <input type=\"text\"name=\"last_name\"/>\n\n</form>\n\n</body>\n\n</html>\n\nAttributes\n\nFollowing is the list of attributes for <input> tag for creating text field.\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Type:Indicates the type of input control and for text input control it will be set to\u00a0text. |\n\n| --- | --- |\n\n1\n\nType:Indicates the type of input control and for text input control it will be set to\u00a0text.\n\n\n\n| 2 | Name:Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n2\n\nName:Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 3 | Value:This can be used to provide an initial value inside the control. |\n\n| --- | --- |\n\n3\n\nValue:This can be used to provide an initial value inside the control.\n\n\n\n| 4 | Size:Allows to specify the width of the text-input control in terms of characters. |\n\n| --- | --- |\n\n4\n\nSize:Allows to specify the width of the text-input control in terms of characters.\n\n\n\n| 5 | Maxlength:Allows to specify the maximum number of characters a user can enter into the text box. |\n\n| --- | --- |\n\n5\n\nMaxlength:Allows to specify the maximum number of characters a user can enter into the text box.\n\nPassword input controls\n\nThis is also a single-line text input but it masks the character as soon as a user enters it. They are also created using HTML <input>tag but type attribute is set to\u00a0password.\n\n\n### Example\n\n\nHere is a basic example of a single-line password input used to take user password \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Password Input Control</title>\n\n</head>\n\n<body>\n\n<form>\n\nUser ID : <input type=\"text\" name=\"user_id\"/>\n\n<br>\n\nPassword: <input type=\"password\" name=\"password\"/>\n\n</form>\n\n</body>\n\n</html>\n\nMultiple-Line Text Input Controls\n\nThis is used when the user is required to give details that may be longer than a single sentence. Multi-line input controls are created using HTML <textarea> tag.\n\n\n### Example\n\n\nHere is a basic example of a multi-line text input used to take item description \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Multiple-Line Input Control</title>\n\n</head>\n\n<body>\n\n<form>\n\nDescription : <br/>\n\n<textarea rows=\"50\"cols=\"50\"name=\"description\">\n\nEnter description here...\n\n</textarea>\n\n</form>\n\n</body>\n\n</html>\n\nThis will produce the following result \u2212\n\nAttributes\n\nFollowing is the list of attributes for <textarea> tag.\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Name: Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n1\n\nName: Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 2 | Rows:  Indicates the number of rows of text area box. |\n\n| --- | --- |\n\n2\n\nRows:  Indicates the number of rows of text area box.\n\n\n\n| 3 | Cols: Indicates the number of columns of text area box |\n\n| --- | --- |\n\n3\n\nCols: Indicates the number of columns of text area box\n\nCheckbox Control\n\nCheckboxes are used when more than one option is required to be selected. They are also created using HTML <input> tag but type attribute is set to\u00a0checkbox..\n\n\n### Example\n\n\nHere is an example HTML code for a form with two checkboxes \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Checkbox Control</title>\n\n</head>\n\n<body>\n\n<form>\n\n<input type=\"checkbox\"name=\"maths\"value=\"on\"> Maths\n\n<inputtype=\"checkbox\"name=\"physics\"value=\"on\"> Physics\n\n</form>\n\n</body>\n\n</html>\n\nAttributes\n\nFollowing is the list of attributes for <checkbox> tag.\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Type: Indicates the type of input control and for checkbox input control it will be set to\u00a0checkbox.. |\n\n| --- | --- |\n\n1\n\nType: Indicates the type of input control and for checkbox input control it will be set to\u00a0checkbox..\n\n\n\n| 2 | Name: Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n2\n\nName: Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 3 | Value: The value that will be used if the checkbox is selected. |\n\n| --- | --- |\n\n3\n\nValue: The value that will be used if the checkbox is selected.\n\n\n\n| 4 | Checked: Set to\u00a0checked\u00a0if you want to select it by default. |\n\n| --- | --- |\n\n4\n\nChecked: Set to\u00a0checked\u00a0if you want to select it by default.\n\nRadio Button Control\n\nRadio buttons are used when out of many options, just one option is required to be selected. They are also created using HTML <input> tag but type attribute is set to\u00a0radio.\n\n\n### Example\n\n\nHere is example HTML code for a form with two radio buttons \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Radio Box Control</title>\n\n</head>\n\n<body>\n\n<form>\n\n<inputtype=\"radio\"name=\"subject\"value=\"maths\"> Maths\n\n<inputtype=\"radio\"name=\"subject\"value=\"physics\"> Physics\n\n</form>\n\n</body>\n\n</html>\n\nAttributes\n\nFollowing is the list of attributes for radio button.\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Type: Indicates the type of input control and for checkbox input control it will be set to radio. |\n\n| --- | --- |\n\n1\n\nType: Indicates the type of input control and for checkbox input control it will be set to radio.\n\n\n\n| 2 | Name: Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n2\n\nName: Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 3 | Value: The value that will be used if the radio box is selected. |\n\n| --- | --- |\n\n3\n\nValue: The value that will be used if the radio box is selected.\n\n\n\n| 4 | Checked: Set to\u00a0checked\u00a0if you want to select it by default. |\n\n| --- | --- |\n\n4\n\nChecked: Set to\u00a0checked\u00a0if you want to select it by default.\n\nSelect Box Control\n\nA select box, also called drop down box which provides option to list down various options in the form of drop down list, from where a user can select one or more options.\n\n\n### Example\n\n\nHere is example HTML code for a form with one drop down box\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>Select Box Control</title>\n\n</head>\n\n<body>\n\n<form>\n\n<selectname=\"dropdown\">\n\n<optionvalue=\"Maths\"selected>Maths</option>\n\n<optionvalue=\"Physics\">Physics</option>\n\n</select>\n\n</form>\n\n</body>\n\n</html>\n\nAttributes\n\nFollowing is the list of important attributes of <select> tag \u2212\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Name: Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n1\n\nName: Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 2 | Size: This can be used to present a scrolling list box. |\n\n| --- | --- |\n\n2\n\nSize: This can be used to present a scrolling list box.\n\n\n\n| 3 | Multiple: If set to \"multiple\" then allows a user to select multiple items from the menu. |\n\n| --- | --- |\n\n3\n\nMultiple: If set to \"multiple\" then allows a user to select multiple items from the menu.\n\nFollowing is the list of important attributes of <option> tag \u2212\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Value: The value that will be used if an option in the select box box is selected. |\n\n| --- | --- |\n\n1\n\nValue: The value that will be used if an option in the select box box is selected.\n\n\n\n| 2 | Selected: Specifies that this option should be the initially selected value when the page loads. |\n\n| --- | --- |\n\n2\n\nSelected: Specifies that this option should be the initially selected value when the page loads.\n\n\n\n| 3 | Label: An alternative way of labeling options |\n\n| --- | --- |\n\n3\n\nLabel: An alternative way of labeling options\n\nFile Upload Box\n\nIf you want to allow a user to upload a file to your web site, you will need to use a file upload box, also known as a file select box. This is also created using the <input> element but type attribute is set to\u00a0file.\n\n\n### Example\n\n\nHere is example HTML code for a form with one file upload box \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>File Upload Box</title>\n\n</head>\n\n<body>\n\n<form>\n\n<inputtype=\"file\"name=\"fileupload\"accept=\"image/*\"/>\n\n</form>\n\n</body>\n\n</html>\n\nAttributes\n\nFollowing is the list of important attributes of file upload box \u2212\n\n\n\n| Sr.No | Attribute & Description |\n\n| --- | --- |\n\nSr.No\n\nAttribute & Description\n\n\n\n| 1 | Name: Used to give a name to the control which is sent to the server to be recognized and get the value. |\n\n| --- | --- |\n\n1\n\nName: Used to give a name to the control which is sent to the server to be recognized and get the value.\n\n\n\n| 2 | Accept: Specifies the types of files that the server accepts. |\n\n| --- | --- |\n\n2\n\nAccept: Specifies the types of files that the server accepts.\n\nButton Controls\n\nThere are various ways in HTML to create clickable buttons. You can also create a clickable button using <input>tag by setting its type attribute to\u00a0button. The type attribute can take the following values \u2212\n\n\n\n| Sr.No | Type & Description |\n\n| --- | --- |\n\nSr.No\n\nType & Description\n\n\n\n| 1 | submit This creates a button that automatically submits a form. |\n\n| --- | --- |\n\n1\n\nsubmit\n\nThis creates a button that automatically submits a form.\n\n\n\n| 2 | reset This creates a button that automatically resets form controls to their initial values. |\n\n| --- | --- |\n\n2\n\nreset\n\nThis creates a button that automatically resets form controls to their initial values.\n\n\n\n| 3 | button This creates a button that is used to trigger a client-side script when the user clicks that button. |\n\n| --- | --- |\n\n3\n\nbutton\n\nThis creates a button that is used to trigger a client-side script when the user clicks that button.\n\n\n\n| 4 | image This creates a clickable button but we can use an image as background of the button. |\n\n| --- | --- |\n\n4\n\nimage\n\nThis creates a clickable button but we can use an image as background of the button.\n\n\n### Example\n\n\nHere is example HTML code for a form with three types of buttons \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>File Upload Box</title>\n\n</head>\n\n<body>\n\n<form>\n\n<inputtype=\"submit\"name=\"submit\"value=\"Submit\"/>\n\n<inputtype=\"reset\"name=\"reset\"value=\"Reset\"/>\n\n<inputtype=\"button\"name=\"ok\"value=\"OK\"/>\n\n<inputtype=\"image\"name=\"imagebutton\"src=\"/html/images/logo.png\"/>\n\n</form>\n\n</body>\n\n</html>\n\nHidden Form Controls\n\nHidden form controls are used to hide data inside the page which later on can be pushed to the server. This control hides inside the code and does not appear on the actual page. For example, following hidden form is being used to keep current page number. When a user will click next page then the value of hidden control will be sent to the web server and there it will decide which page will be displayed next based on the passed current page.\n\n\n### Example\n\n\nHere is example HTML code to show the usage of hidden control \u2212\n\n<!DOCTYPE html>\n\n<html>\n\n<head>\n\n<title>File Upload Box</title>\n\n</head>\n\n<body>\n\n<form>\n\n<p>This is page 10</p>\n\n<inputtype=\"hidden\"name=\"pagename\"value=\"10\"/>\n\n<inputtype=\"submit\"name=\"submit\"value=\"Submit\"/>\n\n<inputtype=\"reset\"name=\"reset\"value=\"Reset\"/>\n\n</form>\n\n</body>\n\n</html>\n\n\n## Lab Task\n\n\nCreate a webportal for a company providing some consultancy services in education.\n\nIt includes many pages, having text, tables, images and an order form.\n\nDated: __________",
        "quizzes": [
            {
                        "question": "Which target attribute value forces a hyperlink to open inside a brand new browser tab or window?",
                        "options": [
                                    "_blank",
                                    "_self",
                                    "_parent",
                                    "_top"
                        ],
                        "correctAnswer": "_blank",
                        "explanation": "Setting target='_blank' instructs the browser to open the linked target document in a new tab or window."
            },
            {
                        "question": "What is the key difference between cellpadding and cellspacing in HTML tables?",
                        "options": [
                                    "Cellpadding controls distance inside the cell border, while cellspacing controls distance between adjacent cells",
                                    "Cellpadding adds borders, while cellspacing colors text",
                                    "Cellpadding is for rows, while cellspacing is for columns",
                                    "They are identical synonyms in HTML5"
                        ],
                        "correctAnswer": "Cellpadding controls distance inside the cell border, while cellspacing controls distance between adjacent cells",
                        "explanation": "Cellpadding adjusts whitespace between the cell boundary and its internal content; cellspacing sets the gap between neighboring cells."
            },
            {
                        "question": "Which form enctype must be specified when submitting binary file uploads via <input type='file'>?",
                        "options": [
                                    "multipart/form-data",
                                    "application/x-www-form-urlencoded",
                                    "text/plain",
                                    "binary/octet-stream"
                        ],
                        "correctAnswer": "multipart/form-data",
                        "explanation": "When uploading files through HTML forms, enctype='multipart/form-data' is required so data is partitioned into mime parts without character encoding distortion."
            }
],
        "flashcards": [
            {
                        "question": "What is the structural difference between <div> and <span>?",
                        "answer": "<div> is a block-level container creating section divisions, whereas <span> is an inline container styling text snippets within sentences."
            },
            {
                        "question": "What is an HTML empty tag?",
                        "answer": "A tag that carries only attributes and has no closing tag (e.g., <img>, <br>, <hr>, <input>)."
            },
            {
                        "question": "What are the allowed type values for an ordered list (<ol>)?",
                        "answer": "'1' (default digits), 'I' (uppercase Roman), 'i' (lowercase Roman), 'A' (uppercase letters), and 'a' (lowercase letters)."
            },
            {
                        "question": "Why are hidden form controls (<input type='hidden'>) used?",
                        "answer": "They pass persistent application data (e.g. user session IDs, page numbers) to the server without displaying anything on the screen."
            }
]
    },
    {
        "order": 11,
        "title": "Lab 11: Introduction to MATLAB  -  Workspace, Vector Operations, M-Files & Debugging",
        "codeSnippet": "% MATLAB Numerical Computation & Matrix Algebra\nclc;\nclear;\n\n% Calculator calculations\nx = 1 + 2 * 3; % x = 7\nans_mult = 4 * x; % ans = 28\n\n% Vectors\nv = [1 4 7 10 13]; % Row vector\nw = [1; 4; 7; 10; 13]; % Column vector\n\n% 3x3 System of Linear Equations\n% 1x + 2y + 3z = 1\n% 4x + 5y + 6z = 1\n% 7x + 8y + 0z = 1\nA = [1 2 3; 4 5 6; 7 8 0];\nB = [1; 1; 1];\n\n% Determinant and Matrix Inversion\ndet_A = det(A);\nc = inv(A);\nX = c * B;\n\ndisp('Determinant:');\ndisp(det_A);\ndisp('Solution Vector X:');\ndisp(X);",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB#11\n\nINTRODUCTION TO MATLAB\n\n\n## Introduction:\n\n\nThe name MATLAB stands for MATrix LABoratory. MATLAB was written originally to provide easy access to matrix software developed by the LINPACK (linear system package) and EISPACK (Eigen system package) projects.\n\nMATLAB is a high-performance language for technical computing. It integrates computation, visualization, and programming environment.  Furthermore, MATLAB is a modern programming language environment:  it has sophisticated data structures, contains built-in editing and debugging tools, and supports object-oriented programming. These factors make MATLAB an excellent tool for teaching and research.\n\nMATLAB has many advantages compared to conventional computer languages (e.g., C, FORTRAN) for solving technical problems.  MATLAB is an interactive system whose basic data element is an array that does not require dimensioning.  The software package has been commercially available since 1984 and is now considered as a standard tool at most universities and industries worldwide.\n\nBasic features:\n\nA minimum MATLAB session:\n\nThe goal of this minimum session (also called starting and exiting sessions) is to learn the first steps:\n\n\u2022 How to log on\n\n\u2022 Invoke MATLAB\n\n\u2022 Do a few simple calculations\n\n\u2022 How to quit MATLAB\n\nStarting MATLAB:\n\nyou can enter MATLAB by double-clicking on the MATLAB shortcut icon on your Windows desktop.  When you start MATLAB, a special window called the MATLAB desktop appears. The desktop is a window that contains other windows. The major tools within or accessible from the desktop are:\n\n\u2022 The Command Window\n\n\u2022 The Command History\n\n\u2022 The Workspace\n\n\u2022 The Current Directory\n\n\u2022 The Help Browser\n\n\u2022 The Start button\n\n\n\n\n![Diagram](assets/images/university/itc/lab10_matlab_desktop.png)\n\n\nFigure : The graphical interface to the MATLAB workspace\n\nWhen MATLAB is started for the first time, the screen looks like the one that shown in the Figure. This illustration also shows the default configuration of the MATLAB desktop. You can customize the arrangement of tools and documents to suit your needs.\n\nYou are now faced with the MATLAB desktop on your computer, which contains the prompt (>>) in the Command Window. Usually, there are 2 types of prompt:\n\n>>for  full  version\n\nEDU>for  educational  version\n\nNote:  To simplify the notation, we will use this prompt, >>, as a standard prompt sign, though our MATLAB  version is for educational purpose.\n\nUsing MATLAB as a calculator:\n\nAs an example of a simple interactive calculation, just type the expression you want to evaluate. Let\u2019s start at the very beginning. For example, let\u2019s suppose you want to calculate the expression, 1 + 2 \u00d7 3. You type it at the prompt command (>>) as follows,\n\n>>  1+2*3 ans  =7\n\nYou will have noticed that if you do not specify an output variable, MATLAB uses a default variable ans, short for answer, to store the results of the current calculation.  Note that the variable ans is created (or overwritten, if it is already existed). To avoid this, you may assign a value to a variable or output argument name. For example,\n\n>>  x  =  1+2*3\n\nx=7\n\nwill result in x being given the value 1 + 2 \u00d7 3 = 7.  This variable name can always be used to refer to the results of the previous computations.  Therefore, computing 4x will result in\n\n>>  4*x\n\nAns=28.0000\n\n\n\n\n![Diagram](assets/images/university/itc/lab10_matlab_command_output.png)\n\n\nCreating MATLAB variables:\n\nMATLAB variables are created with an assignment statement.  The syntax of variable assignment is\n\nvariable  name  =  a  value  (or  an  expression)\n\nFor example,\n\n>>  x  =  expression\n\nwhere expression is a combination of numerical values, mathematical operators, variables, and function calls. On other words, expression can involve:\n\n\u2022 manual entry\n\n\u2022 built-in functions\n\n\u2022 user-defined functions\n\nOverwriting variable:\n\nOnce a variable has been created, it can be reassigned.  In addition, if you do not wish to see the intermediate results, you can suppress the numerical output by putting a semicolon\n\n(;) at the end of the line. Then the sequence of commands looks like this:\n\n>>  t  =  5; >>  t  =  t+1\n\nt = 6\n\nError messages:\n\nIf we enter an expression incorrectly, MATLAB will return an error message. For example, in the following, we left out the multiplication sign, *, in the following expression\n\n>>  x  =  10; >>  5x\n\n???  5x |\n\nError:  Unexpected  MATLAB  expression.\n\nControlling the hierarchy of operations or precedence:\n\nLet\u2019s consider the previous arithmetic operation, but now we will include parentheses.  For example, 1 + 2 \u00d7 3 will become (1 + 2) \u00d7 3\n\n>>  (1+2)*3\n\nAns=9\n\nand, from previous example\n\n>>  1+2*3\n\nAns=7\n\nBy adding parentheses, these two expressions give different results:  9 and 7.\n\nEntering multiple statements per line:\n\nIt is possible to enter multiple statements per line.  Use commas (,) or semicolons (;) to enter more than one statement at once.  Commas  (,) allow multiple statements per line without suppressing output.\n\n>>  a=7;  b=cos(a),  c=cosh(a)\n\nb=0.6570\n\nc =48.3170\n\nMiscellaneous commands:\n\nHere are few additional useful commands:\n\n\u2022 To clear the Command Window, type clc\n\n\u2022 To abort a MATLAB computation, type ctrl-c\n\n\u2022 To continue a line, type . . .\n\nMatrix generation:\n\nMatrices are fundamental to MATLAB. Therefore, we need to become familiar with matrix generation and manipulation. Matrices can be generated in several ways.\n\nEntering a vector:\n\nA vector is a special case of a matrix. The purpose of this section is to show how to create vectors and matrices in MATLAB. As discussed earlier, an array of dimension 1 \u00d7 n is called a row vector, whereas an array of dimension m \u00d7 1 is called a column vector. The elements of vectors in MATLAB are enclosed by square brackets and are separated by spaces or by commas. For example, to enter a row vector, v, type\n\n>>  v  =  [1  4  7  10  13]\n\nv=1471013\n\nColumn vectors are created in a similar way,  however,  semicolon  (;)  must separate the components of a column vector,\n\n>>  w  =  [1;4;7;10;13]\n\nw=\n\n1 4 7\n\n10 13\n\n>>  A  =  [1  2  3;  4  5  6;  7  8  9]\n\nMATLAB then displays the 3 \u00d7 3 matrix as follows,\n\nA=\n\n123\n\n456\n\n789\n\n\n## M-File Scripts:\n\n\nA script file is an external file that contains a sequence of MATLAB statements. Script files have a filename Extension .m and are often called M-files. M-Files can be scripts that simply execute a series of MATLAB statements, or they can be functions that can accept arguments and can produce one or more outputs.\n\n\n### Examples\n\n\nHere are two simple scripts.\n\n\n### Example 1\n\n\nConsider the system of equations:\n\nx + 2y + 3z  = 1\n\n3x + 3y + 4z =  1\n\n2x + 3y + 3z =  2\n\n\n## Debugging M-files:\n\n\n\n## Introduction:\n\n\nThis section introduces general techniques for finding errors in M-files.  Debugging  is the process by which you isolate and fix errors in your program or code.\n\nDebugging helps to correct two kind of errors:\n\n\u2022 Syntax errors - For example omitting a parenthesis or misspelling a function name.\n\n\u2022 Run-time errors - Run-time errors are usually apparent and difficult to track down. They produce unexpected results.\n\nDebugging process:\n\nWe can debug the M-files using the Editor/Debugger as well as using debugging functions from the Command Window. The debugging process consists of\n\n\u2022 Preparing for debugging\n\n\u2022 Setting breakpoints\n\n\u2022 Running an M-file with breakpoints\n\n\u2022 Stepping through an M-file\n\n\u2022 Examining values\n\n\u2022 Correcting problems\n\n\u2022 Ending debugging\n\nPreparing for debugging:\n\nHere we use the Editor/Debugger for debugging. Do the following to prepare for debugging:\n\n\u2022 Open the file\n\n\u2022 Save changes\n\n\u2022 Be sure the file you run and any files it calls are in the directories that are on the search path.\n\nSetting breakpoints:\n\nSet breakpoints to pause execution of the function, so we can examine where the problem might be.\n\nThere are three basic types of breakpoints:\n\n\u2022 A standard breakpoint, which stops at a specified line.\n\n\u2022 A conditional breakpoint, which stops at a specified line and under specified conditions.\n\n\u2022 An error breakpoint that stops when it produces the specified type of warning, error, NaN, or infinite value.\n\nYou cannot set breakpoints while MATLAB is busy, for example, running an M-file.\n\nRunning with breakpoints:\n\nAfter setting breakpoints, run the M-file from the Editor/Debugger or from the Command Window. Running the M-file results in the following:\n\n\u2022 The prompt in the Command Window changes to\n\nK>>\n\nindicating that MATLAB is in debug mode.\n\n\u2022 The program pauses at the first  breakpoint.  This means that line will be executed when you continue. The pause is indicated by the green arrow.\n\n\u2022 In breakpoint, we can examine variable, step through programs, and run other calling functions.\n\nExamining values:\n\nWhile  the  program  is  paused,  we  can  view  the  value  of  any  variable  currently  in  the workspace.   Examine values when we want to see whether a line of code has produced the expected result or not.  If the result is as expected, step to the next line, and continue running.  If the result is not as expected, then that line, or the previous line, contains an error. When we run a program, the current workspace is shown in the Stack field. Use who or whos to list the variables in the current workspace.\n\nViewing values as datatips:\n\nFirst, we position the cursor to the left of a variable on that line. Its current value appears. This is called a datatip, which is like a tooltip for data.  If you have trouble getting the datatip to appear, click in the line and then move the cursor next to the variable.\n\nCorrecting and ending debugging:\n\nWhile debugging, we can change the value of a variable to see if the new  value produces expected results. While the program is paused, assign a new value to the variable in the Command Window, Workspace browser, or Array Editor.  Then continue running and stepping through the program.\n\nEnding debugging:\n\nAfter identifying a problem, end the debugging session. It is best to quit debug mode before editing an M-file. Otherwise, you can get unexpected results when you run the file. To end debugging, select Exit Debug Mode from the Debug menu.\n\n\n## Lab Task\n\n\nTo calculate the value of the expression  y = e-a sin(x) + 10y1/2 , for a = 5, x = 2 and y = 8.\n\nConsider the following system of linear equations\n\n1x + 2y +3z  = 1\n\n4x + 5y + 6z = 1\n\n7x + 8y         = 1\n\nFind out the following and add output.\n\ndet(A)\n\nc=inv(A)=A-1\n\nX = c * B",
        "quizzes": [
            {
                        "question": "What is the historical origin of the name MATLAB?",
                        "options": [
                                    "MATrix LABoratory",
                                    "Mathematical Tables Library",
                                    "Matrix Algorithm Batch",
                                    "Modern Applied Technology Lab"
                        ],
                        "correctAnswer": "MATrix LABoratory",
                        "explanation": "MATLAB stands for MATrix LABoratory, originally built to provide access to LINPACK and EISPACK matrix libraries."
            },
            {
                        "question": "What is the effect of placing a semicolon (;) at the end of a MATLAB command?",
                        "options": [
                                    "It suppresses the screen display of the computed result",
                                    "It terminates and exits the MATLAB program",
                                    "It comments out the preceding code",
                                    "It converts the output into a floating-point number"
                        ],
                        "correctAnswer": "It suppresses the screen display of the computed result",
                        "explanation": "In MATLAB, terminating a statement with a semicolon executes the command while suppressing console printout."
            },
            {
                        "question": "How does the MATLAB prompt change when entering debug mode at an active breakpoint?",
                        "options": [
                                    "K>>",
                                    "DEBUG>>",
                                    "??>>",
                                    "STOP>>"
                        ],
                        "correctAnswer": "K>>",
                        "explanation": "When MATLAB halts execution at a breakpoint, the Command Window prompt changes from >> to K>> to indicate debug mode."
            }
],
        "flashcards": [
            {
                        "question": "What default variable does MATLAB assign when a calculation output is not named?",
                        "answer": "ans (short for answer)."
            },
            {
                        "question": "How are row vectors distinguished from column vectors in MATLAB syntax?",
                        "answer": "Row vector elements are separated by spaces or commas ([1 2 3]), while column vector elements are separated by semicolons ([1; 2; 3])."
            },
            {
                        "question": "What is the difference between MATLAB commands clc and clear?",
                        "answer": "clc clears the Command Window screen, whereas clear deletes all variables from the memory workspace."
            },
            {
                        "question": "What are the three types of breakpoints in MATLAB?",
                        "answer": "Standard breakpoints, conditional breakpoints, and error breakpoints."
            }
]
    },
    {
        "order": 12,
        "title": "Lab 12: Programming in C++  -  C-Free IDE, Program Anatomy & Console Output",
        "codeSnippet": "#include <iostream.h>\n\nint main(void)\n{\n    // String printing with insertion operator\n    cout << \"Welcome\" << \" To \" << \"Hamdard University\" << endl;\n\n    // Numerical expressions\n    cout << \"Sqr(5) = \" << 5 * 5 << endl\n         << \" and sum of 19 + 10 is: \"\n         << 19 + 10 << endl;\n\n    return 0;\n}",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 12\n\nProgramming in C++ (IDE and Basic Program Structure)\n\n\n## Objective\n\n\nTo Study the features of Integrated Development Environment (IDE) for C++ language and study the basic building blocks and structures of C++ program\n\n\n## Theory\n\n\nIDE Basics:\n\nC++ language features an Integrated Development Environment (IDE) as the programmer\u2019s platform. It is a screen with windows and pulls down Menus. Code of the program, error messages and other information are displayed in separate windows. Programmer uses menu selections or key combination to revoke all the operations necessary for the program development. Debugging capabilities are also built-in the IDE.\n\nGeneral Overview:\n\n\n\n\n![Diagram](assets/images/university/itc/lab12_cfree_launch.png)\n\n\nRun \u2013 Compiles, links and runs the program\n\nEdit Window \u2013 space for writing the program\n\nFunctions \u2013 Functions used in the program\n\nTabs \u2013 Different tabs for different programs\n\nNew \u2013 Opens a new edit window\n\nOpen \u2013 Opens a previously saved program\n\nLine with the error\n\nSave \u2013 Saves the program\n\nBuild Status \u2013 Show the status of build process\n\nError \u2013 Describes the error along with the line number\n\nInvoking the IDE\n\nTo enter the IDE, double click on the C-Free icon at the desktop or select from the start menu. This will make you enter into the IDE interface. Click on the new icon or select it from the File Menu which will look like the figure given below. Start writing your program where cursor is currently placed. Press F5 to compile and run your program.\n\n\n\n\n![Diagram](assets/images/university/itc/lab12_cfree_ide.png)\n\n\nIf your source file does not have any error then an output window will pop up and display the result.\n\n\n\n\n![Diagram](assets/images/university/itc/lab12_cfree_editor_window.png)\n\n\nUsing Menus\n\nIf the menu bar is inactive, you can invoke by pressing the ALT function key. To select different menu, move the highlight left or right with cursor (arrow) keys. You can also revoke the selection by pressing the key combination for the specific menu.\n\nOpening New Window\n\nTo type in program you will need to open an Edit window. For this, open file menu and click \u2018new\u2019. A window will appear within the C-Free screen with line numbers on the left. If the code is too long you can see the code by scrolling the window.\n\n\n\n\n![Diagram](assets/images/university/itc/lab12_cfree_output_window.png)\n\n\nWriting a Window\n\nFor writing program the Edit window will be active. Type the program code with the proper syntax and command. Characters will appear where the cursor is positioned. Press [Enter] to move to the next line. Use the cursor keys to move to any position on the screen. You can delete characters by using [Del] key. You can delete the entire line by selecting the line and pressing the [Del] key or by pressing CTRL+Y key combination.\n\nSaving a Program\n\nAfter typing the program code, you should save it to the disk. To perform this operation, select Save from the File menu. Pressing the [CTRL+S] combination can also complete this operation. Save the file and provide an appropriate and unique name to the file. Make sure you add the \u201c.cpp\u201d extension to your filename. You can save the code after compiling the program but saving it before is more appropriate.\n\nExecuting a Program\n\nIf the program is compiled and linked without errors, the program is executed by selecting Run from the Build menu or by pressing the [F5] key.\n\nCorrecting Error\n\nIf the compiler, recognize some error, it will let you know through the Build window, which is at the bottom of the program window. The error will be listed and the line containing the error will be highlighted.\n\nNow you have to see your Edit window and remove the error by appropriate actions. These errors are due to different reasons. For example; wrong termination, wrong syntax, etc.\n\nExiting IDE\n\nBefore exiting IDE, programmer must save the necessary source file. If the file is not closed and you try to exit the IDE, it will ask whether you wish to save the program or exit anyway.\n\nAn Edit window can be closed by different ways. You can click on the small cross in the upper right corner, you can select Close from the Window menu, you can right click on the tab of the program and click \u2018close\u2019 or you can press the [Alt] [X] key combination.\n\nYou can close the C-Free IDE by selecting EXIT from the File menu or by pressing the keys [Alt] [F4].\n\n\n## Structure of C++ program\n\n\nIn order to a write program in any programming language, it is necessary to know about its command and syntax. Programmers must also know the basic usage of commands and other programming structures. Programs written in C++ language are really not much difficult to understand than one written in any other language, once you become familiar with the basic syntax.\n\n\n## Function Definition:\n\n\nAll C++ programs are divided into units called \u2018functions\u2019. Every C++ program consists of one or more functions. Consider the following program:\n\n#include <iostream.h>\n\nmain ()\n\n{\n\ncout << \u201cThis is a program\u201d << endl;\n\n}\n\nThe above program has a function named \u201cmain\u201d. This function is one to which control is passed from the Operating System when the program is invoked, i.e. it is the first function which will be executed. The word \u201cvoid\u201d preceding \u201cmain\u201d specifies that the function \u201cmain\u201d will not return a value. The second \u201cvoid\u201d in parentheses specifies that the function takes no arguments.\n\n\n## Delimiters:\n\n\nThe braces after the function definition signal the beginning and the end of the body of the function. The opening brace { indicates the start of a block of code whereas the closing brace } indicates the end of block or it terminates the block of code.\n\nBraces are also used to delimit blocks of code in situations other than functions. They are used in loops and decision-making statements within a program.\n\n\n## Statement Terminator:\n\n\nStatement in C++ language are terminated with a semicolon \u201c;\u201d. Semicolon terminates the line not the carriage return you type afterwards. C++ language pays no attention to carriage return in your program listing. The compiler pays no attention to any of the so called \u201cwhite space\u201d characters: the carriage return, the space and the tab.\n\nProgrammers can place as many of few white space characters in a program; they will be invisible and will be ignored by the compiler.\n\n\n## Program Indentation:\n\n\nAs you can place as many white space characters in the program, therefore, they can be used to make the program easier to read. Consider the previous program, which can also be written as follows without proper indentation.\n\nvoid main (void) { cout << \u201cThis is a program\u201d << endl; }\n\nThe compiler would not know the difference; however, stretching the code out vertically makes for a more comprehensive program, and aligning and matching braces makes it easier to ensure that each opening brace has a closing brace.\n\nIndentation of block of code enclosed in braces is an important aspect of making C++ program readable. Indentation the line of code is not critical in small programs but when there are many sets of nested braces in a program, indentation becomes increasingly important.\n\n\n## The cout Statement:\n\n\nConsider the program line:\n\ncout<< \u201cThis is a program\u201d << endl;\n\nThe cout statement causes the phrase in quotes to be printed on screen. The cout statement is always followed by insertion operator << i.e. every element in the cout statement must be separated with << operator as it is used to separate the quoted phrase and manipulation operator \u201cendl\u201d. As C++ language distinguishes between uppercase and lowercase characters, thus the statements \u2018COUT\u2019 and \u2018cout\u2019 are not the same.\n\ncout statement is an output statement and has the following Syntax.\n\nSYNTAX\n\ncout<< e1; / << e1<< e2<< e3 \u2026 << en;\n\nHere e stands for an element. As syntax indicates, cout can take either one element or multiple elements separated by << operators. Don\u2019t forget ; (semicolon) at the end of cout statement as it terminates the statement.\n\n\n## Printing strings:\n\n\nAny symbol or sequence of characters and symbols enclosed within double quotation is treated as strings in C++. Consider the following program:\n\n#include <iostream.h>\n\nmain ()\n\n{\n\ncout<< \u201cWelcome\u201d\n\n<< \u201c To \u201c\n\n<< \u201cHamdard University\u201d;\n\n}\n\nCompile and run the aforementioned program and note down the output.\n\n\n## Printing numbers:\n\n\ncout behaves differently when it encounters numerical expressions instead of strings. Recall that anything enclosed within double quotation is printed as it is on the output screen. Numerical expressions on the other hand are substituted with the result of expression and resulting answer is than printed on the output screen. Consider the following program:\n\n#include <iostream.h>\n\nint main (void)\n\n{\n\ncout<< \u201cSqr(5) = \u201c << 5*5 << endl\n\n<< \u201c and sum of 19 + 10 is: \u201c\n\n<< 19+10 << endl;  }\n\nCompile and run the above mentioned program and note down the output.\n\n\n## Lab Task\n\n\nWrite a program which prints your bio data\n\nWrite a program that prints the table of 8\n\nSample Output\n\n8 x 1 = 8\n\n8 x 2 = 16\n\n8 x 3 = 24\n\n8 x 4 = 32\n\n8 x 5 = 40\n\n8 x 6 = 48\n\n8 x 7 = 56\n\n8 x 8 = 64\n\n8 x 9 = 72\n\n8 x 10 = 80\n\nWrite a program which prints the following shape on the display screen.\n\n*\n\n**\n\n***\n\n****\n\nWrite a program which prints the GPA of your five courses\n\nSample Output\n\n\n\n| Courses | GPA |\n\n| --- | --- |\n\nCourses\n\nGPA\n\n\n\n| Calculus: | 3.5 |\n\n| --- | --- |\n\nCalculus:\n\n3.5\n\n\n\n| Physics: | 2.5 |\n\n| --- | --- |\n\nPhysics:\n\n2.5\n\n\n\n| Basic Electronics: | 2.0 |\n\n| --- | --- |\n\nBasic Electronics:\n\n2.0\n\n\n\n| Introduction to Computing | 3.9 |\n\n| --- | --- |\n\nIntroduction to Computing\n\n3.9\n\n\n\n| Islamic Studies | 3.0 |\n\n| --- | --- |\n\nIslamic Studies\n\n3.0",
        "quizzes": [
            {
                        "question": "Which function serves as the mandatory entry point where C++ program execution begins?",
                        "options": [
                                    "main()",
                                    "start()",
                                    "init()",
                                    "cout()"
                        ],
                        "correctAnswer": "main()",
                        "explanation": "In standard C++, the operating system transfers control to the main() function upon execution."
            },
            {
                        "question": "What keyboard shortcut compiles and runs a C++ program in the C-Free IDE?",
                        "options": [
                                    "F5",
                                    "F9",
                                    "Ctrl+R",
                                    "Alt+X"
                        ],
                        "correctAnswer": "F5",
                        "explanation": "In C-Free IDE, pressing the F5 function key triggers compilation, linking, and execution."
            },
            {
                        "question": "What is the role of the << operator when used with cout in C++?",
                        "options": [
                                    "Insertion operator (streams data into standard output)",
                                    "Extraction operator (takes input from keyboard)",
                                    "Bitwise left-shift comparison",
                                    "Statement terminator"
                        ],
                        "correctAnswer": "Insertion operator (streams data into standard output)",
                        "explanation": "The << operator is the insertion (stream output) operator that sends data operands into the cout output stream."
            }
],
        "flashcards": [
            {
                        "question": "What character is used as the mandatory statement terminator in C++?",
                        "answer": "The semicolon (;)."
            },
            {
                        "question": "What is the purpose of the endl manipulator in a cout statement?",
                        "answer": "It inserts a newline character and flushes the console output stream."
            },
            {
                        "question": "What shortcut key combination deletes an entire line of code in the C-Free editor?",
                        "answer": "CTRL + Y."
            },
            {
                        "question": "What file extension must be given to C++ source code files?",
                        "answer": ".cpp"
            }
]
    },
    {
        "order": 13,
        "title": "Lab 13: Programming in C++  -  Variables, Data Types, cin Input & Decision Control",
        "codeSnippet": "#include <iostream.h>\n\nint main(void)\n{\n    int age;\n    cout << \"Enter your age: \";\n    cin >> age;\n\n    if (age <= 0)\n    {\n        cout << \"Invalid age\" << endl;\n    }\n    else\n    {\n        cout << \"Age in days: \" << age * 365 << endl;\n        cout << \"Welcome to Hamdard University\" << endl;\n    }\n\n    return 0;\n}",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 13\n\nVariables, Data Types and I/O Functions\n\n\n## Objective\n\n\nLearn to write programs declaring different variables and data types\n\nTo learn statements for providing input and displaying output\n\n\n## Theory\n\n\n\n## Variable:\n\n\nA variable is a named memory location that can hold various values. All variables must be declared before they can be used. A variable\u2019s declaration serves one important purpose that it tells the C compiler what type of variable is being used. Variable declaration means that you are giving an identity to the variable, which is to be used in the program.\n\n\n## Basic Data Types of C language:\n\n\nC support four basic data type described below:\n\n\n### Table 1: Data type Description\n\n\n\n\n| Character | Character data | Char |\n\n| --- | --- | --- |\n\nCharacter\n\nCharacter data\n\nChar\n\n\n\n| Integer | Signed whole  number | Int |\n\n| --- | --- | --- |\n\nInteger\n\nSigned whole  number\n\nInt\n\n\n\n| Float | Floating point number | Float |\n\n| --- | --- | --- |\n\nFloat\n\nFloating point number\n\nFloat\n\n\n\n| Void | Valueless | Void |\n\n| --- | --- | --- |\n\nVoid\n\nValueless\n\nVoid\n\nData Type Description:\n\nCharacter:\n\nIt is one bit long and it is most commonly used to hold a single character. A variable of type char can also be used as a \u201clittle integer\u201d if desired. A character constant is either a single alphabet, a single digit, or a single special symbol enclosed within single inverted commas. For example \u2018A\u2018, \u20180\u2018, or \u2018&\u2018. It requires 1 byte in the memory for storage.\n\nInteger:\n\nInteger may hold signed whole number (Number with no fractional part). It may hold values in the range \u201332768 to 32767.\n\nFloat:\n\nData type float hold signed floating-point values, which may have fractional components. Float can hold very large values.\n\n\n## Variable Declaration:\n\n\nVariable are generally declared as:\n\nType var-name;\n\nHere  \u2018Type\u2019 is C data type (e.g char, int, float etc )and \u2018var-name\u2019 is the name of the variable. You can also declare more than one variable of same type by using a comma-separated list. For example\n\nint a,b,c ;\n\n\n## Value Assignment to the Variable\n\n\nA programmer can assign a unique value to the variable. The general form of an assignment statement is\n\nVariable name = value;\n\nFor example;\n\nX = 1000;\n\n\n### Example Programs\n\n\n\n### Program 1:\n\n\nThis program declares a variable and assigns it a value.\n\n#include<iostream.h>\n\nint main (void)\n\n{\n\nint number;\n\nnumber = 1000;\n\ncout<<\"The value is \"<< number<<endl;\n\n}\n\nOutput\n\nThe result of the above program will be:\n\nThe value is 1000\n\n\n### Program 2:\n\n\nThis program declares different type of variables and prints their assigned values.\n\n#include<iostream.h>\n\nint main  (void)\n\n{\n\nint event = 5;\n\nchar heat = 'c';\n\nfloat time = 27.25;\n\ncout<<\"The winning time in heat \"<< heat <<\" of event was \"\n\n<< event << \" is \"<< time<<endl;\n\n}\n\nOutput\n\nThe result of the program will be:\n\nThe winning time in heat c of event 5 is 27.25.\n\nVariable Declaration and Definition:\n\nVariables are used to hold values in memory. All variable must be defined before their usage. C++ provides list of primitive data types including int, float, char, double and bool. Variable definition has the following syntax.\n\nSyntax\n\nType var1; / var1, var2, var3, \u2026, var4;\n\n\n### Example\n\n\nint age;\n\nfloat gpa, per, pi;\n\n\n## Input Statement:\n\n\nThe cin statement allows the user to enter data from the keyboard. The cin statement allows the user to enter a number or a single character. The cin statement consists of the keyword cin followed by the extraction operator (>>) followed by a variableName where the input is to be stored then ended by a semicolon (;). It has the following syntax.\n\nSyntax\n\ncin>> VariableName;\n\nConsider the following program which prompts a user for the age and then returns his/her age in days.\n\n#include <iostream.h> //default compiler selected\n\nint main (void)\n\n{\n\nint age;\n\ncout<< \u201cEnter your age: \u201c;\n\ncin>> age; //age variable created earlier\n\ncout<< \u201cAge in days: \u201c << age*365 << endl;\n\n}\n\nCompile and run the program and note down the output.\n\nIn C++, decisions to execute or not execute a statement or group of statements can be made by using the statement if (expression). The expression must be an expression that can be evaluated as either true or false. If it evaluates to true, a succeeding statement or group of statements enclosed in { . . . }, called a block statement will be executed.\n\nSyntax\n\nif ( expression )\n\nstatement;/ block\n\nNOTE: block will be of statements, instructions or may have other if statements.\n\nCompile and run the following program and note down the output.\n\n#include <iostream.h>\n\nint main (void)\n\n{\n\nint age;\n\ncout << \u201cEnter your age: \u201c;\n\ncin >> age;\n\nif (age <= 0)\n\ncout << \u201cInvalid age\u201d << endl;\n\n}\n\n\n## Control Structures\n\n\nThe \u2018if-else\u2019 statement:\n\nIndentation and format:\n\nThe general form of the \u2018if-else\u2019 construct is as follows:\n\nif (expression )\n\nstatement;/block\n\nelse\n\nstatement;/block\n\nFor clarity and making a program easy to understand, each \u2018else\u2019 should be indented the same amount as its matching \u2018if\u2019.\n\nCompile and run the following program and note down the output.\n\n#include <iostream.h>\n\nint main (void)\n\n{\n\nint age;\n\ncout << \u201cEnter your age: \u201c;\n\ncin >> age;\n\nif (age <= 0)\n\ncout << \u201cInvalid age\u201d << endl;\n\nelse\n\ncout << \u201cWelcome to Hamdard University\u201d << endl;\n\n}\n\n\n## Lab Task\n\n\nWrite a program that inputs, three numbers and find the greatest numbers among these numbers.\n\nSample Output\n\nEnter First Number: 2\n\nEnter Second Number: 3\n\nEnter Third Number: 5\n\nThe greatest number is 5\n\nWrite a program that swaps the value of two variables using a third variable\n\nSample Output\n\nVariable1: 5\n\nVariable2: 9\n\nAfter swapping\n\nVariable1: 9\n\nVariable2: 5\n\nWrite a program that checks whether the entered year is a leap year or not\n\nWrite a program that checks whether the entered number is positive or negative",
        "quizzes": [
            {
                        "question": "What is the extraction operator symbol used with the cin input statement in C++?",
                        "options": [
                                    ">> (extraction operator)",
                                    "<< (insertion operator)",
                                    "== (relational equals)",
                                    "-> (member pointer)"
                        ],
                        "correctAnswer": ">> (extraction operator)",
                        "explanation": "In C++, the stream extraction operator >> reads input from standard input (cin) and stores it into a variable."
            },
            {
                        "question": "How much memory does a standard char primitive variable occupy in C++?",
                        "options": [
                                    "1 byte",
                                    "2 bytes",
                                    "4 bytes",
                                    "8 bytes"
                        ],
                        "correctAnswer": "1 byte",
                        "explanation": "A char variable in C++ stores a single character and requires exactly 1 byte (8 bits) of memory."
            },
            {
                        "question": "What happens if the condition in an if statement evaluates to false, and no else branch exists?",
                        "options": [
                                    "Execution bypasses the if block and proceeds to the next line",
                                    "The program crashes with a segmentation fault",
                                    "The compiler generates a syntax error",
                                    "The program resets back to main()"
                        ],
                        "correctAnswer": "Execution bypasses the if block and proceeds to the next line",
                        "explanation": "If an if statement evaluates to false and there is no else clause, the enclosed block is skipped entirely and program control advances."
            }
],
        "flashcards": [
            {
                        "question": "What is a variable in computer programming?",
                        "answer": "A named location in memory used to store and manipulate data values during program execution."
            },
            {
                        "question": "What numeric range can a signed 16-bit integer hold?",
                        "answer": "-32,768 to 32,767."
            },
            {
                        "question": "How are character literals enclosed in C++?",
                        "answer": "Character constants are enclosed within single quotation marks (e.g., 'A', 'c')."
            },
            {
                        "question": "What logic determines whether an if or an else block executes?",
                        "answer": "The condition expression: if true, the if-block executes; if false, the else-block executes."
            }
]
    },
    {
        "order": 14,
        "title": "Lab 14: Programming in C++  -  Arithmetic, Relational & Logical Operators",
        "codeSnippet": "#include <iostream.h>\n\nint main()\n{\n    int a = 13, b = 6;\n    cout << \"The Modulus of a,b is :: \" << a % b << endl;\n    cout << \"The Sum of a,b is :: \" << a + b << endl;\n\n    // Unary increment\n    int c = a++;\n    cout << \"Value of a++ is: \" << c << endl;\n    cout << \"Value of a is: \" << a << endl;\n\n    // Relational and Logical Operators\n    if (a > b && b != 0)\n    {\n        cout << \"Condition is true: a > b and b is non-zero\" << endl;\n    }\n\n    return 0;\n}",
        "content": "![University Header](assets/images/university/itc/lab0_hamdard_logo.png)\n\n\n# LAB # 14\n\nArithmetic and logic operations\n\n\n## Objective\n\n\nLearn to write programs using different arithmetic and logical operators\n\n\n## Theory\n\n\n\n## Arithmetic Operators:\n\n\nArithmetic Operators\u00a0are used to do basic arithmetic operations like addition, subtraction, multiplication, division, and modulus.\n\nTypes of Arithmetic Operators:\n\nThe following table lists the arithmetic operators used in C++.\n\n\n\n| Operator | Action | Description |\n\n| --- | --- | --- |\n\nOperator\n\nAction\n\nDescription\n\n\n\n| + | Addition | Adds two operands |\n\n| --- | --- | --- |\n\n+\n\nAddition\n\nAdds two operands\n\n\n\n| - | Subtraction | Subtracts second operand from the first |\n\n| --- | --- | --- |\n\n-\n\nSubtraction\n\nSubtracts second operand from the first\n\n\n\n| * | Multiplication | Multiplies both operands |\n\n| --- | --- | --- |\n\n*\n\nMultiplication\n\nMultiplies both operands\n\n\n\n| / | Division | Divides numerator by de-numerator |\n\n| --- | --- | --- |\n\n/\n\nDivision\n\nDivides numerator by de-numerator\n\n\n\n| % | Modulus | Modulus Operator and remainder of after an integer division |\n\n| --- | --- | --- |\n\n%\n\nModulus\n\nModulus Operator and remainder of after an integer division\n\nSample Program\n\n\n\n| #include <iostream.h>int main( ){int x = 13;int y = 6;int a = x%y;int b = x+y;cout << \"The Modulus of x,y is ::\" << a << '\\n' ;cout << \"The Sum of x,y is ::\" << b << '\\n' ;return 0;} |\n\n| --- |\n\n| Program Output:  The Modulus of x,y is :: 1The Sum of x,y is :: 19 |\n\n\n### Program Output:\n\n\nThe Modulus of x,y is :: 1The Sum of x,y is :: 19\n\n\n## Unary Arithmetic Operators\n\n\nUnary operators are operators that only take one operand.There are two unary arithmetic operators, plus (+), and minus (-). These are used as increment and decrement operators.\n\n\n\n| Increment | ++ | Increment operator, increases integer value by one |\n\n| --- | --- | --- |\n\nIncrement\n\n++\n\nIncrement operator, increases integer value by one\n\n\n\n| Decrement | -- | Decrement operator, decreases integer value by one |\n\n| --- | --- | --- |\n\nDecrement\n\n--\n\nDecrement operator, decreases integer value by one\n\n\n### Examples\n\n\n\n\n| x = x+1;  is the same as  x++; | x = x-1;  is the same as  x--; |\n\n| --- | --- |\n\nx = x+1;\n\nis the same as\n\nx++;\n\nx = x-1;\n\nis the same as\n\nx--;\n\nSample Program:\n\n\n\n| #include <iostream.h>  main() { int a = 21; int c ;  // Value of a will not be increased before assignment. c = a++; cout << \"Value of a++ is :\" << c << endl ;  // After expression value of a is increased cout << \"Value of a is :\" << a << endl ;  // Value of a will be increased before assignment. c = ++a; cout << \"Value of ++a is  :\" << c << endl ; return 0; } |\n\n| --- |\n\n#include <iostream.h>\n\nmain()\n\n{\n\nint a = 21;\n\nint c ;\n\n// Value of a will not be increased before assignment.\n\nc = a++;\n\ncout << \"Value of a++ is :\" << c << endl ;\n\n// After expression value of a is increased\n\ncout << \"Value of a is :\" << a << endl ;\n\n// Value of a will be increased before assignment.\n\nc = ++a;\n\ncout << \"Value of ++a is  :\" << c << endl ;\n\nreturn 0;\n\n}\n\n\n\n| Program Output:  Value of a++ is :21 Value of a is :22 Value of ++a is  :23 |\n\n| --- |\n\n\n### Program Output:\n\n\nValue of a++ is :21\n\nValue of a is :22\n\nValue of ++a is  :23\n\n\n## Assignment operator (=)\n\n\nThe assignment operator assigns a value to a variable. The assignment operation always takes place from right to left.\n\ne.g. x = 5;\n\nThis statement assigns the integer value\u00a05\u00a0to the variable\u00a0x.\n\nSample Program:\n\n\n\n| #include <iostream.h>  int main () { int a, b;         // a:?,  b:? a = 10;           // a:10, b:? b = 4;            // a:10, b:4 a = b;            // a:4,  b:4 b = 7;            // a:4,  b:7  cout << \"a:\"; cout << a; cout << \" b:\"; cout << b; } |\n\n| --- |\n\n#include <iostream.h>\n\nint main ()\n\n{\n\nint a, b;         // a:?,  b:?\n\na = 10;           // a:10, b:?\n\nb = 4;            // a:10, b:4\n\na = b;            // a:4,  b:4\n\nb = 7;            // a:4,  b:7\n\ncout << \"a:\";\n\ncout << a;\n\ncout << \" b:\";\n\ncout << b;\n\n}\n\n\n\n| Program Output:  a:4   b:7 |\n\n| --- |\n\n\n### Program Output:\n\n\na:4   b:7\n\n\n## Relational Operators:\n\n\nIn the following table different relational operators are listed that are supported by C++ language\n\n\n\n| Operator | Description | Example |\n\n| --- | --- | --- |\n\nOperator\n\nDescription\n\n\n### Example\n\n\n\n\n| == | Checks if the values of two operands are equal or not | (A == B) |\n\n| --- | --- | --- |\n\n==\n\nChecks if the values of two operands are equal or not\n\n(A == B)\n\n\n\n| != | Checks if the values of two operands are equal or not | (A!= B) |\n\n| --- | --- | --- |\n\n!=\n\nChecks if the values of two operands are equal or not\n\n(A!= B)\n\n\n\n| > | Checks if the value of left operand is greater than the value of the right operand | (A > B) |\n\n| --- | --- | --- |\n\n>\n\nChecks if the value of left operand is greater than the value of the right operand\n\n(A > B)\n\n\n\n| < | Checks if the value of left operand is less than the value of the right operand | (A < B) |\n\n| --- | --- | --- |\n\n<\n\nChecks if the value of left operand is less than the value of the right operand\n\n(A < B)\n\n\n\n| >= | Checks if the value of left operand is greater than or equal to the value of the right operand | (A >= B |\n\n| --- | --- | --- |\n\n>=\n\nChecks if the value of left operand is greater than or equal to the value of the right operand\n\n(A >= B\n\n\n\n| <= | Checks if the value of left operand is less than or equal to the value of the right operand | (A <= B) |\n\n| --- | --- | --- |\n\n<=\n\nChecks if the value of left operand is less than or equal to the value of the right operand\n\n(A <= B)\n\nSample Program\n\n\n\n| #include <iostream.h>  main() { int a = 21; int b = 10; int c ;  if( a == b ) { cout <<\u201ca is equal to b\" << endl ; } else { cout <<\"a is not equal to b\" << endl ; } if ( a < b ) { cout <<\"a is less than b\" << endl ; } else { cout <<\"a is not less than b\" << endl ; } if ( a > b ) { cout <<\"a is greater than b\" << endl ; } else { cout <<\"a is not greater than b\" << endl ; } return 0; } |\n\n| --- |\n\n#include <iostream.h>\n\nmain()\n\n{\n\nint a = 21;\n\nint b = 10;\n\nint c ;\n\nif( a == b )\n\n{\n\ncout <<\u201ca is equal to b\" << endl ;\n\n}\n\nelse\n\n{\n\ncout <<\"a is not equal to b\" << endl ;\n\n}\n\nif ( a < b )\n\n{\n\ncout <<\"a is less than b\" << endl ;\n\n}\n\nelse\n\n{\n\ncout <<\"a is not less than b\" << endl ;\n\n}\n\nif ( a > b )\n\n{\n\ncout <<\"a is greater than b\" << endl ;\n\n}\n\nelse\n\n{\n\ncout <<\"a is not greater than b\" << endl ;\n\n}\n\nreturn 0;\n\n}\n\n\n\n| Program Output:  a is not equal to b a is not less than b a is greater than b |\n\n| --- |\n\n\n### Program Output:\n\n\na is not equal to b\n\na is not less than b\n\na is greater than b\n\n\n## Logical Operators:\n\n\nThere are following logical operators supported by C++ that are defined in  the table below:\n\n\n\n| Operator | Description | Example |\n\n| --- | --- | --- |\n\nOperator\n\nDescription\n\n\n### Example\n\n\n\n\n| && | Called Logical AND operator. If both the operands are non-zero, then condition becomes true. | (A && B) |\n\n| --- | --- | --- |\n\n&&\n\nCalled Logical AND operator. If both the operands are non-zero, then condition becomes true.\n\n(A && B)\n\n\n\n|  |  |  | Called Logical OR Operator. If any of the two operands is non-zero, then condition becomes true. | (A |  | B) |\n\n| --- | --- | --- | --- | --- | --- | --- |\n\n||\n\nCalled Logical OR Operator. If any of the two operands is non-zero, then condition becomes true.\n\n(A || B)\n\n\n\n| ! | Called Logical NOT Operator. Use to reverse the logical state of its operand. If a condition is true, then Logical NOT operator will make false. | !(A && B) |\n\n| --- | --- | --- |\n\n!\n\nCalled Logical NOT Operator. Use to reverse the logical state of its operand. If a condition is true, then Logical NOT operator will make false.\n\n!(A && B)\n\nSample Program\n\n\n\n| #include <iostream.h> main() { int a = 5; int b = 20; int c ;  if ( a && b ) { cout << \"Line 1 - Condition is true\"<< endl ; } if ( a |  | b ) { cout << \"Line 2 - Condition is true\"<< endl ; } /* Let's change the values of  a and b */ a = 0; b = 10; if ( a && b ) { cout << \"Line 3 - Condition is true\"<< endl ; } else { cout << \"Line 4 - Condition is not true\"<< endl ; } if ( !(a && b) ) { cout << \"Line 5 - Condition is true\"<< endl ; } return 0; } |\n\n| --- | --- | --- |\n\n#include <iostream.h>\n\nmain()\n\n{\n\nint a = 5;\n\nint b = 20;\n\nint c ;\n\nif ( a && b )\n\n{\n\ncout << \"Line 1 - Condition is true\"<< endl ;\n\n}\n\nif ( a || b )\n\n{\n\ncout << \"Line 2 - Condition is true\"<< endl ;\n\n}\n\n/* Let's change the values of  a and b */\n\na = 0;\n\nb = 10;\n\nif ( a && b )\n\n{\n\ncout << \"Line 3 - Condition is true\"<< endl ;\n\n}\n\nelse\n\n{\n\ncout << \"Line 4 - Condition is not true\"<< endl ;\n\n}\n\nif ( !(a && b) )\n\n{\n\ncout << \"Line 5 - Condition is true\"<< endl ;\n\n}\n\nreturn 0;\n\n}\n\n\n\n| Program Output:  Line 1 - Condition is true Line 2 - Condition is true Line 4 - Condition is not true Line 5 - Condition is true |\n\n| --- |\n\n\n### Program Output:\n\n\nLine 1 - Condition is true\n\nLine 2 - Condition is true\n\nLine 4 - Condition is not true\n\nLine 5 - Condition is true\n\n\n## Lab Task\n\n\nWrite a program that prints the area and the parameter of the rectangle\n\nArea of rectangle: LxB\n\nParameter of rectangle: 2(L+B)\n\nSample Output\n\nEnter length of the rectangle: 6\n\nEnter breadth of rectangle: 9\n\nArea of a rectangle is 54\n\nWrite a program that checks whether the entered alphabet is a vowel or not\n\nWrite a program that checks whether the number entered as input is odd or even.\n\nWrite a program that takes two numbers as input and then calculate and print the sum, difference, product and quotients of these two numbers\n\nSample Output\n\nEnter first number: 6\n\nEnter second number: 2\n\nSum: 8\n\nDifference: 4\n\nProduct: 12\n\nQuotient: 3",
        "quizzes": [
            {
                        "question": "What is the result of 13 % 6 in C++?",
                        "options": [
                                    "1 (remainder of integer division 13 / 6)",
                                    "2 (quotient)",
                                    "0",
                                    "7"
                        ],
                        "correctAnswer": "1 (remainder of integer division 13 / 6)",
                        "explanation": "The modulus operator % calculates the integer remainder: 13 divided by 6 is 2 with a remainder of 1."
            },
            {
                        "question": "If int a = 21, what is the value of c after executing c = a++;?",
                        "options": [
                                    "21 (post-increment assigns first, then increments a to 22)",
                                    "22",
                                    "20",
                                    "Undefined"
                        ],
                        "correctAnswer": "21 (post-increment assigns first, then increments a to 22)",
                        "explanation": "With post-increment (a++), the current value 21 is assigned to c before a is incremented to 22."
            },
            {
                        "question": "Which logical operator evaluates to true if either one of the operands is true?",
                        "options": [
                                    "|| (Logical OR)",
                                    "&& (Logical AND)",
                                    "! (Logical NOT)",
                                    "== (Equality)"
                        ],
                        "correctAnswer": "|| (Logical OR)",
                        "explanation": "The logical OR operator || returns true if at least one of its conditions evaluates to true."
            }
],
        "flashcards": [
            {
                        "question": "In which direction does variable assignment always execute in C++?",
                        "answer": "From right to left (the right-hand expression is evaluated and stored into the left-hand variable)."
            },
            {
                        "question": "What is the difference between pre-increment (++a) and post-increment (a++)?",
                        "answer": "Pre-increment increases the variable before its value is used in the expression; post-increment uses the original value before increasing."
            },
            {
                        "question": "What mathematical operator returns the remainder of integer division?",
                        "answer": "The modulus operator (%)."
            },
            {
                        "question": "What does the logical NOT operator (!) do?",
                        "answer": "It inverts the boolean state of its operand, turning true into false and false into true."
            }
]
    },
]


def seed_itc_curriculum(db: Optional[Prisma] = None, verbose: bool = True):
    owns_connection = False
    if db is None:
        db = Prisma()
        for attempt in range(1, 5):
            try:
                db.connect()
                break
            except Exception as e:
                if attempt == 4:
                    raise
                print(f"[!] DB connection attempt {attempt} failed ({e}), retrying in 3s...")
                time.sleep(3)
        owns_connection = True
    elif not db.is_connected():
        for attempt in range(1, 5):
            try:
                db.connect()
                break
            except Exception as e:
                if attempt == 4:
                    raise
                print(f"[!] DB connection attempt {attempt} failed ({e}), retrying in 3s...")
                time.sleep(3)

    try:
        if verbose:
            print("======================================================================")
            print(f"[*] SEEDING UNIVERSITY COURSE: '{COURSE_DATA['title']}'")
            print(f"    Category: {COURSE_DATA['category']} | Labs to seed: {len(LABS_DATA)}")
            print("======================================================================")

        # 1. Locate or create Lesson record
        lesson = db.lesson.find_first(where={"title": {"contains": "Introduction to Computing"}})
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
                print(f"[+] Created Lesson record: ID={lesson.id}")
        else:
            lesson = db.lesson.update(
                where={"id": lesson.id},
                data={
                    "title": COURSE_DATA["title"],
                    "category": COURSE_DATA["category"],
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[*] Updated existing Lesson record: ID={lesson.id}")

        # 2. Idempotent cleanup of old steps, quizzes, and flashcards for ONLY THIS LESSON
        del_q = db.quiz.delete_many(where={"lessonId": lesson.id})
        del_f = db.flashcard.delete_many(where={"lessonId": lesson.id})
        del_s = db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"[*] Cleared previous records: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

        # 3. Insert Labs 1 to 14 LessonSteps, Quizzes, and Flashcards
        summary_rows = []
        total_quizzes = 0
        total_flashcards = 0

        for lab in LABS_DATA:
            step = db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": lab["order"],
                    "title": lab["title"],
                    "content": lab["content"],
                    "codeSnippet": lab.get("codeSnippet", "")
                }
            )

            # Insert Quizzes linked to both lessonId and lessonStepId
            for q in lab["quizzes"]:
                db.quiz.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": q["question"],
                        "options": q["options"],
                        "correctAnswer": q["correctAnswer"],
                        "explanation": q.get("explanation", "")
                    }
                )
                total_quizzes += 1

            # Insert Flashcards linked to both lessonId and lessonStepId
            for fc in lab["flashcards"]:
                db.flashcard.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": fc["question"],
                        "answer": fc["answer"]
                    }
                )
                total_flashcards += 1

            summary_rows.append({
                "lab_num": f"Lab {lab['order']}",
                "title": lab["title"][:48],
                "quizzes_count": len(lab["quizzes"]),
                "flashcards_count": len(lab["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 80)
            print("SUMMARY TABLE: UNIVERSITY LABS 1 TO 14 SEEDED SUCCESSFULLY")
            print("=" * 80)
            print(f"{'Lab #':<8} | {'Title':<50} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 80)
            for row in summary_rows:
                print(f"{row['lab_num']:<8} | {row['title']:<50} | {row['quizzes_count']:<8} | {row['flashcards_count']:<10}")
            print("=" * 80)
            print(f"Total LessonSteps: {len(LABS_DATA)}")
            print(f"Total Quizzes:     {total_quizzes}")
            print(f"Total Flashcards:  {total_flashcards}")
            print(f"Category:          {COURSE_DATA['category']}")
            print("=" * 80)

        return {
            "lessonId": lesson.id,
            "title": lesson.title,
            "category": lesson.category,
            "stepsCount": len(LABS_DATA),
            "quizzesCount": total_quizzes,
            "flashcardsCount": total_flashcards
        }

    finally:
        if owns_connection and db.is_connected():
            db.disconnect()


if __name__ == "__main__":
    seed_itc_curriculum()
