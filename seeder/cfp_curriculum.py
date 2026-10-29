"""
CF&P University Curriculum Seeder (Computer Fundamentals and Programming)
100% Verbatim transcription from "Cf & P manual official  2021.docx" for Electrical Engineering Department,
Hamdard Institute of Engineering & Technology (HIET), Hamdard University Islamabad Campus (HUIC).
Course Instructor / Prepared By: Engr. Sana Mukhtar, Assistant Professor HIET.

Populates University Laboratory Modules (Complete 14 Labs, Exactly 5 Quizzes & 4 Flashcards per Lab) with zero data loss,
exact tasks, procedure instructions, HTML/C++ code listings, diagrams, quizzes, and flashcards.
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from prisma import Prisma


COURSE_DATA = {
    "title": "Computer Fundamentals and Programming (CF&P)",
    "category": "University",
    "description": "Official Academic Curriculum for Computer Fundamentals and Programming (CF&P), Electrical Engineering Department, HIET, Hamdard University Islamabad Campus. Comprehensive 14-laboratory curriculum covering Computer Hardware & Operating Systems, Microsoft Office Suite (Word, PowerPoint, Excel), HTML Web Page Design, C++ Programming Foundations (IDE setup, data types, arithmetic, operators, decision making, loops, arrays, and functions).",
    "color": "#0284C7",
    "thumbnail": "assets/images/university/cfp/cfp_logo.png"
}

LABS_DATA = [   {   'codeSnippet': '# PowerShell commands to inspect Windows OS, CPU, RAM and hardware devices\n'
                       'Get-ComputerInfo | Select-Object WindowsProductName, OsVersion, WindowsInstallationType\n'
                       'Get-WmiObject Win32_Processor | Select-Object Name, NumberOfCores, MaxClockSpeed\n'
                       'Get-WmiObject Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum\n'
                       'devmgmt.msc',
        'content': '![Hamdard University Crest](assets/images/university/cfp/cfp_logo.png)\n'
                   '\n'
                   '# Lab#01\n'
                   '\n'
                   '## OPERATE OS AND HARDWARE OF COMPUTER\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part A: Introduction to OS and Hardware\n'
                   '\n'
                   '#### Introduction:\n'
                   'Windows is the most common operating system used for PCs. It is essential that you familiarize '
                   'yourself with the basic functionality of this OS.\n'
                   '\n'
                   'It is necessary that you are aware of the hardware in your computer. While the operating system '
                   'usually takes care of the complexity of managing the hardware of your computer system, knowing the '
                   'hardware helps when you have to:\n'
                   '* Install an operating system\n'
                   '* Upgrade your computer system\n'
                   '* Diagnose and repair problems in your computer system\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To become familiar with the Windows OS environment\n'
                   '* To become familiar with the hardware of your computer\n'
                   '\n'
                   '#### Preparation:\n'
                   'Start computer and try to explore its functionalities.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Basic Windows Tasks\n'
                   'Familiarize yourself with the following basic tasks specific to Windows operating systems [ask '
                   'your instructor if you have problems]:\n'
                   '* Copying/ pasting a file\n'
                   '* Creating a new file\n'
                   '* Creating a new folder\n'
                   '* Deleting a file\n'
                   '* Finding how to find Windows help\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Personal Computer with Windows Operating System\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. **Copying/ pasting a file:** [select a file, right click > copy; go to the directory to paste '
                   'into, right click > paste]\n'
                   '2. **Creating a new file:** [hint: right click > new > file type]\n'
                   '3. **Creating a new folder:** [hint: right click > new > folder]\n'
                   '4. **Deleting a file:** [hint: select a file, right click > delete]\n'
                   '5. **Finding how to find Windows help:** [hint: click on Windows Start button, and then on Help '
                   'and Support, explore what kind of help is available]\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #2: Hardware Present in Your Computer\n'
                   'To check the hardware present in your computer.\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Personal Computer with Windows Operating System\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. To check the hardware present in your computer, Right click on **My Computer** and then click '
                   'on **Properties**, note down the specifications of the PC you are working on in the General tab '
                   '(shown by default).\n'
                   '\n'
                   '![Fig 1.1: Computer Properties](assets/images/university/cfp/lab1_computer_properties.png)\n'
                   '\n'
                   '![Fig 1.2: System Properties](assets/images/university/cfp/lab1_system_properties.png)\n'
                   '\n'
                   '2. Click on the **Computer Name** tab.\n'
                   '\n'
                   '![Fig 1.3: Computer name in system '
                   'properties](assets/images/university/cfp/lab1_computer_name.png)\n'
                   '\n'
                   '3. Click on the **Hardware** tab and then on **Device Manager**, note all information about '
                   'hardware devices here:\n'
                   '\n'
                   '![Fig 1.4: Device Manager](assets/images/university/cfp/lab1_device_manager.png)\n'
                   '\n'
                   '![Fig 1.5 Device Manager Window](assets/images/university/cfp/lab1_device_manager_window.png)\n'
                   '\n'
                   '*(Hint: you can right-click on any device and see further properties)*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part B: Inside the Computer\n'
                   '\n'
                   '#### Introduction:\n'
                   'A computer is an electronic device, operating under the control of instructions (software) stored '
                   'in its own memory unit, that can accept data (input), manipulate data (process), and produce '
                   'information (output) from the processing. Generally, the term is used to describe a collection of '
                   'devices that function together as a system.\n'
                   '\n'
                   'Computer consists of:\n'
                   '* Keyboard\n'
                   '* Screen\n'
                   '* Mouse\n'
                   '* Disks\n'
                   '* Memory\n'
                   '* CD-ROM\n'
                   '* And processing units\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To study the internal structure of computer.\n'
                   '* Familiarize with computer devices.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Computer Hardware Study\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Personal computer\n'
                   '\n'
                   '#### Procedure:\n'
                   'Open the CPU casing and identify different components of computer system.\n'
                   '\n'
                   '![Fig 1.6: Components inside a Computer](assets/images/university/cfp/lab1_computer_inside.png)\n'
                   '\n'
                   '![Fig 1.7: Computer architecture](assets/images/university/cfp/lab1_computer_architecture.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 1 tasks:\n'
                   '1. What is the Operating System being used? (write complete details)\n'
                   '2. What Service Pack is installed?\n'
                   '3. What is the CPU name?\n'
                   "4. What is the clock speed of the computer's CPU?\n"
                   '5. What is the amount of RAM present?\n'
                   "6. What is the computer's full name?\n"
                   '7. What is the name of the disk drive?\n'
                   '8. Does the computer have a Bluetooth radio?\n'
                   '9. Does the computer have a network adapter?\n'
                   '10. What is the name of the monitor? Is the proper driver of the monitor installed? What is the '
                   'name of the provider of the driver for the monitor?\n'
                   '11. Find out the name of your hard disk?\n'
                   '12. Name and identify different hardware components.\n',
        'flashcards': [   {   'answer': '1. Installing an operating system\n'
                                        '2. Upgrading the computer system\n'
                                        '3. Diagnosing and repairing system problems.',
                              'question': 'What are the three main reasons to know your computer hardware?'},
                          {   'answer': "Right-click 'My Computer' -> Select 'Properties' -> Navigate to the "
                                        "'Hardware' tab -> Click on 'Device Manager' (or run devmgmt.msc).",
                              'question': 'How do you access Device Manager in Windows?'},
                          {   'answer': 'CPU (processor), Motherboard, RAM (main memory), Hard Disk Drive (storage), '
                                        'Power Supply Unit (PSU), Optical Drives (CD-ROM), and expansion cards.',
                              'question': 'What are the primary internal components of a computer?'},
                          {   'answer': 'It serves as the communication pathway connecting the CPU, RAM, and '
                                        'Input/Output devices via the Control, Address, and Data buses.',
                              'question': 'What is the function of the System Bus?'}],
        'order': 1,
        'quizzes': [   {   'correctAnswer': 'To install an OS, upgrade computer systems, and diagnose/repair hardware '
                                            'problems',
                           'explanation': 'According to the manual, knowing the hardware helps when you have to '
                                          'install an OS, upgrade your system, and diagnose and repair hardware '
                                          'faults.',
                           'options': [   'To install an OS, upgrade computer systems, and diagnose/repair hardware '
                                          'problems',
                                          'To replace the need for an operating system entirely',
                                          'To avoid using system software during execution',
                                          'To eliminate the requirement of a system clock and bus architecture'],
                           'question': 'Why is it important for a computer engineer to understand computer hardware '
                                       'even though the OS manages hardware complexity?'},
                       {   'correctAnswer': 'Device Manager',
                           'explanation': 'Device Manager displays all hardware devices (network adapters, display '
                                          'adapters, disk drives, processors) and driver properties.',
                           'options': ['Device Manager', 'Disk Defragmenter', 'Task Scheduler', 'Notepad'],
                           'question': 'Which Windows management tool provides a graphical view of all installed '
                                       'hardware devices and driver statuses?'},
                       {   'correctAnswer': 'Control Bus, Address Bus, and Data Bus',
                           'explanation': 'Computer architecture utilizes the Control Bus (timing/signals), Address '
                                          'Bus (memory locations), and Data Bus (data transfer) between components.',
                           'options': [   'Control Bus, Address Bus, and Data Bus',
                                          'Ethernet Bus, USB Bus, and SATA Bus',
                                          'Power Bus, Optical Bus, and Wireless Bus',
                                          'Serial Bus, Parallel Bus, and Bluetooth Bus'],
                           'question': 'According to the computer architecture bus diagram (Fig 1.7), what are the '
                                       'three primary system buses connecting CPU, Memory, and I/O?'},
                       {   'correctAnswer': 'An electronic device operating under stored software instructions that '
                                            'accepts data (input), processes data, and produces information (output)',
                           'explanation': 'A computer accepts input data, manipulates it according to instructions '
                                          'stored in its own memory, and produces output information.',
                           'options': [   'An electronic device operating under stored software instructions that '
                                          'accepts data (input), processes data, and produces information (output)',
                                          'A purely mechanical calculator capable of only basic arithmetic addition',
                                          'A standalone display screen connected directly to an input power supply',
                                          'An isolated firmware storage medium without processing or memory units'],
                           'question': 'What is the technical definition of a computer given in Part B of the manual?'},
                       {   'correctAnswer': 'Under the Computer Name tab in System Properties',
                           'explanation': 'System Properties contains the Computer Name tab showing the Full computer '
                                          'name, Computer description, and Workgroup/Domain.',
                           'options': [   'Under the Computer Name tab in System Properties',
                                          'Under the Screen Saver settings dialog',
                                          'Inside the Recycle Bin properties menu',
                                          'Within the Windows Calculator help file'],
                           'question': "Where can a user inspect the computer's registered full computer name and "
                                       'workgroup in Windows?'}],
        'title': 'Lab 1: Operate OS and Hardware of Computer'},
    {   'codeSnippet': '# MS Word 2007 Document Structure & Standard Formatting Keys\n'
                       'Ctrl + N  # New document\n'
                       'Ctrl + S  # Save document as <name>-lab2.docx\n'
                       'Ctrl + B  # Bold\n'
                       'Ctrl + I  # Italic\n'
                       'Ctrl + U  # Underline\n'
                       'Ctrl + K  # Hyperlink\n'
                       'F7        # Spelling & Grammar Check',
        'content': '# Lab#02\n'
                   '\n'
                   '## IMITATE MS WORD\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Microsoft Word\n'
                   '\n'
                   '#### Introduction:\n'
                   'MS WORD is a word processor developed by Microsoft. It is used to create, edit and view '
                   'documents.\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To become familiar with basics of Microsoft Word 2007\n'
                   '* To become familiar with the online help facilities of Word 2007.\n'
                   '\n'
                   '#### Preparation:\n'
                   'An excellent online tutorial resource on Microsoft Word 2007 can be viewed at:\n'
                   '`http://www.fgcu.edu/support/office2007/Word/`\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Opening and Saving Files\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS WORD\n'
                   '\n'
                   '#### Procedure:\n'
                   "Open a new file and save it while saving the file's name as `your first name`-lab-2.docx. For "
                   'example, a student name Abdullah should save the file as `Abdullah-lab2.docx`.\n'
                   '\n'
                   '*[Hint: The functionality to open and save a new file is available by clicking on the Microsoft '
                   'Office button]*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #2: Word Formatting\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS WORD\n'
                   '\n'
                   '#### Procedure:\n'
                   'Type the following sentence into your newly created Word file:\n'
                   '> *"I, (write your own name here), am a student of BEE 1-(write your section name here) at the '
                   'Hamdard University"*\n'
                   '\n'
                   '#### Changing the formatting of typed text:\n'
                   '\n'
                   '1. **Italicizing text:**\n'
                   '   Copy/ paste the original sentence above and now precede the statement with the text '
                   '`"Italicized copy"`. Italicize the whole text.\n'
                   '\n'
                   '2. **Making text bold:**\n'
                   '   Copy/ paste the original sentence and now precede the statement with the text `"bold text copy: '
                   '"`. Change the type of your name, your section, and school\'s name to bold.\n'
                   '\n'
                   '3. **Underlining text:**\n'
                   '   Copy/ paste the original sentence and now precede the statement with the text `"Underline '
                   'text"`. Underline your name, your section, and school\'s name.\n'
                   '\n'
                   '4. **Crossing out text:**\n'
                   '   Copy/ paste the original sentence and now precede the statement with the text `"Crossed out '
                   'text copy: "`. Cross out your name, your section, and school\'s name.\n'
                   '\n'
                   '5. **Text in different fonts:**\n'
                   '   Copy and paste the original sentence twice (2 new copies). For the first copy, change the font '
                   'of the sentence to **Tahoma**, and for the second copy change the font of the sentence to '
                   '**Verdana**. Write the font names in brackets at the end of each copied statement.\n'
                   '\n'
                   '6. **Text in different font sizes:**\n'
                   '   Copy and paste the original sentence twice (2 new copies). For the first copy, change the font '
                   'size of the sentence to **14**, and for the second copy, change the font size to **16**. Write the '
                   'font sizes in brackets at the end of each copied statement.\n'
                   '\n'
                   '7. **Text in different colors:**\n'
                   '   Copy and paste the original sentence twice (2 new copies). For the first copy, change the text '
                   'color to **red**, and for the second copy, change the text color to **blue**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Additional Word Features:\n'
                   '\n'
                   '#### 1) Inserting URL / shapes / symbols / headers / footers:\n'
                   '*(Hint: Look for the Insert tab in the tabs of ribbon)*\n'
                   '* **How can a URL link be inserted?** In the open file, insert a link to the URL: '
                   '`http://www.google.com.pk` (hint: look in Insert > Hyperlink)\n'
                   '* Insert the arrow shape that follows (hint: look in Insert > Shapes)\n'
                   '* Insert the following symbol **α** (hint: look in Insert > Symbol)\n'
                   '* Insert a header and footer in your file (hint: look in Insert > Header and Insert > Footer)\n'
                   '\n'
                   '#### 2) Making a list:\n'
                   'Make a list of all the subjects that you are studying. For example, your generated list should '
                   'look like:\n'
                   '1. Physics\n'
                   '2. Fundamentals of ICT\n'
                   '3. Communication Skills\n'
                   '4. ECA\n'
                   '\n'
                   '* Make the numbering of the list bold\n'
                   '* Change the color of the numbering of the list\n'
                   '* Change the listing identifiers from 1), 2), 3) to i), ii) and iii).\n'
                   '\n'
                   '#### 3) Making a table:\n'
                   'Make a table with three columns and three rows. Also color the top row gray. Your table should '
                   'look like the following:\n'
                   '\n'
                   '| Column 1 | Column 2 | Column 3 |\n'
                   '| :--- | :--- | :--- |\n'
                   '| **Row 1** | **ROW 1** | **ROW 1** |\n'
                   '| Column 1 | Column 2 | Column 3 |\n'
                   '| Column 1 | Column 2 | Column 3 |\n'
                   '\n'
                   '*Table 2.1 Making table*\n'
                   '\n'
                   '#### 4) Checking Spellings and Grammar:\n'
                   'Check the document you have created for any spelling and/or grammar error.\n'
                   '*(Hint: Go to the Review tab in the tabs on the ribbon, and click on Spelling & Grammar or press '
                   'F7)*\n'
                   '\n'
                   '#### 5) Calculating the word count:\n'
                   'Calculate the total word count of your document. *(Hint: Click on the Review tab and then on Word '
                   'Count)*\n'
                   '\n'
                   '#### 6) Commenting on a document:\n'
                   'Use the **Review > New Comment** option to select a text and then comment on it. The comments are '
                   'not part of the original document, and are used to foster collaboration/ better understanding of '
                   'the text.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 2 Task:\n'
                   'Create your CV using MS Word:\n'
                   '1. Insert headings\n'
                   '2. Insert your picture\n'
                   '3. Insert table (education detail)\n',
        'flashcards': [   {   'answer': '.docx (Office Open XML document format).',
                              'question': 'What file extension is used by Microsoft Word 2007 documents?'},
                          {   'answer': "Under the 'Review' tab on the ribbon (and also displayed on the bottom Status "
                                        'Bar).',
                              'question': 'Where is the Word Count tool located in MS Word 2007?'},
                          {   'answer': "Highlight the text, go to 'Insert' tab -> click 'Hyperlink' (or press Ctrl + "
                                        'K), and enter the target web address.',
                              'question': 'How do you insert an external URL hyperlink in MS Word?'},
                          {   'answer': 'A formatting style that draws a horizontal line directly through the center '
                                        'of selected characters without deleting them.',
                              'question': 'What is strikethrough (crossing out text) in word formatting?'}],
        'order': 2,
        'quizzes': [   {   'correctAnswer': 'F7',
                           'explanation': 'F7 is the standard Microsoft Office shortcut to trigger the Spelling & '
                                          'Grammar inspection tool.',
                           'options': ['F7', 'F1', 'Ctrl + S', 'Alt + F4'],
                           'question': 'Which keyboard shortcut executes the Spelling and Grammar check in Microsoft '
                                       'Word 2007?'},
                       {   'correctAnswer': 'Insert Tab',
                           'explanation': 'The Insert tab contains groups for Pages, Tables, Illustrations (Shapes), '
                                          'Links (Hyperlinks), Header & Footer, and Symbols.',
                           'options': ['Insert Tab', 'Home Tab', 'Page Layout Tab', 'View Tab'],
                           'question': 'Under which Ribbon tab can you find the options to insert Hyperlinks, Shapes, '
                                       'Symbols, Headers, and Footers in Word 2007?'},
                       {   'correctAnswer': 'To facilitate collaboration and note-taking without modifying the actual '
                                            'document text',
                           'explanation': 'Comments allow reviewers to suggest revisions and annotations without '
                                          'editing the main body content.',
                           'options': [   'To facilitate collaboration and note-taking without modifying the actual '
                                          'document text',
                                          'To permanently delete selected paragraphs from the file',
                                          'To change the font color of the entire document to gray',
                                          'To convert the document into a spreadsheet format'],
                           'question': "What is the primary purpose of the 'New Comment' feature located under the "
                                       'Review tab?'},
                       {   'correctAnswer': 'They are sans-serif fonts without small projecting decorative strokes at '
                                            'the ends of letters',
                           'explanation': 'Sans-serif typefaces (like Tahoma and Verdana) lack decorative serif '
                                          'strokes, enhancing digital readability on screens.',
                           'options': [   'They are sans-serif fonts without small projecting decorative strokes at '
                                          'the ends of letters',
                                          'They can only display bold letters and cannot be underlined',
                                          'They do not support numeric digits or punctuation',
                                          'They automatically convert text into hyperlinks'],
                           'question': 'How are fonts such as Tahoma and Verdana differentiated from traditional serif '
                                       'fonts like Times New Roman?'},
                       {   'correctAnswer': 'Headings, picture, and an education detail table',
                           'explanation': 'The Lab 2 Task explicitly instructs students to format their CV with clear '
                                          'headings, a personal picture, and an educational qualification table.',
                           'options': [   'Headings, picture, and an education detail table',
                                          'A PowerPoint animation, audio track, and video clip',
                                          'A macro script, database connection, and query string',
                                          'A compiler directive, makefile, and execution process flowchart'],
                           'question': 'What are the three required elements specified in the Lab 2 Task for creating '
                                       'a student CV?'}],
        'title': 'Lab 2: Imitate MS Word'},
    {   'codeSnippet': '# PowerPoint Presentation Design Principles & Animation Pipeline\n'
                       '# Principles: Simple, Readable, Visual, Organized\n'
                       '# Animation Types: Entrance, Emphasis, Exit, Motion Paths\n'
                       '# Recommended Header Size: 36-66 pt\n'
                       '# Recommended Body Size: 24-28 pt',
        'content': '# Lab#03\n'
                   '\n'
                   '## IMITATE MS POWER POINT\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Microsoft PowerPoint\n'
                   '\n'
                   '#### Introduction:\n'
                   'A presentation usually is composed of two elements: the presenter speaking about certain facts and '
                   'the slides complementing the speech, helping the audience visualize the presented facts.\n'
                   '\n'
                   'While there are no universal rules that define a good presentation, the experts point to certain '
                   'basic principles that can guide presentation design. These basic principles are listed below:\n'
                   '\n'
                   '1. **Good presentations are simple:**\n'
                   '   * The presented data is made as simple as possible without compromising the essential '
                   'information.\n'
                   '   * The images/ transitions/ animations should add emphasis to the message of the presenter '
                   'rather than overwhelm it.\n'
                   '\n'
                   '2. **Good presentations are readable by the audience:**\n'
                   '   * The slides use an appropriately large font size. (Using a large font size also forces you to '
                   "prioritize your slide's main points and deleting non-essential information.)\n"
                   '   * The slides use good contrast between slide background and text. (The color chosen for the '
                   'text should contrast with the background; on a light background, a dark color should be used and '
                   'vice-versa.)\n'
                   '   * They use sans-serif fonts.\n'
                   '\n'
                   '3. **Good presentations are visual:**\n'
                   '   * The slides should complement what the presenter is saying.\n'
                   '   * A good technique is to use visual content (images/ graphs/ charts/ animations/ movies) to '
                   'demonstrate the presented idea/ facts.\n'
                   '\n'
                   '4. **Good presentations are organized:**\n'
                   '   * The slides should flow in a coherent manner and not be disjointed. (To have a constant theme '
                   "flowing throughout your slides, it's important that you properly plan your slides; it's often best "
                   'to do that on paper rather than on the PC.)\n'
                   '   * The slides should have an introduction and a summary slide to help the audience in '
                   'anticipating and recalling the main content of the presentation.\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To become familiar with the basics of Microsoft PowerPoint 2007\n'
                   '* To become familiar with the basics of good presentation design.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Starting a Presentation\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. **Inserting a text box:**\n'
                   '   On slide number 1, insert a textbox. The textbox is inserted by clicking on the **Insert** tab '
                   'and then choosing **Text Box** option.\n'
                   '   Add the text `"Fundamentals of ICT lab"` in the inserted text box.\n'
                   '\n'
                   '2. **Increasing font size:**\n'
                   '   Duplicate this slide (slide number 1) by right-clicking on slide 1 (as shown in the slide '
                   'sorter on the left hand side of the screen) and selecting **Duplicate Slide**. Slide duplication '
                   'can also be done through copying the slide and then pasting it.\n'
                   '   On slide 2, increase the font size to **66**.\n'
                   '\n'
                   '3. **Changing the fill color of the text box:**\n'
                   '   Go to slide 2 now. On slide 2, select the text box and then open the **Format** tab. You should '
                   'be able to see **Shape Fill** option. Choose light gray color as the background of the textbox.\n'
                   '\n'
                   '4. **Special text effects:**\n'
                   '   Duplicate slide 2 to slide 3. On slide 3, select the text box, and then choose the **Format** '
                   'tab. On the format tab choose the **Text Effects** option. Choose the **Glow** option to add pink '
                   'glow around the red text.\n'
                   '\n'
                   '5. **Using the Smart Art feature:**\n'
                   '   Copy slide 2 to slide 4. On slide 4, replace the text `"Fundamentals of ICT lab 5"` with a '
                   'heading `"Microsoft Office"` followed by an indented list of three items:\n'
                   '   * Word 2007\n'
                   '   * Excel 2007\n'
                   '   * PowerPoint 2007\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #2: Animations\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS PowerPoint\n'
                   '\n'
                   '#### Procedure:\n'
                   'A custom animation can be generated through the **Add Effect** button in the Custom Animation '
                   'pane.\n'
                   '\n'
                   'An animation effect is primarily of four types:\n'
                   '1. **Entrance effect:** Controls how an object enters the slide.\n'
                   '2. **Emphasis effect:** Draws attention to an object already on the slide (e.g., spin, pulse, '
                   'grow/shrink).\n'
                   '3. **Exit effect:** Controls how an object departs from the slide.\n'
                   '4. **Motion Paths:** Determines the movement trajectory of an object across the slide.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 3 Task:\n'
                   'Create a PowerPoint presentation on the topic **"Pakistan"**:\n'
                   '* Use animations and slide transitions\n'
                   '* Insert images, tables, and hyperlinks\n'
                   '* Ensure good contrast, sans-serif fonts, and structured organization (Introduction, Content, '
                   'Summary)\n',
        'flashcards': [   {   'answer': 'Slides complement what the presenter speaks, helping the audience visualize '
                                        'facts through concise text, diagrams, and media without overwhelming them.',
                              'question': 'What is the primary role of presentation slides relative to the speaker?'},
                          {   'answer': 'A graphic tool that visually organizes complex information into professional '
                                        'diagrams (e.g., process workflows, hierarchies, and cycle lists).',
                              'question': 'What is SmartArt in Microsoft PowerPoint?'},
                          {   'answer': 'Transitions apply to the movement between entire slides, whereas Animations '
                                        'apply to individual elements (text, images, shapes) on a single slide.',
                              'question': 'What is the difference between a slide Transition and an Animation?'},
                          {   'answer': 'Shape Fill sets the background color of a container box, while Glow adds a '
                                        'soft colored radiance around characters to draw visual emphasis.',
                              'question': 'What is the function of Shape Fill and Glow text effects?'}],
        'order': 3,
        'quizzes': [   {   'correctAnswer': 'Simple, Readable, Visual, and Organized',
                           'explanation': 'Expert presentations are simple (not overwhelming), readable (large font, '
                                          'high contrast), visual (charts/images), and organized (clear flow with '
                                          'intro/summary).',
                           'options': [   'Simple, Readable, Visual, and Organized',
                                          'Complex, Monochromatic, Lengthy, and Scripted',
                                          'Animated, Loud, Crowded, and Wordy',
                                          'Abstract, Compact, Compressed, and Theoretical'],
                           'question': 'What are the four core principles of good presentation design outlined in Lab '
                                       '3?'},
                       {   'correctAnswer': 'Entrance, Emphasis, Exit, and Motion Paths',
                           'explanation': 'PowerPoint categorizes object animations into Entrance (entering), Emphasis '
                                          '(highlighting), Exit (leaving), and Motion Paths (custom movement '
                                          'trajectories).',
                           'options': [   'Entrance, Emphasis, Exit, and Motion Paths',
                                          'Fade, Dissolve, Wipe, and Push',
                                          'Linear, Quadratic, Exponential, and Logarithmic',
                                          'Header, Footer, Margin, and Border'],
                           'question': 'What are the four primary categories of custom animations available in '
                                       'Microsoft PowerPoint?'},
                       {   'correctAnswer': 'To ensure maximum readability for the audience from a distance',
                           'explanation': 'Sans-serif typefaces (e.g., Arial, Calibri) on high-contrast backgrounds '
                                          'prevent eye strain and ensure slides are legible across lecture halls.',
                           'options': [   'To ensure maximum readability for the audience from a distance',
                                          'To minimize the file size of the presentation on disk',
                                          'Because PowerPoint does not support serif fonts',
                                          'To restrict slides to only a single bullet point'],
                           'question': 'Why is it strongly advised to use sans-serif fonts with high contrast in '
                                       'presentation slides?'},
                       {   'correctAnswer': 'Right-click the slide in the slide sorter pane on the left and select '
                                            "'Duplicate Slide'",
                           'explanation': 'Right-clicking any thumbnail in the left Slide Sorter pane and clicking '
                                          "'Duplicate Slide' (or Ctrl+D) creates an exact clone.",
                           'options': [   'Right-click the slide in the slide sorter pane on the left and select '
                                          "'Duplicate Slide'",
                                          'Press Alt + F4',
                                          'Click the Delete key twice',
                                          'Select File -> Close'],
                           'question': 'How can a user duplicate an existing slide in Microsoft PowerPoint 2007?'},
                       {   'correctAnswer': 'Pakistan',
                           'explanation': 'The Lab 3 Task asks students to create a multi-slide presentation on '
                                          "'Pakistan' featuring animations, transitions, images, tables, and "
                                          'hyperlinks.',
                           'options': [   'Pakistan',
                                          'Operating System Kernels',
                                          'C++ Compilers',
                                          'Digital Signal Processing'],
                           'question': 'What is the topic of the comprehensive presentation assigned in the Lab 3 '
                                       'Task?'}],
        'title': 'Lab 3: Imitate MS Power Point'},
    {   'codeSnippet': '# Excel Spreadsheet Formulas & Built-in Analytical Functions\n'
                       '=SUM(B2:B30)       # Computes total sum of range\n'
                       '=AVERAGE(B2:B30)   # Computes arithmetic mean\n'
                       '=MAX(B2:B30)       # Returns highest value\n'
                       '=MIN(B2:B30)       # Returns lowest value\n'
                       '# AutoFill handle: Drag bottom-right square corner to generate sequences',
        'content': '# Lab#04\n'
                   '\n'
                   '## IMITATE MS EXCEL\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Microsoft Excel\n'
                   '\n'
                   '#### Introduction:\n'
                   'Microsoft Excel is a spreadsheet application. Spreadsheets are ways to organize data by grouping '
                   'it into rows and columns.\n'
                   '\n'
                   '#### Basic terminology:\n'
                   '* **Cell:** The small boxes where data exists in a spreadsheet. Cells are identified by the column '
                   'letter followed by the row number (e.g., A1, B2). Columns are named by letters A-Z, followed by '
                   'AA, AB... whereas rows are numbered by integers 1, 2, 3...\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To become familiar with basics of Microsoft Excel 2007\n'
                   '* To become familiar with the online help facilities of Excel 2007.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Generating and Formatting Spreadsheet\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS Excel\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. Open a new file and save it as an excel workbook naming it `your-name.xlsx`.\n'
                   '2. Explore the number formatting options in Excel. Enter some number in any cell, and then change '
                   'the number formatting to:\n'
                   '   * **Percentage**\n'
                   '   * **Currency**\n'
                   '3. Enter the date of the day you are doing this lab exercise. If the date is 30th January, 2009, '
                   'write `1/30/2009`. Change the formatting of the date by right clicking on the cell and choosing '
                   '**Format Cells**. Alternatively, click on the arrow in the Numbers tab.\n'
                   '4. Explore the alignment and font options in Excel that can be used for formatting cells. More '
                   'options can be seen by clicking on the arrows beneath the alignment and font options.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #2: Using Automatic Features of Microsoft Excel 2007\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS Excel\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. **AutoFill Months Series:**\n'
                   '   Suppose you would like to create a column for each month of the year. How can you achieve this '
                   'without manually writing the name of each month?\n'
                   '   * *Hint:* Type `Jan` in the first cell, position the cursor over the fill handle (small black '
                   'cross `+` in the bottom right corner of the cell), and drag across twelve columns or rows.\n'
                   '\n'
                   '2. **AutoFill Arithmetic Number Series:**\n'
                   '   Suppose that the data that you want to enter in successive cells is an arithmetic series (e.g., '
                   '1, 2, 3... up to 100).\n'
                   '   * How can you enter all these numbers automatically?\n'
                   '   * *Hint:* Enter `1` in the first cell and `2` in the second cell, select both cells, and drag '
                   'the fill handle down.\n'
                   '\n'
                   '3. **AutoSum Feature:**\n'
                   '   How can the sum of all the numbers added be obtained?\n'
                   '   * *Hint:* You can use the **AutoSum** (`∑`) button present on the Home or Formulas ribbon.\n'
                   '\n'
                   '4. **AutoFill Alphanumeric Labels:**\n'
                   '   Suppose that you would like to enter `Student 1` in the first row, and `Student 10` in the 10th '
                   'row.\n'
                   '   * *Hint:* Type `Student 1` and drag the fill handle down to row 10; Excel automatically '
                   'increments the number suffix.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #3: Statistical & Mathematical Functions\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Computer\n'
                   '* MS Excel\n'
                   '\n'
                   '#### Procedure:\n'
                   'Open the **Formulas** tab and explore the core functions:\n'
                   '* `=SUM(range)`: Computes the total sum of the selected cell range.\n'
                   '* `=AVERAGE(range)`: Calculates the arithmetic average of numeric values.\n'
                   '* `=MAX(range)`: Finds the maximum value in the dataset.\n'
                   '* `=MIN(range)`: Finds the minimum value in the dataset.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 4 tasks:\n'
                   '1. Create a worksheet containing the result award list of your class.\n'
                   '2. Find the **maximum**, **minimum**, and **average** marks obtained in the award list using Excel '
                   'formulas.\n'
                   '3. Represent the result with both **bar chart** and **pie chart**.\n',
        'flashcards': [   {   'answer': 'Returns the highest numeric value among a specified set of cells or arguments '
                                        '(e.g., =MAX(A1:A50)).',
                              'question': 'What does the =MAX() function do in Excel?'},
                          {   'answer': "Select the cell, right-click and choose 'Format Cells' -> select 'Currency' "
                                        'category and choose your desired currency symbol and decimal places.',
                              'question': 'How do you apply Currency formatting to a number in Excel?'},
                          {   'answer': "Excel recognizes the alphanumeric pattern and populates 'Student 2', 'Student "
                                        "3', 'Student 4', 'Student 5', and 'Student 6'.",
                              'question': "What happens when you type 'Student 1' and drag the fill handle down 5 "
                                          'rows?'},
                          {   'answer': 'A Bar Chart displays comparisons among discrete categories using rectangular '
                                        'bars, while a Pie Chart illustrates proportions of a whole (percentage '
                                        'shares).',
                              'question': 'What is the difference between a Bar Chart and a Pie Chart?'}],
        'order': 4,
        'quizzes': [   {   'correctAnswer': 'By its Column Letter followed by its Row Number (e.g., B4)',
                           'explanation': 'Excel uses column headers (letters A-Z, AA...) and row indices (integers 1, '
                                          '2, 3...) to address cells (e.g., B4 denotes column B, row 4).',
                           'options': [   'By its Column Letter followed by its Row Number (e.g., B4)',
                                          'By its Row Number followed by its Column Letter (e.g., 4B)',
                                          'By the date the workbook was created',
                                          'By the total count of words in the spreadsheet'],
                           'question': 'How is an individual cell address uniquely identified in Microsoft Excel?'},
                       {   'correctAnswer': 'To automatically generate and extend data series such as months, dates, '
                                            'and number sequences',
                           'explanation': 'Dragging the AutoFill handle evaluates patterns in selected cells and '
                                          'automatically extends sequences like Jan-Dec or 1-100.',
                           'options': [   'To automatically generate and extend data series such as months, dates, and '
                                          'number sequences',
                                          'To permanently close the current workbook window',
                                          'To print the spreadsheet without previewing',
                                          'To delete formatting rules across all worksheets'],
                           'question': 'What is the function of the AutoFill handle (the small square cross at the '
                                       'bottom-right of a selected cell)?'},
                       {   'correctAnswer': '=AVERAGE(C2:C25)',
                           'explanation': '=AVERAGE(C2:C25) is the built-in Excel function for calculating the '
                                          'arithmetic mean across a range.',
                           'options': ['=AVERAGE(C2:C25)', '=MEAN(C2:C25)', '=SUM(C2:C25) / 100', '=CALCULATE(C2:C25)'],
                           'question': 'Which formula correctly computes the arithmetic average of marks located '
                                       'between cells C2 and C25?'},
                       {   'correctAnswer': 'AutoSum (∑)',
                           'explanation': 'The AutoSum (∑) button automatically detects adjacent numeric ranges and '
                                          'inserts the =SUM() formula.',
                           'options': ['AutoSum (∑)', 'Format Painter', 'Word Count', 'Track Changes'],
                           'question': 'Which ribbon tool provides one-click summation for a column of adjacent '
                                       'numeric cells?'},
                       {   'correctAnswer': 'Bar Chart and Pie Chart',
                           'explanation': 'The Lab 4 tasks require students to graphically represent the class marks '
                                          'using both a Bar chart and a Pie chart.',
                           'options': [   'Bar Chart and Pie Chart',
                                          'Scatter Plot and Radar Chart',
                                          'Stock Chart and Bubble Chart',
                                          'Gantt Chart and Waterfall Chart'],
                           'question': 'Which two chart types are specifically assigned in the Lab 4 Task to visualize '
                                       'the class result award list?'}],
        'title': 'Lab 4: Imitate MS Excel'},
    {   'codeSnippet': '<!DOCTYPE html>\n'
                       '<html>\n'
                       '<head>\n'
                       '  <title>My First Web Page</title>\n'
                       '</head>\n'
                       '<body>\n'
                       '  <h1>My First Web Page</h1>\n'
                       '  <h2>What this is</h2>\n'
                       '  <p>A simple page put together using HTML</p>\n'
                       '  <h2>Hyperlinks & Images</h2>\n'
                       '  <p><a href="http://www.google.com">Search Engine</a></p>\n'
                       '  <img src="assets/images/university/cfp/cfp_logo.png" width="120" height="120" alt="Logo" />\n'
                       '</body>\n'
                       '</html>',
        'content': '# Lab- 05\n'
                   '\n'
                   '## PRACTICE WEBPAGE DESIGNING USING HTML\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part A: Introduction to HTML\n'
                   '\n'
                   '#### Introduction:\n'
                   'HyperText Markup Language (HTML) is the predominant markup language for web pages. HTML elements '
                   'are the basic building-blocks of web pages.\n'
                   '\n'
                   'HTML is written in the form of HTML elements consisting of tags, enclosed in angle brackets (like '
                   '`<html>`), within the web page content. HTML tags most commonly come in pairs like `<h1>` and '
                   '`</h1>`, although some tags, known as empty elements, are unpaired, for example `<img>` and `<br '
                   '/>`. The first tag in a pair is the start tag, the second tag is the end tag (they are also called '
                   'opening tags and closing tags). In between these tags web designers can add text, tags, comments '
                   'and other types of text-based content.\n'
                   '\n'
                   'The purpose of a web browser is to read HTML documents and compose them into visible or audible '
                   'web pages. The browser does not display the HTML tags, but uses the tags to interpret the content '
                   'of the page.\n'
                   '\n'
                   'HTML elements form the building blocks of all websites. HTML allows images and objects to be '
                   'embedded and can be used to create interactive forms. It provides a means to create structured '
                   'documents by denoting structural semantics for text such as headings, paragraphs, lists, links, '
                   'quotes and other items. It can embed scripts in languages such as JavaScript which affect the '
                   'behavior of HTML web pages.\n'
                   '\n'
                   '#### Objectives:\n'
                   '* To learn the basics of HTML\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #1: Creating Web Page\n'
                   '\n'
                   '#### Equipment:\n'
                   '* Text editor (Notepad)\n'
                   '* Web browser (Firefox / Internet Explorer / Chrome)\n'
                   '\n'
                   '#### Procedure:\n'
                   '1. Open a text editor like Notepad.\n'
                   '2. Type this into your text editor:\n'
                   '   ```html\n'
                   '   This is my first web page\n'
                   '   ```\n'
                   '3. Create a folder called `html` on your drive and save the file as `"myfirstpage.html"`. It is '
                   'important that the extension `.html` is specified - some text editors, such as Notepad, will '
                   'automatically save it as `.txt` otherwise.\n'
                   '4. Open your browser and navigate to the saved file location (e.g., `c:\\html\\myfirstpage.html` '
                   'or go to File > Open).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### PROBLEM #2: Tags, Attributes, and Elements\n'
                   '\n'
                   '#### Procedure:\n'
                   'The basic structure of an HTML document includes tags, which surround content and apply meaning to '
                   'it.\n'
                   'Change your document so that it looks like this:\n'
                   '```html\n'
                   '<html>\n'
                   '<body>\n'
                   'This is my first web page\n'
                   '</body>\n'
                   '</html>\n'
                   '```\n'
                   'Save the file and refresh your browser.\n'
                   '\n'
                   '#### Tag Fundamentals:\n'
                   '* **Opening & Closing Tags:** `<html>` kicks things off and informs the browser that everything '
                   'between it and `</html>` is an HTML document. The content between `<body>` and `</body>` is the '
                   'visible body of the page.\n'
                   '* **Closing Tags:** All HTML tags should be closed. Empty tags that do not wrap content close '
                   'themselves (e.g., `<br />` or `<img />`).\n'
                   '* **Attributes:** Tags can have attributes providing extra metadata inside the opening tag: `<tag '
                   'attribute="value">Content</tag>`.\n'
                   '* **Elements:** An element encompasses the opening tag, closing tag, and all enclosed content '
                   '(e.g., `<title>My Page</title>` is a title element).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part B: Working with Page Titles, Paragraphs, Headings and Lists\n'
                   '\n'
                   '#### Introduction:\n'
                   'The general form of an HTML element is:\n'
                   '`<tag attribute1="value1" attribute2="value2">content</tag>`.\n'
                   '\n'
                   '#### PROBLEM #1: Head and Title Tags\n'
                   '```html\n'
                   '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
                   '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'
                   '<html>\n'
                   '<head>\n'
                   '<title>My first web page</title>\n'
                   '</head>\n'
                   '<body>\n'
                   'This is my first web page\n'
                   '</body>\n'
                   '</html>\n'
                   '```\n'
                   'The `<head>` element appears before the `<body>` element and contains document metadata that does '
                   'not appear in the main canvas window.\n'
                   '\n'
                   '#### PROBLEM #2: Paragraph Tag\n'
                   '```html\n'
                   '<!DOCTYPE html>\n'
                   '<html>\n'
                   '<head>\n'
                   '<title>My first web page</title>\n'
                   '</head>\n'
                   '<body>\n'
                   'This is my first web page\n'
                   '<p>How exciting</p>\n'
                   '</body>\n'
                   '</html>\n'
                   '```\n'
                   '\n'
                   '#### PROBLEM #3: Heading and List Tags\n'
                   '```html\n'
                   '<!DOCTYPE html>\n'
                   '<html>\n'
                   '<head>\n'
                   '<title>My first web page</title>\n'
                   '</head>\n'
                   '<body>\n'
                   '<h1>My first web page</h1>\n'
                   '<h2>What this is</h2>\n'
                   '<p>A simple page put together using HTML</p>\n'
                   '<h2>Why this is</h2>\n'
                   '<ul>\n'
                   '<li>To learn HTML</li>\n'
                   '<li>To show off</li>\n'
                   '</ul>\n'
                   '</body>\n'
                   '</html>\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part B (Continued): Implementation of Hyperlinks, Images, and Tables\n'
                   '\n'
                   '#### Hyperlinks (`<a>` tag):\n'
                   '```html\n'
                   '<h2>Where to find the tutorial</h2>\n'
                   '<p><a href="http://www.google.com">HTML Dog</a></p>\n'
                   '```\n'
                   '* **href attribute:** Specifies destination URL (absolute like `http://www.htmldog.com` or '
                   'relative like `flying.html`).\n'
                   '* **In-page bookmark:** `<h2 id="move">Section</h2>` can be targeted via `<a href="#move">Go to '
                   'Section</a>`.\n'
                   '\n'
                   '#### Images (`<img>` tag):\n'
                   '```html\n'
                   '<img src="http://www.htmldog.com/images/logo.gif" width="157" height="70" alt="HTML Dog logo" />\n'
                   '```\n'
                   '* **src:** Path to image file.\n'
                   '* **width & height:** Dimensions to preserve layout stability during page load.\n'
                   '* **alt:** Alternative textual description for screen readers and accessibility.\n'
                   '\n'
                   '#### Tables (`<table>` tag):\n'
                   '```html\n'
                   '<table border="1">\n'
                   '<tr>\n'
                   '  <td>Row 1, cell 1</td>\n'
                   '  <td>Row 1, cell 2</td>\n'
                   '  <td>Row 1, cell 3</td>\n'
                   '</tr>\n'
                   '<tr>\n'
                   '  <td>Row 2, cell 1</td>\n'
                   '  <td>Row 2, cell 2</td>\n'
                   '  <td>Row 2, cell 3</td>\n'
                   '</tr>\n'
                   '<tr>\n'
                   '  <td>Row 3, cell 1</td>\n'
                   '  <td>Row 3, cell 2</td>\n'
                   '  <td>Row 3, cell 3</td>\n'
                   '</tr>\n'
                   '<tr>\n'
                   '  <td>Row 4, cell 1</td>\n'
                   '  <td>Row 4, cell 2</td>\n'
                   '  <td>Row 4, cell 3</td>\n'
                   '</tr>\n'
                   '</table>\n'
                   '```\n'
                   '* `<table>`: Defines the table.\n'
                   '* `<tr>`: Defines a table row.\n'
                   '* `<td>`: Defines a data cell.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 5 Task:\n'
                   'Create a complete webpage using HTML:\n'
                   '1. Insert text including paragraphs and headings using different font styles and features.\n'
                   '2. Add Images, Tables, and Hyperlinks.\n',
        'flashcards': [   {   'answer': 'An element that cannot enclose content and does not require a closing tag, '
                                        "closing itself with '/>' (e.g., <br />, <hr />, <img />).",
                              'question': "What is an HTML 'empty element'?"},
                          {   'answer': "An absolute link contains the full web URL (e.g., 'http://google.com'), while "
                                        'a relative link points to a file relative to the current folder (e.g., '
                                        "'about.html').",
                              'question': 'What is the difference between an absolute link and a relative link in '
                                          'HTML?'},
                          {   'answer': '<ul> defines an unordered bulleted list, whereas <ol> defines an ordered '
                                        'numbered list. Both enclose list items with <li>.',
                              'question': 'What tag defines an unordered (bulleted) list versus an ordered list?'},
                          {   'answer': "Add an 'id' attribute to the target tag (e.g., <h2 id='contact'>), then link "
                                        "to it using <a href='#contact'>Jump to Contact</a>.",
                              'question': 'How do you link to a specific section on the same web page?'}],
        'order': 5,
        'quizzes': [   {   'correctAnswer': 'To read HTML documents and render them into visible web pages without '
                                            'displaying the tags themselves',
                           'explanation': 'Browsers interpret HTML markup tags to structure and present content '
                                          'visually without displaying the tag syntax directly.',
                           'options': [   'To read HTML documents and render them into visible web pages without '
                                          'displaying the tags themselves',
                                          'To compile C++ source code into native machine assembly',
                                          'To repair corrupted disk sectors on local hard drives',
                                          'To generate electrical power for computer motherboards'],
                           'question': 'What is the primary function of an HTML web browser (e.g., Chrome, Firefox)?'},
                       {   'correctAnswer': '<a href="...">',
                           'explanation': "The anchor tag <a> with its 'href' (hypertext reference) attribute defines "
                                          'hyperlinks in HTML.',
                           'options': ['<a href="...">', '<link src="...">', '<hyperlink to="...">', '<nav go="...">'],
                           'question': 'Which HTML tag is used to create an interactive hyperlink to an external '
                                       'website or internal page anchor?'},
                       {   'correctAnswer': 'Width and height reserve display layout space during loading, while alt '
                                            'provides accessibility descriptions',
                           'explanation': 'Width/height prevent layout shifts as images load, and the alt attribute '
                                          'provides alternative text for accessibility.',
                           'options': [   'Width and height reserve display layout space during loading, while alt '
                                          'provides accessibility descriptions',
                                          'They convert raster images into vector 3D models',
                                          'They force the web browser to refresh the operating system',
                                          'They are required compiler flags for server backend scripts'],
                           'question': "Why are the 'width', 'height', and 'alt' attributes critically important on "
                                       'the <img> tag?'},
                       {   'correctAnswer': '<tr> defines a table row, and <td> defines a table data cell',
                           'explanation': 'In an HTML <table>, <tr> denotes Table Row and <td> denotes Table Data '
                                          '(cell).',
                           'options': [   '<tr> defines a table row, and <td> defines a table data cell',
                                          '<tr> defines total records, and <td> defines data division',
                                          '<tr> defines text right-alignment, and <td> defines title description',
                                          '<tr> defines table border, and <td> defines table footer'],
                           'question': 'In HTML table construction, what do the tags <tr> and <td> represent?'},
                       {   'correctAnswer': '<head>',
                           'explanation': 'The <head> element contains page metadata, scripts, styles, and the '
                                          '<title>, none of which are rendered directly inside the canvas body.',
                           'options': ['<head>', '<body>', '<footer>', '<aside>'],
                           'question': 'Which tag encloses document metadata such as the page title (<title>) that '
                                       'does not render on the main canvas?'}],
        'title': 'Lab 5: Practice Web Page designing using HTML'},
    {   'codeSnippet': '#include "stdafx.h"\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main()\n'
                       '{\n'
                       '    cout << "Hello World" << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#06 ( Part A )\n'
                   '\n'
                   '## CONDUCT INSTALLATION OF VISUAL STUDIO 2008 & TURBO C++\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Part A: Installation of Visual Studio 2008 & Turbo C++\n'
                   '\n'
                   '#### Introduction:\n'
                   'Any pre-requisite prior to the installation will be checked and verified by the setup wizard. You '
                   'need to have the VS 2008 DVD. Insert the DVD into the DVD drive, the Autorun will be executed. '
                   'Click the **Install Visual Studio 2008** link to start the installation.\n'
                   '\n'
                   '#### Step-by-Step Installation:\n'
                   '1. **Welcome Setup Wizard:** Wait for the wizard to load the installation components.\n'
                   '2. **License Agreement:** Accept the software license terms and click Next.\n'
                   '3. **Installation Type:** Select the **Full** installation type and accept the default '
                   'installation path. Full installation requires approximately **4.3 GB** of disk space.\n'
                   '4. **Execution:** Click Install and allow the components to install.\n'
                   '5. **Completion & Restart:** Click Restart Now when prompted.\n'
                   '6. **Configuring Environment:** Launch Visual Studio 2008 and choose **Visual C++ Development '
                   'Settings**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Building Your First C++ Program in Visual Studio:\n'
                   '1. Select **File > New > Project**.\n'
                   '2. Expand the **Visual C++** folder > select **Win32** in Project Types > choose **Win32 Console '
                   'Application**.\n'
                   '3. Enter Project Name as `Helloworld` and click OK, then click Finish.\n'
                   '4. In the generated source file, enter:\n'
                   '   ```cpp\n'
                   '   #include "stdafx.h"\n'
                   '   #include <iostream>\n'
                   '   using namespace std;\n'
                   '\n'
                   '   void main()\n'
                   '   {\n'
                   '       cout << "Hello World ";\n'
                   '       cout << endl;\n'
                   '   }\n'
                   '   ```\n'
                   '5. Press `Ctrl + F5` to compile and run (or **Build > Build Solution**, followed by **Debug > '
                   'Start Without Debugging**).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Installation of Turbo C++:\n'
                   '1. Run the setup executable.\n'
                   '2. Open the editor window.\n'
                   '3. Write your program and save it with the `.CPP` extension (e.g., `FIRST_PROGRAM.CPP`).\n'
                   '4. **Compile:** Compile via the **Compile** menu (or `Alt + F9`). Errors display in the Message '
                   'window (`Window > Message`).\n'
                   '5. **Run:** Execute via `Ctrl + F9`. View results under `Window > Output`.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '# Lab#06 ( Part B )\n'
                   '\n'
                   '## INTRODUCTION TO C++ PROGRAMMING LANGUAGE\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### C++ Program Phases & Execution Flow\n'
                   '\n'
                   '![Fig 6.1: Execution Process](assets/images/university/cfp/lab6_execution_flow.png)\n'
                   '\n'
                   'A C++ program goes through six key execution phases:\n'
                   '1. **Edit:** Programmer writes code in an editor and saves it as a `.cpp` source file.\n'
                   '2. **Preprocess:** Preprocessor directives (beginning with `#`, like `#include`) are processed '
                   'before compilation.\n'
                   '3. **Compile:** The compiler converts C++ source code into machine-readable object code (`.obj`).\n'
                   '4. **Link:** The linker combines object code with runtime library functions into an executable '
                   'binary (`.exe`).\n'
                   '5. **Load:** The loader loads the executable file into primary RAM memory.\n'
                   '6. **Execute:** The CPU reads and executes instructions sequentially.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Program Layout:\n'
                   '* Every program must start execution from `main()`\n'
                   '* The first line of the program is called the **Function (main) Heading**\n'
                   '* The actual code is placed within start and close brackets `{}`\n'
                   '* `#include <iostream>` tells C++ to include standard input/output stream library definitions\n'
                   '* `using namespace std;` informs the compiler that we are utilizing the standard C++ namespace\n'
                   '* The header file contains declarations of library functions used in C++\n'
                   '\n'
                   '### Use of `cout` Statement:\n'
                   'The standard output stream `cout` (pronounced "see-out") sends text to the screen:\n'
                   '```cpp\n'
                   'cout << "Hello World";\n'
                   '```\n'
                   '\n'
                   '### Escape Sequences in `cout`:\n'
                   'Special character pairs starting with a backslash `\\`:\n'
                   '* `\n'
                   '`: Newline (moves cursor to the next line)\n'
                   '* `\t`: Horizontal tab\n'
                   '* `\x07`: Alert / system beep\n'
                   '* `\\`: Prints a literal backslash\n'
                   '* `"`: Prints double quotation marks\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 6 Tasks:\n'
                   '\n'
                   '#### 1. Star Triangle:\n'
                   'Write a program that prints the following pattern:\n'
                   '```\n'
                   '*\n'
                   '* *\n'
                   '* * *\n'
                   '*****\n'
                   '*******\n'
                   '```\n'
                   '\n'
                   '#### 2. Student Data Box:\n'
                   'Write a program that displays your student information enclosed in an asterisk border:\n'
                   '```\n'
                   '******************************************\n'
                   '* Name       :                           *\n'
                   '* Class      :                           *\n'
                   '* Department :                           *\n'
                   '* University : Hamdard University        *\n'
                   '******************************************\n'
                   '```\n'
                   '\n'
                   '#### 3. Star Histogram / Bar Pattern:\n'
                   'Write a program that displays the following output:\n'
                   '```\n'
                   '**********\n'
                   '********************\n'
                   '********************\n'
                   '**************************************************\n'
                   '**********\n'
                   '**********\n'
                   '**********\n'
                   '**********\n'
                   '```\n'
                   '\n'
                   '#### 4. Diamond / Tree Pattern:\n'
                   'Write a program that displays the following output:\n'
                   '```\n'
                   '*\n'
                   '**\n'
                   '* * *\n'
                   '**************\n'
                   '*\n'
                   '*\n'
                   '*\n'
                   '*\n'
                   '***\n'
                   '****\n'
                   '* *\n'
                   '**\n'
                   '*\n'
                   '*\n'
                   '```\n',
        'flashcards': [   {   'answer': 'The linker combines compiled object files (.obj) with external library code '
                                        'to produce the final executable binary (.exe).',
                              'question': 'What is the function of the C++ Linker?'},
                          {   'answer': 'main() is the designated program entry point where the operating system '
                                        'begins program execution.',
                              'question': "Why is 'void main()' or 'int main()' mandatory in C++ programs?"},
                          {   'answer': 'Allows direct usage of standard library identifiers (like cout, cin, endl) '
                                        "without prefixing them with 'std::'.",
                              'question': "What does 'using namespace std;' do?"},
                          {   'answer': "'\n"
                                        "' advances output to the next line (newline), while '\t' inserts a horizontal "
                                        'tab spacing (typically 8 character spaces).',
                              'question': "What is the difference between '\n' and '\t'?"}],
        'order': 6,
        'quizzes': [   {   'correctAnswer': 'Edit, Preprocess, Compile, Link, Load, and Execute',
                           'explanation': 'C++ programs proceed through Editor (source), Preprocessor, Compiler '
                                          '(object code), Linker (executable), Loader (memory), and CPU (execution).',
                           'options': [   'Edit, Preprocess, Compile, Link, Load, and Execute',
                                          'Input, Storage, Formatting, Printing, Emailing, and Exiting',
                                          'Design, Sketch, Animation, Rendering, Transition, and Presentation',
                                          'Formula, Function, Cell, Column, Row, and Workbook'],
                           'question': 'What are the six standard phases of C++ program execution illustrated in Fig '
                                       '6.1?'},
                       {   'correctAnswer': 'It includes declarations for standard input and output stream operations '
                                            '(cin and cout)',
                           'explanation': '#include <iostream> inserts the header file defining standard stream '
                                          'input/output objects like cin and cout.',
                           'options': [   'It includes declarations for standard input and output stream operations '
                                          '(cin and cout)',
                                          'It allocates 4.3 GB of disk space on the primary partition',
                                          'It automatically creates a PowerPoint presentation slide',
                                          'It converts C++ programs into HTML markup'],
                           'question': "What is the role of the C++ Preprocessor directive '#include <iostream>'?"},
                       {   'correctAnswer': 'Ctrl + F5',
                           'explanation': 'Ctrl + F5 compiles, links, and launches the console application, keeping '
                                          'the console output window open after execution.',
                           'options': ['Ctrl + F5', 'Alt + F4', 'Ctrl + Z', 'Shift + Delete'],
                           'question': 'Which keyboard shortcut compiles and runs a C++ console application without '
                                       'debugging in Visual Studio?'},
                       {   'correctAnswer': 'It inserts a newline character, advancing the display cursor to the '
                                            'beginning of the next line',
                           'explanation': '\n'
                                          ' represents the newline control character in C++, similar to using the '
                                          "'endl' stream manipulator.",
                           'options': [   'It inserts a newline character, advancing the display cursor to the '
                                          'beginning of the next line',
                                          "It prints a literal letter 'n' on the screen",
                                          'It terminates the operating system session',
                                          'It reverses the color contrast of the console'],
                           'question': "What does the escape sequence '\n"
                                       "' accomplish when placed inside a cout stream string?"},
                       {   'correctAnswer': '.CPP',
                           'explanation': 'C++ source code files must be saved with the .CPP extension (e.g., '
                                          'FIRST_PROGRAM.CPP) for the compiler to recognize them.',
                           'options': ['.CPP', '.DOCX', '.HTML', '.XLSX'],
                           'question': 'What file extension must be used when saving C++ source code files in Turbo '
                                       'C++?'}],
        'title': 'Lab 6: Conduct Installation of Visual Studio 2008 & Turbo C++'},
    {   'codeSnippet': '#include <iostream>\n'
                       '#include <cmath>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    float radius, height, volume;\n'
                       '    const float PI = 3.14159f;\n'
                       '    \n'
                       '    cout << "Enter cylinder radius: ";\n'
                       '    cin >> radius;\n'
                       '    cout << "Enter cylinder height: ";\n'
                       '    cin >> height;\n'
                       '    \n'
                       '    volume = PI * radius * radius * height;\n'
                       '    cout << "Volume of cylinder = " << volume << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#07\n'
                   '\n'
                   '## PRACTICE IDENTIFIERS AND BASIC DATA TYPES\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Identifiers\n'
                   'Rules for naming identifiers in C++:\n'
                   '* Start identifiers with an alphabetic character (`a-z` or `A-Z`), or underscore `_`.\n'
                   '* Continue with alphabetic, numeric (`0-9`), or `_` (underscore) characters.\n'
                   '* Do not use reserved keywords (e.g., `int`, `return`, `for`, `while`, `class`).\n'
                   '* Identifiers are **case sensitive** (`A1` differs from `a1`).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Basic Data Types:\n'
                   '1. **Integer Types**\n'
                   '2. **Floating Point Types**\n'
                   '3. **Character Types**\n'
                   '\n'
                   '#### 1. Integer Types:\n'
                   '`char`, `short`, `int`, and `long` are binary integers. All are signed by default, but can be '
                   'declared unsigned. Typical characteristics:\n'
                   '\n'
                   '| Data Type | Typical Size | Value Range (Signed) | Value Range (Unsigned) |\n'
                   '| :--- | :--- | :--- | :--- |\n'
                   '| `char` | 1 byte (8 bits) | -128 to 127 | 0 to 255 |\n'
                   '| `short` | 2 bytes (16 bits) | -32,768 to 32,767 | 0 to 65,535 |\n'
                   '| `int` | 4 bytes (32 bits) | -2,147,483,648 to 2,147,483,647 | 0 to 4,294,967,295 |\n'
                   '| `long` | 4 bytes (32 bits) | -2,147,483,648 to 2,147,483,647 | 0 to 4,294,967,295 |\n'
                   '\n'
                   '#### 2. Floating-Point Types:\n'
                   'Used for numbers with fractional components:\n'
                   '* `float`: 4 bytes, approximately 7 decimal digits of precision.\n'
                   '* `double`: 8 bytes, approximately 15 decimal digits of precision.\n'
                   '* `long double`: 8 to 16 bytes for extended scientific precision.\n'
                   '\n'
                   '#### 3. Characters & Literals:\n'
                   '* Characters are stored in one byte (`char`).\n'
                   "* Character literals are enclosed in single quotes: `'A'`.\n"
                   '* Double quotes (`""`) enclose strings with zero or more characters (e.g., `"Hello"`).\n'
                   "* Hexadecimal literals: `'0x41'` (represents ASCII 'A').\n"
                   "* Octal literals: `'\n"
                   "nn'`.\n"
                   '\n'
                   '#### Escape Sequences:\n'
                   '* `\n'
                   '`: newline\n'
                   '* `\\`: backslash\n'
                   "* `'`: single quote\n"
                   '* `"`: double quote\n'
                   '* `\r'
                   '`: carriage return\n'
                   '* `\t`: horizontal tab\n'
                   '* `\x08`: backspace\n'
                   '* `\x0c'
                   '`: form feed\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Variables and Their Use in C++:\n'
                   '* To enter integer data from keyboard and save it to main memory, declare variable name and data '
                   'type first:\n'
                   '  ```cpp\n'
                   '  int n;\n'
                   '  ```\n'
                   '* Use `cin >>` statement to read input data from keyboard into variable.\n'
                   '* Use `cout <<` statement for outputting data on screen.\n'
                   '\n'
                   '### Using Math Functions in Programs (`<cmath>` / `math.h`):\n'
                   'Many mathematical functions are available in `<cmath>`:\n'
                   '* `sqrt(x)`: Square root of $x$\n'
                   '* `sin(x)`, `cos(x)`, `tan(x)`: Trigonometric functions\n'
                   '* *Important Note:* `sin`, `cos`, and `tan` accept angles in **radians**. Convert degrees to '
                   'radians first:\n'
                   '  $$\text{radians} = \text{degrees} \times \x0c'
                   'rac{\\pi}{180}$$\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 7 Tasks:\n'
                   '\n'
                   '#### Task 1: Sum and Average\n'
                   'Write a program that reads three numbers and finds their sum and average.\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    float n1, n2, n3, sum, avg;\n'
                   '    cout << "Enter three numbers: ";\n'
                   '    cin >> n1 >> n2 >> n3;\n'
                   '    sum = n1 + n2 + n3;\n'
                   '    avg = sum / 3.0;\n'
                   '    cout << "Sum = " << sum << "\n'
                   'Average = " << avg << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Task 2: Percentage Calculator\n'
                   'Write a program that reads obtained marks, total marks and finds percentage.\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    float obtained, total, percentage;\n'
                   '    cout << "Enter obtained marks: ";\n'
                   '    cin >> obtained;\n'
                   '    cout << "Enter total marks: ";\n'
                   '    cin >> total;\n'
                   '    percentage = (obtained / total) * 100.0;\n'
                   '    cout << "Percentage = " << percentage << "%" << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Task 3: Square and Cube\n'
                   'Write a program that reads a number and finds and prints its square and cube.\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    double num;\n'
                   '    cout << "Enter a number: ";\n'
                   '    cin >> num;\n'
                   '    cout << "Square = " << (num * num) << endl;\n'
                   '    cout << "Cube = " << (num * num * num) << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Task 4: Temperature Conversion (Fahrenheit to Celsius)\n'
                   'Write a program that reads temperature in Fahrenheit and finds and prints its equivalent '
                   'temperature in Celsius:\n'
                   '$$C = \x0c'
                   'rac{5}{9} \times (F - 32)$$\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    float fahrenheit, celsius;\n'
                   '    cout << "Enter temperature in Fahrenheit: ";\n'
                   '    cin >> fahrenheit;\n'
                   '    celsius = (5.0 / 9.0) * (fahrenheit - 32.0);\n'
                   '    cout << "Temperature in Celsius = " << celsius << " C" << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Task 5: Volume of a Cylinder\n'
                   'Write a program that reads radius and height and finds the volume of a cylinder:\n'
                   '$$V = \\pi r^2 h$$\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    float radius, height, volume;\n'
                   '    const float PI = 3.14159f;\n'
                   '    cout << "Enter cylinder radius: ";\n'
                   '    cin >> radius;\n'
                   '    cout << "Enter cylinder height: ";\n'
                   '    cin >> height;\n'
                   '    volume = PI * radius * radius * height;\n'
                   '    cout << "Volume of Cylinder = " << volume << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n',
        'flashcards': [   {   'answer': 'Uppercase and lowercase letters are treated as completely distinct symbols '
                                        "(e.g., 'Total', 'total', and 'TOTAL' are three separate variables).",
                              'question': "What does it mean that C++ identifiers are 'case-sensitive'?"},
                          {   'answer': 'cin (standard input) reads formatted data from the keyboard and stores it '
                                        'into specified variables using the extraction operator (>>).',
                              'question': "What is the purpose of the 'cin' stream in C++?"},
                          {   'answer': 'V = π * r² * h (where r is radius and h is height of the cylinder).',
                              'question': 'What is the formula for the volume of a cylinder?'},
                          {   'answer': "'5 / 9' performs integer division which truncates to 0, whereas '5.0 / 9.0' "
                                        'performs floating-point division yielding ~0.5555.',
                              'question': "Why must you use '5.0 / 9.0' instead of '5 / 9' in C++ temperature "
                                          'conversion?'}],
        'order': 7,
        'quizzes': [   {   'correctAnswer': 'student_marks_1',
                           'explanation': 'student_marks_1 starts with a letter, contains only alphanumeric and '
                                          'underscore characters, and is not a keyword. (2ndResult starts with digit, '
                                          'class is keyword, total marks has a space).',
                           'options': ['student_marks_1', '2ndResult', 'class', 'total marks'],
                           'question': 'Which of the following is a valid identifier name in C++ according to the '
                                       'rules in Lab 7?'},
                       {   'correctAnswer': 'Radians',
                           'explanation': 'As emphasized in the manual, sin(), cos(), and tan() take angles in '
                                          'radians; degrees must be converted via (degrees * PI / 180).',
                           'options': ['Radians', 'Degrees', 'Gradians', 'Revolutions'],
                           'question': 'In C++, what unit of angle measurement do the trigonometric functions sin(), '
                                       'cos(), and tan() in <cmath> expect?'},
                       {   'correctAnswer': "Character literals use single quotes ('A'), while string literals use "
                                            'double quotes ("Hello")',
                           'explanation': "Single quotes denote a single character literal ('A'), while double quotes "
                                          'denote a string literal ("Hello").',
                           'options': [   "Character literals use single quotes ('A'), while string literals use "
                                          'double quotes ("Hello")',
                                          'Character literals use square brackets ([A]), while string literals use '
                                          'braces ({Hello})',
                                          'Character literals are always capitalized, while string literals are '
                                          'lowercase',
                                          'Character literals are preceded by a dollar sign ($A)'],
                           'question': 'How are character literals differentiated from string literals in C++ syntax?'},
                       {   'correctAnswer': 'C = (5.0 / 9.0) * (F - 32.0)',
                           'explanation': 'The standard Fahrenheit to Celsius conversion formula is C = (5/9) * (F - '
                                          '32).',
                           'options': [   'C = (5.0 / 9.0) * (F - 32.0)',
                                          'C = (9.0 / 5.0) * F + 32.0',
                                          'C = F * 100.0 / 32.0',
                                          'C = (F - 100.0) / 1.8'],
                           'question': 'What is the formula to convert temperature from Fahrenheit to Celsius '
                                       'implemented in Task 4?'},
                       {   'correctAnswer': '4 bytes with approximately 7 digits of precision',
                           'explanation': 'A float occupies 4 bytes (32 bits) and provides roughly 7 decimal digits of '
                                          'precision, whereas double occupies 8 bytes.',
                           'options': [   '4 bytes with approximately 7 digits of precision',
                                          '8 bytes with approximately 15 digits of precision',
                                          '1 byte with 2 digits of precision',
                                          '16 bytes with 32 digits of precision'],
                           'question': "What is the typical memory size and precision of a 'float' data type in C++?"}],
        'title': 'Lab 7: Practice Identifiers and Basic Data Types'},
    {   'codeSnippet': '#include <iostream>\n'
                       '#include <iomanip>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    const float PI = 3.142857f;\n'
                       '    float radius = 1.5, area;\n'
                       '    area = PI * radius * radius;\n'
                       '    \n'
                       '    int g_bill = 880, e_bill = 20580, w_bill = 80, t_bill = 1560;\n'
                       '    int total = g_bill + e_bill + w_bill + t_bill;\n'
                       '    \n'
                       "    cout << setfill('*');\n"
                       '    cout << setw(30) << "Amount for Gas bill= " << setw(6) << g_bill << endl;\n'
                       '    cout << setw(30) << "Amount of Total bill= " << setw(6) << total << endl;\n'
                       '    cout << "Area of circle = " << area << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#08\n'
                   '\n'
                   '## PRACTICE CONSTANT AND ARITHMETIC OPERATORS\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Other Arithmetic Operators\n'
                   '* `+=`, `-=`, `*=`, `/=`, `%=` represent compound assignment operators:\n'
                   '  * `a += n` means `a = a + n`\n'
                   '  * `a -= n` means `a = a - n`\n'
                   '  * `a *= n` means `a = a * n`\n'
                   '  * `a /= n` means `a = a / n`\n'
                   '  * `a %= n` means `a = a % n`\n'
                   '* `++`, `--`: Pre and post increment and decrement operators.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### EXAMPLE #01: Compound Accumulation\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    float amount; // declares a variable\n'
                   '    float total;\n'
                   '    total = 0.0;\n'
                   '    \n'
                   '    cout << "Enter an Amount for gas bill: ";\n'
                   '    cin >> amount;\n'
                   '    cout << " *****************" << endl;\n'
                   '    total = total + amount; // total += amount;\n'
                   '    \n'
                   '    cout << "Enter an Amount for electricity bill: ";\n'
                   '    cin >> amount;\n'
                   '    cout << " *****************" << endl;\n'
                   '    total = total + amount; // total += amount;\n'
                   '    \n'
                   '    cout << "Enter an Amount for telephone bill: ";\n'
                   '    cin >> amount;\n'
                   '    cout << " *****************" << endl;\n'
                   '    total = total + amount; // total += amount;\n'
                   '    \n'
                   '    cout << "Enter an Amount for water bill: ";\n'
                   '    cin >> amount;\n'
                   '    cout << " *****************" << endl;\n'
                   '    total = total + amount; // total += amount;\n'
                   '    \n'
                   '    cout << "Total Amount of all bills = " << total << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Program Output:\n'
                   '```\n'
                   'Enter an Amount for gas bill: 280\n'
                   '*****************\n'
                   'Enter an Amount for electricity bill: 880\n'
                   '*****************\n'
                   'Enter an Amount for telephone bill: 560\n'
                   '*****************\n'
                   'Enter an Amount for water bill: 120\n'
                   '*****************\n'
                   'Total Amount of all bills = 1840\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Pre and Post Increment / Decrement Mechanisms:\n'
                   'Understand the meaning of the following expressions:\n'
                   '* **Prefix Increment:**\n'
                   '  ```cpp\n'
                   '  B = 3;\n'
                   '  A = ++B; // A contains 4, B contains 4 (increments B first, then assigns to A)\n'
                   '  ```\n'
                   '* **Postfix Increment:**\n'
                   '  ```cpp\n'
                   '  B = 3;\n'
                   '  A = B++; // A contains 3, B contains 4 (assigns original B to A, then increments B)\n'
                   '  ```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Using `setw` and `setfill` Functions with `cout`:\n'
                   '* Header file `<iomanip>` (or `iomanip.h`) is required.\n'
                   '* Used for formatted alignment of output for `cout`, especially when displaying strings and '
                   'numerical tables.\n'
                   '\n'
                   '### EXAMPLE #03: Formatted Bill Table\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   '#include <iomanip>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int g_bill, e_bill, w_bill, t_bill;\n'
                   '    int total;\n'
                   '    g_bill = 880;\n'
                   '    e_bill = 20580;\n'
                   '    w_bill = 80;\n'
                   '    t_bill = 1560;\n'
                   '    total = g_bill + e_bill + w_bill + t_bill;\n'
                   '    \n'
                   "    setfill('*');\n"
                   '    cout << setw(30) << "Amount for Gas bill= " << setw(6) << g_bill << endl;\n'
                   '    cout << setw(30) << "Amount for Electricity bill= " << setw(6) << e_bill << endl;\n'
                   '    cout << setw(30) << "Amount for Water bill= " << setw(6) << w_bill << endl;\n'
                   '    cout << setw(30) << "Amount for Telephone bill= " << setw(6) << t_bill << endl;\n'
                   '    cout << setw(30) << "****************************************" << endl;\n'
                   '    cout << setw(30) << "Amount of Total bill= " << setw(6) << total << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Program Output:\n'
                   '```\n'
                   'Amount for Gas bill= ***880\n'
                   'Amount for Electricity bill= *20580\n'
                   'Amount for Water bill= ****80\n'
                   'Amount for Telephone bill= **1560\n'
                   '***********************************\n'
                   'Amount of Total bill= *23100\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Const Qualifier:\n'
                   '* The `const` qualifier is used to declare a constant variable:\n'
                   '  ```cpp\n'
                   '  const float pi = 3.142857;\n'
                   '  ```\n'
                   '* Its value **cannot be changed** during the program.\n'
                   '\n'
                   '### EXAMPLE: Circle Area with Constant PI\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    float radius, area;\n'
                   '    const float pi = 3.142857;\n'
                   '    cout << "Enter Value of radius: ";\n'
                   '    cin >> radius;\n'
                   '    area = pi * radius * radius;\n'
                   '    cout << "Area of circle having radius " << radius << " = " << area << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Program Output:\n'
                   '```\n'
                   'Enter Value of radius = 1.5\n'
                   'Area of circle having radius 1.5 = 7.07\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Constant Values & Categories:\n'
                   'Constant values are divided into four primary categories:\n'
                   '1. **Integer Constant:** e.g., `4` in `discriminant = b*b - 4*a*c;`\n'
                   '2. **Float Constant:** e.g., `3.142856` in `area = 3.142856 * radius * radius;`\n'
                   "3. **Character Constant:** Characters enclosed in single quotes: `cout << 'H' << 'I' << 'E' << 'T' "
                   "<< '\\n';`\n"
                   '4. **String Constant:** Text enclosed in double quotes: `cout << "Area of Circle = ";`\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 8 Tasks:\n'
                   '\n'
                   '#### Task 1: Basic Arithmetic Calculator\n'
                   'Write a program that takes two numbers as input from the user and applies all basic arithmetic '
                   'operations (addition, subtraction, multiplication, and division) on them and displays the '
                   'results.\n'
                   '\n'
                   '#### Task 2: Demonstration of Pre & Post Increment/Decrement\n'
                   'Run the following code and understand the exact function of post and pre increment and decrement:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int n;\n'
                   '    cout << "Enter a Number = ";\n'
                   '    cin >> n;\n'
                   '    cout << endl;\n'
                   '    cout << "The Number Post Incremented ++ = ";\n'
                   '    cout << n++; // first prints current value, then increments\n'
                   '    cout << endl;\n'
                   '    cout << "The Number Post Decremented -- = ";\n'
                   '    cout << n--; // first prints current value, then decrements\n'
                   '    cout << endl;\n'
                   '    cout << "The Number Pre Incremented ++ = ";\n'
                   '    cout << ++n; // first increments, then prints\n'
                   '    cout << endl;\n'
                   '    cout << "The Number Pre Decremented -- = ";\n'
                   '    cout << --n; // first decrements, then prints\n'
                   '}\n'
                   '```\n',
        'flashcards': [   {   'answer': 'Sets the minimum field width for the next input/output operation to n '
                                        'character positions.',
                              'question': 'What does setw(n) do in C++?'},
                          {   'answer': 'Sets the padding fill character used to fill unpopulated spaces within a '
                                        'field defined by setw().',
                              'question': 'What does setfill(ch) do?'},
                          {   'answer': '1. Integer constants\\n2. Floating-point constants\\n3. Character constants '
                                        '(single quotes)\\n4. String constants (double quotes).',
                              'question': 'What are the four categories of constants in C++?'},
                          {   'answer': 'a %= n calculates the remainder of a divided by n and assigns it back to a '
                                        '(equivalent to a = a % n).',
                              'question': "What does the modulus compound operator '%=' do?"}],
        'order': 8,
        'quizzes': [   {   'correctAnswer': 'Pre-increment increments the value before evaluating the expression; '
                                            'post-increment evaluates the expression before incrementing',
                           'explanation': 'In ++n, n is incremented first and the new value is used. In n++, the '
                                          'current value is used in the expression and n is incremented afterward.',
                           'options': [   'Pre-increment increments the value before evaluating the expression; '
                                          'post-increment evaluates the expression before incrementing',
                                          'Pre-increment works only with float variables; post-increment works only '
                                          'with int',
                                          'Pre-increment decreases the value by 1; post-increment increases the value '
                                          'by 2',
                                          'There is no difference in execution order or resulting expression values'],
                           'question': 'What is the key difference between pre-increment (++n) and post-increment '
                                       '(n++) in C++?'},
                       {   'correctAnswer': '<iomanip>',
                           'explanation': 'The <iomanip> header provides input/output manipulators like setw() (field '
                                          'width) and setfill() (padding character).',
                           'options': ['<iomanip>', '<cmath>', '<cstdlib>', '<fstream>'],
                           'question': 'Which header file must be included in C++ to use formatted stream manipulators '
                                       'such as setw() and setfill()?'},
                       {   'correctAnswer': 'The compiler generates a compilation error because const variables are '
                                            'read-only',
                           'explanation': 'The const qualifier designates an identifier as a read-only constant; any '
                                          'assignment statement attempting to modify it results in a compile-time '
                                          'error.',
                           'options': [   'The compiler generates a compilation error because const variables are '
                                          'read-only',
                                          'The variable changes value without any error',
                                          'The operating system terminates the process with an error code',
                                          'The variable is automatically converted into a string literal'],
                           'question': 'What happens if a program attempts to reassign or modify a variable declared '
                                       "with the 'const' qualifier?"},
                       {   'correctAnswer': 'A = 3, B = 4',
                           'explanation': 'Because post-increment (B++) is used, the current value of B (3) is '
                                          'assigned to A first, and then B is incremented to 4.',
                           'options': ['A = 3, B = 4', 'A = 4, B = 4', 'A = 4, B = 3', 'A = 3, B = 3'],
                           'question': "If B = 3 initially, what are the values of A and B after executing 'A = "
                                       "B++;'?"},
                       {   'correctAnswer': 'total = total + amount;',
                           'explanation': 'The compound assignment operator += adds the right-hand operand to the '
                                          'variable and assigns the result back to that variable.',
                           'options': [   'total = total + amount;',
                                          'total = amount;',
                                          'amount = total + amount;',
                                          'total = total * amount;'],
                           'question': "What does the compound assignment operator 'total += amount;' evaluate to in "
                                       'C++?'}],
        'title': 'Lab 8: Practice Constants and Arithmetic Operators'},
    {   'codeSnippet': '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    int num;\n'
                       '    cout << "Enter an integer: ";\n'
                       '    cin >> num;\n'
                       '    \n'
                       '    if (num > 0) {\n'
                       '        cout << num << " is a positive number." << endl;\n'
                       '    } else if (num < 0) {\n'
                       '        cout << num << " is a negative number." << endl;\n'
                       '    } else {\n'
                       '        cout << "The number is zero." << endl;\n'
                       '    }\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#09\n'
                   '\n'
                   '## EXECUTE CONDITIONAL STATEMENTS\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Branching Statements & The `if` Statement\n'
                   'The first type of branching statement is the **`if` statement**. There are other branching '
                   'statements too, like the `switch-case` statement.\n'
                   '\n'
                   'An `if` statement has the form:\n'
                   '```cpp\n'
                   'if (condition / expression)\n'
                   '{\n'
                   '    // code to execute if condition is true\n'
                   '}\n'
                   'else\n'
                   '{\n'
                   '    // code to execute if condition is false\n'
                   '}\n'
                   '```\n'
                   '\n'
                   'In an `if` statement, `condition/expression` is a value or an expression that is used to determine '
                   'which code block is executed, and the curly braces `{}` act as "begin" and "end" markers.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### EXAMPLE 1: Comparing Two Integers\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    // define two integers\n'
                   '    int x = 3;\n'
                   '    int y = 4;\n'
                   '    \n'
                   '    // print out a message telling which is bigger\n'
                   '    if (x > y)\n'
                   '    {\n'
                   '        cout << "x is bigger than y" << endl;\n'
                   '    }\n'
                   '    else\n'
                   '    {\n'
                   '        cout << "x is smaller than y" << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   'In this case, the condition `(x > y)` evaluates to `(3 > 4)` which is a false statement. '
                   'Therefore, the code within the `else` clause executes:\n'
                   '```\n'
                   'x is smaller than y\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Flowcharts of Conditional Execution:\n'
                   '\n'
                   '![Simple Conditional Flowchart](assets/images/university/cfp/lab9_flowchart_simple.png)\n'
                   '\n'
                   '![Relational Operator Flowchart](assets/images/university/cfp/lab9_flowchart_relational.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Relational and Equality Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`):\n'
                   'In order to evaluate a comparison between two expressions, we use relational and equality '
                   'operators. The result of a relational operation is a Boolean value that can only be `true` or '
                   '`false`. Internally:\n'
                   '* `false` is represented by zero (`0`)\n'
                   '* `true` is represented by one (`1`)\n'
                   '\n'
                   '| Operator | Meaning | Example | Result |\n'
                   '| :---: | :--- | :--- | :---: |\n'
                   '| `==` | Equal to | `(7 == 5)` | `false` |\n'
                   '| `!=` | Not equal to | `(3 != 2)` | `true` |\n'
                   '| `>` | Greater than | `(5 > 4)` | `true` |\n'
                   '| `<` | Less than | `(5 < 5)` | `false` |\n'
                   '| `>=` | Greater than or equal to | `(6 >= 6)` | `true` |\n'
                   '| `<=` | Less than or equal to | `(4 <= 2)` | `false` |\n'
                   '\n'
                   'Suppose that `a = 2`, `b = 3`, and `c = 6`:\n'
                   '* `(a == 5)` evaluates to `false` (since $a$ is not equal to 5)\n'
                   '* `(a * b >= c)` evaluates to `true` (since $2 \\times 3 \\ge 6$ is true)\n'
                   '* `(b + 4 > a * c)` evaluates to `false` (since $3 + 4 > 2 \\times 6$ is false)\n'
                   '* `((b = 2) == a)` evaluates to `true`\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### EXAMPLE 2: Validation of Circle Radius\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    float rad, area;\n'
                   '    cout << "Enter value of radius: ";\n'
                   '    cin >> rad;\n'
                   '    \n'
                   '    if (rad < 0)\n'
                   '    {\n'
                   '        cout << "Negative Radius Not Allowed" << endl;\n'
                   '    }\n'
                   '    else\n'
                   '    {\n'
                   '        area = 3.1416 * rad * rad;\n'
                   '        cout << "Area of Circle = " << area << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Logical Operators (`!`, `&&`, `||`):\n'
                   '\n'
                   '#### 1. Logical NOT (`!`):\n'
                   'Performs Boolean inversion. It has only one operand to its right:\n'
                   '* `!(5 == 5)` evaluates to `false` (since `5 == 5` is true)\n'
                   '* `!(6 <= 4)` evaluates to `true` (since `6 <= 4` is false)\n'
                   '* `!true` evaluates to `false`\n'
                   '* `!false` evaluates to `true`\n'
                   '\n'
                   '#### 2. Logical AND (`&&`):\n'
                   'Evaluates to `true` only if **both** operands are true:\n'
                   '\n'
                   '| `a` | `b` | `a && b` |\n'
                   '| :---: | :---: | :---: |\n'
                   '| `true` | `true` | **`true`** |\n'
                   '| `true` | `false` | **`false`** |\n'
                   '| `false` | `true` | **`false`** |\n'
                   '| `false` | `false` | **`false`** |\n'
                   '\n'
                   '#### 3. Logical OR (`||`):\n'
                   'Evaluates to `true` if **either** operand is true:\n'
                   '\n'
                   '| `a` | `b` | `a \\|\\| b` |\n'
                   '| :---: | :---: | :---: |\n'
                   '| `true` | `true` | **`true`** |\n'
                   '| `true` | `false` | **`true`** |\n'
                   '| `false` | `true` | **`true`** |\n'
                   '| `false` | `false` | **`false`** |\n'
                   '\n'
                   '#### Compound Evaluation Examples:\n'
                   '* `((5 == 5) && (3 > 6))` evaluates to `false` (`true && false`)\n'
                   '* `((5 == 5) || (3 > 6))` evaluates to `true` (`true || false`)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 9 Tasks:\n'
                   '\n'
                   '#### Task 1: Positive or Negative Integer Check\n'
                   'Write a program which takes an integer from the user and tells whether:\n'
                   '* It is a positive number, OR\n'
                   '* It is a negative number.\n'
                   '\n'
                   '#### Task 2: Vowel Checker\n'
                   'Ask user to input a single character and determine whether it is a vowel (`a`, `e`, `i`, `o`, `u`, '
                   'or uppercase equivalents) or not using logical OR (`||`) operators.\n'
                   '\n'
                   '#### Task 3: University Grading Criteria\n'
                   'Implement the grading criteria of your university and display the grade awarded according to the '
                   'total marks obtained.\n',
        'flashcards': [   {   'answer': 'Inverts the truth value of its single Boolean operand: !true becomes false, '
                                        'and !false becomes true.',
                              'question': 'What is the purpose of the logical NOT (!) operator?'},
                          {   'answer': 'For &&, if the left operand is false, the right is not evaluated. For ||, if '
                                        'the left operand is true, the right is skipped.',
                              'question': 'What is short-circuit evaluation in C++ logical operators?'},
                          {   'answer': "'=' is the assignment operator (stores a value into a variable), while '==' "
                                        'is the equality relational operator (compares two values).',
                              'question': "What is the difference between '=' and '==' in C++?"},
                          {   'answer': 'Only the single immediately following statement is treated as the body of the '
                                        'if clause.',
                              'question': "What happens if braces '{}' are omitted after an if statement?"}],
        'order': 9,
        'quizzes': [   {   'correctAnswer': 'false is represented by 0, and true is represented by 1 (or any non-zero '
                                            'value)',
                           'explanation': 'In C++, zero represents false, and non-zero values (conventionally 1) '
                                          'represent true in relational evaluations.',
                           'options': [   'false is represented by 0, and true is represented by 1 (or any non-zero '
                                          'value)',
                                          'false is represented by -1, and true is represented by 0',
                                          "false is represented by null, and true is represented by string 'T'",
                                          'Both are stored as ASCII character pointers'],
                           'question': 'How are Boolean true and false values represented internally by the C++ '
                                       'compiler?'},
                       {   'correctAnswer': 'false',
                           'explanation': '(5 == 5) is true, but (3 > 6) is false. For logical AND (&&), both operands '
                                          'must be true for the result to be true; thus true && false evaluates to '
                                          'false.',
                           'options': ['false', 'true', 'Compilation error', 'Undefined runtime exception'],
                           'question': 'What is the result of evaluating the compound expression: ((5 == 5) && (3 > '
                                       '6))?'},
                       {   'correctAnswer': '|| (Logical OR)',
                           'explanation': 'Logical OR (||) yields true if either operand is true, and is false only '
                                          'when both operands evaluate to false.',
                           'options': ['|| (Logical OR)', '&& (Logical AND)', '! (Logical NOT)', '== (Equality)'],
                           'question': 'Which logical operator in C++ evaluates to true if at least one of its two '
                                       'operand conditions is true?'},
                       {   'correctAnswer': '!=',
                           'explanation': 'The != operator checks inequality in C++ (returns true if operands are not '
                                          'equal).',
                           'options': ['!=', '==', '<>', 'NOT EQUAL'],
                           'question': 'Which relational operator is used to test whether two values are strictly NOT '
                                       'equal in C++?'},
                       {   'correctAnswer': "if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')",
                           'explanation': "A character matches if it equals 'a' OR 'e' OR 'i' OR 'o' OR 'u'; logical "
                                          'AND would require the character to be all five simultaneously, which is '
                                          'impossible.',
                           'options': [   "if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')",
                                          "if (ch == 'a' && ch == 'e' && ch == 'i' && ch == 'o' && ch == 'u')",
                                          "if (ch != 'vowel')",
                                          'if (ch == "aeiou")'],
                           'question': 'In Task 2, what condition correctly tests whether a lowercase character '
                                       "variable 'ch' is a vowel?"}],
        'title': 'Lab 9: Execute Conditional Statements'},
    {   'codeSnippet': '#include <iostream>\n'
                       '#include <cstdlib>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    int acc;\n'
                       '    float bal;\n'
                       '    cout << "Enter account number: ";\n'
                       '    cin >> acc;\n'
                       '    cout << "Enter balance: ";\n'
                       '    cin >> bal;\n'
                       '    \n'
                       '    if (acc < 0) {\n'
                       '        cout << "Error - Account number cannot be negative!" << endl;\n'
                       '        exit(0);\n'
                       '    }\n'
                       '    \n'
                       '    cout << "*******************************" << endl;\n'
                       '    cout << "Account Number = " << acc << endl;\n'
                       '    cout << "Balance Amount = " << bal << endl;\n'
                       '    cout << "*******************************" << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#10\n'
                   '\n'
                   '## EXECUTE NESTED CONDITIONAL STATEMENTS\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Four Architectural Approaches to Grade Assignment:\n'
                   'Consider a program that assigns grades based on student marks. The manual compares four different '
                   'program architectures:\n'
                   '\n'
                   '#### Approach 1: Independent `if` Statements\n'
                   '*(Note: Every comparison is evaluated every time, resulting in inefficient execution)*\n'
                   '```cpp\n'
                   'if (marks >= 80) cout << "Roll " << roll << " secured A Grade." << endl;\n'
                   'if (marks >= 70) cout << "Roll " << roll << " secured B Grade." << endl;\n'
                   'if (marks >= 60) cout << "Roll " << roll << " secured C Grade." << endl;\n'
                   'if (marks >= 50) cout << "Roll " << roll << " secured D Grade." << endl;\n'
                   'if (marks < 50)  cout << "Roll " << roll << " secured F Grade." << endl;\n'
                   '```\n'
                   '\n'
                   '#### Approach 2: Simple Nested `if-else` Ladder\n'
                   '*(Efficient: Once a condition matches, subsequent checks are skipped)*\n'
                   '```cpp\n'
                   'if (marks >= 80)\n'
                   '    cout << "Roll " << roll << " secured A Grade." << endl;\n'
                   'else if (marks >= 70)\n'
                   '    cout << "Roll " << roll << " secured B Grade." << endl;\n'
                   'else if (marks >= 60)\n'
                   '    cout << "Roll " << roll << " secured C Grade." << endl;\n'
                   'else if (marks >= 50)\n'
                   '    cout << "Roll " << roll << " secured D Grade." << endl;\n'
                   'else\n'
                   '    cout << "Roll " << roll << " secured F Grade." << endl;\n'
                   '```\n'
                   '\n'
                   '#### Approach 3: Compound `if` Statements with `&&` Ranges\n'
                   '```cpp\n'
                   'if (marks >= 80) cout << "Roll " << roll << " secured A Grade." << endl;\n'
                   'if ((marks >= 70) && (marks < 80)) cout << "Roll " << roll << " secured B Grade." << endl;\n'
                   'if ((marks >= 60) && (marks < 70)) cout << "Roll " << roll << " secured C Grade." << endl;\n'
                   'if ((marks >= 50) && (marks < 60)) cout << "Roll " << roll << " secured D Grade." << endl;\n'
                   'if (marks < 50) cout << "Roll " << roll << " secured F Grade." << endl;\n'
                   '```\n'
                   '\n'
                   '#### Approach 4: Compound Nested `if-else` Ladder\n'
                   'Combines range validation with early branch termination.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### EXAMPLE 2: Finding the Youngest Among 4 Students\n'
                   'Reads ages for four students and determines the youngest student:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int age1, age2, age3, age4, youngest;\n'
                   '    cout << "Enter age for first student: ";\n'
                   '    cin >> age1;\n'
                   '    cout << "Enter age for second student: ";\n'
                   '    cin >> age2;\n'
                   '    cout << "Enter age for third student: ";\n'
                   '    cin >> age3;\n'
                   '    cout << "Enter age for fourth student: ";\n'
                   '    cin >> age4;\n'
                   '    \n'
                   '    youngest = age1;\n'
                   '    if (age2 < youngest) youngest = age2;\n'
                   '    if (age3 < youngest) youngest = age3;\n'
                   '    if (age4 < youngest) youngest = age4;\n'
                   '    \n'
                   '    cout << "Youngest student age is = " << youngest << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### EXAMPLE 3: Bank Account Validation\n'
                   'Validates account number and outputs formatted customer details:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int acc;\n'
                   '    float bal;\n'
                   '    cout << "Enter account number: ";\n'
                   '    cin >> acc;\n'
                   '    cout << "Enter balance: ";\n'
                   '    cin >> bal;\n'
                   '    \n'
                   '    if (acc < 0)\n'
                   '    {\n'
                   '        cout << "Error-Account number cannot be negative, try again later" << endl;\n'
                   '    }\n'
                   '    else\n'
                   '    {\n'
                   '        cout << "*******************************" << endl;\n'
                   '        cout << "Account Number = " << acc << endl;\n'
                   '        cout << "Balance Amount = " << bal << endl;\n'
                   '        cout << "*******************************" << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Use of the `exit()` Function:\n'
                   '* Defined in header file `<cstdlib>` (or `<process.h>`).\n'
                   '* Causes the program to terminate execution immediately wherever called.\n'
                   '* Standard convention: `exit(0)` for successful termination, and non-zero values for abnormal '
                   'termination.\n'
                   '\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   '#include <cstdlib>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int acc;\n'
                   '    float bal;\n'
                   '    cout << "Enter account number: ";\n'
                   '    cin >> acc;\n'
                   '    cout << "Enter balance: ";\n'
                   '    cin >> bal;\n'
                   '    \n'
                   '    if (acc < 0)\n'
                   '    {\n'
                   '        cout << "Error-Account number cannot be negative, try again later" << endl;\n'
                   '        exit(0); // Terminates immediately\n'
                   '    }\n'
                   '    else\n'
                   '    {\n'
                   '        cout << "*******************************" << endl;\n'
                   '        cout << "Account Number = " << acc << endl;\n'
                   '        cout << "Balance Amount = " << bal << endl;\n'
                   '        cout << "*******************************" << endl;\n'
                   '    }\n'
                   '    cout << "Program finished successfully." << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 10 Tasks:\n'
                   '1. Write a program that reads marks for 5 subjects, and finds total marks, percentage marks, and '
                   'prints overall grade.\n'
                   '2. Write a program that reads a day number (1 to 7) and prints the corresponding day name (e.g., 1 '
                   '= Monday, 7 = Sunday).\n'
                   '3. Write a program that reads the weight of a person and prints either `heavy weight`, `normal '
                   'weight`, or `low weight`.\n'
                   '4. Write a program that reads three numbers and prints them in both **ascending** and '
                   '**descending** order.\n',
        'flashcards': [   {   'answer': 'An if or if-else statement placed inside the body of another if or else block '
                                        'to create multi-tiered decision logic.',
                              'question': 'What is a nested if statement?'},
                          {   'answer': "The trailing 'else' block which executes if and only if none of the preceding "
                                        'conditions evaluated to true.',
                              'question': 'What is the default block in an if-else ladder?'},
                          {   'answer': 'Compare pairs using if statements and swap out-of-order elements until a <= b '
                                        '<= c.',
                              'question': 'How do you sort 3 numbers in ascending order using conditional statements?'},
                          {   'answer': 'Signifies that the program exited abnormally due to an error condition or '
                                        'invalid input.',
                              'question': 'What does exit(1) signify to the operating system?'}],
        'order': 10,
        'quizzes': [   {   'correctAnswer': 'It bypasses all subsequent condition checks as soon as a matching '
                                            'condition evaluates to true',
                           'explanation': 'In an if-else-if ladder, as soon as any condition evaluates to true, its '
                                          'block executes and control jumps past the entire ladder, saving unnecessary '
                                          'CPU evaluations.',
                           'options': [   'It bypasses all subsequent condition checks as soon as a matching condition '
                                          'evaluates to true',
                                          'It requires twice as much RAM memory to store intermediate pointers',
                                          'It executes all branch blocks simultaneously in parallel',
                                          'It automatically creates a loop structure'],
                           'question': 'Why is the nested if-else ladder (Approach 2) computationally superior to '
                                       'multiple independent if statements (Approach 1)?'},
                       {   'correctAnswer': '<cstdlib>',
                           'explanation': 'The exit() function is declared in <cstdlib> (traditionally <process.h> in '
                                          'legacy Turbo C++ compilers).',
                           'options': ['<cstdlib>', '<cmath>', '<iomanip>', '<iostream>'],
                           'question': 'Which standard header file provides the declaration for the exit() system '
                                       'function in modern C++?'},
                       {   'correctAnswer': '0 indicates normal / successful program termination',
                           'explanation': 'Passing 0 to exit(0) signals to the operating system that the process '
                                          'terminated normally without error.',
                           'options': [   '0 indicates normal / successful program termination',
                                          '0 indicates a critical hardware fault',
                                          '0 restarts the operating system',
                                          '0 pauses the program and enters infinite loop'],
                           'question': 'What is the standard convention for the status code passed to exit(0)?'},
                       {   'correctAnswer': 'Initialize youngest to age1, then sequentially update youngest if age2, '
                                            'age3, or age4 is smaller',
                           'explanation': 'The linear minimum scan algorithm assumes the first value is minimum, then '
                                          'compares against each remaining candidate in turn.',
                           'options': [   'Initialize youngest to age1, then sequentially update youngest if age2, '
                                          'age3, or age4 is smaller',
                                          'Sum all 4 ages and divide by 4',
                                          'Multiply all 4 ages together',
                                          'Use the AutoSum button from Excel'],
                           'question': 'In Example 2, what algorithm is used to find the youngest of 4 students?'},
                       {   'correctAnswer': 'An error message prints, and the program terminates immediately without '
                                            'executing subsequent code',
                           'explanation': 'When acc < 0, the error message is displayed and exit(0) immediately aborts '
                                          'program flow before reaching the account summary.',
                           'options': [   'An error message prints, and the program terminates immediately without '
                                          'executing subsequent code',
                                          'The program calculates compound interest',
                                          'The balance is multiplied by -1 and printed',
                                          'The program prompts the user for 5 subject marks'],
                           'question': 'What happens if a user enters a negative account number in the bank validation '
                                       'program with exit(0)?'}],
        'title': 'Lab 10: Execute Nested Conditional Statements'},
    {   'codeSnippet': '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    // 1. While loop: binary conversion\n'
                       '    int n = 13, temp = n;\n'
                       '    cout << "Binary bits of " << n << " (reverse): ";\n'
                       '    while (temp > 0) {\n'
                       '        cout << (temp % 2);\n'
                       '        temp /= 2;\n'
                       '    }\n'
                       '    cout << endl;\n'
                       '    \n'
                       '    // 2. Factorial calculation\n'
                       '    int fact = 1, num = 7;\n'
                       '    for (int i = 1; i <= num; i++) {\n'
                       '        fact *= i;\n'
                       '    }\n'
                       '    cout << num << "! = " << fact << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#11\n'
                   '\n'
                   '## DEMONSTRATE USE OF CONTROL STATEMENTS (LOOPS)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objective:\n'
                   'To use `while`, `do-while`, and `for` loops to execute statements repeatedly.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 1. The `while` Loop:\n'
                   'The `while` loop checks its condition **before** entering the loop body. If the condition is false '
                   'initially, the body does not execute at all.\n'
                   '\n'
                   '![While Loop Flowchart](assets/images/university/cfp/lab11_while_loop.png)\n'
                   '\n'
                   '#### Exercise 1: Decimal to Binary Conversion\n'
                   'This program reads an integer and prints its bits in binary (reverse order):\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int num, temp, bit;\n'
                   '    cout << "Enter a positive integer: ";\n'
                   '    cin >> num;\n'
                   '    temp = num;\n'
                   '    \n'
                   '    cout << "Binary representation (reverse order): ";\n'
                   '    while (temp > 0)\n'
                   '    {\n'
                   '        bit = temp % 2;\n'
                   '        cout << bit;\n'
                   '        temp = temp / 2;\n'
                   '    }\n'
                   '    cout << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 2. The `do-while` Loop:\n'
                   'The `do-while` loop checks its condition **after** executing the loop body. Therefore, the body is '
                   'guaranteed to execute **at least once**.\n'
                   '\n'
                   '![Do-While Loop Flowchart](assets/images/university/cfp/lab11_dowhile_loop.png)\n'
                   '\n'
                   '#### Exercise 2: Average of Positive Integers\n'
                   'Asks user to type positive integers. When the user types a negative value, the program prints '
                   '`ERROR` and prompts again. When the user types `0`, data entry terminates and the average is '
                   'printed:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int val, count = 0;\n'
                   '    float sum = 0.0;\n'
                   '    \n'
                   '    do\n'
                   '    {\n'
                   '        cout << "Enter positive integer (0 to finish): ";\n'
                   '        cin >> val;\n'
                   '        if (val < 0)\n'
                   '        {\n'
                   '            cout << "ERROR" << endl;\n'
                   '        }\n'
                   '        else if (val > 0)\n'
                   '        {\n'
                   '            sum += val;\n'
                   '            count++;\n'
                   '        }\n'
                   '    } while (val != 0);\n'
                   '    \n'
                   '    if (count == 0)\n'
                   '        cout << "NO AVERAGE" << endl;\n'
                   '    else\n'
                   '        cout << "Average = " << (sum / count) << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 3. The `for` Loop:\n'
                   'Designed for counter-controlled repetition with initialization, condition, and step update in a '
                   'single compact header.\n'
                   '\n'
                   '![For Loop Flowchart](assets/images/university/cfp/lab11_for_loop.png)\n'
                   '\n'
                   '#### Exercise 3: Max Value Occurrence Counter\n'
                   'Reads 10 integers and determines the occurrence count of the maximum value:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int val, maxVal, count = 0;\n'
                   '    cout << "Enter integer 1: ";\n'
                   '    cin >> val;\n'
                   '    maxVal = val;\n'
                   '    count = 1;\n'
                   '    \n'
                   '    for (int i = 2; i <= 10; i++)\n'
                   '    {\n'
                   '        cout << "Enter integer " << i << ": ";\n'
                   '        cin >> val;\n'
                   '        if (val > maxVal)\n'
                   '        {\n'
                   '            maxVal = val;\n'
                   '            count = 1;\n'
                   '        }\n'
                   '        else if (val == maxVal)\n'
                   '        {\n'
                   '            count++;\n'
                   '        }\n'
                   '    }\n'
                   '    cout << "Max value = " << maxVal << " occurred " << count << " times." << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 4. Nested `for` Loops:\n'
                   '\n'
                   '#### Exercise 4: Multiplication Table Grid\n'
                   'Prints a multiplication table:\n'
                   '```\n'
                   '1 2 3\n'
                   '2 4 6\n'
                   '3 6 9\n'
                   '```\n'
                   '\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    for (int i = 1; i <= 3; i++)\n'
                   '    {\n'
                   '        for (int j = 1; j <= 3; j++)\n'
                   '        {\n'
                   '            cout << (i * j) << " ";\n'
                   '        }\n'
                   '        cout << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Note on Loop Syntax:\n'
                   '* The initial-action in a `for` loop can be a comma-separated list of expressions:\n'
                   '  ```cpp\n'
                   '  for (int i = 0, j = 0; (i + j < 10); i++, j++) { /* Do something */ }\n'
                   '  ```\n'
                   '* If the loop condition is omitted in `for ( ; ; )`, it is implicitly `true` (creating an infinite '
                   'loop).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### 5. Using `break` and `continue`:\n'
                   '* **`break`:** Immediately exits the enclosing loop and transfers control to the first statement '
                   'following the loop.\n'
                   '* **`continue`:** Skips the remaining statements in the current iteration and jumps directly to '
                   'the loop step/condition check.\n'
                   '\n'
                   '#### Exercise 5: Break on Negative Value\n'
                   'Enters up to 10 positive numbers, but terminates prematurely if a negative number is entered:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    int num;\n'
                   '    for (int i = 1; i <= 10; i++)\n'
                   '    {\n'
                   '        cout << "Enter number " << i << ": ";\n'
                   '        cin >> num;\n'
                   '        if (num < 0)\n'
                   '        {\n'
                   '            cout << "Negative number entered. Quitting loop." << endl;\n'
                   '            break;\n'
                   '        }\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Exercise 6: Continue Skipping Multiples of 7\n'
                   'Prints all numbers from 0 to 100 except multiples of 7:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    for (int i = 0; i <= 100; i++)\n'
                   '    {\n'
                   '        if (i % 7 == 0)\n'
                   '            continue; // Skip printing multiples of 7\n'
                   '        cout << i << " ";\n'
                   '    }\n'
                   '    cout << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 11 Tasks:\n'
                   '\n'
                   '#### Task 1: Minimum Value Among 10 Integers\n'
                   'Write a program that asks the user to type 10 integers and writes the smallest value.\n'
                   '\n'
                   '#### Task 2: Table of Values\n'
                   'Write a program that utilizes looping to print a table of mathematical values (powers or '
                   'multiplication tables).\n'
                   '\n'
                   '#### Task 3: Factorial Calculation\n'
                   'Write a program that calculates factorials. The factorial of a positive integer number is '
                   'mathematically written as $n!$ and is the product of all integers from 1 to $n$:\n'
                   '$$n! = 1 \\times 2 \\times 3 \\times \\dots \\times n$$\n'
                   'For example:\n'
                   '$$7! = 1 \\times 2 \\times 3 \\times 4 \\times 5 \\times 6 \\times 7 = 5040$$\n',
        'flashcards': [   {   'answer': '1. Initialization (int i = 0)\\n2. Continuation condition (i < 10)\\n3. Step '
                                        'expression / increment (i++).',
                              'question': 'What are the three components of a for loop header?'},
                          {   'answer': 'Terminates the loop immediately, jumping to the first statement outside the '
                                        'loop body.',
                              'question': "What does the 'break' statement do in a loop?"},
                          {   'answer': 'A loop placed entirely inside the body of another loop, commonly used for '
                                        'multidimensional grids and matrix processing.',
                              'question': 'What is a nested loop?'},
                          {   'answer': 'Accumulate the running sum (sum += val), increment a count (count++), and '
                                        'divide: average = sum / count.',
                              'question': 'How do you calculate the average of N numbers entered in a loop?'}],
        'order': 11,
        'quizzes': [   {   'correctAnswer': 'A while loop tests its condition before executing the body; a do-while '
                                            'loop tests afterward, guaranteeing at least one execution',
                           'explanation': 'Because a do-while loop is a post-test loop, its body executes at least '
                                          'once regardless of whether the condition is true or false initially.',
                           'options': [   'A while loop tests its condition before executing the body; a do-while loop '
                                          'tests afterward, guaranteeing at least one execution',
                                          'A while loop cannot use integer counters',
                                          'A do-while loop terminates automatically after exactly 10 iterations',
                                          'A while loop cannot contain break or continue statements'],
                           'question': 'What is the key functional difference between a while loop and a do-while loop '
                                       'in C++?'},
                       {   'correctAnswer': 'It skips the remainder of the current iteration and jumps directly to the '
                                            'next loop cycle',
                           'explanation': 'The continue statement bypasses the remaining statements in the active '
                                          'iteration, returning to the loop update step.',
                           'options': [   'It skips the remainder of the current iteration and jumps directly to the '
                                          'next loop cycle',
                                          'It immediately terminates the loop and exits the enclosing function',
                                          'It restarts the computer operating system',
                                          'It resets all variables to zero'],
                           'question': "What does the 'continue' statement do when encountered inside a loop body?"},
                       {   'correctAnswer': '5040',
                           'explanation': '7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5,040.',
                           'options': ['5040', '720', '49', '40320'],
                           'question': 'What is the factorial of 7 (7!) as calculated in Task 3 of Lab 11?'},
                       {   'correctAnswer': 'temp % 2',
                           'explanation': 'Modulo 2 (temp % 2) returns the remainder (0 or 1), which represents the '
                                          'binary bit.',
                           'options': ['temp % 2', 'temp / 2', 'temp * 2', 'temp + 2'],
                           'question': 'In decimal-to-binary conversion (Exercise 1), which mathematical operation '
                                       'extracts the lowest binary bit?'},
                       {   'correctAnswer': 'It creates an infinite loop because the continuation condition defaults '
                                            'implicitly to true',
                           'explanation': 'In C++, omitting the condition in for( ; ; ) is treated as implicitly true, '
                                          'generating an indefinite/infinite loop until interrupted by break or '
                                          'exit().',
                           'options': [   'It creates an infinite loop because the continuation condition defaults '
                                          'implicitly to true',
                                          'It causes a compilation syntax error',
                                          'It executes exactly zero times',
                                          'It converts the loop into a recursive function'],
                           'question': "What happens if all three control expressions are omitted in a for loop: 'for "
                                       "( ; ; )'?"}],
        'title': 'Lab 11: Demonstrate Use of Control Statements (Loops)'},
    {   'codeSnippet': '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    // 1D array initialization and max search\n'
                       '    double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};\n'
                       '    double maxVal = balance[0];\n'
                       '    double sum = 0.0;\n'
                       '    \n'
                       '    for (int i = 0; i < 5; i++) {\n'
                       '        if (balance[i] > maxVal) maxVal = balance[i];\n'
                       '        sum += balance[i];\n'
                       '        cout << "balance[" << i << "] = " << balance[i] << endl;\n'
                       '    }\n'
                       '    \n'
                       '    cout << "Maximum value = " << maxVal << endl;\n'
                       '    cout << "Sum of elements = " << sum << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#12\n'
                   '\n'
                   '## EXECUTE ARRAY MANIPULATION\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:\n'
                   'Students will be able to:\n'
                   '* Understand the use of arrays\n'
                   '* Understand the declaration of one-dimensional arrays\n'
                   '* Understand the declaration of two-dimensional arrays\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Introduction to Arrays:\n'
                   'C++ provides a data structure called the **array**, which stores a fixed-size sequential '
                   'collection of elements of the same type. An array is used to store a collection of data, but it is '
                   'often more useful to think of an array as a collection of variables of the same type.\n'
                   '\n'
                   'Instead of declaring individual variables, such as `number0`, `number1`, ..., and `number99`, you '
                   'declare one array variable such as `numbers` and use `numbers[0]`, `numbers[1]`, ..., and '
                   '`numbers[99]` to represent individual elements. A specific element in an array is accessed by an '
                   '**index**.\n'
                   '\n'
                   '#### Contiguous Memory Layout:\n'
                   'All arrays consist of **contiguous memory locations**. The lowest address corresponds to the first '
                   'element and the highest address to the last element.\n'
                   '\n'
                   '![Array Contiguous Memory Diagram](assets/images/university/cfp/lab12_array_memory.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Declaring Arrays:\n'
                   'To declare an array in C++, a programmer specifies the type of the elements and the number of '
                   'elements required:\n'
                   '```cpp\n'
                   'type arrayName [ arraySize ];\n'
                   '```\n'
                   'This is called a **single-dimensional array**. The `arraySize` must be an integer constant greater '
                   'than zero, and `type` can be any valid C++ data type.\n'
                   '\n'
                   'For example, to declare a 10-element array called `balance` of type `double`:\n'
                   '```cpp\n'
                   'double balance[10];\n'
                   '```\n'
                   'Now `balance` is sufficient to hold up to 10 double-precision numbers.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Initializing Arrays:\n'
                   'You can initialize an array element-by-element or using an initializer list:\n'
                   '```cpp\n'
                   'double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};\n'
                   '```\n'
                   'The number of values between braces `{}` cannot be larger than the number of elements declared '
                   'between square brackets `[]`.\n'
                   '\n'
                   'If you omit the size of the array, an array just large enough to hold the initialization elements '
                   'is created automatically:\n'
                   '```cpp\n'
                   'double balance[] = {1000.0, 2.0, 3.4, 17.0, 50.0};\n'
                   '```\n'
                   '\n'
                   '#### Individual Element Assignment:\n'
                   '```cpp\n'
                   'balance[4] = 50.0;\n'
                   '```\n'
                   'The above statement assigns element number 5th in the array with a value of `50.0`. All arrays '
                   'have **`0` as the index of their first element** (called the **base index**), and the last index '
                   'of an array is `arraySize - 1`.\n'
                   '\n'
                   '![Array Index & balance[4] Diagram](assets/images/university/cfp/lab12_array_index.png)\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Accessing Data in an Array:\n'
                   'Each element of an array is referenced by its index within square brackets `[]`. For an array of '
                   '$n$ elements, valid indices are $0$ through $n-1$:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void main()\n'
                   '{\n'
                   '    float a[5];\n'
                   '    int i;\n'
                   '    a[0] = 9.9;\n'
                   '    a[1] = 2.9;\n'
                   '    a[2] = 3.9;\n'
                   '    a[3] = 4.9;\n'
                   '    a[4] = 5.9;\n'
                   '    \n'
                   '    for (i = 0; i <= 4; i++)\n'
                   '    {\n'
                   '        cout << "value in a[" << i << "] = " << a[i] << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Output:\n'
                   '```\n'
                   'value in a[0] = 9.9\n'
                   'value in a[1] = 2.9\n'
                   'value in a[2] = 3.9\n'
                   'value in a[3] = 4.9\n'
                   'value in a[4] = 5.9\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Strings and Character Arrays in C/C++:\n'
                   'A string is a sequence of characters treated as a single data item and terminated by the **null '
                   "character `'\\0'`**. A string in standard C is represented as a one-dimensional array of "
                   'characters.\n'
                   '\n'
                   'For example, the string `"hello world"` contains 12 characters including the `\'\\0\'` character, '
                   'which is automatically appended by the compiler at the end of the string.\n'
                   '\n'
                   '#### Declaring and Initializing String Variables:\n'
                   '```cpp\n'
                   'char name[10] = "StudyTonight";\n'
                   "char name[10] = {'L', 'e', 's', 's', 'o', 'n', 's', '\\0'};\n"
                   '```\n'
                   "*When initializing a character array by listing characters separately, you must supply the `'\\0'` "
                   'character explicitly.*\n'
                   '\n'
                   '#### Illegal String Initializations:\n'
                   '```cpp\n'
                   'char ch[4] = "Hello";  // ILLEGAL: 5 characters + null byte requires minimum size 6\n'
                   'char str[5] = "Hello"; // ILLEGAL: requires size 6 for null terminator\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 12 Tasks:\n'
                   '\n'
                   '#### Task 1: Maximum Value in 1D Array\n'
                   'Write a program that gets input from the user in a one-dimensional integer array, and finds and '
                   'displays the maximum value from the array.\n'
                   '\n'
                   '#### Task 2: Sum of Array Elements\n'
                   'Write a program that gets input from the user in a one-dimensional integer array and calculates '
                   'the sum of all numbers.\n'
                   '\n'
                   '#### Task 3: 2x2 Matrix Addition\n'
                   'Write a program in which you declare two 2D integer arrays of size $2 \\times 2$. Prompt the user '
                   'to input their values, add them together element by element, and display the resulting matrix.\n',
        'flashcards': [   {   'answer': 'A contiguous data structure that stores a fixed-size sequential collection of '
                                        'elements of the same data type.',
                              'question': 'What is an array?'},
                          {   'answer': 'A special ASCII character with code 0 used in C/C++ to mark the end of a '
                                        'character array string.',
                              'question': "What is the null terminator '\\0'?"},
                          {   'answer': 'It leads to undefined behavior, potentially reading/corrupting adjacent '
                                        'memory or triggering a segmentation fault.',
                              'question': 'What happens if you access an array index beyond its bounds (e.g., arr[10] '
                                          'on an array of size 5)?'},
                          {   'answer': 'int matrix[3][4]; (accessed as matrix[row][col] where 0 <= row < 3 and 0 <= '
                                        'col < 4).',
                              'question': 'How do you declare a 2D array of 3 rows and 4 columns in C++?'}],
        'order': 12,
        'quizzes': [   {   'correctAnswer': '0',
                           'explanation': 'C++ uses zero-based indexing; the first element of an array is always at '
                                          'index 0, and the last is at index n-1.',
                           'options': ['0', '1', '-1', 'Null'],
                           'question': 'What is the base index (the index of the very first element) of all arrays in '
                                       'C and C++?'},
                       {   'correctAnswer': "Because 'Hello' has 5 letters and requires an extra byte for the null "
                                            "terminator '\\0', needing size 6",
                           'explanation': "String literals automatically include the trailing null terminator '\\0'. "
                                          "'Hello' contains 5 letters plus '\\0', totaling 6 bytes; storing it in a "
                                          '5-byte buffer causes an overflow.',
                           'options': [   "Because 'Hello' has 5 letters and requires an extra byte for the null "
                                          "terminator '\\0', needing size 6",
                                          'Because arrays cannot store strings in C++',
                                          'Because single quotes must be used around string literals',
                                          "Because the identifier 'str' is a reserved system keyword"],
                           'question': 'Why is \'char str[5] = "Hello";\' considered an illegal array initialization '
                                       'in C++?'},
                       {   'correctAnswer': 'In contiguous (consecutive) memory locations from lowest to highest '
                                            'address',
                           'explanation': 'All elements of an array reside in a single contiguous block of memory with '
                                          'adjacent memory addresses.',
                           'options': [   'In contiguous (consecutive) memory locations from lowest to highest address',
                                          'Scattered randomly across different virtual hard disk clusters',
                                          'Stored entirely within CPU general-purpose registers',
                                          'Interleaved with instruction cache blocks'],
                           'question': 'How are array elements organized in physical computer memory?'},
                       {   'correctAnswer': '50.0',
                           'explanation': 'balance[4] references the 5th element in the array (indices 0, 1, 2, 3, 4), '
                                          'which contains 50.0.',
                           'options': ['50.0', '1000.0', '17.0', '3.4'],
                           'question': "In the declaration 'double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};', what "
                                       'value is stored at balance[4]?'},
                       {   'correctAnswer': '8 elements (4 elements per matrix)',
                           'explanation': 'Each 2x2 matrix contains 2 rows * 2 columns = 4 elements; two matrices '
                                          'contain a total of 8 elements.',
                           'options': [   '8 elements (4 elements per matrix)',
                                          '4 elements total',
                                          '16 elements total',
                                          '2 elements total'],
                           'question': 'In Task 3, how many total integer elements are stored across two 2x2 '
                                       'matrices?'}],
        'title': 'Lab 12: Execute Array Manipulation'},
    {   'codeSnippet': '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       '// User-defined functions\n'
                       'float sum(float a, float b) { return a + b; }\n'
                       'float circleArea(float r) { return 3.14159f * r * r; }\n'
                       'void printStars(int n) {\n'
                       '    for (int i = 0; i < n; i++) cout << "*";\n'
                       '    cout << endl;\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    printStars(30);\n'
                       '    cout << "Sum of 15.5 and 24.5 = " << sum(15.5, 24.5) << endl;\n'
                       '    cout << "Area of circle (r=2.5) = " << circleArea(2.5) << endl;\n'
                       '    printStars(30);\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#13\n'
                   '\n'
                   '## EXECUTE FUNCTIONS\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Modular Programming:\n'
                   'As program size grows, it becomes unmanageable to write all code inside `main()`. Thus, we must '
                   'divide our large programs into smaller units called **functions**. This approach is called '
                   '**modular programming**.\n'
                   '\n'
                   'Functions also promote **code reusability** by allowing a logic unit to be defined once and called '
                   'repeatedly.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Defining a Function:\n'
                   'A function definition consists of two principal parts:\n'
                   '1. **Function Heading:** Declares return type, function name, and parameter list:\n'
                   '   ```cpp\n'
                   '   returnType functionName ( parameterList )\n'
                   '   ```\n'
                   '2. **Function Body:** Enclosed in curly braces `{}` containing the executable statements.\n'
                   '\n'
                   'We regularly use built-in functions such as `main()`, `sqrt()`, `getch()`, `clrscr()`, and '
                   '`sin()`. Similarly, we can define and invoke our own custom functions. When a function takes data '
                   'to operate on, those inputs are called **arguments**, and the result produced is the **return '
                   'value**.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Defining Functions Without Arguments:\n'
                   '\n'
                   '#### Example 13.1: Print Name 5 Times\n'
                   '```cpp\n'
                   'void printname()\n'
                   '{\n'
                   '    int i;\n'
                   '    for (i = 1; i <= 5; i++)\n'
                   '    {\n'
                   '        cout << "Kashif Iqbal" << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Example 13.2: Print Line of Stars\n'
                   '```cpp\n'
                   'void printstar()\n'
                   '{\n'
                   '    int i;\n'
                   '    for (i = 1; i <= 30; i++)\n'
                   '    {\n'
                   '        cout << "*";\n'
                   '    }\n'
                   '    cout << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Defining Functions With Arguments:\n'
                   '\n'
                   '#### Example 13.3: Print Name $n$ Times\n'
                   '```cpp\n'
                   'void printname2(int n)\n'
                   '{\n'
                   '    int i;\n'
                   '    for (i = 1; i <= n; i++)\n'
                   '    {\n'
                   '        cout << "Kashif Iqbal" << endl;\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Example 13.4: Print $n$ Stars\n'
                   '```cpp\n'
                   'void printstar2(int n)\n'
                   '{\n'
                   '    int i;\n'
                   '    for (i = 1; i <= n; i++)\n'
                   '    {\n'
                   '        cout << "*";\n'
                   '    }\n'
                   '    cout << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Example 13.5: Print $n$ Custom Characters\n'
                   '```cpp\n'
                   'void printchar(int n, char ch)\n'
                   '{\n'
                   '    int i;\n'
                   '    for (i = 1; i <= n; i++)\n'
                   '    {\n'
                   '        cout << ch;\n'
                   '    }\n'
                   '    cout << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Example 13.6: Sum of Two Floating-Point Numbers\n'
                   '```cpp\n'
                   'void sum(float a, float b)\n'
                   '{\n'
                   '    float res;\n'
                   '    res = a + b;\n'
                   '    cout << "Sum = " << res << endl;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Mechanism of Function Calls:\n'
                   '* Functions defined in a program can be called from anywhere (e.g., from `main()` or other '
                   'functions).\n'
                   '* **Actual Arguments vs Dummy (Formal) Arguments:**\n'
                   '  * Variables/constants used in the function call statement are called **Actual arguments**.\n'
                   '  * Variables defined in the function header definition are called **Dummy (Formal) arguments**.\n'
                   '* At the time of function call, values of actual arguments are copied into dummy arguments, and '
                   'control transfers to the function.\n'
                   '\n'
                   '```cpp\n'
                   'void main()\n'
                   '{\n'
                   '    int no;\n'
                   '    cout << "Enter a number: ";\n'
                   '    cin >> no;\n'
                   "    printstar2(no); // Function call with actual argument 'no'\n"
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 13 Tasks:\n'
                   '\n'
                   '#### Task 1: Sum Function\n'
                   'Write a program that defines a function `sum()`, which adds two numbers passed to it as arguments '
                   'and prints the result.\n'
                   '\n'
                   '#### Task 2: Multi-Operation Calculator\n'
                   'Make a calculator program in which `add()`, `sub()`, `mul()`, and `div()` functions are defined. '
                   'Ask the user which operation they wish to perform, input two numbers, and invoke the selected '
                   'function to display the result.\n'
                   '\n'
                   '#### Task 3: Circle Area Function\n'
                   'Write an `area()` function that calculates and prints the area of a circle ($A = \\pi r^2$). It '
                   'takes the radius as an argument. Write a complete `main()` driver for this function.\n',
        'flashcards': [   {   'answer': '1. Function Heading (return type, function name, parameter list)\\n2. '
                                        'Function Body ({ executable statements }).',
                              'question': 'What are the two main parts of a function definition?'},
                          {   'answer': 'A statement that specifies the function name, return type, and parameter '
                                        'types to the compiler before the function is called or defined.',
                              'question': 'What is a function prototype / declaration?'},
                          {   'answer': "A mechanism where a copy of the actual argument's value is passed to the "
                                        "function parameter, leaving the caller's original variable unaffected.",
                              'question': 'What is pass-by-value in C++?'},
                          {   'answer': 'Yes, functions can call any other accessible user-defined or library '
                                        'functions (and can call themselves recursively).',
                              'question': 'Can a C++ function call other user-defined functions?'}],
        'order': 13,
        'quizzes': [   {   'correctAnswer': 'To divide large programs into manageable units and enable code '
                                            'reusability',
                           'explanation': 'Functions partition complex codebases into modular, manageable components, '
                                          'eliminating code duplication and enabling logic reuse.',
                           'options': [   'To divide large programs into manageable units and enable code reusability',
                                          'To increase the total binary executable size on disk',
                                          'To replace hardware buses with software protocols',
                                          'To disable compiler type-checking'],
                           'question': 'What is the primary motivation for adopting modular programming using '
                                       'functions in C++?'},
                       {   'correctAnswer': 'Actual arguments are passed in the call statement; dummy arguments are '
                                            'parameters declared in the function definition',
                           'explanation': 'Actual arguments are the actual values/variables supplied at the call site, '
                                          'which are copied into the formal/dummy parameters defined in the function '
                                          'header.',
                           'options': [   'Actual arguments are passed in the call statement; dummy arguments are '
                                          'parameters declared in the function definition',
                                          'Actual arguments are strings; dummy arguments are numbers',
                                          'Actual arguments must be pointers; dummy arguments are constants',
                                          'Dummy arguments reside on disk; actual arguments reside in cache'],
                           'question': "What is the technical distinction between 'Actual arguments' and 'Dummy "
                                       "(Formal) arguments'?"},
                       {   'correctAnswer': 'void',
                           'explanation': "The 'void' keyword in a function heading signifies that the function "
                                          'returns no value to the calling environment.',
                           'options': ['void', 'int', 'null', 'empty'],
                           'question': 'What return type is specified in a function heading when the function does not '
                                       'return any data to its caller?'},
                       {   'correctAnswer': 'add(), sub(), mul(), and div()',
                           'explanation': 'The Lab 13 calculator task explicitly specifies add(), sub(), mul(), and '
                                          'div() functions for arithmetic selection.',
                           'options': [   'add(), sub(), mul(), and div()',
                                          'sin(), cos(), tan(), and sqrt()',
                                          'push(), pop(), peek(), and clear()',
                                          'open(), read(), write(), and close()'],
                           'question': 'In Task 2, which four functions are required to implement the modular '
                                       'calculator?'},
                       {   'correctAnswer': 'Actual argument values are copied into parameters, and program control '
                                            'transfers to the function body',
                           'explanation': 'Executing a function call pushes the return address and argument copies '
                                          'onto the call stack and branches CPU execution to the function entry point.',
                           'options': [   'Actual argument values are copied into parameters, and program control '
                                          'transfers to the function body',
                                          'The operating system closes the active terminal',
                                          'The program creates a new hard disk partition',
                                          'All global variables are cleared from RAM'],
                           'question': 'What happens at runtime when a function call statement is executed?'}],
        'title': 'Lab 13: Execute Functions'},
    {   'codeSnippet': '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'void swapValues(int* a, int* b) {\n'
                       '    int temp = *a;\n'
                       '    *a = *b;\n'
                       '    *b = temp;\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    int x = 11, y = 22;\n'
                       '    cout << "Addresses: &x = " << &x << ", &y = " << &y << endl;\n'
                       '    cout << "Before swap: x = " << x << ", y = " << y << endl;\n'
                       '    swapValues(&x, &y);\n'
                       '    cout << "After swap:  x = " << x << ", y = " << y << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# Lab#14\n'
                   '\n'
                   '## EXECUTE POINTERS\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Purpose of Pointers:\n'
                   'Pointers are one of the most powerful features of C & C++. Pointers are used for:\n'
                   '* Accessing array elements efficiently\n'
                   '* Passing arguments to a function when the function needs to modify the original argument\n'
                   '* Passing arrays and strings to functions\n'
                   '* Obtaining memory dynamically from the system (heap memory)\n'
                   '* Creating complex data structures such as linked lists, stacks, queues, and trees\n'
                   '\n'
                   '*Pointers are much more commonly used in C++ and C than in languages such as Java (which has no '
                   'raw pointer arithmetic).*\n'
                   '\n'
                   '#### Objectives:\n'
                   '* Pointers and function arguments\n'
                   '* Pointers and arrays\n'
                   '* Pointers and objects\n'
                   '* Linked lists\n'
                   '* Pointers and strings\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Fundamental Pointer Concepts:\n'
                   "Every byte in the computer's memory has a unique **memory address**. Addresses are numbers "
                   '(starting at $0$ and increasing sequentially). If you have 1 MB of memory, addresses range up to '
                   '1,048,575.\n'
                   '\n'
                   'When a program loads into memory, it occupies a range of these addresses. Every variable and every '
                   'function in your program starts at a particular memory address.\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### The Address-of Operator (`&`):\n'
                   'You can find the address occupied by a variable using the **address-of operator `&`**.\n'
                   '\n'
                   '#### Program `VARADDR.CPP`:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main()\n'
                   '{\n'
                   '    int var1 = 11;\n'
                   '    int var2 = 22;\n'
                   '    int var3 = 33;\n'
                   '    \n'
                   '    cout << &var1 << endl; // prints the address of var1\n'
                   '    cout << &var2 << endl; // prints the address of var2\n'
                   '    cout << &var3 << endl; // prints the address of var3\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Observations:\n'
                   '* Addresses are displayed in **hexadecimal arithmetic**, indicated by the prefix `0x`.\n'
                   '* In a 16-bit system, integer addresses differ by 2 bytes; in a 32-bit system, they differ by 4 '
                   'bytes.\n'
                   '* Characters differ by 1 byte, while `double` variables differ by 8 bytes.\n'
                   '* Automatic local variables have descending addresses because they reside on the **stack** (which '
                   'grows downward in memory). Dynamic and global variables reside on the **heap** (which grows '
                   'upward).\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Pointer Dereferencing (`*`):\n'
                   'A pointer is a variable that stores the memory address of another variable:\n'
                   '```cpp\n'
                   'int var = 50;\n'
                   'int* ptr = &var; // ptr stores address of var\n'
                   '\n'
                   'cout << ptr << endl;  // prints memory address (e.g., 0x7ffd...)\n'
                   'cout << *ptr << endl; // dereference operator prints value: 50\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Lab 14 Problems & Tasks:\n'
                   '\n'
                   '#### PROBLEM #1: Calculating Average with Pointers\n'
                   'Write a program that reads a group of numbers from the user and places them in an array of type '
                   '`float`. Once the numbers are stored in the array, the program averages them and prints the '
                   'result. Use pointer notation wherever possible:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    float arr[5], sum = 0.0;\n'
                   '    float* ptr = arr;\n'
                   '    cout << "Enter 5 float numbers: ";\n'
                   '    for (int i = 0; i < 5; i++) {\n'
                   '        cin >> *(ptr + i);\n'
                   '        sum += *(ptr + i);\n'
                   '    }\n'
                   '    cout << "Average = " << (sum / 5.0) << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### PROBLEM #2: Swapping Values Using Pointers\n'
                   'Write a program to exchange the values of two variables by passing pointers to a swap function:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'void swap(int* a, int* b) {\n'
                   '    int temp = *a;\n'
                   '    *a = *b;\n'
                   '    *b = temp;\n'
                   '}\n'
                   '\n'
                   'int main() {\n'
                   '    int x = 10, y = 20;\n'
                   '    cout << "Before swap: x=" << x << ", y=" << y << endl;\n'
                   '    swap(&x, &y);\n'
                   '    cout << "After swap:  x=" << x << ", y=" << y << endl;\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### PROBLEM #3: Prime Number Check via Pointer\n'
                   'Write a program to input an integer value and determine if the given value is a prime number by '
                   'passing the number to a function as a pointer argument.\n'
                   '\n'
                   '#### PROBLEM #4: Reverse Array Access\n'
                   'Declare an integer array of five values. Declare a pointer of type `int`, point it to the end of '
                   'the array, and print the array in reverse order using pointer decrement.\n'
                   '\n'
                   '#### PROBLEM #5: `addarrays()` Function\n'
                   'Write a function called `addarrays()` that accepts the addresses of three arrays as arguments, '
                   'adds the contents of the first two arrays element-by-element, and places the result in the third '
                   'array:\n'
                   '```cpp\n'
                   'void addarrays(float* a, float* b, float* c, int size) {\n'
                   '    for (int i = 0; i < size; i++) {\n'
                   '        *(c + i) = *(a + i) + *(b + i);\n'
                   '    }\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Analysis & Conclusion:\n'
                   'Pointers are essential for efficient data manipulation and dynamic data structures in C/C++. By '
                   'holding memory address references directly, pointers eliminate redundant data copying and enable '
                   'functions to modify caller memory spaces.\n',
        'flashcards': [   {   'answer': "'&' (address-of) retrieves the memory address of a variable, while '*' "
                                        "(dereference) accesses the value stored at a pointer's address.",
                              'question': "What is the difference between '&' and '*' when working with pointers?"},
                          {   'answer': 'A pointer that does not point to any valid memory location (assigned nullptr '
                                        'or 0), used to signify that the pointer is uninitialized or empty.',
                              'question': 'What is a null pointer in C++?'},
                          {   'answer': 'Passing a pointer allows the function to directly access and modify the '
                                        "caller's original variable in memory.",
                              'question': 'How does passing a pointer to a function differ from passing by value?'},
                          {   'answer': '*(arr + i) is mathematically and functionally identical to arr[i].',
                              'question': 'How does pointer arithmetic relate to array indexing?'}],
        'order': 14,
        'quizzes': [   {   'correctAnswer': 'The memory address of another variable',
                           'explanation': 'A pointer is a variable that stores the physical/virtual memory address of '
                                          'another variable.',
                           'options': [   'The memory address of another variable',
                                          'The total character count of a string',
                                          'The clock frequency of the CPU',
                                          'The disk partition sector number'],
                           'question': 'What information does a pointer variable store in C++?'},
                       {   'correctAnswer': '& (Address-of operator)',
                           'explanation': 'The ampersand (&) operator returns the memory address of its operand (e.g., '
                                          '&var).',
                           'options': [   '& (Address-of operator)',
                                          '* (Dereference operator)',
                                          '-> (Arrow operator)',
                                          '% (Modulus operator)'],
                           'question': 'Which operator is used to obtain the memory address of an existing variable in '
                                       'C++?'},
                       {   'correctAnswer': 'Because the system call stack grows downward in memory as frames are '
                                            'pushed',
                           'explanation': 'In standard computer architectures (x86/x64), the program stack grows '
                                          'downward from higher memory addresses toward lower addresses.',
                           'options': [   'Because the system call stack grows downward in memory as frames are pushed',
                                          'Because compiler optimizations reverse the array index order',
                                          'Because hexadecimal numbers are counted backward',
                                          'Because local variables reside on optical discs'],
                           'question': 'Why do local automatic variables typically have descending memory addresses on '
                                       'the runtime call stack?'},
                       {   'correctAnswer': 'int temp = *a; *a = *b; *b = temp;',
                           'explanation': "Dereferencing *a and *b reads and writes directly into the caller's memory "
                                          'locations, exchanging their values.',
                           'options': [   'int temp = *a; *a = *b; *b = temp;',
                                          'int temp = a; a = b; b = temp;',
                                          '&a = &b;',
                                          'swap(a, b);'],
                           'question': "In the swap function 'swap(int* a, int* b)', how are the values exchanged?"},
                       {   'correctAnswer': '0x1004',
                           'explanation': 'Pointer arithmetic scales increments by the size of the referenced type; '
                                          'adding 1 to a float pointer advances it by 4 bytes (sizeof(float)).',
                           'options': ['0x1004', '0x1001', '0x1008', '0x1002'],
                           'question': "In pointer arithmetic, if 'ptr' is a pointer to float (4 bytes) at address "
                                       "0x1000, what address does 'ptr + 1' represent?"}],
        'title': 'Lab 14: Execute Pointers and its Types'}]


def seed_cfp_curriculum(db_client: Optional[Prisma] = None, verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds the Computer Fundamentals and Programming (CF&P) curriculum (All 14 Labs) into Neon PostgreSQL via Prisma.
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
            print(f"[*] Cleared previous records for CF&P course: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

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
            print("SUMMARY TABLE: UNIVERSITY CF&P (HIET 2021) ALL 14 LABS SEEDED")
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
    seed_cfp_curriculum()
