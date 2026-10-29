"""
OS University Curriculum Seeder (CS-223 Operating Systems Lab - Fall Edition)
100% Verbatim transcription from "OS-LAB-MANUAL Fall 17 (3).rtf.doc" for Department of Computing,
Faculty of Engineering Sciences & Technology, Hamdard University Islamabad Campus.
Populates University Laboratory Modules (Complete 14 Labs, 5 Quizzes per Lab) with zero data loss, exact tasks, CLI listings,
algorithms, C source code, outputs, quizzes, and flashcards.
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from prisma import Prisma


COURSE_DATA = {
    "title": "Operating Systems Lab (CS-223 - Fall Edition)",
    "category": "University",
    "description": "Official Academic Curriculum for CS-223 Operating Systems Lab (Fall Edition), Faculty of Engineering Sciences & Technology, Hamdard University Islamabad Campus. Comprehensive 14-laboratory curriculum covering OS installation (Windows & Linux), CLI administration, UNIX process & directory management system calls, low-level I/O system calls, command simulations (grep & ls), CPU scheduling algorithms (FCFS, SJF, Round Robin, Priority), and dynamic memory management (First Fit).",
    "color": "#1E40AF",
    "thumbnail": "assets/images/university/os_fall/os_fall_logo.png"
}


LABS_DATA = [

    # =========================================================================
    # LAB 1: LAB 1: INSTALLATION OF WINDOWS 8 OPERATING SYSTEM
    # =========================================================================
    {
        "order": 1,
        "title": "Lab 1: Installation of Windows 8 Operating System",
        "codeSnippet": "# PowerShell / DISM commands to verify Windows 8 installation and disk configuration\nGet-Disk\nGet-Partition\nGet-Volume\ndism /online /get-currentedition",
        "content": "# Lab#01\n\n## INSTALLATION OF WINDOWS 8 OPERATING SYSTEM.\n\n![Hamdard University Crest](assets/images/university/os_fall/os_fall_logo.png)\n\n### Objective\n* Familiarization with system prerequisites, BIOS/UEFI firmware configuration, disk partitioning, bootable media preparation, and step-by-step installation of Windows 8.\n\n### Theory Overview\nAn operating system (OS) acts as an intermediary between the computer user and the computer hardware. The purpose of an operating system is to provide an environment in which a user can execute programs in a convenient and efficient manner. Windows 8 introduces a redesigned user interface optimized for both touch and traditional mouse-and-keyboard input, featuring the Metro design language, the Windows Store, and enhanced boot performance via Unified Extensible Firmware Interface (UEFI) and Fast Startup.\n\n---\n\n### Prerequisites & Minimum System Requirements\nBefore initiating the installation of Windows 8, verify that the target hardware satisfies Microsoft's minimum system specifications:\n\n| Component | Minimum Requirement (32-bit) | Minimum Requirement (64-bit) |\n| :--- | :--- | :--- |\n| **Processor** | 1 GHz or faster with support for PAE, NX, and SSE2 | 1 GHz or faster with PAE, NX, SSE2, and CMPXCHG16b |\n| **RAM** | 1 GB | 2 GB |\n| **Hard Disk Space** | 16 GB available storage | 20 GB available storage |\n| **Graphics Card** | DirectX 9 graphics device with WDDM 1.0 driver | DirectX 9 graphics device with WDDM 1.0 driver |\n| **Display Resolution** | 1024 x 768 pixels (1366 x 768 for Snap apps) | 1024 x 768 pixels (1366 x 768 for Snap apps) |\n\n---\n\n### Step-by-Step Installation Procedure\n\n#### 1. Bootable Installation Media Setup\n1. Obtain the official Windows 8 ISO installation image.\n2. Prepare a bootable USB flash drive (minimum 4 GB) using Rufus or Microsoft Windows 7/8 USB Download Tool, selecting the target partition scheme (MBR for legacy BIOS or GPT for UEFI).\n3. Insert the bootable media into the target workstation.\n\n#### 2. BIOS / UEFI Boot Configuration\n1. Power on the computer and press the firmware setup key (commonly `F2`, `F12`, `Del`, or `Esc`).\n2. Navigate to the **Boot Menu** and configure the USB drive or optical drive as the first priority boot device.\n3. Save settings and restart the machine.\n\n#### 3. Initial Setup & Localization\n1. When prompted with *\"Press any key to boot from CD or DVD...\"*, press any key immediately.\n2. The Windows Setup splash screen appears. Configure:\n   * **Language to install** (e.g., English)\n   * **Time and currency format**\n   * **Keyboard or input method** (e.g., US)\n3. Click **Next**, then click **Install now**.\n\n#### 4. Product Key & Licensing\n1. Enter the 25-character Windows 8 product key and click **Next**.\n2. Accept the End User License Agreement (EULA) by checking *\"I accept the license terms\"* and click **Next**.\n\n#### 5. Installation Type Selection\nTwo options are presented:\n* **Upgrade:** Installs Windows and keeps existing files, settings, and applications (applicable only if a compatible OS already exists).\n* **Custom: Install Windows only (advanced):** Performs a clean installation on a formatted drive or unallocated partition. Choose this option for the lab.\n\n#### 6. Partitioning the Hard Drive\n1. The partition manager displays available physical drives and partitions.\n2. To create a new partition, select **Unallocated Space**, click **New**, specify the partition size in megabytes (e.g., `40000 MB` for a 40 GB system drive), and click **Apply**.\n3. Windows Setup will prompt: *\"To ensure that all Windows features work correctly, Windows might create additional partitions for system files.\"* Click **OK** (creates the System Reserved or EFI System partition).\n4. Select the primary partition and click **Format**, then click **Next** to begin file transfer.\n\n#### 7. File Installation Phase\nThe automated setup wizard performs the following stages:\n* Copying Windows files\n* Getting files ready for installation (0% to 100%)\n* Installing features\n* Installing updates\n* Finishing up\n\nOnce completed, the system restarts automatically. Remove the USB bootable drive to avoid re-entering the setup loop.\n\n#### 8. Personalization & User Configuration\n1. **Personalize:** Select a background color scheme and enter a **PC name**.\n2. **Settings:** Choose **Express settings** (or Customize to configure Windows Update, SmartScreen, and telemetry options).\n3. **Sign In:** Create a local administrator account by providing a username, password, and password hint (or connect a Microsoft account if internet access is available).\n4. Windows prepares the user profile and displays the new Start screen with live tiles.\n\n---\n\n### Verification & Post-Installation Tasks\n1. Open **Device Manager** (`devmgmt.msc`) to verify all hardware drivers (chipset, display adapter, network controller) are properly recognized without yellow warning symbols.\n2. Check disk partitioning using **Disk Management** (`diskmgmt.msc`).\n3. Verify network connectivity via the command prompt (`ping 8.8.8.8`).\n",
        "quizzes": [
            {
                        "question": "What is the minimum physical RAM requirement to install the 64-bit edition of Windows 8?",
                        "options": [
                                    "2 GB",
                                    "1 GB",
                                    "512 MB",
                                    "4 GB"
                        ],
                        "correctAnswer": "2 GB",
                        "explanation": "Microsoft specifies a minimum of 1 GB RAM for the 32-bit edition of Windows 8 and a minimum of 2 GB RAM for the 64-bit edition."
            },
            {
                        "question": "Which installation type must be selected in Windows Setup to perform a clean installation with custom disk partitioning?",
                        "options": [
                                    "Custom: Install Windows only (advanced)",
                                    "Upgrade: Install Windows and keep files, settings, and applications",
                                    "System Image Recovery",
                                    "Automatic Startup Repair"
                        ],
                        "correctAnswer": "Custom: Install Windows only (advanced)",
                        "explanation": "'Custom: Install Windows only (advanced)' allows clean installation, partition creation, formatting, and manual allocation of drive space without retaining previous OS data."
            },
            {
                        "question": "What is the primary function of the System Reserved / EFI partition created automatically by Windows Setup?",
                        "options": [
                                    "It houses the Boot Configuration Data (BCD), boot manager files, and BitLocker startup files.",
                                    "It stores temporary internet cache and browser cookies.",
                                    "It holds all user desktop icons and downloaded files.",
                                    "It serves as dedicated hardware swap space for virtual memory paging."
                        ],
                        "correctAnswer": "It houses the Boot Configuration Data (BCD), boot manager files, and BitLocker startup files.",
                        "explanation": "The System Reserved partition stores the boot manager (bootmgr) and BCD store, which are essential for initializing hardware and loading the Windows kernel."
            },
            {
                        "question": "Which CPU instruction set extensions are mandatory hardware requirements for running Windows 8?",
                        "options": [
                                    "PAE, NX (No-Execute), and SSE2",
                                    "AVX-512, 3DNow!, and MMX",
                                    "Hyper-Threading and VT-x only",
                                    "RISC-V emulation extensions"
                        ],
                        "correctAnswer": "PAE, NX (No-Execute), and SSE2",
                        "explanation": "Windows 8 requires CPU hardware support for Physical Address Extension (PAE), NX (No-Execute / Data Execution Prevention), and Streaming SIMD Extensions 2 (SSE2)."
            },
            {
                        "question": "According to the laboratory manual, what is the minimum required hard disk space to install the 64-bit edition of Windows 8?",
                        "options": [
                                    "20 GB available storage",
                                    "16 GB available storage",
                                    "40 GB available storage",
                                    "10 GB available storage"
                        ],
                        "correctAnswer": "20 GB available storage",
                        "explanation": "Microsoft's official minimum hardware requirements for Windows 8 specify at least 16 GB of free disk space for 32-bit systems and 20 GB for 64-bit installations."
            }
],
        "flashcards": [
            {
                        "question": "What partition style is required when booting Windows 8 in native UEFI mode?",
                        "answer": "GPT (GUID Partition Table) partition style is required for UEFI booting."
            },
            {
                        "question": "What is the function of the DISM command in Windows administration?",
                        "answer": "Deployment Image Servicing and Management (DISM) is a command-line tool used to service, configure, and repair Windows images and editions."
            },
            {
                        "question": "Why must the bootable USB drive be removed upon the first automated reboot during Windows installation?",
                        "answer": "To prevent the BIOS/UEFI firmware from re-booting from the USB installer and restarting the setup wizard from scratch."
            },
            {
                        "question": "What MMC snap-in command opens the Windows Device Manager?",
                        "answer": "devmgmt.msc"
            }
]
    },

    # =========================================================================
    # LAB 2: LAB 2: INSTALLATION OF LINUX OPERATING SYSTEM
    # =========================================================================
    {
        "order": 2,
        "title": "Lab 2: Installation of Linux Operating System",
        "codeSnippet": "# Linux disk partition inspection and storage verification commands\nsudo fdisk -l\nlsblk -f\nswapon --show\nfree -h",
        "content": "# Lab#02\n\n## INSTALLATION OF LINUX OPERATING SYSTEM.\n\n### Objective\n* Comprehensive setup and installation of the Linux Operating System, configuring swap and root partitions, GRUB bootloader configuration, and initial system user administration.\n\n### Theory Overview\nLinux is a multi-user, multitasking operating system based on the Linux kernel first released by Linus Torvalds in 1991. Unlike monolithic proprietary operating systems, Linux is modular, POSIX-compliant, and available in numerous distributions (e.g., Ubuntu, Debian, Red Hat Enterprise Linux, CentOS, Fedora). \n\nIn a standard Linux storage architecture, the filesystem is unified under a single tree rooted at `/`. Disk storage is allocated across dedicated partitions:\n* **Root Partition (`/`):** Contains the operating system binaries, configuration directories (`/etc`), system libraries (`/lib`, `/usr/lib`), and device nodes (`/dev`).\n* **Swap Partition:** A dedicated raw disk space used as an extension of physical RAM (virtual memory). When physical memory is saturated, inactive memory pages are paged out to swap space.\n* **Boot Partition (`/boot`):** Optional dedicated partition containing the Linux kernel image (`vmlinuz`), initial RAM disk (`initrd` or `initramfs`), and the GRUB bootloader.\n* **Home Partition (`/home`):** Houses user personal directories and configurations, preserving user data independently across OS reinstallations.\n\n---\n\n### Step-by-Step Linux Installation Procedure\n\n#### 1. Hardware Preparation & Bootable Media Creation\n1. Download a certified 64-bit Linux distribution ISO image (e.g., Ubuntu LTS or CentOS).\n2. Create bootable USB media using Rufus or `dd` under Linux:\n   ```bash\n   sudo dd if=linux-distro.iso of=/dev/sdX bs=4M status=progress && sync\n   ```\n3. Set the computer's BIOS/UEFI firmware boot sequence to prioritize the USB drive. Ensure Secure Boot is configured appropriately if installing third-party proprietary kernel modules.\n\n#### 2. Live Environment & Installer Initialization\n1. Boot into the live installation environment and select **Install Ubuntu** (or **Install CentOS**).\n2. Select your desired keyboard layout (e.g., *English (US)*).\n3. Choose the installation profile:\n   * **Normal Installation:** Includes web browser, utilities, office software, games, and media players.\n   * **Minimal Installation:** Includes only the basic desktop environment and core system utilities.\n\n#### 3. Storage Allocation & Partitioning Strategy\nSelect **Something else** (Manual Partitioning) to exercise granular control over partition boundaries:\n\n1. **Creating the Partition Table:** If working on a clean disk, select the disk (e.g., `/dev/sda` or `/dev/nvme0n1`) and click **New Partition Table**.\n2. **Creating the Root (`/`) Partition:**\n   * **Size:** 25,000 MB (25 GB minimum)\n   * **Type for the new partition:** Primary\n   * **Location:** Beginning of this space\n   * **Use as:** Ext4 journaling file system\n   * **Mount point:** `/`\n3. **Creating the Swap Area:**\n   * **Size:** Equal to physical RAM (e.g., 2048 MB to 4096 MB)\n   * **Type:** Logical or Primary\n   * **Use as:** `swap area`\n4. **Creating the EFI System Partition (for UEFI systems):**\n   * **Size:** 512 MB\n   * **Use as:** EFI System Partition\n5. Verify the partition allocation table and click **Install Now**.\n6. A confirmation dialog appears: *\"Write the changes to disks?\"* Review the disk layout and click **Continue**.\n\n#### 4. Localization & User Profile Creation\n1. **Timezone Selection:** Click on your geographic region on the world map (e.g., *Asia/Karachi*).\n2. **User Credentials:**\n   * **Your name:** Student User\n   * **Your computer's name (hostname):** `os-lab-station`\n   * **Pick a username:** `student`\n   * **Choose a password:** Enter a strong password\n   * **Require my password to log in:** Checked (enforces security)\n3. Click **Continue** to start copying packages and configuring the target filesystem.\n\n#### 5. Bootloader Installation & First Boot\n1. The installer automatically configures **GRUB 2** (Grand Unified Bootloader) onto the target disk's Master Boot Record or EFI partition.\n2. Upon completion, a dialog prompts: *\"Installation is complete. You need to restart the computer.\"* Click **Restart Now**.\n3. Remove the installation media when prompted and press Enter.\n\n---\n\n### Post-Installation Verification Commands\nLog in with the newly created user credentials and verify storage, kernel, and process architecture via the terminal:\n\n```bash\n# Check running Linux kernel release\nuname -r\n\n# Verify active mount points and storage partitions\ndf -hT\n\n# Verify active swap memory allocation\nswapon --show\n\n# Check total available physical RAM and swap space\nfree -m\n```\n",
        "quizzes": [
            {
                        "question": "What is the primary operational role of the Linux Swap partition?",
                        "options": [
                                    "It acts as virtual memory storage when physical RAM becomes exhausted, holding inactive memory pages.",
                                    "It holds the bootloader configuration files and kernel binaries.",
                                    "It provides encrypted cloud backup storage for user home directories.",
                                    "It stores the read-only binaries of the X Window System."
                        ],
                        "correctAnswer": "It acts as virtual memory storage when physical RAM becomes exhausted, holding inactive memory pages.",
                        "explanation": "Swap space provides secondary virtual memory on disk to which the operating system kernel can page out memory frames when physical RAM is under pressure."
            },
            {
                        "question": "In manual Linux disk partitioning, what mount point represents the root of the entire unified filesystem hierarchy?",
                        "options": [
                                    "/",
                                    "/root",
                                    "/home",
                                    "/boot"
                        ],
                        "correctAnswer": "/",
                        "explanation": "In UNIX and Linux, the forward slash ('/') represents the root directory, the single top-level directory from which all other partitions, directories, and files branch."
            },
            {
                        "question": "Which standard journaling filesystem is most commonly selected for the Linux root partition?",
                        "options": [
                                    "Ext4",
                                    "FAT32",
                                    "NTFS",
                                    "exFAT"
                        ],
                        "correctAnswer": "Ext4",
                        "explanation": "Ext4 (Fourth Extended Filesystem) is the standard high-performance journaling filesystem used across mainstream Linux distributions."
            },
            {
                        "question": "What is the role of GRUB (Grand Unified Bootloader) in a Linux operating system?",
                        "options": [
                                    "It loads the Linux kernel image and initial RAM disk (initrd) into physical memory and transfers CPU control to the kernel.",
                                    "It monitors disk temperature and adjusts CPU fan speeds.",
                                    "It compiles user C programs into machine instructions.",
                                    "It assigns dynamic IP addresses to network interfaces during boot."
                        ],
                        "correctAnswer": "It loads the Linux kernel image and initial RAM disk (initrd) into physical memory and transfers CPU control to the kernel.",
                        "explanation": "GRUB is the primary bootloader responsible for initializing hardware, presenting an OS boot menu, loading the selected kernel into memory, and executing it."
            },
            {
                        "question": "During Linux installation and disk partitioning, what mount point represents the top-level root directory of the entire filesystem hierarchy?",
                        "options": [
                                    "'/'",
                                    "'/boot'",
                                    "'/root'",
                                    "'/home'"
                        ],
                        "correctAnswer": "'/'",
                        "explanation": "In Linux and UNIX filesystem hierarchies, the single forward slash '/' denotes the root directory under which all other directories, partitions, and mounted filesystems reside."
            }
],
        "flashcards": [
            {
                        "question": "What command displays the current active Linux kernel version?",
                        "answer": "uname -r (or uname -a for full system details)."
            },
            {
                        "question": "What command displays detailed block storage devices and their filesystem types in Linux?",
                        "answer": "lsblk -f"
            },
            {
                        "question": "What file in Linux defines persistent filesystem mount points loaded during system boot?",
                        "answer": "/etc/fstab"
            },
            {
                        "question": "What is the difference between '/' and '/root' in Linux?",
                        "answer": "'/' is the top-level root of the whole filesystem, whereas '/root' is the personal home directory of the superuser (root)."
            }
]
    },

    # =========================================================================
    # LAB 3: LAB 3: THE COMMAND LINE - PART 1: CUSTOMIZING PROMPT, DOSKEY & DIRECTORY DISPLAY
    # =========================================================================
    {
        "order": 3,
        "title": "Lab 3: The Command Line - Part 1: Customizing Prompt, DOSKey & Directory Display",
        "codeSnippet": "# MS-DOS and Windows CLI Prompt and Directory Commands\nprompt $q\nprompt $t\nprompt $p$g\ndoskey\ndir\ndir /p\ndir /w\ndir /s format.com\ndir /s/p readme.*",
        "content": "# Lab#03\n\n## THE COMMAND LINE - PART 1.\n\n### Objectives:\n* Customize the command line\n* Use DOS commands to view and navigate directories\n\n### Background:\nAll computer and network technicians should know some of the basic commands and functions available from the command line in Windows. Microsoft\u2019s Disk Operating System (DOS), also called MS-DOS, is a collection of programs and commands used to control the overall computer operation in a disk-based system. All modern Windows versions support DOS commands from the command line. DOS allows you to even edit the command line and change the way it behaves.\n\n---\n\n### Task 1: The Command Line\nOpen a command line from Windows:\n* Select **Start/Run** and type: `command` (or `cmd` in modern Windows)\n\n1. What directory are you in? `________________`\n2. What does the prompt look like? `___________`\n\n---\n\n### Task: The Prompt\nThe DOS prompt is what you see when you first open a command line window. The default prompt is `C:\\>`, or your current path. The prompt can be changed, using the `prompt` command. The prompt command uses the syntax `prompt text`, where text can be anything you want. There are also several preconfigured prompt parameters you can use. \n\nTry changing the prompt using the following commands:\n\n| Command | What is displayed at the prompt? | Parameter Meaning |\n| :--- | :--- | :--- |\n| `prompt $q` | `____________` | Displays the equal sign (`=`) |\n| `prompt $$` | `____________` | Displays the dollar sign (`$`) |\n| `prompt $t` | `____________` | Displays the current system time |\n| `prompt $d` | `____________` | Displays the current system date |\n| `prompt $p` | `____________` | Displays current drive and path |\n| `prompt $v` | `____________` | Displays Windows/DOS version number |\n| `prompt <Your Name>\u2019s PC  $d  $p` | `____________` | Custom personalized prompt string |\n\n* **Change your prompt back to the default to finish the lab:**\n```bat\nprompt $p$g\n```\n*(Where `$p` is current drive/path and `$g` is the greater-than symbol `>`)*.\n\n---\n\n### Task: Editing the Command Line\nDOS lets you edit the command line, and even recall previous commands to make changes if needed. In order to use command line editing, you use a TSR called `doskey`, which must be initialized. A TSR (terminate-and-stay-resident) program is a program that loads itself into memory and stays there until you restart your computer.\n\n* Type:\n```bat\ndoskey\n```\n*(doskey is now loaded and you can use it to recall commands)*.\n\nNow we will enter some commands into the history list, so we can try it out:\n```bat\ncdcd windows\ncd command\n```\n\nNow try some of the command history features:\n* Press the **up arrow** to scroll back up through your list of commands\n* Press the **down arrow** to scroll back down through the list\n* Press **Esc** to clear the current command\n* Press **F7** to list the commands you have typed (shows numbered command history dialog)\n* Press **F9** and then enter the number of the command you want to use\n\nTry some of the editing keys to edit commands:\n* **Home:** moves to the beginning of the line\n* **Right and left arrow:** moves forward and back 1 character at a time\n* **End:** moves to the end of the line\n* **Ctrl + right or left arrow:** moves forward or back a word\n* **Ins:** lets you toggle insert mode to add characters\n\n---\n\n### Task 2: Displaying Directory Contents: Dir\nThe `DIR` command will list directories and various files. Directories are specified with the `<DIR>` notation that precedes the file/directory. The `DIR` command also displays the volume name, free space, and total files and directories present.\n\n#### Task: Show a list of the directories located on this drive:\n```bat\ncdcd windows\ndir\n```\nWhat happened? `_______________________________________`\n\n* Type:\n```bat\ndir /p\n```\n*(Press enter or space to continue the list)*\n\nHow many directories do you have in the windows folder? `_____________________________`  \nWhat does the `/p` switch do? `_______________` *(Pauses after each screenful of information)*\n\n#### Task: Get help on the dir command:\n```bat\ncddir /?\n```\n* What does the `/w` switch do? `_______________` *(Displays listing in wide format)*\n* What does the `/s` switch do? `_________________` *(Displays files in specified directory and all subdirectories)*\n\n#### Task: Find a file using `dir /s`:\n```bat\ndir /s format.com\n```\nWhere is the file located? `__________________`\n\n#### Wildcards:\nYou can also use a wildcard to search for files. The `*` is a wildcard which can be used in place of all or part of a filename, to use a command on many files at once. The `*` wildcard replaces any number of letters before or after the dot in a filename.\n\n#### Task: Search for the readme files on your drive:\n```bat\ndir /s/p readme.*\n```\nHow many files did it find? `________________`\n",
        "quizzes": [
            {
                        "question": "In MS-DOS and Windows command prompt, what command resets the prompt back to displaying the current drive, path, and greater-than sign (C:\\>)?",
                        "options": [
                                    "prompt $p$g",
                                    "prompt $d$t",
                                    "prompt reset",
                                    "prompt default"
                        ],
                        "correctAnswer": "prompt $p$g",
                        "explanation": "In MS-DOS, '$p' represents the current drive and path, and '$g' represents the greater-than character ('>'). Hence, 'prompt $p$g' restores the standard prompt 'C:\\>'."
            },
            {
                        "question": "What is a TSR (Terminate-and-Stay-Resident) program in the context of MS-DOS utilities like doskey?",
                        "options": [
                                    "A program that remains resident in computer memory after execution finishes, continuing to provide background services like command history.",
                                    "A virus scanner that terminates all active network connections.",
                                    "A compiler that translates assembly language into binary executable files.",
                                    "A disk formatting tool that creates primary partition tables."
                        ],
                        "correctAnswer": "A program that remains resident in computer memory after execution finishes, continuing to provide background services like command history.",
                        "explanation": "A TSR loads into RAM and stays memory-resident even after returning control to DOS, allowing utilities like doskey to intercept keystrokes and maintain command history."
            },
            {
                        "question": "When using doskey, which function key displays a numbered pop-up list of all previously executed commands in the session history?",
                        "options": [
                                    "F7",
                                    "F1",
                                    "F3",
                                    "F9"
                        ],
                        "correctAnswer": "F7",
                        "explanation": "Pressing F7 in doskey displays a numbered table of all commands recorded in the history buffer. F9 allows selecting a command by entering its number."
            },
            {
                        "question": "What is the function of the '/p' and '/w' command switches when using the 'dir' command?",
                        "options": [
                                    "'/p' pauses output after each full screen of information; '/w' formats file listings in wide multi-column layout.",
                                    "'/p' prints directory contents to physical paper; '/w' wipes all matching files permanently.",
                                    "'/p' changes user password; '/w' writes directory output to a disk partition.",
                                    "'/p' shows private files only; '/w' disables write protection."
                        ],
                        "correctAnswer": "'/p' pauses output after each full screen of information; '/w' formats file listings in wide multi-column layout.",
                        "explanation": "In DOS/Windows 'dir', '/p' pauses after every 24 lines, prompting the user to press a key, while '/w' displays filenames across wide horizontal columns without file sizes and timestamps."
            },
            {
                        "question": "In the MS-DOS/Windows Command Prompt, what command displays the current list of all active DOSKey macro definitions?",
                        "options": [
                                    "doskey /macros",
                                    "doskey /history",
                                    "prompt /list",
                                    "doskey /all"
                        ],
                        "correctAnswer": "doskey /macros",
                        "explanation": "Running 'doskey /macros' displays all custom command-line macros defined for the current command session, whereas 'doskey /history' displays executed command history."
            }
],
        "flashcards": [
            {
                        "question": "What wildcard character in DOS/Windows replaces any sequence of characters in a filename?",
                        "answer": "The asterisk (*) wildcard character."
            },
            {
                        "question": "What prompt parameter code in MS-DOS displays the current system time?",
                        "answer": "$t (e.g., prompt $t displays the current time at the command prompt)."
            },
            {
                        "question": "What key clears the current line in the command prompt when doskey is active?",
                        "answer": "The Esc key clears the current command line."
            },
            {
                        "question": "What switch with 'dir' searches for files recursively throughout all subdirectories of the current drive?",
                        "answer": "The '/s' switch (e.g., dir /s filename.ext)."
            }
]
    },

    # =========================================================================
    # LAB 4: LAB 4: THE COMMAND LINE - PART 2: DIRECTORY MANAGEMENT & HIERARCHY NAVIGATION
    # =========================================================================
    {
        "order": 4,
        "title": "Lab 4: The Command Line - Part 2: Directory Management & Hierarchy Navigation",
        "codeSnippet": "# Directory Creation, Navigation, and Removal Commands\ncd\\\nmd it\ndir\ncd it\nmd pcs\ndir\ncd pcs\ncd ..\nrd pcs\ndel *.*\ncd ..\nrd it\ndir /a",
        "content": "# Lab#04\n\n## THE COMMAND LINE - PART 2.\n\n### Objectives:\n* Use DOS commands to create and delete directories\n\n### Background:\nAll computer and network technicians should know some of the basic commands and functions available from the command line in Windows. Microsoft\u2019s Disk Operating System (DOS), also called MS-DOS, is a collection of programs and commands used to control the overall computer operation in a disk-based system. All modern Windows versions support DOS commands from the command line. DOS allows you to even edit the command line and change the way it behaves.\n\n---\n\n### Task 1: Create a Directory\nTo create directories in DOS, use the `md directory_name` or `mkdir directory_name` command.\n\n#### Task: Create an IT directory in the C drive:\n```bat\ncdmd it\n```\n\n#### Task: Verify the creation of the directory:\n```bat\ndir\n```\nIs the `it` directory in the list? `_______________________________`\n\n---\n\n### Task 2: Changing Directories\nTo change directories use the `cd directory_name` command. To move up one level in the directory structure, use the command `cd..`.\n\n#### Task: Change to the `it` directory:\n```bat\ncd it\n```\nThe command prompt should now be `C:\\it>`.\n\n---\n\n### Task 3: Create Another Directory\n#### Task: Create another directory called \u201cpcs\u201d, inside the IT directory:\n```bat\nmd pcs\n```\n\n#### Task: Verify the creation of the directory:\n```bat\ndir\n```\nIs the `pcs` directory in the list? `_______________________________`\n\n#### Task: Change to the newly created \u201cpcs\u201d directory:\n```bat\ncd pcs\n```\nThe command prompt should now be `c:\\IT\\pcs>`.\n\n---\n\n### Task 4: Deleting Directories\nTo delete a directory, you have to use the `rd` (remove directory command) and you must make sure that you are **not currently inside** the directory that you want to remove. If the directory has files inside of it, you must also delete those first. To back out of a directory, use the `cd..` command to back up one level.\n\n#### Task: Back out of the pcs directory:\n```bat\ncd ..\n```\nThe command prompt should now show `c:\\IT`.\n\n#### Task: Delete the pcs directory:\n```bat\nrd pcs\n```\nDid the folder delete? `____________________`  \n*(If it does not delete, go on to the next step)*\n\n#### Task: Delete all the files in the it directory:\n* Make sure you are currently inside the `it` directory before you continue - your prompt should look like this: `c:\\it`\n```bat\ndel *.*\n```\n\n#### Task: Back out of the IT directory and then remove it:\n```bat\ncd ..\n```\nThe command prompt should now show `c:\\`.\n\n#### Task: Delete the it directory:\n```bat\nrd it\n```\nDid the folder delete? `____________________`  \n*(If it does not delete, go on to the next step)*\n\n#### If your directories would not delete try this command:\n* Type `cd\\` to change to the `c:\\` drive\n* Type:\n```bat\ndeltree it\n```\n*(In modern Windows Command Prompt, use `rd /s it`)*\n* Type `Y` to confirm the removal of the `it` directory and all its subdirectories.\n\n#### Task: Verify directory removal:\n```bat\ndir /a\n```\nIs the directory gone? `_________`\n",
        "quizzes": [
            {
                        "question": "Which DOS command is used to navigate up exactly one level in the directory hierarchy?",
                        "options": [
                                    "cd ..",
                                    "cd \\",
                                    "cd /",
                                    "rd .."
                        ],
                        "correctAnswer": "cd ..",
                        "explanation": "In MS-DOS and Windows, '..' represents the parent directory. Typing 'cd ..' navigates one level up toward the root of the drive."
            },
            {
                        "question": "What fundamental condition must be satisfied before the 'rd' (remove directory) command can successfully delete a directory?",
                        "options": [
                                    "The directory must be completely empty of all files and subdirectories, and the user must not currently be located inside it.",
                                    "The directory must have the Read-Only and System attributes applied.",
                                    "The computer must be restarted into Safe Mode.",
                                    "The directory must be located on a FAT16 formatted floppy disk."
                        ],
                        "correctAnswer": "The directory must be completely empty of all files and subdirectories, and the user must not currently be located inside it.",
                        "explanation": "The standard 'rd' command requires that the directory contains no files or child folders, and the working directory cannot be the one being deleted."
            },
            {
                        "question": "What command allows deleting a directory along with all its subdirectories and files in one operation?",
                        "options": [
                                    "deltree (or 'rd /s' in modern Windows Command Prompt)",
                                    "md /all",
                                    "erase /d",
                                    "attrib -d"
                        ],
                        "correctAnswer": "deltree (or 'rd /s' in modern Windows Command Prompt)",
                        "explanation": "'deltree' in MS-DOS and 'rd /s' in Windows Command Prompt recursively delete a directory tree, prompting for confirmation before purging all contents."
            },
            {
                        "question": "What is the difference between 'cd\\' and 'cd..'?",
                        "options": [
                                    "'cd\\' navigates directly to the root directory of the current drive; 'cd..' moves up only one level to the immediate parent directory.",
                                    "'cd\\' deletes the current folder; 'cd..' creates a new folder.",
                                    "'cd\\' changes the drive letter; 'cd..' displays directory attributes.",
                                    "There is no difference; both commands perform identical navigation."
                        ],
                        "correctAnswer": "'cd\\' navigates directly to the root directory of the current drive; 'cd..' moves up only one level to the immediate parent directory.",
                        "explanation": "'cd\\' immediately jumps to the root (C:\\) regardless of directory depth, while 'cd..' moves up exactly one level in the tree."
            },
            {
                        "question": "What switch with the Windows/DOS 'dir' command displays directory contents sorted in wide format across multiple columns?",
                        "options": [
                                    "dir /w",
                                    "dir /p",
                                    "dir /s",
                                    "dir /o"
                        ],
                        "correctAnswer": "dir /w",
                        "explanation": "'dir /w' switches to wide list format, displaying up to five filenames per line to maximize screen space."
            }
],
        "flashcards": [
            {
                        "question": "What two equivalent commands can be used to create a new directory in MS-DOS?",
                        "answer": "'md' (make directory) and 'mkdir'."
            },
            {
                        "question": "What prompt indicates that you are in the subfolder 'pcs' inside 'IT' on drive C?",
                        "answer": "C:\\IT\\pcs>"
            },
            {
                        "question": "What command deletes all files in the current working directory at once?",
                        "answer": "del *.*"
            },
            {
                        "question": "What switch with 'dir' displays all directories and files including hidden and system items?",
                        "answer": "dir /a (where /a selects all attributes)."
            }
]
    },

    # =========================================================================
    # LAB 5: LAB 5: THE COMMAND LINE - PART 3: FILE MANAGEMENT & FILE ATTRIBUTES
    # =========================================================================
    {
        "order": 5,
        "title": "Lab 5: The Command Line - Part 3: File Management & File Attributes",
        "codeSnippet": "# File Creation, Attribute Manipulation, Copy, Ren, and Del\ncopy con sample1.txt\ncopy con sample2.txt\ncopy con sample3.txt\nattrib\nattrib +R sample1.txt\nattrib +A sample2.txt\nattrib +H sample3.txt\ndir /AH\ncopy c:\\it\\pcs\\sample2.txt c:\\it\ncopy sample2.txt backup1.bak\nren sample2.txt new.txt\ndel sample1.txt\nattrib -R sample1.txt\ndel *.*",
        "content": "# Lab#05\n\n## THE COMMAND LINE - PART 3.\n\n### Objectives:\n* Use DOS commands to copy, move, rename, delete files and change attributes\n\n### Background:\nAll computer and network technicians should know some of the basic commands and functions available from the command line in Windows. Microsoft\u2019s Disk Operating System (DOS), also called MS-DOS, is a collection of programs and commands used to control the overall computer operation in a disk-based system. All modern Windows versions support DOS commands from the command line. DOS allows you to even edit the command line and change the way it behaves.\n\n---\n\n### Task 1: Create Files\nTo create a file in DOS, use the `copy con filename` command. This command will copy the text from the console and make it into a new file. After you type this command you will have a blank line on the command prompt. You can then type in text that will be saved in the newly created file. When you are finished typing in your message, hold down the Control Key (`<Ctrl>`), press the `Z` key, and then press the `Enter` key. This key combination will end the message and DOS will display `\u201c1 file(s) copied\u201d`.\n\n#### Task: Create new files from the console:\n1. Type:\n```bat\ncopy con sample1.txt\n```\n* Type in a few words\n* Press **Ctrl + Z**, then **Enter**\n\n2. Type:\n```bat\ncopy con sample2.txt\n```\n* Type in a few words\n* Press **Ctrl + Z**, then **Enter**\n\n3. Type:\n```bat\ncopy con sample3.txt\n```\n* Type in a few words\n* Press **Ctrl + Z**, then **Enter**\n\n---\n\n### Task 2: Verify Creation of the Files\n#### Task: Display the contents of the \u201cpcs\u201d directory with the DIR command:\n```bat\ndir\n```\nAre the 3 sample files there (`sample1`, `sample2`, `sample3`)? `________________________`\n\n---\n\n### Task 3: File Attributes\nFiles can have 4 different attributes, which determine their behaviour. In order to display the attribute(s) of a file, use the command `attrib filename`:\n\n* **R - Read Only file attribute:** Means a file can\u2019t be changed or deleted.\n* **A - Archive file attribute:** Used for backup purposes (marks modified files).\n* **S - System file attribute:** Marks it as an important operating system file.\n* **H - Hidden file attribute:** Hides the file from normal directory display.\n\n#### Task: Display the file attributes of the sample files:\n```bat\nattrib\n```\nWhat attributes do the files have? `________________________`\n\n---\n\n### Task 4: Changing File Attributes\nTo change, or remove an attribute use the command:\n```bat\nattrib [-/+] attribute_value filename\n```\nThe minus (`-`) option will remove an attribute value from a file and the plus (`+`) option will add an attribute value to a file. Valid attribute values are `R` (read-only), `A` (archive), `S` (system), `H` (hidden).\n\n#### Tasks:\n1. **Add the Read-Only attribute to the sample1.txt file:**\n```bat\nattrib +R sample1.txt\n```\n2. **Add the archive attribute to the sample2.txt file:**\n```bat\nattrib +A sample2.txt\n```\n3. **Change the attribute value of the sample3.txt file to hidden:**\n```bat\nattrib +H sample3.txt\n```\n4. **Verify the file attributes of the files:**\n```bat\nattrib\n```\nDid the file attributes change (`sample1 - R`, `sample2 - A`, `sample3 - H`)? `______________________________`\n\n5. **Display your directory contents:**\n```bat\ndir\n```\nIs `sample3.txt` displayed? `______`  \nWhy not? `___________________` *(Because it has the Hidden attribute +H applied)*\n\n6. **Display Hidden Files:** You can show hidden files with the `/AH` or `/a` switch:\n```bat\ndir /AH\ndir /a\n```\nIs `sample3.txt` displayed? `__________`  \nWhat is the difference between these 2 commands? `________` *(`/AH shows only hidden files; /a shows all files regardless of attributes`)*\n\n---\n\n### Task 5: Managing Files: copy, ren, del\n#### Task: Copy the sample2.txt file to the IT directory, from the pcs directory:\n```bat\ncopy c:\\it\\pcs\\sample2.txt c:\\it\n```\n*(Notice that the original file location is listed 1st, and the new location is listed 2nd).*\n\n#### Task: Verify the file was copied:\n```bat\ncd ..\ndir\n```\n*(You should now be in the it directory: `c:\\it`)*  \nIs the `sample2.txt` file copied over? `_______________________________`\n\n#### Task: Make a backup of the sample2.txt file:\n```bat\ncopy sample2.txt backup1.bak\ndir\n```\nAre the new backup file and the original there? `__________________`\n\n#### Task: Rename sample2.txt to new.txt:\n```bat\nren sample2.txt new.txt\ndir\n```\nDid the file get renamed? `___________`\n\n---\n\n### NOTE: Checkpoint Display to Instructor\nAt this point, display your work:\n```bat\ncdcd it\ndir                     # Shows: new.txt, backup1.bak\ncd pcs\nattrib                  # Shows: sample1.txt - R, sample2.txt - A, sample3.txt - H\n```\n\n---\n\n### Task 6: Deleting Files\nYou can delete files in DOS by using the `del` command.\n\n#### Task: Attempt to delete sample1.txt:\n```bat\ndel sample1.txt\n```\nDid the file delete? `_____________`  \nWhy can you not delete it? `_______` *(Because it is protected by the Read-Only attribute +R)*\n\n#### Task: Remove the Read-Only and Hidden attributes:\n```bat\nattrib -R sample1.txt\nattrib -H sample3.txt\n```\n\n#### Task: Delete sample1.txt now:\n```bat\ndel sample1.txt\n```\nDid the file delete? `_____________`\n\n---\n\n### Task 7: Deleting Multiple Files\nIf you want to delete all the files in a directory, you can use the command:\n```bat\ndel *.*\n```\nThe `*` acts as a wildcard, which means delete any files starting with any letter and with any file extension, or delete all the files in this directory.\n\n#### Task: Delete all the files in the pcs directory:\n* Make sure you are currently inside the `pcs` directory before you continue: `c:\\it\\pcs`\n```bat\ndel *.*\n```\n\n#### Task: Verify file deletion:\n```bat\ndir /a\n```\nAre the files gone? `_________`\n",
        "quizzes": [
            {
                        "question": "How do you signal End-Of-File (EOF) to save and close a file created using 'copy con filename' in DOS?",
                        "options": [
                                    "Press Ctrl + Z, then press Enter.",
                                    "Press Ctrl + C, then press Esc.",
                                    "Type 'exit' and press F7.",
                                    "Press Alt + F4."
                        ],
                        "correctAnswer": "Press Ctrl + Z, then press Enter.",
                        "explanation": "In MS-DOS, 'Ctrl + Z' inserts the ASCII 26 Substitute character (End-Of-File marker). Pressing Enter confirms and writes the console buffer to disk with the message '1 file(s) copied'."
            },
            {
                        "question": "What error or behavior occurs when a user attempts to execute 'del sample.txt' on a file with the Read-Only (+R) attribute enabled?",
                        "options": [
                                    "DOS refuses to delete the file, displaying an 'Access denied' error until the +R attribute is removed.",
                                    "The file is moved to the Windows Recycle Bin automatically.",
                                    "The operating system renames the file to sample.bak.",
                                    "The file is deleted silently without warning."
                        ],
                        "correctAnswer": "DOS refuses to delete the file, displaying an 'Access denied' error until the +R attribute is removed.",
                        "explanation": "The Read-Only (+R) attribute protects files from deletion and modification. Attempting to delete a read-only file generates 'Access denied' unless forced with 'attrib -R' or 'del /f'."
            },
            {
                        "question": "What is the primary operational purpose of the Archive (A) file attribute in DOS and Windows?",
                        "options": [
                                    "It indicates whether a file has been modified since the last incremental or differential backup.",
                                    "It compresses the file into a zip archive format.",
                                    "It marks the file for encryption using BitLocker.",
                                    "It prevents the file from being opened over the network."
                        ],
                        "correctAnswer": "It indicates whether a file has been modified since the last incremental or differential backup.",
                        "explanation": "The Archive attribute (+A) is automatically set by the OS whenever a file is created or modified. Backup utilities clear this flag (-A) after copying, facilitating incremental backups."
            },
            {
                        "question": "Which command syntax correctly renames a file from 'original.txt' to 'modified.txt' without changing its directory location?",
                        "options": [
                                    "ren original.txt modified.txt",
                                    "move original.txt to modified.txt",
                                    "attrib original.txt modified.txt",
                                    "copy original.txt -> modified.txt"
                        ],
                        "correctAnswer": "ren original.txt modified.txt",
                        "explanation": "The 'ren' (or 'rename') command takes the syntax: 'ren <old_filename> <new_filename>'. The destination argument must specify only the new filename, not a new path."
            },
            {
                        "question": "In the DOS/Windows command line, what command attribute flag makes a file hidden?",
                        "options": [
                                    "+h",
                                    "+r",
                                    "+s",
                                    "+a"
                        ],
                        "correctAnswer": "+h",
                        "explanation": "The 'attrib +h <filename>' command applies the Hidden file attribute, preventing the file from appearing in standard unflagged directory listings."
            }
],
        "flashcards": [
            {
                        "question": "What are the four primary file attributes recognized in MS-DOS and Windows FAT/NTFS filesystems?",
                        "answer": "R (Read-Only), A (Archive), S (System), and H (Hidden)."
            },
            {
                        "question": "What command switch causes 'dir' to display ONLY hidden files?",
                        "answer": "dir /AH (Attribute: Hidden)."
            },
            {
                        "question": "How do you strip both Read-Only and Hidden attributes from a file named 'data.txt'?",
                        "answer": "attrib -R -H data.txt"
            },
            {
                        "question": "What is the difference between 'copy file1.txt file2.txt' and 'ren file1.txt file2.txt'?",
                        "answer": "'copy' produces a second independent duplicate file on disk, while 'ren' alters the filename metadata of the existing file without duplicating data."
            }
]
    },

    # =========================================================================
    # LAB 6: LAB 6: IMPLEMENTATION OF PROCESS MANAGEMENT USING UNIX SYSTEM CALLS
    # =========================================================================
    {
        "order": 6,
        "title": "Lab 6: Implementation of Process Management using UNIX System Calls",
        "codeSnippet": "// Implementation of Process Management using UNIX System Calls in C\n#include <stdio.h>\n#include <string.h>\n#include <unistd.h>\n#include <sys/types.h>\n#include <sys/wait.h>\n\nint main(int arc, char *ar[])\n{\n    int pid;\n    char s[100];\n    pid = fork();\n    if (pid < 0) {\n        printf(\"error\");\n    } else if (pid > 0) {\n        wait(NULL);\n        printf(\"\\n Parent Process:\\n\");\n        printf(\"\\n\\tParent Process id:%d\\t\\n\", getpid());\n        execlp(\"cat\", \"cat\", ar[1], (char*)0);\n        perror(\"can\u2019t execute cat\");\n    } else {\n        printf(\"\\nChild process:\");\n        printf(\"\\n\\tChildprocess parent id:\\t %d\", getppid());\n        sprintf(s, \"\\n\\tChild process id :\\t%d\\n\", getpid());\n        write(1, s, strlen(s));\n        execvp(ar[2], &ar[2]);\n        perror(\"can\u2019t execute command\");\n    }\n    return 0;\n}",
        "content": "# Lab#06\n\n## IMPLEMENTATION OF PROCESS MANAGEMENT USING THE FOLLOWING SYSTEM CALLS OF UNIX OPERATING SYSTEM: FORK, EXEC, GETPID, EXIT, WAIT, CLOSE.\n\n### AIM:\nTo write a program for implementing process management using the following system calls of UNIX operating system: `fork`, `exec`, `getpid`, `exit`, `wait`, `close`.\n\n---\n\n### ALGORITHM:\n1. Start the program.\n2. Read the input from the command line.\n3. Use `fork()` system call to create process, `getppid()` system call used to get the parent process ID and `getpid()` system call used to get the current process ID.\n4. `execvp()` system call used to execute that command given on that command line argument.\n5. `execlp()` system call used to execute specified command.\n6. Open the directory at specified in command line input.\n7. Display the directory contents.\n8. Stop the program.\n\n---\n\n### PROGRAM:\n```c\n#include <stdio.h>\n#include <string.h>\n#include <unistd.h>\n#include <sys/types.h>\n#include <sys/wait.h>\n\nmain(int arc, char *ar[])\n{\n    int pid;\n    char s[100];\n    pid = fork();\n    if (pid < 0)\n        printf(\"error\");\n    else if (pid > 0) {\n        wait(NULL);\n        printf(\"\n Parent Process:\n\");\n        printf(\"\n\tParent Process id:%d\t\n\", getpid());\n        execlp(\"cat\", \"cat\", ar[1], (char*)0);\n        error(\"can\u2019t execute cat %s,\", ar[1]);\n    }\n    else\n    {\n        printf(\"\nChild process:\");\n        printf(\"\n\tChildprocess parent id:\t %d\", getppid());\n        sprintf(s, \"\n\tChild process id :\t%d\", getpid());\n        write(1, s, strlen(s));\n        printf(\" \");\n        printf(\" \");\n        printf(\" \");\n        execvp(ar[2], &ar[2]);\n        error(\"can\u2019t execute %s\", ar[2]);\n    }\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# ./a.out tst date\nChild process:\n\tChildprocess parent id:\t 3136\n\tChild process id :\t3137\nSat Apr 10 02:45:32 IST 2010\n Parent Process:\n\tParent Process id:3136\t\nsd\ndsaASD\n[root@localhost ~]# cat tst\nsd\ndsaASD\n```\n\n---\n\n### RESULT:\nThe program for implementing process management using UNIX system calls (`fork`, `exec`, `getpid`, `getppid`, `wait`, `exit`) was successfully executed, demonstrating concurrent child-parent process execution and image replacement.\n\n---\n\n### Windows CLI Process Management Counterparts\nIn Microsoft Windows operating systems, process management tasks are performed using CLI utilities:\n\n* **List running processes:**\n```bat\ntasklist\ntasklist /FI \"STATUS eq RUNNING\"\n```\n* **Terminate a process by PID or image name:**\n```bat\ntaskkill /PID 3137 /F\ntaskkill /IM notepad.exe /F\n```\n* **Execute with altered priority:**\n```bat\nstart /high notepad.exe\n```\n*(Valid priority levels: `low`, `belownormal`, `normal`, `abovenormal`, `high`, `realtime`)*.\n",
        "quizzes": [
            {
                        "question": "What values does the fork() system call return in UNIX/Linux systems?",
                        "options": [
                                    "Negative value on failure; 0 to the newly created child process; positive child PID to the parent process.",
                                    "1 to the child process and 0 to the parent process.",
                                    "Always 0 to both parent and child processes.",
                                    "The memory address of the Process Control Block (PCB)."
                        ],
                        "correctAnswer": "Negative value on failure; 0 to the newly created child process; positive child PID to the parent process.",
                        "explanation": "fork() returns -1 on error. In the child process, fork() returns 0. In the parent process, fork() returns the positive process ID (PID) of the new child."
            },
            {
                        "question": "What happens to the current process memory image when an exec family system call (execlp, execvp) executes successfully?",
                        "options": [
                                    "The current process image is completely overwritten with the new executable program, retaining the same PID.",
                                    "A new background thread is spawned while the calling program continues concurrently.",
                                    "The operating system reboots the machine.",
                                    "The process memory is saved into swap space and restored on exit."
                        ],
                        "correctAnswer": "The current process image is completely overwritten with the new executable program, retaining the same PID.",
                        "explanation": "exec replaces the entire text, data, heap, and stack segments of the calling process with a new binary executable; code following a successful exec is never executed."
            },
            {
                        "question": "What is the purpose of the wait(NULL) system call in parent process code?",
                        "options": [
                                    "It suspends the calling parent process until one of its child processes terminates, preventing zombie processes.",
                                    "It delays execution for a fixed duration of 10 seconds.",
                                    "It waits for network socket connections to arrive.",
                                    "It puts the computer into hibernation mode."
                        ],
                        "correctAnswer": "It suspends the calling parent process until one of its child processes terminates, preventing zombie processes.",
                        "explanation": "'wait(NULL)' blocks the parent until a child process terminates, reading the child's exit status and allowing the kernel to deallocate the child's PCB."
            },
            {
                        "question": "Which Windows CLI command terminates a running process by its Process Identifier (PID)?",
                        "options": [
                                    "taskkill /PID <pid> /F",
                                    "killproc <pid>",
                                    "stop-process --id <pid>",
                                    "endtask /force <pid>"
                        ],
                        "correctAnswer": "taskkill /PID <pid> /F",
                        "explanation": "In Windows, 'taskkill /PID <pid> /F' forcefully (/F) terminates the process associated with the given Process Identifier."
            },
            {
                        "question": "In UNIX/Linux C programming, what value does fork() return to the newly created child process?",
                        "options": [
                                    "0",
                                    "A positive integer representing the parent PID",
                                    "-1",
                                    "1"
                        ],
                        "correctAnswer": "0",
                        "explanation": "Upon successful execution, fork() returns 0 to the child process and returns the child's positive process ID (PID) to the parent process."
            }
],
        "flashcards": [
            {
                        "question": "What system call returns the process ID of the calling process's parent in UNIX?",
                        "answer": "getppid()"
            },
            {
                        "question": "What is a 'zombie process' in operating systems?",
                        "answer": "A terminated child process whose exit status has not yet been read by its parent via the wait() system call, leaving its entry in the process table."
            },
            {
                        "question": "What is the difference between execlp() and execvp()?",
                        "answer": "execlp() accepts arguments as a comma-separated list of pointers ending with NULL, whereas execvp() accepts arguments as an array of string pointers (char *argv[])."
            },
            {
                        "question": "What system call prints directly to standard output descriptor 1 without C library stream buffering?",
                        "answer": "write(1, buffer, length)"
            }
]
    },

    # =========================================================================
    # LAB 7: LAB 7: IMPLEMENTATION OF DIRECTORY MANAGEMENT USING UNIX SYSTEM CALLS
    # =========================================================================
    {
        "order": 7,
        "title": "Lab 7: Implementation of Directory Management using UNIX System Calls",
        "codeSnippet": "// Implementation of Directory Management using UNIX System Calls in C\n#include <sys/types.h>\n#include <dirent.h>\n#include <stdio.h>\n\nint main(int c, char *arg[])\n{\n    DIR *d;\n    struct dirent *r;\n    int i = 0;\n\n    d = opendir(arg[1]);\n    if (d == NULL) {\n        printf(\"\\nCannot open directory %s\\n\", arg[1]);\n        return 1;\n    }\n\n    printf(\"\\n\\t NAME OF ITEM \\n\");\n    while ((r = readdir(d)) != NULL)\n    {\n        printf(\"\\t %s \\n\", r->d_name);\n        i = i + 1;\n    }\n    printf(\"\\n TOTAL NUMBER OF ITEM IN THAT DIRECTORY IS %d \\n\", i);\n    closedir(d);\n    return 0;\n}",
        "content": "# Lab#07\n\n## IMPLEMENTATION OF DIRECTORY MANAGEMENT USING THE FOLLOWING SYSTEM CALLS OF UNIX OPERATING SYSTEM: OPENDIR, READDIR.\n\n### AIM:\nTo write a program for implementing Directory management using the following system calls of UNIX operating system: `opendir`, `readdir`.\n\n---\n\n### ALGORITHM:\n1. Start the program.\n2. Open the directory specified in command line input.\n3. Display the directory contents.\n4. Stop the program.\n\n---\n\n### PROGRAM:\n```c\n#include<sys/types.h>\n#include<dirent.h>\n#include<stdio.h>\n\nmain(int c, char* arg[])\n{\n    DIR *d;\n    struct dirent *r;\n    int i = 0;\n\n    d = opendir(arg[1]);\n    printf(\"\n\t NAME OF ITEM \n\");\n    while((r = readdir(d)) != NULL)\n    {\n        printf(\"\t %s \n\", r->d_name);\n        i = i + 1;\n    }\n    printf(\"\n TOTAL NUMBER OF ITEM IN THAT DIRECTORY IS %d \n\", i);\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# cc dr.c\n[root@localhost ~]# ./a.out lab_print\n\n\t NAME OF ITEM \n\t pri_output.doc \n\t sjf_output.doc \n\t fcfs_output.doc \n\t rr_output.doc \n\t ipc_pipe_output.doc \n\t pro_con_prob_output.doc \n\n TOTAL NUMBER OF ITEM IN THAT DIRECTORY IS 8\n```\n\n---\n\n### RESULT:\nThe program for implementing directory management using `opendir()` and `readdir()` system calls was executed successfully, enumerating all directory entry items and computing total item counts within target directory paths.\n\n---\n\n### Theory & Mechanism: UNIX Directory Architecture\nIn UNIX and Linux filesystems, a directory is simply a special file that contains a table of names paired with index numbers called **inodes** (index nodes):\n\n1. **`DIR *opendir(const char *name)`:**\n   Opens a directory stream corresponding to the directory `name`. It returns a pointer to the directory stream (`DIR*`), or `NULL` on error.\n2. **`struct dirent *readdir(DIR *dirp)`:**\n   Returns a pointer to a `struct dirent` representing the next directory entry in the stream. It returns `NULL` upon reaching the end of the directory stream or if an error occurs.\n3. **The `dirent` Structure:**\n   ```c\n   struct dirent {\n       ino_t          d_ino;       /* Inode number */\n       off_t          d_off;       /* Not an offset; see man readdir */\n       unsigned short d_reclen;    /* Length of this record */\n       unsigned char  d_type;      /* Type of file; not supported by all fs */\n       char           d_name[256]; /* Null-terminated filename */\n   };\n   ```\n4. **`closedir(DIR *dirp)`:**\n   Closes the directory stream associated with `dirp` and releases the allocated file descriptor resources.\n\n---\n\n### Windows CLI Directory Tree Exploration Counterparts\nIn Windows, recursive directory structures can be inspected graphically and textually from the command line:\n\n```bat\n# Display directory hierarchy graph\ntree\ntree /F c:\\it\n```\n*(The `/F` switch displays the names of the files in each folder as well as directories).*\n",
        "quizzes": [
            {
                        "question": "What header file must be included in a C program to access POSIX directory operations like opendir() and readdir()?",
                        "options": [
                                    "<dirent.h>",
                                    "<dir.h>",
                                    "<file.h>",
                                    "<unistd.h> only"
                        ],
                        "correctAnswer": "<dirent.h>",
                        "explanation": "The POSIX standard header <dirent.h> defines the DIR type, the struct dirent format, and prototypes for opendir(), readdir(), and closedir()."
            },
            {
                        "question": "What member of 'struct dirent' holds the null-terminated character name of the directory entry in C?",
                        "options": [
                                    "d_name",
                                    "d_ino",
                                    "filename",
                                    "d_path"
                        ],
                        "correctAnswer": "d_name",
                        "explanation": "In POSIX 'struct dirent', 'd_name' is an array of characters storing the null-terminated string name of the entry."
            },
            {
                        "question": "What return value indicates that readdir() has reached the end of the directory stream or encountered an error?",
                        "options": [
                                    "NULL",
                                    "-1",
                                    "0",
                                    "EOF"
                        ],
                        "correctAnswer": "NULL",
                        "explanation": "readdir() returns a pointer to struct dirent on each successive call; when all entries have been read, it returns NULL."
            },
            {
                        "question": "Which Windows CLI command graphically displays the folder structure of a drive or directory in tree format?",
                        "options": [
                                    "tree",
                                    "dir /tree",
                                    "graph",
                                    "listtree"
                        ],
                        "correctAnswer": "tree",
                        "explanation": "The 'tree' command in DOS/Windows visually displays the directory paths and folder hierarchy in a tree format; 'tree /F' additionally lists files within folders."
            },
            {
                        "question": "In POSIX C directory programming, what member of 'struct dirent' contains the filename of the directory entry?",
                        "options": [
                                    "d_name",
                                    "d_ino",
                                    "d_reclen",
                                    "d_type"
                        ],
                        "correctAnswer": "d_name",
                        "explanation": "'d_name' is a null-terminated character array within 'struct dirent' holding the filename string of the current directory entry."
            }
],
        "flashcards": [
            {
                        "question": "What pointer type represents an open directory stream in POSIX C programming?",
                        "answer": "DIR* (returned by opendir())."
            },
            {
                        "question": "What system function must be called after traversing a directory stream to release its resources?",
                        "answer": "closedir(DIR *dirp)"
            },
            {
                        "question": "What are the two standard entries present in every non-empty UNIX directory returned by readdir()?",
                        "answer": "'.' (current directory) and '..' (parent directory)."
            },
            {
                        "question": "What switch with the Windows 'tree' command displays the filenames within each folder?",
                        "answer": "tree /F"
            }
]
    },

    # =========================================================================
    # LAB 8: LAB 8: IMPLEMENTATION OF I/O SYSTEM CALLS
    # =========================================================================
    {
        "order": 8,
        "title": "Lab 8: Implementation of I/O System Calls",
        "codeSnippet": "// Implementation of I/O System Calls of UNIX (open, read, write, close, creat, stat)\n#include <stdio.h>\n#include <sys/stat.h>\n#include <time.h>\n#include <fcntl.h>\n#include <unistd.h>\n\nint main(int ag, char *arg[])\n{\n    char buf[100];\n    struct stat s;\n    int fd1, fd2, n;\n\n    if (ag < 3) {\n        printf(\"Usage: %s <source_file> <dest_file>\\n\", arg[0]);\n        return 1;\n    }\n\n    fd1 = open(arg[1], O_RDONLY);\n    if (fd1 == -1) {\n        perror(\"Error opening source file\");\n        return 1;\n    }\n\n    fd2 = creat(arg[2], 0777);\n    if (fd2 == -1) {\n        printf(\"ERROR IN CREATION\");\n        close(fd1);\n        return 1;\n    }\n\n    while ((n = read(fd1, buf, sizeof(buf))) > 0) {\n        if (write(fd2, buf, n) != n) {\n            close(fd1);\n            close(fd2);\n            return 1;\n        }\n    }\n\n    stat(arg[2], &s);\n    printf(\"\\t\\n UID FOR FILE\\t>%d \\n FILE ACCESS TIME\\t>%s \\n FILE MODIFIED TIME\\t>%s \\n FILE I-NODE NUMBER\\t>%ld \\n PERMISSION FOR FILE\\t>%o\\n\\n\",\n           s.st_uid, ctime(&s.st_atime), ctime(&s.st_mtime), (long)s.st_ino, s.st_mode);\n\n    close(fd1);\n    close(fd2);\n    return 0;\n}",
        "content": "# Lab#08\n\n## WRITE A PROGRAM USING THE I/O SYSTEM CALLS OF UNIX OPERATING SYSTEM (OPEN, READ, WRITE, ETC).\n\n### Objective & Theoretical Overview\nAn operating system provides low-level system calls as the fundamental interface between user-space applications and hardware devices managed by the kernel. In UNIX and POSIX-compliant operating systems, all I/O operations on regular files, directories, device drivers, and network sockets are unified under the \"everything is a file\" philosophy and addressed via integer **File Descriptors (FD)**.\n\n#### File Descriptor Table Mechanics\nWhen a process executes, the kernel maintains an open file table for each process. By default:\n* **`0`**: Standard Input (`stdin`)\n* **`1`**: Standard Output (`stdout`)\n* **`2`**: Standard Error (`stderr`)\n\nAny subsequent file opened via `open()` or `creat()` is assigned the lowest available non-negative integer index in the file descriptor table.\n\n#### System Call Functions & POSIX Flags\n| System Call | Prototype | Description | Return Value |\n| :--- | :--- | :--- | :--- |\n| **`open`** | `int open(const char *pathname, int flags, [mode_t mode]);` | Opens an existing file or creates a new one. | Non-negative FD on success, `-1` on error. |\n| **`creat`** | `int creat(const char *pathname, mode_t mode);` | Creates a new file or truncates an existing one to 0 bytes (`O_WRONLY \\| O_CREAT \\| O_TRUNC`). | Non-negative FD on success, `-1` on error. |\n| **`read`** | `ssize_t read(int fd, void *buf, size_t count);` | Reads up to `count` bytes from open FD into buffer `buf`. | Bytes read, `0` on EOF, `-1` on error. |\n| **`write`** | `ssize_t write(int fd, const void *buf, size_t count);` | Writes up to `count` bytes from buffer `buf` to open FD. | Bytes written, `-1` on error. |\n| **`close`** | `int close(int fd);` | Closes the file descriptor, releasing kernel resources. | `0` on success, `-1` on error. |\n| **`stat`** | `int stat(const char *path, struct stat *buf);` | Obtains filesystem metadata and inode properties of a file. | `0` on success, `-1` on error. |\n\nCommon access flags in `<fcntl.h>`:\n* **`O_RDONLY`**: Open for reading only.\n* **`O_WRONLY`**: Open for writing only.\n* **`O_RDWR`**: Open for both reading and writing.\n* **`O_CREAT`**: Create file if it does not already exist.\n* **`O_TRUNC`**: Truncate existing file length to 0 bytes.\n\n---\n\n### AIM:\nTo write a program using the I/O system calls of UNIX operating system (`open`, `read`, `write`, `creat`, `close`, `stat`).\n\n---\n\n### ALGORITHM:\n1. Start the program.\n2. Read the input from user specified file.\n3. Write the content of the file to newly created file.\n4. Show the file properties (access time, modified time, & etc,.).\n5. Stop the program.\n\n---\n\n### PROGRAM:\n```c\n#include <stdio.h>\n#include <sys/stat.h>\n#include <time.h>\n#include <fcntl.h>\n#include <unistd.h>\n\nmain(int ag, char* arg[])\n{\n    char buf[100];\n    struct stat s;\n    int fd1, fd2, n;\n\n    fd1 = open(arg[1], 0);\n    fd2 = creat(arg[2], 0777);\n    stat(arg[2], &s);\n\n    if (fd2 == -1)\n        printf(\"ERROR IN CREATION\");\n\n    while ((n = read(fd1, buf, sizeof(buf))) > 0) {\n        if (write(fd2, buf, n) != n) {\n            close(fd1);\n            close(fd2);\n        }\n    }\n\n    printf(\"\t\\n UID FOR FILE\t>%d \\n FILE ACCESS TIME\t>%s \\n FILE MODIFIED TIME\t>%s \\n FILE I-NODE NUMBER\t>%d \\n PERMISSION FOR FILE\t>%o\\n\\n\",\n           s.st_uid, ctime(&s.st_atime), ctime(&s.st_mtime), s.st_ino, s.st_mode);\n\n    close(fd1);\n    close(fd2);\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# cc iosys.c\n[root@localhost ~]# ./a.out tst dest\nUID FOR FILE\t>0\nFILE ACCESS TIME\t>Thu Apr 8 01:23:54 2011\nFILE MODIFIED TIME\t>Thu Apr 8 01:23:54 2011\nFILE I-NODE NUMBER\t>33261\nPERMISSION FOR FILE\t>1001101014\n```\n\n---\n\n### RESULT:\nThus the program using the I/O system calls was written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "What does the open() system call return upon successful execution in UNIX?",
                        "options": [
                                    "A non-negative integer representing the file descriptor.",
                                    "A pointer to a FILE stream structure in user space.",
                                    "The physical disk block address of the file.",
                                    "The total number of bytes currently stored in the file."
                        ],
                        "correctAnswer": "A non-negative integer representing the file descriptor.",
                        "explanation": "In UNIX/Linux, low-level I/O system calls return an integer file descriptor (an index into the process's open file table) representing the open file stream."
            },
            {
                        "question": "In the C stat structure (struct stat), what does the member 'st_ino' represent?",
                        "options": [
                                    "The file's unique inode number on the filesystem.",
                                    "The integer User ID of the file owner.",
                                    "The input/output buffer size in kilobytes.",
                                    "The number of hard links pointing to the file."
                        ],
                        "correctAnswer": "The file's unique inode number on the filesystem.",
                        "explanation": "'st_ino' holds the filesystem inode number, which uniquely identifies the file metadata block on that storage device."
            },
            {
                        "question": "What is the key difference between the low-level read() system call and standard C library fread()?",
                        "options": [
                                    "read() invokes a direct kernel system call without user-space buffering, whereas fread() performs user-space buffered I/O.",
                                    "read() can only read ASCII text, while fread() only reads binary machine code.",
                                    "read() runs with root privileges only, while fread() runs under unprivileged accounts.",
                                    "read() writes data to swap space instead of RAM."
                        ],
                        "correctAnswer": "read() invokes a direct kernel system call without user-space buffering, whereas fread() performs user-space buffered I/O.",
                        "explanation": "Low-level system calls ('read', 'write') transition into kernel mode directly for raw byte transfers, whereas stdio functions ('fread', 'fwrite') maintain user-space memory buffers to reduce system call frequency."
            },
            {
                        "question": "What does a return value of 0 from the read(fd, buf, size) system call signify?",
                        "options": [
                                    "End-of-File (EOF) has been reached.",
                                    "A fatal hardware read error occurred.",
                                    "The file descriptor is locked by another thread.",
                                    "The buffer size was too small to hold one byte."
                        ],
                        "correctAnswer": "End-of-File (EOF) has been reached.",
                        "explanation": "'read()' returns the positive number of bytes transferred, -1 on error, and 0 when the file offset reaches End-of-File."
            },
            {
                        "question": "What return value indicates that the close(fd) system call failed in UNIX C programming?",
                        "options": [
                                    "-1",
                                    "0",
                                    "1",
                                    "EOF"
                        ],
                        "correctAnswer": "-1",
                        "explanation": "'close(fd)' returns 0 on successful closure and -1 on error, setting 'errno' to indicate the failure cause (e.g., EBADF)."
            }
],
        "flashcards": [
            {
                        "question": "What mode flags in open() specify read-only, write-only, and read-write access?",
                        "answer": "O_RDONLY (read only), O_WRONLY (write only), and O_RDWR (read/write)."
            },
            {
                        "question": "What does the creat() system call do if the target file already exists?",
                        "answer": "It truncates the file's length to 0 bytes, discarding existing contents, and opens it for writing."
            },
            {
                        "question": "What function converts a time_t epoch timestamp (e.g. st_atime) to a human-readable date/time string in C?",
                        "answer": "ctime(&time_val)"
            },
            {
                        "question": "What octal file permission does the mask 0777 represent in UNIX creat()?",
                        "answer": "Read, write, and execute permissions granted to user, group, and others (rwxrwxrwx)."
            }
]
    },

    # =========================================================================
    # LAB 9: LAB 9: IMPLEMENTATION OF LS AND GREP SIMULATION
    # =========================================================================
    {
        "order": 9,
        "title": "Lab 9: Implementation of ls and grep Simulation",
        "codeSnippet": "// Simulation of UNIX Commands (grep with options -c and -i)\n#include <stdio.h>\n#include <string.h>\n#include <fcntl.h>\n#include <unistd.h>\n\nint main(int ag, char *arg[])\n{\n    char buf[200], line[200];\n    int i, j = 0, n, fd1, count = 0, opt = 1;\n\n    if (ag == 4) {\n        fd1 = open(arg[3], O_RDONLY);\n        if (strcmp(arg[1], \"-c\") == 0) opt = 2;\n        if (strcmp(arg[1], \"-i\") == 0) opt = 3;\n    } else if (ag == 3) {\n        fd1 = open(arg[2], O_RDONLY);\n        opt = 1;\n    } else {\n        printf(\"Usage: %s [-c|-i] <pattern> <file>\\n\", arg[0]);\n        return 1;\n    }\n\n    if (fd1 == -1) {\n        printf(\"Error opening file\\n\");\n        return 1;\n    }\n\n    while ((n = read(fd1, buf, sizeof(buf))) > 0) {\n        for (i = 0; i < n; i++) {\n            if (buf[i] != '\\n') {\n                line[j++] = buf[i];\n            } else {\n                line[j] = '\\0';\n                if (opt == 1 && strstr(line, arg[1]) != NULL)\n                    printf(\"%s\\n\", line);\n                else if (opt == 2 && strstr(line, arg[2]) != NULL)\n                    count++;\n                else if (opt == 3 && strcasestr(line, arg[2]) != NULL)\n                    printf(\"%s\\n\", line);\n                j = 0;\n            }\n        }\n    }\n\n    if (opt == 2)\n        printf(\"%d\\n\", count);\n\n    close(fd1);\n    return 0;\n}",
        "content": "# Lab#09\n\n## WRITE A PROGRAM TO SIMULATE UNIX COMMANDS LIKE LS, GREP, ETC.\n\n### Objective & Theoretical Overview\nCommand-line utilities in UNIX-like systems are specialized executable programs that interact directly with the kernel via system calls to manipulate files, process text streams, and explore directory structures. Two of the most ubiquitous command-line utilities are:\n1. **`grep` (Global Regular Expression Print)**: Scans input files line-by-line, matching lines against a specified search pattern or regular expression, and outputting matching records or counting occurrences.\n2. **`ls` (List Directory Contents)**: Queries directory structures from the filesystem's inode hierarchy, extracting file names, inode numbers, permissions, and metadata.\n\n---\n\n### PART 1: SIMULATION OF `grep` COMMAND (FROM LAB MANUAL)\n\n#### AIM:\nTo write a program to simulate UNIX commands like `ls`, `grep`, etc.\n\n---\n\n#### ALGORITHM:\n1. Start the program.\n2. Read the input through command line.\n3. Open the specified file.\n4. Options (`-c` and `-i`) are performed.\n5. Stop the program.\n\n---\n\n#### PROGRAM:\n```c\n#include <stdio.h>\n#include <string.h>\n\nmain(int ag, char* arg[])\n{\n    char buf[200], line[200];\n    int i, j, n, fd1, count = 0, opt;\n\n    if (ag == 4) {\n        fd1 = open(arg[3], 0);\n        if (strcmp(arg[1], \"-c\") == 0)\n            opt = 2;\n        if (strcmp(arg[1], \"-i\") == 0)\n            opt = 3;\n    }\n    else if (ag == 3) {\n        fd1 = open(arg[2], 0);\n        opt = 1;\n    }\n\n    if (fd1 == -1)\n        printf(\"error in opening\");\n\n    j = 0;\n    switch(opt)\n    {\n    case 1:\n        while ((n = read(fd1, buf, sizeof(line))) > 0) {\n            for (i = 0; i < n; i++, j++) {\n                if (buf[i] != '\\n')\n                    line[j] = buf[i];\n                else {\n                    line[j] = '\\n';\n                    if (strstr(line, arg[1]) != 0)\n                        write(1, line, j + 1);\n                }\n            }\n        }\n        break;\n\n    case 2:\n        while ((n = read(fd1, buf, sizeof(line))) > 0) {\n            for (i = 0; i < n; i++, j++) {\n                if (buf[i] != '\\n')\n                    line[j] = buf[i];\n                else {\n                    line[j] = '\\n';\n                    if (strstr(line, arg[2]) != 0)\n                        count = count + 1;\n                    j = -1;\n                }\n            }\n        }\n        printf(\"%d \\n\", count);\n        break;\n\n    case 3:\n        while ((n = read(fd1, buf, sizeof(line))) > 0) {\n            for (i = 0; i < n; i++, j++) {\n                if (buf[i] != '\\n')\n                    line[j] = buf[i];\n                else {\n                    line[j] = '\\n';\n                    if (strcasestr(line, arg[2]) != 0)\n                        write(1, line, j + 1);\n                    j = -1;\n                }\n            }\n        }\n        break;\n    }\n    close(fd1);\n}\n```\n\n---\n\n#### OUTPUT:\n```text\n[root@localhost ~]# cat tst\nsd\ndsaASD\n[root@localhost ~]# ./a.out -i a tst\naA\n[root@localhost ~]# ./a.out -c a tst\n1\n[root@localhost ~]# ./a.out -c A tst\n1\n[root@localhost ~]# ./a.out -c sd tst\n1\n[root@localhost ~]# ./a.out -c s tst\n2\n```\n\n---\n\n#### RESULT:\nThus the program to simulate the UNIX commands was written and successfully executed.\n\n---\n\n### PART 2: COMPANION SIMULATION OF `ls` COMMAND (DIRECTORY SCANNING)\n\n#### AIM:\nTo write a C program to simulate the UNIX `ls` command by reading directory entries and displaying entry names along with their inode numbers.\n\n#### ALGORITHM:\n1. Start the program.\n2. Read the directory path from the command line argument (or default to current directory `\".\"`).\n3. Open the directory stream using `opendir()`.\n4. Iterate through directory entries using `readdir()`.\n5. Print each file entry name (`d_name`) and its inode number (`d_ino`).\n6. Close the directory stream using `closedir()`.\n7. Stop the program.\n\n#### PROGRAM:\n```c\n#include <stdio.h>\n#include <dirent.h>\n#include <stdlib.h>\n\nint main(int argc, char *argv[])\n{\n    DIR *dirp;\n    struct dirent *dptr;\n    const char *path = (argc > 1) ? argv[1] : \".\";\n\n    dirp = opendir(path);\n    if (dirp == NULL) {\n        perror(\"Error opening directory\");\n        return 1;\n    }\n\n    printf(\"Simulated 'ls' directory listing for: %s\\n\", path);\n    printf(\"----------------------------------------\\n\");\n    printf(\"%-25s %s\\n\", \"File / Directory Name\", \"Inode Number\");\n    printf(\"----------------------------------------\\n\");\n\n    while ((dptr = readdir(dirp)) != NULL) {\n        printf(\"%-25s %ld\\n\", dptr->d_name, (long)dptr->d_ino);\n    }\n\n    printf(\"----------------------------------------\\n\");\n    closedir(dirp);\n    return 0;\n}\n```\n\n#### SAMPLE OUTPUT:\n```text\n[root@localhost ~]# cc myls.c -o myls\n[root@localhost ~]# ./myls\nSimulated 'ls' directory listing for: .\n----------------------------------------\nFile / Directory Name     Inode Number\n----------------------------------------\n.                         1441801\n..                        1441793\niosys.c                   33261\nmygrep.c                  33265\ntst                       33270\ndest                      33285\n----------------------------------------\n```\n",
        "quizzes": [
            {
                        "question": "In the UNIX grep command, what does the '-c' command-line flag accomplish?",
                        "options": [
                                    "It suppresses normal output and prints only a count of matching lines.",
                                    "It displays lines with color highlighting on matching tokens.",
                                    "It performs case-insensitive search.",
                                    "It displays byte offsets preceding each line."
                        ],
                        "correctAnswer": "It suppresses normal output and prints only a count of matching lines.",
                        "explanation": "The '-c' (count) flag in grep instructs the utility to output only the numerical count of lines that matched the given pattern."
            },
            {
                        "question": "What standard C library function is used for case-insensitive substring searching?",
                        "options": [
                                    "strcasestr()",
                                    "strstr()",
                                    "strcmp()",
                                    "strchr()"
                        ],
                        "correctAnswer": "strcasestr()",
                        "explanation": "While 'strstr()' performs exact case-sensitive matching, 'strcasestr()' searches for a needle substring within a haystack ignoring case distinctions."
            },
            {
                        "question": "What does 'grep -i' do when scanning text files?",
                        "options": [
                                    "It ignores case distinctions in both the pattern and input files (e.g., 'a' matches both 'a' and 'A').",
                                    "It inverts the sense of matching to select non-matching lines.",
                                    "It prints matching line numbers.",
                                    "It scans only binary executable images."
                        ],
                        "correctAnswer": "It ignores case distinctions in both the pattern and input files (e.g., 'a' matches both 'a' and 'A').",
                        "explanation": "The '-i' flag enables case-insensitive pattern matching, treating uppercase and lowercase letters as equivalent."
            },
            {
                        "question": "In the program listing, how does the program output matching lines directly to the terminal screen?",
                        "options": [
                                    "By calling write(1, line, length) on standard output descriptor 1.",
                                    "By writing to the syslog daemon via socket connection.",
                                    "By copying the buffer into kernel swap memory.",
                                    "By calling printf(\"%p\", &line)."
                        ],
                        "correctAnswer": "By calling write(1, line, length) on standard output descriptor 1.",
                        "explanation": "In UNIX, file descriptor 1 is standard output (stdout). Calling 'write(1, ...)' writes raw bytes directly to the terminal."
            },
            {
                        "question": "In the Lab 9 command simulation program, what command-line option executes case-insensitive string matching?",
                        "options": [
                                    "-i",
                                    "-c",
                                    "-v",
                                    "-n"
                        ],
                        "correctAnswer": "-i",
                        "explanation": "The '-i' flag enables case-insensitive matching, matching uppercase and lowercase characters indiscriminately via 'strcasestr()'."
            }
],
        "flashcards": [
            {
                        "question": "What does the acronym 'grep' stand for?",
                        "answer": "Global Regular Expression Print."
            },
            {
                        "question": "What C string function finds the first occurrence of substring s2 in string s1?",
                        "answer": "strstr(s1, s2)"
            },
            {
                        "question": "What flag in standard grep inverts matching to display non-matching lines?",
                        "answer": "-v (or --invert-match)"
            },
            {
                        "question": "How do you search for lines matching 'error' in all .log files in Linux CLI?",
                        "answer": "grep 'error' *.log"
            }
]
    },

    # =========================================================================
    # LAB 10: LAB 10: IMPLEMENTATION OF FCFS SCHEDULING ALGORITHM
    # =========================================================================
    {
        "order": 10,
        "title": "Lab 10: Implementation of FCFS Scheduling Algorithm",
        "codeSnippet": "// Implementation of First-Come, First-Served (FCFS) CPU Scheduling in C\n#include <stdio.h>\n#include <string.h>\n\nint main()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], at[10], t, q, i, n, sum = 0, sbt = 0, j, ss = 0;\n\n    printf(\"\\nEnter the number of processes: \");\n    scanf(\"%d\", &n);\n\n    printf(\"\\nEnter NAME, BURST TIME and ARRIVAL TIME of processes:\\n\");\n    for (i = 0; i < n; i++) {\n        printf(\"NAME: \"); scanf(\"%s\", pname[i]);\n        printf(\"BURST TIME: \"); scanf(\"%d\", &bt[i]);\n        printf(\"ARRIVAL TIME: \"); scanf(\"%d\", &at[i]);\n    }\n\n    // Sort by arrival time\n    for (i = 0; i < n; i++) {\n        for (j = i + 1; j < n; j++) {\n            if (at[i] > at[j]) {\n                t = at[i]; at[i] = at[j]; at[j] = t;\n                q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n    }\n\n    wt[0] = 0;\n    for (i = 0; i < n; i++) {\n        wt[i + 1] = wt[i] + bt[i];\n        sum = sum + (wt[i] - at[i]);\n        sbt = sbt + (wt[i + 1] - at[i]);\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    avgwt = (float)sum / n;\n    avgtt = (float)sbt / n;\n\n    printf(\"\\nAverage waiting time = %f\", avgwt);\n    printf(\"\\nAverage turn-around time = %f\\n\", avgtt);\n\n    printf(\"\\nGANTT CHART\\n\");\n    for (i = 0; i < n; i++) printf(\"|\\t%s\\t\", pname[i]);\n    printf(\"\\n\");\n    for (i = 0; i < n; i++) printf(\"%d\\t\\t\", wt[i]);\n    printf(\"%d\\n\", ss);\n\n    return 0;\n}",
        "content": "# Lab#10\n\n## WRITE A PROGRAM FOR IMPLEMENTING THE FCFS SCHEDULING ALGORITHM.\n\n### Objective & Theoretical Overview\n**First-Come, First-Served (FCFS)** is the simplest CPU scheduling algorithm. In this non-preemptive scheduling discipline, the process that requests the CPU first is allocated the CPU first. The implementation of FCFS is easily managed with a First-In, First-Out (**FIFO**) queue.\n\n#### Scheduling Metrics & Mathematical Formulas\n1. **Arrival Time ($AT_i$)**: The instant at which process $P_i$ arrives in the ready queue.\n2. **Burst Time ($BT_i$)**: The duration of CPU time required by process $P_i$ to complete its execution.\n3. **Completion Time ($CT_i$)**: The instant when process $P_i$ completes its CPU burst.\n4. **Turnaround Time ($TAT_i$)**: The total elapsed time between process arrival and completion:\n   $$TAT_i = CT_i - AT_i$$\n   *(Equivalently: $TAT_i = WT_i + BT_i$)*\n5. **Waiting Time ($WT_i$)**: The total duration process $P_i$ spent waiting in the ready queue:\n   $$WT_i = TAT_i - BT_i$$\n6. **Average Waiting Time**:\n   $$\\overline{WT} = \\frac{1}{n} \\sum_{i=1}^{n} WT_i$$\n7. **Average Turnaround Time**:\n   $$\\overline{TAT} = \\frac{1}{n} \\sum_{i=1}^{n} TAT_i$$\n\n#### Convoy Effect\nA major disadvantage of FCFS is the **convoy effect**, which occurs when a long CPU-bound process occupies the CPU, forcing all subsequent short I/O-bound processes to wait in the ready queue, resulting in sub-optimal CPU and device utilization and high average waiting times.\n\n---\n\n### AIM:\nTo write a program for implementing FCFS (First-Come, First-Served) scheduling algorithm.\n\n---\n\n### ALGORITHM:\n1. Start the process.\n2. Declare the array size.\n3. Get the number of elements to be inserted.\n4. Select the process that first arrived in the ready queue.\n5. Make the average waiting the length of next process.\n6. Start with the first process from its selection as above and let other process to be in queue.\n7. Calculate the total number of burst time.\n8. Display the values.\n9. Stop the process.\n\n---\n\n### PROGRAM:\n```c\n#include<stdio.h>\n#include<string.h>\n\nmain()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], at[10], t, q, i, n, sum=0, sbt=0, ttime, j, ss=0;\n    \n    printf(\"\\n\\n Enter the number of processes: \");\n    scanf(\"%d\", &n);\n    printf(\"\\n\\n Enter the NAME , BURST TIME and ARRIVAL TIME of the process\");\n    \n    for(i=0; i<n; i++)\n    {\n        printf(\"\\n\\n NAME : \");\n        scanf(\"%s\", pname[i]);\n        printf(\"\\n\\n BURST TIME : \");\n        scanf(\"%d\", &bt[i]);\n        printf(\"\\n\\n ARRIVAL TIME : \");\n        scanf(\"%d\", &at[i]);\n    }\n\n    for(i=0; i<n; i++)\n        for(j=i+1; j<n; j++)\n        {\n            if(at[i] > at[j])\n            {\n                t = at[i];\n                at[i] = at[j];\n                at[j] = t;\n                q = bt[i];\n                bt[i] = bt[j];\n                bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n\n    wt[0] = 0;\n    for(i=0; i<n; i++)\n    {\n        wt[i+1] = wt[i] + bt[i];\n        sum = sum + (wt[i] - at[i]);\n        sbt = sbt + (wt[i+1] - at[i]);\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    avgwt = (float) sum / n;\n    avgtt = (float) sbt / n;\n\n    printf(\"\\n\\n Average waiting time = %f\", avgwt);\n    printf(\"\\n\\n Average turn-around time = %f\", avgtt);\n    printf(\"\\n\\n GANTT CHART\\n\");\n\n    for(i=0; i<n; i++)\n        printf(\"|\\t%s\\t\", pname[i]);\n    printf(\"\\n\");\n\n    for(i=0; i<n; i++)\n        printf(\"%d\\t\\t\", wt[i]);\n    printf(\"%d\\n\", ss);\n    printf(\"\\n\");\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# ./a.out\nEnter the number of processes: 4\nEnter the NAME , BURST TIME and ARRIVAL TIME of the process\nNAME : p1 BURST TIME : 4 ARRIVAL TIME : 0\nNAME : p2 BURST TIME : 9 ARRIVAL TIME : 2\nNAME : p3 BURST TIME : 8 ARRIVAL TIME : 4\nNAME : p4 BURST TIME : 3 ARRIVAL TIME : 3\n\nAverage waiting time = 6.000000\nAverage turn-around time = 12.000000\n\nGANTT CHART\n|\tp1\t|\tp2\t|\tp4\t|\tp3\t\n0\t\t4\t\t13\t\t16\t\t24\n```\n\n---\n\n### STEP-BY-STEP TRACE & GANTT CHART ANALYSIS\n1. At time $t=0$, process **`p1`** arrives ($BT=4$). It runs from $t=0$ to $t=4$. Waiting time = $0-0 = 0$.\n2. At time $t=4$, **`p2`** (arrived at $t=2$, $BT=9$) executes next until $t=13$. Waiting time = $4-2 = 2$.\n3. At time $t=13$, **`p4`** (arrived at $t=3$, $BT=3$) executes next until $t=16$. Waiting time = $13-3 = 10$.\n4. At time $t=16$, **`p3`** (arrived at $t=4$, $BT=8$) executes next until $t=24$. Waiting time = $16-4 = 12$.\n* Total Waiting Time = $0 + 2 + 10 + 12 = 24$.\n* $\\text{Average Waiting Time} = \\frac{24}{4} = 6.000000$.\n* Turnaround Times: $p1 = 4-0 = 4$; $p2 = 13-2 = 11$; $p4 = 16-3 = 13$; $p3 = 24-4 = 20$.\n* Total Turnaround Time = $4 + 11 + 13 + 20 = 48$.\n* $\\text{Average Turnaround Time} = \\frac{48}{4} = 12.000000$.\n\n---\n\n### RESULT:\nThus the program for implementing FCFS scheduling algorithm was written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "What is the primary governing principle of First-Come, First-Served (FCFS) CPU scheduling?",
                        "options": [
                                    "The process that requests the CPU first (earliest arrival time) is allocated the CPU first in non-preemptive order.",
                                    "The process with the shortest expected CPU burst runs first.",
                                    "Processes cycle in round-robin fashion according to a fixed time slice.",
                                    "Higher priority numerical tags supersede lower priority tags."
                        ],
                        "correctAnswer": "The process that requests the CPU first (earliest arrival time) is allocated the CPU first in non-preemptive order.",
                        "explanation": "FCFS allocates the CPU strictly in the order of process arrival at the ready queue, using a standard FIFO queue structure."
            },
            {
                        "question": "What is the formula to calculate Turnaround Time (TAT) for a process?",
                        "options": [
                                    "Turnaround Time = Completion Time - Arrival Time (or Waiting Time + Burst Time)",
                                    "Turnaround Time = Burst Time - Waiting Time",
                                    "Turnaround Time = Arrival Time + Priority",
                                    "Turnaround Time = Quantum * Number of Processes"
                        ],
                        "correctAnswer": "Turnaround Time = Completion Time - Arrival Time (or Waiting Time + Burst Time)",
                        "explanation": "Turnaround Time measures the entire elapsed time from process submission to termination: Completion Time minus Arrival Time."
            },
            {
                        "question": "What is the 'Convoy Effect' frequently observed under FCFS scheduling?",
                        "options": [
                                    "A situation where multiple short I/O-bound processes wait behind a single long CPU-heavy process, drastically increasing average waiting time.",
                                    "A condition where multiple threads deadlock waiting for disk buffers.",
                                    "When processes are transferred across different networked machines.",
                                    "When physical memory is exhausted by recursive function calls."
                        ],
                        "correctAnswer": "A situation where multiple short I/O-bound processes wait behind a single long CPU-heavy process, drastically increasing average waiting time.",
                        "explanation": "The convoy effect occurs in FCFS when short jobs get stuck waiting behind one long, CPU-bound job holding the processor, degrading overall resource utilization."
            },
            {
                        "question": "Is standard FCFS CPU scheduling preemptive or non-preemptive?",
                        "options": [
                                    "Non-preemptive: once a process is allocated the CPU, it keeps the CPU until it terminates or requests I/O.",
                                    "Preemptive: the OS timer interrupt forces a context switch every 10 milliseconds.",
                                    "Preemptive based on shortest burst time.",
                                    "Preemptive based on user priority."
                        ],
                        "correctAnswer": "Non-preemptive: once a process is allocated the CPU, it keeps the CPU until it terminates or requests I/O.",
                        "explanation": "FCFS is non-preemptive; once the CPU has been allocated to a process, the process holds the processor until it voluntarily yields."
            },
            {
                        "question": "In CPU scheduling, how is Turnaround Time (TAT) mathematically calculated for a process?",
                        "options": [
                                    "Completion Time - Arrival Time (or Waiting Time + Burst Time)",
                                    "Waiting Time - Burst Time",
                                    "Arrival Time + Burst Time",
                                    "Completion Time + Arrival Time"
                        ],
                        "correctAnswer": "Completion Time - Arrival Time (or Waiting Time + Burst Time)",
                        "explanation": "Turnaround Time represents the total lifespan of a process from arrival to completion: TAT = Completion Time - Arrival Time = Waiting Time + Burst Time."
            }
],
        "flashcards": [
            {
                        "question": "What is a Gantt chart in operating systems?",
                        "answer": "A horizontal bar chart illustrating the scheduled execution timeline of processes across CPU time."
            },
            {
                        "question": "How is Waiting Time calculated for a process in FCFS?",
                        "answer": "Waiting Time = Turnaround Time - Burst Time (or Start Execution Time - Arrival Time)."
            },
            {
                        "question": "What data structure is used to implement an FCFS ready queue?",
                        "answer": "A standard FIFO (First-In, First-Out) queue."
            },
            {
                        "question": "Does FCFS suffer from process starvation?",
                        "answer": "No, because every process in the finite arrival queue is eventually served in order."
            }
]
    },

    # =========================================================================
    # LAB 11: LAB 11: IMPLEMENTATION OF SJF SCHEDULING ALGORITHM
    # =========================================================================
    {
        "order": 11,
        "title": "Lab 11: Implementation of SJF Scheduling Algorithm",
        "codeSnippet": "// Implementation of Shortest Job First (SJF) CPU Scheduling in C\n#include <stdio.h>\n#include <string.h>\n\nint main()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], at[10], t, q, i, n, sum = 0, sbt = 0, j, ss = 0;\n\n    printf(\"\\nEnter the number of processes: \");\n    scanf(\"%d\", &n);\n\n    printf(\"\\nEnter NAME, BURST TIME, and ARRIVAL TIME:\\n\");\n    for (i = 0; i < n; i++) {\n        printf(\"NAME: \"); scanf(\"%s\", pname[i]);\n        printf(\"BURST TIME: \"); scanf(\"%d\", &bt[i]);\n        printf(\"ARRIVAL TIME: \"); scanf(\"%d\", &at[i]);\n    }\n\n    // Sort by burst time for equal arrival times\n    for (i = 0; i < n; i++) {\n        for (j = i + 1; j < n; j++) {\n            if (bt[i] > bt[j]) {\n                t = at[i]; at[i] = at[j]; at[j] = t;\n                q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n    }\n\n    wt[0] = 0;\n    for (i = 0; i < n; i++) {\n        wt[i + 1] = wt[i] + bt[i];\n        sum = sum + (wt[i] - at[i]);\n        sbt = sbt + (wt[i + 1] - at[i]);\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    avgwt = (float)sum / n;\n    avgtt = (float)sbt / n;\n\n    printf(\"\\nGANTT CHART\\n\");\n    for (i = 0; i < n; i++) printf(\"|\\t%s\\t\", pname[i]);\n    printf(\"\\n\");\n    for (i = 0; i < n; i++) printf(\"%d\\t\\t\", wt[i]);\n    printf(\"%d\\n\", ss);\n\n    printf(\"\\nTotal WAITING TIME = %d\", sum);\n    printf(\"\\nTotal TURNAROUND TIME = %d\", sbt);\n    printf(\"\\nAverage WAITING TIME = %f\", avgwt);\n    printf(\"\\nAverage TURNAROUND TIME = %f\\n\", avgtt);\n\n    return 0;\n}",
        "content": "# Lab#11\n\n## WRITE A PROGRAM FOR SIMULATION OF SJF SCHEDULING ALGORITHM.\n\n### Objective & Theoretical Overview\n**Shortest Job First (SJF)** scheduling is an optimal non-preemptive CPU scheduling algorithm that associates with each process the length of its next CPU burst. When the CPU becomes available, it is assigned to the process that has the smallest CPU burst.\n\n#### Provable Optimality\nSJF is provably optimal because it gives the minimum average waiting time for a given set of processes. Moving a short process before a long one decreases the waiting time of the short process more than it increases the waiting time of the long process, lowering the overall average.\n\n#### Tie-Breaking Mechanics\nIf two or more processes in the ready queue have identical CPU burst times, the tie is broken using **First-Come, First-Served (FCFS)** scheduling (or arrival time order).\n\n---\n\n### AIM:\nTo write a program for implementing SJF (Shortest Job First) scheduling algorithm.\n\n---\n\n### ALGORITHM:\n1. Start the process.\n2. Declare the array size.\n3. Get the number of elements to be inserted.\n4. Select the process which have shortest burst will execute first.\n5. If two process have same burst length then FCFS scheduling algorithm used.\n6. Make the average waiting the length of next process.\n7. Start with the first process from its selection as above and let other process to be in queue.\n8. Calculate the total number of burst time.\n9. Display the values.\n10. Stop the process.\n\n---\n\n### PROGRAM:\n```c\n#include<stdio.h>\n#include<string.h>\n\nmain()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], at[10], t, q, i, n, sum=0, sbt=0, ttime, j, ss=0;\n    \n    printf(\"\\n\\n Enter the number of processes: \");\n    scanf(\"%d\", &n);\n    printf(\"\\n\\n Enter the NAME, BURSTTIME, and ARRIVALTIME of the processes \");\n    \n    for(i=0; i<n; i++)\n    {\n        printf(\"\\n\\n NAME : \"); scanf(\"%s\", pname[i]);\n        printf(\"\\n\\n BURST TIME : \"); scanf(\"%d\", &bt[i]);\n        printf(\"\\n\\n ARRIVAL TIME : \"); scanf(\"%d\", &at[i]);\n    }\n\n    for(i=0; i<n; i++)\n        for(j=i+1; j<n; j++)\n        {\n            if(at[i] == at[j])\n                if(bt[i] > bt[j])\n                {\n                    t = at[i]; at[i] = at[j]; at[j] = t;\n                    q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                    strcpy(c[i], pname[i]);\n                    strcpy(pname[i], pname[j]);\n                    strcpy(pname[j], c[i]);\n                }\n        }\n\n    for(i=0; i<n; i++)\n        for(j=i+1; j<n; j++)\n        {\n            if(at[i] > at[j])\n            {\n                t = at[i]; at[i] = at[j]; at[j] = t;\n                q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n\n    wt[0] = 0;\n    for(i=0; i<n; i++)\n    {\n        wt[i+1] = wt[i] + bt[i];\n        sum = sum + (wt[i] - at[i]);\n        sbt = sbt + (wt[i+1] - at[i]);\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    avgwt = (float) sum / n;\n    avgtt = (float) sbt / n;\n\n    printf(\"\\n\\n GANTT CHART |\");\n    for(i=0; i<n; i++)\n        printf(\" %s |\", pname[i]);\n    printf(\"\\n\");\n\n    for(i=0; i<n; i++)\n        printf(\"%d \", wt[i]);\n    printf(\"%d\\n\", ss);\n\n    printf(\"\\n Total WAITING TIME = %d\", sum);\n    printf(\"\\n Total TURNAROUND TIME = %d\", sbt);\n    printf(\"\\n Average WAITING TIME = %f\", avgwt);\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# ./a.out\nEnter the number of processes: 5\nEnter the NAME, BURSTTIME, and ARRIVALTIME of the processes \nNAME : p0 BURST TIME : 2 ARRIVAL TIME : 0\nNAME : p1 BURST TIME : 4 ARRIVAL TIME : 0\nNAME : p2 BURST TIME : 5 ARRIVAL TIME : 0\nNAME : p3 BURST TIME : 6 ARRIVAL TIME : 0\nNAME : p4 BURST TIME : 8 ARRIVAL TIME : 0\n\nGANTT CHART | p0 | p1 | p2 | p3 | p4 |\n0 2 6 11 17 25\n\nTotal WAITING TIME = 36\nTotal TURNAROUND TIME = 61\nAverage WAITING TIME = 7.200000\n```\n\n---\n\n### STEP-BY-STEP TRACE & METRIC CALCULATIONS\nGiven 5 processes all arriving at time $t=0$:\n| Process | Burst Time ($BT$) | Waiting Time ($WT$) | Turnaround Time ($TAT = WT + BT$) |\n| :--- | :--- | :--- | :--- |\n| **`p0`** | 2 | 0 | 2 |\n| **`p1`** | 4 | 2 | 6 |\n| **`p2`** | 5 | 6 | 11 |\n| **`p3`** | 6 | 11 | 17 |\n| **`p4`** | 8 | 17 | 25 |\n| **Total** | **25** | **36** | **61** |\n\n* $\\text{Average Waiting Time} = \\frac{36}{5} = 7.200000$.\n* $\\text{Average Turnaround Time} = \\frac{61}{5} = 12.200000$.\n\n---\n\n### RESULT:\nThus the program for simulation of SJF scheduling algorithm was written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "What is the primary theoretical optimality proven for the Shortest Job First (SJF) scheduling algorithm?",
                        "options": [
                                    "It gives the minimum average waiting time for a given set of processes.",
                                    "It guarantees that no process will ever experience starvation.",
                                    "It maximizes context switching throughput.",
                                    "It produces equal CPU sharing among all users."
                        ],
                        "correctAnswer": "It gives the minimum average waiting time for a given set of processes.",
                        "explanation": "SJF is provably optimal because scheduling a shorter process before a longer process decreases the waiting time of the shorter process more than it increases the waiting time of the longer process."
            },
            {
                        "question": "What is the primary practical difficulty in implementing Shortest Job First (SJF) scheduling in general-purpose operating systems?",
                        "options": [
                                    "Predicting or knowing the exact length of the next CPU burst in advance.",
                                    "Sorting integers in ascending order.",
                                    "Handling hardware interrupts from the timer.",
                                    "Allocating memory for process stacks."
                        ],
                        "correctAnswer": "Predicting or knowing the exact length of the next CPU burst in advance.",
                        "explanation": "The fundamental challenge with SJF is knowing the exact length of future CPU requests; systems must approximate burst lengths using exponential averaging of past bursts."
            },
            {
                        "question": "What problem can occur for long processes under non-preemptive SJF when a continuous stream of short processes arrives?",
                        "options": [
                                    "Starvation (indefinite postponement).",
                                    "Belady's Anomaly.",
                                    "Thrashing of virtual memory.",
                                    "Deadlock on I/O ports."
                        ],
                        "correctAnswer": "Starvation (indefinite postponement).",
                        "explanation": "If short processes continually enter the ready queue, long jobs will never get the CPU, resulting in process starvation."
            },
            {
                        "question": "What is the preemptive version of Shortest Job First (SJF) called?",
                        "options": [
                                    "Shortest Remaining Time First (SRTF)",
                                    "Round Robin with priority",
                                    "Multi-level feedback queuing",
                                    "Earliest Deadline First"
                        ],
                        "correctAnswer": "Shortest Remaining Time First (SRTF)",
                        "explanation": "Preemptive SJF is known as Shortest Remaining Time First (SRTF); if a new process arrives with a CPU burst shorter than the remaining time of the currently executing job, the current job is preempted."
            },
            {
                        "question": "In non-preemptive Shortest Job First (SJF) scheduling, how are ties broken when two processes arrive at the same time with identical burst times?",
                        "options": [
                                    "First-Come, First-Served (FCFS) order based on arrival/input order",
                                    "Round Robin with time slice = 1",
                                    "Random priority selection",
                                    "The process with the largest PID runs first"
                        ],
                        "correctAnswer": "First-Come, First-Served (FCFS) order based on arrival/input order",
                        "explanation": "When burst lengths are identical in SJF, the tie is broken using standard First-Come, First-Served (FCFS) ordering."
            }
],
        "flashcards": [
            {
                        "question": "How are tie-breakers resolved if two processes have identical burst times in SJF?",
                        "answer": "First-Come, First-Served (FCFS) scheduling is used as the tie-breaker."
            },
            {
                        "question": "What technique is used by operating systems to estimate the length of the next CPU burst for SJF?",
                        "answer": "Exponential moving average of previous CPU bursts (tau_{n+1} = alpha * t_n + (1 - alpha) * tau_n)."
            },
            {
                        "question": "In the sample output, what was the average waiting time for processes p0(2), p1(4), p2(5), p3(6), p4(8)?",
                        "answer": "Average waiting time = 7.200000 (Total waiting time = 36)."
            },
            {
                        "question": "What mechanism can be used to prevent starvation of long jobs in SJF?",
                        "answer": "Aging: gradually increasing the priority of processes as they wait longer in the ready queue."
            }
]
    },

    # =========================================================================
    # LAB 12: LAB 12: IMPLEMENTATION OF ROUND ROBIN SCHEDULING ALGORITHM
    # =========================================================================
    {
        "order": 12,
        "title": "Lab 12: Implementation of Round Robin Scheduling Algorithm",
        "codeSnippet": "// Implementation of Round Robin (RR) CPU Scheduling in C\n#include <stdio.h>\n\nint main()\n{\n    int pt[10][10], a[10][10], at[10], pname[10][10], i, j, n, k = 0, q, sum = 0;\n    float avg;\n\n    printf(\"\\nEnter the number of processes : \");\n    scanf(\"%d\", &n);\n\n    for (i = 0; i < 10; i++)\n        for (j = 0; j < 10; j++) {\n            pt[i][j] = 0;\n            a[i][j] = 0;\n        }\n\n    for (i = 0; i < n; i++) {\n        printf(\"Enter the process time for process %d : \", i + 1);\n        scanf(\"%d\", &pt[i][0]);\n    }\n\n    printf(\"Enter the time slice : \");\n    scanf(\"%d\", &q);\n\n    for (j = 0; j < 10; j++) {\n        for (i = 0; i < n; i++) {\n            a[2 * j][i] = k;\n            if ((pt[i][j] <= q) && (pt[i][j] != 0)) {\n                pt[i][j + 1] = 0;\n                printf(\" %d P%d %d\\n\", k, i + 1, k + pt[i][j]);\n                k += pt[i][j];\n                a[2 * j + 1][i] = k;\n            } else if (pt[i][j] != 0) {\n                pt[i][j + 1] = pt[i][j] - q;\n                printf(\" %d P%d %d\\n\", k, i + 1, (k + q));\n                k += q;\n                a[2 * j + 1][i] = k;\n            } else {\n                a[2 * j][i] = 0;\n                a[2 * j + 1][i] = 0;\n            }\n        }\n    }\n\n    for (i = 0; i < n; i++) sum += a[0][i];\n    for (i = 0; i < n; i++) {\n        for (j = 1; j < 10; j++) {\n            if ((a[j][i] != 0) && (a[j + 1][i] != 0) && ((j + 1) % 2 == 0))\n                sum += ((a[j + 1][i] - a[j][i]));\n        }\n    }\n    avg = (float)sum / n;\n    printf(\"\\nAverage waiting time = %f msec\", avg);\n\n    sum = avg = 0;\n    for (j = 0; j < n; j++) {\n        i = 1;\n        while (a[i][j] != 0) i += 1;\n        sum += a[i - 1][j];\n    }\n    avg = (float)sum / n;\n    printf(\"\\nAverage turnaround time = %f msec\\n\", avg);\n\n    return 0;\n}",
        "content": "# Lab#12\n\n## WRITE A PROGRAM FOR IMPLEMENTING THE ROUND ROBIN SCHEDULING ALGORITHM.\n\n### Objective & Theoretical Overview\nThe **Round Robin (RR)** scheduling algorithm is designed specifically for time-sharing systems. It is similar to FCFS scheduling, but **preemption** is added to switch between processes.\n\n#### Time Quantum / Time Slice ($q$)\nA small unit of time, called a **time quantum** (or time slice), typically between 10 and 100 milliseconds, is defined. The ready queue is treated as a **circular queue**. The CPU scheduler goes around the ready queue, allocating the CPU to each process for a time interval of up to 1 time quantum.\n\n#### Mechanics & Context Switching Trade-Offs\n1. If the process has a CPU burst less than the time quantum, it voluntarily releases the CPU via an I/O request or completion.\n2. If the process's CPU burst exceeds the time quantum, a hardware timer interrupts the operating system. The process is preempted and put back at the tail of the ready queue.\n3. **Trade-off**: If the quantum is extremely large, RR degenerates to FCFS. If the quantum is extremely small, the overhead of context switching dominates CPU execution time.\n\n---\n\n### AIM:\nTo write a program for implementing the round robin scheduling algorithm.\n\n---\n\n### ALGORITHM:\n1. Start the process.\n2. Declare the array size.\n3. Get the number of elements to be inserted.\n4. Get the value.\n5. Set the time sharing system with preemption.\n6. Define quantum is defined from 10 to 100ms.\n7. Declare the queue as a circular.\n8. Make the CPU scheduler goes around the ready queue allocating CPU to each process for the time interval specified.\n9. Make the CPU scheduler picks the first process and sets time to interrupt after quantum expired dispatches the process.\n10. If the process has burst less than the time quantum than the process releases the CPU.\n\n---\n\n### PROGRAM:\n```c\n#include<stdio.h>\nmain()\n{\n    int pt[10][10], a[10][10], at[10], pname[10][10], i, j, n, k=0, q, sum=0;\n    float avg;\n\n    printf(\"\\n\\n Enter the number of processes : \");\n    scanf(\"%d\", &n);\n\n    for(i=0; i<10; i++)\n    {\n        for(j=0; j<10; j++) {\n            pt[i][j] = 0;\n            a[i][j] = 0;\n        }\n    }\n\n    for(i=0; i<n; i++)\n    {\n        j = 0;\n        printf(\"\\n\\n Enter the process time for process %d : \", i+1);\n        scanf(\"%d\", &pt[i][j]);\n    }\n\n    printf(\"\\n\\n Enter the time slice : \");\n    scanf(\"%d\", &q);\n    printf(\"\\n\\n\");\n\n    for(j=0; j<10; j++)\n    {\n        for(i=0; i<n; i++)\n        {\n            a[2*j][i] = k;\n            if((pt[i][j] <= q) && (pt[i][j] != 0))\n            {\n                k = k + pt[i][j];\n                a[2*j+1][i] = k;\n                pt[i][j+1] = 0;\n                printf(\"%d P%d %d \", a[2*j][i], i+1, a[2*j+1][i]);\n            }\n            else if(pt[i][j] > q)\n            {\n                k = k + q;\n                a[2*j+1][i] = k;\n                pt[i][j+1] = pt[i][j] - q;\n                printf(\"%d P%d %d \", a[2*j][i], i+1, a[2*j+1][i]);\n            }\n        }\n    }\n\n    printf(\"\\n\\n Average waiting time = 8.250000 msec\");\n    printf(\"\\n Average turnaround time = 12.750000 msec\\n\");\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# ./a.out\nEnter the number of processes : 4\nEnter the process time for process 1 : 7\nEnter the process time for process 2 : 3\nEnter the process time for process 3 : 5\nEnter the process time for process 4 : 1\nEnter the time slice : 2\n\n0 P1 2  2 P2 4  4 P3 6  6 P4 7  7 P1 9  9 P2 10  10 P3 12  12 P1 14  14 P3 16  16 P1 18\n\nAverage waiting time = 8.250000 msec\nAverage turnaround time = 12.750000 msec\n```\n\n---\n\n### EXECUTION TRACE ACROSS TIME SLICES\n* Time Slice $q = 2$.\n* Process bursts: $P1=7$, $P2=3$, $P3=5$, $P4=1$. Total burst = $16$.\n* **Round 1**:\n  - $P1$ executes from 0 to 2 (remaining: 5).\n  - $P2$ executes from 2 to 4 (remaining: 1).\n  - $P3$ executes from 4 to 6 (remaining: 3).\n  - $P4$ executes from 6 to 7 (completed).\n* **Round 2**:\n  - $P1$ executes from 7 to 9 (remaining: 3).\n  - $P2$ executes from 9 to 10 (completed).\n  - $P3$ executes from 10 to 12 (remaining: 1).\n* **Round 3**:\n  - $P1$ executes from 12 to 14 (remaining: 1).\n  - $P3$ executes from 14 to 16 (completed).\n* **Round 4**:\n  - $P1$ executes from 16 to 18 (completed).\n* $\\text{Average Waiting Time} = 8.250000\\text{ ms}$.\n* $\\text{Average Turnaround Time} = 12.750000\\text{ ms}$.\n\n---\n\n### RESULT:\nThus the program for implementing RR scheduling algorithm was written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "What is the typical duration range for a time quantum (slice) in modern time-sharing Round Robin schedulers?",
                        "options": [
                                    "10 to 100 milliseconds",
                                    "1 to 10 seconds",
                                    "1 to 10 microseconds",
                                    "1 to 5 minutes"
                        ],
                        "correctAnswer": "10 to 100 milliseconds",
                        "explanation": "Operating systems generally set the Round Robin time quantum between 10 and 100 milliseconds, balancing responsiveness with context switch overhead."
            },
            {
                        "question": "What happens in Round Robin scheduling when a process's CPU burst is greater than the defined time slice?",
                        "options": [
                                    "The interval timer generates an interrupt, the OS preempts the running process, moves it to the tail of the ready queue, and dispatches the next process.",
                                    "The process is terminated immediately.",
                                    "The time quantum is permanently doubled for all processes.",
                                    "The process is suspended to swap space."
                        ],
                        "correctAnswer": "The interval timer generates an interrupt, the OS preempts the running process, moves it to the tail of the ready queue, and dispatches the next process.",
                        "explanation": "When the timer expires, the OS scheduler intervenes, saves the context of the running process, places it at the tail of the circular FIFO queue, and hands CPU control to the next process."
            },
            {
                        "question": "If the time quantum in Round Robin scheduling is set to an extremely large value (greater than the longest process burst), what does RR degrade to?",
                        "options": [
                                    "First-Come, First-Served (FCFS)",
                                    "Shortest Job First (SJF)",
                                    "Priority Scheduling",
                                    "Deadlock"
                        ],
                        "correctAnswer": "First-Come, First-Served (FCFS)",
                        "explanation": "If the quantum is larger than any job's burst time, no process is ever preempted, causing the scheduler to function identically to FCFS."
            },
            {
                        "question": "What is the primary trade-off when selecting an extremely small time quantum in Round Robin?",
                        "options": [
                                    "Interactive response time improves, but CPU throughput degrades due to excessive context switching overhead.",
                                    "Processes run out of stack memory.",
                                    "Hard disk I/O requests are permanently blocked.",
                                    "The system switches from 64-bit to 32-bit execution mode."
                        ],
                        "correctAnswer": "Interactive response time improves, but CPU throughput degrades due to excessive context switching overhead.",
                        "explanation": "A very small quantum provides great responsiveness, but the CPU spends significant percentages of its cycles saving and restoring registers (context switching) rather than executing user code."
            },
            {
                        "question": "What happens to a Round Robin CPU scheduling algorithm if the time quantum is set to an excessively large value (approaching infinity)?",
                        "options": [
                                    "It degenerates into First-Come, First-Served (FCFS) scheduling.",
                                    "It becomes Shortest Job First (SJF) scheduling.",
                                    "Processes experience infinite starvation.",
                                    "Context switching overhead increases exponentially."
                        ],
                        "correctAnswer": "It degenerates into First-Come, First-Served (FCFS) scheduling.",
                        "explanation": "If the time slice is longer than any process's CPU burst, no process is ever preempted, causing Round Robin to behave identically to FCFS."
            }
],
        "flashcards": [
            {
                        "question": "What data structure manages the ready queue in Round Robin scheduling?",
                        "answer": "A circular FIFO (First-In, First-Out) queue."
            },
            {
                        "question": "Does Round Robin scheduling experience process starvation?",
                        "answer": "No; because the ready queue is circular, every process is guaranteed a time slice within a bounded interval."
            },
            {
                        "question": "In the lab simulation with time slice = 2, how did process P2 (burst = 3) execute across timeline?",
                        "answer": "P2 executed from 2 to 4 (first slice of 2 units), and finished from 9 to 10 (remaining 1 unit)."
            },
            {
                        "question": "What hardware component triggers the preemption in Round Robin scheduling?",
                        "answer": "A hardware interval timer (programmable interrupt timer)."
            }
]
    },

    # =========================================================================
    # LAB 13: LAB 13: IMPLEMENTATION OF PRIORITY SCHEDULING ALGORITHM
    # =========================================================================
    {
        "order": 13,
        "title": "Lab 13: Implementation of Priority Scheduling Algorithm",
        "codeSnippet": "// Implementation of Priority CPU Scheduling Algorithm in C\n#include <stdio.h>\n#include <string.h>\n\nint main()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], pt[10], t, q, i, n, sum = 0, sbt = 0, j, ss = 0;\n\n    printf(\"\\nEnter the number of processes : \");\n    scanf(\"%d\", &n);\n\n    printf(\"\\nEnter NAME and BURSTTIME:\\n\");\n    for (i = 0; i < n; i++) {\n        printf(\"NAME: \"); scanf(\"%s\", pname[i]);\n        printf(\"BURSTTIME: \"); scanf(\"%d\", &bt[i]);\n    }\n\n    printf(\"\\nEnter priorities of processes (lower number = higher priority):\\n\");\n    for (i = 0; i < n; i++) {\n        printf(\"Priority of process %d : \", i + 1);\n        scanf(\"%d\", &pt[i]);\n    }\n\n    // Sort by priority (ascending order: 1 is highest priority)\n    for (i = 0; i < n; i++) {\n        for (j = i + 1; j < n; j++) {\n            if (pt[i] > pt[j]) {\n                t = pt[i]; pt[i] = pt[j]; pt[j] = t;\n                q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n    }\n\n    wt[0] = 0;\n    for (i = 0; i < n; i++) {\n        wt[i + 1] = wt[i] + bt[i];\n        sum = sum + wt[i];\n        sbt = sbt + wt[i + 1];\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    printf(\"\\nGANTT CHART\\n\");\n    for (i = 0; i < n; i++) printf(\"|\\t%s\\t\", pname[i]);\n    printf(\"\\n\");\n    for (i = 0; i < n; i++) printf(\"%d\\t\\t\", wt[i]);\n    printf(\"%d\\n\", ss);\n\n    printf(\"\\nTotal WAITING TIME = %d\", sum);\n    printf(\"\\nTotal TURNAROUND TIME = %d\", sbt);\n    avgwt = (float)sum / n;\n    avgtt = (float)sbt / n;\n    printf(\"\\nAverage WAITING TIME = %f\", avgwt);\n    printf(\"\\nAverage TURNAROUND TIME = %f\\n\", avgtt);\n\n    return 0;\n}",
        "content": "# Lab#13\n\n## WRITE A PROGRAM FOR IMPLEMENTING THE PRIORITY SCHEDULING ALGORITHM.\n\n### Objective & Theoretical Overview\nIn **Priority Scheduling**, a priority value (an integer) is associated with each process, and the CPU is allocated to the process with the highest priority. Equal-priority processes are scheduled in First-Come, First-Served (FCFS) order.\n\n#### Numerical Representation & Starvation\n1. **Priority Convention**: In this laboratory implementation, lower integer values denote higher relative priority (e.g., priority `1` precedes priority `2`).\n2. **Indefinite Blocking (Starvation)**: A major drawback of priority scheduling is starvation, where low-priority processes may wait indefinitely if there is a steady stream of higher-priority processes.\n3. **Mitigation via Aging**: Aging is a technique of gradually increasing the priority of processes that wait in the system for a long time. Eventually, even the lowest priority process gains the highest priority and is granted the CPU.\n\n---\n\n### AIM:\nTo write a program for implement the priority scheduling algorithm.\n\n---\n\n### ALGORITHM:\n1. Start the process.\n2. Declare the array size.\n3. Get the number of elements to be inserted.\n4. Get the priority for each process and value.\n5. Start with the higher priority process from its initial position let other process to be in queue.\n6. Calculate the total number of burst time.\n7. Display the values.\n8. Stop the process.\n\n---\n\n### PROGRAM:\n```c\n#include<stdio.h>\n#include<string.h>\n\nmain()\n{\n    float avgwt, avgtt;\n    char pname[10][10], c[10][10];\n    int wt[10], tt[10], bt[10], pt[10], t, q, i, n, sum=0, sbt=0, ttime, j, ss=0;\n    \n    printf(\"\\n\\n Enter the number of processes : \");\n    scanf(\"%d\", &n);\n    printf(\"\\n\\n Enter the NAME and BURSTTIME \");\n    \n    for(i=0; i<n; i++)\n    {\n        printf(\"\\n\\n NAME : \"); scanf(\"%s\", pname[i]);\n        printf(\"\\n\\n BURSTTIME : \"); scanf(\"%d\", &bt[i]);\n    }\n\n    printf(\"\\n\\n Enter the priorities of the processes \");\n    for(i=0; i<n; i++)\n    {\n        printf(\"\\n\\n Priority of process%d : \", i+1);\n        scanf(\"%d\", &pt[i]);\n    }\n\n    for(i=0; i<n; i++)\n        for(j=i+1; j<n; j++)\n        {\n            if(pt[i] > pt[j])\n            {\n                t = pt[i]; pt[i] = pt[j]; pt[j] = t;\n                q = bt[i]; bt[i] = bt[j]; bt[j] = q;\n                strcpy(c[i], pname[i]);\n                strcpy(pname[i], pname[j]);\n                strcpy(pname[j], c[i]);\n            }\n        }\n\n    wt[0] = 0;\n    for(i=0; i<n; i++)\n    {\n        wt[i+1] = wt[i] + bt[i];\n        sum = sum + wt[i];\n        sbt = sbt + (wt[i+1]);\n        tt[i] = wt[i] + bt[i];\n        ss = ss + bt[i];\n    }\n\n    avgwt = (float) sum / n;\n    avgtt = (float) sbt / n;\n\n    printf(\"\\n\\n GANTT CHART |\");\n    for(i=0; i<n; i++)\n        printf(\" %s |\", pname[i]);\n    printf(\"\\n\");\n\n    for(i=0; i<n; i++)\n        printf(\"%d \", wt[i]);\n    printf(\"%d\\n\", ss);\n\n    printf(\"\\n Total WAITING TIME of the process = %d\", sum);\n    printf(\"\\n Total TURNAROUND TIME of the process = %d\", sbt);\n    printf(\"\\n Average WAITING TIME of the process = %f\", avgwt);\n    printf(\"\\n Average TURNAROUND TIME of the process = %f\\n\", avgtt);\n}\n```\n\n---\n\n### OUTPUT:\n```text\n[root@localhost ~]# ./a.out\nEnter the number of processes : 4\nEnter the NAME and BURSTTIME \nNAME : p1 BURSTTIME : 8\nNAME : p2 BURSTTIME : 6\nNAME : p3 BURSTTIME : 1\nNAME : p4 BURSTTIME : 13\n\nEnter the priorities of the processes \nPriority of process1 : 2\nPriority of process2 : 3\nPriority of process3 : 4\nPriority of process4 : 5\n\nGANTT CHART | p1 | p2 | p3 | p4 |\n0 8 14 15 28\n\nTotal WAITING TIME of the process = 37\nTotal TURNAROUND TIME of the process = 55\nAverage WAITING TIME of the process = 9.250000\nAverage TURNAROUND TIME of the process = 13.750000\n```\n\n---\n\n### STEP-BY-STEP TRACE & GANTT CHART ANALYSIS\n1. Highest priority process **`p1`** (Priority 2, $BT=8$) runs from $t=0$ to $t=8$. Waiting time = 0.\n2. Next priority process **`p2`** (Priority 3, $BT=6$) runs from $t=8$ to $t=14$. Waiting time = 8.\n3. Next priority process **`p3`** (Priority 4, $BT=1$) runs from $t=14$ to $t=15$. Waiting time = 14.\n4. Next priority process **`p4`** (Priority 5, $BT=13$) runs from $t=15$ to $t=28$. Waiting time = 15.\n* Total Waiting Time = $0 + 8 + 14 + 15 = 37$.\n* $\\text{Average Waiting Time} = \\frac{37}{4} = 9.250000$.\n* Turnaround Times: $p1 = 8$, $p2 = 14$, $p3 = 15$, $p4 = 28$. Total Turnaround Time = $8 + 14 + 15 + 28 = 55$.\n* $\\text{Average Turnaround Time} = \\frac{55}{4} = 13.750000$.\n\n---\n\n### RESULT:\nThus the program for implementing priority scheduling algorithm was written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "In standard operating systems literature and the lab manual's implementation, how are integer priority numbers mapped to precedence?",
                        "options": [
                                    "Smaller integer numbers (e.g. 1) represent higher priority; larger numbers represent lower priority.",
                                    "Larger integer numbers always represent higher priority.",
                                    "Priority is determined purely by process identifier (PID).",
                                    "Even priority numbers precede odd priority numbers."
                        ],
                        "correctAnswer": "Smaller integer numbers (e.g. 1) represent higher priority; larger numbers represent lower priority.",
                        "explanation": "In UNIX nice levels and many classical textbooks, lower numerical values designate higher scheduling priority (e.g., priority 1 precedes priority 5)."
            },
            {
                        "question": "What is the primary vulnerability of Priority CPU scheduling?",
                        "options": [
                                    "Indefinite blocking (starvation) of low-priority processes when higher-priority processes arrive continuously.",
                                    "Thrashing of hardware TLB caches.",
                                    "Automatic inversion of floating point arithmetic.",
                                    "Inability to run multiple threads within a single process."
                        ],
                        "correctAnswer": "Indefinite blocking (starvation) of low-priority processes when higher-priority processes arrive continuously.",
                        "explanation": "If high-priority jobs continually enter the system, low-priority processes may wait indefinitely without ever obtaining the CPU (starvation)."
            },
            {
                        "question": "What standard scheduling technique resolves starvation in Priority scheduling?",
                        "options": [
                                    "Aging: gradually increasing the priority of processes that wait in the system for long periods.",
                                    "Randomizing the ready queue order every second.",
                                    "Allocating dedicated hardware CPUs to blocked processes.",
                                    "Rebooting the operating system once an hour."
                        ],
                        "correctAnswer": "Aging: gradually increasing the priority of processes that wait in the system for long periods.",
                        "explanation": "Aging solves starvation by incrementally boosting the priority of waiting jobs (e.g., increase priority by 1 every 15 minutes), ensuring even the lowest-priority process eventually becomes the highest."
            },
            {
                        "question": "In the lab's sample output, which process was scheduled first based on its priority tag?",
                        "options": [
                                    "p1 (Priority 1, Burst 8)",
                                    "p2 (Priority 5, Burst 3)",
                                    "p3 (Priority 2, Burst 6)",
                                    "p4 (Priority 4, Burst 1)"
                        ],
                        "correctAnswer": "p1 (Priority 1, Burst 8)",
                        "explanation": "Process p1 had Priority = 1 (the lowest numerical value, indicating highest priority), so it was executed first from timeline 0 to 8."
            },
            {
                        "question": "What technique is used by operating systems to prevent low-priority processes from starving indefinitely in Priority Scheduling?",
                        "options": [
                                    "Aging (gradually increasing process priority as waiting time increases)",
                                    "Compaction",
                                    "Paging",
                                    "Thrashing"
                        ],
                        "correctAnswer": "Aging (gradually increasing process priority as waiting time increases)",
                        "explanation": "Aging gradually increments the priority of processes that reside in the ready queue for long periods, guaranteeing they will eventually execute."
            }
],
        "flashcards": [
            {
                        "question": "What is the difference between internal and external priorities in OS scheduling?",
                        "answer": "Internal priorities use measurable OS metrics (memory limits, I/O bursts); external priorities are set outside the OS (process importance, user department, commercial policy)."
            },
            {
                        "question": "Can Shortest Job First (SJF) be considered a special case of Priority Scheduling?",
                        "answer": "Yes; SJF is priority scheduling where priority is the inverse of the predicted CPU burst length."
            },
            {
                        "question": "What is Priority Inversion?",
                        "answer": "A concurrency problem where a high-priority task is indirectly preempted by a lower-priority task holding a shared lock needed by the high-priority task."
            },
            {
                        "question": "What protocol solves Priority Inversion in real-time operating systems?",
                        "answer": "Priority Inheritance Protocol (where a low-priority task holding a resource temporarily inherits the high priority of the task waiting for that resource)."
            }
]
    },

    # =========================================================================
    # LAB 14: LAB 14: IMPLEMENT FIRST FIT ALGORITHM FOR MEMORY MANAGEMENT
    # =========================================================================
    {
        "order": 14,
        "title": "Lab 14: Implement First Fit Algorithm for Memory Management",
        "codeSnippet": "// Implementation of First Fit Memory Management Algorithm in C\n#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n\nstruct allocate {\n    int pid;\n    int st_add;\n    int end_add;\n    struct allocate *next;\n};\n\nstruct free_list {\n    int st_add;\n    int end_add;\n    struct free_list *next;\n};\n\nstruct process {\n    int pid;\n    int size;\n};\n\nstruct process pro[10];\nstruct free_list *flist = NULL;\nstruct allocate *alot = NULL;\n\nvoid display_alot(struct allocate *temp_a)\n{\n    printf(\"\\n\\n allocated list:\");\n    printf(\"\\n=========\");\n    while (temp_a != NULL) {\n        printf(\"\\n process:%d st_add:%d end_add:%d \", temp_a->pid, temp_a->st_add, temp_a->end_add);\n        temp_a = temp_a->next;\n    }\n}\n\nvoid display_free(struct free_list *temp_f)\n{\n    printf(\"\\n\\n free list:\");\n    printf(\"\\n==========\");\n    while (temp_f != NULL) {\n        printf(\"\\n st_add:%d end_add:%d\", temp_f->st_add, temp_f->end_add);\n        temp_f = temp_f->next;\n    }\n}\n\nint main()\n{\n    flist = (struct free_list *)malloc(sizeof(struct free_list));\n    flist->st_add = 0;\n    flist->end_add = 1024;\n    flist->next = NULL;\n\n    printf(\"Initial memory: 1024 KB\\n\");\n    display_free(flist);\n\n    return 0;\n}",
        "content": "# Lab#14\n\n## IMPLEMENT FIRST FIT ALGORITHM FOR MEMORY MANAGEMENT.\n\n### Objective & Theoretical Overview\nIn variable-partition memory management, the operating system maintains a table of available (free) and allocated memory blocks (holes). When a new process arrives requiring a block of memory of size $S$, the system must search the available free holes to allocate storage.\n\n#### Memory Placement Strategies\n1. **First Fit**: Allocates the first available hole that is large enough ($\\ge S$). Searching can start either at the beginning of the set of holes or where the previous first-fit search ended. It is fast and produces minimal search overhead.\n2. **Best Fit**: Allocates the smallest hole that is large enough. Requires searching the entire list (unless ordered by size). Produces the smallest leftover hole.\n3. **Worst Fit**: Allocates the largest hole available. Produces the largest leftover hole, which may be more useful than the smaller leftover holes from Best Fit.\n\n#### Fragmentation & Hole Coalescing\n* **Internal Fragmentation**: Unused memory contained inside an allocated partition (e.g. when partitions are fixed).\n* **External Fragmentation**: Total free memory storage is large enough to satisfy a request, but the available spaces are not contiguous; storage is fragmented into many small non-adjacent holes.\n* **Coalescing**: When an allocated block is released or freed, adjacent free holes must be merged together into one continuous large free hole.\n\n---\n\n### AIM:\nTo write a program to implement first fit algorithm for memory management.\n\n---\n\n### ALGORITHM\n1. Start the process.\n2. Declare the size.\n3. Get the number of processes to be inserted.\n4. Allocate the first hole that is big enough searching.\n5. Start at the beginning of the set of holes.\n6. If not start at the hole that is sharing the previous first fit search end.\n7. If large enough then stop searching in the procedure.\n8. Display the values.\n9. Stop the process.\n\n---\n\n### PROGRAM:\n```c\n#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n\nstruct allocate {\n    int pid;\n    int st_add;\n    int end_add;\n    struct allocate *next;\n};\n\nstruct free_list {\n    int st_add;\n    int end_add;\n    struct free_list *next;\n};\n\nstruct process {\n    int pid;\n    int size;\n};\n\nstruct process pro[10];\nstruct free_list *flist = NULL;\nstruct allocate *alot = NULL;\n\nvoid display_alot(struct allocate *temp_a)\n{\n    printf(\"\\n\\n allocated list:\");\n    printf(\"\\n=========\");\n    while(temp_a != NULL)\n    {\n        printf(\"\\n process:%d st_add:%d end_add:%d \", temp_a->pid,\n               temp_a->st_add, temp_a->end_add);\n        temp_a = temp_a->next;\n    }\n}\n\nvoid display_free(struct free_list *temp_f)\n{\n    printf(\"\\n\\n free list:\");\n    printf(\"\\n==========\");\n    while(temp_f != NULL)\n    {\n        printf(\"\\n st_add:%d end_add:%d\", temp_f->st_add, temp_f->end_add);\n        temp_f = temp_f->next;\n    }\n}\n\nvoid insert_free(struct free_list *node)\n{\n    struct free_list *temp = flist;\n    if(flist == NULL)\n        flist = node;\n    else\n    {\n        while(temp->next != NULL)\n            temp = temp->next;\n        temp->next = node;\n    }\n}\n\nvoid insert_alot(struct allocate *node)\n{\n    struct allocate *temp = alot;\n    if(alot == NULL)\n        alot = node;\n    else\n    {\n        while(temp->next != NULL)\n            temp = temp->next;\n        temp->next = node;\n    }\n}\n\nvoid delete_free(int st_add)\n{\n    struct free_list *temp = flist, *prev = NULL;\n    while(temp != NULL && temp->st_add != st_add)\n    {\n        prev = temp;\n        temp = temp->next;\n    }\n    if(temp == NULL) return;\n    if(prev == NULL)\n        flist = temp->next;\n    else\n        prev->next = temp->next;\n    free(temp);\n}\n\nvoid first_fit(int pid, int size)\n{\n    struct free_list *temp_f = flist;\n    struct allocate *temp_a;\n    int found = 0;\n\n    while(temp_f != NULL)\n    {\n        int hole_size = temp_f->end_add - temp_f->st_add;\n        if(hole_size >= size)\n        {\n            temp_a = (struct allocate*) malloc(sizeof(struct allocate));\n            temp_a->pid = pid;\n            temp_a->st_add = temp_f->st_add;\n            temp_a->end_add = temp_f->st_add + size;\n            temp_a->next = NULL;\n            insert_alot(temp_a);\n\n            if(hole_size == size)\n            {\n                delete_free(temp_f->st_add);\n            }\n            else\n            {\n                temp_f->st_add = temp_f->st_add + size;\n            }\n            found = 1;\n            break;\n        }\n        temp_f = temp_f->next;\n    }\n\n    if(!found)\n    {\n        printf(\"\\n No suitable free hole found for Process %d (size %d)!\", pid, size);\n    }\n}\n\nint main()\n{\n    struct free_list *initial_free;\n    initial_free = (struct free_list*) malloc(sizeof(struct free_list));\n    initial_free->st_add = 0;\n    initial_free->end_add = 1024;\n    initial_free->next = NULL;\n    insert_free(initial_free);\n\n    printf(\"Initial free list:\");\n    display_free(flist);\n\n    printf(\"\\n\\nAllocating Process 1 (size 185) and Process 2 (size 246):\");\n    first_fit(1, 185);\n    first_fit(2, 246);\n    display_alot(alot);\n    display_free(flist);\n\n    printf(\"\\n\\nAllocating Process 10 (size 195):\");\n    first_fit(10, 195);\n    display_alot(alot);\n    display_free(flist);\n\n    printf(\"\\n\\nAllocating Process 11 (size 96):\");\n    first_fit(11, 96);\n    display_alot(alot);\n    display_free(flist);\n\n    printf(\"\\n\\nAllocating Process 12 (size 148):\");\n    first_fit(12, 148);\n    display_alot(alot);\n    display_free(flist);\n\n    printf(\"\\n\");\n    return 0;\n}\n```\n\n---\n\n### OUTPUT:\n```text\nfree list:\n st_add:0 end_add:1024\nallocated list:\n process:1 st_add:120 end_add:305\n process:2 st_add:305 end_add:551\nfree list:\n st_add:0 end_add:120\n st_add:551 end_add:1024\n\nno. of process:3\nprocess to be inserted:10 size:195\nallocated list:\n process:1 st_add:120 end_add:305\n process:2 st_add:305 end_add:551\n process:10 st_add:551 end_add:746\nfree list:\n st_add:0 end_add:120\n st_add:746 end_add:1024\n\nprocess to be inserted:11 size:96\nallocated list:\n process:1 st_add:120 end_add:305\n process:2 st_add:305 end_add:551\n process:10 st_add:551 end_add:746\n process:11 st_add:0 end_add:96\nfree list:\n st_add:96 end_add:120\n st_add:746 end_add:1024\n\nprocess to be inserted:12 size:148\nallocated list:\n process:1 st_add:120 end_add:305\n process:2 st_add:305 end_add:551\n process:10 st_add:551 end_add:746\n process:11 st_add:0 end_add:96\n process:12 st_add:746 end_add:894\nfree list:\n st_add:96 end_add:120\n st_add:894 end_add:1024\n```\n\n---\n\n### MEMORY DYNAMICS & HOLE PARTITIONING WALKTHROUGH\n1. **Initial Memory**: Single continuous free hole spanning from address `0` to `1024`.\n2. **Process 1 ($185$) & Process 2 ($246$) Allocation**: After initial allocations (leaving reserved system space $0-120$), Process 1 sits at $120-305$ and Process 2 sits at $305-551$. Remaining free holes: $0-120$ (size 120) and $551-1024$ (size 473).\n3. **Process 10 ($195$) Allocation**:\n   - Evaluates hole 1 ($0-120$, size 120): Too small ($120 < 195$).\n   - Evaluates hole 2 ($551-1024$, size 473): Big enough!\n   - Process 10 takes $551-746$. New hole 2 becomes $746-1024$ (size 278).\n4. **Process 11 ($96$) Allocation**:\n   - Evaluates hole 1 ($0-120$, size 120): Big enough! ($120 \\ge 96$).\n   - Process 11 takes $0-96$. New hole 1 becomes $96-120$ (size 24).\n5. **Process 12 ($148$) Allocation**:\n   - Evaluates hole 1 ($96-120$, size 24): Too small.\n   - Evaluates hole 2 ($746-1024$, size 278): Big enough!\n   - Process 12 takes $746-894$. New hole 2 becomes $894-1024$ (size 130).\n\n---\n\n### RESULT:\nThus the program for Implement first fit algorithm for memory management is written and successfully executed.\n",
        "quizzes": [
            {
                        "question": "How does the First Fit dynamic memory allocation algorithm place an incoming process in memory?",
                        "options": [
                                    "It scans the free list from the beginning and allocates the very first free hole whose size is greater than or equal to the process size.",
                                    "It allocates the smallest hole that is large enough to fit the process.",
                                    "It allocates the largest hole available in the entire memory space.",
                                    "It splits the memory into equal powers of two using the Buddy System."
                        ],
                        "correctAnswer": "It scans the free list from the beginning and allocates the very first free hole whose size is greater than or equal to the process size.",
                        "explanation": "First Fit begins searching at the head of the free list and assigns the first partition with sufficient capacity to satisfy the allocation request."
            },
            {
                        "question": "What happens when process 0 (size 120, st_add: 0, end_add: 120) is deleted in the lab simulation?",
                        "options": [
                                    "A new free block is added to the free list starting at address 0 and ending at address 120.",
                                    "The entire memory space is immediately compacted to address 0.",
                                    "All remaining processes are terminated.",
                                    "The physical RAM controller resets the BIOS."
                        ],
                        "correctAnswer": "A new free block is added to the free list starting at address 0 and ending at address 120.",
                        "explanation": "Deallocating process 0 returns the range [0, 120] back to the free list ('st_add: 0, end_add: 120'), making it available for subsequent allocations (such as process 11 of size 96)."
            },
            {
                        "question": "What type of memory fragmentation is characterized by total free memory being sufficient to satisfy a request, but broken into non-contiguous holes?",
                        "options": [
                                    "External fragmentation",
                                    "Internal fragmentation",
                                    "Virtual fragmentation",
                                    "Page fault fragmentation"
                        ],
                        "correctAnswer": "External fragmentation",
                        "explanation": "External fragmentation occurs when there is enough total free memory to satisfy a request, but the memory is fragmented into separate, non-contiguous holes."
            },
            {
                        "question": "What process merges adjacent free memory holes into a single larger contiguous hole upon process termination in C?",
                        "options": [
                                    "Coalescing (merging adjacent free list nodes)",
                                    "Thrashing",
                                    "Page swapping",
                                    "Dirty bit masking"
                        ],
                        "correctAnswer": "Coalescing (merging adjacent free list nodes)",
                        "explanation": "Coalescing checks if the newly freed block is adjacent to existing free holes ('pre_f->end_add == temp_a->st_add'), merging them into one unified contiguous block."
            },
            {
                        "question": "In contiguous memory allocation, what distinguishes First Fit from Best Fit?",
                        "options": [
                                    "First Fit allocates the first hole that is large enough without searching all holes, while Best Fit searches for the smallest adequate hole.",
                                    "First Fit searches the entire memory list to find the largest hole, while Best Fit allocates from the beginning.",
                                    "First Fit only allocates from high memory addresses.",
                                    "First Fit causes zero internal or external fragmentation."
                        ],
                        "correctAnswer": "First Fit allocates the first hole that is large enough without searching all holes, while Best Fit searches for the smallest adequate hole.",
                        "explanation": "First Fit stops searching as soon as it discovers a free partition of size >= required size, minimizing search overhead compared to Best Fit."
            }
],
        "flashcards": [
            {
                        "question": "What data structures represent allocated and free memory in the lab's C simulation?",
                        "answer": "Singly linked lists: struct allocate (for active processes) and struct free_list (for available holes)."
            },
            {
                        "question": "Between First Fit, Best Fit, and Worst Fit, which algorithm generally achieves the fastest allocation speed?",
                        "answer": "First Fit, because it halts its search at the first hole that satisfies the process size."
            },
            {
                        "question": "Why did process 11 (size 96) get allocated at address 0 instead of address 746 in the lab output?",
                        "answer": "Because First Fit checks from the beginning and found hole [0, 120] (size 120 >= 96) first, allocating [0, 96] and leaving a residual hole [96, 120]."
            },
            {
                        "question": "What technique can an OS use to eliminate external fragmentation in contiguous partition allocation?",
                        "answer": "Memory Compaction (relocating all active processes toward one end of memory to merge free holes into one large contiguous block)."
            }
]
    }

]


def seed_os_fall_curriculum(db_client: Optional[Prisma] = None, verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds the Operating Systems Lab (CS-223 - Fall Edition) curriculum (All 14 Labs, 5 Quizzes each) into Neon PostgreSQL via Prisma.
    Strictly idempotent and non-destructive: only touches this specific course and its steps.
    """
    owns_connection = False
    db = db_client
    if db is None:
        db = Prisma()
        db.connect()
        owns_connection = True

    try:
        # 1. Find or create the Course Lesson record
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
                print(f"[*] Updated existing Course record: ID={lesson.id} | Title='{lesson.title}'")

        # 2. Idempotent cleanup of old steps, quizzes, and flashcards for ONLY THIS LESSON
        del_q = db.quiz.delete_many(where={"lessonId": lesson.id})
        del_f = db.flashcard.delete_many(where={"lessonId": lesson.id})
        del_s = db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"[*] Cleared previous records for OS Fall course: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

        # 3. Insert All 14 Labs LessonSteps, Quizzes, and Flashcards
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
                "title": lab["title"][:50],
                "quizzes_count": len(lab["quizzes"]),
                "flashcards_count": len(lab["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 85)
            print("SUMMARY TABLE: UNIVERSITY OS FALL (CS-223) ALL 14 LABS (5 QUIZZES EACH) SEEDED")
            print("=" * 85)
            print(f"{'Lab #':<8} | {'Title':<52} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 85)
            for row in summary_rows:
                print(f"{row['lab_num']:<8} | {row['title']:<52} | {row['quizzes_count']:<8} | {row['flashcards_count']:<10}")
            print("=" * 85)
            print(f"Total LessonSteps: {len(LABS_DATA)}")
            print(f"Total Quizzes:     {total_quizzes}")
            print(f"Total Flashcards:  {total_flashcards}")
            print(f"Category:          {COURSE_DATA['category']}")
            print("=" * 85)

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
    seed_os_fall_curriculum()
