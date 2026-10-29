"""
Intro to computing Curriculum Seeder (List of Experiments)
Hamdard University Islamabad Campus - Hamdard Institute of Engineering & Technology (HIET).

100% VERBATIM transcription from "Intro to coumputing (List of Experiments).docx".
Complete 14-Lab Curriculum Covering:
- Lab 1: Be able to operate under supervision the Computer Hardware (CLO-1, PLO-1, P3)
- Lab 2: Be able to operate under supervision the Windows Operating System and its Components (CLO-1, PLO-1, P3)
- Lab 3: Practicing the basics of Networking and Routing (CLO-1, PLO-1, P3)
- Lab 4: Imitate Microsoft Word (CLO-1, PLO-1, P3)
- Lab 5: Imitate Microsoft Excel (CLO-1, PLO-1, P3)
- Lab 6: Practice the basics of Microsoft Excel (CLO-1, PLO-1, P3)
- Lab 7: Imitate Microsoft Excel (CLO-2, PLO-1, P3)
- Lab 8: Practicing the basics of HTML (CLO-2, PLO-1, P3)
- Lab 9: Be able to repeat the basics of HTML (CLO-2, PLO-1, P3)
- Lab 10: Practice Web Page designing using HTML (CLO-2, PLO-1, P3)
- Lab 11: Be able to operate under supervision the basics of Matlab (CLO-2, PLO-1, P3)
- Lab 12: Practicing the basics of Programming in C++ (CLO-2, PLO-1, P3)
- Lab 13: Be able to operate under supervision the basics functions of C++ (CLO-2, PLO-1, P3)
- Lab 14: Be able to manipulate with guidance the Arithmetic and logic operations in C++ (CLO-2, PLO-1, P3)

Assessments:
- EXACTLY 5 verified multi-choice Quizzes per Lab (70 Quizzes total)
- EXACTLY 4 Flashcards per Lab (56 Flashcards total)
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(backend_dir, ".env"))

from prisma import Prisma

COURSE_DATA = {
    "title": "Intro to computing",
    "category": "University",
    "description": "Official Academic Curriculum for Intro to computing (List of Experiments), Faculty of Engineering Sciences & Technology (FEST), Hamdard University Islamabad Campus / Hamdard Institute of Engineering & Technology (HIET). Comprehensive hands-on laboratory sequence structured around Outcome-Based Education (OBE) CLO-1/CLO-2, PLO-1, and Psychomotor Taxonomy Level P3 (Guided Response). Covers Computer Hardware Operations, Windows OS Environment & Diagnostics, Networking & Routing Essentials, Microsoft Word Technical Documentation, Microsoft Excel Spreadsheets, Built-in Formulas & Relative/Absolute Addressing, Advanced Data Analysis & Visual Charts, HTML Web Page Construction, MATLAB Engineering Computations, and C++ Programming Fundamentals.",
    "color": "#4F46E5",
    "thumbnail": "assets/images/university/itc_exp/itc_exp_logo.png"
}

LABS_PART1 = [   {   'codeSnippet': '# Windows Command Prompt: Hardware Inspection & Diagnostics\n'
                       '\n'
                       '# 1. Display detailed computer system hardware & BIOS specifications:\n'
                       'systeminfo\n'
                       '\n'
                       '# 2. Query Central Processing Unit (CPU) details via WMIC:\n'
                       'wmic cpu get name, maxclockspeed, numberofcores, numberoflogicalprocessors\n'
                       '\n'
                       '# 3. Query installed Physical Memory (RAM) capacity and speed:\n'
                       'wmic memorychip get capacity, speed, manufacturer, devicelocator\n'
                       '\n'
                       '# 4. Query physical disk drives and storage interfaces:\n'
                       'wmic diskdrive get model, size, mediatype, interfacetype\n'
                       '\n'
                       '# 5. Launch Windows DirectX Diagnostic Tool for display and sound hardware:\n'
                       'dxdiag',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 1: Be able to operate under supervision the Computer Hardware\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to operate under supervision the Computer Hardware** | '
                   '**CLO-1** | **PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Identify and inspect the essential internal and external components of a personal computer '
                   'system.\n'
                   '* Understand the fundamental Von Neumann architecture: CPU, Primary Memory (RAM/ROM), Secondary '
                   'Storage, and Input/Output subsystems.\n'
                   '* Operate computer hardware under supervision following electrostatic discharge (ESD) and '
                   'electrical safety precautions.\n'
                   '* Differentiate between system ports, peripheral interfaces, bus architectures, and power supply '
                   'units (SMPS).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   'A personal computer is an electronic system composed of hardware—the physical, tangible parts—and '
                   'software—the instructions that control them.\n'
                   '\n'
                   '![Computer Hardware Components](assets/images/university/itc/lab1_hardware.png)\n'
                   '\n'
                   '#### 1. Central Processing Unit (CPU):\n'
                   "Often referred to as the 'brain' of the computer, the CPU executes program instructions and "
                   'coordinates the actions of all other units. It comprises:\n'
                   '* **Arithmetic Logic Unit (ALU):** Performs all arithmetic computations (addition, subtraction, '
                   'multiplication) and logical comparisons (AND, OR, NOT, greater-than, equal-to).\n'
                   '* **Control Unit (CU):** Directs the flow of data through the processor and coordinates the '
                   'execution of instructions using the Fetch-Decode-Execute cycle.\n'
                   '* **Registers & Cache Memory:** Ultra-fast, internal storage locations (L1, L2, L3 cache) used to '
                   'hold immediate data and frequently referenced machine instructions.\n'
                   '\n'
                   '![Central Processing Unit](assets/images/university/itc/lab1_cpu.png)\n'
                   '\n'
                   '#### 2. Motherboard (System Board):\n'
                   'The primary printed circuit board (PCB) that houses the CPU socket, RAM slots, expansion bus slots '
                   '(PCI Express), chipset (Northbridge/Southbridge or unified PCH), BIOS/UEFI firmware chip, and '
                   'power connectors.\n'
                   '\n'
                   '![Motherboard Architecture](assets/images/university/itc/lab1_motherboard.png)\n'
                   '![Motherboard Diagram](assets/images/university/itc/lab1_motherboard_diagram.png)\n'
                   '\n'
                   '#### 3. Primary Memory (RAM & ROM):\n'
                   '* **Random Access Memory (RAM):** Volatile primary storage that provides high-speed read/write '
                   'access for currently executing applications and the operating system kernel. When power is lost, '
                   'all data in RAM is erased.\n'
                   '* **Read-Only Memory (ROM):** Non-volatile memory holding the firmware (Basic Input/Output System '
                   '- BIOS or Unified Extensible Firmware Interface - UEFI) required to initialize system hardware '
                   'during the Power-On Self-Test (POST).\n'
                   '\n'
                   '![RAM Module](assets/images/university/itc/lab1_ram.png)\n'
                   '\n'
                   '#### 4. Secondary Storage (HDD & SSD):\n'
                   '* **Hard Disk Drive (HDD):** Magnetic storage device consisting of spinning magnetic platters and '
                   'read/write actuator heads. Connects via SATA interface (3 Gbps or 6 Gbps).\n'
                   '* **Solid State Drive (SSD):** Non-volatile flash memory storage utilizing NAND gates. Offers '
                   'drastically higher data transfer throughput and zero mechanical latency compared to HDDs.\n'
                   '\n'
                   '![Hard Disk Drive](assets/images/university/itc/lab1_hdd.png)\n'
                   '\n'
                   '#### 5. Power Supply Unit (Switched-Mode Power Supply - SMPS):\n'
                   'Converts incoming high-voltage Alternating Current (AC, 110V/220V) from the wall outlet into '
                   'regulated, low-voltage Direct Current (DC: +3.3V, +5V, +12V, -12V) required to power the '
                   'motherboard, processor, disk drives, and cooling fans.\n'
                   '\n'
                   '#### 6. Input/Output Interfaces & System Ports:\n'
                   'The system unit communicates with external peripheral devices through standardized ports on the '
                   'rear and front I/O panels:\n'
                   '* **USB (Universal Serial Bus):** High-speed serial connection for mice, keyboards, printers, '
                   'flash drives (USB 2.0: 480 Mbps, USB 3.0: 5 Gbps).\n'
                   '* **Video Ports:** HDMI (High-Definition Multimedia Interface), DisplayPort, DVI, and legacy VGA '
                   '(Video Graphics Array 15-pin D-sub analog).\n'
                   '* **Audio Jacks:** 3.5mm stereo output, line-in, and microphone jacks.\n'
                   '* **Ethernet RJ-45:** Gigabit network interface for local area network (LAN) cabling.\n'
                   '\n'
                   '![Input Output Ports](assets/images/university/itc/lab1_ports.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures & Safety Guidelines:\n'
                   '\n'
                   '1. **Safety First:** Disconnect the AC power cable from the SMPS before opening the system unit '
                   'casing. Avoid working on damp surfaces.\n'
                   '2. **Electrostatic Discharge (ESD) Prevention:** Touch an unpainted metallic part of the chassis '
                   'or use an anti-static wrist strap to ground static charges before handling the motherboard, RAM, '
                   'or CPU.\n'
                   '3. **Component Inspection:** Locate the CPU heatsink and cooling fan, RAM DIMM slots, SATA data '
                   'cables, 24-pin ATX motherboard power connector, and 4/8-pin CPU 12V connector.\n'
                   '4. **Peripheral Connections:** Connect keyboard, mouse, monitor, and power cables to their '
                   'designated ports.\n'
                   '5. **Boot Verification:** Power on the PC and verify that the system completes POST with a single '
                   'confirmation beep.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   "1. Inspect a desktop PC system unit under the supervisor's guidance. Identify and list the "
                   'manufacturer and model of the CPU, RAM capacity, and HDD/SSD storage capacity.\n'
                   '2. Execute the CLI command `systeminfo` in Command Prompt. Note down the OS Name, System '
                   'Manufacturer, System Model, Processor model, and Total Physical Memory.\n'
                   '3. Using `wmic memorychip get capacity, speed`, determine the exact clock speed (in MHz) and '
                   'capacity of each installed RAM module.\n'
                   '4. Draw a schematic block diagram illustrating how the CPU, RAM, Secondary Storage, and I/O '
                   'devices interconnect through the system bus (Data Bus, Address Bus, Control Bus).',
        'flashcards': [   {   'answer': 'The Control Unit directs the flow of data through the processor and '
                                        'coordinates the execution of instructions using the Fetch-Decode-Execute '
                                        'cycle.',
                              'question': 'What is the role of the Control Unit (CU) within the CPU?'},
                          {   'answer': 'Power-On Self-Test (POST) is a hardware diagnostic sequence executed by the '
                                        'BIOS/UEFI firmware in ROM upon system power-up to verify core hardware '
                                        'components.',
                              'question': 'What is POST and which component initiates it?'},
                          {   'answer': 'An SSD uses solid-state NAND flash memory with zero moving parts, providing '
                                        'significantly faster read/write throughput and near-instant access times '
                                        'compared to mechanical magnetic platters in an HDD.',
                              'question': 'What is the key performance difference between an SSD and an HDD?'},
                          {   'answer': 'The Address Bus (specifies physical memory locations), the Data Bus '
                                        '(transfers bidirectional data bytes), and the Control Bus (transmits timing '
                                        'and control signals).',
                              'question': 'What are the three components of the system bus that interconnect hardware '
                                          'modules?'}],
        'order': 1,
        'quizzes': [   {   'correctAnswer': 'Arithmetic Logic Unit (ALU)',
                           'explanation': 'The Arithmetic Logic Unit (ALU) performs all arithmetic operations (such as '
                                          'addition and subtraction) and logical decisions (AND, OR, NOT, comparisons) '
                                          'in the computer system.',
                           'options': [   'Arithmetic Logic Unit (ALU)',
                                          'Control Unit (CU)',
                                          'Cache Memory',
                                          'Program Counter (PC)'],
                           'question': 'Which internal component of the Central Processing Unit (CPU) is specifically '
                                       'responsible for executing mathematical calculations and logical comparisons?'},
                       {   'correctAnswer': 'RAM is volatile and loses its contents when powered down, while ROM is '
                                            'non-volatile',
                           'explanation': 'RAM is volatile primary memory that requires electrical power to retain '
                                          'data. ROM is non-volatile and permanently stores firmware instructions such '
                                          'as the BIOS/UEFI even when the computer is turned off.',
                           'options': [   'RAM is volatile and loses its contents when powered down, while ROM is '
                                          'non-volatile',
                                          'ROM is volatile and faster than RAM',
                                          'RAM stores the BIOS/UEFI firmware permanently',
                                          'ROM provides temporary execution workspace for user software'],
                           'question': 'What is the primary technical distinction between Random Access Memory (RAM) '
                                       'and Read-Only Memory (ROM)?'},
                       {   'correctAnswer': 'Converts high-voltage AC electricity into low-voltage regulated DC power '
                                            'for internal components',
                           'explanation': 'The SMPS converts incoming high-voltage Alternating Current (AC, 110V/220V) '
                                          'into multiple regulated low-voltage Direct Current (DC) rails (+3.3V, +5V, '
                                          '+12V) needed by PC components.',
                           'options': [   'Converts high-voltage AC electricity into low-voltage regulated DC power '
                                          'for internal components',
                                          'Provides uninterruptible battery power during utility blackouts',
                                          'Amplifies audio signals before sending them to external speakers',
                                          'Synchronizes the clock frequency of the processor and system memory'],
                           'question': 'What function does the Switched-Mode Power Supply (SMPS) perform in a desktop '
                                       'computer system?'},
                       {   'correctAnswer': 'Ground oneself by touching unpainted chassis metal or wearing an '
                                            'anti-static wrist strap',
                           'explanation': 'To prevent catastrophic ESD damage to sensitive semiconductor chips, '
                                          'technicians must ground themselves using an anti-static wrist strap or by '
                                          'periodically touching an unpainted metallic part of the chassis.',
                           'options': [   'Ground oneself by touching unpainted chassis metal or wearing an '
                                          'anti-static wrist strap',
                                          'Keep the PC plugged into mains power and running during disassembly',
                                          'Wear synthetic wool gloves and work on a nylon carpet',
                                          'Moisten the motherboard with clean water before touching chips'],
                           'question': 'Which precautions must be strictly observed to prevent Electrostatic Discharge '
                                       '(ESD) damage when handling internal PC hardware?'},
                       {   'correctAnswer': 'systeminfo',
                           'explanation': "The 'systeminfo' command queries and displays comprehensive operating "
                                          'system and hardware configuration information including processor, BIOS, '
                                          'physical RAM, and network adapters.',
                           'options': ['systeminfo', 'ipconfig', 'ping', 'chkdsk'],
                           'question': 'In the Windows Command Prompt, which utility provides a comprehensive summary '
                                       'of OS version, system manufacturer, processor model, and total physical RAM?'}],
        'title': 'Lab 1: Be able to operate under supervision the Computer Hardware'},
    {   'codeSnippet': '# Windows Run Dialog & Command Prompt: Operating System Utilities\n'
                       '\n'
                       '# 1. Launch Device Manager to inspect installed drivers and hardware status:\n'
                       'devmgmt.msc\n'
                       '\n'
                       '# 2. Launch System Properties to inspect Computer Name, Workgroup, and Hardware:\n'
                       'sysdm.cpl\n'
                       '\n'
                       '# 3. Launch Windows Task Manager to monitor processes, CPU, and RAM utilization:\n'
                       'taskmgr\n'
                       '\n'
                       '# 4. Launch Computer Management console:\n'
                       'compmgmt.msc\n'
                       '\n'
                       '# 5. Query active running tasks and processes via CLI:\n'
                       'tasklist\n'
                       '\n'
                       '# 6. File operation: create directory structure and verify via command line:\n'
                       'mkdir C:/ITC_Lab/MyDocuments\n'
                       'dir C:/ITC_Lab',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 2: Be able to operate under supervision the Windows Operating System and its Components\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to operate under supervision the Windows Operating System and '
                   'its Components** | **CLO-1** | **PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the fundamental role of an Operating System as an intermediary between user '
                   'applications and physical hardware.\n'
                   '* Navigate and customize the Windows Graphical User Interface (GUI): Desktop, Taskbar, Start Menu, '
                   'System Tray, and Notification Area.\n'
                   '* Access and configure core system management tools: System Properties, Device Manager, and '
                   'Control Panel.\n'
                   '* Perform file and folder management operations: creating, renaming, copying, moving, deleting, '
                   'and setting file attributes in File Explorer.\n'
                   '* Utilize Windows Task Manager to monitor CPU, RAM, and Disk performance and manage running '
                   'processes.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   'An **Operating System (OS)** is system software that manages computer hardware, software '
                   'resources, and provides common services for computer programs. Without an operating system, a '
                   'computer cannot execute application programs or respond to user interactions.\n'
                   '\n'
                   '#### 1. Core Functions of an Operating System:\n'
                   '* **Processor Management:** Allocates CPU time slices to active processes using scheduling '
                   'algorithms.\n'
                   '* **Memory Management:** Allocates and deallocates primary memory (RAM) and virtual memory (paging '
                   'file) to programs.\n'
                   '* **File System Management:** Organizes physical disk storage into structured hierarchies of '
                   'directories and files (e.g., NTFS, FAT32).\n'
                   '* **Device Management:** Communicates with hardware controllers via specialized software drivers.\n'
                   '* **Security & Access Control:** Enforces user authentication, credentials, and file permissions.\n'
                   '\n'
                   '#### 2. Key Windows GUI Components:\n'
                   '* **The Desktop:** The primary workspace on the screen displaying icons, shortcuts, and background '
                   'wallpaper.\n'
                   '* **The Taskbar:** Horizontal strip typically located at the bottom of the screen containing the '
                   'Start button, pinned applications, active running windows, and the System Tray (notification area '
                   'with clock and volume).\n'
                   '* **File Explorer (Windows Explorer):** Graphical file management interface providing tree '
                   'navigation of logical drives (C:, D:), folders, and libraries.\n'
                   '\n'
                   '#### 3. Administrative Control Tools:\n'
                   '\n'
                   '![System Properties](assets/images/university/itc/lab2_system_properties.png)\n'
                   '\n'
                   '* **System Properties (`sysdm.cpl`):** Displays OS edition, processor model, installed RAM, '
                   'Computer Name, Workgroup, and advanced performance settings.\n'
                   '* **Device Manager (`devmgmt.msc`):** Lists all hardware detected by the OS. A yellow exclamation '
                   'mark indicates a missing or malfunctioning hardware driver.\n'
                   '\n'
                   '![Device Manager](assets/images/university/itc/lab2_devicemanager.png)\n'
                   '\n'
                   '* **Computer Name Tab:** Used to configure the computer name and join a Workgroup or domain '
                   'network.\n'
                   '\n'
                   '![Computer Name Configuration](assets/images/university/itc/lab2_computer_name.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Navigating the Desktop & Taskbar:**\n'
                   '   * Pin an application to the Taskbar by right-clicking its icon and selecting *Pin to taskbar*.\n'
                   '   * Customize the Notification Area icons and inspect system audio and network icons.\n'
                   '2. **Inspecting System Specifications:**\n'
                   '   * Press `Windows Key + Pause/Break` or run `sysdm.cpl` in the Run dialog (`Win + R`).\n'
                   '   * Record the Windows Edition, System Type (64-bit vs 32-bit), Processor, and Installed Memory.\n'
                   '3. **Operating Device Manager:**\n'
                   '   * Launch `devmgmt.msc`. Expand categories such as *Display adapters*, *Network adapters*, and '
                   '*Disk drives*.\n'
                   '   * Verify that no devices display warning triangles.\n'
                   '4. **File Management Workflow:**\n'
                   '   * Open File Explorer (`Win + E`). Navigate to `C:/Users/Student/Documents`.\n'
                   '   * Create a folder named `ITC_Lab_Work`. Create a subfolder named `Lab_02`.\n'
                   '   * Create a text file named `System_Specs.txt`. Enter your system properties into the file.\n'
                   '   * Practice copying (`Ctrl + C`), cutting (`Ctrl + X`), pasting (`Ctrl + V`), and deleting '
                   '(`Del` and `Shift + Del` for permanent deletion).\n'
                   '5. **Process Monitoring via Task Manager:**\n'
                   '   * Press `Ctrl + Shift + Esc` to open Task Manager. View the *Processes* and *Performance* '
                   'tabs.\n'
                   '   * Observe real-time graphs for CPU, Memory, and Disk utilization.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Using `sysdm.cpl`, record the exact Computer Name, Workgroup, Windows edition, and 64-bit OS '
                   'status of your laboratory PC.\n'
                   '2. Open Device Manager (`devmgmt.msc`). Locate your network adapter model and display adapter '
                   'model. State their exact hardware device names.\n'
                   '3. In File Explorer, create a folder structure `C:/ITC_2026/Operating_Systems`. Create two text '
                   'files within it, move one file to your desktop, and permanently delete the other using keyboard '
                   'shortcuts.\n'
                   '4. Launch Task Manager (`taskmgr`). Identify the process consuming the highest amount of physical '
                   'RAM and explain how to terminate a non-responsive program.',
        'flashcards': [   {   'answer': 'An Operating System acts as an intermediary between computer hardware and '
                                        'user applications, managing CPU scheduling, memory allocation, storage '
                                        'filesystems, and device I/O.',
                              'question': 'What is the primary role of an Operating System?'},
                          {   'answer': 'The Taskbar provides quick access to the Start menu, pinned application '
                                        'shortcuts, buttons for all open application windows, and the notification '
                                        'area (system tray).',
                              'question': 'What is the function of the Windows Taskbar?'},
                          {   'answer': 'Press Windows Key + R. It allows users to directly launch programs, control '
                                        'panel applets (.cpl), and management consoles (.msc) by typing their '
                                        'executable names.',
                              'question': 'How do you access the Windows Run dialog, and what is its purpose?'},
                          {   'answer': 'NTFS (New Technology File System), which provides file permissions (ACLs), '
                                        'encryption (EFS), compression, journaling, and support for large volume '
                                        'sizes.',
                              'question': 'What file system is standard for Windows system hard drives and SSDs?'}],
        'order': 2,
        'quizzes': [   {   'correctAnswer': 'Device Manager (devmgmt.msc)',
                           'explanation': 'Device Manager (devmgmt.msc) provides a centralized tree view of all '
                                          'hardware installed on the computer and allows technicians to install, '
                                          'update, enable, or disable device drivers.',
                           'options': [   'Device Manager (devmgmt.msc)',
                                          'Disk Cleanup (cleanmgr.exe)',
                                          'Task Scheduler (taskschd.msc)',
                                          'Event Viewer (eventvwr.msc)'],
                           'question': 'Which Windows administrative utility is used to view, enable, disable, and '
                                       'update drivers for all installed hardware devices?'},
                       {   'correctAnswer': "'Delete' moves the file to the Recycle Bin, while 'Shift + Delete' "
                                            'permanently deletes it bypassing the Recycle Bin',
                           'explanation': 'Pressing Delete sends the file to the Recycle Bin where it can be restored. '
                                          'Pressing Shift + Delete bypasses the Recycle Bin and deletes the file '
                                          'directly from the filesystem.',
                           'options': [   "'Delete' moves the file to the Recycle Bin, while 'Shift + Delete' "
                                          'permanently deletes it bypassing the Recycle Bin',
                                          "'Shift + Delete' creates an encrypted backup copy before deletion",
                                          "'Delete' removes the file permanently, while 'Shift + Delete' moves it to "
                                          'the Recycle Bin',
                                          'Both commands perform the exact same action'],
                           'question': "In the Windows GUI, what is the key difference between pressing 'Delete' "
                                       "versus pressing 'Shift + Delete' on a selected file?"},
                       {   'correctAnswer': 'Ctrl + Shift + Esc',
                           'explanation': 'Ctrl + Shift + Esc directly opens Windows Task Manager immediately. Ctrl + '
                                          'Alt + Del opens the Windows GINA/security options screen.',
                           'options': ['Ctrl + Shift + Esc', 'Ctrl + Alt + Delete', 'Alt + F4', 'Windows Key + Tab'],
                           'question': 'Which keyboard shortcut directly opens Windows Task Manager without passing '
                                       'through the security lock screen?'},
                       {   'correctAnswer': 'The device has a hardware conflict, missing driver, or is malfunctioning',
                           'explanation': 'A yellow exclamation mark indicates that the operating system has detected '
                                          'the hardware but cannot operate it properly due to a missing driver, '
                                          'corrupted driver, or resource conflict.',
                           'options': [   'The device has a hardware conflict, missing driver, or is malfunctioning',
                                          'The device is operating at maximum gigabit speed',
                                          'The device is currently sharing files across the network',
                                          'The device is powered off by the power supply'],
                           'question': 'What is indicated in Device Manager when a hardware component has a yellow '
                                       'exclamation mark icon next to its name?'},
                       {   'correctAnswer': 'System Properties',
                           'explanation': "'sysdm.cpl' opens the System Properties dialog box, which contains the "
                                          'Computer Name, Hardware, Advanced, System Protection, and Remote tabs.',
                           'options': ['System Properties', 'Network Connections', 'Internet Options', 'User Accounts'],
                           'question': "Which Windows command dialog tool can be launched via 'sysdm.cpl' to inspect "
                                       'and change the computer name and workgroup membership?'}],
        'title': 'Lab 2: Be able to operate under supervision the Windows Operating System and its Components'},
    {   'codeSnippet': '# Windows Command Prompt: Network Diagnostics & Configuration\n'
                       '\n'
                       '# 1. Display full IP configuration, MAC address, and DNS servers:\n'
                       'ipconfig /all\n'
                       '\n'
                       '# 2. Release and renew dynamic DHCP IP address:\n'
                       'ipconfig /release\n'
                       'ipconfig /renew\n'
                       '\n'
                       '# 3. Test Layer 3 connectivity to local default gateway and remote host:\n'
                       'ping 192.168.1.1\n'
                       'ping 8.8.8.8\n'
                       '\n'
                       '# 4. Trace the hop-by-hop network routing path to a destination host:\n'
                       'tracert google.com\n'
                       '\n'
                       "# 5. Display the local computer's IP routing table:\n"
                       'route print\n'
                       '\n'
                       '# 6. Inspect the local Address Resolution Protocol (ARP) cache:\n'
                       'arp -a',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 3: Practicing the basics of Networking and Routing\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Practicing the basics of Networking and Routing** | **CLO-1** | '
                   '**PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the concept of computer networks, LAN topologies, and transmission media.\n'
                   '* Learn the structure of IPv4 addressing: IP address, Subnet Mask, Default Gateway, and DNS '
                   'servers.\n'
                   '* Configure static and dynamic (DHCP) IP addressing on Windows network interface cards (NICs).\n'
                   '* Utilize essential Windows CLI network diagnostic commands: `ipconfig`, `ping`, and `tracert`.\n'
                   '* Understand the role of routers in interconnecting disparate networks and directing IP packets.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   'A **Computer Network** is a telecommunications system that allows computers to exchange data and '
                   'share hardware resources (printers, storage) and software services.\n'
                   '\n'
                   '![Networking Architecture](assets/images/university/itc/lab3_networking.png)\n'
                   '\n'
                   '#### 1. Network Classifications:\n'
                   '* **Local Area Network (LAN):** Interconnects computers within a limited geographical area (e.g., '
                   'a university computer lab, office, or single building).\n'
                   '* **Wide Area Network (WAN):** Spans large geographical regions (cities, countries, continents), '
                   'often connecting multiple LANs via telecom carriers (e.g., the Internet).\n'
                   '\n'
                   '#### 2. Network Transmission Media:\n'
                   '* **Unshielded Twisted Pair (UTP):** Most common LAN cable (Cat 5e/Cat 6), terminating in RJ-45 '
                   'modular connectors with a maximum segment distance of 100 meters.\n'
                   '* **Optical Fiber:** Uses pulses of light transmitted through glass cores, immune to '
                   'electromagnetic interference (EMI), ideal for high-speed campus backbones.\n'
                   '* **Wireless (Wi-Fi):** Uses radio frequency signals (IEEE 802.11 a/b/g/n/ac/ax) to connect mobile '
                   'hosts via Wireless Access Points (WAPs).\n'
                   '\n'
                   '#### 3. IPv4 Addressing Essentials:\n'
                   'An IPv4 address is a 32-bit logical address formatted as four decimal octets separated by dots '
                   '(e.g., `192.168.1.50`).\n'
                   '\n'
                   '![TCP/IP Configuration](assets/images/university/itc/lab3_tcp_ip_config.png)\n'
                   '\n'
                   '* **IP Address:** Identifies the unique host interface on the network.\n'
                   '* **Subnet Mask:** Delineates which bits of the IP address belong to the Network ID (NetID) and '
                   'which belong to the Host ID (HostID) (e.g., `255.255.255.0` for a /24 subnet).\n'
                   '* **Default Gateway:** The IP address of the local router interface that forwards packets destined '
                   'for remote networks or the Internet.\n'
                   '* **DNS Server (Domain Name System):** Translates human-readable domain names (e.g., '
                   '`www.hamdard.edu.pk`) into machine-routable IP addresses.\n'
                   '\n'
                   '![IP Details](assets/images/university/itc/lab3_ip_details.png)\n'
                   '\n'
                   '#### 4. The Role of a Router:\n'
                   'A **Router** is a Layer 3 internetworking device that examines incoming IP packet destination '
                   'headers, consults its internal routing table, and determines the optimal path to forward packets '
                   'between different subnets.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Locating Network Adapters:**\n'
                   '   * Open *Network Connections* by typing `ncpa.cpl` in the Run dialog.\n'
                   '   * Right-click on *Ethernet* or *Wi-Fi* adapter, select *Properties*, and select *Internet '
                   'Protocol Version 4 (TCP/IPv4)*.\n'
                   '2. **Inspecting Configuration via Command Prompt:**\n'
                   '   * Launch Command Prompt (`cmd.exe`).\n'
                   '   * Execute `ipconfig /all` to view physical MAC address, IPv4 address, subnet mask, default '
                   'gateway, and DHCP server.\n'
                   '3. **Testing Local & Remote Connectivity via Ping:**\n'
                   '   * Test the local TCP/IP protocol stack: `ping 127.0.0.1` (Loopback address).\n'
                   '   * Test local network connectivity: `ping <Default_Gateway_IP>`.\n'
                   '   * Test Internet connectivity: `ping 8.8.8.8` (Google public DNS).\n'
                   '4. **Tracing Route Hops via Tracert:**\n'
                   '   * Execute `tracert google.com`. Observe each intermediary router hop, latency, and TTL '
                   'decrement.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   "1. Execute `ipconfig /all` in Command Prompt. Record your computer's Physical (MAC) Address, IPv4 "
                   'Address, Subnet Mask, Default Gateway, and DNS Server.\n'
                   "2. Perform a ping test to your neighbor's computer IP address and the laboratory default gateway. "
                   'Record the round-trip times (RTT) and packet loss percentage.\n'
                   '3. Run `tracert www.hamdard.edu.pk`. Count how many router hops the packet traverses from the lab '
                   'PC to the web server.\n'
                   '4. Explain the operational difference between a Layer 2 Switch (which operates on MAC addresses '
                   'within a LAN) and a Layer 3 Router (which routes between IP subnets).',
        'flashcards': [   {   'answer': 'The Subnet Mask separates the 32-bit IPv4 address into its Network ID (NetID) '
                                        'portion and Host ID (HostID) portion, allowing devices to determine if a '
                                        'destination is local or remote.',
                              'question': 'What is the function of the Subnet Mask?'},
                          {   'answer': 'DNS translates human-friendly alphanumeric domain names (e.g. www.google.com) '
                                        'into numerical IP addresses (e.g. 142.250.190.46) required for routing.',
                              'question': 'What service does the Domain Name System (DNS) provide?'},
                          {   'answer': 'ICMP (Internet Control Message Protocol), specifically ICMP Echo Request '
                                        '(Type 8) and ICMP Echo Reply (Type 0).',
                              'question': "What protocol utility is used by the 'ping' command?"},
                          {   'answer': 'A Switch operates at Layer 2 (Data Link) forwarding frames within the same '
                                        'local network using MAC addresses. A Router operates at Layer 3 (Network) '
                                        'forwarding packets between different networks using IP addresses.',
                              'question': 'What is the key functional difference between a network switch and a '
                                          'router?'}],
        'order': 3,
        'quizzes': [   {   'correctAnswer': 'ipconfig /all',
                           'explanation': "The 'ipconfig /all' command displays detailed configuration values for all "
                                          'network adapters, including MAC address, IP address, subnet mask, default '
                                          'gateway, lease times, and DNS servers.',
                           'options': ['ipconfig /all', 'netstat -a', 'ping -t', 'tracert'],
                           'question': 'Which Windows command displays the complete network configuration, including '
                                       'the physical MAC address, DHCP server, and DNS servers?'},
                       {   'correctAnswer': 'To route traffic destined for external networks outside the local subnet',
                           'explanation': 'The default gateway is the local router interface that receives and '
                                          'forwards packets destined for IP addresses located outside the local '
                                          'subnet.',
                           'options': [   'To route traffic destined for external networks outside the local subnet',
                                          'To assign dynamic IP addresses automatically to local hosts',
                                          'To convert digital signals into analog telephone frequencies',
                                          'To protect the computer from software viruses'],
                           'question': "What is the primary function of the Default Gateway in a computer's TCP/IP "
                                       'network configuration?'},
                       {   'correctAnswer': '127.0.0.1',
                           'explanation': '127.0.0.1 is the IPv4 loopback address. Pinging 127.0.0.1 verifies that the '
                                          'local TCP/IP network protocol stack is installed and functioning properly '
                                          'without sending packets onto the physical network wire.',
                           'options': ['127.0.0.1', '192.168.1.1', '0.0.0.0', '255.255.255.255'],
                           'question': 'Which IPv4 address is universally reserved for testing the internal TCP/IP '
                                       'software stack (Loopback test)?'},
                       {   'correctAnswer': 'tracert',
                           'explanation': "The 'tracert' (traceroute) utility uses ICMP Echo packets with incrementing "
                                          'Time-To-Live (TTL) values to map and report every router hop traversed to '
                                          'reach a destination host.',
                           'options': ['tracert', 'ping', 'nslookup', 'arp'],
                           'question': 'What network diagnostic utility sends ICMP Echo Request packets and traces '
                                       'every intermediary router hop along the path to a destination host?'},
                       {   'correctAnswer': 'RJ-45',
                           'explanation': 'The RJ-45 (Registered Jack 45) 8P8C modular connector is the standard '
                                          'connector used with twisted-pair Ethernet cables in local area networks.',
                           'options': ['RJ-45', 'RJ-11', 'BNC', 'ST connector'],
                           'question': 'Which transmission media connector is standard for terminating Cat 5e and Cat '
                                       '6 Unshielded Twisted Pair (UTP) Ethernet network cables?'}],
        'title': 'Lab 3: Practicing the basics of Networking and Routing'},
    {   'codeSnippet': '# Microsoft Word Keyboard Shortcuts & Document Formatting Reference\n'
                       '\n'
                       '# Essential File & Navigation Shortcuts:\n'
                       '# Ctrl + N  : Create a new blank document\n'
                       '# Ctrl + O  : Open an existing document\n'
                       '# Ctrl + S  : Save active document (Save / Save As)\n'
                       '# Ctrl + P  : Open Print dialog and preview\n'
                       '\n'
                       '# Typography & Character Formatting:\n'
                       '# Ctrl + B  : Toggle Bold font style\n'
                       '# Ctrl + I  : Toggle Italic font style\n'
                       '# Ctrl + U  : Toggle Underline font style\n'
                       '# Ctrl + [  : Decrease font size by 1 point\n'
                       '# Ctrl + ]  : Increase font size by 1 point\n'
                       '\n'
                       '# Paragraph Alignment & Structure:\n'
                       '# Ctrl + L  : Left align paragraph\n'
                       '# Ctrl + E  : Center align paragraph\n'
                       '# Ctrl + R  : Right align paragraph\n'
                       '# Ctrl + J  : Justify paragraph text evenly\n'
                       '# Ctrl + Enter : Insert Page Break',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 4: Imitate Microsoft Word\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Imitate Microsoft Word** | **CLO-1** | **PLO-1** | **P3 (Guided '
                   'Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the architecture of Microsoft Word: Quick Access Toolbar, Ribbon system, Tabs, '
                   'Groups, and Status Bar.\n'
                   '* Master text entry, selection techniques, and typography formatting: fonts, sizes, styles (Bold, '
                   'Italic, Underline), and colors.\n'
                   '* Apply paragraph formatting: text alignments (Left, Center, Right, Justify), line spacing, and '
                   'bulleted/numbered lists.\n'
                   '* Design structured documents with headers, footers, page numbering, page margins, and table '
                   'insertions.\n'
                   '* Produce a professional Curriculum Vitae (CV) or technical lab report adhering to standard '
                   'academic document formatting.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   '**Microsoft Word** is a full-featured word processing application developed by Microsoft. It '
                   'provides tools for creating, formatting, editing, and printing text documents ranging from simple '
                   'memos to comprehensive academic dissertations.\n'
                   '\n'
                   '![Word Ribbon System](assets/images/university/itc/lab4_word_ribbon.png)\n'
                   '\n'
                   '#### 1. The Ribbon Interface Structure:\n'
                   'The Ribbon organizes commands into logical categories across several primary tabs:\n'
                   '* **Home Tab:** Holds the most frequently used commands divided into groups: Clipboard, Font, '
                   'Paragraph, Styles, and Editing.\n'
                   '* **Insert Tab:** Allows users to insert external elements: Tables, Pictures, Shapes, SmartArt, '
                   'Header & Footer, Page Numbers, and Text Boxes.\n'
                   '* **Page Layout (Layout) Tab:** Controls page setup parameters: Margins (Normal, Narrow, Wide), '
                   'Orientation (Portrait vs. Landscape), Page Size (A4, Letter), and Multi-column layouts.\n'
                   '\n'
                   '![Page Setup Margins](assets/images/university/itc/lab4_word_margins.png)\n'
                   '![Page Orientation](assets/images/university/itc/lab4_word_orientation.png)\n'
                   '\n'
                   '#### 2. Typography & Character Formatting:\n'
                   '* **Font Family:** Standard professional fonts include Times New Roman, Calibri, Arial, and '
                   'Garamond.\n'
                   '* **Font Size:** Standard body text is typically 11 pt or 12 pt; section headings are typically 14 '
                   'pt or 16 pt bold.\n'
                   '* **Font Styles:** Bold (`Ctrl+B`) for emphasis, Italic (`Ctrl+I`) for citations/terms, Underline '
                   '(`Ctrl+U`) for hyperlinks or headings.\n'
                   '* **Subscript & Superscript:** For chemical formulas (H2O) and mathematical powers (X^2).\n'
                   '\n'
                   '#### 3. Paragraph Formatting & Alignment:\n'
                   '\n'
                   '![Paragraph Alignment](assets/images/university/itc/lab4_word_alignment.png)\n'
                   '\n'
                   '* **Left Align (`Ctrl+L`):** Standard alignment for English text; left margin is flush while right '
                   'margin is ragged.\n'
                   '* **Center Align (`Ctrl+E`):** Used primarily for titles, cover pages, and table headings.\n'
                   '* **Right Align (`Ctrl+R`):** Used for dates, signatures, or right-to-left languages.\n'
                   '* **Justify (`Ctrl+J`):** Spaces words evenly so both left and right margins align straight '
                   'against the margins, standard for textbooks and formal reports.\n'
                   '* **Line Spacing:** Standard spacing is 1.15 or 1.5 lines with 6 pt space after paragraphs.\n'
                   '\n'
                   '![Bulleted & Numbered Lists](assets/images/university/itc/lab4_word_bullets_numbers.png)\n'
                   '\n'
                   '#### 4. Tables in Microsoft Word:\n'
                   'Tables present tabular data organized in horizontal rows and vertical columns. Users can merge '
                   'cells, split cells, apply borders, shade cells, and format column widths proportionally.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Document Setup:**\n'
                   '   * Launch Microsoft Word. Select *Blank document*.\n'
                   '   * Navigate to the *Layout* tab. Set Margins to *Normal* (1 inch top, bottom, left, right). Set '
                   'Paper Size to *A4*.\n'
                   '2. **Headers, Footers & Page Numbering:**\n'
                   '   * Navigate to the *Insert* tab -> *Header*. Choose *Blank (Three Columns)*.\n'
                   "   * Enter 'Hamdard University' on the left and 'Intro to computing' on the right.\n"
                   '   * Insert Page Number at *Bottom of Page* -> *Plain Number 3* (bottom right).\n'
                   '3. **Creating a Formatted Curriculum Vitae (CV):**\n'
                   '   * Insert your full name as Title (Font: Calibri, 20 pt, Bold, Center aligned).\n'
                   '   * Insert contact details (Email, Phone, Address) in 10 pt centered.\n'
                   '   * Insert horizontal line separator.\n'
                   '   * Create Section Headings: *Career Objective*, *Education*, *Technical Skills*, *Projects*, '
                   '*Achievements* (Font: 14 pt, Bold, Left aligned, Shaded background).\n'
                   '4. **Inserting an Academic Credentials Table:**\n'
                   '   * Go to *Insert* -> *Table* -> Insert a 5-row by 4-column table.\n'
                   '   * Enter headers: *Degree/Certificate*, *Institution*, *Year*, *Grade/CGPA*.\n'
                   '   * Format table header row with bold text and light gray fill.\n'
                   '5. **Spell Checking and Saving:**\n'
                   '   * Press `F7` to run the Spelling and Grammar checker.\n'
                   '   * Save the file as `StudentName_CV.docx` (`Ctrl + S`).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create a professional two-page Curriculum Vitae (CV) in Microsoft Word following the exact '
                   'formatting guidelines practiced in this lab.\n'
                   '2. Ensure the document includes a formal header, page numbers in footer, justified paragraph text, '
                   'bulleted skill lists, and a formatted academic qualifications table.\n'
                   '3. Insert a professional passport-size photograph into the top right corner of the CV, setting its '
                   'text wrapping to *Square* or *Tight*.\n'
                   '4. Export and save the completed document in both `.docx` and `.pdf` formats.',
        'flashcards': [   {   'answer': 'Portrait orientation positions the page vertically (height greater than '
                                        'width), which is standard for letters and reports. Landscape orientation '
                                        'positions the page horizontally (width greater than height), ideal for wide '
                                        'tables and diagrams.',
                              'question': 'What is the difference between Portrait and Landscape orientation?'},
                          {   'answer': 'Format Painter allows you to copy all formatting (font, size, color, '
                                        'paragraph spacing) from one piece of text and apply it quickly to another '
                                        'selection.',
                              'question': 'What is the function of the Format Painter tool in Microsoft Word?'},
                          {   'answer': 'The F7 function key launches the Spelling and Grammar pane.',
                              'question': 'What keyboard shortcut activates the Spelling & Grammar check in Word?'},
                          {   'answer': 'A bulleted list is used when item order is not sequential or hierarchical. A '
                                        'numbered list is used for ordered sequences, steps, priorities, or rankings.',
                              'question': 'What is the difference between a bulleted list and a numbered list?'}],
        'order': 4,
        'quizzes': [   {   'correctAnswer': 'Justify (Ctrl + J)',
                           'explanation': 'Justify (Ctrl + J) adjusts the spacing between words so that text flushes '
                                          'evenly against both the left and right margins, producing a clean and '
                                          'formal appearance typical of newspapers and books.',
                           'options': [   'Justify (Ctrl + J)',
                                          'Align Left (Ctrl + L)',
                                          'Center (Ctrl + E)',
                                          'Align Right (Ctrl + R)'],
                           'question': 'Which paragraph alignment setting in Microsoft Word distributes text evenly '
                                       'between both the left and right margins to create clean, flush edges?'},
                       {   'correctAnswer': 'Layout (Page Layout)',
                           'explanation': 'The Layout (or Page Layout) tab contains the Page Setup group, which '
                                          'provides controls for Margins, Orientation (Portrait/Landscape), Size, '
                                          'Columns, and Breaks.',
                           'options': ['Layout (Page Layout)', 'Insert', 'Home', 'Review'],
                           'question': 'Which tab on the Microsoft Word Ribbon contains tools for adjusting Page '
                                       'Margins, Orientation, and Paper Size?'},
                       {   'correctAnswer': 'Ctrl + Enter',
                           'explanation': 'Pressing Ctrl + Enter inserts a page break immediately, advancing '
                                          'subsequent text to the top of the next page.',
                           'options': ['Ctrl + Enter', 'Shift + Enter', 'Alt + Enter', 'Ctrl + Shift + Enter'],
                           'question': 'Which keyboard shortcut immediately inserts a hard Page Break at the current '
                                       'cursor position in Microsoft Word?'},
                       {   'correctAnswer': '.docx',
                           'explanation': "Modern versions of Microsoft Word use the OpenXML-based '.docx' file format "
                                          "as default, replacing the legacy binary '.doc' format.",
                           'options': ['.docx', '.doc', '.txt', '.rtf'],
                           'question': 'In Microsoft Word, what is the default file format extension for documents '
                                       'created in modern versions (2007 through 2026)?'},
                       {   'correctAnswer': 'Header & Footer',
                           'explanation': 'Headers appear in the top margin of every page, and Footers appear in the '
                                          'bottom margin, commonly used for document titles, page numbers, and dates.',
                           'options': ['Header & Footer', 'Footnotes & Endnotes', 'Watermark', 'Text Box'],
                           'question': 'Which feature in Microsoft Word automatically displays information such as the '
                                       'author, document title, or page number at the top or bottom of every page?'}],
        'title': 'Lab 4: Imitate Microsoft Word'},
    {   'codeSnippet': '# Microsoft Excel Spreadsheet Structure & Navigation Reference\n'
                       '\n'
                       '# Workbook Hierarchy:\n'
                       '# Workbook (File .xlsx) -> Worksheets (Sheets) -> Rows & Columns -> Cells\n'
                       '\n'
                       '# Grid Dimensions in Excel 2016 / 2019 / 365:\n'
                       '# Maximum Rows    : 1,048,576 rows (numbered 1, 2, 3...)\n'
                       '# Maximum Columns : 16,384 columns (labeled A, B... Z, AA... XFD)\n'
                       '\n'
                       '# Cell Addressing Syntax:\n'
                       '# [Column Letter][Row Number]  e.g., A1, B12, Z100, AA5\n'
                       '\n'
                       '# Essential Excel Navigation Shortcuts:\n'
                       '# Arrow Keys    : Move one cell Up, Down, Left, or Right\n'
                       '# Tab           : Move one cell to the Right\n'
                       '# Enter         : Move one cell Down\n'
                       '# Shift + Tab   : Move one cell to the Left\n'
                       '# Shift + Enter : Move one cell Up\n'
                       '# Ctrl + Home   : Jump immediately to cell A1\n'
                       '# Ctrl + End    : Jump to the last active cell containing data',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 5: Imitate Microsoft Excel\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Imitate Microsoft Excel** | **CLO-1** | **PLO-1** | **P3 (Guided '
                   'Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the fundamental concepts of spreadsheets: Workbooks, Worksheets, Rows, Columns, and '
                   'Cells.\n'
                   '* Navigate the Excel interface: Name Box, Formula Bar, Sheet Tabs, and Gridlines.\n'
                   '* Understand cell data types: Labels (Text), Values (Numbers), Dates, and Formulas.\n'
                   '* Apply basic cell formatting: fonts, fill colors, cell borders, alignment, text wrap, and merge & '
                   'center.\n'
                   '* Format numerical data: Currency, Percentage, Decimals, and Dates.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   '**Microsoft Excel** is a powerful spreadsheet application used for data entry, financial '
                   'accounting, numerical analysis, mathematical computation, and graphical representation of tabular '
                   'data.\n'
                   '\n'
                   '![Excel Formatted Cells](assets/images/university/itc/lab5_excel_formatted_cells.png)\n'
                   '\n'
                   '#### 1. Spreadsheet Architecture:\n'
                   '* **Workbook:** An Excel document file (with `.xlsx` extension) that holds one or more individual '
                   'worksheets.\n'
                   '* **Worksheet:** A two-dimensional grid of vertical columns (labeled with letters A through XFD) '
                   'and horizontal rows (numbered 1 through 1,048,576).\n'
                   '* **Cell:** The intersection of a row and a column. Each cell possesses a unique coordinate '
                   'address known as the **Cell Reference** (e.g., `C5` represents the cell in column C and row 5).\n'
                   '* **Active Cell:** The currently selected cell outlined with a thick border; its address is '
                   'displayed in the **Name Box**.\n'
                   '* **Formula Bar:** Displays the actual contents, text, or underlying formula of the currently '
                   'selected cell.\n'
                   '\n'
                   '#### 2. Cell Data Types & Default Alignment:\n'
                   '* **Text (Labels):** Any alphanumeric string (e.g., `Employee Name`, `Item A`). By default, Excel '
                   'aligns text to the **left** of the cell.\n'
                   '* **Numbers (Values):** Numerical values used in calculations (e.g., `5000`, `45.75`). By default, '
                   'Excel aligns numbers to the **right** of the cell.\n'
                   '* **Dates & Times:** Stored internally as serial numbers (counting days since January 1, 1900). '
                   'Aligns to the **right**.\n'
                   '* **Boolean (Logical):** `TRUE` or `FALSE`. Centered by default.\n'
                   '\n'
                   '![Borders and Gridlines](assets/images/university/itc/lab5_excel_borders_grid.png)\n'
                   '\n'
                   '#### 3. Cell Formatting & Layout Tools:\n'
                   '* **Merge & Center:** Combines two or more adjacent selected cells into a single larger cell and '
                   'centers the contents, commonly used for table titles.\n'
                   '* **Wrap Text:** Displays multi-line text within a cell without increasing column width.\n'
                   '* **Column Width & Row Height:** Adjusts cell dimensions to prevent text truncation (`###` error '
                   'appears when numbers exceed column width).\n'
                   '\n'
                   '![Adjusting Column Width](assets/images/university/itc/lab5_excel_column_width.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Creating a New Workbook:**\n'
                   '   * Launch Microsoft Excel. Select *Blank workbook*. Rename `Sheet1` to `Inventory_2026`.\n'
                   '2. **Entering Table Titles & Headers:**\n'
                   '   * In cell `A1`, type: `HAMDARD UNIVERSITY COMPUTER LAB INVENTORY`.\n'
                   '   * Select cells `A1:F1`. Click *Merge & Center* on the Home tab. Set Font to 14 pt, Bold, Fill '
                   'Color: Dark Blue, Font Color: White.\n'
                   '   * In row 3, enter column headers: `A3: Item ID`, `B3: Item Description`, `C3: Category`, `D3: '
                   'Quantity`, `E3: Unit Price`, `F3: Total Cost`.\n'
                   '3. **Populating Sample Data:**\n'
                   '   * Enter 5 rows of computer lab inventory items (e.g., Optical Mouse, Mechanical Keyboard, '
                   '24-inch LCD Monitor, Core i7 Desktop PC, Cat6 Patch Cable).\n'
                   '4. **Applying Number Formatting:**\n'
                   '   * Select the Unit Price column (`E4:E8`). On the Home tab -> Number group, click the '
                   '*Accounting / Currency* format symbol (`$`). Set to 2 decimal places.\n'
                   '   * Ensure quantities are formatted as integer numbers with zero decimal places.\n'
                   '5. **Applying Borders:**\n'
                   '   * Select the entire table range `A3:F8`. Click *Borders* -> *All Borders*.\n'
                   '   * Apply a *Thick Outside Border* around the perimeter.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create an Excel workbook named `Lab5_Student_Record.xlsx`. Structure a worksheet containing '
                   'student exam records with fields: *Roll No*, *Student Name*, *Department*, *Attendance '
                   'Percentage*, *Midterm Marks*, *Final Marks*.\n'
                   '2. Enter records for at least 8 students. Apply appropriate data formatting (e.g. Percentage '
                   'format for attendance, integers for marks).\n'
                   '3. Apply professional visual formatting: custom header colors, cell borders, text wrapping for '
                   'long headers, and adjusted column widths so no text is truncated.\n'
                   '4. Explain why numbers align to the right by default in Excel cells while text strings align to '
                   'the left.',
        'flashcards': [   {   'answer': '1,048,576 rows (numbered 1 to 1048576) and 16,384 columns (labeled A through '
                                        'XFD).',
                              'question': 'What is the maximum number of rows and columns available in a modern Excel '
                                          'worksheet?'},
                          {   'answer': 'A Workbook is the entire file (.xlsx) which can contain multiple individual '
                                        'sheets. A Worksheet is a single spreadsheet tab within the workbook composed '
                                        'of a row/column grid.',
                              'question': 'What is the difference between a Workbook and a Worksheet in Excel?'},
                          {   'answer': 'The Formula Bar displays the underlying data, text, or formula entered into '
                                        'the active cell, allowing users to view and edit formulas directly.',
                              'question': 'What is the purpose of the Formula Bar?'},
                          {   'answer': 'Wrap Text allows extra-long text within a cell to wrap across multiple lines '
                                        'by increasing the row height, keeping the text visible without expanding '
                                        'column width.',
                              'question': "What does the 'Wrap Text' feature do?"}],
        'order': 5,
        'quizzes': [   {   'correctAnswer': 'D10',
                           'explanation': 'Cell addresses in Excel specify the column letter first followed by the row '
                                          "number. The fourth column is 'D' and the tenth row is '10', resulting in "
                                          "the cell reference 'D10'.",
                           'options': ['D10', '10D', 'C10', 'D9'],
                           'question': 'What is the unique address of a cell located at the intersection of the fourth '
                                       'column and tenth row in Microsoft Excel?'},
                       {   'correctAnswer': 'Numbers align to the right, and text aligns to the left',
                           'explanation': 'By default in Excel, text entries align to the left edge of a cell, while '
                                          'numbers, currencies, and dates align to the right edge to facilitate '
                                          'vertical decimal alignment.',
                           'options': [   'Numbers align to the right, and text aligns to the left',
                                          'Numbers align to the left, and text aligns to the right',
                                          'Both numbers and text align to the center',
                                          'Both numbers and text align to the left'],
                           'question': 'By default, how does Microsoft Excel horizontally align numeric values versus '
                                       'text labels within a cell?'},
                       {   'correctAnswer': 'The column width is too narrow to display the formatted number completely',
                           'explanation': 'A string of hash symbols (###) indicates that the column is too narrow to '
                                          'display the complete numerical or date value. Double-clicking the column '
                                          'header boundary auto-fits the column to resolve it.',
                           'options': [   'The column width is too narrow to display the formatted number completely',
                                          'A mathematical division by zero error occurred',
                                          'The formula references a deleted cell',
                                          'The user entered invalid text into a numeric field'],
                           'question': "What does a sequence of hash symbols (e.g., '#######') displayed inside an "
                                       'Excel cell indicate?'},
                       {   'correctAnswer': 'Name Box',
                           'explanation': 'The Name Box, located to the left of the Formula Bar, displays the cell '
                                          'reference (e.g., A1) of the currently selected active cell or named range.',
                           'options': ['Name Box', 'Formula Bar', 'Status Bar', 'Title Bar'],
                           'question': 'Which interface element in Microsoft Excel displays the cell address of the '
                                       'currently active cell?'},
                       {   'correctAnswer': 'Merge & Center',
                           'explanation': "'Merge & Center' joins two or more adjacent cells into one unified cell and "
                                          'centers the content, commonly utilized for worksheet and table titles.',
                           'options': ['Merge & Center', 'Wrap Text', 'AutoFit', 'Format Painter'],
                           'question': 'Which Excel feature combines multiple selected adjacent cells into a single '
                                       'large cell and centers the contents horizontally?'}],
        'title': 'Lab 5: Imitate Microsoft Excel'},
    {   'codeSnippet': '# Microsoft Excel Basic Formulas & Mathematical Operators Reference\n'
                       '\n'
                       '# 1. All formulas in Excel MUST begin with an equals sign (=):\n'
                       '# =A1 + B1      (Addition)\n'
                       '# =A1 - B1      (Subtraction)\n'
                       '# =A1 * B1      (Multiplication)\n'
                       '# =A1 / B1      (Division)\n'
                       '# =A1 ^ 2       (Exponentiation)\n'
                       '\n'
                       '# 2. Common Statistical & Aggregate Built-in Functions:\n'
                       '# =SUM(A1:A10)     : Computes total sum of values in range\n'
                       '# =AVERAGE(B1:B10) : Calculates arithmetic mean of values in range\n'
                       '# =MAX(C1:C10)     : Identifies maximum numeric value in range\n'
                       '# =MIN(D1:D10)     : Identifies minimum numeric value in range\n'
                       '# =COUNT(E1:E10)   : Counts number of cells containing numeric values\n'
                       '# =COUNTA(E1:E10)  : Counts non-empty cells (numbers and text)\n'
                       '\n'
                       '# 3. Cell Referencing Types:\n'
                       '# Relative Reference : A1        (changes when formula is copied)\n'
                       '# Absolute Reference : $A$1      (locks both column A and row 1)\n'
                       '# Mixed Reference    : $A1 / A$1 (locks either column or row)',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 6: Practice the basics of Microsoft Excel\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Practice the basics of Microsoft Excel** | **CLO-1** | **PLO-1** | '
                   '**P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the fundamental rule of Excel formulas: all formulas begin with an equal sign (`=`).\n'
                   '* Perform basic arithmetic operations using standard math operators: `+`, `-`, `*`, `/`, and `^`.\n'
                   '* Master essential built-in mathematical and aggregate functions: `=SUM()`, `=AVERAGE()`, '
                   '`=MIN()`, `=MAX()`, and `=COUNT()`.\n'
                   '* Understand the difference between **Relative Cell Referencing** (`A1`) and **Absolute Cell '
                   'Referencing** (`$A$1`).\n'
                   '* Utilize the **AutoFill handle** to replicate formulas and generate continuous data series '
                   'automatically.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   'The primary power of Microsoft Excel lies in its calculation engine. Formulas allow users to '
                   'perform dynamic mathematical computations that automatically recalculate whenever input cell '
                   'values change.\n'
                   '\n'
                   '#### 1. Formula Syntax & Rules:\n'
                   '* **The Equal Sign (`=`):** Instructs Excel that the cell contains an executable formula rather '
                   'than static text.\n'
                   '* **Mathematical Precedence (PEMDAS):** Excel evaluates mathematical operations in standard '
                   'algebraic order: Parentheses `()`, Exponents `^`, Multiplication `*` & Division `/`, Addition `+` '
                   '& Subtraction `-`.\n'
                   '\n'
                   '![AutoSum Button](assets/images/university/itc/lab5_excel_autosum_button.png)\n'
                   '\n'
                   '#### 2. Essential Built-in Functions:\n'
                   '* **`=SUM(range)`:** Adds all numeric values within a specified range (e.g. `=SUM(C2:C20)`).\n'
                   '* **`=AVERAGE(range)`:** Calculates the arithmetic mean (sum divided by count) of numbers in a '
                   'range.\n'
                   '* **`=MAX(range)`:** Returns the highest numerical value in a range.\n'
                   '* **`=MIN(range)`:** Returns the lowest numerical value in a range.\n'
                   '* **`=COUNT(range)`:** Counts how many cells in the range contain numbers.\n'
                   '\n'
                   '![AutoSum Formula](assets/images/university/itc/lab5_excel_autosum_formula.png)\n'
                   '\n'
                   '#### 3. Cell Referencing Types:\n'
                   '* **Relative Referencing (`A1`):** When a formula containing relative references is copied to '
                   'another cell, Excel automatically shifts the row and column coordinates relative to the new '
                   'position (e.g., copying `=A1+B1` from row 1 down to row 2 becomes `=A2+B2`).\n'
                   '* **Absolute Referencing (`$A$1`):** Uses dollar signs (`$`) to lock specific column and row '
                   'coordinates. When copied, the reference remains fixed on that exact cell (e.g., used when '
                   'referencing a tax rate or conversion factor stored in a single cell).\n'
                   '* Pressing the `F4` key while editing a cell reference cycles between Relative, Absolute, and '
                   'Mixed references (`A1` -> `$A$1` -> `A$1` -> `$A1`).\n'
                   '\n'
                   '![AutoFill Feature](assets/images/university/itc/lab5_excel_autofill.png)\n'
                   '\n'
                   '#### 4. The AutoFill Handle:\n'
                   'The small solid green square at the bottom-right corner of the active cell selection is the **Fill '
                   'Handle**. Dragging it copies formulas, increments numeric sequences (1, 2, 3...), days of the week '
                   '(Monday, Tuesday...), and months (January, February...).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Building a Monthly Household Budget Spreadsheet:**\n'
                   '   * In column A, list 6 expense categories: *Rent*, *Groceries*, *Electricity*, *Internet*, '
                   '*Transport*, *Entertainment*.\n'
                   '   * In columns B, C, D, enter expenses for *January*, *February*, and *March*.\n'
                   '2. **Applying Formula Computations:**\n'
                   '   * In cell `E2`, calculate total expense for Rent across 3 months: `=SUM(B2:D2)`.\n'
                   '   * Use the AutoFill handle to drag the formula from `E2` down to `E7` for all expense rows.\n'
                   '   * In cell `F2`, calculate average monthly expense for Rent: `=AVERAGE(B2:D2)`. AutoFill down to '
                   '`F7`.\n'
                   '3. **Computing Column Summaries:**\n'
                   '   * In row 8, compute monthly totals using the *AutoSum* button (`Alt + =`): `=SUM(B2:B7)` in '
                   'cell `B8`. Copy across to columns C, D, and E.\n'
                   '   * In row 9, calculate the highest expense for each month using `=MAX(B2:B7)`.\n'
                   '   * In row 10, calculate the lowest expense for each month using `=MIN(B2:B7)`.\n'
                   '4. **Practicing Absolute Referencing:**\n'
                   '   * In cell `H1`, enter a sales tax rate: `0.15` (15%).\n'
                   '   * In column G, calculate Tax Amount for each category using absolute referencing: `=E2 * '
                   '$H$1`.\n'
                   '   * Copy the formula down and verify that `$H$1` does not change.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create an Excel worksheet named `Lab6_Payroll.xlsx`. Design an employee payroll sheet with '
                   'columns: *Employee ID*, *Name*, *Basic Salary*, *Medical Allowance (15% of Basic)*, *House Rent '
                   '(30% of Basic)*, *Tax (5% of Basic)*, and *Net Salary*.\n'
                   '2. Populate records for 6 employees with varying basic salaries.\n'
                   '3. Use appropriate formulas with cell references to compute *Medical Allowance*, *House Rent*, '
                   '*Tax*, and *Net Salary* (`Net = Basic + Allowances - Tax`).\n'
                   '4. In the summary section at the bottom, calculate *Total Payroll Expense* using `=SUM()`, '
                   '*Average Salary* using `=AVERAGE()`, *Maximum Salary* using `=MAX()`, and *Minimum Salary* using '
                   '`=MIN()`.\n'
                   '5. Explain the consequence if the formula for Tax calculation did not use absolute referencing for '
                   'the tax rate cell.',
        'flashcards': [   {   'answer': 'A Relative Reference (e.g., A1) automatically shifts relative to the target '
                                        'position when copied. An Absolute Reference (e.g., $A$1) uses dollar signs to '
                                        'lock the row and column coordinates permanently.',
                              'question': 'What is the difference between a Relative Reference and an Absolute '
                                          'Reference in Excel?'},
                          {   'answer': 'The small solid square located at the bottom-right corner of an active cell. '
                                        'Dragging it copies formulas, values, or generates progressive sequences '
                                        '(dates, numbers, weekdays).',
                              'question': 'What is the AutoFill Handle in Excel?'},
                          {   'answer': '92, because the MAX function identifies and returns the highest numerical '
                                        'value in the arguments list.',
                              'question': 'What is the result of the formula =MAX(10, 45, 8, 92, 33)?'},
                          {   'answer': 'Alt + = (press Alt and the equals key simultaneously).',
                              'question': 'What keyboard shortcut triggers AutoSum for a selected column or row?'}],
        'order': 6,
        'quizzes': [   {   'correctAnswer': 'Equals sign (=)',
                           'explanation': 'In Microsoft Excel, every formula and function must begin with an equals '
                                          'sign (=) to signal to the calculation engine that the cell contains '
                                          'executable instructions rather than text.',
                           'options': ['Equals sign (=)', 'Plus sign (+)', 'At symbol (@)', 'Asterisk (*)'],
                           'question': 'Every mathematical calculation and built-in function in Microsoft Excel must '
                                       'begin with which character?'},
                       {   'correctAnswer': '=AVERAGE()',
                           'explanation': "The '=AVERAGE()' function calculates the arithmetic mean of the numbers "
                                          'provided as arguments or referenced within a cell range.',
                           'options': ['=AVERAGE()', '=MEAN()', '=MEDIAN()', '=SUM()'],
                           'question': 'Which Excel built-in function computes the arithmetic mean of a selected range '
                                       'of numerical values?'},
                       {   'correctAnswer': '=A2 * $B$1',
                           'explanation': 'A1 is a relative reference, so it shifts down one row to A2. $B$1 is an '
                                          'absolute reference (locked with dollar signs), so it remains fixed on $B$1.',
                           'options': ['=A2 * $B$1', '=A2 * $B$2', '=A1 * $B$1', '=A2 * B2'],
                           'question': "If cell C1 contains the formula '=A1 * $B$1', what does the formula become "
                                       'when copied into cell C2?'},
                       {   'correctAnswer': 'F4',
                           'explanation': 'Pressing the F4 function key while selecting or editing a cell reference in '
                                          'the formula bar cycles between relative (A1), absolute ($A$1), and mixed '
                                          '(A$1, $A1) reference styles.',
                           'options': ['F4', 'F2', 'F9', 'F12'],
                           'question': 'Which keyboard function key toggles through relative, absolute, and mixed cell '
                                       'referencing styles (e.g., A1 -> $A$1 -> A$1 -> $A1)?'},
                       {   'correctAnswer': '=COUNT()',
                           'explanation': "The '=COUNT()' function specifically counts cells in a range that contain "
                                          "numbers. '=COUNTA()' counts all non-empty cells including text, and "
                                          "'=COUNTBLANK()' counts empty cells.",
                           'options': ['=COUNT()', '=COUNTA()', '=COUNTBLANK()', '=SUM()'],
                           'question': 'Which function counts the total number of cells within a specified range that '
                                       'contain numeric values?'}],
        'title': 'Lab 6: Practice the basics of Microsoft Excel'},
    {   'codeSnippet': '# Microsoft Excel Data Analysis, Sorting, Filtering & Chart Types\n'
                       '\n'
                       '# 1. Conditional Logical Functions:\n'
                       '# =IF(Logical_Test, Value_if_True, Value_if_False)\n'
                       '# Example: Determine Pass/Fail status based on passing threshold of 50:\n'
                       '# =IF(E2>=50, \\"Pass\\", \\"Fail\\")\n'
                       '\n'
                       '# 2. Nested Logical Function for Academic Letter Grading:\n'
                       '# =IF(E2>=85, \\"A\\", IF(E2>=75, \\"B\\", IF(E2>=65, \\"C\\", IF(E2>=50, \\"D\\", '
                       '\\"F\\"))))\n'
                       '\n'
                       '# 3. Chart Types & Best Use Cases:\n'
                       '# Column / Bar Chart : Comparing discrete categories (e.g. subject scores)\n'
                       '# Pie Chart          : Showing proportional parts of a whole (100% total)\n'
                       '# Line Chart         : Tracking numerical trends over continuous time\n'
                       '# Scatter Plot       : Observing scientific correlation between two numeric variables',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 7: Imitate Microsoft Excel\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Imitate Microsoft Excel** | **CLO-2** | **PLO-1** | **P3 (Guided '
                   'Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   "* Organize and analyze complex datasets using Excel's **Sort** and **Filter** capabilities.\n"
                   '* Implement conditional logic formulas using the `=IF()` function for decision making.\n'
                   '* Select, insert, and customize visual analytical charts: 2D/3D Clustered Column Charts, Bar '
                   'Charts, and Pie Charts.\n'
                   '* Format chart elements: Chart Title, Axis Titles, Data Labels, Legend, and Chart Styles.\n'
                   '* Construct an end-to-end Student Academic Award List & Grade Sheet containing automated grading, '
                   'rankings, and visual charts.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\\n\n'
                   'Beyond basic calculations, modern business and engineering workflows rely on Microsoft Excel for '
                   'data analysis, decision modeling, and visual reporting.\n'
                   '\n'
                   '#### 1. Sorting & Filtering Datasets:\n'
                   '* **Sorting:** Arranges data rows in a specified order. Can sort alphabetically (A to Z or Z to '
                   'A), numerically (Smallest to Largest or Largest to Smallest), or chronologically. Excel supports '
                   'multi-level sorting (e.g. sort primarily by Department, then secondarily by Salary).\n'
                   '\n'
                   '![Custom Sort Dialog](assets/images/university/itc/lab5_excel_custom_sort.png)\n'
                   '\n'
                   '* **AutoFilter:** Displays dropdown filter arrows in table headers, allowing users to temporarily '
                   "display only rows that satisfy specific criteria (e.g., view only students from 'Electrical "
                   "Engineering' with score > 80).\n"
                   '\n'
                   '#### 2. The Logical `=IF()` Function:\n'
                   'The `=IF()` function tests a logical condition and returns one value if the condition evaluates to '
                   '`TRUE`, and another value if it evaluates to `FALSE`:\n'
                   '```excel\n'
                   '=IF(logical_test, value_if_true, value_if_false)\n'
                   '```\n'
                   'For example: `=IF(TotalMarks >= 50, "Pass", "Fail")`.\n'
                   'Multiple IF functions can be nested to handle complex multi-tier evaluations such as letter grades '
                   '(A, B, C, D, F).\n'
                   '\n'
                   '#### 3. Visual Charts & Graph Representation:\n'
                   'Charts transform complex columns of numbers into intuitive graphical visuals that clearly '
                   'communicate patterns, comparisons, and proportions.\n'
                   '\n'
                   '![Excel Charts Selection](assets/images/university/itc/lab5_excel_charts.png)\n'
                   '\n'
                   '* **Column / Bar Chart:** Uses vertical or horizontal rectangular bars to compare values across '
                   'categories (e.g., comparing student scores across subjects).\n'
                   '* **Pie Chart:** Shows the proportional contribution of each category relative to a 100% total '
                   '(e.g., market share, budget distribution).\n'
                   '* **Line Chart:** Displays data points connected by straight line segments, ideal for showing '
                   'trends over time.\n'
                   '\n'
                   '![Chart Step by Step](assets/images/university/itc/lab5_excel_chart_steps.png)\n'
                   '![Chart Elements Customization](assets/images/university/itc/lab5_excel_chart_elements.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Creating a Comprehensive Student Award List:**\n'
                   '   * Create a worksheet with columns: `Roll No`, `Student Name`, `ITC Theory (100)`, `ITC Lab '
                   '(50)`, `Total (150)`, `Percentage (%)`, `Result (Pass/Fail)`, `Grade`.\n'
                   '   * Enter data for 10 students with realistic exam marks.\n'
                   '2. **Applying Formula Computations:**\n'
                   '   * Compute Total: `=C4 + D4`.\n'
                   '   * Compute Percentage: `=(E4 / 150) * 100`. Format column as number with 2 decimal places.\n'
                   '   * Compute Result using IF: `=IF(F4>=50, "Pass", "Fail")`.\n'
                   '   * Compute Letter Grade using Nested IF:\n'
                   '     `=IF(F4>=80, "A", IF(F4>=70, "B", IF(F4>=60, "C", IF(F4>=50, "D", "F"))))`.\n'
                   '3. **Applying Conditional Formatting:**\n'
                   "   * Highlight students with Grade 'A' using Light Green fill.\n"
                   "   * Highlight students with Result 'Fail' using Light Red fill with dark red text.\n"
                   '4. **Sorting and Filtering:**\n'
                   '   * Apply AutoFilter (`Ctrl + Shift + L`). Filter records to display only students who passed.\n'
                   '   * Sort the list descending by Percentage to rank the students from 1st position downward.\n'
                   '5. **Creating and Customizing Charts:**\n'
                   '   * Select student names and their total percentage columns.\n'
                   '   * Navigate to *Insert* -> *Charts* -> *2-D Clustered Column Chart*.\n'
                   "   * Set Chart Title to 'ITC Class Performance 2026'. Add Axis Titles (Horizontal: 'Students', "
                   "Vertical: 'Percentage (%)').\n"
                   '   * Create a 3D Pie Chart showing the distribution of grades (A, B, C, D, F) across the class.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Complete the Student Award List worksheet in Excel following all computational and conditional '
                   'formatting steps practiced in this lab.\n'
                   '2. Generate a 2D Clustered Column Chart comparing individual student percentages against the class '
                   'average.\n'
                   '3. Generate a Pie Chart displaying the percentage distribution of Letter Grades (A, B, C, D, F) in '
                   'the class, adding Data Labels showing percentages on each slice.\n'
                   '4. Explain the key analytical advantage of a Column Chart over a Pie Chart when presenting '
                   'comparison data with more than 8 discrete categories.',
        'flashcards': [   {   'answer': 'A formula where one IF function is placed inside another IF function as the '
                                        'value_if_true or value_if_false argument, allowing the formula to test '
                                        'multiple hierarchical conditions (e.g. grading scales).',
                              'question': 'What is a Nested IF function in Excel?'},
                          {   'answer': 'Use a Column Chart to compare discrete independent categories (e.g. sales by '
                                        'department, scores by student). Use a Line Chart to display continuous trends '
                                        'over sequential intervals of time (e.g. stock prices, monthly temperature).',
                              'question': 'When should you choose a Column Chart instead of a Line Chart?'},
                          {   'answer': 'The Legend provides a color-coded visual key identifying which data series or '
                                        'category corresponds to each color or pattern displayed on the chart.',
                              'question': 'What is the function of the Chart Legend?'},
                          {   'answer': 'Sorting reorders the rows of a table based on one or more column values (A-Z, '
                                        'Largest to Smallest). Filtering hides rows that do not meet specified '
                                        'criteria while leaving matching rows visible.',
                              'question': 'What is the difference between Sorting and Filtering in Excel?'}],
        'order': 7,
        'quizzes': [   {   'correctAnswer': '=IF(logical_test, value_if_true, value_if_false)',
                           'explanation': 'The Excel IF function accepts three arguments in order: the logical_test '
                                          'condition to evaluate, the value_if_true to return if the condition '
                                          'evaluates to true, and the value_if_false to return if false.',
                           'options': [   '=IF(logical_test, value_if_true, value_if_false)',
                                          '=IF(value_if_true, logical_test, value_if_false)',
                                          '=IF(condition, result)',
                                          '=IF(logical_test THEN value_if_true ELSE value_if_false)'],
                           'question': "What is the correct syntax for an '=IF()' conditional function in Microsoft "
                                       'Excel?'},
                       {   'correctAnswer': 'Pie Chart',
                           'explanation': 'A Pie Chart displays data as proportional slices of a circle representing '
                                          '100% of the total, making it ideal for visualizing demographic shares, '
                                          'budgets, and proportions.',
                           'options': ['Pie Chart', 'Scatter Plot', 'Line Chart', 'Area Chart'],
                           'question': 'Which chart type in Microsoft Excel is best suited for illustrating the '
                                       'proportional percentage contribution of categories to a 100% whole?'},
                       {   'correctAnswer': 'Ctrl + Shift + L',
                           'explanation': 'Pressing Ctrl + Shift + L immediately toggles the AutoFilter dropdown '
                                          'arrows on or off for the active table or selected headers.',
                           'options': ['Ctrl + Shift + L', 'Ctrl + F', 'Alt + F4', 'Ctrl + Shift + F'],
                           'question': 'Which keyboard shortcut toggles the AutoFilter dropdown arrows on and off '
                                       'across the selected table header row in Excel?'},
                       {   'correctAnswer': 'Displays exact numerical values directly on or above chart bars or slices',
                           'explanation': 'Data Labels display the exact numerical data values or percentages directly '
                                          'on the graphical bars, points, or pie slices, allowing viewers to read '
                                          'values without referring back to the axes.',
                           'options': [   'Displays exact numerical values directly on or above chart bars or slices',
                                          'Sets the background gradient color of the chart canvas',
                                          'Rotates the 3D perspective of the chart',
                                          'Deletes all negative values from the chart series'],
                           'question': "What is the primary function of the 'Data Labels' chart element in Microsoft "
                                       'Excel?'},
                       {   'correctAnswer': 'Conditional Formatting',
                           'explanation': 'Conditional Formatting automatically applies visual styling (colors, data '
                                          'bars, icon sets) to cells based on dynamic criteria or threshold rules '
                                          'configured by the user.',
                           'options': ['Conditional Formatting', 'Format Painter', 'Data Validation', 'AutoCorrect'],
                           'question': "Which Excel feature automatically changes a cell's fill color, font style, or "
                                       'border when its value satisfies a specified rule (such as highlighting failing '
                                       'marks below 50 in red)?'}],
        'title': 'Lab 7: Imitate Microsoft Excel'}]

LABS_PART2 = [   {   'codeSnippet': '<!-- Basic HTML5 Document Structure Template -->\n'
                       '<!DOCTYPE html>\n'
                       '<html lang="en">\n'
                       '<head>\n'
                       '    <meta charset="UTF-8">\n'
                       '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                       '    <title>Hamdard University - My First Webpage</title>\n'
                       '</head>\n'
                       '<body>\n'
                       '    <!-- Heading Hierarchy -->\n'
                       '    <h1>Introduction to Computing: Laboratory Work</h1>\n'
                       '    <h2>Department of Computer Science & Engineering</h2>\n'
                       '    <h3>Hamdard Institute of Engineering & Technology (HIET)</h3>\n'
                       '    <hr>\n'
                       '    <!-- Paragraphs and Breaks -->\n'
                       '    <p>HyperText Markup Language (HTML) is the standard markup language for creating Web '
                       'pages.</p>\n'
                       '    <p>HTML describes the structure of a Web page semantically using a series of '
                       'elements.<br>\n'
                       '    Browsers do not display the HTML tags, but use them to render the content of the '
                       'page.</p>\n'
                       '</body>\n'
                       '</html>',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 8: Practicing the basics of HTML\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Practicing the basics of HTML** | **CLO-2** | **PLO-1** | **P3 '
                   '(Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the foundational concept of the World Wide Web (WWW) and HyperText Markup Language '
                   '(HTML).\n'
                   '* Learn the standard skeleton structure of an HTML5 document: `<!DOCTYPE html>`, `<html>`, '
                   '`<head>`, `<title>`, and `<body>`.\n'
                   '* Master the heading hierarchy from `<h1>` (most significant) down to `<h6>` (least significant).\n'
                   '* Utilize paragraph elements `<p>`, line break elements `<br>`, and horizontal rules `<hr>`.\n'
                   '* Author HTML code in a standard text editor (Notepad / VS Code), save as `.html`, and render in '
                   'web browsers (Chrome, Firefox, Edge).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '**HTML (HyperText Markup Language)** is the universal markup language used to structure content on '
                   'the World Wide Web. Unlike programming languages such as C++ or Python, HTML is not a compiled '
                   'procedural language; rather, it uses a system of tags to annotate text, images, and other media '
                   'for web browser rendering.\n'
                   '\n'
                   '#### 1. Anatomy of an HTML Document:\n'
                   'Every valid modern HTML5 web page consists of fundamental structural tags:\n'
                   '* `<!DOCTYPE html>`: The document type declaration that informs the web browser that the document '
                   'is written in HTML5.\n'
                   '* `<html>`: The root container element that encloses all other HTML elements on the page.\n'
                   '* `<head>`: Contains metadata, character encoding declarations (`<meta charset="UTF-8">`), '
                   'external stylesheets, scripts, and the document title.\n'
                   "* `<title>`: Defines the page title displayed in the browser's title bar, tab label, and search "
                   'engine results.\n'
                   '* `<body>`: Contains all visible page contents rendered in the browser viewport (text, headings, '
                   'paragraphs, images, tables, links).\n'
                   '\n'
                   '#### 2. HTML Tags & Elements:\n'
                   'An HTML element typically consists of a **start tag** (`<tagname>`), content, and an **end tag** '
                   '(`</tagname>`):\n'
                   '```html\n'
                   '<p>This is paragraph content.</p>\n'
                   '```\n'
                   '* **Container Tags:** Elements that enclose content and require an explicit closing tag (e.g. '
                   '`<h1>...</h1>`, `<p>...</p>`).\n'
                   '* **Empty (Self-Closing) Tags:** Elements that contain no textual content and do not require '
                   'closing tags: `<br>` (line break) and `<hr>` (thematic horizontal break rule).\n'
                   '\n'
                   '#### 3. Heading Hierarchy (`<h1>` to `<h6>`):\n'
                   'HTML provides six levels of section headings:\n'
                   '* `<h1>`: Main document heading (largest font size, bold, highest SEO importance; typically used '
                   'once per page).\n'
                   '* `<h2>`: Major section heading.\n'
                   '* `<h3>`: Subsection heading.\n'
                   '* `<h4>`, `<h5>`, `<h6>`: Progressively smaller subsidiary headings.\n'
                   '\n'
                   '#### 4. Paragraphs and Line Breaks:\n'
                   '* `<p>`: Defines a block-level paragraph. Web browsers automatically add vertical margin space '
                   '(blank line) before and after paragraph elements.\n'
                   '* `<br>`: Forces an inline line break without inserting extra paragraph margin spacing.\n'
                   '* `<hr>`: Inserts a horizontal rule divider to visually separate distinct thematic topics or '
                   'sections.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Creating an HTML File in a Text Editor:**\n'
                   '   * Launch *Notepad* (or VS Code). Open a new file.\n'
                   '   * Type the standard HTML5 skeleton starting with `<!DOCTYPE html>`.\n'
                   '2. **Structuring Page Headings:**\n'
                   "   * Within the `<body>` element, write an `<h1>` tag with the text 'Welcome to My Academic "
                   "Webpage'.\n"
                   "   * Add an `<h2>` tag titled 'Personal Background' and an `<h3>` tag titled 'Contact Details'.\n"
                   '3. **Adding Paragraphs and Separators:**\n'
                   '   * Insert a paragraph `<p>` describing your degree program at Hamdard University.\n'
                   '   * Use `<br>` within a paragraph to separate your email address and campus address onto distinct '
                   'lines.\n'
                   '   * Insert `<hr>` to create a clean divider between the personal section and academic section.\n'
                   '4. **Saving and Browser Rendering:**\n'
                   '   * In Notepad, click *File* -> *Save As*.\n'
                   '   * Set *Save as type* to *All Files (*.*)*.\n'
                   '   * Name the file `index.html`. Choose UTF-8 encoding. Save into `C:/ITC_Lab/HTML`.\n'
                   '   * Double-click `index.html` to open it in Google Chrome or Microsoft Edge. Inspect the rendered '
                   'output.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create an HTML file named `lab8_basic.html`. Build a structured web page that includes all six '
                   'heading levels (`<h1>` through `<h6>`) demonstrating the hierarchical scale of text.\n'
                   '2. Below each heading, write a short paragraph `<p>` explaining the purpose of that heading '
                   'level.\n'
                   '3. Use horizontal rules `<hr>` between sections and line breaks `<br>` within paragraphs.\n'
                   '4. Right-click in the browser window and select *View Page Source* (`Ctrl + U`). Confirm that your '
                   'raw HTML markup matches the rendered output in the DOM inspector.',
        'flashcards': [   {'answer': 'HyperText Markup Language.', 'question': 'What does the acronym HTML stand for?'},
                          {   'answer': '<head> contains non-visible metadata, title, character encoding, and links to '
                                        'scripts/styles. <body> contains all visible content rendered in the browser '
                                        'window.',
                              'question': 'What is the difference between the <head> and <body> elements in HTML?'},
                          {   'answer': 'It inserts a horizontal rule (thematic break line) across the width of the '
                                        'container, visually separating distinct topics or sections.',
                              'question': 'What does the <hr> tag do in an HTML document?'},
                          {   'answer': 'Browsers collapse multiple consecutive spaces, tabs, and newline characters '
                                        'into a single space. To create an actual line break or extra spacing, '
                                        'developers must use <br>, <p>, or CSS margins.',
                              'question': 'How do web browsers treat whitespace and line returns in raw HTML code?'}],
        'order': 8,
        'quizzes': [   {   'correctAnswer': 'Informs the web browser that the document is written using the HTML5 '
                                            'specification',
                           'explanation': "The '<!DOCTYPE html>' declaration is not an HTML tag; it is an instruction "
                                          'to the web browser declaring that the document adheres to the modern HTML5 '
                                          'standard.',
                           'options': [   'Informs the web browser that the document is written using the HTML5 '
                                          'specification',
                                          'Links an external cascading style sheet (CSS) file',
                                          'Initializes the web server database connection',
                                          'Encrypts the HTML source code for security'],
                           'question': "What is the primary function of the '<!DOCTYPE html>' declaration placed at "
                                       'the very beginning of an HTML document?'},
                       {   'correctAnswer': '<h1>',
                           'explanation': "'<h1>' defines the most important, top-level heading in HTML, typically "
                                          'rendered in the largest font size by default.',
                           'options': ['<h1>', '<head>', '<h6>', '<heading>'],
                           'question': 'Which HTML element represents the most significant, highest-level heading in a '
                                       'document?'},
                       {   'correctAnswer': '<br>',
                           'explanation': "'<br>' (line break) is a void (empty) tag because it inserts a break in "
                                          'text and cannot contain child text or elements, hence requiring no closing '
                                          "'</br>' tag.",
                           'options': ['<br>', '<p>', '<title>', '<body>'],
                           'question': 'Which of the following HTML tags is an empty (void) element that does NOT '
                                       'require an ending closing tag?'},
                       {   'correctAnswer': 'Inside the <head> element',
                           'explanation': "The '<title>' element specifies the title of the document shown in browser "
                                          "tabs and bookmarks, and must reside inside the '<head>' section.",
                           'options': [   'Inside the <head> element',
                                          'Inside the <body> element',
                                          'Directly before the <!DOCTYPE html> declaration',
                                          'Inside the <footer> element'],
                           'question': "Where must the '<title>' element be located within an HTML document "
                                       'structure?'},
                       {   'correctAnswer': '.html or .htm',
                           'explanation': "Web browsers recognize files with the '.html' or '.htm' file extensions as "
                                          'HyperText Markup Language documents and parse them using their HTML '
                                          'rendering engines.',
                           'options': ['.html or .htm', '.txt', '.doc', '.exe'],
                           'question': 'What file extension must be used when saving an HTML source file so that web '
                                       'browsers can properly interpret and render it?'}],
        'title': 'Lab 8: Practicing the basics of HTML'},
    {   'codeSnippet': '<!-- HTML Text Formatting, Lists & Hyperlinks Example -->\n'
                       '<!DOCTYPE html>\n'
                       '<html lang="en">\n'
                       '<head>\n'
                       '    <title>HTML Formatting, Lists & Navigation</title>\n'
                       '</head>\n'
                       '<body>\n'
                       '    <!-- Text Formatting Elements -->\n'
                       '    <p>This is <b>bold</b> text and this is <strong>important strong</strong> text.</p>\n'
                       '    <p>This is <i>italic</i> text and this is <em>emphasized</em> text.</p>\n'
                       "    <p>Scientific notation: Water is H<sub>2</sub>O and Einstein's equation is E = "
                       'mc<sup>2</sup>.</p>\n'
                       '    <hr>\n'
                       '    <!-- Unordered List -->\n'
                       '    <h3>Core Hardware Components (Unordered List):</h3>\n'
                       '    <ul type="square">\n'
                       '        <li>Central Processing Unit (CPU)</li>\n'
                       '        <li>Random Access Memory (RAM)</li>\n'
                       '        <li>Solid State Drive (SSD)</li>\n'
                       '    </ul>\n'
                       '    <!-- Ordered List -->\n'
                       '    <h3>PC Assembly Steps (Ordered List):</h3>\n'
                       '    <ol type="1">\n'
                       '        <li>Install CPU into motherboard socket.</li>\n'
                       '        <li>Mount CPU heatsink and cooling fan.</li>\n'
                       '        <li>Insert RAM modules into DIMM slots.</li>\n'
                       '    </ol>\n'
                       '    <hr>\n'
                       '    <!-- Anchor Hyperlinks -->\n'
                       '    <p>Visit <a href="https://www.hamdard.edu.pk" target="_blank">Hamdard University Official '
                       'Website</a>.</p>\n'
                       '</body>\n'
                       '</html>',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 9: Be able to repeat the basics of HTML\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to repeat the basics of HTML** | **CLO-2** | **PLO-1** | **P3 '
                   '(Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Master HTML text formatting tags: bold `<b>`, strong `<strong>`, italic `<i>`, emphasized '
                   '`<em>`, underline `<u>`, marked `<mark>`, subscript `<sub>`, and superscript `<sup>`.\n'
                   '* Construct unordered bulleted lists using `<ul>` and ordered numbered lists using `<ol>` with '
                   'list item elements `<li>`.\n'
                   '* Create multi-level nested lists.\n'
                   '* Implement anchor hyperlinks using `<a href="...">` to navigate between local HTML files and '
                   'external web URLs.\n'
                   '* Understand the `target="_blank"` attribute for opening links in new browser tabs.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   'Enhancing raw text with semantic formatting, organized lists, and interactive hyperlinks is what '
                   'transforms static text into rich HyperText.\n'
                   '\n'
                   '#### 1. Text Formatting Tags:\n'
                   'HTML defines special elements for formatting text with physical or semantic meaning:\n'
                   '* `<b>`: Renders bold text physically without added semantic importance.\n'
                   '* `<strong>`: Renders bold text with strong semantic importance (interpreted by screen readers as '
                   'emphasized speech).\n'
                   '* `<i>`: Italic text for foreign words, technical terms, or thoughts.\n'
                   '* `<em>`: Emphasized text rendered in italics, carrying semantic stress.\n'
                   '* `<u>`: Underlines text (used sparingly to avoid confusion with hyperlinks).\n'
                   '* `<mark>`: Highlights text with a yellow background marker.\n'
                   '* `<sub>`: Subscript text positioned lower than the baseline with smaller font (e.g. Chemical '
                   'formulas: `H<sub>2</sub>O`).\n'
                   '* `<sup>`: Superscript text positioned higher than the baseline (e.g. Mathematical exponents: '
                   '`X<sup>2</sup>`).\n'
                   '\n'
                   '#### 2. HTML Lists:\n'
                   '* **Unordered Lists (`<ul>`):** Groups items marked with bullets (disc, circle, square):\n'
                   '  ```html\n'
                   '  <ul>\n'
                   '      <li>Item 1</li>\n'
                   '      <li>Item 2</li>\n'
                   '  </ul>\n'
                   '  ```\n'
                   '* **Ordered Lists (`<ol>`):** Groups items marked with sequential numbers or letters (`type="1"`, '
                   '`type="A"`, `type="a"`, `type="I"`, `type="i"`):\n'
                   '  ```html\n'
                   '  <ol type="A">\n'
                   '      <li>First Step</li>\n'
                   '      <li>Second Step</li>\n'
                   '  </ol>\n'
                   '  ```\n'
                   '* **Nested Lists:** A list placed inside a list item `<li>` of another list to create multi-level '
                   'outlines.\n'
                   '\n'
                   '#### 3. Anchor Hyperlinks (`<a>`):\n'
                   'Hyperlinks connect web documents across the Internet using the anchor tag `<a>`:\n'
                   '```html\n'
                   '<a href="https://www.example.com" target="_blank">Click Here</a>\n'
                   '```\n'
                   '* `href` (Hypertext Reference): Specifies the destination URL (web address or relative file path '
                   'like `about.html`).\n'
                   '* `target="_blank"`: Instructs the browser to open the linked document in a new tab or window.\n'
                   '* `target="_self"`: Default behavior; opens the link in the same window/tab.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Practicing Text Formatting:**\n'
                   '   * Create a file named `formatting.html`. Write a paragraph demonstrating `<b>`, `<strong>`, '
                   '`<i>`, `<em>`, `<mark>`, and `<u>`.\n'
                   '   * Write mathematical and chemical formulas: $CO_2$, $H_2SO_4$, $a^2 + b^2 = c^2$ using `<sub>` '
                   'and `<sup>`.\n'
                   '2. **Creating Lists:**\n'
                   '   * Create an unordered list of four programming languages (C++, Python, Java, JavaScript).\n'
                   '   * Create an ordered list of university semester courses using roman numerals (`type="I"`).\n'
                   "   * Create a nested list where 'Computer Hardware' contains sub-items for 'Input Devices' and "
                   "'Output Devices'.\n"
                   '3. **Adding Hyperlinks:**\n'
                   '   * Add an external hyperlink linking to `https://www.hamdard.edu.pk` with `target="_blank"`.\n'
                   '   * Create a second HTML file `contact.html`. Create relative hyperlinks between '
                   '`formatting.html` and `contact.html` allowing bidirectional navigation.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create an HTML file named `lab9_lists_links.html`. Design a complete syllabus outline page for '
                   "'Introduction to Computing'.\n"
                   '2. The page must include:\n'
                   '   * A formatted introductory paragraph using `<strong>`, `<em>`, and `<mark>`.\n'
                   '   * A 3-level nested list outlining the course modules.\n'
                   '   * At least three external hyperlinks with `target="_blank"` pointing to academic reference '
                   'resources.\n'
                   '   * An internal anchor link jumping from the bottom of the page back to the top heading.',
        'flashcards': [   {   'answer': 'An Absolute URL provides the complete web address including protocol (e.g., '
                                        'https://www.google.com). A Relative URL points to a file within the same '
                                        'website directory structure (e.g., about.html or images/pic.png).',
                              'question': 'What is an Absolute URL versus a Relative URL in an anchor tag?'},
                          {   'answer': "type='1' (standard numbers 1, 2, 3), type='A' (uppercase letters A, B, C), "
                                        "type='a' (lowercase letters), type='I' (uppercase Roman numerals), and "
                                        "type='i' (lowercase Roman numerals).",
                              'question': 'What type attribute values can be applied to an <ol> tag?'},
                          {   'answer': '<mark> text to be highlighted </mark>.',
                              'question': 'What tag is used to create highlighted text with a yellow background?'},
                          {   'answer': 'It renders text in subscript, positioned half a character below the normal '
                                        'text baseline, commonly used in chemical formulas like H2O.',
                              'question': 'What is the purpose of the <sub> tag?'}],
        'order': 9,
        'quizzes': [   {   'correctAnswer': '<sup>',
                           'explanation': "'<sup>' defines superscript text, which appears half a character above the "
                                          'normal baseline and is used for exponents and footnotes.',
                           'options': ['<sup>', '<sub>', '<super>', '<power>'],
                           'question': 'Which HTML element is used to render text as superscript (e.g., displaying '
                                       'mathematical powers like X²)?'},
                       {   'correctAnswer': 'target="_blank"',
                           'explanation': 'Setting \'target="_blank"\' instructs the browser to open the linked '
                                          'document in a new tab or window instead of replacing the current page.',
                           'options': ['target="_blank"', 'href="_new"', 'window="new"', 'tab="true"'],
                           'question': "Which attribute on the anchor tag '<a>' specifies whether the destination web "
                                       'page opens in a new browser tab?'},
                       {   'correctAnswer': '<ol>',
                           'explanation': "'<ol>' stands for Ordered List, which automatically numbers its child "
                                          "'<li>' list items in sequential order (1, 2, 3...).",
                           'options': ['<ol>', '<ul>', '<dl>', '<list>'],
                           'question': 'Which HTML list element defines an ordered list where items are numbered '
                                       'sequentially by default?'},
                       {   'correctAnswer': "'<strong>' carries semantic importance for screen readers and SEO, "
                                            "whereas '<b>' is purely visual styling",
                           'explanation': "While both tags render text in bold font visually, '<strong>' conveys "
                                          'semantic meaning indicating that the text is of serious importance, which '
                                          'is vocalized with emphasis by screen readers.',
                           'options': [   "'<strong>' carries semantic importance for screen readers and SEO, whereas "
                                          "'<b>' is purely visual styling",
                                          "'<b>' renders in italics, whereas '<strong>' renders in bold",
                                          "'<b>' is an HTML5 tag, whereas '<strong>' was deprecated in HTML4",
                                          'There is no difference; they are completely interchangeable'],
                           'question': "What is the technical semantic difference between the '<b>' tag and the "
                                       "'<strong>' tag in modern HTML?"},
                       {   'correctAnswer': '<li>',
                           'explanation': "'<li>' stands for List Item and must be contained directly inside either an "
                                          "'<ol>' or '<ul>' element to represent an item in the list.",
                           'options': ['<li>', '<item>', '<list-item>', '<ul>'],
                           'question': 'Which tag defines an individual item within either an ordered list (<ol>) or '
                                       'an unordered list (<ul>)?'}],
        'title': 'Lab 9: Be able to repeat the basics of HTML'},
    {   'codeSnippet': '<!-- Semantic Layout, Tables & Images Webpage Template -->\n'
                       '<!DOCTYPE html>\n'
                       '<html lang="en">\n'
                       '<head>\n'
                       '    <title>Student Academic Portfolio & Schedule</title>\n'
                       '</head>\n'
                       '<body>\n'
                       '    <!-- Semantic Header & Navigation -->\n'
                       '    <header>\n'
                       '        <h1>Faculty of Engineering Sciences & Technology (FEST)</h1>\n'
                       '        <nav>\n'
                       '            <a href="#profile">Profile</a> | \n'
                       '            <a href="#courses">Courses</a> | \n'
                       '            <a href="#timetable">Timetable</a>\n'
                       '        </nav>\n'
                       '    </header>\n'
                       '    <hr>\n'
                       '    <!-- Image Insertion with alt attribute -->\n'
                       '    <section id="profile">\n'
                       '        <h2>Student Profile</h2>\n'
                       '        <img src="assets/images/university/itc_exp/itc_exp_logo.png" \n'
                       '             alt="Hamdard University Crest" width="120" height="120">\n'
                       '        <p>Name: Muhammad Ali | Degree: BS Computer Science</p>\n'
                       '    </section>\n'
                       '    <!-- HTML Table with merged headers (colspan/rowspan) -->\n'
                       '    <section id="timetable">\n'
                       '        <h2>Weekly Laboratory Timetable</h2>\n'
                       '        <table border="1" cellpadding="8" cellspacing="0">\n'
                       '            <tr>\n'
                       '                <th>Day</th>\n'
                       '                <th>09:00 - 11:00</th>\n'
                       '                <th>11:00 - 01:00</th>\n'
                       '            </tr>\n'
                       '            <tr>\n'
                       '                <td>Monday</td>\n'
                       '                <td>Introduction to Computing Lab</td>\n'
                       '                <td>Programming Fundamentals</td>\n'
                       '            </tr>\n'
                       '            <tr>\n'
                       '                <td>Wednesday</td>\n'
                       '                <td colspan="2" align="center">Engineering Workshop / Project Work</td>\n'
                       '            </tr>\n'
                       '        </table>\n'
                       '    </section>\n'
                       '    <footer>\n'
                       '        <hr>\n'
                       '        <p>&copy; 2026 Hamdard University Islamabad Campus. All rights reserved.</p>\n'
                       '    </footer>\n'
                       '</body>\n'
                       '</html>',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 10: Practice Web Page designing using HTML\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Practice Web Page designing using HTML** | **CLO-2** | **PLO-1** | '
                   '**P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Integrate visual images into web documents using the `<img>` tag with proper `src`, `alt`, '
                   '`width`, and `height` attributes.\n'
                   '* Design structured tabular layouts using `<table>`, `<tr>` (table row), `<th>` (table header), '
                   'and `<td>` (table data) elements.\n'
                   '* Master table cell merging using the `colspan` and `rowspan` attributes.\n'
                   '* Apply HTML5 semantic layout container elements: `<header>`, `<nav>`, `<section>`, `<article>`, '
                   'and `<footer>`.\n'
                   '* Construct an end-to-end Student Academic Portfolio web page project integrating text, images, '
                   'tables, and navigation links.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   'Modern web design requires organizing content logically into semantic sections, displaying '
                   'structured tabular data, and presenting multimedia assets.\n'
                   '\n'
                   '#### 1. Image Embedding (`<img>`):\n'
                   'Images are linked into web pages using the empty (self-closing) `<img>` element:\n'
                   '```html\n'
                   '<img src="profile.jpg" alt="Student Portrait" width="200" height="200">\n'
                   '```\n'
                   '* `src` (source): Specifies the relative or absolute path to the image file (e.g. `.png`, `.jpg`, '
                   '`.svg`).\n'
                   '* `alt` (alternate text): Crucial accessibility attribute. Provides descriptive text if the image '
                   'fails to load and enables screen readers to vocalize image content to visually impaired users.\n'
                   '* `width` & `height`: Specifies display dimensions in pixels.\n'
                   '\n'
                   '#### 2. HTML Tables:\n'
                   'Tables organize data into rows and columns:\n'
                   '* `<table>`: Enclosing wrapper for the table.\n'
                   '* `<tr>`: Table Row container.\n'
                   '* `<th>`: Table Header cell (bold and center-aligned by default).\n'
                   '* `<td>`: Table Data cell (normal weight and left-aligned by default).\n'
                   '* `colspan="n"`: Merges a cell horizontally across $n$ columns.\n'
                   '* `rowspan="n"`: Merges a cell vertically across $n$ rows.\n'
                   '* `border`, `cellpadding`, `cellspacing`: Basic table presentation attributes.\n'
                   '\n'
                   '#### 3. HTML5 Semantic Structural Tags:\n'
                   'HTML5 introduced semantic tags that clearly describe their meaning to both the browser and '
                   'developer:\n'
                   '* `<header>`: Represents introductory content or navigation links at the top of a page.\n'
                   '* `<nav>`: Encloses major site navigation menu hyperlinks.\n'
                   '* `<section>`: Defines a standalone thematic section of content.\n'
                   '* `<article>`: Represents self-contained, independent distributable content (e.g. a blog post or '
                   'news item).\n'
                   '* `<footer>`: Contains footer information: copyright notices, author contact, and privacy links.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Embedding Images:**\n'
                   '   * Place an image file `logo.png` in your project folder.\n'
                   '   * Insert the image using `<img src="logo.png" alt="University Crest" width="150">`.\n'
                   '   * Verify what happens when an invalid filename is entered: the browser displays the `alt` '
                   'text.\n'
                   '2. **Constructing a Class Timetable Table:**\n'
                   '   * Create a 5-day by 4-time-slot course schedule table.\n'
                   '   * Use `<th>` for days of the week and class hours.\n'
                   '   * Use `colspan="2"` to represent a 2-hour laboratory session spanning two consecutive slots.\n'
                   '   * Use `rowspan="2"` for a multi-day recurring lab or workshop.\n'
                   '3. **Structuring with Semantic Tags:**\n'
                   '   * Organize the complete document inside `<header>`, `<nav>`, `<section id="about">`, `<section '
                   'id="schedule">`, and `<footer>`.\n'
                   '   * Add internal anchor links in the `<nav>` allowing the user to click and smooth-scroll to each '
                   'section.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Create a complete HTML web page project named `lab10_portfolio.html` representing your Personal '
                   'Academic Portfolio.\n'
                   '2. The portfolio page must include:\n'
                   '   * A semantic `<header>` with campus logo image and `<nav>` navigation bar.\n'
                   "   * An 'About Me' `<section>` featuring your photo, contact info, and career objectives.\n"
                   "   * An 'Academic Credentials' `<table>` with columns: *Examination*, *Board/University*, *Passing "
                   'Year*, *Marks/CGPA*.\n'
                   "   * A 'Weekly Lab Schedule' table demonstrating both `colspan` and `rowspan` cell merges.\n"
                   '   * A semantic `<footer>` with copyright notice and university email address.',
        'flashcards': [   {   'answer': '<th> defines a header cell (rendered bold and centered by default). <td> '
                                        'defines a standard data cell (rendered normal weight and left-aligned by '
                                        'default).',
                              'question': 'What is the difference between <td> and <th> in an HTML table?'},
                          {   'answer': 'rowspan specifies the number of vertical rows a cell should span or merge '
                                        'downward.',
                              'question': 'What is the function of the rowspan attribute in an HTML table?'},
                          {   'answer': '<header> (introductory page banner and titles), <nav> (navigation menu '
                                        'links), and <footer> (footer section containing copyright and contact '
                                        'details).',
                              'question': 'Name three HTML5 semantic layout elements and their purposes.'},
                          {   'answer': 'The browser will render the image at its original intrinsic pixel dimensions, '
                                        'which may disrupt layout flow before the image finishes downloading.',
                              'question': "What happens if an image's width and height attributes are omitted from an "
                                          '<img> tag?'}],
        'order': 10,
        'quizzes': [   {   'correctAnswer': 'alt',
                           'explanation': "The 'alt' (alternative text) attribute provides a textual description of "
                                          'the image for screen readers and is displayed if the image fails to load '
                                          'due to network errors.',
                           'options': ['alt', 'title', 'src', 'description'],
                           'question': "Which attribute on the '<img>' tag is mandatory for web accessibility to "
                                       'describe the image content if it fails to load or for screen readers?'},
                       {   'correctAnswer': 'colspan="3"',
                           'explanation': '\'colspan="3"\' instructs the table cell to span horizontally across 3 '
                                          "columns. 'rowspan' merges cells vertically across rows.",
                           'options': ['colspan="3"', 'rowspan="3"', 'span="3"', 'merge="3"'],
                           'question': 'Which HTML table attribute is used to merge a single data cell horizontally '
                                       'across three adjacent columns?'},
                       {   'correctAnswer': 'Bold and center-aligned',
                           'explanation': "By default in web browsers, table header cells ('<th>') render with bold "
                                          'text and center horizontal alignment.',
                           'options': [   'Bold and center-aligned',
                                          'Italic and left-aligned',
                                          'Underlined and right-aligned',
                                          'Normal font weight and left-aligned'],
                           'question': 'In an HTML table, what is the default visual appearance of content enclosed '
                                       "inside a '<th>' element?"},
                       {   'correctAnswer': '<nav>',
                           'explanation': "The '<nav>' element represents a section of a page that links to other "
                                          'pages or to parts within the page (the main site navigation menu).',
                           'options': ['<nav>', '<menu>', '<header>', '<links>'],
                           'question': 'Which HTML5 semantic element is specifically intended to enclose the primary '
                                       'website navigation hyperlinks?'},
                       {   'correctAnswer': '<tr>',
                           'explanation': "'<tr>' stands for Table Row and groups together '<th>' (header) or '<td>' "
                                          '(data) cells on the same horizontal row.',
                           'options': ['<tr>', '<td>', '<th>', '<row>'],
                           'question': 'Which tag defines an individual horizontal row inside an HTML table?'}],
        'title': 'Lab 10: Practice Web Page designing using HTML'},
    {   'codeSnippet': '% MATLAB Engineering Calculations & Signal Plotting Script\n'
                       '% 1. Scalar Arithmetic and Variable Definitions\n'
                       'a = 15;\n'
                       'b = 25;\n'
                       'c = a + b;           % Semicolon suppresses command window printing\n'
                       '\n'
                       '% 2. Row and Column Vectors\n'
                       'row_vec = [1, 2, 3, 4, 5];\n'
                       'col_vec = [1; 2; 3; 4; 5];\n'
                       '\n'
                       '% 3. Matrix Definitions and Operations\n'
                       'A = [1, 2; 3, 4];\n'
                       'B = [5, 6; 7, 8];\n'
                       'C_add = A + B;       % Matrix Addition\n'
                       'C_mul = A * B;       % Matrix Multiplication\n'
                       'C_elem = A .* B;     % Element-by-element array multiplication\n'
                       '\n'
                       '% 4. 2D Function Plotting\n'
                       't = 0 : 0.01 : 2*pi; % Time vector from 0 to 2*pi with step 0.01\n'
                       'y = sin(t);          % Sine wave calculation\n'
                       "plot(t, y, 'b-', 'LineWidth', 2);\n"
                       "title('Sine Wave Signal: y = sin(t)');\n"
                       "xlabel('Time (radians)');\n"
                       "ylabel('Amplitude');\n"
                       'grid on;',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 11: Be able to operate under supervision the basics of Matlab\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to operate under supervision the basics of Matlab** | '
                   '**CLO-2** | **PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the purpose and engineering applications of **MATLAB** (Matrix Laboratory).\n'
                   '* Familiarize with the MATLAB Desktop Environment: Command Window, Workspace, Current Folder, and '
                   'Command History.\n'
                   '* Define scalar variables, row vectors, column vectors, and 2D matrices.\n'
                   '* Master the use of the semicolon (`;`) for command suppression.\n'
                   '* Perform matrix arithmetic: addition (`+`), subtraction (`-`), matrix multiplication (`*`), and '
                   'element-wise array operations (`.*`, `./`).\n'
                   '* Generate 2D scientific graphs using `plot(x, y)`, and format charts with `title`, `xlabel`, '
                   '`ylabel`, and `grid on`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '**MATLAB** (Matrix Laboratory) is a high-performance interactive computing environment and '
                   'programming language developed by MathWorks. It is widely used in electrical engineering, computer '
                   'systems, robotics, control systems, and data science for mathematical computations, matrix '
                   'manipulation, algorithm development, and data visualization.\n'
                   '\n'
                   '![MATLAB Desktop Layout](assets/images/university/itc/lab10_matlab_desktop.png)\n'
                   '\n'
                   '#### 1. The MATLAB Desktop Environment:\n'
                   '* **Command Window:** The primary interactive window where users enter commands at the prompt '
                   '(`>>`) and view immediate numerical results.\n'
                   '* **Workspace:** Displays all variables currently created in memory, including their names, data '
                   'types, dimensions (e.g. `1x100 double`), and values.\n'
                   '* **Current Folder:** Shows all files, scripts (`.m`), and functions in the active directory.\n'
                   '* **Command History:** Logs previously executed commands, allowing users to recall past commands '
                   'using the Up-Arrow key.\n'
                   '\n'
                   '![MATLAB Command Output](assets/images/university/itc/lab10_matlab_command_output.png)\n'
                   '\n'
                   '#### 2. Variables and Matrix Representation:\n'
                   'In MATLAB, every variable is treated as a matrix or array by default:\n'
                   '* **Scalar:** A $1 \\times 1$ matrix (e.g. `x = 10`).\n'
                   '* **Row Vector:** Elements separated by spaces or commas inside brackets: `R = [1, 2, 3, 4]` ($1 '
                   '\\times 4$).\n'
                   '* **Column Vector:** Elements separated by semicolons: `C = [1; 2; 3; 4]` ($4 \\times 1$).\n'
                   '* **2D Matrix:** Rows separated by semicolons: `A = [1, 2, 3; 4, 5, 6]` ($2 \\times 3$).\n'
                   '\n'
                   '#### 3. Semicolon (`;`) Operator:\n'
                   'In MATLAB, terminating a statement with a semicolon executes the calculation silently without '
                   'printing the result to the Command Window. Omitting the semicolon forces MATLAB to display the '
                   'variable name and output immediately.\n'
                   '\n'
                   '#### 4. Matrix Multiplication vs. Element-Wise Operations:\n'
                   '* **Matrix Multiplication (`*`):** Standard linear algebra dot product; requires the inner '
                   'dimensions to match (e.g., $m \\times k$ multiplied by $k \\times n$).\n'
                   '* **Element-wise Array Operations (`.*`, `./`, `.^`):** The dot prefix instructs MATLAB to apply '
                   'the operation to corresponding individual elements of identically sized matrices.\n'
                   '\n'
                   '#### 5. Scientific 2D Plotting:\n'
                   'MATLAB provides robust graphics capabilities:\n'
                   '* `plot(x, y)`: Plots vector $x$ on the horizontal axis against vector $y$ on the vertical axis.\n'
                   "* `title('Text')`: Sets the title of the figure.\n"
                   "* `xlabel('Text')` & `ylabel('Text')`: Labels the coordinate axes.\n"
                   '* `grid on`: Displays gridlines on the plot for easy reading.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Scalar Arithmetic:**\n'
                   '   * Launch MATLAB. In the Command Window, enter: `x = 5; y = 12; z = sqrt(x^2 + y^2)`.\n'
                   '   * Observe the result `z = 13` displayed in the Command Window and verify the variables in the '
                   'Workspace.\n'
                   '2. **Vector and Matrix Definition:**\n'
                   '   * Create a row vector `A = [2, 4, 6, 8, 10]`.\n'
                   '   * Create a column vector `B = [1; 3; 5; 7; 9]`.\n'
                   '   * Create a $3 \\times 3$ matrix `M = [1, 2, 3; 4, 5, 6; 7, 8, 9]`.\n'
                   "   * Compute the transpose of matrix `M` using the prime operator: `M_trans = M'`.\n"
                   '3. **Element-by-Element Operations:**\n'
                   '   * Define `v1 = [1, 2, 3]` and `v2 = [4, 5, 6]`.\n'
                   '   * Compute `v_prod = v1 .* v2`. Observe result `[4, 10, 18]`.\n'
                   '4. **Plotting a Continuous Sine Wave:**\n'
                   '   * Define time: `t = 0:0.05:2*pi;`.\n'
                   '   * Compute signal: `y = sin(t);`.\n'
                   "   * Plot graph: `plot(t, y); grid on; xlabel('Time (s)'); ylabel('Amplitude'); title('Sine "
                   "Wave');`.\n"
                   '\\n---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. In MATLAB, define two $3 \\times 3$ matrices $P$ and $Q$. Compute their matrix sum ($P + Q$), '
                   'matrix product ($P * Q$), and element-wise product ($P .* Q$). State the difference between the '
                   'two products.\n'
                   '2. Generate a vector $x$ from $-10$ to $+10$ with step size $0.1$. Compute $y = x^2 - 4x + 3$. '
                   'Plot the quadratic parabola curve with axis labels and a title.\n'
                   '3. On a single graph, plot both $y_1 = \\sin(t)$ and $y_2 = \\cos(t)$ over the range $0 \\le t '
                   '\\le 4\\pi$ using different colors (blue and red). Use the `legend` command to identify the '
                   'curves.\n'
                   '4. Explain the function of the MATLAB Workspace window.',
        'flashcards': [   {'answer': 'MATrix LABoratory.', 'question': 'What does the MATLAB acronym stand for?'},
                          {   'answer': 'A row vector separates elements with spaces or commas (e.g., [1, 2, 3]). A '
                                        'column vector separates elements with semicolons (e.g., [1; 2; 3]).',
                              'question': 'How do you define a 1D row vector versus a 1D column vector in MATLAB?'},
                          {   'answer': "The prime operator (e.g., A') computes the matrix transpose, converting rows "
                                        'into columns and columns into rows.',
                              'question': "What does the transpose operator (') do in MATLAB?"},
                          {   'answer': 'v = 0 : 0.5 : 10;',
                              'question': 'What command creates a vector of numbers from 0 to 10 with a step increment '
                                          'of 0.5?'}],
        'order': 11,
        'quizzes': [   {   'correctAnswer': 'Suppresses the display of the calculation output in the Command Window',
                           'explanation': 'In MATLAB, terminating a statement with a semicolon suppresses the '
                                          'echoing/printing of the result in the Command Window, speeding up script '
                                          'execution.',
                           'options': [   'Suppresses the display of the calculation output in the Command Window',
                                          'Terminates the execution of the entire script',
                                          'Clears all variables stored in the Workspace',
                                          'Saves the variable permanently to hard disk storage'],
                           'question': 'What is the effect of placing a semicolon (;) at the end of a MATLAB command '
                                       'line statement?'},
                       {   'correctAnswer': '.*',
                           'explanation': "The dot-asterisk operator ('.*') performs element-by-element "
                                          'multiplication, multiplying corresponding elements individually rather than '
                                          "performing linear algebra matrix multiplication ('*').",
                           'options': ['.*', '*', 'x', '.^'],
                           'question': 'Which MATLAB operator is used to perform element-by-element array '
                                       'multiplication between two matrices of identical dimensions?'},
                       {   'correctAnswer': 'Workspace',
                           'explanation': 'The MATLAB Workspace displays all variables currently stored in active '
                                          'memory, showing their names, dimensions, values, and min/max stats.',
                           'options': ['Workspace', 'Command Window', 'Command History', 'Current Folder'],
                           'question': 'Which window in the MATLAB desktop interface displays all currently created '
                                       'variables along with their dimensions, byte size, and data classes?'},
                       {   'correctAnswer': 'plot(x, y)',
                           'explanation': "The 'plot(x, y)' function creates a two-dimensional Cartesian line plot of "
                                          'vector x versus vector y in a new figure window.',
                           'options': ['plot(x, y)', 'graph(x, y)', 'line(x, y)', 'draw(x, y)'],
                           'question': "What command generates a 2D line graph of vector 'x' on the horizontal axis "
                                       "versus vector 'y' on the vertical axis in MATLAB?"},
                       {   'correctAnswer': 'clear',
                           'explanation': "'clear' removes all variables from the Workspace memory. 'clc' clears text "
                                          "from the Command Window without deleting variables, and 'close all' closes "
                                          'open figure windows.',
                           'options': ['clear', 'clc', 'close all', 'reset'],
                           'question': 'In MATLAB, which command clears all variables from the active Workspace '
                                       'memory?'}],
        'title': 'Lab 11: Be able to operate under supervision the basics of Matlab'},
    {   'codeSnippet': '// Standard C++ Console Application Structure\n'
                       '#include <iostream>   // Preprocessor directive for input/output stream\n'
                       '#include <string>     // Include string library\n'
                       'using namespace std;  // Allows using standard names (cout, cin) without std:: prefix\n'
                       '\n'
                       'int main() {\n'
                       '    // Variable Declarations\n'
                       '    string studentName;\n'
                       '    int currentAge;\n'
                       '    float currentGPA;\n'
                       '\n'
                       '    // Interactive Standard Output & Input\n'
                       '    cout << "====================================" << endl;\n'
                       '    cout << "  HAMDARD UNIVERSITY CS DEPARTMENT  " << endl;\n'
                       '    cout << "====================================" << endl;\n'
                       '\n'
                       '    cout << "Enter your Full Name: ";\n'
                       '    getline(cin, studentName);\n'
                       '\n'
                       '    cout << "Enter your Current Age (in years): ";\n'
                       '    cin >> currentAge;\n'
                       '\n'
                       '    cout << "Enter your Semester GPA (0.0 to 4.0): ";\n'
                       '    cin >> currentGPA;\n'
                       '\n'
                       '    // Computation\n'
                       '    int birthYear = 2026 - currentAge;\n'
                       '\n'
                       '    // Output Results\n'
                       '    cout << "\\n--- Student Profile Summary ---" << endl;\n'
                       '    cout << "Student Name : " << studentName << endl;\n'
                       '    cout << "Approx Birth : " << birthYear << endl;\n'
                       '    cout << "Academic GPA : " << currentGPA << endl;\n'
                       '\n'
                       '    return 0; // Return 0 indicates successful program termination\n'
                       '}',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 12: Practicing the basics of Programming in C++\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Practicing the basics of Programming in C++** | **CLO-2** | **PLO-1** '
                   '| **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the fundamental structure of a C++ source program: preprocessor directives, '
                   'namespace, and the `main()` function.\n'
                   '* Understand the compilation and execution pipeline: Source Code (`.cpp`) -> Preprocessor -> '
                   'Compiler (`.obj`) -> Linker -> Executable (`.exe`).\n'
                   '* Learn fundamental C++ data types: `int`, `float`, `double`, `char`, `bool`, and `string`.\n'
                   '* Master standard console output using `cout <<` (insertion operator) and formatting using `endl` '
                   'and `\\n`.\n'
                   '* Master standard console input using `cin >>` (extraction operator) to create interactive '
                   'programs.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   '**C++** is a general-purpose, statically typed, compiled programming language created by Bjarne '
                   'Stroustrup as an extension of the C language. It is renowned for its performance, low-level memory '
                   'manipulation, and foundational role in operating systems, game engines, and embedded systems.\n'
                   '\n'
                   '![C-Free / Dev-C++ IDE Interface](assets/images/university/itc/lab12_cfree_ide.png)\n'
                   '\n'
                   '#### 1. Anatomy of a Basic C++ Program:\n'
                   '* `#include <iostream>`: Preprocessor directive that includes the standard Input/Output stream '
                   'library, granting access to `cout` and `cin`.\n'
                   '* `using namespace std;`: Imports the standard C++ namespace so functions and objects can be '
                   'referenced without prefixing `std::` (e.g. `cout` instead of `std::cout`).\n'
                   '* `int main()`: The entry point where program execution begins. Every C++ program must have '
                   'exactly one `main()` function.\n'
                   '* `{ ... }`: Braces delineate blocks of executable statements.\n'
                   '* `;` (Semicolon): Every statement in C++ must end with a semicolon.\n'
                   '* `return 0;`: Signals to the operating system that the program has executed and terminated '
                   'successfully.\n'
                   '\n'
                   '![C-Free Editor Window](assets/images/university/itc/lab12_cfree_editor_window.png)\n'
                   '\n'
                   '#### 2. Fundamental Data Types & Memory Sizes:\n'
                   '* **`int` (Integer):** Stores whole numbers (e.g. `-25`, `0`, `450`); typically 4 bytes (32 '
                   'bits).\n'
                   '* **`float` (Floating Point):** Stores single-precision decimal fractions (e.g. `3.14159f`); '
                   'typically 4 bytes.\n'
                   '* **`double` (Double Precision):** Stores high-precision decimal numbers; 8 bytes (64 bits).\n'
                   "* **`char` (Character):** Stores a single ASCII character enclosed in single quotes (e.g. `'A'`, "
                   "`'7'`, `'$'`); 1 byte.\n"
                   '* **`bool` (Boolean):** Stores logical truth values `true` (1) or `false` (0); 1 byte.\n'
                   '* **`string`:** A sequence of characters enclosed in double quotes (requires `#include '
                   '<string>`).\n'
                   '\n'
                   '#### 3. Standard Console I/O Streams:\n'
                   '* **`cout` (Character Output):** Used with the stream insertion operator (`<<`) to print text and '
                   'variable values to the console screen.\n'
                   '* **`cin` (Character Input):** Used with the stream extraction operator (`>>`) to read values '
                   'entered by the user via the keyboard into variables.\n'
                   '* **`endl` vs `\\n`:** Inserts a newline. `endl` additionally flushes the output stream buffer.\n'
                   '\n'
                   '![C-Free Console Output Window](assets/images/university/itc/lab12_cfree_output_window.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Writing and Compiling Your First Program:**\n'
                   '   * Launch your C++ IDE (Dev-C++, Code::Blocks, or Visual Studio).\n'
                   '   * Create a new source file: *File* -> *New* -> *Source File*. Save as `lab12_first.cpp`.\n'
                   "   * Type the standard 'Hello World' program:\n"
                   '     ```cpp\n'
                   '     #include <iostream>\n'
                   '     using namespace std;\n'
                   '     int main() {\n'
                   '         cout << "Hello, World from Hamdard University!" << endl;\n'
                   '         return 0;\n'
                   '     }\n'
                   '     ```\n'
                   '   * Click *Compile & Run* (`F11`). Observe the output console window.\n'
                   '2. **Interactive User Input:**\n'
                   '   * Declare integer variables `num1`, `num2`, and `sum`.\n'
                   '   * Prompt user: `cout << "Enter first number: "; cin >> num1;`.\n'
                   '   * Prompt user: `cout << "Enter second number: "; cin >> num2;`.\n'
                   '   * Calculate: `sum = num1 + num2;`.\n'
                   '   * Print: `cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << endl;`.\n'
                   '   * Test with multiple positive and negative numbers.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Write a complete C++ program that prompts the user to enter their Student Name, Roll Number, '
                   'and marks in three subjects (Math, English, Science). Compute and display the Total Marks and '
                   'Percentage.\n'
                   '2. Write a C++ program that calculates the area and circumference of a circle given radius $r$ '
                   'entered by the user ($Area = \\pi r^2$, $Circumference = 2 \\pi r$). Use constant $\\pi = '
                   '3.14159$.\n'
                   '3. Write a program that converts temperature entered in degrees Celsius into degrees Fahrenheit '
                   'using formula: $F = (C \\times 9/5) + 32$.\n'
                   '4. Explain what occurs if a semicolon is omitted at the end of an executable statement in C++.',
        'flashcards': [   {   'answer': "Both insert a newline character, but 'endl' additionally flushes the output "
                                        'stream buffer, ensuring that all buffered text is written to the screen '
                                        'immediately.',
                              'question': "What is the difference between endl and '\\n' in C++?"},
                          {   'answer': 'The compiler translates human-readable C++ source code (.cpp) into machine '
                                        'language object code (.obj) understandable by the computer CPU.',
                              'question': 'What is the role of the C++ Compiler?'},
                          {   'answer': '4 bytes (32 bits), allowing it to represent values from -2,147,483,648 to '
                                        '+2,147,483,647.',
                              'question': 'What memory size is typically occupied by a standard int variable in modern '
                                          '32-bit/64-bit systems?'},
                          {   'answer': 'It imports all elements from the standard C++ namespace (std) into the '
                                        "current global scope, allowing you to type 'cout' and 'cin' directly without "
                                        "writing 'std::cout' or 'std::cin'.",
                              'question': "What does 'using namespace std;' do in a C++ program?"}],
        'order': 12,
        'quizzes': [   {   'correctAnswer': '<<',
                           'explanation': "In C++, the stream insertion operator ('<<') is used with 'cout' to direct "
                                          'text and variable values to the standard output stream.',
                           'options': ['<<', '>>', '==', '::'],
                           'question': "Which stream insertion operator is used in conjunction with 'cout' to send "
                                       'data to the standard console display in C++?'},
                       {   'correctAnswer': 'main()',
                           'explanation': "The 'main()' function is the mandatory entry point where program execution "
                                          'begins in any standard C++ console application.',
                           'options': ['main()', 'start()', 'run()', 'init()'],
                           'question': 'Every standalone executable C++ program must contain which mandatory function '
                                       'as its primary starting entry point?'},
                       {   'correctAnswer': 'float (or double)',
                           'explanation': "'float' and 'double' are floating-point types designed to store real "
                                          "numbers with decimal fractions. 'int' stores whole integers only.",
                           'options': ['float (or double)', 'int', 'char', 'bool'],
                           'question': 'Which fundamental C++ data type is specifically designed to store fractional '
                                       'numbers with decimal points (such as 3.14159)?'},
                       {   'correctAnswer': "Includes the input/output stream header library needed for 'cin' and "
                                            "'cout'",
                           'explanation': "'#include <iostream>' directs the C++ preprocessor to include the standard "
                                          "input/output stream library, providing the definitions for 'cin' and "
                                          "'cout'.",
                           'options': [   "Includes the input/output stream header library needed for 'cin' and 'cout'",
                                          'Compiles the program into machine language code',
                                          'Allocates memory space for local variables',
                                          'Declares the standard namespace automatically'],
                           'question': "What is the function of the preprocessor directive '#include <iostream>' at "
                                       'the beginning of a C++ source file?'},
                       {   'correctAnswer': '>>',
                           'explanation': "The stream extraction operator ('>>') is used with 'cin' to read keyboard "
                                          'input from the input stream and store it into the target variable.',
                           'options': ['>>', '<<', '->', '+='],
                           'question': "Which operator is used with 'cin' to extract data entered by the user from the "
                                       'keyboard into a variable?'}],
        'title': 'Lab 12: Practicing the basics of Programming in C++'},
    {   'codeSnippet': '// C++ Modular Programming: User-Defined Functions\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       '// 1. Function Prototypes (Declarations)\n'
                       'int calculateSum(int a, int b);\n'
                       'double calculateAverage(int a, int b);\n'
                       'int findMaximum(int a, int b);\n'
                       'void displayBanner();\n'
                       '\n'
                       'int main() {\n'
                       '    displayBanner(); // Void function call\n'
                       '\n'
                       '    int x, y;\n'
                       '    cout << "Enter two integer values: ";\n'
                       '    cin >> x >> y;\n'
                       '\n'
                       '    // Calling functions and capturing return values\n'
                       '    int sum = calculateSum(x, y);\n'
                       '    double avg = calculateAverage(x, y);\n'
                       '    int maxVal = findMaximum(x, y);\n'
                       '\n'
                       '    cout << "\\nResults Computed by Functions:" << endl;\n'
                       '    cout << "Sum     : " << sum << endl;\n'
                       '    cout << "Average : " << avg << endl;\n'
                       '    cout << "Maximum : " << maxVal << endl;\n'
                       '\n'
                       '    return 0;\n'
                       '}\n'
                       '\n'
                       '// 2. Function Definitions (Implementations)\n'
                       'void displayBanner() {\n'
                       '    cout << "====================================" << endl;\n'
                       '    cout << "  C++ Modular Function Diagnostics  " << endl;\n'
                       '    cout << "====================================" << endl;\n'
                       '}\n'
                       '\n'
                       'int calculateSum(int a, int b) {\n'
                       '    return a + b; // Returns integer sum\n'
                       '}\n'
                       '\n'
                       'double calculateAverage(int a, int b) {\n'
                       '    return (double)(a + b) / 2.0; // Cast to double for precision\n'
                       '}\n'
                       '\n'
                       'int findMaximum(int a, int b) {\n'
                       '    if (a > b) return a;\n'
                       '    else return b;\n'
                       '}',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 13: Be able to operate under supervision the basics functions of C++\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to operate under supervision the basics functions of C++** | '
                   '**CLO-2** | **PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Understand the concept and architectural advantages of **Modular Programming** and code '
                   'reusability.\n'
                   '* Differentiate between a **Function Prototype** (declaration), **Function Definition**, and '
                   '**Function Call**.\n'
                   '* Understand function return types: value-returning functions (`int`, `double`, `bool`) versus '
                   'non-returning functions (`void`).\n'
                   '* Distinguish between **Formal Parameters** (in function headers) and **Actual Arguments** (passed '
                   'in function calls).\n'
                   '* Understand the **Call-by-Value** parameter passing mechanism and local variable scope.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   'A **Function** is a self-contained, named block of C++ statements designed to perform a specific, '
                   'well-defined task. Rather than writing repetitive code inside `main()`, functions allow '
                   'programmers to divide large, complex problems into manageable, reusable modules (the '
                   '*Divide-and-Conquer* principle).\n'
                   '\n'
                   '![C-Free Editor Functions](assets/images/university/itc/lab12_cfree_editor_window.png)\n'
                   '\n'
                   '#### 1. Components of a Function in C++:\n'
                   "* **Function Prototype (Declaration):** Informs the compiler about the function's name, return "
                   'type, and parameter list before `main()` is compiled:\n'
                   '  ```cpp\n'
                   '  int add(int a, int b); // Prototype ending with semicolon\n'
                   '  ```\n'
                   '* **Function Definition:** Contains the actual body of executable statements:\n'
                   '  ```cpp\n'
                   '  int add(int a, int b) {\n'
                   '      return a + b; // return statement sending result back to caller\n'
                   '  }\n'
                   '  ```\n'
                   '* **Function Call:** Invokes the function during program execution, passing arguments:\n'
                   '  ```cpp\n'
                   '  int result = add(10, 20);\n'
                   '  ```\n'
                   '\n'
                   '#### 2. Return Types:\n'
                   '* **Value-Returning Functions:** Return a single computed value of a specific data type (`int`, '
                   '`float`, `double`, `string`) to the calling expression using the `return` keyword.\n'
                   '* **Void Functions (`void`):** Perform actions (such as printing banners or writing files) without '
                   'returning any value. A `return;` statement without an expression is optional.\n'
                   '\n'
                   '#### 3. Formal Parameters vs. Actual Arguments:\n'
                   '* **Actual Arguments:** The real values or variables passed to the function in the calling '
                   'statement (e.g. `add(x, y)`).\n'
                   "* **Formal Parameters:** The local placeholder variables declared in the function's header that "
                   'receive copies of the argument values (e.g. `int add(int a, int b)`).\n'
                   '\n'
                   '#### 4. Call-by-Value Mechanism & Scope:\n'
                   'By default in C++, arguments are passed **by value**. This means the function receives independent '
                   "copies of the caller's arguments. Any modifications made to the formal parameters inside the "
                   'function do not affect the original variables in `main()`. Local variables declared inside a '
                   'function exist only during its execution and are destroyed when the function returns.\n'
                   '\n'
                   '![C-Free Console Output](assets/images/university/itc/lab12_cfree_output_window.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Writing a Void Helper Function:**\n'
                   '   * Create a function `void printGreeting(string name)` that outputs a welcome message.\n'
                   '   * Call it multiple times from `main()` with different student names.\n'
                   '2. **Writing a Value-Returning Math Function:**\n'
                   '   * Declare and implement `int square(int n) { return n * n; }`.\n'
                   '   * Implement `int cube(int n) { return n * n * n; }`.\n'
                   '   * Prompt the user for a number, call both functions, and print the results.\n'
                   '3. **Implementing a Maximum Finder Function:**\n'
                   '   * Implement `int findMax(int a, int b, int c)` that evaluates three parameters and returns the '
                   'largest value.\n'
                   '   * Test with multiple combinations of inputs.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Write a modular C++ program with user-defined functions that performs basic arithmetic '
                   'calculations. Include separate functions: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and '
                   '`divide(a, b)`.\n'
                   '2. Implement a function `bool isEven(int number)` that returns `true` if the integer is even and '
                   '`false` if it is odd. Test it by asking the user for a number in `main()`.\n'
                   '3. Implement a function `double calculateSimpleInterest(double principal, double rate, double '
                   'time)` that computes interest using formula $I = (P \\times R \\times T) / 100$.\n'
                   '4. Explain what happens to a local variable declared inside a function after the function finishes '
                   'execution.',
        'flashcards': [   {   'answer': 'Code reusability, modularity, readability, easier debugging, and the ability '
                                        'to decompose complex problems into smaller, manageable sub-problems.',
                              'question': 'What is the primary benefit of modular programming using functions?'},
                          {   'answer': 'Block scope: it exists only from its declaration until the closing brace } of '
                                        'the function, and is inaccessible outside that function.',
                              'question': 'What is the scope of a local variable declared inside a function in C++?'},
                          {   'answer': 'No. A standard return statement can return at most one value (unless '
                                        'returning a struct, class, pair, or tuple).',
                              'question': 'Can a C++ function return more than one value using a single standard '
                                          'return statement?'},
                          {   'answer': 'A Parameter is the variable declared in the function signature (e.g., int x). '
                                        'An Argument is the actual value passed into the function during a call (e.g., '
                                        '25).',
                              'question': 'What is the difference between an Argument and a Parameter?'}],
        'order': 13,
        'quizzes': [   {   'correctAnswer': 'Declares the function name, return type, and parameter list before its '
                                            'call so the compiler recognizes it',
                           'explanation': "A function prototype informs the compiler about the function's interface "
                                          '(name, return type, and parameter types) so it can validate calls before '
                                          'the function definition is encountered.',
                           'options': [   'Declares the function name, return type, and parameter list before its call '
                                          'so the compiler recognizes it',
                                          'Executes the function automatically upon program startup',
                                          'Allocates permanent heap memory for the function variables',
                                          'Imports external library header files'],
                           'question': 'What is the purpose of a Function Prototype in a C++ source program?'},
                       {   'correctAnswer': 'void',
                           'explanation': "The 'void' keyword indicates that a function does not return any value to "
                                          'the calling function.',
                           'options': ['void', 'null', 'empty', 'static'],
                           'question': 'Which C++ keyword is used as the return type for a function that performs '
                                       'actions (such as printing output) without returning any value to the caller?'},
                       {   'correctAnswer': 'Only the local copy inside the function changes; the original variable in '
                                            'the caller remains unchanged',
                           'explanation': 'In call-by-value, a copy of the argument value is passed into the function '
                                          'parameter. Changes made to this local copy do not modify the original '
                                          'variable in the calling function.',
                           'options': [   'Only the local copy inside the function changes; the original variable in '
                                          'the caller remains unchanged',
                                          'The original variable in the calling function is permanently altered',
                                          'A compilation error occurs',
                                          'The program terminates immediately with a segmentation fault'],
                           'question': "In the default 'Call-by-Value' parameter passing mechanism in C++, what "
                                       'happens when a function modifies its formal parameter?'},
                       {   'correctAnswer': 'Formal Parameters',
                           'explanation': 'Variables defined in the function declaration or definition header are '
                                          'called Formal Parameters. The actual values or variables passed into the '
                                          'function call are Actual Arguments.',
                           'options': ['Formal Parameters', 'Actual Arguments', 'Global Variables', 'Static Constants'],
                           'question': 'What are the placeholder variables declared in a function header called, as '
                                       'opposed to the real values passed in during a call?'},
                       {   'correctAnswer': 'return',
                           'explanation': "The 'return' statement terminates execution of the function and yields the "
                                          'specified return value back to the caller.',
                           'options': ['return', 'send', 'output', 'exit'],
                           'question': 'Which C++ statement is used inside a value-returning function to send the '
                                       'computed result back to the calling expression?'}],
        'title': 'Lab 13: Be able to operate under supervision the basics functions of C++'},
    {   'codeSnippet': '// C++ Operators & Decision Control Structures\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    int score;\n'
                       '    cout << "Enter student numerical score (0 to 100): ";\n'
                       '    cin >> score;\n'
                       '\n'
                       '    // 1. Relational & Logical Operators in Decision Control\n'
                       '    if (score < 0 || score > 100) {\n'
                       '        cout << "Invalid score! Score must be between 0 and 100." << endl;\n'
                       '    } else {\n'
                       '        // 2. If - Else If - Else Ladder for Letter Grading\n'
                       '        char grade;\n'
                       '        if (score >= 85) {\n'
                       "            grade = 'A';\n"
                       '        } else if (score >= 70) {\n'
                       "            grade = 'B';\n"
                       '        } else if (score >= 55) {\n'
                       "            grade = 'C';\n"
                       '        } else if (score >= 50) {\n'
                       "            grade = 'D';\n"
                       '        } else {\n'
                       "            grade = 'F';\n"
                       '        }\n'
                       '\n'
                       '        cout << "\\nAssigned Grade: " << grade << endl;\n'
                       '\n'
                       '        // 3. Modulus (%) Operator for Even / Odd Parity Check\n'
                       '        if (score % 2 == 0) {\n'
                       '            cout << "The entered score (" << score << ") is an EVEN number." << endl;\n'
                       '        } else {\n'
                       '            cout << "The entered score (" << score << ") is an ODD number." << endl;\n'
                       '        }\n'
                       '    }\n'
                       '\n'
                       '    return 0;\n'
                       '}',
        'content': '![Hamdard University HIET Crest](assets/images/university/itc_exp/itc_exp_logo.png)\n'
                   '\n'
                   '# LAB # 14: Be able to manipulate with guidance the Arithmetic and logic operations in C++\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Curriculum & OBE Mapping\n'
                   '| Course | Title of Experiment | CLO | PLO | Taxonomy Level |\n'
                   '| :--- | :--- | :---: | :---: | :---: |\n'
                   '| **Intro to computing** | **Be able to manipulate with guidance the Arithmetic and logic '
                   'operations in C++** | **CLO-2** | **PLO-1** | **P3 (Guided Response)** |\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   '* Master C++ **Arithmetic Operators**: addition (`+`), subtraction (`-`), multiplication (`*`), '
                   'division (`/`), and modulus (`%`).\n'
                   '* Understand integer division truncation versus floating-point division.\n'
                   '* Apply **Relational Operators**: equal-to (`==`), not-equal-to (`!=`), greater-than (`>`), '
                   'less-than (`<`), greater-than-or-equal (`>=`), less-than-or-equal (`<=`).\n'
                   '* Master **Logical Operators**: logical AND (`&&`), logical OR (`||`), and logical NOT (`!`).\n'
                   '* Implement decision control structures: `if`, `if-else`, and multi-way `else if` ladders.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory Overview:-\n'
                   '\n'
                   'Operators are foundational symbols that instruct the compiler to perform specific mathematical, '
                   'relational, or logical manipulations on operands.\n'
                   '\n'
                   '#### 1. Arithmetic Operators:\n'
                   '* `+` (Addition), `-` (Subtraction), `*` (Multiplication)\n'
                   '* `/` (Division): In C++, dividing two integers performs **Integer Division**, discarding any '
                   'fractional remainder (e.g. `7 / 2` evaluates to `3`). If either operand is floating-point (e.g. '
                   '`7.0 / 2`), floating-point division is performed, producing `3.5`.\n'
                   '* `%` (Modulus): Computes the integer remainder of division (e.g. `7 % 2` produces `1`). Works '
                   'only with integer operands.\n'
                   '* `++` (Increment) and `--` (Decrement): Increases or decreases a variable by 1.\n'
                   '\n'
                   '#### 2. Relational Operators:\n'
                   'Relational operators compare two values and evaluate to a boolean truth value (`true` or '
                   '`false`):\n'
                   '* `==` (Equality check; *do not confuse with assignment `=`*)\n'
                   '* `!=` (Not equal to)\n'
                   '* `>`, `<`, `>=`, `<=` (Comparative inequalities)\n'
                   '\n'
                   '#### 3. Logical Operators:\n'
                   'Used to combine multiple relational expressions:\n'
                   '* `&&` (Logical AND): True only if **both** operands are true (`true && true -> true`).\n'
                   '* `||` (Logical OR): True if **at least one** operand is true (`true || false -> true`).\n'
                   '* `!` (Logical NOT): Inverts truth value (`!true -> false`).\n'
                   '\n'
                   '#### 4. Decision Control Structures:\n'
                   'Decision structures allow conditional execution paths based on boolean evaluations:\n'
                   '* **Single `if`:** Executes a block of code only if the condition evaluates to true.\n'
                   '* **`if - else`:** Executes the `if` block if true; otherwise executes the alternative `else` '
                   'block.\n'
                   '* **`else if` Ladder:** Evaluates a series of mutually exclusive conditions sequentially until one '
                   'matches.\n'
                   '\n'
                   '![C-Free Output](assets/images/university/itc/lab12_cfree_output_window.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Laboratory Procedures:\n'
                   '\n'
                   '1. **Testing Arithmetic and Modulus Operators:**\n'
                   '   * Write a program that inputs two integers $a$ and $b$.\n'
                   '   * Compute quotient `a / b` and remainder `a % b`.\n'
                   '   * Observe what happens if $b = 0$ (runtime division by zero error).\n'
                   '2. **Even / Odd Parity Program:**\n'
                   '   * Read an integer from the user.\n'
                   '   * Use the condition `if (number % 2 == 0)` to check for even numbers.\n'
                   '3. **Finding the Maximum of Three Numbers:**\n'
                   '   * Read three integers `num1`, `num2`, `num3`.\n'
                   '   * Use compound logical conditions:\n'
                   '     ```cpp\n'
                   '     if (num1 >= num2 && num1 >= num3) {\n'
                   '         cout << "Largest is num1" << endl;\n'
                   '     } else if (num2 >= num1 && num2 >= num3) {\n'
                   '         cout << "Largest is num2" << endl;\n'
                   '     } else {\n'
                   '         cout << "Largest is num3" << endl;\n'
                   '     }\n'
                   '     ```\n'
                   '4. **Leap Year Evaluation:**\n'
                   '   * A year is leap if divisible by 4 and not by 100, or divisible by 400:\n'
                   '     `if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab Tasks (Guided Response - P3):\n'
                   '1. Write a complete C++ program that prompts the user to enter their age. The program determines '
                   "voting eligibility: if age $\\ge 18$, print 'Eligible to Vote'; otherwise calculate and display "
                   'how many years remain until eligible.\n'
                   '2. Write a program that takes three subject marks from the user, computes the average, and assigns '
                   'a letter grade using an `else if` ladder: $\\ge 85$: Grade A, $\\ge 70$: Grade B, $\\ge 55$: Grade '
                   'C, $\\ge 50$: Grade D, $< 50$: Grade F.\n'
                   '3. Write a program that functions as a Simple Calculator: inputs two numbers and a character '
                   'operator (`+`, `-`, `*`, `/`, `%`), computes the operation, and displays the result.\n'
                   '4. Explain the difference between the equality operator (`==`) and the assignment operator (`=`).',
        'flashcards': [   {   'answer': '&& (Logical AND), || (Logical OR), and ! (Logical NOT).',
                              'question': 'What are the three logical operators in C++?'},
                          {   'answer': 'For &&, if the first operand is false, the second is not evaluated because '
                                        'the result must be false. For ||, if the first operand is true, the second is '
                                        'not evaluated because the result must be true.',
                              'question': 'What is short-circuit evaluation in C++ logical operations?'},
                          {   'answer': 'No. The % operator requires integer operands. For floating-point remainder, '
                                        'the fmod() function from <cmath> must be used.',
                              'question': 'Can the modulus operator (%) be used with float or double operands in '
                                          'standard C++?'},
                          {   'answer': 'Prefix (++x) increments the variable first and then returns the new value. '
                                        'Postfix (x++) returns the original value first and then increments the '
                                        'variable.',
                              'question': 'What is the difference between prefix increment (++x) and postfix increment '
                                          '(x++)?'}],
        'order': 14,
        'quizzes': [   {   'correctAnswer': '4',
                           'explanation': 'Because both 17 and 4 are integer literals, C++ performs integer division, '
                                          'which truncates (discards) the fractional remainder .25, yielding 4.',
                           'options': ['4', '4.25', '1', '5'],
                           'question': "What is the result of the integer division expression '17 / 4' in a standard "
                                       'C++ program?'},
                       {   'correctAnswer': '%',
                           'explanation': "The modulus operator ('%') calculates the remainder of integer division. "
                                          'For example, 17 % 4 evaluates to 1.',
                           'options': ['%', '/', '//', 'rem'],
                           'question': 'Which C++ arithmetic operator computes the integer remainder left over after '
                                       'dividing two integers?'},
                       {   'correctAnswer': "'==' tests whether two values are equal, while '=' assigns a value to a "
                                            'variable',
                           'explanation': "'==' is a relational operator that checks equality and returns true or "
                                          "false. '=' is an assignment operator that stores the right-hand value into "
                                          'the left-hand variable.',
                           'options': [   "'==' tests whether two values are equal, while '=' assigns a value to a "
                                          'variable',
                                          "'=' tests whether two values are equal, while '==' assigns a value",
                                          "'==' is used only with floating-point numbers",
                                          "'=' is a logical operator, while '==' is an arithmetic operator"],
                           'question': "What is the critical syntax difference between the equality operator '==' and "
                                       "the assignment operator '=' in C++?"},
                       {   'correctAnswer': '&& (Logical AND)',
                           'explanation': "The logical AND operator ('&&') requires both conditions to be true in "
                                          'order for the compound expression to evaluate to true.',
                           'options': ['&& (Logical AND)', '|| (Logical OR)', '! (Logical NOT)', '!= (Not Equal)'],
                           'question': 'In C++, which logical operator evaluates to true if and only if BOTH of its '
                                       'condition operands are true?'},
                       {   'correctAnswer': 'true (1)',
                           'explanation': 'Since 15 is greater than 10 (true) and 15 is less than 20 (true), both '
                                          'conditions are satisfied, so true && true evaluates to true (1).',
                           'options': ['true (1)', 'false (0)', 'Syntax Error', 'Undefined'],
                           'question': 'If variable x has the value 15, what is the boolean outcome of the expression '
                                       "'(x > 10 && x < 20)'?"}],
        'title': 'Lab 14: Be able to manipulate with guidance the Arithmetic and logic operations in C++'}]

DAYS_DATA = LABS_PART1 + LABS_PART2

def seed_itc_experiments_curriculum(verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds all 14 Labs for 'Intro to computing' into Neon PostgreSQL via Prisma.
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
            print(f"[*] Cleared previous records for {COURSE_DATA['title']}: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

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
                "day_num": f"Lab {day['order']}",
                "title": day["title"][:50],
                "quizzes_count": len(day["quizzes"]),
                "flashcards_count": len(day["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 85)
            print("SUMMARY TABLE: UNIVERSITY INTRO TO COMPUTING COMPLETE 14-LAB CURRICULUM SEEDED")
            print("=" * 85)
            print(f"{'Lab #':<8} | {'Title':<52} | {'Quizzes':<8} | {'Flashcards':<10}")
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
    seed_itc_experiments_curriculum()
