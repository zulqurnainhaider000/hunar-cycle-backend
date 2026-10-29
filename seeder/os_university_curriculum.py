"""
OS University Curriculum Seeder (CS-223L Operating Systems)
100% Verbatim transcription from "Operating Systems (Updated Version).pdf" for Department of Computing, Faculty of Engineering Sciences & Technology, Hamdard University Islamabad Campus.
Populates University Laboratory Modules (Labs 1 to 14) with zero data loss, exact paragraphs, CLI listings, tables, tasks, quizzes, and flashcards.
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from prisma import Prisma

COURSE_DATA = {
    "title": "Operating Systems (CS-223L)",
    "category": "University",
    "description": "Official Academic Curriculum for CS-223L Operating Systems. Comprehensive university laboratory manual covering Linux shell commands, file and directory administration, shell scripting fundamentals, control flow & functions, Perl scripting, Linux process management & job control, POSIX multithreading (Pthreads), CPU scheduling, page replacement, memory allocation, and classical synchronization problems.",
    "color": "#2563EB",
    "thumbnail": "assets/images/university/os/os_fest_logo.png"
}

LABS_DATA = [
    {
        "order": 1,
        "title": "Lab 1: Practice Frequently Used Linux Operating System Commands",
        "codeSnippet": "# Frequently used Linux commands\npwd\ncd /home/user1\nls -la /usr/bin\nman grep\nfind / -name myfile -print\ncat file.txt | grep \"pattern\" | more",
        "content": "# Lab#01\n\n## PRACTICE SOME OF THE MOST FREQUENTLY USED LINUX OPERATING SYSTEM COMMANDS.\n\n![OS Architecture Overview](assets/images/university/os/os_architecture_overview.png)\n\n### Objective\n* Familiarization with some of the most frequently used Linux commands\n\n### Theory Overview\nA Linux command is any executable file. That is, a command consists of any file that is designed to be run, as opposed to files containing data or configuration information. This means that any executable file added to the system becomes a new command on the system. Most Linux commands are very flexible. When you enter a Linux command, there are several ways to tailor the basic command to your specific needs. There are two main ways used to modify the effect of a command:\n* Specifying or redirecting a command's input and output\n* Using command options\n\n#### Command options\nYou can use command options to fine-tune the actions of a Linux command. Quite often, a Linux command will do almost—but not quite—what you want it to do. Instead of making you learn a second command, Linux lets you modify the basic, or default, actions of the command by using options.\n\n#### OTHER PARAMETERS\nLinux commands often use parameters that are not actual command options. These parameters, such as filenames or directories, are not preceded by a dash.\n\n#### INPUT AND OUTPUT REDIRECTION\nLinux allows to \"pipe\" the output from a command so that it becomes another command's input. This is done by typing two or more commands separated by the `|` character. (This character normally is found on the same key as the `\\` character. You must hold down the Shift key or you will get `\\` instead of `|`). The `|` character means \"Use the output from the previous command as the input for the next command.\" Therefore, typing `command_1 | command_2` does both commands, one after the other, before giving you the results.\n\nAnother thing you can do in Linux is to send output to a file instead of the screen. There are many different reasons why you might want to do this. You might want to save a \"snapshot\" of a command's output as it was at a certain time, or you might want to save a command's output for further examination. You might also want to save the output from a command that takes a very long time to run, and so on.\nTo send output to a file, use the `>` symbol.\n\n#### EXECUTING A LINUX COMMAND\nFrom the command prompt simply type the name of the command:\n```bash\n$ command\n```\nWhere `$` is the prompt character for the Bourne shell.\n\nOr if the command is not on your path type the complete path and name of the command such as:\n```bash\n$ /usr/bin/command\n```\n\nSome of the frequently used Linux commands are:\n* `su`\n* `pwd`, `cd`, and `ls`\n* `more` and `less`\n* `find` and `grep`\n* `man`\n\n---\n\n### su\n**Description:** Runs a new shell under different user and group IDs. If no user is specified, the new shell will run as the root user.\nUsually, when you want to temporarily become a different user, you will simply switch to another virtual terminal, log in as the other user, log out when you're done, and return to your \"home\" virtual terminal. However, there are times when this is impractical or inconvenient. Perhaps all your virtual terminals are already busy, or perhaps you're in a situation (such as logged on via a telephone and modem) in which you don't have virtual terminals available. In these cases, you can use the `su` command. \"su\" stands for \"super user.\" If you type `su` by itself, you will be prompted for the root password. If you successfully enter the root password, you will see the root `#` prompt, and you will have all of root's privileges. You can also become any other user by typing `su <username>`. If you are root when you type `su <username>`, you are not asked for that user's password since in principle you could change the user's password or examine all the user's files from the root login anyway. If you are an \"ordinary\" user trying to change to another ordinary user, you will be asked to enter the password of the user you are trying to become.\n\n**Syntax:**\n```bash\nsu [ -flmp] [ -c command] [ -s shell] [ --login] [ --fast] [ --preserve-environment] [ --command=command] [--shell=shell] [-] [user]\n```\n(see the man pages for the description of the flags and options)\n```bash\n$ su <username>    # to become another user\n$ su               # to become the root user\n```\n\n**Adding a new user:**\n```bash\n# useradd user1\n# passwd user1\n<password>\n```\n\n---\n\n### pwd\n**Description:** Displays the name of the current directory. `pwd` stands for present working directory. By typing this command you are informed of which directory you are currently in.\n\n**Syntax:**\n```bash\n$ pwd\n```\n\n---\n\n### cd\n**Description:** Changes the current directory to any accessible directory on the system.\n\n**Syntax:**\nFor instance to change from `/home/user1` to a subdirectory of user1 `wordfiles` use the following:\n```bash\n$ cd wordfiles\n$ pwd\n/home/user1/wordfiles\n```\nTo change to `/tmp` use the following:\n```bash\n$ cd /tmp\n$ pwd\n/tmp\n```\n\n---\n\n### ls\n**Description:** Displays the listing of files and directories. If no file or directory is specified, then the current directory's contents are displayed. By default the contents are sorted alphabetically.\n\n**Syntax:**\nTo view the contents of user1 home directory use this:\n```bash\n$ ls\n```\nTo list the contents of any directory on the system use:\n```bash\n$ ls /usr\n```\n\n---\n\n### more\n**Description:** Displays one or more files screen by screen and allows for searching and jumping to an arbitrary location in the file.\n\n**Syntax:**\n```bash\nmore [-dlfs] [-number] [+number] [file....]\n```\n\n**IMPORTANT FLAGS AND OPTIONS:**\n* `-number`: sets the number of lines per screen.\n* `+number`: specifies the line to start on when displaying.\n* `-d`: prompts the user at the end of each screen.\n* `-f`: causes long lines not to be folded and to be counted as a single line.\n* `-l`: prevents Ctrl+L from being treated as a form feed.\n* `-s`: squeezes multiple blank lines into a single blank line.\n\nFor example if there is a large text file called \"textfile\", it can be viewed a page at a time with the following command:\n```bash\n$ more textfile\n```\nAfter pressing Enter, the first screen of the file is seen with the text `-More-` displayed on the last line of the screen. Pressing the space bar jumps forward a full screen length, while pressing enter key moves forward one line at a time. When the end of the body of the text is reached, the command prompt appears. To search forward through a file, enter slash (`/`) followed by the word or phrase you want to search for and then press enter. The display jumps forward to the first occurrence of the word or phrase being searched for and displays the occurrence near the top of the screen. The same search can be repeated by entering `n` after the first search, avoiding the need to type the same word or phrase repeatedly.\n\n---\n\n### less\n**Description:** Displays a text file one screen at a time while allowing searching and backward scrolling.\n\n**Syntax:**\n```bash\nless [-aeEGiINrsS] file.....\n```\n(the details of the flags can be seen from man pages).\nThis command is an improved version of the previous one. In addition to the functions previously described the following are some of the other actions that can be performed using `less`:\n* Jumping directly to a line.\n* Jumping directly to the beginning or end of file.\n* Moving backward through the file.\n* Searching backward through the file.\n\n---\n\n### find\n**Description:** Looks for files below the specified paths that match all the criteria indicated by the command-line options and takes any action indicated by those options. If no paths are specified, the search takes place below the current directory.\n\n**Syntax:**\n```bash\nfind [path.....] [options]\n```\n(see the man pages for the flags and options).\nThis command can be used to search for files by name, date of creation, size and even file type. To search for files by name use the following syntax:\n```bash\n$ find starting-directory parameters actions\n```\n* The `starting-directory` specifies where to begin searching.\n* The `parameters` are where you specify the criteria by which to search. Here use `-name filename` to specify the file to search for.\n* The `actions` section indicates what actions to take on found files. If `-print` is used then the full name and path of file is displayed.\n\nTo search for all files named `myfile` on your system, use this:\n```bash\n$ find / -name myfile -print\n```\n*(Notice that the previous command attempted to search for the entire system. To do this effectively user must be logged in as the root user).*\n\n---\n\n### grep\n**Description:** Searches files for lines matching a specific pattern and displays the lines.\n\n`grep` stands for Global Regular Expression Parser. What `grep` does, essentially, is find and display lines that contain a pattern that you specify. There are two basic ways to use grep:\n1. **Filter output of other commands:** The general syntax is `<command> | grep <pattern>`. For instance, to see every actively running process:\n```bash\nps -a | grep R\n```\nIn this application, grep passes on only those lines that contain the pattern (single letter R). To search for an R with spaces around it:\n```bash\ngrep \" R \"\n```\nYou must use quotes whenever you search for a pattern that contains one or more blank spaces.\n2. **Search for lines in a specified file:** The syntax is:\n```bash\ngrep <pattern> <filename>\n```\nBe careful: specify the pattern first and filename second.\n\n**Syntax:**\nAssuming that you are in your home directory, searching for the word \"hello\" in each file in your home directory:\n```bash\n$ grep hello*\n```\nIn general the pattern for grep is:\n```bash\n$ grep text-pattern file-list\n```\nTo check for the contents of all files in a directory:\n```bash\n$ grep text-pattern *\n```\nTo search for a phrase with spaces:\n```bash\n$ grep \"is a test\" *\n```\n\n---\n\n### USING THE man PAGES\nThe man pages are manual pages provided in a standard format with most Linux software. Almost all the commands that ship with Red Hat Linux distribution include man pages. Using the man command in its most basic form:\n```bash\n$ man command-name\n```\n**Syntax:**\n```bash\nman [options] [section] [title]\n```\n\n**The man pages are divided into sections:**\n1. Executable programs or shell commands\n2. System calls (functions provided by the kernel)\n3. Library calls (functions within system libraries)\n4. Special files (usually found in `/dev`)\n5. File formats and conventions e.g. `/etc/passwd`\n6. Games\n7. Macro packages and conventions\n8. System administration commands (usually only for a privileged user)\n9. Kernel routines (nonstandard)\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Write a command to:\n   * List all files (and subdirectories) in the home directory.\n   * List all files beginning with `memo` owned by `ann`.\n   * Search the current directory, look for filenames that don't begin with a capital letter.\n   * Search the system for files that were modified within the last two days.\n   * List files in your home folder in human readable format.\n   * List all files in the current directory and their sizes; use multiple columns and mark special files.\n   * List the contents of directories `/bin` and `/etc`.\n   * List C source files in the current directory, showing larger file first.\n   * Count all files in the current directory.\n",
        "quizzes": [
            {
                "question": "What does the pipe operator (|) accomplish when executing commands in Linux?",
                "options": [
                    "It directs the standard output of the preceding command to become the standard input of the subsequent command.",
                    "It executes two commands strictly in parallel across different physical CPU cores.",
                    "It redirects the terminal error stream into a permanent log file on disk.",
                    "It terminates the preceding process and launches the next process with elevated root privileges."
                ],
                "correctAnswer": "It directs the standard output of the preceding command to become the standard input of the subsequent command.",
                "explanation": "In Linux, the pipe operator (|) connects the standard output (stdout) of the first command directly to the standard input (stdin) of the second command."
            },
            {
                "question": "What is the primary operational advantage of the 'less' command compared to 'more' when inspecting long text files?",
                "options": [
                    "less allows both backward scrolling and forward scrolling through a file, whereas more only scrolls forward.",
                    "less automatically edits and formats binary machine files in real time.",
                    "less executes the entire text file as an executable shell script.",
                    "more requires root privileges to open text files, while less does not."
                ],
                "correctAnswer": "less allows both backward scrolling and forward scrolling through a file, whereas more only scrolls forward.",
                "explanation": "While 'more' only allows forward paging, 'less' is an enhanced pager supporting bi-directional navigation (backward scrolling, line jumps, and reverse regex searches)."
            },
            {
                "question": "Which section of the Linux man manual pages documents System Calls provided directly by the operating system kernel?",
                "options": [
                    "Section 2",
                    "Section 1",
                    "Section 3",
                    "Section 8"
                ],
                "correctAnswer": "Section 2",
                "explanation": "In standard Linux manual documentation, Section 1 covers executable programs and shell commands, Section 2 covers kernel system calls, Section 3 covers library calls, and Section 8 covers system administration commands."
            },
            {
                "question": "Which Linux command lists all C source files (*.c) in the current directory sorted with the largest file displayed first?",
                "options": [
                    "ls -lS *.c",
                    "ls -lt *.c",
                    "find . -name *.c -sort",
                    "grep -S *.c"
                ],
                "correctAnswer": "ls -lS *.c",
                "explanation": "The '-S' option in 'ls' sorts directory contents by file size in descending order (largest first), and '*.c' matches all C source files."
            }
        ],
        "flashcards": [
            {
                "question": "What does 'pwd' stand for and what information does it return?",
                "answer": "Print Working Directory (or Present Working Directory). It prints the absolute path of the directory you are currently working in."
            },
            {
                "question": "What does 'grep' stand for and what is its primary function?",
                "answer": "Global Regular Expression Parser. It searches files or input streams for lines matching a specified pattern or regular expression and outputs matching lines."
            },
            {
                "question": "How do you search for a pattern containing multiple words or blank spaces using grep?",
                "answer": "Enclose the multi-word pattern in quotation marks, e.g., grep \"is a test\" filename."
            },
            {
                "question": "How does the '>' operator differ from '|' in Linux CLI?",
                "answer": "The '>' operator redirects standard output to a file (creating or overwriting it), whereas '|' pipes output as standard input into another executable command."
            }
        ]
    },
    {
        "order": 2,
        "title": "Lab 2: Practice Linux Commands Related to Files and Directories",
        "codeSnippet": "# File manipulation and permissions\ncat > notes.txt << 'EOF'\nOperating Systems Lab 2\nEOF\nchmod 755 notes.txt\nchown user:users notes.txt\ntar cvf backup.tar notes.txt\ngzip backup.tar",
        "content": "# Lab#02\n\n## PRACTICE LINUX COMMANDS RELATED TO FILES AND DIRECTORIES.\n\n### Objective\n* Studying the Linux commands related to files and directories.\n\n### Theory Overview\nThe most basic concept of a file defines it as a distinct chunk of information that is found on the hard drive. Distinct means that there can be many different files, each with its own particular contents. To keep files from getting confused with each other, every file must have a unique identity. In Linux, you identify each file by its name and location. In each location or directory, there can be only one file by a particular name.\n\n#### Filenames\nLinux allows filenames to be up to 256 characters long. These characters can be lower- and uppercase letters, numbers, and other characters, usually the dash (`-`), the underscore (`_`), and the dot (`.`). They can't include reserved metacharacters such as the asterisk (`*`), question mark (`?`), backslash (`\\`), and space, because these all have meaning to the shell.\n\n#### Directories\nLinux, like many other computer systems, organizes files in directories. You can think of directories as file folders and their contents as the files. However, there is one absolutely crucial difference between the Linux file system and an office filing system. In the office, file folders usually don't contain other file folders. In Linux, file folders can contain other file folders. In fact, there is no Linux \"filing cabinet\"—just a huge file folder that holds some files and other folders. These folders contain files and possibly other folders in turn, and so on.\n\n#### Parent Directories and Subdirectories\nImagine a scenario in which you have a directory, A, that contains another directory, B. Directory B is then a subdirectory of directory A, and directory A is the parent directory of directory B.\n\n#### The Root Directory\nIn Linux, the directory that holds all the other directories is called the root directory. This is the ultimate parent directory; every other directory is some level of subdirectory. From the root directory, the whole structure of directory upon directory springs and grows like some electronic elm. This is called a tree structure because, from the single root directory, directories and subdirectories branch off like tree limbs.\n\n#### Naming Directories\nDirectories are named just like files, and they can contain upper- and lowercase letters, numbers, and characters such as `-`, `.`, and `_`. The slash (`/`) character is used to show files or directories within other directories. For instance, `usr/bin` means that `bin` is found in the `usr` directory. Note that you can't tell, from this example, whether `bin` is a file or a directory, although you know that `usr` must be a directory because it holds another item—namely, `bin`. When you see `usr/bin/grep`, you know that both `usr` and `bin` must be directories, but again, you can't be sure about `grep`. The `ls` program shows directories with a following `/`—for example, `fido/`. This notation implies that you could have, for instance, `fido/file`; therefore, `fido` must be a directory.\n\nThe root directory is shown simply by the symbol `/` rather than mentioned by name. If `/` has no name before it, it stands for the root directory. For example, `/usr` means that the `usr` subdirectory is found in the root directory, and `/usr/bin` means that `bin` is found in the `usr` directory and that `usr` is a subdirectory of the root directory. Remember, by definition the root directory can't be a subdirectory.\n\n#### THE HOME DIRECTORY\nLinux provides each user with his or her own directory, called the home directory. Within this home directory, users can store their own files and create subdirectories. Users generally have complete control over what's found in their home directories. Because there are usually no Linux system files or files belonging to other users in your home directory, you can create, name, move, and delete files and directories as you see fit. The location of a user's home directory is specified by Linux and can't be changed by the user. This is both to keep things tidy and to preserve system security.\n\n#### IMPORTANT DIRECTORIES IN THE LINUX FILE SYSTEM\nMost of the directories that hold Linux system files are \"standard.\" Other UNIX systems will have identical directories with similar contents:\n* `/`: Root directory. Holds the actual Linux operating system, as well as subdirectories. Do not clutter this directory with your files!\n* `/home`: Holds users' home directories. In other UNIX systems, this can be the `/usr` or `/u` directory.\n* `/bin`: Holds many of the basic Linux programs. `bin` stands for binaries, files that are executable.\n* `/usr`: Holds user-oriented directories:\n  * `docs`: Various documents, including useful Linux information.\n  * `man`: The man pages accessed by typing `man <command>`.\n  * `games`: Games programs.\n* `/usr/bin`: Holds user-oriented Linux programs.\n* `/var/spool`: Spool directory (holds `mail`, `spool` files for printers, `uucp`).\n* `/dev`: Linux treats everything as a file! Holds device special files that serve as gateways to physical hardware components (e.g. `/dev/fd0` floppy disk, `/dev/tty` terminals, `/dev/hd0` hard disk partitions). A famous device is `/dev/null` (the \"bit bucket\") where all sent information vanishes.\n* `/usr/sbin`: System administration executable files (run by root).\n* `/sbin`: System files that are run automatically by the Linux system.\n* `/etc`: Holds system configuration text files.\n\n---\n\n### CREATING FILES\nA file can be created by output redirection:\n```bash\n$ ls -l /bin > test\n```\nWhen you redirect to a file, Linux automatically creates the file if it doesn't already exist.\n\n#### THE CAT COMMAND\nThe `cat` command stands for **concatenate**. It takes all its input and outputs it:\n```bash\n$ cat > newfile\nHello world\nHere's some text\n```\nPress `^D` (Ctrl-D) at the start of a blank line to signal End Of File (EOF).\nTo view files:\n```bash\n$ cat newfile\n```\nTo append to an existing file, use `>>`:\n```bash\n$ cat >> newfile\nSome more lines\n```\nTo concatenate multiple files:\n```bash\n$ cat newfile anotherfile > thirdfile\n```\n\n---\n\n### MOVING AND COPYING FILES\n* `mv <source> <destination>`: Moves or renames files. Extremely efficient because file contents are not copied; Linux simply updates directory pointers.\n* `cp <source> <destination>`: Creates a second physical duplicate on disk.\n\nExamples:\n```bash\n$ mv fileone /tmp\n$ mv fileone /tmp/newfilename\n$ mv fileone newfilename             # Renaming\n$ mv *.bak *.tmp *.old /tmp          # Moving multiple files\n```\n\nFor copying:\n```bash\n$ cp thisfile thisfile-copy\n$ cp thisfile /tmp\n$ cp -i thisfile newfile             # -i prompts before overwriting\n$ alias cp='cp -i'                   # Safe alias\n$ cp fileone filetwo filethree /tmp  # Copy multiple files to destination directory\n$ cp *.txt *.doc *.bak /tmp\n$ cp -R somedir /tmp                 # -R recursive directory copy\n```\n\n**Common `cp` flags:**\n* `-a` / `--archive`: Copies recursively, preserving symbolic links, ownership, and permissions (`-dpR`).\n* `-b` / `--backup`: Makes backups before overwriting.\n* `-d` / `--no-dereference`: Copies links as links.\n* `-f` / `--force`: Forces overwrite.\n* `-i` / `--interactive`: Prompts before overwriting.\n* `-l` / `--link`: Creates hard links instead of copying.\n* `-p` / `--preserve`: Preserves ownership, timestamps, and permissions.\n* `-R` / `--recursive`: Recursively copies directories.\n\n---\n\n### CREATING AND REMOVING DIRECTORIES\n* **Create Directory:** `mkdir <name>`\n```bash\n$ mkdir newdir\n```\n*(Note: Linux does not recognize DOS abbreviation `md`; you must use `mkdir`)*.\n\n* **Move Directory:** `mv <directory> <destination>`\n* **Remove File:** `rm <filename>`\n  * `rm -i *files` (Interactive removal)\n  * `rm -r <directory>` (Recursive removal of directory and contents)\n  * *Warning: Never run `rm -rf /` as root!*\n* **Remove Directory:** `rmdir <directory>`\n  * Directory must be completely empty (cannot contain files or subdirectories).\n  * If files starting with `.` exist, they must be removed first using `rm .*`.\n\n---\n\n### FILE PERMISSIONS AND OWNERSHIP\nAll Linux files have ownership (User and Group) and permission settings:\n```text\n-rw-r--r-- 1 fido users 163 Dec 7 14:31 myfile\n```\n* Leading character: `-` for regular file, `d` for directory.\n* Ownership: `chown <owner> <filename>` (e.g. `chown root myfile`).\n* Group: `chgrp <group> <filename>`.\n\n#### Permission Triplets:\n* **User (Owner)** | **Group** | **Other (Everyone else)**\n* `r`: Read (value = 4)\n* `w`: Write (value = 2)\n* `x`: Execute (value = 1)\n\n**Numeric Permissions:**\n* `7` (`rwx`): 4 + 2 + 1 = Read, write, execute\n* `6` (`rw-`): 4 + 2 = Read and write\n* `5` (`r-x`): 4 + 1 = Read and execute\n* `4` (`r--`): Read only\n* `0` (`---`): No permissions\n\nChanging permissions with `chmod`:\n```bash\n$ chmod 755 myfile       # rwxr-xr-x\n$ chmod 701 myfile       # rwx-----x\n$ chmod go+r myfile      # Symbolic mode: add read for group and other\n```\n*(Note: Directory execute permission `x` is required to `cd` into it; write permission `w` on a directory allows creating or deleting files within it).*\n\n---\n\n### THE tar AND gzip COMMANDS\n* **`tar` (Tape Archive):** Creates archives of files without compression.\n  * Create: `tar cvf archive.tar file-list` (`c`=create, `v`=verbose, `f`=file)\n  * View: `tar tvf archive.tar` (`t`=table of contents)\n  * Extract: `tar xvf archive.tar` (`x`=extract)\n* **`gzip`:** Compresses individual files by adding `.gz` extension:\n  * Compress: `gzip test.pdf` -> produces `test.pdf.gz`\n  * Uncompress: `gzip -d test.pdf.gz` or `gunzip test.pdf.gz`\n\n---\n\n### SOFTWARE INSTALLATION\n1. **RPM (Red Hat Package Manager):**\n```bash\n$ rpm -ivh /home/user/xyz.rpm\n```\n* `-i`: install\n* `-v`: verbose\n* `-h`: print hash marks during progress\n* `-e`: erase/uninstall\n* `-q`: query\n* `-U`: upgrade\n\n2. **Source Tarball (`.tar.gz`):**\n```bash\n1. tar xzvf software.tar.gz\n2. Read README / INSTALL\n3. ./configure          # Generates Makefile\n4. make                 # Compiles source code\n5. su                   # Switch to root\n6. make install         # Copies binaries to system paths\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Explain what the following commands do (with examples) and practice them:\n   * `lockfile`\n   * `cksum`\n   * `comm`\n   * `csplit`\n   * `chattr`\n   * `touch`\n2. What do the following commands do:\n   * `cat ch1`\n   * `cat ch1 ch2 ch3 > \"your-practical-group\"`\n   * `cat note5 >> notes`\n   * `cat > temp1`\n   * `cat > temp2 << \"yourname\"`\n3. Practice the following commands and explain each:\n   * `cpio`\n   * `sort`\n   * `fuser`\n   * `file`\n4. What does the `z` option of the `tar` command do? Explain with examples.\n5. Differentiate between `cp` and `cpio` command?\n6. Write two commands to take the backup of your home-folder and all sub-folders. The destination folder should be `/home/bkup`. (NOTE: size of backup should be smaller than original folder).\n7. What is the difference between the permissions `777` and `775` of the `chmod` command?\n",
        "quizzes": [
            {
                "question": "What is the numeric octal representation of the permission string '-rwxr-xr--'?",
                "options": [
                    "754",
                    "764",
                    "755",
                    "644"
                ],
                "correctAnswer": "754",
                "explanation": "Owner 'rwx' = 4+2+1=7; Group 'r-x' = 4+0+1=5; Other 'r--' = 4+0+0=4. Hence the octal code is 754."
            },
            {
                "question": "Why is the 'mv' command generally much faster and more efficient than 'cp' when moving files on the same filesystem?",
                "options": [
                    "mv merely updates file system directory entries without duplicating physical data blocks on disk.",
                    "mv compresses the file before relocating it to the destination directory.",
                    "mv executes asynchronously in kernel background memory without filesystem verification.",
                    "cp requires elevated root privileges for every single file operation."
                ],
                "correctAnswer": "mv merely updates file system directory entries without duplicating physical data blocks on disk.",
                "explanation": "On the same filesystem, 'mv' simply updates inode directory pointers rather than copying raw byte blocks across disk sectors, making it virtually instantaneous."
            },
            {
                "question": "What sequence of standard commands is used to build and install software from an uncompressed source tarball in Linux?",
                "options": [
                    "./configure followed by make and make install",
                    "rpm -ivh followed by make",
                    "tar -cvf followed by ./configure",
                    "make clean followed by rpm -U"
                ],
                "correctAnswer": "./configure followed by make and make install",
                "explanation": "The standard GNU build process requires running './configure' to detect system dependencies and create a Makefile, 'make' to compile, and 'make install' (as root) to copy binaries to destination directories."
            },
            {
                "question": "What is the key difference between permissions 777 and 775 when set using chmod?",
                "options": [
                    "In 775, Others (world) are denied write permissions (r-x = 5), whereas 777 allows full write permissions to everyone (rwx = 7).",
                    "In 775, the group owner cannot execute the file.",
                    "In 777, only the root user can edit the file.",
                    "In 775, the file owner loses read permissions."
                ],
                "correctAnswer": "In 775, Others (world) are denied write permissions (r-x = 5), whereas 777 allows full write permissions to everyone (rwx = 7).",
                "explanation": "777 grants 'rwx' (7) to User, Group, and Others. 775 grants 'rwx' (7) to User and Group, but restricts Others to 'r-x' (5, read and execute without write access)."
            }
        ],
        "flashcards": [
            {
                "question": "What does the device file '/dev/null' represent in Linux?",
                "answer": "The 'bit bucket' or null device. Any data redirected or written to /dev/null is immediately discarded and vanishes without consuming storage."
            },
            {
                "question": "What character sequence signals End of File (EOF) when entering text using the 'cat' command?",
                "answer": "Ctrl+D (^D) typed at the beginning of a blank line."
            },
            {
                "question": "What is the difference between '>' and '>>' redirection operators?",
                "answer": "'>' overwrites or creates a new file with the command output, while '>>' appends the output to the end of the file without overwriting existing contents."
            },
            {
                "question": "What flag in the tar command integrates gzip compression directly?",
                "answer": "The 'z' flag (e.g., tar -xzvf archive.tar.gz or tar -czvf archive.tar.gz)."
            }
        ]
    },
    {
        "order": 3,
        "title": "Lab 3: Practice Fundamentals of Shell Programming",
        "codeSnippet": "#!/bin/bash\n# Shell programming fundamentals\necho \"Program name: $0\"\necho \"Total arguments passed: $#\"\necho \"Arguments in reverse: $2 $1\"\necho \"All arguments: $*\"\necho \"Exit status: $?",
        "content": "# Lab#03\n\n## PRACTICE FUNDAMENTALS OF SHELL PROGRAMMING.\n\n### Objectives\n* Familiarization with the fundamentals of shell programming\n\n### Theory Overview\nWhen a user enters commands from the command line, he is entering them one at a time and getting a response from the system. From time to time it is required to execute more than one command, one after the other, and get the final result. This can be done with a shell program or a shell script. A shell program is a series of Linux commands and utilities that have been put into a file by using a text editor. When a shell program is executed the commands are interpreted and executed by Linux one after the other.\n\nA shell program is like any other programming language and it has its own syntax. It allows the user to define variables, assign various values, and so on.\n\n#### Creating and Executing a Shell Program\nAt the simplest level, shell programs are just files that contain one or more shell or Linux commands. These programs can be used to simplify repetitive tasks, to replace two or more commands that are always executed together with a single command, to automate the installation of other programs, and to write simple interactive applications.\n\nFor example, assume you have a CD-ROM drive mounted on your Linux system. When changing the CD, you must force Linux to read the new directory contents:\n```bash\numount /dev/cdrom\nmount -t iso9660 /dev/cdrom /cdrom\n```\nInstead of typing both commands every time, you can put both into a text file called `remount`.\n\n#### Execution Methods:\n1. **Making the file executable:**\n```bash\n$ chmod +x remount\n$ ./remount\n```\n*(Note: The shell program must be in a directory within your search path, or you must specify its relative/absolute path).*\n\n2. **Passing the script to the shell interpreter:**\n```bash\n$ bash remount\n$ tcsh remount\n```\n\n3. **Sourcing the script:**\nUsing the `.` command (in pdksh and bash) or `source` (in tcsh):\n```bash\n$ . remount\n$ source remount\n```\nThis tells the active shell to execute commands directly within the current shell environment without spawning a subshell.\n\n#### Command Aliases\nCommand aliases are shorthand abbreviations defined by the user to save keystrokes:\n```bash\nalias goconfig='cd /usr/X11R6/lib/X11/configs'\n```\nTo remove an alias:\n```bash\nunalias goconfig\n```\n*(Note: No spaces are allowed on either side of the `=` sign).*\nEntering `alias` without arguments displays all currently defined aliases.\n\n#### The Bang Line\nThe bang line tells the kernel which shell or language interpreter must be used to interpret the script. It appears on the first line:\n```bash\n#!/bin/bash\n```\nInstructions following this line are parsed using the Bourne-Again Shell (`bash`).\n\n#### Using Variables\nVariables belong to three major classifications:\n1. **Environment variables:** Part of the system environment (e.g. `PATH`, `SHELL`, `PWD`, `LOGNAME`).\n2. **Built-in variables:** Provided automatically by the shell (read-only).\n3. **User variables:** Defined and manipulated by the programmer.\n\nShell programming is a **non-typed, interpretive language**. Variables do not require data type declarations; the same variable can hold integers or character strings.\n\n#### Assigning and Accessing Variables:\n```bash\ncount=5               # bash/pdksh (NO spaces around =)\nset count = 5         # tcsh\n\nname=Garry\necho $count           # Precede with $ to access stored value\necho count            # Omission of $ displays literal text 'count'\n```\n\n#### Positional Parameters\nPositional parameters store command-line arguments passed to the script:\n* `$1`: First parameter\n* `$2`: Second parameter\n* `$3` ... `$9`: Subsequent parameters\n\nExample reverse script (`reverse`):\n```bash\n#!/bin/bash\n# program reverse: prints command line parameters in reverse order\necho \"$2\" \"$1\"\n```\nExecution:\n```bash\n$ ./reverse hello there\nthere hello\n```\n\n#### Built-in Shell Variables:\n| Variable | Description |\n| :--- | :--- |\n| `$#` | Stores the number of command-line arguments passed to the script. |\n| `$?` | Stores the exit status (return code) of the last executed command. |\n| `$0` | Stores the name of the shell program as invoked. |\n| `$*` | Stores all arguments entered on the command line as a single string (`$1 $2 ...`). |\n| `\"$@\"` | Stores all arguments entered on the command line individually quoted (`\"$1\"` `\"$2\"` ...). |\n\n#### Importance of Quotation Marks:\n* **Double quotes (`\"\"`):** Hides whitespace characters from the shell, while allowing variable expansion (`$VAR`) and command substitution:\n```bash\ngreeting=\"hello there $LOGNAME\"\n```\n* **Single quotes (`''`):** The strongest quoting mechanism. Hides ALL special characters (including `$`, `\\`, and spaces). Suppresses variable substitution entirely:\n```bash\ngreeting='hello there $LOGNAME'    # Prints literal $LOGNAME\n```\n* **Backslash (`\\`):** Hides a single special character:\n```bash\ndisk_price=\\$5.00\n```\n*(Without `\\`, the shell attempts to substitute `$5`, yielding `.00`).*\n* **Backticks (`` `command` ``):** Command substitution. Executes the enclosed command and replaces it with the output:\n```bash\ncontents=`ls`\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Write a shell program that takes one parameter (your name) and displays it on the screen.\n2. Write a shell program that takes a number of parameters equal to the last digit of your roll number and displays the values of the built-in variables such as `$#`, `$0`, and `$*` on the screen.\n3. Write a script that displays the values of the following environment variables:\n   * i) `SHELL`\n   * ii) `PWD`\n",
        "quizzes": [
            {
                "question": "What is the function of the 'shebang' or bang line (#!/bin/bash) placed at the beginning of a script?",
                "options": [
                    "It instructs the Linux kernel which interpreter binary must be invoked to parse and execute the script.",
                    "It gives the script permanent administrative root permissions automatically.",
                    "It compiles the shell script directly into native x86 machine binary before execution.",
                    "It acts as a standard comment line that is completely ignored by the kernel loader."
                ],
                "correctAnswer": "It instructs the Linux kernel which interpreter binary must be invoked to parse and execute the script.",
                "explanation": "The shebang sequence (#! followed by the path to an interpreter) informs the operating system kernel loader which executable binary should be used to interpret the script contents."
            },
            {
                "question": "In bash shell scripting, which built-in variable stores the total count of arguments passed on the command line?",
                "options": [
                    "$#",
                    "$*",
                    "$?",
                    "$0"
                ],
                "correctAnswer": "$#",
                "explanation": "'$#' evaluates to the number of positional parameters passed to the script. '$?' stores exit status, '$0' stores script name, and '$*' stores all arguments."
            },
            {
                "question": "How do single quotes ('') differ from double quotes (\"\") in shell variable assignment?",
                "options": [
                    "Single quotes treat all enclosed characters literally and suppress variable expansion ($VAR), while double quotes permit variable substitution.",
                    "Single quotes allow variable substitution, while double quotes treat all characters literally.",
                    "Single quotes are reserved exclusively for integer variables in bash.",
                    "Double quotes cause syntax errors when enclosing spaces."
                ],
                "correctAnswer": "Single quotes treat all enclosed characters literally and suppress variable expansion ($VAR), while double quotes permit variable substitution.",
                "explanation": "Single quotes provide strong quoting, suppressing all special character interpretation including variable evaluation ($). Double quotes preserve variable expansion and command substitution."
            },
            {
                "question": "What happens in bash if spaces are placed around the assignment operator, such as 'count = 5'?",
                "options": [
                    "The shell interprets 'count' as a command name and '=' as an argument, producing a 'command not found' error.",
                    "The shell automatically ignores the spaces and assigns 5 to count.",
                    "The shell converts the variable count into a system environment variable.",
                    "The shell allocates count as an array data structure."
                ],
                "correctAnswer": "The shell interprets 'count' as a command name and '=' as an argument, producing a 'command not found' error.",
                "explanation": "In bash variable assignment, no spaces are allowed around '='. With spaces, bash parses 'count' as an executable command name."
            }
        ],
        "flashcards": [
            {
                "question": "What does the built-in variable '$?' represent in Linux shell scripting?",
                "answer": "It stores the exit status (return code) of the most recently executed command. A value of 0 indicates success, while non-zero values indicate errors."
            },
            {
                "question": "What does '$0' store in a running shell script?",
                "answer": "The name of the script or program as it was invoked on the command line."
            },
            {
                "question": "What is the difference between '$*' and '\"$@\"'?",
                "answer": "'$*' expands all arguments into a single concatenated string, whereas '\"$@\"' expands arguments into separate individually quoted strings (\"$1\" \"$2\" ...)."
            },
            {
                "question": "How does command substitution using backticks (`` `cmd` ``) or $(cmd) work?",
                "answer": "It executes the enclosed command and replaces the backtick expression with the standard output produced by that command."
            }
        ]
    },
    {
        "order": 4,
        "title": "Lab 4: Practice Conditional Statements, Iteration & User Defined Functions in Shell Scripting",
        "codeSnippet": "#!/bin/bash\n# Conditional statement and loop example\nif [ -f \"sample.txt\" ]; then\n    echo \"sample.txt exists!\"\nelse\n    echo \"Creating sample.txt...\"\n    touch sample.txt\nfi\n\nfor file in *.txt; do\n    echo \"Processing $file\"\ndone",
        "content": "# Lab#04\n\n## PRACTICE CONDITIONAL STATEMENTS, ITERATION STATEMENTS AND FUNCTIONS IN SHELL SCRIPTING\n\n### Objective\n* Conditional statements, iteration statements and functions in Shell Scripting\n\n### Theory Overview\nIn bash and pdksh, a command called `test` is used to evaluate conditional expressions. You would typically use the `test` command to evaluate a condition that is used in a conditional statement or to evaluate the entrance or exit criteria for an iteration statement.\n\n**Syntax:**\n```bash\ntest expression\n# or\n[ expression ]\n```\n*(Note: Spaces are mandatory inside `[` and `]`).*\n\nSeveral built-in operators can be classified into four groups:\n\n#### 1. Integer Operators\n| Operator | Meaning |\n| :--- | :--- |\n| `int1 -eq int2` | Returns True if int1 is equal to int2. |\n| `int1 -ge int2` | Returns True if int1 is greater than or equal to int2. |\n| `int1 -gt int2` | Returns True if int1 is greater than int2. |\n| `int1 -le int2` | Returns True if int1 is less than or equal to int2. |\n| `int1 -lt int2` | Returns True if int1 is less than int2. |\n| `int1 -ne int2` | Returns True if int1 is not equal to int2. |\n\n#### 2. String Operators\n| Operator | Meaning |\n| :--- | :--- |\n| `str1 = str2` | Returns True if str1 is identical to str2. |\n| `str1 != str2` | Returns True if str1 is not identical to str2. |\n| `str` | Returns True if str is not null. |\n| `-n str` | Returns True if the length of str is greater than zero. |\n| `-z str` | Returns True if the length of str is equal to zero. |\n\n#### 3. File Operators\n| Operator | Meaning |\n| :--- | :--- |\n| `-d filename` | Returns True if filename is a directory. |\n| `-f filename` | Returns True if filename is an ordinary regular file. |\n| `-r filename` | Returns True if filename can be read by the process. |\n| `-s filename` | Returns True if filename has a nonzero length. |\n| `-w filename` | Returns True if filename can be written by the process. |\n| `-x filename` | Returns True if filename is executable. |\n\n#### 4. Logical Operators\n| Operator | Meaning |\n| :--- | :--- |\n| `! expr` | Logical NOT. Returns True if expr is false. |\n| `expr1 -a expr2` | Logical AND. Returns True if expr1 AND expr2 are true. |\n| `expr1 -o expr2` | Logical OR. Returns True if expr1 OR expr2 is true. |\n\n---\n\n### CONDITIONAL STATEMENTS\nBoth `if` and `case` constructs are supported.\n\n#### The `if` Statement\n```bash\nif [ expression ]\nthen\n    commands\nelif [ expression2 ]\nthen\n    commands\nelse\n    commands\nfi\n```\nThe closing keyword is `fi` (reverse of `if`).\n\nExample:\n```bash\nif [ -f \"sar.txt\" ]\nthen\n    echo \"There is a .txt file in the current directory.\"\nelse\n    echo \"Could not find the .txt file.\"\nfi\n```\n\n#### The `case` Statement\nThe `case` statement compares a string against patterns including wildcard characters:\n```bash\ncase string1 in\n    str1)\n        commands;;\n    str2)\n        commands;;\n    *)\n        commands;;\nesac\n```\nEach pattern branch terminates with `;;` and the statement closes with `esac`.\n\nExample parsing command-line options:\n```bash\ncase $1 in\n    -i)\n        count=`grep ^i $2 | wc -l`\n        echo \"Lines starting with i in $2: $count\"\n        ;;\n    -e)\n        count=`grep ^e $2 | wc -l`\n        echo \"Lines starting with e in $2: $count\"\n        ;;\n    *)\n        echo \"That option is not recognized\"\n        ;;\nesac\n```\n\n---\n\n### ITERATION STATEMENTS\n\n#### 1. The `for` Statement\n**Form 1 (Iterating over a list):**\n```bash\nfor var1 in list\ndo\n    commands\ndone\n```\n\n**Form 2 (Iterating over positional parameters `\"$@\"`):**\n```bash\nfor file\ndo\n    tr a-z A-Z < $file > $file.caps\ndone\n```\n\n#### 2. The `while` Statement\nExecutes code block repeatedly while expression evaluates to true:\n```bash\nwhile [ expression ]\ndo\n    statements\ndone\n```\n\n#### 3. The `until` Statement\nExecutes code block repeatedly while expression evaluates to false:\n```bash\nuntil [ expression ]\ndo\n    commands\ndone\n```\n\n#### 4. The `shift` Command\nShifts all positional parameters leftward. `$1` takes the value of `$2`, `$2` takes `$3`, etc.\n`shift 2` moves parameters two positions over. Very useful for parsing command-line flags.\n\nExample option parser:\n```bash\nwhile [ \"$1\" ]\ndo\n    if [ \"$1\" = \"-i\" ]; then\n        infile=\"$2\"\n        shift 2\n    elif [ \"$1\" = \"-o\" ]; then\n        outfile=\"$2\"\n        shift 2\n    else\n        echo \"Program $0 does not recognize option $1\"\n        break\n    fi\ndone\n```\n\n#### 5. Additional Control Statements\n* `break`: Exits a loop immediately.\n* `exit [n]`: Exits script returning numeric status code `n`.\n* `read var`: Reads user input from standard input.\n* `select` (pdksh): Generates interactive numbered menus.\n\n---\n\n### USER DEFINED FUNCTIONS\nFunctions group common routines together for modularity:\n```bash\nfname () {\n    shell commands\n}\n```\nParameters passed to functions are accessed inside as `$1`, `$2`, `$@`.\n\n**Comprehensive Modular Script Example:**\n```bash\nupper () {\n    shift\n    for i in \"$@\"\n    do\n        tr a-z A-Z < \"$1\" > \"$1.out\"\n        mv \"$1.out\" \"$1\"\n        shift\n    done\n}\n\nlower () {\n    shift\n    for i in \"$@\"\n    do\n        tr A-Z a-z < \"$1\" > \"$1.out\"\n        mv \"$1.out\" \"$1\"\n        shift\n    done\n}\n\nprint () {\n    shift\n    for i in \"$@\"\n    do\n        lpr \"$1\"\n        shift\n    done\n}\n\nusage_error () {\n    echo \"$1 syntax is $1 <option> <input files>\"\n    echo \"Options: -p (print), -u (uppercase), -l (lowercase)\"\n}\n\ncase $1 in\n    p | -p) print \"$@\";;\n    u | -u) upper \"$@\";;\n    l | -l) lower \"$@\";;\n    *) usage_error \"$0\";;\nesac\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. What `test` command should be used to test that `/usr/bin` is a directory or a symbolic link?\n2. Write a script that takes two strings as input, compares them and depending upon the results of the comparison prints the results.\n3. Write a script that takes a number (parameter) from 1-3 as input and uses `case` to display the name of the corresponding month.\n4. Write a script that creates a backup version of each file in your home directory to a subdirectory called `backup` using `for` statement. If the operation fails an error message is to be displayed.\n5. Write a script that calculates the average of all even numbers less than or equal to your roll number and prints the result.\n6. Write a function that displays the name of the week days starting from Sunday if the user passes a day number. If a number provided is not between 1 and 7 an error message is displayed.\n7. Write scripts that display the parameters passed along with the parameter number using `while` and `until` statements.\n8. Write a script that displays the following menu:\n   * Quotient\n   * Remainder\n   Depending on user's choice, the result of division must be displayed and the loop breaks. The two numbers (dividend and divisor) must be supplied at runtime as command line arguments. If user chooses an item not in the list, prompt user to make proper choice and restart the loop.\n",
        "quizzes": [
            {
                "question": "Which test operator checks whether a given file path is an ordinary regular file (and not a directory or device)?",
                "options": [
                    "-f",
                    "-d",
                    "-r",
                    "-s"
                ],
                "correctAnswer": "-f",
                "explanation": "The '-f' operator returns true if the specified file exists and is a regular file. '-d' tests for directories, and '-s' checks if file size is non-zero."
            },
            {
                "question": "What is the primary operational difference between a 'while' loop and an 'until' loop in shell scripting?",
                "options": [
                    "A while loop executes as long as the test condition is true, whereas an until loop executes as long as the test condition is false.",
                    "A while loop executes only once, while an until loop executes infinitely.",
                    "An until loop requires C-style syntax with curly braces.",
                    "A while loop can only test integer expressions."
                ],
                "correctAnswer": "A while loop executes as long as the test condition is true, whereas an until loop executes as long as the test condition is false.",
                "explanation": "'while' continues execution while its condition evaluates to 0 (True), whereas 'until' continues looping while its condition evaluates to non-zero (False), stopping once the condition becomes True."
            },
            {
                "question": "What does the 'shift' command do to positional parameters in shell scripting?",
                "options": [
                    "It shifts all positional parameters leftward by one position, discarding $1 and making $2 the new $1.",
                    "It shifts the execution priority of the script from foreground to background.",
                    "It multiplies all integer parameters by 2.",
                    "It swaps the values of $1 and $2."
                ],
                "correctAnswer": "It shifts all positional parameters leftward by one position, discarding $1 and making $2 the new $1.",
                "explanation": "'shift' moves positional parameters left by one ($1=$2, $2=$3, etc.), decrementing '$#'. 'shift n' moves parameters left by n positions."
            },
            {
                "question": "In a bash case statement, how must each matching pattern block be terminated?",
                "options": [
                    ";;",
                    "break",
                    "done",
                    "esac"
                ],
                "correctAnswer": ";;",
                "explanation": "In bash, each pattern command block within a case statement must terminate with double semicolons (;;), and the entire construct terminates with 'esac'."
            }
        ],
        "flashcards": [
            {
                "question": "What integer comparison operator in bash tests if int1 is not equal to int2?",
                "answer": "-ne (e.g., [ \"$a\" -ne \"$b\" ])."
            },
            {
                "question": "What string test operator returns true if a string is empty (length zero)?",
                "answer": "-z (e.g., [ -z \"$str\" ] returns true if string length is 0)."
            },
            {
                "question": "How do keywords 'fi' and 'esac' relate to their opening statements?",
                "answer": "They are the reverse spellings of 'if' and 'case', used in Bourne-compatible shells to mark the closing boundary of their respective blocks."
            },
            {
                "question": "How are arguments accessed inside a user-defined shell function?",
                "answer": "They are accessed as positional parameters ($1, $2, $3, $@) localized to that function call."
            }
        ]
    },
    {
        "order": 5,
        "title": "Lab 5: Practice Perl Scripting",
        "codeSnippet": "#!/usr/bin/perl\n# Perl scripting: scalars, arrays, and hashes\nmy $scaler = \"OS Lab 5\";\nmy @arr = (10, 20, 30);\nmy %hash = (\"Linux\" => \"Red Hat\", \"Shell\" => \"Bash\");\n\nprint \"$scaler\\n\";\nprint \"Array element: $arr[0]\\n\";\nprint \"Hash value: $hash{'Linux'}\\n\";",
        "content": "# Lab#05\n\n## PRACTICE PERL SCRIPTING.\n\n### Objective\n* Perl Scripting\n\n### Theory Overview\nPerl (Practical Extraction and Report Language) is a powerful scripting tool used to manage files, create reports, edit text and perform many other tasks when using Red Hat Linux. Perl is included with Red Hat Linux. It contains the best features of C, BASIC and a variety of other programming languages, with a hearty dollop of awk, sed, and shell scripting thrown in. It was developed in the mid 1980s by Larry Wall to overcome file handling limitations of the awk command. Although originally designed as a data extraction and report generation language, Perl appeals to many Unix and Linux system administrators because it can be used to create new software tools that fill a gap between the capabilities of shell scripts and compiled C programs. Another advantage of Perl over other Unix tools is that it can process and extract data from binary files (those without line terminators or that contain binary data, such as some databases and compiled programs), whereas sed and awk can't.\n\nPerl interprets its language in text files known as Perl programs. Although some consider Perl an interpreter, the programs are actually compiled in memory and then run by Perl's internal interpreter.\n\n#### A Simple Perl Program\nThe following is a simple Perl program that prints a short message:\n```perl\n#!/usr/bin/perl\nprint \"first Perl program \\n\";\n```\nThat's the entire program. Type that in and save it to a file called `perlprog.pl`. Then make the file executable using the `chmod` command and run it at the command prompt:\n```bash\n$ chmod +x perlprog.pl\n$ ./perlprog.pl\n```\nOr you can use Perl to run the script like this:\n```bash\n# perl perlprog.pl\n```\n\n#### Comments\nThe `#` character indicates that the rest of the screen line is a comment. The interpreter ignores the comment line. Using a comment character is standard practice in shell programming.\n\n---\n\n### Perl Variable Types\nThere are three variable types in Perl: **scalars**, **arrays**, and **hashes**.\n\n#### 1. Scalars (`$`)\nScalar variable types are indicated with a `$` character. Scalars can be numerical or strings, and they can change types from one to the other as needed:\n```perl\n#!/usr/bin/perl\n$scalvar=\"George12\";\nprint \" $scalvar \\n \";\n$scalvar++;\nprint \" $scalvar \\n \";\n```\n\n#### 2. Arrays (`@`)\nPerl arrays are indicated with an `@` character. Each element in the array is a scalar value. Because scalar values are indicated with a `$` character, each individual element in an array is also indicated with a `$` character:\n```perl\n#!/usr/bin/perl\n@arr1=( 1, 2, 3 );\nprint \" @arr1 \";\nprint \" $arr1[1] \";\n```\n\n#### 3. Hashes (`%`)\nHashes are indicated with a `%` character. A hash, which used to go by the name associative array, is a list of name and value pairs. Individual elements in the hash are referenced by name, rather than by index (unlike an array). Again because the values are scalars, the `$` character is used to reference individual elements:\n```perl\n#!/usr/bin/perl\nforeach $key (keys %ENV) {\n    print \" $key = $ENV{$key}\\n\";\n}\n```\n\n---\n\n### Operators\nPerl supports a number of operators to perform various operations.\n\n#### Comparison Operators\nThe numeric comparison operators used by Perl are similar to those used in C (`==`, `!=`, `<`, `>`, `<=`, `>=`).\nThe string comparison operators are shown below:\n| Operator | Meaning | Operator | Meaning |\n| :--- | :--- | :--- | :--- |\n| `eq` | is equal to | `ne` | not equal to |\n| `lt` | less than | `cmp` | return -1 if less than, 0 if equal, 1 if greater |\n| `gt` | greater than | `=~` | matched by regular expression |\n| `le` | less than or equal to | `!~` | not matched by regular expression |\n| `ge` | greater than or equal to | | |\n\n#### Compound Operators\nPerl uses compound operators similar to C:\n* `&&`: Logical AND\n* `||`: Logical OR\n* `!`: Logical NOT\n* `()`: Parentheses (used to group compound statements)\n\n#### Arithmetic Operators\nPerl supports a wide variety of math operations:\n* `x**y`: raises x to the y power\n* `-y`: negates y\n* `++y`: prefix increment\n\n---\n\n### Conditional Statements\nPerl uses two conditional statements, `if` and `unless`, which function opposite one another.\n\n#### The `if` Statement\n```perl\n#!/usr/bin/perl\n$name=\"master\";\nif ($name eq \"master\") {\n    print \" \\n Hello master \\n\";\n}\nelsif ($name eq \"teacher\") {\n    print \"\\n Hello teacher \\n \";\n}\nelse {\n    print \"\\n who are you \\n\";\n}\nprint \"\\n this line will be printed at any cost \\n \";\n```\n\n#### The `unless` Statement\n`unless` performs a statement or block if a condition is false:\n```perl\nunless ($name eq \"Rich\") {\n    print \"Go away, you're not allowed in here! \\n\";\n}\n```\n\n---\n\n### Looping Constructs\nPerl has four looping constructs: `for`, `foreach`, `while`, and `until`.\n\n#### 1. `for`\nThe `for` construct performs a statement block for a set of conditions:\n```perl\nfor ($i=1; $i<=10; $i++) {\n    print \"$i \\n\";\n}\n```\n\n#### 2. `foreach`\nThe `foreach` construct performs a statement block for each element in a list or array:\n```perl\n#!/usr/bin/perl\n@arr1=`ls`;\nforeach $name (@arr1) {\n    print \"$name\";\n}\n```\n\n#### 3. `while`\n`while` performs a statement block as long as a condition is true:\n```perl\nwhile ($x<10) {\n    print \"$x \\n\";\n    $x++;\n}\n```\n\n#### 4. `until`\n`until` performs a statement block as long as a condition is false:\n```perl\n#!/usr/bin/perl\n$var=1;\nuntil ($var gt 5) {\n    print \" $var \\n \";\n    $var++;\n}\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Write a program in Perl that takes input from user through command line in an array and then displays it.\n2. Write a program using Perl that takes two nos. as input `num1` and `num2`, checks which one is greater and displays that number.\n3. Write a program that generates the table of last digit of your roll number. Perform this task using Perl and C both.\n",
        "quizzes": [
            {
                "question": "Which sigil (prefix character) is used in Perl to denote a hash (associative array)?",
                "options": [
                    "%",
                    "$",
                    "@",
                    "&"
                ],
                "correctAnswer": "%",
                "explanation": "In Perl, scalars use '$', indexed arrays use '@', hashes (associative key-value pairs) use '%', and subroutines use '&'."
            },
            {
                "question": "How does the 'unless' statement in Perl behave in comparison to the 'if' statement?",
                "options": [
                    "It executes its code block only when the condition evaluates to false.",
                    "It executes its code block indefinitely in an infinite loop.",
                    "It automatically catches exceptions thrown by the kernel.",
                    "It behaves identically to an 'if' statement with inverted data types."
                ],
                "correctAnswer": "It executes its code block only when the condition evaluates to false.",
                "explanation": "'unless (condition)' is syntactic sugar for 'if (!condition)', executing the body only when the tested expression is false."
            },
            {
                "question": "What string comparison operator in Perl tests whether string A is strictly equal to string B?",
                "options": [
                    "eq",
                    "==",
                    "===",
                    "=~"
                ],
                "correctAnswer": "eq",
                "explanation": "Perl differentiates between numeric and string equality. '==' compares numbers, whereas 'eq' compares strings lexically."
            },
            {
                "question": "Why did Perl gain widespread popularity among Unix/Linux system administrators compared to awk and sed?",
                "options": [
                    "Perl can process binary files directly and bridges the functionality gap between shell scripts and compiled C programs.",
                    "Perl does not require an operating system kernel to execute.",
                    "Perl scripts execute directly in hardware microcode.",
                    "Perl replaced the C compiler for building Linux kernels."
                ],
                "correctAnswer": "Perl can process binary files directly and bridges the functionality gap between shell scripts and compiled C programs.",
                "explanation": "Larry Wall designed Perl to eliminate awk/sed limitations, offering powerful regular expressions, data structures, and binary file handling without needing full C compilation."
            }
        ],
        "flashcards": [
            {
                "question": "What is a Hash in Perl?",
                "answer": "An associative array (%hash) storing key-value pairs where individual elements are looked up by name/key ($hash{$key}) rather than by numeric index."
            },
            {
                "question": "What does the Perl operator 'cmp' return?",
                "answer": "It compares two strings alphabetically: returns -1 if left < right, 0 if equal, and 1 if left > right."
            },
            {
                "question": "How are individual elements of an array '@arr' accessed in Perl?",
                "answer": "Using the scalar sigil '$' followed by array name and index in square brackets, e.g., $arr[0]."
            },
            {
                "question": "How does Perl execute program source files?",
                "answer": "Perl compiles scripts in memory into an internal bytecode tree and immediately runs them via its high-speed internal runtime engine."
            }
        ]
    },
    {
        "order": 6,
        "title": "Lab 6: Demonstrate Process Management in Linux",
        "codeSnippet": "# Process management, monitoring, and job control\nps -u\ntop\nnice -n 10 my_job &\njobs\nkill -15 1234\nkill -9 1234\ncrontab -l",
        "content": "# Lab#06\n\n## DEMONSTRATE PROCESS MANAGEMENT IN LINUX.\n\n### Objective\n* Managing processes on the Linux system\n\n### Theory Overview\nEverything that runs on a Linux system is a process—every user task, every system daemon—everything is a process. Knowing how to manage the processes running on your Linux system is an important (indeed even critical) aspect of system administration. This lab looks at processes in some detail. The following topics are introduced:\n* How to find out what processes are running\n* Determine when a process is hogging the system\n* How to find out which processes are locked up\n* How to terminate a process\n* How to properly manage processes\n\nIn the course of discussing processes, we look at the main aspects of process control that you need in order to keep your system running smoothly.\nYou may come across the terms **process** and **job** used when dealing with multitasking operating systems. For most purposes, both terms are correct. However, a job is usually a process started by a shell (and may involve many processes), while a process is a single entity that is executing.\n\n#### Processes\nA formal definition of a process is that it is a **single program running in its own virtual address space**. This means that everything running under Linux is a process. This is compared to a job, which may involve several commands executing in series. Alternatively, a single command line issued at the shell prompt may involve more than one process, especially when pipes or redirection are involved. For example, the command:\n```bash\nnroff -man ps.1 | grep kill | more\n```\nwill start three processes, one for each command.\n\n#### Types of Processes:\n1. **Interactive processes:** A process initiated from (and controlled by) a shell. Interactive processes may be in foreground or background.\n2. **Batch processes:** Processes that are not associated with a terminal but are submitted to a queue to be executed sequentially.\n3. **Daemon processes:** Processes usually initiated when Linux boots and that run in the background until required.\n\n---\n\n### USING THE ps COMMAND\nThe easiest method of finding out what processes are running on your system is to use the `ps` (process status) command.\nWhen logged in as a normal user:\n```bash\n$ ps\nPID TTY STAT TIME COMMAND\n 41 v01 S    0:00 -bash\n134 v01 R    0:00 ps\n```\n\n#### ps Command Output Columns:\n* **PID:** Process ID number. Every process has a unique integer identifier assigned sequentially at launch.\n* **TTY:** Terminal or virtual console window from which the process was started.\n* **STAT:** Current execution status:\n  * `S`: Sleeping (not currently active on CPU).\n  * `R`: Running (actively executing on CPU).\n* **TIME:** Total accumulated system CPU time consumed by the process.\n* **COMMAND:** Command line invoked to run the process. Child processes spawned show up here as well.\n\n#### Login Shells\nAs a general convention, a login shell has a hyphen placed before its name (such as `-bash`) to distinguish it from subshells spawned later (`pdksh`, `bash`).\n\n#### For the Superuser\nWhen the superuser (`root`) issues `ps`, all processes on the system are displayed:\n```bash\nps | more\nps > /tmp/ps_file\n```\n\n#### Format and Flags of the ps Command:\n* `a`: Shows processes owned by other users in addition to the current user's processes.\n* `f`: Displays processes in a process tree showing parent-child hierarchy.\n* `l`: Displays long format including `PPID`, `PRI`, and `NI`.\n* `m`: Displays memory report.\n* `r`: Displays only currently running processes.\n* `txx`: Displays processes controlled by tty `xx`.\n* `u`: Displays user format (includes `USER`, `%CPU`, `%MEM`, `START`).\n* `ef`: Displays all processes in standard system syntax.\n* `eo`: Process status in user-defined format.\n\n```bash\n$ ps -u\nUSER PID %CPU %MEM SIZE RSS TTY STAT START TIME COMMAND\nbill  41  0.1  6.8  364 472 v01 S    23:19 0:01 -bash\nbill 138  0.0  3.3   72 228 v01 R    23:34 0:00 ps -u\n```\nCombining options:\n```bash\n$ ps -au\n```\nDisplays all processes across all users with resource utilization columns.\n\n#### Identifying Parent Processes (PPID):\n```bash\n$ ps -l\nF UID PID PPID PRI NI SIZE RSS WCHAN STAT TTY TIME COMMAND\n0 501  41    1  15  0  364 472 114d9c    S v01 0:00 -bash\n0 501 121   41  29  0   64 208      0    R v01 0:00 ps -l\n```\nThe `PPID` (Parent Process ID) column reveals which process spawned that particular process. The login Bourne shell has PPID 1 (`init`), which is the ancestor of all user processes.\n\n---\n\n### The top Command\nThe `top` command provides a real-time, text-based interactive display constantly updating the most CPU- and memory-intensive processes.\n\n---\n\n### PROCESS PRIORITIES\nLinux provides two commands to alter scheduling priority:\n* `nice`: Launches a program with modified scheduling priority:\n```bash\n$ nice -n 12 xosview &\n```\nPriority values range from **-20 (highest priority)** to **19 (lowest priority)**.\n* `renice`: Resets priority of an already running process. Regular users can only increase their nice value (making tasks lower priority), whereas `root` can assign any priority in the range -20 to 19.\n\n---\n\n### gnome-system-monitor\nA graphical utility providing process listing and resource control, analogous to the Windows Task Manager.\n\n---\n\n### USING kill\nTerminates hung or run-away processes:\n```bash\n$ kill <PID>\n```\nIf a process does not terminate gracefully, force termination using signal 9:\n```bash\n$ kill -9 <PID>\n```\n* **Killing Child Processes:** When killing a parent, check if children become dormant or respawn. Terminate using the parent PID (`PPID`).\n* **Killing Rights:** Regular users can only kill their own processes. Attempting to kill another user's process results in `kill: - Not owner`. Superuser `root` can terminate any process.\n\n---\n\n### SERVICES\nServices can be managed in Red Hat Linux:\n1. `service <service_name> <start/stop/restart>`\n2. Giving direct script path: `/etc/rc.d/network restart`\n\n---\n\n### JOBS AND SCHEDULING\n* **`at`:** Schedules a command to run once at a specified future time:\n```bash\nat 17:00\n```\n* **`cron`:** Recurring periodic job scheduler using `/etc/crontab`:\n```text\n05 * * * * /myscript.d\n```\n*(Runs `/myscript.d` at 5 minutes past every hour, every day, every month).*\nEditing user crontab:\n```bash\n$ crontab -e\n0 0 5 * * 6 /root/crontest.sh     # Runs at 05:00 every Saturday\n```\n* `crontab -l`: Lists installed cron jobs.\n* `crontab -r`: Deletes installed crontab file.\n\n#### Job Control Commands:\n* `&`: Appended to a command to launch it in the background:\n```bash\n$ command &\n```\n* `jobs`: Lists active background and stopped jobs with job numbers.\n* `fg <job_number>`: Brings a background or stopped process to the foreground.\n* `bg <job_number>`: Resumes a stopped process in the background.\n* `<Ctrl>z`: Suspends (stops) current foreground process.\n\n#### Command History List:\n`bash` maintains command history:\n```bash\nhistory 5     # Displays last 5 commands\n```\n\n---\n\n### RUNLEVELS\nA runlevel is a system state defined in `/etc/inittab`:\n* `0`: Halt (shuts down system)\n* `1`: Single-user mode (administrative maintenance)\n* `2`: Multiuser mode without NFS\n* `3`: Full multiuser text mode\n* `4`: Unused\n* `5`: X11 graphical desktop mode (default Red Hat GUI)\n* `6`: Reboot\n\nChanging runlevels dynamically:\n```bash\n# telinit S     # Change to single-user mode\n# telinit 3     # Return to multi-user text mode\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Practice the following commands and explain their purpose:\n   * a. `kill`\n   * b. `ps`\n   * c. `killall`\n   * d. `renice`\n   * e. `init`\n2. What information is contained in `init.d` and `rc.d`?\n",
        "quizzes": [
            {
                "question": "What is Process ID 1 (PID 1) on a traditional Linux operating system?",
                "options": [
                    "The init process, which serves as the ancestor of all user and daemon processes.",
                    "The Linux kernel swap space daemon.",
                    "The primary root bash login shell.",
                    "The graphical X11 display server."
                ],
                "correctAnswer": "The init process, which serves as the ancestor of all user and daemon processes.",
                "explanation": "PID 1 is the 'init' system process spawned directly by the kernel at boot. It serves as the ultimate parent (ancestor) of all system daemons and user sessions."
            },
            {
                "question": "What nice value corresponds to the highest scheduling priority in Linux?",
                "options": [
                    "-20",
                    "19",
                    "0",
                    "100"
                ],
                "correctAnswer": "-20",
                "explanation": "Linux nice values range from -20 (highest priority/least nice) to 19 (lowest priority/most nice). Only root can assign negative nice values."
            },
            {
                "question": "What signal does 'kill -9 <PID>' send to a process?",
                "options": [
                    "SIGKILL, an uncatchable forceful termination signal handled directly by the kernel.",
                    "SIGTERM, requesting polite graceful termination.",
                    "SIGSTOP, pausing the process in background memory.",
                    "SIGHUP, reloading configuration files."
                ],
                "correctAnswer": "SIGKILL, an uncatchable forceful termination signal handled directly by the kernel.",
                "explanation": "Signal 9 is SIGKILL, which cannot be caught, blocked, or ignored by the process. The operating system kernel immediately reclaims all process resources."
            },
            {
                "question": "Which Linux runlevel boots the system into Full Multiuser Text mode without a GUI?",
                "options": [
                    "Runlevel 3",
                    "Runlevel 5",
                    "Runlevel 1",
                    "Runlevel 6"
                ],
                "correctAnswer": "Runlevel 3",
                "explanation": "Runlevel 3 corresponds to Full Multiuser Mode (console/text mode). Runlevel 5 is X11 Graphical Desktop mode, 1 is single-user, and 6 is reboot."
            }
        ],
        "flashcards": [
            {
                "question": "What does a STAT value of 'S' vs 'R' mean in ps command output?",
                "answer": "'S' means Sleeping (waiting for an event or I/O resource), while 'R' means Running (currently executing or runnable on the CPU)."
            },
            {
                "question": "How do you resume a stopped foreground process (Ctrl+Z) in the background?",
                "answer": "By executing 'bg' followed by its job number (e.g., bg %1)."
            },
            {
                "question": "What is the five-field syntax format of a standard Linux crontab entry?",
                "answer": "minute (0-59), hour (0-23), day of month (1-31), month (1-12), and day of week (0-6, where 0=Sunday), followed by the command path."
            },
            {
                "question": "Can an ordinary unprivileged user renice their own process to a negative nice value?",
                "answer": "No. Ordinary users can only increase their nice value (lowering priority). Only the superuser (root) can assign negative nice values (-20 to -1)."
            }
        ]
    },
    {
        "order": 7,
        "title": "Lab 7: Demonstrate Multithreading Using POSIX Thread Library (Open-Ended Lab)",
        "codeSnippet": "#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\nvoid *compute_avg(void *param);\n\nint main(int argc, char *argv[]) {\n    pthread_t tid;\n    pthread_attr_t attr;\n    pthread_attr_init(&attr);\n    pthread_create(&tid, &attr, compute_avg, NULL);\n    pthread_join(tid, NULL);\n    printf(\"Thread execution finished successfully.\\n\");\n    return 0;\n}",
        "content": "# Lab#07\n\n## DEMONSTRATE MULTITHREADING USING POSIX THREAD LIBRARY. + (OPEN ENDED LAB)\n\n### Objective\n* Familiarization with POSIX Thread Library\n\n### Theory Overview\nTechnically, a **thread** is defined as an independent stream of instructions that can be scheduled to run as such by the operating system.\nA thread is a semi-process that has its own stack, and executes a given piece of code. Unlike a real process, the thread normally shares its memory with other threads (whereas for processes we usually have a different memory area for each one of them).\n\nA **Thread Group** is a set of threads all executing inside the same process. They all share the same memory, and thus can access the same global variables, same heap memory, same set of file descriptors, etc. All these threads execute in parallel (i.e. using time slices, or if the system has several processors, then really in parallel).\n\nHistorically, hardware vendors have implemented their own proprietary versions of threads. These implementations differed substantially from each other, making it difficult for programmers to develop portable threaded applications.\nIn order to take full advantage of the capabilities provided by threads, a standardized programming interface was required. For UNIX systems, this interface has been specified by the **IEEE POSIX 1003.1c standard (1995)**. Implementations which adhere to this standard are referred to as **POSIX threads**, or **Pthreads**. Most hardware vendors now offer Pthreads in addition to their proprietary threads.\n\n#### Advantages of Threads over Processes (fork):\nCompared to the standard `fork()`, threads carry a lot less overhead:\n* `fork()` produces a second copy of the calling process. The parent and child are completely independent, each with its own address space, with its own copies of its variables.\n* Threads share a common address space:\n  1. **Less CPU Overhead:** The kernel does not need to make a new independent copy of the process memory space, file descriptors, etc. This saves a lot of CPU time, making thread creation **ten to a hundred times faster** than new process creation. Because of this, you can use a whole bunch of threads and not worry about CPU and memory overhead.\n  2. **Faster Termination:** It takes less time to terminate a thread than a process.\n  3. **Faster Context Switching:** Context switching between threads in the same process is much faster than context switching between separate processes.\n  4. **Direct Communication:** Communicating between threads of one process is simple because they share the address space. Data produced by one thread is immediately available to all other threads.\n\n*Trade-off:* Because threads in a group all use the same memory space, if one thread corrupts memory, other threads might suffer as well. With processes, the operating system protects address spaces from one another.\n\n---\n\n### THREAD CREATION AND TERMINATION\n\n#### Example 1: Creating and Joining Two Threads\n```c\n#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\nvoid *print_message_function( void *ptr );\n\nint main()\n{\n     pthread_t thread1, thread2;\n     char *message1 = \"Thread 1\";\n     char *message2 = \"Thread 2\";\n     int  iret1, iret2;\n\n    /* Create independent threads each of which will execute function */\n     iret1 = pthread_create( &thread1, NULL, print_message_function, (void*) message1);\n     iret2 = pthread_create( &thread2, NULL, print_message_function, (void*) message2);\n\n     /* Wait till threads are complete before main continues. Unless we  */\n     /* wait we run the risk of executing an exit which will terminate   */\n     /* the process and all threads before the threads have completed.   */\n     pthread_join( thread1, NULL);\n     pthread_join( thread2, NULL); \n\n     printf(\"Thread 1 returns: %d\\n\", iret1);\n     printf(\"Thread 2 returns: %d\\n\", iret2);\n     exit(0);\n}\n\nvoid *print_message_function( void *ptr )\n{\n     char *message;\n     message = (char *) ptr;\n     printf(\"%s \\n\", message);\n}\n```\n\n**Compilation:**\n```bash\ncc -lpthread pthread1.c\n# or C++:\ng++ -lpthread pthread1.c\n```\n**Run:**\n```bash\n$ ./a.out\nThread 1\nThread 2\nThread 1 returns: 0\nThread 2 returns: 0\n```\n\n---\n\n#### Example 2: Thread Array with Parameter Passing\n```c\n#include <pthread.h>\n#include <stdio.h>\n#include <stdlib.h>\n\n// Function executed by threads\nvoid *thread_function(void *arg) {\n    int *num = (int *)arg; // Casting argument to int pointer\n    printf(\"Thread %d is running. \\n\", *num);\n    pthread_exit(NULL); // Thread exit with no return value\n}\n\nint main() {\n    pthread_t threads[3]; // Array of thread IDs\n    int args[3] = {1, 2, 3}; // Arguments to pass to each thread\n\n    // Creating 3 threads\n    for (int i = 0; i < 3; i++) {\n        if (pthread_create(&threads[i], NULL, thread_function, (void *)&args[i]) != 0) {\n            printf(\"Error creating thread %d \\n\", i);\n            return 1;\n        }\n    }\n\n    // Waiting for each thread to finish\n    for (int i = 0; i < 3; i++) {\n        pthread_join(threads[i], NULL);\n    }\n\n    printf(\"All threads completed. \\n\");\n    return 0;\n}\n```\n\n**Explanation:**\n* **Thread Function (`thread_function`):** Executed by each thread. Receives argument (`arg`), casts it to an integer pointer, prints which thread is running, and terminates using `pthread_exit()`.\n* **Main Function:**\n  * Array `threads[3]` holds thread IDs.\n  * Array `args` stores values `(1, 2, 3)` passed to each thread.\n  * `pthread_create()` creates three threads inside a loop.\n  * `pthread_join()` waits for each thread to finish.\n  * Once all threads finish, prints `\"All threads completed.\"`\n\n---\n\n#### Example 3: Function Argument by Reference\n```c\n#include <stdio.h>\n#include <pthread.h>\n\n// Function to be executed by each thread\nvoid* threadFunction(void* arg) {\n    int *id = (int*) arg;\n    printf(\"Thread ID: %d \\n\", *id);\n    return NULL;\n}\n\nint main() {\n    pthread_t thread1, thread2; // Declare thread variables\n    int id1 = 1, id2 = 2; // Arguments for threads\n\n    // Create two threads\n    pthread_create(&thread1, NULL, threadFunction, &id1); // Thread 1\n    pthread_create(&thread2, NULL, threadFunction, &id2); // Thread 2\n\n    // Wait for threads to complete\n    pthread_join(thread1, NULL); // Join thread 1\n    pthread_join(thread2, NULL); // Join thread 2\n\n    printf(\"Threads completed. \\n\");\n    return 0;\n}\n```\n\n**Explanation:**\n* `pthread_create()` creates a new thread and executes the function `threadFunction`.\n* The thread ID is passed as a reference, and the thread function takes a `void*` argument to pass data.\n* `pthread_join()` ensures the main program waits for worker threads before exiting.\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Open Ended Lab:\nMake a multithreaded program that calculates various statistical values for a list of numbers. It creates three separate worker threads:\n1. One thread will determine the **average** of the numbers.\n2. The second will determine the **maximum** value.\n3. The third will determine the **minimum** value.\n\nFor example, suppose your program is passed the integers: `90 81 78 95 79 72 85`\nThe program will report:\n* The average value is 82\n* The minimum value is 72\n* The maximum value is 95\n",
        "quizzes": [
            {
                "question": "What is the primary difference in memory allocation between a thread created with pthread_create() and a child process created with fork()?",
                "options": [
                    "Threads share the same virtual address space, heap, and global variables within the process, whereas fork() creates a distinct, separate address space.",
                    "Threads each run in separate hardware CPUs, whereas processes share one CPU.",
                    "Processes share heap memory, whereas threads receive independent isolated kernels.",
                    "Threads require a separate system init process for execution."
                ],
                "correctAnswer": "Threads share the same virtual address space, heap, and global variables within the process, whereas fork() creates a distinct, separate address space.",
                "explanation": "Threads within a process share the text segment, data segment, heap, and file descriptors, maintaining only private stacks and registers. 'fork()' produces an independent copy of the process address space."
            },
            {
                "question": "What is the purpose of the 'pthread_join()' function in a multi-threaded C application?",
                "options": [
                    "It suspends the calling thread until the target worker thread terminates, preventing premature program exit.",
                    "It combines two independent thread stacks into a single memory block.",
                    "It passes mutex ownership from one thread to another.",
                    "It restarts a terminated thread with new arguments."
                ],
                "correctAnswer": "It suspends the calling thread until the target worker thread terminates, preventing premature program exit.",
                "explanation": "'pthread_join(thread, NULL)' blocks the calling thread (e.g. main) until the target thread finishes execution, ensuring results are computed before main exits."
            },
            {
                "question": "Which compiler flag must be passed to GCC/Clang when compiling programs that utilize the POSIX Pthreads library?",
                "options": [
                    "-lpthread",
                    "-lposix",
                    "-threads",
                    "-pthreads_static"
                ],
                "correctAnswer": "-lpthread",
                "explanation": "The POSIX thread library is linked during compilation using the '-lpthread' linker flag (e.g., 'gcc -lpthread program.c')."
            },
            {
                "question": "In the Open-Ended Lab task of Lab 7, how do worker threads return statistical values (average, min, max) to the main thread?",
                "options": [
                    "By updating shared global variables or returning allocated pointers via pthread_exit() / pthread_join().",
                    "By writing to a temporary disk file in /tmp/stats.",
                    "By sending inter-process Unix domain socket signals.",
                    "By issuing fork() calls back to the parent process."
                ],
                "correctAnswer": "By updating shared global variables or returning allocated pointers via pthread_exit() / pthread_join().",
                "explanation": "Because all Pthreads share the same process memory space, worker threads can directly write their results (average, min, max) to global variables or pass return pointers through pthread_exit."
            }
        ],
        "flashcards": [
            {
                "question": "What standard defines POSIX threads (Pthreads)?",
                "answer": "The IEEE POSIX 1003.1c standard (1995)."
            },
            {
                "question": "Why is thread creation ten to a hundred times faster than process creation with fork()?",
                "answer": "Because the kernel does not need to duplicate the process memory address space, page tables, or file descriptors; it only allocates a stack and register set."
            },
            {
                "question": "What signature is required for a POSIX thread start routine?",
                "answer": "void *function_name(void *arg) - it accepts a void pointer and returns a void pointer."
            },
            {
                "question": "What potential danger exists when multiple threads share memory without synchronization?",
                "answer": "Memory corruption, race conditions, and lack of isolation: if one thread corrupts shared memory or crashes, all threads in the process are affected."
            }
        ]
    },
    {
        "order": 8,
        "title": "Lab 8: Demonstrate Thread Synchronization Issues Using POSIX Thread Library",
        "codeSnippet": "// Mutex example in C using POSIX Thread Library\n#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\nvoid *functionC();\npthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;\nint counter = 0;\n\nint main()\n{\n   int rc1, rc2;\n   pthread_t thread1, thread2;\n\n   if((rc1 = pthread_create(&thread1, NULL, &functionC, NULL)))\n      printf(\"Thread creation failed: %d\\n\", rc1);\n\n   if((rc2 = pthread_create(&thread2, NULL, &functionC, NULL)))\n      printf(\"Thread creation failed: %d\\n\", rc2);\n\n   pthread_join(thread1, NULL);\n   pthread_join(thread2, NULL);\n\n   exit(0);\n}\n\nvoid *functionC()\n{\n   pthread_mutex_lock(&mutex1);\n   counter++;\n   printf(\"Counter value: %d\\n\", counter);\n   pthread_mutex_unlock(&mutex1);\n}",
        "content": "# Lab#08\n\n## DEMONSTRATE THREAD SYNCHRONIZATION ISSUES USING POSIX THREAD LIBRARY.\n\n### Objective\n* Mutex, Join and condition variables\n\n### Theory Overview\nThe threads library provides three synchronization mechanisms:\n\n* **mutexes** - Mutual exclusion lock: Block access to variables by other threads. This enforces exclusive access by a thread to a variable or set of variables.\n* **joins** - Make a thread wait till others are complete (terminated).\n* **condition variables** - data type `pthread_cond_t`\n\n---\n\n### Mutexes:\nMutexes are used to prevent data inconsistencies due to race conditions. A race condition often occurs when two or more threads need to perform operations on the same memory area, but the results of computations depends on the order in which these operations are performed. Mutexes are used for serializing shared resources. Anytime a global resource is accessed by more than one thread the resource should have a Mutex associated with it. One can apply a mutex to protect a segment of memory (\"critical region\") from other threads. Mutexes can be applied only to threads in a single process and do not work between processes as do semaphores.\n\n#### Example threaded function:\n\n| Without Mutex | With Mutex |\n| :--- | :--- |\n| ```c<br>int counter=0;<br><br>/* Function C */<br>void functionC()<br>{<br>   counter++;<br>}<br>``` | ```c<br>/* Note scope of variable and mutex are the same */<br>pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;<br>int counter=0;<br><br>/* Function C */<br>void functionC()<br>{<br>   pthread_mutex_lock( &mutex1 );<br>   counter++;<br>   pthread_mutex_unlock( &mutex1 );<br>}<br>``` |\n\n#### Possible execution sequence:\n\n**Without Mutex:**\n* Thread 1: `counter = 0`\n* Thread 2: `counter = 0`\n* Thread 1: `counter = 1`\n* Thread 2: `counter = 1`\n\nIf register load and store operations for the incrementing of variable counter occurs with unfortunate timing, it is theoretically possible to have each thread increment and overwrite the same variable with the same value. Another possibility is that thread two would first increment counter locking out thread one until complete and then thread one would increment it to 2.\n\n**With Mutex:**\n* Sequence 1: Thread 1 reads `counter = 0`, Thread 2 locked out. Thread 1 has exclusive use of variable counter. `counter = 1`.\n* Sequence 2: Thread 2 acquires mutex, reads `counter = 1`, `counter = 2`.\n\n---\n\n### Example 1: mutex1.c\n```c\n#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\nvoid *functionC();\npthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;\nint counter = 0;\n\nmain()\n{\n   int rc1, rc2;\n   pthread_t thread1, thread2;\n\n   /* Create independent threads each of which will execute functionC */\n   if( (rc1=pthread_create( &thread1, NULL, &functionC, NULL)) )\n   {\n      printf(\"Thread creation failed: %d \\n\", rc1);\n   }\n\n   if( (rc2=pthread_create( &thread2, NULL, &functionC, NULL)) )\n   {\n      printf(\"Thread creation failed: %d \\n\", rc2);\n   }\n\n   /* Wait till threads are complete before main continues. Unless we */\n   /* wait we run the risk of executing an exit which will terminate  */\n   /* the process and all threads before the threads have completed.  */\n   pthread_join( thread1, NULL);\n   pthread_join( thread2, NULL);\n\n   exit(0);\n}\n\nvoid *functionC()\n{\n   pthread_mutex_lock( &mutex1 );\n   counter++;\n   printf(\"Counter value: %d \\n\", counter);\n   pthread_mutex_unlock( &mutex1 );\n}\n```\n\n**Compile:** `cc -lpthread mutex1.c`  \n**Run:** `./a.out`  \n**Results:**  \n```text\nCounter value: 1\nCounter value: 2\n```\n\nWhen a mutex lock is attempted against a mutex which is held by another thread, the thread is blocked until the mutex is unlocked. When a thread terminates, the mutex does not unless explicitly unlocked. Nothing happens by default.\n\n---\n\n### Joins:\nA join is performed when one wants to wait for a thread to finish. A thread calling routine may launch multiple threads then wait for them to finish to get the results. One wait for the completion of the threads with a join.\n\n### Example 2: join1.c\n```c\n#include <stdio.h>\n#include <pthread.h>\n\n#define NTHREADS 10\nvoid *thread_function(void *);\npthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;\nint counter = 0;\n\nmain()\n{\n   pthread_t thread_id[NTHREADS];\n   int i, j;\n\n   for(i=0; i < NTHREADS; i++)\n   {\n      pthread_create( &thread_id[i], NULL, thread_function, NULL );\n   }\n\n   for(j=0; j < NTHREADS; j++)\n   {\n      pthread_join( thread_id[j], NULL);\n   }\n   \n   /* Now that all threads are complete I can print the final result. */\n   /* Without the join I could be printing a value before all the threads */\n   /* have been completed. */\n\n   printf(\"Final counter value: %d \\n\", counter);\n}\n\nvoid *thread_function(void *dummyPtr)\n{\n   printf(\"Thread number %ld \\n\", pthread_self());\n   pthread_mutex_lock( &mutex1 );\n   counter++;\n   pthread_mutex_unlock( &mutex1 );\n}\n```\n\n**Compile:** `cc -lpthread join1.c`  \n**Run:** `./a.out`  \n**Results:**  \n```text\nThread number 1026\nThread number 2051\nThread number 3076\nThread number 4101\nThread number 5126\nThread number 6151\nThread number 7176\nThread number 8201\nThread number 9226\nThread number 10251\nFinal counter value: 10\n```\n\n---\n\n### Condition Variables:\nA condition variable is a variable of type `pthread_cond_t` and is used with the appropriate functions for waiting and later, process continuation. The condition variable mechanism allows threads to suspend execution and relinquish the processor until some condition is true. A condition variable must always be associated with a mutex to avoid a race condition created by one thread preparing to wait and another thread which may signal the condition before the first thread actually waits on it resulting in a deadlock. The thread will be perpetually waiting for a signal that is never sent. Any mutex can be used, there is no explicit link between the mutex and the condition variable.\n\n#### Functions used in conjunction with the condition variable:\n\n* **Creating/Destroying:**\n  * `pthread_cond_init`\n  * `pthread_cond_t cond = PTHREAD_COND_INITIALIZER;`\n  * `pthread_cond_destroy`\n* **Waiting on condition:**\n  * `pthread_cond_wait`\n  * `pthread_cond_timedwait` - place limit on how long it will block.\n* **Waking thread based on condition:**\n  * `pthread_cond_signal`\n  * `pthread_cond_broadcast` - wake up all threads blocked by the specified condition variable.\n\n---\n\n### Example 3: cond1.c\n```c\n#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\npthread_mutex_t count_mutex     = PTHREAD_MUTEX_INITIALIZER;\npthread_mutex_t condition_mutex = PTHREAD_MUTEX_INITIALIZER;\npthread_cond_t  condition_cond  = PTHREAD_COND_INITIALIZER;\n\nvoid *functionCount1();\nvoid *functionCount2();\nint count = 0;\n#define COUNT_DONE   10\n#define COUNT_HALT1  3\n#define COUNT_HALT2  6\n\nmain()\n{\n   pthread_t thread1, thread2;\n\n   pthread_create( &thread1, NULL, &functionCount1, NULL);\n   pthread_create( &thread2, NULL, &functionCount2, NULL);\n   pthread_join( thread1, NULL);\n   pthread_join( thread2, NULL);\n\n   exit(0);\n}\n\nvoid *functionCount1()\n{\n   for(;;)\n   {\n      pthread_mutex_lock( &condition_mutex );\n      while( count >= COUNT_HALT1 && count <= COUNT_HALT2 )\n      {\n         pthread_cond_wait( &condition_cond, &condition_mutex );\n      }\n      pthread_mutex_unlock( &condition_mutex );\n\n      pthread_mutex_lock( &count_mutex );\n      count++;\n      printf(\"Counter value functionCount1: %d \\n\", count);\n      pthread_mutex_unlock( &count_mutex );\n\n      if(count >= COUNT_DONE) return(NULL);\n   }\n}\n\nvoid *functionCount2()\n{\n    for(;;)\n    {\n       pthread_mutex_lock( &condition_mutex );\n       if( count < COUNT_HALT1 || count > COUNT_HALT2 )\n       {\n          pthread_cond_signal( &condition_cond );\n       }\n       pthread_mutex_unlock( &condition_mutex );\n\n       pthread_mutex_lock( &count_mutex );\n       count++;\n       printf(\"Counter value functionCount2: %d \\n\", count);\n       pthread_mutex_unlock( &count_mutex );\n\n       if(count >= COUNT_DONE) return(NULL);\n    }\n}\n```\n\n**Compile:** `cc -lpthread cond1.c`  \n**Run:** `./a.out`  \n**Results:**  \n```text\nCounter value functionCount1: 1\nCounter value functionCount1: 2\nCounter value functionCount1: 3\nCounter value functionCount2: 4\nCounter value functionCount2: 5\nCounter value functionCount2: 6\nCounter value functionCount2: 7\nCounter value functionCount1: 8\nCounter value functionCount1: 9\nCounter value functionCount1: 10\nCounter value functionCount2: 11\n```\n\nNote that `functionCount1()` was halted while count was between the values `COUNT_HALT1` and `COUNT_HALT2`. The only thing that has been ensured is that `functionCount2` will increment the count between the values `COUNT_HALT1` and `COUNT_HALT2`. Everything else is random.\n\n### Tools:\nRed Hat Linux\n",
        "quizzes": [
            {
                "question": "What is the primary purpose of a mutex in POSIX multithreaded programming?",
                "options": [
                    "To enforce mutual exclusion and prevent race conditions when multiple threads access shared memory.",
                    "To speed up thread execution by assigning each thread to a dedicated physical processor core.",
                    "To automatically terminate any thread that consumes more than 100 milliseconds of CPU time.",
                    "To allow processes on different networked hosts to share address spaces."
                ],
                "correctAnswer": "To enforce mutual exclusion and prevent race conditions when multiple threads access shared memory.",
                "explanation": "Mutexes (mutual exclusion locks) serialize access to critical regions and shared variables, ensuring only one thread can modify the shared resource at any given time."
            },
            {
                "question": "Why must a condition variable (pthread_cond_t) always be associated with a mutex in POSIX threads?",
                "options": [
                    "To prevent a race condition where a signaling thread signals before the waiting thread actually enters the wait state.",
                    "Because condition variables cannot allocate memory without a mutex.",
                    "To allow threads to communicate across different physical machines over the network.",
                    "Because POSIX threads do not permit functions to accept more than one argument without a mutex."
                ],
                "correctAnswer": "To prevent a race condition where a signaling thread signals before the waiting thread actually enters the wait state.",
                "explanation": "If a condition variable were used without a mutex, a thread checking the predicate might be interrupted, and another thread could signal before the first waits, causing a missed wakeup and permanent deadlock."
            },
            {
                "question": "What happens when a thread calls pthread_join(thread_id, NULL)?",
                "options": [
                    "The calling thread suspends execution until the target thread terminates.",
                    "The target thread is forcibly aborted and its memory wiped immediately.",
                    "Both threads merge their stack memories and share local variables.",
                    "The calling thread copies all register contents of the target thread into global variables."
                ],
                "correctAnswer": "The calling thread suspends execution until the target thread terminates.",
                "explanation": "'pthread_join' blocks the calling thread until the specified target thread finishes execution, allowing clean synchronization and reclamation of resources."
            },
            {
                "question": "What is the difference between pthread_cond_signal and pthread_cond_broadcast?",
                "options": [
                    "pthread_cond_signal unblocks at least one waiting thread, while pthread_cond_broadcast unblocks all threads waiting on the condition variable.",
                    "pthread_cond_signal transmits an IPC message over UNIX sockets, while broadcast transmits to the local loopback interface.",
                    "pthread_cond_signal locks the mutex, while pthread_cond_broadcast unlocks the mutex.",
                    "pthread_cond_signal is deprecated in POSIX standards and replaced by pthread_cond_broadcast."
                ],
                "correctAnswer": "pthread_cond_signal unblocks at least one waiting thread, while pthread_cond_broadcast unblocks all threads waiting on the condition variable.",
                "explanation": "'pthread_cond_signal' wakes up at least one thread waiting on the condition variable, whereas 'pthread_cond_broadcast' wakes up all currently blocked threads."
            }
        ],
        "flashcards": [
            {
                "question": "What is a race condition in multithreaded systems?",
                "answer": "A condition where multiple threads access and manipulate shared data concurrently, and the final outcome depends on the non-deterministic order of thread execution."
            },
            {
                "question": "Can POSIX mutexes be shared across different processes?",
                "answer": "By default, standard mutexes protect threads within a single process. Sharing between processes requires semaphores or process-shared mutex attributes (PTHREAD_PROCESS_SHARED)."
            },
            {
                "question": "How do you statically initialize a POSIX mutex in C?",
                "answer": "Using the macro: pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;"
            },
            {
                "question": "What function is used to retrieve the unique thread identifier of the currently executing thread?",
                "answer": "pthread_self() returns the thread ID (pthread_t) of the calling thread."
            }
        ]
    },
    {
        "order": 9,
        "title": "Lab 9: Execute the Simulation of Various CPU Scheduling Algorithms",
        "codeSnippet": "// Simulation of Round Robin Scheduling Algorithm using C in Linux\n#include <stdio.h>\n\nint main()\n{\n    int et[30], ts, n, i, x = 0, tot = 0;\n    char pn[10][10];\n\n    printf(\"Enter the no of processes: \");\n    scanf(\"%d\", &n);\n    printf(\"Enter the time quantum: \");\n    scanf(\"%d\", &ts);\n\n    for(i = 0; i < n; i++)\n    {\n        printf(\"enter process name & estimated time: \");\n        scanf(\"%s %d\", pn[i], &et[i]);\n    }\n\n    printf(\"\\nThe processes are:\\n\");\n    for(i = 0; i < n; i++)\n        printf(\"process %d: %s\\n\", i + 1, pn[i]);\n\n    for(i = 0; i < n; i++)\n        tot = tot + et[i];\n\n    while(x != tot)\n    {\n        for(i = 0; i < n; i++)\n        {\n            if(et[i] > ts)\n            {\n                x = x + ts;\n                printf(\"\\n%s -> %d\", pn[i], ts);\n                et[i] = et[i] - ts;\n            }\n            else if(et[i] > 0)\n            {\n                x = x + et[i];\n                printf(\"\\n%s -> %d\", pn[i], et[i]);\n                et[i] = 0;\n            }\n        }\n    }\n\n    printf(\"\\nTotal Estimated Time: %d\\n\", tot);\n    return 0;\n}",
        "content": "# Lab#09\n\n## EXECUTE THE SIMULATION OF VARIOUS CPU SCHEDULING ALGORITHMS.\n\n### Objective\n* Simulation of Round Robin Scheduling Algorithm Using C Language in Linux\n\n### Theory Overview\n\n#### Round Robin Scheduling (RR)\nIn interactive environments, such as time-sharing systems, the primary requirement is to provide reasonably good response time and, in general, to share system resources equitably among all users. Obviously, only preemptive disciplines may be considered in such environments, and one of the most popular is time slicing, also known as round robin.\n\nIn this scheme, the processor time is divided into slices or quanta which are allocated to processes waiting in a ready queue. A time quantum is generally from 1 to 100 milliseconds. The ready queue is treated as a circular queue.\n\nThe RR scheduling attempts to reduce the penalty that short jobs suffer with FCFS by the use of preemption based on clock.\n\n#### Mechanism\nTo implement RR scheduling, the ready queue is kept as a FIFO queue of processes. New processes are added to the tail of the ready queue. The CPU scheduler picks the process for running from the ready queue. No process can run for more than one time slice when there are others in the ready queue. If a process does not complete before its slice expires, it is placed at the end of the ready queue and CPU allocated to the next ready job on FCFS basis. This arrangement of the ready list effectively lowers the scheduling priority of the preempted process.\n\nIn this way, processor time is effectively allocated to processes on a rotating priority basis (hence the name round robin) and every one of them in turn receives approximately $1/N$ of processor time, where $N$ is the number of ready processes.\n\nIt is obviously a preemptive scheduling scheme.\n\n#### Implementation\nThe implementation of RR scheduling requires support of an interval timer – preferably a dedicated one, as opposed to sharing the system time base. The timer is usually set to interrupt the OS whenever a time slice expires and thus force the scheduler to be invoked.\n\nThe scheduler itself simply stores the context of the running process, moves it to the end of the ready queue and dispatches the process at the head of the ready queue. The scheduler is also invoked to dispatch a new process whenever the running process surrenders control to the OS before expiration of its quantum, say, by requesting I/O. The interval timer is usually reset at that point, in order to provide the full time slot to the new running process.\n\nThe frequent setting and resetting of a dedicated interval timer makes hardware support desirable in systems that use time slicing.\n\n---\n\n### Characteristics\n* **Decision Mode:** Preemptive (at time quantum).\n* **Selection Function:** Constant\n* **Throughput:** May be low if quantum is too small\n* **Response time:** Good for short processes.\n* **Overhead:** Minimum\n* **Effect on processes:** Fair treatment\n* **Starvation:** No\n\n### Advantage\nRR scheduling is often regarded as a fair scheduling discipline because it achieves equitable sharing of system resources. It is one of the best known scheduling disciplines for achieving good and relatively evenly distributed terminal response time.\n\n### Drawbacks\n* Round-robin scheduling generally discriminates against long non interactive jobs. Long processes may require several quanta and thus be forced to cycle through the ready queue a few times before completion.\n* One drawback to RR is its relative treatment of processor-bound and I/O-bound processes. Generally, an I/O-bound process has a shorter processor burst (amount of time spent executing between I/O operations) than a processor-bound process. If there is a mix of processor-bound and I/O-bound processes, then the following will happen: An I/O bound process uses a processor for a short period and then is blocked for I/O; it waits for the I/O operation to complete and then joins the ready queue. On the other hand, a processor-bound process generally uses a complete time quantum while executing and immediately returns to the ready queue. Thus processor-bound processes tend to receive an unfair portion of processor time, which results in poor performance for I/O bound processes, inefficient use of I/O devices and an increase in the variance of response time.\n\n---\n\n### Programming in C with LINUX\nC is a programming language that can be used to create programs for Linux. The C language is used in text files called source code files. The source code files are read by programs included with the GNU gcc compiler suite during the process of building a new Linux program. C is a compiled language which means that the C code is first analyzed by the preprocessor and then translated into assembler language first and then into machine instructions that are appropriate to the target CPU. An assembler then creates a binary, or object, file from the machine instructions. Finally the object file is linked to any required external software support by the linker. A C program is stored in a text file that ends with a `.c` extension and always contain at least one routine, or function, such as `main()`. Functions are the commands that perform each step of the task that the C program was written to accomplish.\n\nWe shall create an executable program for Linux using gcc. The aim of the program is to simulate the Round Robin Scheduling algorithm using C language.\n\nTo get started, type in the following text, using your Linux text editor:\n\n```c\n#include<stdio.h>\n#include<conio.h>\n\nvoid main()\n{\n    int et[30], ts, n, i, x=0, tot=0;\n    char pn[10][10];\n    clrscr();\n    printf(\"Enter the no of processes:\");\n    scanf(\"%d\", &n);\n    printf(\"Enter the time quantum:\");\n    scanf(\"%d\", &ts);\n    for(i=0; i<n; i++)\n    {\n        printf(\"enter process name & estimated time:\");\n        scanf(\"%s %d\", pn[i], &et[i]);\n    }\n    printf(\"The processes are:\");\n    for(i=0; i<n; i++)\n        printf(\"process %d: %s\\n\", i+1, pn[i]);\n    for(i=0; i<n; i++)\n        tot = tot + et[i];\n    while(x != tot)\n    {\n        for(i=0; i<n; i++)\n        {\n            if(et[i] > ts)\n            {\n                x = x + ts;\n                printf(\"\\n %s -> %d\", pn[i], ts);\n                et[i] = et[i] - ts;\n            }\n            else if(et[i] > 0)\n            {\n                x = x + et[i];\n                printf(\"\\n %s -> %d\", pn[i], et[i]);\n                et[i] = 0;\n            }\n        }\n    }\n    printf(\"\\nTotal Estimated Time: %d\", tot);\n    getch();\n}\n```\n\n#### Output:\n```text\nInput:\nEnter the no of processes: 2\nEnter the time quantum: 3\nEnter the process name & estimated time: p1 12\nEnter the process name & estimated time: p2 15\n\nOutput:\np1 -> 3\np2 -> 3\np1 -> 3\np2 -> 3\np1 -> 3\np2 -> 3\np1 -> 3\np2 -> 3\np2 -> 3\nTotal Estimated Time: 27\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Simulate the SJF (Shortest Job First) CPU Scheduling Algorithm using C.\n",
        "quizzes": [
            {
                "question": "What scheduling paradigm characterizes the Round Robin (RR) CPU scheduling algorithm?",
                "options": [
                    "Preemptive time-slicing with a circular ready queue.",
                    "Non-preemptive priority scheduling based on arrival time.",
                    "Multilevel feedback queuing with exponential decay.",
                    "Static priority scheduling where CPU-bound jobs have highest precedence."
                ],
                "correctAnswer": "Preemptive time-slicing with a circular ready queue.",
                "explanation": "Round Robin assigns a fixed time quantum (slice) to each process in a circular FIFO queue, preempting the currently running process when its quantum expires."
            },
            {
                "question": "What is the consequence of choosing an excessively small time quantum in Round Robin scheduling?",
                "options": [
                    "Context-switch overhead increases drastically, reducing CPU throughput and useful execution time.",
                    "Processes experience indefinite starvation and cannot complete.",
                    "The algorithm degenerates into non-preemptive First-Come, First-Served (FCFS).",
                    "The system runs out of physical memory due to PCB stack overflow."
                ],
                "correctAnswer": "Context-switch overhead increases drastically, reducing CPU throughput and useful execution time.",
                "explanation": "If the time quantum is too small, the system spends a disproportionate amount of time performing context switches rather than executing user process instructions."
            },
            {
                "question": "Why does standard Round Robin scheduling tend to discriminate against I/O-bound processes in mixed workloads?",
                "options": [
                    "I/O-bound processes release the CPU before their quantum expires, while CPU-bound processes use their full slice, thus receiving more CPU time relative to their waiting time.",
                    "I/O-bound processes are permanently demoted to the lowest priority queue.",
                    "The operating system disables timer interrupts during I/O operations.",
                    "I/O-bound processes require exponential bursts that exceed the hardware timer limit."
                ],
                "correctAnswer": "I/O-bound processes release the CPU before their quantum expires, while CPU-bound processes use their full slice, thus receiving more CPU time relative to their waiting time.",
                "explanation": "I/O-bound jobs relinquish the CPU quickly to do I/O, but join the end of the ready queue behind CPU-bound jobs that utilized complete time quanta, causing poor response times for I/O devices."
            },
            {
                "question": "Does Round Robin scheduling suffer from process starvation?",
                "options": [
                    "No, because every ready process gets approximately 1/N of the CPU time within a finite time bound.",
                    "Yes, because long jobs can be indefinitely preempted by shorter jobs.",
                    "Yes, if new processes arrive faster than the quantum duration.",
                    "Only on multi-core systems when affinity is disabled."
                ],
                "correctAnswer": "No, because every ready process gets approximately 1/N of the CPU time within a finite time bound.",
                "explanation": "Because of the circular FIFO queue and guaranteed preemption after one quantum, every ready process is guaranteed a turn in CPU execution; thus starvation is impossible."
            }
        ],
        "flashcards": [
            {
                "question": "What is a CPU time quantum?",
                "answer": "A predefined, discrete unit of CPU time (typically 10 to 100 milliseconds) allocated to a process before preemption in time-sharing systems."
            },
            {
                "question": "What happens if a process's CPU burst is shorter than the assigned time quantum?",
                "answer": "The process releases the CPU voluntarily (e.g. for I/O or termination), and the scheduler dispatches the next process immediately without waiting for quantum expiration."
            },
            {
                "question": "How does Round Robin behave if the time quantum is made extremely large (approaching infinity)?",
                "answer": "It degenerates into First-Come, First-Served (FCFS) scheduling, where each process runs to completion before relinquishing the CPU."
            },
            {
                "question": "What hardware component is essential for implementing preemptive Round Robin scheduling in an OS?",
                "answer": "An interval timer (hardware programmable timer) that generates periodic timer interrupts to invoke the OS scheduler."
            }
        ]
    },
    {
        "order": 10,
        "title": "Lab 10: Execute the Simulation of FIFO and LRU Page Replacement Algorithms",
        "codeSnippet": "// Simulation of Least Recently Used (LRU) Page Replacement Algorithm in C\n#include <stdio.h>\n\nint main()\n{\n    int g=0, a[5], b[20], p=0, q=0, m=0, h, k, i, q1=1, j, u, n;\n    char f='F';\n\n    printf(\"Enter the number of pages: \");\n    scanf(\"%d\", &n);\n    printf(\"Enter %d Page Numbers: \", n);\n    for(i=0; i<n; i++)\n        scanf(\"%d\", &b[i]);\n\n    for(i=0; i<n; i++)\n    {\n        if(p==0)\n        {\n            if(q>=3)\n                q=0;\n            a[q]=b[i];\n            q++;\n            if(q1<3)\n                q1=q;\n        }\n        printf(\"\\n%d\\t\", b[i]);\n        for(h=0; h<q1; h++)\n            printf(\"%d \", a[h]);\n\n        p=0;\n        g=0;\n        printf(\"--> %c\", f);\n        m++;\n\n        if(q1==3)\n        {\n            for(k=0; k<q1; k++)\n            {\n                if(b[i+1]==a[k])\n                    p=1;\n            }\n            for(j=0; j<q1; j++)\n            {\n                u=0;\n                k=i;\n                while(k>=(i-1) && (k>=0))\n                {\n                    if(b[k]==a[j])\n                        u++;\n                    k--;\n                }\n            }\n        }\n        else\n        {\n            if(u==0)\n                q=j;\n            for(k=0; k<q; k++)\n            {\n                if(b[i+1]==a[k])\n                    p=1;\n            }\n        }\n    }\n    printf(\"\\nNo of faults: %d\\n\", m);\n    return 0;\n}",
        "content": "# Lab#10\n\n## EXECUTE THE SIMULATION OF FIFO AND LRU PAGE REPLACEMENT ALGORITHMS.\n\n### Objective\n* Least Recently Used (LRU) Page Replacement Algorithm simulation\n* First in First Out (FIFO) Page Replacement Algorithm simulation\n\n### Theory Overview\nIn a computer operating system that uses paging for virtual memory management, page replacement algorithms decide which memory pages to page out (swap out, write to disk) when a page of memory needs to be allocated. Paging happens when a page fault occurs and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.\n\nWhen the page that was selected for replacement and paged out is referenced again it has to be paged in (read in from disk), and this involves waiting for I/O completion. This determines the quality of the page replacement algorithm: the less time waiting for page-ins, the better the algorithm. A page replacement algorithm looks at the limited information about accesses to the pages provided by hardware, and tries to guess which pages should be replaced to minimize the total number of page misses, while balancing this with the costs (primary storage and processor time) of the algorithm itself.\n\nThere are a variety of Page Replacement Algorithms:\n\n---\n\n### FIFO Page Replacement\nThe simplest page-replacement algorithm is a FIFO algorithm. The first-in, first-out (FIFO) page replacement algorithm is a low-overhead algorithm that requires little book-keeping on the part of the operating system. The idea is obvious from the name - the operating system keeps track of all the pages in memory in a queue, with the most recent arrival at the back, and the earliest arrival in front. When a page needs to be replaced, the page at the front of the queue (the oldest page) is selected. While FIFO is cheap and intuitive, it performs poorly in practical application. Thus, it is rarely used in its unmodified form. This algorithm experiences Belady's anomaly.\n\nFIFO page replacement algorithm is used by the VAX/VMS operating system, with some modifications.\n\nE.g. a,b,c,d, and e are page nos. Consider the following reference string:\n`cadbebabca`\n\nSuppose there are four frames of memory numbered from 0 to 3. The following illustrates how the allocations of frames will proceed:\n\n![FIFO Page Replacement](assets/images/university/os/lab10_fifo_page_replacement.png)\n\nThere would be three page faults altogether for the above reference string if FIFO is used.\n\n---\n\n### LRU (Least Recently Used)\nThis algorithm is based on the observation that pages that have been heavily used in the last few instructions will probably be heavily used again in the next few. Conversely, pages that have not been used for ages will probably remain unused for a long time. This idea suggests a realizable algorithm: when a page fault occurs, throw out the page that has been unused for the longest time. This strategy is thus called LRU (Least Recently Used) paging.\n\n#### Implementation:\nWhile LRU can provide near-optimal performance in theory, it is rather expensive to implement in practice. There are a few implementation methods for this algorithm that try to reduce the cost yet keep as much of the performance as possible.\n\n* **Linked List Method:** The most expensive method is the linked list method, which uses a linked list containing all the pages in memory. At the back of this list is the least recently used page, and at the front is the most recently used page. The cost of this implementation lies in the fact that items in the list will have to be moved about every memory reference, which is a very time-consuming process.\n* **Hardware Counter Method:** Another method that requires hardware support is as follows: suppose the hardware has a 64-bit counter that is incremented at every instruction. Whenever a page is accessed, it gains a value equal to the counter at the time of page access. Whenever a page needs to be replaced, the operating system selects the page with the lowest counter and swaps it out. With present hardware, this is not feasible because the OS needs to examine the counter for every page in memory.\n\nBecause of implementation costs, one may consider algorithms that are similar to LRU, but which offer cheaper implementations.\n\n#### Advantages:\n* One important advantage of the LRU algorithm is that it is amenable to full statistical analysis. It has been proven, for example, that LRU can never result in more than N-times more page faults than Optimal algorithm, where N is proportional to the number of pages in the managed pool.\n* This algorithm doesn't experience Belady's anomaly.\n\n#### Disadvantage:\nLRU's weakness is that its performance tends to degenerate under many quite common reference patterns. For example, if there are N pages in the LRU pool, an application executing a loop over array of N + 1 pages will cause a page fault on each and every access. As loops over large arrays are common, much effort has been put into modifying LRU to work better in such situations. Many of the proposed LRU modifications try to detect looping reference patterns and to switch into suitable replacement algorithm, like Most Recently Used (MRU).\n\ne.g.: Consider the following reference string:  \n`cadbebabcd`\n\nSuppose there are four frames of memory numbered from 0 to 3. The following illustrates how the allocations of frames will proceed:\n\n![LRU Page Replacement](assets/images/university/os/lab10_lru_page_replacement.png)\n\nThere would be three page faults altogether for the above reference string if LRU is used.\n\n---\n\n### Belady's Anomaly\nGiven a reference string, it would be natural to assume that the more the total number of frames in main memory, the fewer the number of page faults. But this is not true for some algorithms. For e.g. FIFO. This anomaly is called Belady's Anomaly.\n\nTo illustrate this consider the following reference string:  \n`0 1 2 3 0 1 4 0 1 2 3 4`\n\n![Belady's Anomaly / Page Replacement](assets/images/university/os/lab10_page_replacement.png)\n\n* **Case 1:** 3 frames available $\\rightarrow$ 9 page faults\n* **Case 2:** 4 frames available $\\rightarrow$ 10 page faults\n\n---\n\n### C Simulation of Least Recently Used Page Replacement Algorithm\nWe shall create an executable program for Linux using gcc. The aim of the program is to simulate the Least Recently Used Page Replacement Algorithm using C language.\n\nType in the following text, using your Linux text editor:\n\n```c\n#include<stdio.h>\n#include<conio.h>\n\nvoid main()\n{\n    int g=0, a[5], b[20], p=0, q=0, m=0, h, k, i, q1=1, j, u, n;\n    char f='F';\n    clrscr();\n    printf(\"Enter the number of pages:\");\n    scanf(\"%d\", &n);\n    printf(\"Enter %d Page Numbers:\", n);\n    for(i=0; i<n; i++)\n        scanf(\"%d\", &b[i]);\n    for(i=0; i<n; i++)\n    {\n        if(p==0)\n        {\n            if(q>=3)\n                q=0;\n            a[q]=b[i];\n            q++;\n            if(q1<3)\n            {\n                q1=q;\n                //g=1;\n            }\n        }\n        printf(\"\\n%d\", b[i]);\n        printf(\"\\t\");\n        for(h=0; h<q1; h++)\n            printf(\"%d\", a[h]);\n        if((p==0) && (q<=3))\n        {\n        }\n        p=0;\n        g=0;\n        printf(\"-->%c\", f);\n        m++;\n        if(q1==3)\n        {\n            for(k=0; k<q1; k++)\n            {\n                if(b[i+1]==a[k])\n                    p=1;\n            }\n            for(j=0; j<q1; j++)\n            {\n                u=0;\n                k=i;\n                while(k>=(i-1) && (k>=0))\n                {\n                    if(b[k]==a[j])\n                        u++;\n                    k--;\n                }\n            }\n        }\n        else\n        {\n            if(u==0)\n                q=j;\n            for(k=0; k<q; k++)\n            {\n                if(b[i+1]==a[k])\n                    p=1;\n            }\n        }\n    }\n    printf(\"\\nNo of faults:%d\", m);\n    getch();\n}\n```\n\nCompile and run the program using the same procedure as given in the previous lab.\n\n#### OUTPUT:\n```text\nInput:\nEnter the Number of Pages: 12\nEnter 12 Page Numbers:\n1 3 2 1 5 2 4 5 3 2 5 2\n\nOutput:\n2  2-> F\n2  23-> F\n2  23\n1  231-> F\n5  251-> F\n2  251\n3  254-> F\n4  254\n3  354-> F\n2  352-> F\n5  352\n2  352\nNo of faults: 7\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Simulate the FIFO Page Replacement Algorithm using C.\n",
        "quizzes": [
            {
                "question": "What is Belady's Anomaly in the context of virtual memory page replacement?",
                "options": [
                    "The counter-intuitive phenomenon where increasing the number of page frames results in an increased number of page faults for certain algorithms like FIFO.",
                    "A condition where thrashing causes the CPU utilization to drop to exactly 0%.",
                    "An error where pages are written to swap disk faster than they can be read back.",
                    "The failure of LRU when memory addresses exceed 32 bits."
                ],
                "correctAnswer": "The counter-intuitive phenomenon where increasing the number of page frames results in an increased number of page faults for certain algorithms like FIFO.",
                "explanation": "Belady's Anomaly occurs in FIFO and certain non-stack algorithms where allocating more physical memory frames actually increases the total page fault rate on specific reference strings."
            },
            {
                "question": "Does the Least Recently Used (LRU) algorithm suffer from Belady's Anomaly?",
                "options": [
                    "No, because LRU belongs to the class of 'stack algorithms' where the set of pages in an n-frame memory is always a subset of an (n+1)-frame memory.",
                    "Yes, whenever the reference string contains cyclical loops of length greater than 4.",
                    "Yes, on architectures with less than 64-bit counter support.",
                    "Only when virtual memory is implemented without TLB hardware caching."
                ],
                "correctAnswer": "No, because LRU belongs to the class of 'stack algorithms' where the set of pages in an n-frame memory is always a subset of an (n+1)-frame memory.",
                "explanation": "LRU is proven to be a stack algorithm; the set of pages in memory with n frames is always a subset of the pages that would be in memory with n+1 frames, completely precluding Belady's Anomaly."
            },
            {
                "question": "Under what common programming scenario does LRU page replacement perform exceptionally poorly?",
                "options": [
                    "When executing loops over large arrays spanning N + 1 pages when only N frames are available in the page pool.",
                    "When executing recursive functions that stay within a single 4KB stack page.",
                    "When allocating dynamic memory with malloc() in C.",
                    "When all processes are CPU-bound and execute without system calls."
                ],
                "correctAnswer": "When executing loops over large arrays spanning N + 1 pages when only N frames are available in the page pool.",
                "explanation": "When an application repeatedly cycles across N+1 pages in an N-page pool, every single page access targets the least recently used page that was just evicted, causing a 100% page fault miss rate."
            },
            {
                "question": "What happens when a page fault occurs in an operating system?",
                "options": [
                    "The MMU traps to the OS kernel, which locates the missing page in secondary storage, selects a frame (evicting one if full), and loads the page before resuming the faulting instruction.",
                    "The running process is immediately killed with a SIGSEGV signal.",
                    "The CPU flushes all L1 cache and reboots the machine into single-user mode.",
                    "The disk controller writes the entire contents of RAM to the swap partition."
                ],
                "correctAnswer": "The MMU traps to the OS kernel, which locates the missing page in secondary storage, selects a frame (evicting one if full), and loads the page before resuming the faulting instruction.",
                "explanation": "A page fault is a hardware interrupt indicating the requested virtual page is not present in physical RAM; the OS fetches it from backing store, updates the page table, and restarts the instruction."
            }
        ],
        "flashcards": [
            {
                "question": "What is the replacement criterion for the FIFO page replacement algorithm?",
                "answer": "The page that was brought into memory earliest (the oldest page in the frame queue) is selected for eviction."
            },
            {
                "question": "What is the replacement criterion for the LRU page replacement algorithm?",
                "answer": "The page that has not been referenced for the longest period of time is selected for eviction."
            },
            {
                "question": "Why is pure LRU rarely implemented strictly in hardware/operating systems?",
                "answer": "It imposes significant overhead, requiring either updating a linked list on every single memory reference or tracking high-resolution 64-bit hardware timestamps for every page."
            },
            {
                "question": "What is a 'reference string' in page replacement studies?",
                "answer": "An ordered sequence of memory page numbers accessed by a running program over time (e.g., 0 1 2 3 0 1 4 0 1 2 3 4)."
            }
        ]
    },
    {
        "order": 11,
        "title": "Lab 11: Execute the Simulation of First Fit and Best Fit Memory Allocation Algorithms",
        "codeSnippet": "// C implementation of First-Fit Memory Allocation Algorithm\n#include <stdio.h>\n\nvoid firstFit(int blockSize[], int m, int processSize[], int n)\n{\n    int i, j;\n    int allocation[n];\n\n    for(i = 0; i < n; i++)\n        allocation[i] = -1;\n\n    for (i = 0; i < n; i++)\n    {\n        for (j = 0; j < m; j++)\n        {\n            if (blockSize[j] >= processSize[i])\n            {\n                allocation[i] = j;\n                blockSize[j] -= processSize[i];\n                break;\n            }\n        }\n    }\n\n    printf(\"\\nProcess No.\\tProcess Size\\tBlock no.\\n\");\n    for (int i = 0; i < n; i++)\n    {\n        printf(\" %i\\t\\t%i\\t\\t\", i + 1, processSize[i]);\n        if (allocation[i] != -1)\n            printf(\"%i\", allocation[i] + 1);\n        else\n            printf(\"Not Allocated\");\n        printf(\"\\n\");\n    }\n}\n\nint main()\n{\n    int blockSize[] = {100, 500, 200, 300, 600};\n    int processSize[] = {212, 417, 112, 426};\n    int m = sizeof(blockSize) / sizeof(blockSize[0]);\n    int n = sizeof(processSize) / sizeof(processSize[0]);\n\n    firstFit(blockSize, m, processSize, n);\n    return 0;\n}",
        "content": "# Lab#11\n\n## EXECUTE THE SIMULATION OF FIRST FIT AND BEST FIT MEMORY ALLOCATION ALGORITHMS.\n\n### Objective\n* Simulation of First Fit and Best Fit Memory Allocation Algorithms\n\n### Theory Overview\n\n#### Partition Allocation Methods in Memory Management\nIn the operating system, the following are four common memory management techniques:\n\n* **Single contiguous allocation:** Simplest allocation method used by MS-DOS. All memory (except some reserved for OS) is available to a process.\n* **Partitioned allocation:** Memory is divided into different blocks or partitions. Each process is allocated according to the requirement.\n* **Paged memory management:** Memory is divided into fixed-sized units called page frames, used in a virtual memory environment.\n* **Segmented memory management:** Memory is divided into different segments (a segment is a logical grouping of the process’ data or code). In this management, allocated memory doesn’t have to be contiguous.\n\nMost of the operating systems (for example Windows and Linux) use **Segmentation with Paging**. A process is divided into segments and individual segments have pages.\n\nIn Partition Allocation, when there is more than one partition freely available to accommodate a process’s request, a partition must be selected. To choose a particular partition, a partition allocation method is needed. A partition allocation method is considered better if it avoids internal fragmentation.\n\nWhen it is time to load a process into the main memory and if there is more than one free block of memory of sufficient size then the OS decides which free block to allocate.\n\nThere are different Placement Algorithms:\n\n* **A. First Fit**\n* **B. Best Fit**\n* **C. Worst Fit**\n* **D. Next Fit**\n\n---\n\n### Placement Algorithms:\n\n#### 1. First Fit\nIn the first fit, the partition is allocated which is the first sufficient block from the top of Main Memory. It scans memory from the beginning and chooses the first available block that is large enough. Thus it allocates the first hole that is large enough.\n\n![First Fit Strategy](assets/images/university/os/lab11_first_fit.png)\n\n#### 2. Best Fit\nAllocate the process to the partition which is the first smallest sufficient partition among the free available partition. It searches the entire list of holes to find the smallest hole whose size is greater than or equal to the size of the process.\n\n![Best Fit Strategy](assets/images/university/os/lab11_best_fit.png)\n\n#### 3. Worst Fit\nAllocate the process to the partition which is the largest sufficient among the freely available partitions available in the main memory. It is opposite to the best-fit algorithm. It searches the entire list of holes to find the largest hole and allocate it to process.\n\n![Worst Fit Strategy](assets/images/university/os/lab11_worst_fit.png)\n\n#### 4. Next Fit\nNext fit is similar to the first fit but it will search for the first sufficient partition from the last allocation point.\n\n![Memory Allocation](assets/images/university/os/lab11_memory_allocation.png)\n\n---\n\n### Is Best-Fit really best?\nAlthough best fit minimizes the wastage space, it consumes a lot of processor time for searching the block which is close to the required size. Also, Best-fit may perform poorer than other algorithms in some cases.\n\nIn the first fit, the partition is allocated which is first sufficient from the top of Main Memory.\n\n#### Example:\n**Input:**  \n```text\nblockSize[]   = {100, 500, 200, 300, 600};\nprocessSize[] = {212, 417, 112, 426};\n```\n\n**Output:**  \n```text\nProcess No.    Process Size    Block no.\n   1                212             2\n   2                417             5\n   3                112             2\n   4                426         Not Allocated\n```\n\n* Its advantage is that it is the fastest search as it searches only the first block that is enough to assign a process.\n* It may have problems of not allowing processes to take space even if it was possible to allocate. Consider the above example, process number 4 (of size 426) does not get memory. However it was possible to allocate memory if we had allocated using best fit allocation [block number 4 (of size 300) to process 1, block number 2 to process 2, block number 3 to process 3 and block number 5 to process 4].\n\n---\n\n### Implementation:\n1. Input memory blocks with size and processes with size.\n2. Initialize all memory blocks as free.\n3. Start by picking each process and check if it can be assigned to current block.\n4. If `size-of-process <= size-of-block` if yes then assign and check for next process.\n5. If not then keep checking the further blocks.\n\nBelow is an implementation of above steps:\n\n```c\n// C implementation of First - Fit algorithm\n#include<stdio.h>\n\n// Function to allocate memory to\n// blocks as per First fit algorithm\nvoid firstFit(int blockSize[], int m, int processSize[], int n)\n{\n    int i, j;\n    // Stores block id of the\n    // block allocated to a process\n    int allocation[n];\n\n    // Initially no block is assigned to any process\n    for(i = 0; i < n; i++)\n    {\n        allocation[i] = -1;\n    }\n\n    // pick each process and find suitable blocks\n    // according to its size ad assign to it\n    for (i = 0; i < n; i++)        //here, n -> number of processes\n    {\n        for (j = 0; j < m; j++)        //here, m -> number of blocks\n        {\n            if (blockSize[j] >= processSize[i])\n            {\n                // allocating block j to the ith process\n                allocation[i] = j;\n\n                // Reduce available memory in this block.\n                blockSize[j] -= processSize[i];\n\n                break;    //go to the next process in the queue\n            }\n        }\n    }\n\n    printf(\"\\nProcess No.\\tProcess Size\\tBlock no.\\n\");\n    for (int i = 0; i < n; i++)\n    {\n        printf(\" %i\\t\\t\\t\", i+1);\n        printf(\"%i\\t\\t\\t\\t\", processSize[i]);\n        if (allocation[i] != -1)\n            printf(\"%i\", allocation[i] + 1);\n        else\n            printf(\"Not Allocated\");\n        printf(\"\\n\");\n    }\n}\n\n// Driver code\nint main()\n{\n    int m;    //number of blocks in the memory\n    int n;    //number of processes in the input queue\n    int blockSize[] = {100, 500, 200, 300, 600};\n    int processSize[] = {212, 417, 112, 426};\n    m = sizeof(blockSize) / sizeof(blockSize[0]);\n    n = sizeof(processSize) / sizeof(processSize[0]);\n\n    firstFit(blockSize, m, processSize, n);\n\n    return 0;\n}\n```\n\nCompile and run the program using the same procedure as given in the previous lab.\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. Simulate **BEST FIT** memory allocation algorithm in C.\n\n**Input:**\n```text\nblockSize[]   = {100, 500, 200, 300, 600};\nprocessSize[] = {212, 417, 112, 426};\n```\n\n**Expected Output:**\n```text\nProcess No.     Process Size    Block no.\n1               212             4\n2               417             2\n3               112             3\n4               426             5\n```\n",
        "quizzes": [
            {
                "question": "How does the First Fit memory allocation algorithm select a memory block for an incoming process?",
                "options": [
                    "It scans memory from the beginning and allocates the first available block (hole) that is large enough.",
                    "It scans all blocks and picks the smallest block that is large enough.",
                    "It searches for the absolute largest hole in physical memory to minimize internal fragmentation.",
                    "It selects memory pseudo-randomly to balance wear across DRAM banks."
                ],
                "correctAnswer": "It scans memory from the beginning and allocates the first available block (hole) that is large enough.",
                "explanation": "First Fit allocates the first hole that is large enough by scanning the block list from the beginning of memory."
            },
            {
                "question": "What is the primary drawback of the Best Fit memory allocation algorithm?",
                "options": [
                    "It produces tiny leftover holes (external fragmentation) that are usually too small to satisfy future requests, and incurs search overhead by scanning all blocks.",
                    "It always leaves the largest remaining partition unused.",
                    "It cannot be implemented without specialized virtual memory paging hardware.",
                    "It requires strictly powers of 2 for memory partition sizes."
                ],
                "correctAnswer": "It produces tiny leftover holes (external fragmentation) that are usually too small to satisfy future requests, and incurs search overhead by scanning all blocks.",
                "explanation": "Best Fit searches the entire list to find the tightest fit; this generates many tiny slivers of unused memory that remain unallocatable, plus higher CPU search time."
            },
            {
                "question": "What is the key difference between internal fragmentation and external fragmentation?",
                "options": [
                    "Internal fragmentation is unused space within an allocated partition; external fragmentation occurs when total free space is sufficient but divided into non-contiguous fragments.",
                    "Internal fragmentation occurs only in swap files on disk; external fragmentation occurs in CPU registers.",
                    "External fragmentation is fixed by increasing the clock frequency, while internal fragmentation requires rebooting.",
                    "Internal fragmentation only affects 64-bit systems, while external fragmentation affects 32-bit systems."
                ],
                "correctAnswer": "Internal fragmentation is unused space within an allocated partition; external fragmentation occurs when total free space is sufficient but divided into non-contiguous fragments.",
                "explanation": "Internal fragmentation occurs when allocated storage is larger than requested storage; external fragmentation occurs when free memory is broken into small non-contiguous pieces."
            },
            {
                "question": "How does the Next Fit memory allocation strategy differ from First Fit?",
                "options": [
                    "Next Fit begins searching for the next suitable hole starting from the location of the last allocation rather than from the beginning of memory.",
                    "Next Fit allocates the next process into the swap partition before checking RAM.",
                    "Next Fit searches from the end of memory backward toward address 0.",
                    "Next Fit only allocates blocks that are exactly equal to the process size."
                ],
                "correctAnswer": "Next Fit begins searching for the next suitable hole starting from the location of the last allocation rather than from the beginning of memory.",
                "explanation": "Next Fit is a variant of First Fit that resumes searching from where the previous allocation occurred, distributing allocations more evenly across memory."
            }
        ],
        "flashcards": [
            {
                "question": "What is the Worst Fit memory allocation strategy?",
                "answer": "It allocates the largest available partition in memory to the process, leaving the largest leftover hole."
            },
            {
                "question": "Which memory management scheme combines segmentation and paging in modern Linux and Windows?",
                "answer": "Segmentation with Paging: programs are logically divided into segments, and each segment is subdivided into fixed-size pages."
            },
            {
                "question": "Between First Fit and Best Fit, which algorithm generally provides the fastest allocation search time?",
                "answer": "First Fit, because it terminates searching as soon as it finds the first partition that accommodates the process."
            },
            {
                "question": "What technique can an OS use to eliminate external fragmentation in partitioned memory?",
                "answer": "Compaction (or defragmentation), which relocates all allocated memory partitions to one end of memory to merge free holes into one large contiguous block."
            }
        ]
    },
    {
        "order": 12,
        "title": "Lab 12: Demonstrate the Solution of Bounded Buffer Producer-Consumer Problem Using Semaphore",
        "codeSnippet": "// C implementation of Bounded Buffer Producer-Consumer using Semaphore\n#include <stdio.h>\n#include <stdlib.h>\n\nint mutex = 1;\nint full = 0;\nint empty = 10, x = 0;\n\nvoid producer()\n{\n    --mutex;\n    ++full;\n    --empty;\n    x++;\n    printf(\"\\nProducer produces item %d\", x);\n    ++mutex;\n}\n\nvoid consumer()\n{\n    --mutex;\n    --full;\n    ++empty;\n    printf(\"\\nConsumer consumes item %d\", x);\n    x--;\n    ++mutex;\n}\n\nint main()\n{\n    int n, i;\n    printf(\"\\n1. Press 1 for Producer\"\n           \"\\n2. Press 2 for Consumer\"\n           \"\\n3. Press 3 for Exit\\n\");\n\n    for (i = 1; i > 0; i++) {\n        printf(\"\\nEnter your choice: \");\n        scanf(\"%d\", &n);\n\n        switch (n) {\n        case 1:\n            if ((mutex == 1) && (empty != 0)) {\n                producer();\n            } else {\n                printf(\"Buffer is full!\");\n            }\n            break;\n\n        case 2:\n            if ((mutex == 1) && (full != 0)) {\n                consumer();\n            } else {\n                printf(\"Buffer is empty!\");\n            }\n            break;\n\n        case 3:\n            exit(0);\n            break;\n        }\n    }\n    return 0;\n}",
        "content": "# Lab#12\n\n## DEMONSTRATE THE SOLUTION OF BOUNDED BUFFER PRODUCER-CONSUMER PROBLEM USING SEMAPHORE.\n\n### Objective\n* Bounded Buffer Producer Consumer Problem using Semaphore\n\n### Theory Overview\n\n#### Producer Consumer Problem:\nConcurrency is an important topic in concurrent programming since it allows us to completely understand how the systems work. Among the several challenges faced by practitioners working with these systems, there is a major synchronization issue which is the producer-consumer problem. In this article, we will discuss this problem and look at possible solutions based on C programming.\n\n#### What is the Producer-Consumer Problem?\nThe producer-consumer problem is an example of a multi-process synchronization problem. The problem describes two processes, the producer and the consumer that share a common fixed-size buffer and use it as a queue.\n\nThe producer’s job is to generate data, put it into the buffer, and start again.\n\nAt the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time.\n\n#### What is the Actual Problem?\nGiven the common fixed-size buffer, the task is to make sure that the producer can’t add data into the buffer when it is full and the consumer can’t remove data from an empty buffer. Accessing memory buffers should not be allowed to producers and consumers at the same time.\n\n#### Solution of Producer-Consumer Problem\nThe producer is to either go to sleep or discard data if the buffer is full. The next time the consumer removes an item from the buffer, it notifies the producer, who starts to fill the buffer again. In the same manner, the consumer can go to sleep if it finds the buffer to be empty. The next time the producer transfer data into the buffer, it wakes up the sleeping consumer.\n\n---\n\n### What is a Semaphore?\nA semaphore is a synchronization tool used in computing to manage access to shared resources. It works like a signal that allows multiple processes or threads to coordinate their actions. Semaphores use counters to keep track of how many resources are available, ensuring that no two processes can use the same resource at the same time, thus preventing conflicts and ensuring orderly execution.\n\nA semaphore $S$ is an integer variable that can be accessed only through two standard operations: `wait()` and `signal()`. The `wait()` operation reduces the value of the semaphore by 1 and the `signal()` operation increases its value by 1.\n\n```c\nwait(S){\n    while(S <= 0);   // busy waiting\n    S--;\n}\n\nsignal(S){\n    S++;\n}\n```\n\n#### Types of Semaphore:\n* **Binary Semaphore** – This is similar to mutex lock but not the same thing. It can have only two values – 0 and 1. Its value is initialized to 1. It is used to implement the solution of critical section problems with multiple processes.\n* **Counting Semaphore** – Its value can range over an unrestricted domain. It is used to control access to a resource that has multiple instances.\n\n---\n\n### C Program for Bounded Buffer Producer-Consumer Problem\n```c\n// C program for the above approach\n#include <stdio.h>\n#include <stdlib.h>\n\n// Initialize a mutex to 1\nint mutex = 1;\n\n// Number of full slots as 0\nint full = 0;\n\n// Number of empty slots as size\n// of buffer\nint empty = 10, x = 0;\n\n// Function to produce an item and\n// add it to the buffer\nvoid producer()\n{\n    // Decrease mutex value by 1\n    --mutex;\n\n    // Increase the number of full\n    // slots by 1\n    ++full;\n\n    // Decrease the number of empty\n    // slots by 1\n    --empty;\n\n    // Item produced\n    x++;\n    printf(\" \\nProducer produces item %d\", x);\n\n    // Increase mutex value by 1\n    ++mutex;\n}\n\n// Function to consume an item and\n// remove it from buffer\nvoid consumer()\n{\n    // Decrease mutex value by 1\n    --mutex;\n\n    // Decrease the number of full\n    // slots by 1\n    --full;\n\n    // Increase the number of empty\n    // slots by 1\n    ++empty;\n    printf(\" \\nConsumer consumes item %d\", x);\n    x--;\n\n    // Increase mutex value by 1\n    ++mutex;\n}\n\n// Driver Code\nint main()\n{\n    int n, i;\n    printf(\" \\n1. Press 1 for Producer\"\n           \"\\n2. Press 2 for Consumer\"\n           \"\\n3. Press 3 for Exit\");\n\n// Using '#pragma omp parallel for'\n// can give wrong value due to\n// synchronization issues.\n\n// 'critical' specifies that code is\n// executed by only one thread at a\n// time i.e., only one thread enters\n// the critical section at a given time\n#pragma omp critical\n\n    for (i = 1; i > 0; i++) {\n\n        printf(\" \\nEnter your choice:\");\n        scanf(\"%d\", &n);\n\n        // Switch Cases\n        switch (n) {\n        case 1:\n\n            // If mutex is 1 and empty\n            // is non-zero, then it is\n            // possible to produce\n            if ((mutex == 1)\n                && (empty != 0)) {\n                producer();\n            }\n\n            // Otherwise, print buffer is full\n            else {\n                printf(\"Buffer is full!\");\n            }\n            break;\n\n        case 2:\n\n            // If mutex is 1 and full\n            // is non-zero, then it is\n            // possible to consume\n            if ((mutex == 1)\n                && (full != 0)) {\n                consumer();\n            }\n\n            // Otherwise, print Buffer is empty\n            else {\n                printf(\"Buffer is empty!\");\n            }\n            break;\n\n        // Exit Condition\n        case 3:\n            exit(0);\n            break;\n        }\n    }\n}\n```\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. How do semaphores solve the Producer-Consumer problem?\n2. What happens if the buffer is full?\n3. What happens if the buffer is empty?\n4. Are there other methods to solve the Producer-Consumer problem?\n",
        "quizzes": [
            {
                "question": "In the Producer-Consumer bounded-buffer problem, what do the three semaphores (mutex, empty, full) represent?",
                "options": [
                    "mutex provides mutual exclusion for buffer access; empty tracks vacant buffer slots; full tracks occupied buffer slots.",
                    "mutex manages disk I/O; empty tracks network sockets; full tracks CPU cache usage.",
                    "mutex limits the number of threads; empty kills idle processes; full triggers kernel recompilation.",
                    "All three are binary flags used exclusively by the compiler preprocessor."
                ],
                "correctAnswer": "mutex provides mutual exclusion for buffer access; empty tracks vacant buffer slots; full tracks occupied buffer slots.",
                "explanation": "In classic bounded buffer synchronization: 'mutex' (binary semaphore) ensures only one process manipulates the buffer at once, 'empty' (counting semaphore initialized to N) counts free slots, and 'full' (counting semaphore initialized to 0) counts available items."
            },
            {
                "question": "What happens if a producer attempts to insert an item when the buffer is completely full?",
                "options": [
                    "The producer is blocked on wait(empty) until a consumer consumes an item and executes signal(empty).",
                    "The buffer overflows and overwrites the OS kernel space.",
                    "The oldest item is silently overwritten without notifying the consumer.",
                    "The operating system terminates both processes immediately."
                ],
                "correctAnswer": "The producer is blocked on wait(empty) until a consumer consumes an item and executes signal(empty).",
                "explanation": "When the buffer is full, empty = 0. The producer calls wait(empty) and is put to sleep until a consumer removes an item, freeing a slot and signaling the producer."
            },
            {
                "question": "What is the key architectural difference between a binary semaphore and a counting semaphore?",
                "options": [
                    "A binary semaphore takes values strictly in {0, 1}, whereas a counting semaphore takes non-negative integer values over an unrestricted domain.",
                    "A binary semaphore can only be used by root, while counting semaphores can be used by standard users.",
                    "Binary semaphores operate only in hardware registers, whereas counting semaphores are stored on disk.",
                    "Binary semaphores do not support signal() operations."
                ],
                "correctAnswer": "A binary semaphore takes values strictly in {0, 1}, whereas a counting semaphore takes non-negative integer values over an unrestricted domain.",
                "explanation": "Binary semaphores are restricted to 0 and 1 (acting as mutual exclusion locks), while counting semaphores can take any non-negative integer value to control access to finite resource pools."
            },
            {
                "question": "What is 'busy waiting' in the context of primitive semaphore implementations?",
                "options": [
                    "A process continuously tests a condition in a loop (spin-lock) while waiting, consuming CPU cycles without performing useful work.",
                    "A process waiting in a blocked queue while the CPU is powered down.",
                    "A high-priority process executing background compression.",
                    "An interrupt handler servicing disk read requests."
                ],
                "correctAnswer": "A process continuously tests a condition in a loop (spin-lock) while waiting, consuming CPU cycles without performing useful work.",
                "explanation": "Busy waiting (or spinlocking) occurs when a process sits in a tight loop checking a variable until it changes state, wasting processor time that could be given to other ready processes."
            }
        ],
        "flashcards": [
            {
                "question": "What two atomic operations are defined for a semaphore variable S?",
                "answer": "wait(S) [also known as P(S) or down(S)] and signal(S) [also known as V(S) or up(S)]."
            },
            {
                "question": "What initial value should the 'empty' counting semaphore have for a buffer of size N?",
                "answer": "empty is initialized to N (the total buffer capacity), while 'full' is initialized to 0."
            },
            {
                "question": "Why must the wait operations in producer code follow the order wait(empty) followed by wait(mutex)?",
                "answer": "Reversing them to wait(mutex) followed by wait(empty) can cause a deadlock if the buffer is full, as the producer would hold the mutex while blocked indefinitely waiting for space."
            },
            {
                "question": "What alternative synchronization constructs can solve the Producer-Consumer problem besides semaphores?",
                "answer": "Monitors (with condition variables), message passing (mailboxes/message queues), or channels in languages like Go."
            }
        ]
    },
    {
        "order": 13,
        "title": "Lab 13: Demonstrate the Solution of Classical Dining Philosophers Problem Assuring No Deadlock and No Starvation (Open Ended Lab)",
        "codeSnippet": "// Simulation of Classical Dining Philosophers Problem using Monitors in C++\n#include <iostream>\n#include <pthread.h>\n#include <unistd.h>\nusing namespace std;\n\n#define N 5\n#define THINKING 2\n#define HUNGRY 1\n#define EATING 0\n#define LEFT (phnum + 4) % N\n#define RIGHT (phnum + 1) % N\n\nint phil[N];\n\nclass monitor {\n    int state[N];\n    pthread_cond_t phcond[N];\n    pthread_mutex_t condLock;\n\npublic:\n    void test(int phnum) {\n        if (state[(phnum + 1) % N] != EATING &&\n            state[(phnum + 4) % N] != EATING &&\n            state[phnum] == HUNGRY) {\n            state[phnum] = EATING;\n            pthread_cond_signal(&phcond[phnum]);\n        }\n    }\n\n    void take_fork(int phnum) {\n        pthread_mutex_lock(&condLock);\n        state[phnum] = HUNGRY;\n        test(phnum);\n        if (state[phnum] != EATING) {\n            pthread_cond_wait(&phcond[phnum], &condLock);\n        }\n        cout << \"Philosopher \" << phnum << \" is Eating\" << endl;\n        pthread_mutex_unlock(&condLock);\n    }\n\n    void put_fork(int phnum) {\n        pthread_mutex_lock(&condLock);\n        state[phnum] = THINKING;\n        test(RIGHT);\n        test(LEFT);\n        pthread_mutex_unlock(&condLock);\n    }\n\n    monitor() {\n        for (int i = 0; i < N; i++) state[i] = THINKING;\n        for (int i = 0; i < N; i++) pthread_cond_init(&phcond[i], NULL);\n        pthread_mutex_init(&condLock, NULL);\n    }\n\n    ~monitor() {\n        for (int i = 0; i < N; i++) pthread_cond_destroy(&phcond[i]);\n        pthread_mutex_destroy(&condLock);\n    }\n} phil_object;",
        "content": "# Lab#13\n\n## DEMONSTRATE THE SOLUTION OF CLASSICAL DINING PHILOSOPHERS PROBLEM ASSURING NO DEADLOCK AND NO STARVATION. + (OPEN ENDED LAB)\n\n### Objective\n* Simulation of Classical Dining Philosophers Problem\n\n### Theory Overview\n\n#### Dining Philosophers Problem\nThe Dining Philosopher Problem is a classic synchronization and concurrency problem that deals with resource sharing, deadlock, and starvation in systems where multiple processes require limited resources. In this article, we will discuss the Dining Philosopher Problem in detail along with proper implementation.\n\n#### Problem Statement\nThe Dining Philosopher Problem involves ‘n’ philosophers sitting around a circular table. Each philosopher alternates between two states: thinking and eating. To eat, a philosopher needs two chopsticks, one on their left and one on their right. However, the number of chopsticks is equal to the number of philosophers, and each chopstick is shared between two neighboring philosophers.\n\nThe standard problem considers the value of ‘n’ as 5 i.e. we deal with 5 Philosophers sitting around a circular table.\n\n![Dining Philosophers Setup](assets/images/university/os/lab13_dining_philosophers.png)\n\n#### Constraints and Conditions for the Problem:\n* Every Philosopher needs two forks to eat.\n* Every Philosopher may pick up the forks on the left or right but only one fork at once.\n* Philosophers only eat when they have two forks. We have to design such a protocol i.e. pre and post protocol which ensures that a philosopher only eats if he or she has two forks.\n* Each fork is either clean or dirty.\n\n---\n\n### SOLUTION\nThe correctness properties it needs to satisfy are:\n* **Mutual Exclusion Principle:** No two Philosophers can have the two forks simultaneously.\n* **Free from Deadlock:** Each philosopher can get the chance to eat in a certain finite time.\n* **Free from Starvation:** When few Philosophers are waiting then one gets a chance to eat in a while.\n* **No strict Alternation**\n* **Proper utilization of time**\n\n#### General Algorithm\n```text\nloop forever\n    p1: think\n    p2: preprotocol\n    p3: eat\n    p4: postprotocol\n```\n\n---\n\n### First Attempt (Naive Semaphores)\nWe assume that each philosopher is initialized with its index $i$ and that addition is implicitly modulo 5. Each fork is modeled as a semaphore where wait corresponds to taking a fork and signal corresponds to putting down a fork.\n\n```text\nsemaphore array[0..4] fork ← [1, 1, 1, 1, 1]\nloop forever\n    p1 : think\n    p2 : wait(fork[i])\n    p3 : wait(fork[i + 1])\n    p4 : eat\n    p5 : signal(fork[i])\n    p6 : signal(fork[i + 1])\n```\n\n#### Problem with this solution:\nThis solution may lead to a deadlock under an interleaving that has all the philosophers pick up their left forks before any of them tries to pick up a right fork. In this case, all the Philosophers are waiting for the right fork but no one will execute a single instruction.\n\n---\n\n### Second Attempt (Room Limit Semaphore)\nOne way to tackle the above situation is to limit the number of philosophers entering the room to four. By doing this one of the philosophers will eventually get both the fork and execute all the instruction leading to no deadlock.\n\n```text\nsemaphore array[0..4] fork ← [1, 1, 1, 1, 1]\nsemaphore room ← 4\n\nloop forever\n    p1 : think\n    p2 : wait(room)\n    p3 : wait(fork[i])\n    p4 : wait(fork[i + 1])\n    p5 : eat\n    p6 : signal(fork[i])\n    p7 : signal(fork[i + 1])\n    p8 : signal(room)\n```\n\nIn this solution, we somehow interfere with the given problem as we allow only four philosophers.\n\n---\n\n### Third Attempt (Asymmetric / Chandy-Misra Solution)\nWe use the asymmetric algorithm in the attempt where the first four philosophers execute the original solution but the fifth philosopher waits for the right fork and then for the left fork.\n\n```text\nsemaphore array [0..4] fork ← [1, 1, 1, 1, 1]\n\n// For the first Four Philosophers\nloop forever\n   p1 : think\n   p2 : wait(fork[i])\n   p3 : wait(fork[i + 1])\n   p4 : eat\n   p5 : signal(fork[i])\n   p6 : signal(fork[i + 1])\n\n// For the Fifth Philosopher\nloop forever\n   p1 : think\n   p2 : wait(fork[0])\n   p3 : wait(fork[4])\n   p4 : eat\n   p5 : signal(fork[0])\n   p6 : signal(fork[4])\n```\n\n*Note: This solution is also known as Chandy/Misra Solution.*\n\n#### Advantages of this Solution:\n* Allows a large degree of concurrency\n* Free from Starvation\n* Free from Deadlock\n* More Flexible Solution\n* Economical\n* Fairness\n* Boundedness\n\n---\n\n### Solution with Monitors\nHere, Monitor maintains an array of the fork which counts the number of free forks available to each philosopher. The `takeForks` operation waits on a condition variable until two forks are available. It decrements the number of forks available to its neighbor before leaving the monitor. After eating, a philosopher calls `releaseForks` which updates the array fork and checks if freeing these forks makes it possible to signal.\n\n#### Monitor Algorithm\n```text\nmonitor ForkMonitor:\ninteger array[0..4] fork ← [2, 2, 2, 2, 2]\ncondition array[0..4] OKtoEat\n\noperation takeForks(integer i)\n    if(fork[i] != 2)\n        waitC(OKtoEat[i])\n    fork[i+1] ← fork[i+1] - 1\n    fork[i-1] ← fork[i-1] - 1\n\noperation releaseForks(integer i)\n    fork[i+1] ← fork[i+1] + 1\n    fork[i-1] ← fork[i-1] + 1\n    if(fork[i+1] == 2)\n        signalC(OKtoEat[i+1])\n    if(fork[i-1] == 2)\n        signalC(OKtoEat[i-1])\n\nFor Each Philosopher:\nloop forever:\n    p1 : think\n    p2 : takeForks(i)\n    p3 : eat\n    p4 : releaseForks(i)\n```\n\n---\n\n### Implementation of Dining Philosophers Problem in C++ using Monitors\nHere is the Program for the same using monitors in C++:\n\n```cpp\n// Header file include\n#include <iostream>\n#include <pthread.h>\n#include <unistd.h>\nusing namespace std;\n\n#define N 5\n#define THINKING 2\n#define HUNGRY 1\n#define EATING 0\n#define LEFT (phnum + 4) % N\n#define RIGHT (phnum + 1) % N\n\n// Philosopher index\nint phil[N];\nint times = 200;\n\nclass monitor\n{\n    // state of the philosopher\n    int state[N];\n\n    // Philosopher condition variable\n    pthread_cond_t phcond[N];\n\n    // mutex variable for synchronization\n    pthread_mutex_t condLock;\n\n  public:\n    // Test for the desired condition\n    // i.e. Left and Right philosopher are not eating\n    void test(int phnum)\n    {\n        if (state[(phnum + 1) % 5] != EATING && state[(phnum + 4) % 5] != EATING\n            && state[phnum] == HUNGRY)\n        {\n            state[phnum] = EATING;\n            pthread_cond_signal(&phcond[phnum]);\n        }\n    }\n\n    // Take Fork function\n    void take_fork(int phnum)\n    {\n        pthread_mutex_lock(&condLock);\n\n        // Indicates it is hungry\n        state[phnum] = HUNGRY;\n\n        // test for condition\n        test(phnum);\n\n        // If unable to eat.. wait for the signal\n        if (state[phnum] != EATING)\n        {\n            pthread_cond_wait(&phcond[phnum], &condLock);\n        }\n        cout << \"Philosopher \" << phnum << \" is Eating\" << endl;\n\n        pthread_mutex_unlock(&condLock);\n    }\n\n    // Put Fork function\n    void put_fork(int phnum)\n    {\n        pthread_mutex_lock(&condLock);\n\n        // Indicates that I am thinking\n        state[phnum] = THINKING;\n\n        test(RIGHT);\n        test(LEFT);\n\n        pthread_mutex_unlock(&condLock);\n    }\n\n    // constructor\n    monitor()\n    {\n        for (int i = 0; i < N; i++)\n        {\n            state[i] = THINKING;\n        }\n\n        for (int i = 0; i < N; i++)\n        {\n            pthread_cond_init(&phcond[i], NULL);\n        }\n\n        pthread_mutex_init(&condLock, NULL);\n    }\n\n    // destructor\n    ~monitor()\n    {\n        for (int i = 0; i < N; i++)\n        {\n            pthread_cond_destroy(&phcond[i]);\n        }\n        pthread_mutex_destroy(&condLock);\n    }\n};\n\n// Global Object of the monitor\nmonitor phil_object;\n\nvoid *philosopher(void *arg)\n{\n    int c = 0;\n    while (c < times)\n    {\n        int i = *(int *)arg;\n        sleep(1);\n        phil_object.take_fork(i);\n        sleep(1);\n        phil_object.put_fork(i);\n        c++;\n    }\n    return NULL;\n}\n\nint main()\n{\n    // Declaration...\n    pthread_t thread_id[N];\n    pthread_attr_t attr;\n\n    // Initialization...\n    pthread_attr_init(&attr);\n    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);\n\n    for (int i = 0; i < N; i++)\n    {\n        phil[i] = i;\n    }\n\n    // Creating...\n    for (int i = 0; i < N; i++)\n    {\n        pthread_create(&thread_id[i], &attr, philosopher, &phil[i]);\n        cout << \"Philosopher \" << i + 1 << \" is thinking...\" << endl;\n    }\n\n    // Joining....\n    for (int i = 0; i < N; i++)\n    {\n        pthread_join(thread_id[i], NULL);\n    }\n\n    // Destroying\n    pthread_attr_destroy(&attr);\n    pthread_exit(NULL);\n\n    return 0;\n}\n```\n\n### Conclusion\nThe Dining Philosopher Problem teaches us how to handle shared resources in a system while avoiding issues like deadlock and starvation. It highlights challenges like deadlock and starvation and teaches how to prevent them using proper synchronization techniques. The problem is a classic example used to study synchronization and resource allocation in concurrent systems.\n\n### Tools:\nRed Hat Linux\n\n---\n\n### Lab Tasks:\n1. What is starvation?\n2. Can the problem be solved with just mutexes?\n3. What are the real-world applications of the Dining Philosopher Problem?\n\n### Open Ended Lab:\n1. Make a program of **FCFS (First Come First Served)** CPU Scheduling Algorithm using C.\n",
        "quizzes": [
            {
                "question": "In the naive semaphore solution to the Dining Philosophers problem, what exact condition triggers a deadlock?",
                "options": [
                    "All five philosophers simultaneously pick up their left fork, causing everyone to block indefinitely waiting for their right fork.",
                    "A philosopher eats continuously without ever releasing either fork.",
                    "Two philosophers exchange forks across the table simultaneously.",
                    "The operating system timer interrupt preempts a philosopher during the think() function."
                ],
                "correctAnswer": "All five philosophers simultaneously pick up their left fork, causing everyone to block indefinitely waiting for their right fork.",
                "explanation": "If every philosopher picks up their left fork at the exact same moment, all five forks are held and each philosopher is blocked waiting for their right neighbor to release the fork, creating a circular wait deadlock."
            },
            {
                "question": "How does the Asymmetric (Chandy/Misra) solution eliminate deadlock in the Dining Philosophers problem?",
                "options": [
                    "An odd/even asymmetry breaks the circular wait condition: the first four philosophers pick up left then right, while the fifth picks up right then left.",
                    "It permanently removes one philosopher from the table.",
                    "It replaces all physical chopsticks with an unlimited pool of virtual resources.",
                    "It forces all philosophers to eat strictly in sequential numeric order 0 to 4."
                ],
                "correctAnswer": "An odd/even asymmetry breaks the circular wait condition: the first four philosophers pick up left then right, while the fifth picks up right then left.",
                "explanation": "By having philosopher 4 reverse the acquisition order (picking right fork before left fork), circular wait is impossible, completely preventing deadlock."
            },
            {
                "question": "What is starvation in operating system concurrency?",
                "options": [
                    "A situation where a runnable process or thread is perpetually denied necessary resources despite those resources becoming repeatedly available to others.",
                    "A condition where physical RAM is completely depleted by memory leaks.",
                    "When the CPU fan fails and processor temperature exceeds thermal throttling limits.",
                    "When an operating system kernel exhausts all process identifiers (PIDs)."
                ],
                "correctAnswer": "A situation where a runnable process or thread is perpetually denied necessary resources despite those resources becoming repeatedly available to others.",
                "explanation": "Starvation (indefinite postponement) occurs when a process is ready to run but never allocated the required resources because other processes are continually favored."
            },
            {
                "question": "In the monitor-based solution for the Dining Philosophers problem, when is a philosopher permitted to transition to the EATING state?",
                "options": [
                    "Only when the philosopher is HUNGRY and neither the left nor the right neighbor is in the EATING state.",
                    "Whenever the central timer ticks and grants an eating quantum.",
                    "Whenever at least one fork is clean.",
                    "Whenever the philosopher's process priority is higher than 10."
                ],
                "correctAnswer": "Only when the philosopher is HUNGRY and neither the left nor the right neighbor is in the EATING state.",
                "explanation": "The monitor's test() method checks: 'state[LEFT] != EATING && state[RIGHT] != EATING && state[phnum] == HUNGRY' before setting state to EATING and signaling the condition variable."
            }
        ],
        "flashcards": [
            {
                "question": "What are the four Coffman conditions required for a deadlock to occur?",
                "answer": "1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait."
            },
            {
                "question": "How does limiting room capacity to 4 philosophers prevent deadlock among 5 philosophers?",
                "answer": "With at most 4 philosophers competing for 5 forks, by Pigeonhole Principle at least one philosopher is guaranteed to acquire two forks and eat."
            },
            {
                "question": "What synchronization construct is a 'Monitor'?",
                "answer": "A high-level synchronization abstraction that encapsulates shared data variables with procedures, enforcing automatic mutual exclusion within monitor boundaries."
            },
            {
                "question": "What real-world computing scenarios are modeled by the Dining Philosophers problem?",
                "answer": "Distributed resource allocation, database row locking, bus arbitration, and multithreaded deadlock avoidance in transaction systems."
            }
        ]
    },
    {
        "order": 14,
        "title": "Lab 14: Practice the Installation, Recompilation, and Addition of New Software to the Kernel",
        "codeSnippet": "# Linux Kernel Recompilation and Installation Commands\ncd /usr/src\n# Unpack kernel source\ntar -xvzf linux-x.y.z.tar.gz\n\n# Establish required include symlinks\nln -sf /usr/src/linux/include/linux /usr/include/linux\nln -sf /usr/src/linux/include/asm /usr/include/asm\n\ncd /usr/src/linux\n# Clean old object files and build dependencies\nmake clean\nmake depend\nmake mrproper\n\n# Configure kernel features\nmake config      # or make menuconfig\n\n# Set dependencies and compile compressed kernel image\nmake dep\nmake zImage\nmake zdisk\nmake zlilo\n\n# Backup old kernel and install new kernel image\nmv /vmlinuz /vmlinuz.old\ncp /usr/src/linux/arch/i386/boot/zImage /vmlinuz",
        "content": "# Lab#14\n\n## PRACTICE THE INSTALLATION, RECOMPILATION, AND ADDITION OF NEW SOFTWARE TO THE KERNEL.\n\n### Objective\n* Focusing on the installation, recompilation, and addition of new software to the kernel.\n\n### Theory Overview\nUsually, you will want to leave the kernel alone, except when you are performing a major upgrade or installing a new device driver that has special kernel modifications. The details of the process are usually supplied with the software. However, this lab gives a good idea of the general process.\n\nFew people will want to change the details in the kernel source code, because they lack the knowledge to do so (or have enough knowledge to know that hacking the kernel can severely damage the system). However, most users will want to install new versions of Linux, add patches, or modify the kernel's behavior a little.\n\n> **Note:** Don't modify the kernel unless you know what you are doing. If you damage the source code, your kernel may be unusable —and in the worst cases, your file system may be affected. Take care and follow instructions carefully. You need to know several things about kernel manipulation, and this lab looks at only the basics.\n\nSeveral versions of Linux are commonly used, with a few inconsistencies between them. For that reason, the exact instructions given here may not work with your version of Linux. However, the general approach is the same, and only the directory or utility names may be different. Most versions of Linux supply documentation that lists the recompilation process and the locations of the source code and compiled programs.\n\nBefore you do anything with the kernel or utilities, make sure you have a good set of emergency boot disks, and preferably, a complete backup on tape or diskette. Although the process of modifying the kernel is not difficult, every now and then it does cause problems that can leave you stranded without a working system. Boot disks are the best way to recover, so make at least one extra set.\n\n---\n\n### Upgrading and Installing New Kernel Software\nLinux is a dynamic operating system. New releases of the kernel, or parts of the operating system that can be linked into the kernel, are made available at regular intervals to users. Whether or not you want to upgrade to the new releases is up to you and usually depends on the features or bug fixes that the new release offers. You will probably have to recompile and relink the kernel when new software is added, unless it is loaded as a utility or device driver.\n\nYou should avoid upgrading your system with every new release, for a couple of reasons:\n* The most common problem with constant upgrades is that you may be stuck with a new software package that causes backward compatibility problems with your existing system or that has a major problem with it that was not patched before the new software was released. This can cause you no end of trouble.\n* Most new software releases wipe out existing configuration information, so you have to reconfigure the packages that are being installed from scratch.\n* Another problem with constant upgrades is that the frequency with which new releases are made available is so high that you can probably spend more time simply loading and recompiling kernels and utilities than actually using the system. This becomes tiresome after a while. Because most major releases of the Linux operating system are available, the number of changes to the system is usually quite small. Therefore, you should read the release notes carefully to ensure that the release is worth the installation time and trouble.\n\nThe best advice is to upgrade only once or twice a year, and only when there is a new feature or enhancement to your system that will make a significant difference in the way you use Linux. It's tempting to always have the latest and newest versions of the operating system, but there is a lot to be said for having a stable, functioning operating system.\n\nIf you do upgrade to a new release, bear in mind that you don't have to upgrade everything. The last few Linux releases have changed only about five percent of the operating system with each new major package upgrade. Instead of replacing the entire system, just install those parts that will have a definite effect, such as the kernel, compilers and their libraries, and frequently used utilities. This saves time and reconfiguration.\n\n---\n\n### Compiling the Kernel from Source Code\nUpgrading, replacing, or adding new code to the kernel is usually a simple process: you obtain the source for the kernel, make any configuration changes, compile it, and then place it in the proper location on the file system to run the system properly. The process is often automated by a shell script or installation program, and some upgrades are completely automated —you don't need to do anything except start the upgrade utility.\n\nKernel sources for new releases of Linux are available from CD-ROM distributions, FTP sites, user groups, and many other locations. Most kernel versions are numbered with a version and a patch level, so you will see kernel names such as 1.12.123, where 1 is the major release, 12 is the minor version release, and 123 is the patch number. Most sites of kernel source code maintain several versions simultaneously, so check through the source directories for the latest version of the kernel.\n\nPatch releases are sometimes numbered differently and do not require the entire source of the kernel to install. They just require the source of the patch. In most cases, the patch overlays a section of existing source code, and a simple recompilation is all that's necessary to install the patch. Patches are released quite frequently.\n\nMost kernel source programs are maintained as a gzipped tar file. Unpack the files into a subdirectory called `/usr/src`, which is where most of the source code is kept for Linux. Some versions of Linux keep other directories for the kernel source, so you may want to check any documentation supplied with the system or look for a README file in one of the three `/usr/src` subdirectories: `linux`, `linux-1.2.13`, or `redhat` for more instructions.\n\nOften, unpacking the gzipped tar file in `/usr/src` creates a subdirectory called `/usr/src/linux`, which can overwrite your last version of the kernel source. Before starting the unpacking process, rename or copy any existing `/usr/src/linux` (or whatever name is used with the new kernel) so you have a backup version in case of problems.\n\n---\n\n### Establishing Symbolic Links\nAfter the kernel source has been unpacked, you need to create two symbolic links to the `/usr/include` directory, if they are not created already or set by the installation procedure. Usually, the link commands required are:\n\n```bash\nln -sf /usr/src/linux/include/linux /usr/include/linux\nln -sf /usr/src/linux/include/asm /usr/include/asm\n```\n\nIf the directory names shown are different from your version of Linux, substitute the new directory names for `/usr/src/linux`. Without these links, the upgrade or installation of a new kernel cannot proceed.\n\nAfter the source code has been ungzipped and untarred and the links have been established, the compilation process can begin. You must have a version of gcc or g++ (the GNU C and C++ compilers) or some other compatible compiler available for the compilation. You may have to check with the source-code documentation to make sure you have the correct versions of the compilers; occasionally, new kernel features are added that are not supported by older versions of gcc or g++.\n\n---\n\n### Checking Makefile & Cleaning\nCheck the file `/usr/src/linux/Makefile` (or whatever path the Makefile is in with your source distribution). There will be a line in the file that defined the `ROOT_DEV`, which is the device that is used as the root file system when Linux boots. Usually the line looks like this:\n\n```makefile\nROOT_DEV = CURRENT\n```\n\nIf you have any other value, make sure it is correct for your file-system configuration. If the Makefile has no value, set it as shown in the preceding code line.\n\nIt's a good idea to run `make clean; make depend; make mrproper` before rebuilding the kernel to make sure all old files are removed.\n\n---\n\n### Step-by-Step Kernel Recompilation Procedure\n\n#### 1. Configuration\nThe compilation process begins when you change to the `/usr/src/linux` directory and issue the following command:\n\n```bash\nmake config\n```\n\nThis command invokes the make utility for the C compiler. The process may be slightly different for some versions of Linux, so you should check with any release or installation notes supplied with the source code.\n\n> **Note:** Be sure that you are running either `/bin/bash` or `/bin/sh` before you run make. Running another shell such as `tcsh` may cause you problems with the make files.\n\nThe config program issues a series of questions and prompts that you need to answer to indicate any configuration issues that need to be completed before the actual compilation begins. These may be about the type of disk drive you are using, the CPU, any partitions, or other devices, such as CD-ROMs. Answer the questions as well as you can. If you are unsure, choose the default values or the choice that makes the most sense. The worst case is that you might have to redo the process if the system doesn't run properly. (You do have an emergency boot disk ready, don't you?)\n\n#### 2. Setting Dependencies\nNext, you have to set all the source dependencies. This is a step that is commonly skipped, and it can cause several problems if it is not performed for each software release. Issue the command:\n\n```bash\nmake dep\n```\n\nIf the software you are installing does not have a dep file, check with the release or installation notes to ensure that the dependencies are correctly handled by the other steps.\n\n#### 3. Building the Kernel Image\nAfter that, you can finally compile the new kernel. The command to start the process is:\n\n```bash\nmake zImage\nmake zdisk\nmake zlilo\n```\n\nThis compiles the source code and leaves the new kernel image file in the current directory (usually `/usr/src/linux`). The `make zdisk` is really necessary for creating a boot disk, and therefore expects a blank, unformatted disk in the floppy drive and will ask you for one as it runs. Not all releases or upgrades to the kernel support compressed image compilation.\n\n#### 4. Installing the Kernel Image\nThe last step in the process is to copy the new kernel image file to the boot device or a boot floppy. Use the following command to place the file on a floppy:\n\n```bash\ncp Image /dev/fd0\n```\n\nTo be safe, copy the old kernel to a known image and then copy the newly created image to the root. This would be accomplished with these two commands:\n\n```bash\nmv /vmlinuz /vmlinuz.old\ncp /usr/src/linux/arch/i386/boot/zImage /vmlinuz\n```\n\nNow all that remains is to reboot the system and see if the new kernel loads properly. If there are any problems, boot from a floppy, restore the old kernel, and start the process again. Check the documentation supplied with the release source code for any information about problems you may encounter or steps that may have been added to the process.\n\n### Tools:\nRed Hat Linux\n",
        "quizzes": [
            {
                "question": "Where is the standard Linux kernel source tree conventionally located on the file system?",
                "options": [
                    "/usr/src/linux",
                    "/etc/kernel",
                    "/bin/vmlinuz",
                    "/var/log/kernel"
                ],
                "correctAnswer": "/usr/src/linux",
                "explanation": "Standard Linux distributions maintain the kernel source trees under `/usr/src/` (typically `/usr/src/linux` or versioned `/usr/src/linux-x.y.z`)."
            },
            {
                "question": "Why must symbolic links for 'linux' and 'asm' be created in /usr/include before compiling the kernel?",
                "options": [
                    "So that compiler header file directives (<linux/...> and <asm/...>) reference the exact kernel source headers and target architecture definitions.",
                    "To grant standard non-root users write access to the kernel binaries.",
                    "To enable dynamic runtime loading of Perl scripts in the BIOS.",
                    "To compress the kernel into a zImage archive during linking."
                ],
                "correctAnswer": "So that compiler header file directives (<linux/...> and <asm/...>) reference the exact kernel source headers and target architecture definitions.",
                "explanation": "The C compiler expects standard header paths `/usr/include/linux` and `/usr/include/asm` to point to the active kernel include trees in `/usr/src/linux/include`."
            },
            {
                "question": "What is the purpose of running 'make mrproper' in the Linux kernel source directory?",
                "options": [
                    "It thoroughly cleans the source tree, removing all old configuration files (.config), dependencies, and temporary object files from previous builds.",
                    "It automatically downloads the latest Linux kernel patch from kernel.org.",
                    "It installs the GRUB or LILO bootloader into the Master Boot Record.",
                    "It verifies that all user passwords meet security complexity standards."
                ],
                "correctAnswer": "It thoroughly cleans the source tree, removing all old configuration files (.config), dependencies, and temporary object files from previous builds.",
                "explanation": "'make mrproper' ensures a pristine, uncontaminated build environment by erasing existing configuration (.config) and all stale object files before rebuilding."
            },
            {
                "question": "Why is it critical to backup '/vmlinuz' to '/vmlinuz.old' before copying a newly compiled zImage to the root partition?",
                "options": [
                    "If the newly built kernel fails to boot or encounters panic on hardware detection, the system administrator can still boot the known working fallback kernel.",
                    "Because Linux only allows one file to exist in the root directory at any given time.",
                    "The compiler fails with an error if '/vmlinuz.old' does not exist.",
                    "To clear swap space for the second stage bootloader."
                ],
                "correctAnswer": "If the newly built kernel fails to boot or encounters panic on hardware detection, the system administrator can still boot the known working fallback kernel.",
                "explanation": "Backing up `/vmlinuz` to `/vmlinuz.old` preserves a stable, bootable kernel image that can be loaded from the bootloader (LILO/GRUB) or rescue disk if the new kernel crashes."
            }
        ],
        "flashcards": [
            {
                "question": "What does the command 'make zImage' produce?",
                "answer": "It builds a compressed Linux kernel executable image, typically stored at arch/<arch>/boot/zImage."
            },
            {
                "question": "What command generates kernel header source dependencies before compilation?",
                "answer": "make dep"
            },
            {
                "question": "What setting in the kernel Makefile specifies the root filesystem partition used when Linux boots?",
                "answer": "ROOT_DEV (e.g., ROOT_DEV = CURRENT)."
            },
            {
                "question": "Which shells should be used when executing Linux kernel build makefiles?",
                "answer": "/bin/bash or /bin/sh (alternative shells like tcsh can cause syntax incompatibilities with kernel makefiles)."
            }
        ]
    }
]

def seed_os_curriculum(db_client: Optional[Prisma] = None, verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds the Operating Systems (CS-223L) curriculum (Labs 1 to 14) into Neon PostgreSQL via Prisma.
    Strictly idempotent and non-destructive: only touches the OS course and its steps.
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
            print(f"[*] Cleared previous records for OS course: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

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
                "title": lab["title"][:50],
                "quizzes_count": len(lab["quizzes"]),
                "flashcards_count": len(lab["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 85)
            print("SUMMARY TABLE: UNIVERSITY OS (CS-223L) LABS 1 TO 14 SEEDED SUCCESSFULLY")
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
    seed_os_curriculum()
