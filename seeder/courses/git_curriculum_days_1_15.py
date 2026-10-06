"""
Git & Version Control System Curriculum - Days 1 to 15
Module 1: Version Control Foundation & Git Basics (Days 1-10)
Module 2: Branching & Merging (Days 11-15 of 11-17)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_15 = [
    # ----------------------------------------------------
    # Day 1: Intro to Version Control (Local, Centralized, Distributed)
    # ----------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Intro to Version Control (Local, Centralized, Distributed)",
        concept="Understanding the evolution of tracking project changes from manual folder backups to Distributed Version Control Systems (DVCS).",
        analogy="Think of version control like video game save checkpoints. Instead of naming your files 'project_final', 'project_final_v2', 'project_really_final_FINAL', version control gives you an automatic magical rewind button and timeline for every single change ever made.",
        theory_sections=[
            {
                "heading": "The Evolution of Version Control Systems",
                "body": (
                    "Before version control, developers copied directory folders with timestamps (e.g. `website_backup_2023_10_01`). "
                    "This approach is error-prone, consumes unnecessary disk space, and makes multi-person collaboration almost impossible. "
                    "Version Control Systems (VCS) solve this by recording modifications to a set of files over time so specific versions can be recalled later."
                )
            },
            {
                "heading": "VCS Generations: Local, Centralized, Distributed",
                "body": (
                    "1. **Local VCS**: Simple database keeping patch sets on the local disk (e.g., RCS). Single point of failure; no collaboration.\n"
                    "2. **Centralized VCS (CVCS)**: A single central server houses all file versions, and clients check out files from that central hub (e.g., Subversion/SVN, Perforce). If the server goes down, nobody can save commits or collaborate.\n"
                    "3. **Distributed VCS (DVCS)**: Every developer clones the complete repository—including its entire history—locally (e.g., Git, Mercurial). If any server crashes, any peer's local clone can restore the full historical archive."
                )
            },
            {
                "heading": "Why Distributed Architecture Dominates",
                "body": (
                    "In a DVCS like Git, operations like branching, committing, inspecting historical diffs, and viewing logs are 100% offline and instantaneous. "
                    "Network communication is only required when syncing (pushing or pulling) changes with teammates."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Historical Folder Copying Anti-Pattern",
                "code": "# The messy manual way developers used to track versions:\ncp -r /app /app_backup_v1\ncp -r /app /app_backup_final\ncp -r /app /app_backup_final_fixed_boss_said_urgent",
                "explanation": "Manual copies waste gigabytes of disk space and offer no context on who changed what or why."
            },
            {
                "title": "Verifying Git Installation & Version",
                "code": "# Check if Git is installed on your operating system:\ngit --version\n\n# Output:\n# git version 2.43.0",
                "explanation": "Confirms the Git binary is installed and registered in your system PATH."
            },
            {
                "title": "Viewing Built-In Git Help Documentation",
                "code": "# Open the manual page for any git command:\ngit help\ngit help clone\n\n# Quick synopsis directly in the shell:\ngit commit -h",
                "explanation": "Git provides offline manual pages for every command and flag."
            },
            {
                "title": "Centralized vs Distributed Network Topology",
                "code": "# Centralized (SVN):\n# Developer A <---> [Central Server] <---> Developer B\n\n# Distributed (Git):\n# [Local Repo A] <============ sync ============> [Local Repo B]\n#        \\                                              /\n#         +---> [Remote Hub (GitHub/GitLab)] <---------+",
                "explanation": "Git treats every copy of the repository as an authoritative, standalone clone."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Git Environment",
            description="Run the command to verify your installed Git version and access the help summary.",
            starter_code="# Step 1: Check git version\n# Step 2: Show help overview\n",
            solution_code="git --version\ngit help",
            expected_output="git version 2.x\nusage: git [-v | --version] [-h | --help]..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What distinguishes a Distributed Version Control System (DVCS) like Git from a Centralized VCS (CVCS) like SVN?",
                options=[
                    "Every client maintains a full local clone of the entire repository history, enabling offline work",
                    "A DVCS requires a continuous 24/7 internet connection to save commits",
                    "A DVCS only allows one person to edit files at a time",
                    "A DVCS stores all repository history exclusively in RAM"
                ],
                correct_answer="Every client maintains a full local clone of the entire repository history, enabling offline work",
                explanation="In DVCS, each local clone contains the entire commit graph and history, allowing full offline operation."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is an example of a Centralized Version Control System?",
                options=["Apache Subversion (SVN)", "Git", "Mercurial", "Bazaar"],
                correct_answer="Apache Subversion (SVN)",
                explanation="SVN is a classic Centralized VCS where a single server manages all revision history."
            ),
            QuizQuestionBlueprint(
                question="What happens in a Centralized VCS if the central server suffers catastrophic hardware failure without backups?",
                options=[
                    "Entire historical project revision history is permanently lost",
                    "Clients can automatically rebuild history because they have full clones",
                    "The client files are automatically encrypted",
                    "Centralized VCS never stores data on servers"
                ],
                correct_answer="Entire historical project revision history is permanently lost",
                explanation="In CVCS, clients only have current snapshots, not full project history, creating a single point of failure."
            ),
            QuizQuestionBlueprint(
                question="Which command prints the version of Git currently installed on your operating system?",
                options=["git --version", "git check -v", "git status -v", "git which"],
                correct_answer="git --version",
                explanation="`git --version` queries and prints the current Git runtime version."
            ),
            QuizQuestionBlueprint(
                question="Why are operations like branching, committing, and viewing history instantaneous in Git?",
                options=[
                    "They operate on local files and local databases without contacting a remote network server",
                    "Git skips data verification to be faster",
                    "Git compresses files into zip archives before reading them",
                    "Git runs all operations in kernel mode"
                ],
                correct_answer="They operate on local files and local databases without contacting a remote network server",
                explanation="Because everything is stored locally inside the `.git` directory, network latency is completely eliminated."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 2: What is Git? (Git vs GitHub/GitLab)
    # ----------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: What is Git? (Git vs GitHub/GitLab)",
        concept="Demystifying the critical distinction between Git (the command-line tool) and cloud hosting platforms like GitHub, GitLab, and Bitbucket.",
        analogy="Git is like the engine inside your car (it does the mechanical driving and tracks the journey). GitHub is like a giant social parking garage where you park your car so your friends can inspect it, wash it, and ride together.",
        theory_sections=[
            {
                "heading": "Git: The Engine",
                "body": (
                    "Git is an open-source command-line tool created in 2005 by Linus Torvalds (the creator of the Linux kernel) "
                    "to manage Linux kernel development. It runs entirely on your local machine, tracking file changes, snapshots, and branches."
                )
            },
            {
                "heading": "GitHub, GitLab, and Bitbucket: The Cloud Platforms",
                "body": (
                    "GitHub, GitLab, and Bitbucket are cloud-hosted web services that store Git repositories on the internet. "
                    "They layer collaboration features on top of Git: Issue Trackers, Pull/Merge Requests, Code Reviews, Discussion Boards, and CI/CD automation pipelines."
                )
            },
            {
                "heading": "Git Works 100% Without GitHub",
                "body": (
                    "You do not need an internet connection, a GitHub account, or third-party servers to use Git. "
                    "You can initialize a repository, branch, commit, merge, and diff entirely on an isolated laptop in airplane mode."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Git Without Any Cloud Service",
                "code": "# You can use Git purely locally:\nmkdir secret_project\ncd secret_project\ngit init\necho 'offline code' > app.py\ngit add app.py\ngit commit -m 'Initial local commit'",
                "explanation": "No internet, GitHub account, or remote server required."
            },
            {
                "title": "Associating Local Git with GitHub Remote",
                "code": "# Once you want cloud sharing and collaboration:\ngit remote add origin https://github.com/username/secret_project.git\ngit branch -M main\ngit push -u origin main",
                "explanation": "Connects your local offline repository to a GitHub remote server."
            },
            {
                "title": "Feature Comparison: Git vs GitHub",
                "code": "# Git Features:           # GitHub Features:\n# - File hashing (SHA-1)   # - Web UI Repository Browser\n# - Commits & Branches     # - Pull Requests & Code Review\n# - Fast merges & rebases  # - Issue Trackers & Project Boards\n# - Offline versioning     # - GitHub Actions (CI/CD)",
                "explanation": "Distinguishes core version control capabilities from cloud collaborative SaaS features."
            },
            {
                "title": "Checking Git Core Metadata Locally",
                "code": "# Inspect the hidden directory where local Git saves everything:\nls -la .git\n\n# Output includes: HEAD, config, description, hooks, info, objects, refs",
                "explanation": "Everything Git knows is stored locally in the `.git` directory."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create an Offline Git Repository",
            description="Create a directory named 'offline_app', initialize Git inside it, create a file named 'main.py' with text 'print(\"Hello\")', stage it, and commit it with message 'feat: init app'.",
            starter_code="# Type commands to create dir, init git, write file, stage, and commit\n",
            solution_code="mkdir offline_app\ncd offline_app\ngit init\necho 'print(\"Hello\")' > main.py\ngit add main.py\ngit commit -m 'feat: init app'",
            expected_output="Initialized empty Git repository...\n[main (root-commit) ...] feat: init app\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which statement correctly identifies the relationship between Git and GitHub?",
                options=[
                    "Git is the local version control software; GitHub is a cloud-based hosting service for Git repositories",
                    "Git is a website and GitHub is the command-line tool",
                    "Git cannot be used without paying for a GitHub subscription",
                    "GitHub is an operating system and Git is a text editor"
                ],
                correct_answer="Git is the local version control software; GitHub is a cloud-based hosting service for Git repositories",
                explanation="Git is the standalone DVCS engine; GitHub is a collaborative web platform built on top of Git."
            ),
            QuizQuestionBlueprint(
                question="Who originally designed and created Git in 2005?",
                options=["Linus Torvalds", "Guido van Rossum", "James Gosling", "Tim Berners-Lee"],
                correct_answer="Linus Torvalds",
                explanation="Linus Torvalds created Git to manage development of the Linux operating system kernel."
            ),
            QuizQuestionBlueprint(
                question="Can you create branches and commit changes using Git without an internet connection?",
                options=[
                    "Yes, all Git version control operations run 100% locally on your machine",
                    "No, Git must verify every commit with GitHub's servers",
                    "Only if you pay for Git Enterprise",
                    "No, Git requires DNS resolution for every commit"
                ],
                correct_answer="Yes, all Git version control operations run 100% locally on your machine",
                explanation="Git is distributed and autonomous; local commits and branches do not interact with any network."
            ),
            QuizQuestionBlueprint(
                question="Which of the following features is specific to cloud platforms like GitHub or GitLab rather than core Git CLI?",
                options=["Pull Requests / Code Review UI", "git commit", "git checkout", "git init"],
                correct_answer="Pull Requests / Code Review UI",
                explanation="Pull Requests are collaboration workflows created by platforms like GitHub, not native git commands."
            ),
            QuizQuestionBlueprint(
                question="Where does Git store all internal database objects and history for a project?",
                options=[
                    "In the hidden `.git/` folder inside the project root",
                    "In the Windows Registry / macOS Keychain",
                    "On an encrypted server in Sweden",
                    "Inside your computer's BIOS"
                ],
                correct_answer="In the hidden `.git/` folder inside the project root",
                explanation="The `.git` folder contains the object database, index, configuration, and refs."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 3: Installation & Setup (SSH keys & HTTPS)
    # ----------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Installation & Setup (SSH keys & HTTPS)",
        concept="Configuring secure communication between your local Git environment and remote servers via HTTPS Personal Access Tokens (PAT) and Ed25519 SSH keypairs.",
        analogy="HTTPS with a token is like showing your ID badge at the front door every day. An SSH keypair is like a custom biometric key: you put your public key lock on GitHub's door, and your private key on your computer unlocks it silently every time.",
        theory_sections=[
            {
                "heading": "Remote Authentication Protocols: HTTPS vs SSH",
                "body": (
                    "When pushing and pulling code to remote providers, Git supports two primary communication protocols: "
                    "1. **HTTPS**: Uses SSL/TLS encryption. Passwords are no longer accepted by GitHub/GitLab; developers must use a Personal Access Token (PAT) with granular scopes.\n"
                    "2. **SSH (Secure Shell)**: Uses asymmetric public-key cryptography. You generate a keypair locally, upload the public key to your cloud account, and authenticate automatically without passwords."
                )
            },
            {
                "heading": "Modern SSH Key Generation (Ed25519)",
                "body": (
                    "While RSA (2048/4096-bit) has been standard for decades, modern cryptography recommends `Ed25519` "
                    "(Edwards-curve Digital Signature Algorithm). It is mathematically superior, faster, and generates shorter, more secure keys."
                )
            },
            {
                "heading": "The SSH Agent",
                "body": (
                    "The `ssh-agent` is a background daemon that holds your decrypted private keys in memory so you don't need to re-enter your passphrase for every `git push` or `git pull`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Generating an Ed25519 SSH Keypair",
                "code": "# Generate a modern SSH key with your email as a label:\nssh-keygen -t ed25519 -C \"developer@example.com\"\n\n# Follow prompts: press Enter to accept default location ~/.ssh/id_ed25519\n# Enter a secure passphrase",
                "explanation": "Generates private key `id_ed25519` (keep secret!) and public key `id_ed25519.pub`."
            },
            {
                "title": "Starting SSH Agent and Adding Key",
                "code": "# Start the ssh-agent background process:\neval \"$(ssh-agent -s)\"\n\n# Add your private key to the agent:\nssh-add ~/.ssh/id_ed25519",
                "explanation": "Loads the key into active session memory."
            },
            {
                "title": "Viewing Public Key to Copy to GitHub",
                "code": "# Print public key to copy into GitHub Settings -> SSH and GPG keys:\ncat ~/.ssh/id_ed25519.pub\n\n# Output starts with: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5...",
                "explanation": "Never share your private key; only share the `.pub` file."
            },
            {
                "title": "Testing SSH Connection with GitHub",
                "code": "# Test authentication with GitHub's servers:\nssh -T git@github.com\n\n# Expected success message:\n# Hi username! You've successfully authenticated, but GitHub does not provide shell access.",
                "explanation": "Verifies that your SSH key is authorized and functional."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Generate SSH Key and Test Connectivity",
            description="Write the sequence of shell commands to generate an ed25519 key for 'user@dev.io' (batch non-interactive using -N '' and -f ~/.ssh/test_key) and test SSH connectivity to GitHub.",
            starter_code="# Step 1: Generate non-interactive ed25519 key\n# Step 2: Test SSH connection to git@github.com\n",
            solution_code="ssh-keygen -t ed25519 -C \"user@dev.io\" -N \"\" -f ~/.ssh/test_key\nssh -T git@github.com",
            expected_output="Your identification has been saved in ~/.ssh/test_key\nHi ... You've successfully authenticated..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why does GitHub reject standard account passwords for HTTPS git push operations?",
                options=[
                    "Passwords are deprecated in favor of Personal Access Tokens (PATs) and SSH keys for enhanced security",
                    "GitHub no longer supports HTTPS at all",
                    "Passwords take up too much bandwidth on servers",
                    "Passwords only work on Linux operating systems"
                ],
                correct_answer="Passwords are deprecated in favor of Personal Access Tokens (PATs) and SSH keys for enhanced security",
                explanation="GitHub phased out basic password authentication in 2021 in favor of tokens and asymmetric SSH keys."
            ),
            QuizQuestionBlueprint(
                question="Which file from an SSH keypair should NEVER be shared or uploaded to the internet?",
                options=[
                    "The private key (`~/.ssh/id_ed25519`)",
                    "The public key (`~/.ssh/id_ed25519.pub`)",
                    "The `known_hosts` file",
                    "The `config` file"
                ],
                correct_answer="The private key (`~/.ssh/id_ed25519`)",
                explanation="The private key must remain strictly confidential on your local machine."
            ),
            QuizQuestionBlueprint(
                question="Which modern cryptographic algorithm is recommended for generating secure and compact SSH keys in Git?",
                options=["Ed25519", "MD5", "DES", "Rot13"],
                correct_answer="Ed25519",
                explanation="Ed25519 is widely recognized as the modern, high-speed, secure standard for SSH key generation."
            ),
            QuizQuestionBlueprint(
                question="Which command tests whether your SSH key is successfully recognized by GitHub?",
                options=["ssh -T git@github.com", "git ping github", "ssh check github.com", "git test --ssh"],
                correct_answer="ssh -T git@github.com",
                explanation="`ssh -T git@github.com` attempts an SSH handshake and returns your username upon verification."
            ),
            QuizQuestionBlueprint(
                question="What is the role of the `ssh-agent`?",
                options=[
                    "A background program that caches your decrypted SSH private keys so you don't enter your passphrase repeatedly",
                    "A tool that uploads code directly to cloud hosts",
                    "A compiler that translates C++ into Git bytecode",
                    "A firewall that blocks unauthorized git commands"
                ],
                correct_answer="A background program that caches your decrypted SSH private keys so you don't enter your passphrase repeatedly",
                explanation="`ssh-agent` securely stores private keys in memory for the active terminal session."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 4: Global & Local Config (git config, user.name, user.email)
    # ----------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Global & Local Config (`git config`, user.name, user.email)",
        concept="Mastering Git's three-tier configuration hierarchy (System, Global, Local) to correctly attribute author identity and customize editor behaviors.",
        analogy="Think of Git configuration like company rules: System-level is the law of the country, Global-level is company-wide policy for your whole laptop, and Local-level is the specific dress code for a single project meeting room.",
        theory_sections=[
            {
                "heading": "Git Configuration Levels",
                "body": (
                    "Git stores settings across three distinct scopes:\n"
                    "1. **System (`--system`)**: Applies to every user on the entire operating system (`/etc/gitconfig`).\n"
                    "2. **Global (`--global`)**: Applies to all repositories under the logged-in OS user account (`~/.gitconfig`).\n"
                    "3. **Local (`--local`)**: Applies strictly to the active repository (`.git/config`). Overrides global settings."
                )
            },
            {
                "heading": "Author Identity Attribution",
                "body": (
                    "Every commit in Git permanently bakes in two metadata fields: `user.name` and `user.email`. "
                    "If you contribute to open source and work for a corporate employer, you can configure your work email locally in work repos while keeping your personal email global."
                )
            },
            {
                "heading": "Essential Configuration Parameters",
                "body": (
                    "Key settings include `core.editor` (e.g., VS Code or Vim), `init.defaultBranch` (set to `main`), and `core.autocrlf` "
                    "(handles Windows `CRLF` vs Linux/macOS `LF` line endings)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Global Identity",
                "code": "# Set default identity for all your repositories:\ngit config --global user.name \"Alice Dev\"\ngit config --global user.email \"alice@example.com\"",
                "explanation": "Writes settings to ~/.gitconfig."
            },
            {
                "title": "Configuring Local Override for Work Repo",
                "code": "# Inside corporate work repo, override with company email:\ncd ~/work/enterprise-app\ngit config --local user.email \"alice@enterprise.corp\"",
                "explanation": "Local settings override global settings for this specific repository."
            },
            {
                "title": "Setting Default Branch and Editor",
                "code": "# Set default branch name for all new repos to 'main':\ngit config --global init.defaultBranch main\n\n# Set VS Code as the default commit editor:\ngit config --global core.editor \"code --wait\"",
                "explanation": "Ensures modern branch naming and convenient graphical commit editing."
            },
            {
                "title": "Listing and Inspecting Config Origins",
                "code": "# List all active configuration items along with where they originate:\ngit config --list --show-origin",
                "explanation": "Prints each configuration key alongside the exact file where it is defined."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Git Identity and Default Branch",
            description="Configure the global user name to 'Dev Engineer', global email to 'dev@platform.io', and set the global default initial branch to 'main'.",
            starter_code="# Configure user.name, user.email, and init.defaultBranch globally\n",
            solution_code="git config --global user.name \"Dev Engineer\"\ngit config --global user.email \"dev@platform.io\"\ngit config --global init.defaultBranch main",
            expected_output="Config values stored in ~/.gitconfig"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if a Git parameter is defined in both `--global` and `--local` configurations?",
                options=[
                    "The `--local` configuration takes precedence and overrides the `--global` value",
                    "Git throws a syntax error and halts",
                    "The `--global` configuration always wins",
                    "Git averages the two values together"
                ],
                correct_answer="The `--local` configuration takes precedence and overrides the `--global` value",
                explanation="Local repo settings always override broader global and system settings."
            ),
            QuizQuestionBlueprint(
                question="Where does Git store the `--global` configuration file on Linux/macOS?",
                options=["~/.gitconfig", "/etc/gitconfig", ".git/config", "/var/log/git"],
                correct_answer="~/.gitconfig",
                explanation="Global user settings are stored in the user's home directory inside `.gitconfig`."
            ),
            QuizQuestionBlueprint(
                question="Which flag passed to `git config --list` displays the file path where each setting is located?",
                options=["--show-origin", "--verbose", "--paths", "--debug"],
                correct_answer="--show-origin",
                explanation="`git config --list --show-origin` annotates each configuration key with its file origin."
            ),
            QuizQuestionBlueprint(
                question="Why is setting `user.email` critical in Git?",
                options=[
                    "Every commit records the author's email permanently in the commit history",
                    "Git will refuse to run without an active email address verifying your credit card",
                    "It is used to send spam alerts to your team members",
                    "It determines how fast your code compiles"
                ],
                correct_answer="Every commit records the author's email permanently in the commit history",
                explanation="Git bakes author identity and email immutably into each commit object."
            ),
            QuizQuestionBlueprint(
                question="Which command sets the default branch name for all future `git init` calls to 'main'?",
                options=[
                    "git config --global init.defaultBranch main",
                    "git default branch main",
                    "git branch --set-default main",
                    "git init --global=main"
                ],
                correct_answer="git config --global init.defaultBranch main",
                explanation="`init.defaultBranch` configures the initial branch created by `git init`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 5: Initializing a Repository (git init)
    # ----------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Initializing a Repository (`git init`)",
        concept="Understanding how `git init` turns any standard folder into a tracked repository by instantiating the internal `.git` filesystem database.",
        analogy="`git init` is like giving an ordinary blank notebook a sentient magical memory ribbon. From that moment on, every time you add a page or scratch out a paragraph, the notebook recognizes that it is under surveillance.",
        theory_sections=[
            {
                "heading": "What Does `git init` Actually Do?",
                "body": (
                    "When you run `git init` inside an existing or new folder, Git creates a hidden directory named `.git`. "
                    "This hidden directory contains the entire nervous system of your repository: the object database, pointers (HEAD, refs), hooks, and configuration."
                )
            },
            {
                "heading": "Anatomy of the `.git` Directory",
                "body": (
                    "- `HEAD`: A text file pointing to the currently checked-out branch reference.\n"
                    "- `config`: Repository-specific local configuration values.\n"
                    "- `objects/`: The content-addressable storage where blobs, trees, commits, and annotated tags are stored.\n"
                    "- `refs/`: Stores pointers to commit objects (e.g., `refs/heads/main` or `refs/tags/v1.0`).\n"
                    "- `hooks/`: Example client-side lifecycle scripts."
                )
            },
            {
                "heading": "Bare Repositories (`git init --bare`)",
                "body": (
                    "A standard `git init` has a **working directory** where you write and compile code. "
                    "A bare repository (`git init --bare`) contains **only** the versioning data without any working directory files. "
                    "Bare repositories are used strictly as central remote servers (like GitHub or internal file servers) where developers push code."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Initializing a New Repository",
                "code": "# Create project directory and initialize Git:\nmkdir my-web-app\ncd my-web-app\ngit init\n\n# Output:\n# Initialized empty Git repository in /Users/dev/my-web-app/.git/",
                "explanation": "Instantiates the hidden .git directory."
            },
            {
                "title": "Exploring the Internal .git Directory",
                "code": "# Inspect the internal directory tree created by git init:\ntree -a .git\n# Or on Windows:\n# Get-ChildItem .git -Force\n\n# Contains: HEAD, branches, config, description, hooks, info, objects, refs",
                "explanation": "Shows the default files initialized in the database skeleton."
            },
            {
                "title": "Checking the Initial HEAD Reference",
                "code": "# Read the contents of the HEAD pointer file:\ncat .git/HEAD\n\n# Output:\n# ref: refs/heads/main",
                "explanation": "HEAD points to the symbolic reference where your first commit will land."
            },
            {
                "title": "Creating a Bare Server Repository",
                "code": "# Create a bare repository intended as a remote push target:\nmkdir server-repo.git\ncd server-repo.git\ngit init --bare\n\n# Notice no working files exist—only internal database files",
                "explanation": "Bare repositories are the foundation of remote hubs like GitHub and GitLab."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Initialize Repository and Verify HEAD Pointer",
            description="Initialize a new Git repository in a folder named 'core_service' and display the content of its `.git/HEAD` file.",
            starter_code="# Create folder, enter it, init git, and print .git/HEAD content\n",
            solution_code="mkdir core_service\ncd core_service\ngit init\ncat .git/HEAD",
            expected_output="Initialized empty Git repository...\nref: refs/heads/main"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What critical folder is generated when you run `git init` in a folder?",
                options=[
                    "A hidden `.git/` directory containing the database and tracking files",
                    "A `src/` directory with starter code",
                    "A `.github/` folder with CI/CD scripts",
                    "A `node_modules/` folder"
                ],
                correct_answer="A hidden `.git/` directory containing the database and tracking files",
                explanation="`git init` creates the `.git` folder containing all version control metadata."
            ),
            QuizQuestionBlueprint(
                question="What is a 'bare' Git repository created via `git init --bare`?",
                options=[
                    "A repository without a working directory, used strictly as a remote server target for pushing/pulling",
                    "A repository that has had all of its files and history deleted",
                    "A trial version of Git with limited features",
                    "A repository that runs without security encryption"
                ],
                correct_answer="A repository without a working directory, used strictly as a remote server target for pushing/pulling",
                explanation="Bare repos store only the Git database without checked-out working files."
            ),
            QuizQuestionBlueprint(
                question="What does the `.git/HEAD` file contain in a freshly initialized repository?",
                options=[
                    "A reference pointing to the current branch name (e.g. `ref: refs/heads/main`)",
                    "The password of the current user",
                    "The compiled binary of Git",
                    "A list of all computer hardware specs"
                ],
                correct_answer="A reference pointing to the current branch name (e.g. `ref: refs/heads/main`)",
                explanation="`HEAD` is a pointer referencing whichever branch or commit is currently active."
            ),
            QuizQuestionBlueprint(
                question="If you delete the `.git/` folder from your project directory, what happens?",
                options=[
                    "Your working code files remain, but all Git commit history and branch data are permanently erased",
                    "Your computer operating system crashes",
                    "All your source code files are deleted automatically",
                    "Git restores the folder from the cloud automatically"
                ],
                correct_answer="Your working code files remain, but all Git commit history and branch data are permanently erased",
                explanation="Deleting `.git` removes version control tracking, leaving only current unversioned files."
            ),
            QuizQuestionBlueprint(
                question="Can you run `git init` inside a folder that already contains existing files?",
                options=[
                    "Yes, Git will initialize tracking without altering or deleting your existing files",
                    "No, Git requires an entirely empty folder",
                    "Yes, but Git will automatically delete all existing files",
                    "Only if all files are written in C"
                ],
                correct_answer="Yes, Git will initialize tracking without altering or deleting your existing files",
                explanation="`git init` safely converts existing folders into repositories without disturbing existing files."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 6: Git Architecture (Working Dir, Staging/Index, Local Repo)
    # ----------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Git Architecture (Working Dir, Staging/Index, Local Repo)",
        concept="Mastering Git's Three Trees Architecture: the Working Directory, the Staging Area (Index), and the Commit History (Repository).",
        analogy="Think of cooking at a restaurant: The Working Directory is your messy cutting board where you slice onions and experiment. The Staging Area is your neat serving tray where you assemble only the dishes ready to serve. The Repository is the dining table where the waiter delivers the finished meal forever.",
        theory_sections=[
            {
                "heading": "The Three Areas of Git",
                "body": (
                    "Unlike simpler version control tools that save changes directly from disk to history, Git introduces an intermediate stage called the **Index** or **Staging Area**.\n"
                    "1. **Working Directory**: The actual files on your filesystem that you edit with your IDE or editor.\n"
                    "2. **Staging Area (Index)**: A binary cache file (`.git/index`) that prepares the exact snapshot intended for the next commit.\n"
                    "3. **Git Directory / Repository**: The permanent database of immutable commit objects."
                )
            },
            {
                "heading": "Why Does the Staging Area Exist?",
                "body": (
                    "The staging area gives developers granular control. If you modified 5 files while fixing a bug and also accidentally refactored a function, "
                    "you can stage only the bugfix files into one clean commit, and stage the refactoring into a separate commit."
                )
            },
            {
                "heading": "File Lifecycle States",
                "body": (
                    "Files transition through four states:\n"
                    "- **Untracked**: New files that Git has never seen.\n"
                    "- **Tracked / Unmodified**: Files matching the last commit.\n"
                    "- **Modified**: Tracked files changed in your working directory.\n"
                    "- **Staged**: Changes marked to go into the next commit snapshot."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Visualizing the Three Trees",
                "code": "# Working Directory        Staging Area (Index)         Repository (Commit History)\n#   [ index.html ]   -->       git add      -->   [ Commit: SHA-a1b2c3 ]\n# (Uncommitted files)      (Prepared snapshot)       (Permanent immutable record)",
                "explanation": "Illustrates how files flow across the three architectural stages."
            },
            {
                "title": "Tracking File State Transitions",
                "code": "# 1. Create untracked file:\necho \"<h1>Hello</h1>\" > index.html\n\n# 2. Move file from Working Dir into Staging Area:\ngit add index.html\n\n# 3. Move from Staging Area into Local Repository:\ngit commit -m \"feat: create homepage\"",
                "explanation": "Standard 3-step transition from disk to permanent history."
            },
            {
                "title": "Inspecting the Staging Area Index",
                "code": "# List files currently staged in the binary index:\ngit ls-files --stage\n\n# Output shows file mode, SHA-1 blob hash, stage number, and filename:\n# 100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0   index.html",
                "explanation": "Reveals the internal SHA-1 blob hash stored in the staging index."
            },
            {
                "title": "Checking Git Status Across Trees",
                "code": "# Status command reports differences between Working Dir, Index, and HEAD:\ngit status\n\n# Output segments:\n# Changes to be committed:       <-- In Staging\n# Changes not staged for commit: <-- In Working Dir\n# Untracked files:               <-- New on disk",
                "explanation": "`git status` provides visibility across all three trees."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Stage and Check Staging Index",
            description="Create a file named 'config.json', stage it using `git add`, and run `git ls-files --stage` to verify its registration in the index.",
            starter_code="# Create config.json, stage it, and inspect the index\n",
            solution_code="echo '{\"env\": \"dev\"}' > config.json\ngit add config.json\ngit ls-files --stage",
            expected_output="100644 ... 0\tconfig.json"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which Git area acts as a preparatory buffer between your local disk edits and the permanent commit database?",
                options=[
                    "The Staging Area (also known as the Index)",
                    "The Central Remote Server",
                    "The Recycle Bin",
                    "The CPU Cache"
                ],
                correct_answer="The Staging Area (also known as the Index)",
                explanation="The staging area (index) allows crafting precise commit snapshots."
            ),
            QuizQuestionBlueprint(
                question="What file state represents a file that exists in your project directory but has never been tracked by Git?",
                options=["Untracked", "Staged", "Committed", "Modified"],
                correct_answer="Untracked",
                explanation="Untracked files are on disk but have not been staged via `git add` or committed."
            ),
            QuizQuestionBlueprint(
                question="Why is the Staging Area considered an architectural advantage of Git?",
                options=[
                    "It allows developers to craft granular, atomic commits rather than saving all dirty disk changes at once",
                    "It automatically fixes compiler bugs in your code",
                    "It prevents files from consuming hard drive space",
                    "It encrypts your source code with passwords"
                ],
                correct_answer="It allows developers to craft granular, atomic commits rather than saving all dirty disk changes at once",
                explanation="Staging enables selective grouping of related modifications into discrete commits."
            ),
            QuizQuestionBlueprint(
                question="Which low-level plumbing command displays the exact contents of the Git staging index?",
                options=["git ls-files --stage", "git show --index", "git print index", "git status --raw"],
                correct_answer="git ls-files --stage",
                explanation="`git ls-files --stage` prints the staged files and their SHA-1 blob hashes."
            ),
            QuizQuestionBlueprint(
                question="If you modify a file AFTER running `git add`, what will `git status` show?",
                options=[
                    "The file will appear under BOTH 'Changes to be committed' and 'Changes not staged for commit'",
                    "Git will automatically un-stage the file",
                    "Git will automatically commit the new changes",
                    "Git will throw a fatal error"
                ],
                correct_answer="The file will appear under BOTH 'Changes to be committed' and 'Changes not staged for commit'",
                explanation="The staged snapshot holds the state at `git add` time; subsequent disk edits remain unstaged."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 7: Basic Git Workflow (git status, git add, git commit)
    # ----------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Basic Git Workflow (`git status`, `git add`, `git commit`)",
        concept="The core daily loop of software engineering with Git: checking workspace status, selectively staging changes, and creating atomic commits.",
        analogy="`git status` is looking in the mirror to check your clothes. `git add` is packing the specific items you want into your suitcase. `git commit` is locking the suitcase and slapping a shipping label with a description on it.",
        theory_sections=[
            {
                "heading": "The Daily Loop of Version Control",
                "body": (
                    "Every software developer runs this fundamental triad dozens of times every day:\n"
                    "1. `git status`: Always inspect what is modified, untracked, or staged.\n"
                    "2. `git add <files>`: Explicitly stage changes.\n"
                    "3. `git commit -m \"message\"`: Seal the snapshot into repository history."
                )
            },
            {
                "heading": "Granular Staging vs Blanket Staging",
                "body": (
                    "While `git add .` stages all modified and untracked files in the current directory, professional practice advocates for staging specific files "
                    "or using `git add -p` (patch mode) to stage individual chunks/lines. This guarantees clean, focused pull requests."
                )
            },
            {
                "heading": "What is an Atomic Commit?",
                "body": (
                    "An **atomic commit** encapsulates exactly one logical change (e.g., 'fix: resolve navbar alignment' or 'feat: add user login endpoint'). "
                    "If a commit breaks the build or introduces a bug, atomic commits can be reverted cleanly without undoing unrelated features."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Checking Status with Verbose and Short Flags",
                "code": "# Full readable status:\ngit status\n\n# Compact two-letter status for fast command line scanning:\ngit status -s\n# ?? notes.txt   (Untracked)\n#  M app.py      (Modified in working tree)\n# M  app.py      (Staged in index)",
                "explanation": "Shows full descriptive output vs compact short format."
            },
            {
                "title": "Staging Single Files vs Entire Directories",
                "code": "# Stage a specific file:\ngit add src/auth.py\n\n# Stage all changes in current folder:\ngit add .\n\n# Interactive patch staging (choose specific lines):\ngit add -p src/auth.py",
                "explanation": "Selective staging ensures commits stay focused and atomic."
            },
            {
                "title": "Committing with Inline Message",
                "code": "# Create commit with a clear, descriptive message:\ngit commit -m \"feat: implement JWT token generation\"\n\n# Output confirms commit hash and files changed:\n# [main 7a4e8c1] feat: implement JWT token generation\n#  1 file changed, 45 insertions(+)",
                "explanation": "Creates a permanent snapshot identified by a SHA-1 hash."
            },
            {
                "title": "Combining Stage and Commit for Tracked Files",
                "code": "# Fast track for already-tracked modified files (skips untracked):\ngit commit -am \"fix: correct typo in hero section\"",
                "explanation": "The `-a` flag automatically stages modified tracked files before committing."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Complete Daily Git Cycle",
            description="Create a file 'server.py', check status using `git status -s`, stage 'server.py', and commit it with message 'feat: init server'.",
            starter_code="# Create server.py, check short status, stage, and commit\n",
            solution_code="echo 'import socket' > server.py\ngit status -s\ngit add server.py\ngit commit -m 'feat: init server'",
            expected_output="?? server.py\n[main ...] feat: init server\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary benefit of making 'atomic commits' in Git?",
                options=[
                    "Each commit represents one single logical change, making code review, debugging, and reverting straightforward",
                    "Atomic commits take up 90% less hard drive space",
                    "Atomic commits are processed by quantum computing nodes",
                    "Git only allows 10 lines of code per commit"
                ],
                correct_answer="Each commit represents one single logical change, making code review, debugging, and reverting straightforward",
                explanation="Atomic commits isolate single concerns, simplifying review and rollbacks."
            ),
            QuizQuestionBlueprint(
                question="What does the `-s` flag do when running `git status -s`?",
                options=[
                    "Displays status in a compact, short two-column format",
                    "Runs a silent status check with zero output",
                    "Saves the status to a log file",
                    "Stages all files automatically"
                ],
                correct_answer="Displays status in a compact, short two-column format",
                explanation="The `-s` (or `--short`) flag formats status into concise two-character code indicators."
            ),
            QuizQuestionBlueprint(
                question="What does the `-m` flag signify in `git commit -m \"message\"`?",
                options=[
                    "It provides the commit message directly in the terminal, bypassing the text editor",
                    "It merges branches automatically",
                    "It marks the commit as mandatory",
                    "It minimizes file sizes"
                ],
                correct_answer="It provides the commit message directly in the terminal, bypassing the text editor",
                explanation="The `-m` flag allows passing an inline commit log message directly."
            ),
            QuizQuestionBlueprint(
                question="Does running `git commit -a -m \"update\"` automatically stage brand-new, untracked files?",
                options=[
                    "No, `-a` only automatically stages already-tracked modified files, ignoring untracked files",
                    "Yes, it stages absolutely everything on disk",
                    "Yes, but only if they are Python files",
                    "It deletes untracked files automatically"
                ],
                correct_answer="No, `-a` only automatically stages already-tracked modified files, ignoring untracked files",
                explanation="`-a` only stages files already tracked by Git; new untracked files must be added via `git add`."
            ),
            QuizQuestionBlueprint(
                question="Which command allows interactively reviewing and staging individual code chunks/lines rather than whole files?",
                options=["git add -p", "git add --all", "git stage --slice", "git pick"],
                correct_answer="git add -p",
                explanation="`git add -p` (patch mode) lets you interactively choose hunks of changes to stage."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 8: Writing Good Commit Messages (Standard practices)
    # ----------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Writing Good Commit Messages (Standard practices)",
        concept="Engineering clean, professional commit histories by following industry standards: the 50/72 rule, imperative mood, and contextual rationale.",
        analogy="A bad commit message is like a doctor writing 'patient stuff happened' on a medical chart. A good commit message is like 'Administered 50mg amoxicillin to treat acute bacterial infection'—six months later, anyone knows exactly what happened and why.",
        theory_sections=[
            {
                "heading": "Why Commit Messages Matter",
                "body": (
                    "Code is read far more often than it is written. Two years from now when a line causes a production outage, "
                    "`git blame` will point to the author and commit message. A message like 'fixed bug' or 'updates' provides zero diagnostic value. "
                    "A great commit message explains **why** a change was necessary."
                )
            },
            {
                "heading": "The 7 Golden Rules of Git Commit Messages",
                "body": (
                    "1. Separate subject from body with a blank line.\n"
                    "2. Limit the subject line to 50 characters.\n"
                    "3. Capitalize the subject line.\n"
                    "4. Do not end the subject line with a period.\n"
                    "5. Use the **imperative mood** in the subject line (e.g., 'Add feature', not 'Added feature' or 'Adds feature').\n"
                    "6. Wrap the body at 72 characters.\n"
                    "7. Use the body to explain **what** and **why** vs how (the code diff shows how)."
                )
            },
            {
                "heading": "The Imperative Mood Test",
                "body": (
                    "A properly formed Git commit subject should always complete the sentence:\n"
                    "`\"If applied, this commit will <your subject line>\"`\n"
                    "- If applied, this commit will *Fix race condition in checkout service* (Correct).\n"
                    "- If applied, this commit will *Fixed race condition* (Incorrect grammar)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Bad vs Good Commit Messages",
                "code": "# BAD COMMIT MESSAGES:\n# - 'stuff'\n# - 'wip'\n# - 'fixed bugs and changed styling'\n# - 'final commit for real'\n\n# GOOD COMMIT MESSAGES:\n# - 'Fix race condition during payment checkout'\n# - 'Refactor user authentication to support OAuth2'\n# - 'Add rate limiting to public login endpoint'",
                "explanation": "Clear, imperative subjects provide immediate context."
            },
            {
                "title": "Writing Full Multi-Line Commit via Editor",
                "code": "# Running git commit without -m opens your configured editor:\ngit commit\n\n# Content inside editor:\n# Summarize changes in around 50 characters or less\n# \n# More detailed explanatory text, if necessary. Wrap it to\n# about 72 characters. Explain the problem that this commit\n# solves or the business rationale behind it.",
                "explanation": "Allows thorough documentation of complex architectural changes."
            },
            {
                "title": "Multi-Line Message directly from CLI",
                "code": "# Pass multiple -m flags to supply subject and body directly:\ngit commit \\\n  -m \"Fix memory leak in image processing daemon\" \\\n  -m \"Buffer objects were retained after socket closure. Explicitly calling free() ensures memory drops back to baseline under load.\"",
                "explanation": "Consecutive -m arguments are separated as paragraphs."
            },
            {
                "title": "Inspecting Past Commit Messages",
                "code": "# View full message bodies in history:\ngit log -n 1\n\n# Output displays Author, Date, Subject, and full explanatory Body",
                "explanation": "Shows the complete message recorded in the log."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Professional Imperative Commit",
            description="Create a file 'calc.py', stage it, and commit it with an imperative subject under 50 characters: 'Add addition and subtraction functions'.",
            starter_code="# Create calc.py, stage it, and commit with proper message\n",
            solution_code="echo 'def add(a, b): return a + b' > calc.py\ngit add calc.py\ngit commit -m \"Add addition and subtraction functions\"",
            expected_output="[main ...] Add addition and subtraction functions\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the recommended mood for Git commit subject lines according to standard conventions?",
                options=[
                    "Imperative mood (e.g., 'Add feature', 'Fix bug')",
                    "Past tense (e.g., 'Added feature', 'Fixed bug')",
                    "Present continuous (e.g., 'Adding feature', 'Fixing bug')",
                    "Passive voice (e.g., 'Feature was added by me')"
                ],
                correct_answer="Imperative mood (e.g., 'Add feature', 'Fix bug')",
                explanation="Imperative mood matches Git's generated messages (e.g., 'Merge branch', 'Revert commit')."
            ),
            QuizQuestionBlueprint(
                question="What does the '50/72 rule' recommend in Git commit message formatting?",
                options=[
                    "Keep the subject line under 50 characters and wrap the detailed body at 72 characters",
                    "Commit 50 times a day and write 72 words",
                    "Use font size 50 for headings and 72 for code",
                    "Keep 50 branches open and delete them after 72 days"
                ],
                correct_answer="Keep the subject line under 50 characters and wrap the detailed body at 72 characters",
                explanation="50 characters keeps summary logs readable; 72-char line wrapping prevents terminal overflow."
            ),
            QuizQuestionBlueprint(
                question="Which test sentence verifies if a commit subject line is properly written in imperative mood?",
                options=[
                    "\"If applied, this commit will <your subject line>\"",
                    "\"Yesterday, I worked hard to <your subject line>\"",
                    "\"The customer complained about <your subject line>\"",
                    "\"My manager told me to <your subject line>\""
                ],
                correct_answer="\"If applied, this commit will <your subject line>\"",
                explanation="Plugging the subject into this sentence immediately highlights correct imperative grammar."
            ),
            QuizQuestionBlueprint(
                question="What should the extended body of a commit message explain?",
                options=[
                    "The context, motivation, and 'why' behind the change rather than how (which the code diff shows)",
                    "A line-by-line copy of the diff",
                    "The author's personal diary entry",
                    "The entire contents of the project README"
                ],
                correct_answer="The context, motivation, and 'why' behind the change rather than how (which the code diff shows)",
                explanation="The code diff shows how code changed; the message explains why the change was made."
            ),
            QuizQuestionBlueprint(
                question="Should the subject line of a standard Git commit message end with a period/full-stop?",
                options=[
                    "No, subject lines should not end with a trailing period",
                    "Yes, every commit message must end with three periods",
                    "Yes, a period is required by git syntax parser",
                    "Only on Windows"
                ],
                correct_answer="No, subject lines should not end with a trailing period",
                explanation="Standard conventions omit trailing periods on commit subject lines to conserve space."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 9: Viewing History (git log, --oneline, --graph)
    # ----------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: Viewing History (`git log`, `--oneline`, `--graph`)",
        concept="Navigating, filtering, and visualizing repository history using Git's robust log formatting flags, graphs, and revision ranges.",
        analogy="`git log` is the security camera DVR playback of your project. Standard `git log` shows every detail in slow motion; `--oneline --graph` turns the recording into a subway map showing which trains merged onto which tracks.",
        theory_sections=[
            {
                "heading": "Exploring Project History",
                "body": (
                    "`git log` queries the Directed Acyclic Graph (DAG) of commits starting from `HEAD` backwards along parent pointers. "
                    "By default, it shows commit hash, author, date, and full message."
                )
            },
            {
                "heading": "Essential Log Visualization Flags",
                "body": (
                    "- `--oneline`: Compresses each commit into its short 7-character SHA-1 hash and subject line.\n"
                    "- `--graph`: Draws an ASCII text graph depicting branching and merge histories on the left side.\n"
                    "- `--decorate`: Shows which branch names or tags point to which commits.\n"
                    "- `--stat`: Shows a diffstat summary of files modified, insertions, and deletions per commit."
                )
            },
            {
                "heading": "Filtering History",
                "body": (
                    "Git allows filtering log output across multiple dimensions:\n"
                    "- `git log -n 5`: Limit to the last 5 commits.\n"
                    "- `git log --author=\"Alice\"`: Filter by author name or email.\n"
                    "- `git log --since=\"2 weeks ago\"`: Filter by timeframe.\n"
                    "- `git log -S \"secret_key\"`: The 'pickaxe' search—finds commits that introduced or removed that exact string."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Standard vs Compact Log Output",
                "code": "# Default verbose log:\ngit log\n\n# Beautiful compact single-line history:\ngit log --oneline\n# 7a4e8c1 feat: implement JWT token generation\n# 3f2a1b9 feat: create homepage\n# 1c0d4e8 Initial commit",
                "explanation": "Compresses output into quick glanceable lines."
            },
            {
                "title": "Visualizing Branch Graphs in ASCII",
                "code": "# The ultimate history command:\ngit log --graph --oneline --decorate --all\n\n# Output displays an ASCII branching tree:\n# * 8d1f2e3 (HEAD -> main, origin/main) Merge branch 'feature'\n# |\\  \n# | * 4b2c1d0 (feature) feat: add user avatar upload\n# |/  \n# * a1b2c3d chore: update dependencies",
                "explanation": "Illustrates how branches diverged and merged over time."
            },
            {
                "title": "Inspecting File Change Statistics",
                "code": "# Display files modified and line counters per commit:\ngit log --stat -n 2\n\n# Output shows:\n#  src/auth.py | 15 +++++++++++++--\n#  tests/test_auth.py | 24 ++++++++++++++++++++++++\n#  2 files changed, 37 insertions(+), 2 deletions(-)",
                "explanation": "Provides quantitative insight into changes made per commit."
            },
            {
                "title": "Filtering History by File or Date",
                "code": "# Show only commits that touched a specific file:\ngit log --oneline -- path/to/database.py\n\n# Show commits made in the last 7 days:\ngit log --since=\"7 days ago\" --oneline",
                "explanation": "Narrows historical exploration to targeted files or dates."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Compact Graph History",
            description="Run the command to display repository history formatted as a single line per commit with ASCII graph visualization and all branch decorations.",
            starter_code="# Run git log with graph, oneline, and all flags\n",
            solution_code="git log --graph --oneline --all --decorate",
            expected_output="* ... (HEAD -> main) ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which flag condenses each commit into a 7-character short SHA-1 hash and subject line in `git log`?",
                options=["--oneline", "--short", "--compact", "--summary"],
                correct_answer="--oneline",
                explanation="`git log --oneline` formats each commit on a single readable line."
            ),
            QuizQuestionBlueprint(
                question="What does the `--graph` flag draw in `git log` output?",
                options=[
                    "An ASCII text tree showing branch forks and merges",
                    "A pie chart of languages used",
                    "A line chart showing commits per hour",
                    "A scatter plot of author activity"
                ],
                correct_answer="An ASCII text tree showing branch forks and merges",
                explanation="`--graph` prints an ASCII visual graph of the repository's commit topology."
            ),
            QuizQuestionBlueprint(
                question="Which command limits log output to commits authored specifically by 'John'?",
                options=[
                    "git log --author=\"John\"",
                    "git log --user=\"John\"",
                    "git log --who=\"John\"",
                    "git log --filter-john"
                ],
                correct_answer="git log --author=\"John\"",
                explanation="`--author` filters the commit history by the author field matching the string or regex."
            ),
            QuizQuestionBlueprint(
                question="What does the `-S` flag (the 'pickaxe') do in `git log -S \"QUERY\"`?",
                options=[
                    "Finds commits that added or removed the specific string 'QUERY' within their code diffs",
                    "Searches only for commits made on Saturdays",
                    "Sorts commits alphabetically",
                    "Shows only commits smaller than 100 bytes"
                ],
                correct_answer="Finds commits that added or removed the specific string 'QUERY' within their code diffs",
                explanation="The `-S` flag searches commit diffs for additions or removals of specific text."
            ),
            QuizQuestionBlueprint(
                question="How can you view the commit history for a single specific file `src/app.py`?",
                options=[
                    "git log -- src/app.py",
                    "git log -f src/app.py",
                    "git file log src/app.py",
                    "git history src/app.py"
                ],
                correct_answer="git log -- src/app.py",
                explanation="Passing a file path after `--` restricts `git log` to revisions modifying that path."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 10: Ignoring Files (.gitignore & global ignore)
    # ----------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: Ignoring Files (`.gitignore` & global ignore)",
        concept="Preventing sensitive credentials, compiled binaries, temporary logs, and package caches from polluting repositories using `.gitignore` pattern syntax.",
        analogy="A `.gitignore` file is like a 'Do Not Disturb' sign on your door for Git. You are telling Git: 'I don't care if there are dirty dishes (`.log`) or muddy shoes (`node_modules`) in this room, do not ever pack them into my permanent luggage.'",
        theory_sections=[
            {
                "heading": "Why Ignore Files?",
                "body": (
                    "Not every file in your project directory belongs in version control. Committing unnecessary files causes repository bloat, merge conflicts, "
                    "and catastrophic security breaches (e.g., committing `.env` containing AWS secret keys or database passwords).\n"
                    "Common categories to ignore:\n"
                    "- Build artifacts & compiled binaries (`.o`, `.class`, `dist/`, `build/`).\n"
                    "- Dependencies (`node_modules/`, `venv/`).\n"
                    "- Environment secrets (`.env`, `credentials.json`).\n"
                    "- OS metadata (`.DS_Store`, `Thumbs.db`)."
                )
            },
            {
                "heading": "Pattern Syntax Rules",
                "body": (
                    "- Blank lines or lines starting with `#` are ignored.\n"
                    "- Standard glob patterns apply: `*` matches zero or more chars; `?` matches single char.\n"
                    "- Trailing slash `dir/` specifies that the pattern matches only directories.\n"
                    "- Leading slash `/file` matches files relative to the `.gitignore` directory level.\n"
                    "- An exclamation mark `!` negates a pattern (whitelists an otherwise ignored file)."
                )
            },
            {
                "heading": "Crucial Rule: .gitignore Does NOT Untrack Existing Files",
                "body": (
                    "Adding a file to `.gitignore` only prevents **untracked** files from being staged. "
                    "If a file was already committed in the past, Git continues tracking it! "
                    "You must explicitly remove it from the index using `git rm --cached <file>`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Sample Production .gitignore File",
                "code": "# Python / Node / Env ignore rules:\n.env\n*.log\n__pycache__/\n*.pyc\nnode_modules/\ndist/\n\n# Ignore all .txt files except important notes:\n*.txt\n!important_notes.txt",
                "explanation": "Standard globs, directory markers, and negation rules."
            },
            {
                "title": "Untracking a Mistakenly Committed Secret",
                "code": "# If .env was accidentally committed, remove it from Git index WITHOUT deleting disk file:\ngit rm --cached .env\n\n# Stage .gitignore and commit the removal:\necho \".env\" >> .gitignore\ngit add .gitignore\ngit commit -m \"fix: stop tracking sensitive .env file\"",
                "explanation": "`--cached` removes the file from Git index while preserving it on disk."
            },
            {
                "title": "Debugging Ignore Rules with git check-ignore",
                "code": "# Find out WHICH rule in .gitignore is matching a given file:\ngit check-ignore -v secret.log\n\n# Output reveals filename, line number, and matching pattern:\n# .gitignore:2:*.log    secret.log",
                "explanation": "Helps troubleshoot why a file is being ignored."
            },
            {
                "title": "Configuring Global OS-Level Ignore",
                "code": "# Configure a global ignore file for OS clutter like .DS_Store across all repos:\ngit config --global core.excludesFile ~/.gitignore_global\necho \".DS_Store\" >> ~/.gitignore_global\necho \"Thumbs.db\" >> ~/.gitignore_global",
                "explanation": "Prevents OS files from polluting any repository on your machine."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create .gitignore and Untrack File",
            description="Create a file named 'app.log' and a file named '.gitignore' ignoring '*.log'. Remove 'app.log' from staging if staged and verify with status.",
            starter_code="# Create files, write .gitignore, and check git status\n",
            solution_code="echo 'error 500' > app.log\necho '*.log' > .gitignore\ngit status",
            expected_output="Untracked files:\n  .gitignore"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if you add a file to `.gitignore` that was ALREADY committed in previous commits?",
                options=[
                    "Git continues tracking the file; you must run `git rm --cached` to stop tracking it",
                    "Git automatically deletes the file from history and disk",
                    "Git throws an error and reverts the last commit",
                    "Git corrupts the repository index"
                ],
                correct_answer="Git continues tracking the file; you must run `git rm --cached` to stop tracking it",
                explanation="`.gitignore` only stops untracked files from being staged; already-tracked files must be removed from the cache."
            ),
            QuizQuestionBlueprint(
                question="Which symbol is used in `.gitignore` to negate a rule and whitelist a specific file?",
                options=["!", "^", "*", "~"],
                correct_answer="!",
                explanation="The exclamation mark `!` negates an ignore pattern, preventing matching files from being ignored."
            ),
            QuizQuestionBlueprint(
                question="Which command allows you to troubleshoot and see which exact line in `.gitignore` is ignoring a file?",
                options=["git check-ignore -v <filename>", "git ignore --test <filename>", "git find-ignore <filename>", "git inspect-ignore"],
                correct_answer="git check-ignore -v <filename>",
                explanation="`git check-ignore -v` prints the file, line number, and pattern causing a file to be ignored."
            ),
            QuizQuestionBlueprint(
                question="What does the trailing slash indicate in the `.gitignore` pattern `logs/`?",
                options=[
                    "It matches only directories named 'logs', not files named 'logs'",
                    "It ignores all files except those in 'logs'",
                    "It deletes the folder automatically",
                    "It encrypts the folder"
                ],
                correct_answer="It matches only directories named 'logs', not files named 'logs'",
                explanation="A trailing slash restricts the match strictly to directories."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of configuring `core.excludesFile` globally?",
                options=[
                    "To ignore OS-specific clutter like `.DS_Store` or `Thumbs.db` across all repositories on your computer",
                    "To delete unwanted repositories",
                    "To hide branches from coworkers",
                    "To bypass git commit verification"
                ],
                correct_answer="To ignore OS-specific clutter like `.DS_Store` or `Thumbs.db` across all repositories on your computer",
                explanation="A global excludes file applies ignore patterns universally to every repo on that machine."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 11: Concept of Branches (The HEAD pointer)
    # ----------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Concept of Branches (The HEAD pointer)",
        concept="Understanding branches as lightweight movable pointers to commit hashes and how the HEAD reference tracks your active context.",
        analogy="A branch in Git is not a heavy copy of all your files; it is simply a lightweight sticky note with a name written on it pointing to a specific commit. Moving to another branch just moves your magnifying glass (HEAD) to look at a different sticky note.",
        theory_sections=[
            {
                "heading": "What is a Branch in Git?",
                "body": (
                    "In older systems like SVN, creating a branch copied all project files into a new directory, taking minutes and gigabytes. "
                    "In Git, a branch is merely a 41-byte text file inside `.git/refs/heads/` that stores a 40-character SHA-1 commit hash. "
                    "Creating or deleting a branch takes less than 2 milliseconds and zero extra disk space."
                )
            },
            {
                "heading": "The HEAD Pointer",
                "body": (
                    "`HEAD` is a special reference pointer that tells Git where you are right now. "
                    "Normally, `HEAD` points to a branch reference (e.g. `ref: refs/heads/main`). "
                    "When you make a new commit, the currently checked-out branch advances automatically to the new commit, and `HEAD` moves with it."
                )
            },
            {
                "heading": "Detached HEAD State",
                "body": (
                    "If you check out a specific commit hash directly rather than a branch name (`git checkout <hash>`), "
                    "you enter a **Detached HEAD** state. `HEAD` points directly to a commit rather than a branch. "
                    "Any new commits made here are not associated with any branch and can be garbage-collected if you switch away!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Branch Storage Internals",
                "code": "# Inspect the internal file representing the main branch:\ncat .git/refs/heads/main\n\n# Output is simply a 40-character SHA-1 commit hash:\n# 7a4e8c1d5f2a1b9e3f4a5c6d7e8f9a0b1c2d3e4f",
                "explanation": "Demonstrates that a Git branch is literally just a 41-byte pointer."
            },
            {
                "title": "Inspecting HEAD Reference",
                "code": "# Read the HEAD file to see what branch is active:\ncat .git/HEAD\n\n# Output:\n# ref: refs/heads/main",
                "explanation": "HEAD points to the symbolic reference of your active branch."
            },
            {
                "title": "Visualizing How Branches Advance on Commit",
                "code": "# Initial:\n# [Commit A] <-- main, HEAD\n#\n# After git commit:\n# [Commit A] <-- [Commit B] <-- main, HEAD",
                "explanation": "Committing advances both the current branch pointer and HEAD."
            },
            {
                "title": "Listing Local Branches with Verbose Hash",
                "code": "# List all local branches with their latest commit SHA and subject:\ngit branch -v\n\n# Output:\n# * main     7a4e8c1 feat: implement JWT token generation\n#   feature  3f2a1b9 feat: add payment webhook",
                "explanation": "The asterisk (*) denotes whichever branch HEAD currently points to."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Branch Pointers Internally",
            description="Run `git branch -v` to view your local branches and their active commit pointers.",
            starter_code="# Inspect local branches with commit hashes\n",
            solution_code="git branch -v",
            expected_output="* main ... [commit message]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Under the hood inside the `.git` directory, what is a Git branch?",
                options=[
                    "A simple 41-byte text file containing a 40-character commit SHA-1 hash",
                    "A complete duplicate copy of all files in the project",
                    "A virtual machine snapshot",
                    "A compressed zip archive of your source code"
                ],
                correct_answer="A simple 41-byte text file containing a 40-character commit SHA-1 hash",
                explanation="Branches in Git are lightweight pointers referencing a commit hash."
            ),
            QuizQuestionBlueprint(
                question="What does the `HEAD` reference represent in Git?",
                options=[
                    "A pointer referencing your currently active branch or commit",
                    "The very first commit in repository history",
                    "The remote GitHub server administrator",
                    "The project's README file"
                ],
                correct_answer="A pointer referencing your currently active branch or commit",
                explanation="`HEAD` indicates the currently checked-out branch or commit snapshot."
            ),
            QuizQuestionBlueprint(
                question="What does it mean when your repository is in a 'Detached HEAD' state?",
                options=[
                    "HEAD is pointing directly to a specific commit hash instead of a named branch",
                    "The `.git` directory has been deleted",
                    "Your computer lost its internet connection",
                    "The master branch was renamed"
                ],
                correct_answer="HEAD is pointing directly to a specific commit hash instead of a named branch",
                explanation="Detached HEAD occurs when checking out a commit SHA directly rather than a branch."
            ),
            QuizQuestionBlueprint(
                question="Why is branch creation in Git virtually instantaneous regardless of project size?",
                options=[
                    "Git only writes a 40-character hash into a tiny text file without copying project files",
                    "Git compresses all branches in the background",
                    "Git skips file validation during branch creation",
                    "Git offloads branch creation to GitHub's cloud servers"
                ],
                correct_answer="Git only writes a 40-character hash into a tiny text file without copying project files",
                explanation="Creating a branch requires writing only 41 bytes to disk."
            ),
            QuizQuestionBlueprint(
                question="Which symbol indicates your currently checked-out active branch in `git branch` output?",
                options=["An asterisk (*)", "An arrow (->)", "A hash (#)", "An exclamation mark (!)"],
                correct_answer="An asterisk (*)",
                explanation="The asterisk `*` marks the branch currently pointed to by HEAD."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 12: Creating & Switching Branches (git branch, checkout, switch)
    # ----------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Creating & Switching Branches (`git branch`, `checkout`, `switch`)",
        concept="Mastering branch creation, switching, and the modern `git switch` command introduced to eliminate the overloaded semantics of `git checkout`.",
        analogy="Imagine writing a book in a parallel universe. You branch off to write an alternate ending where the villain wins. You can jump back and forth between the happy timeline and the villain timeline instantly without either timeline altering the other.",
        theory_sections=[
            {
                "heading": "Branch Creation and Navigation",
                "body": (
                    "To work on a new feature or bugfix without endangering production stability, you create a branch. "
                    "Historically, `git checkout` was used for both switching branches and discarding file edits. "
                    "To eliminate this confusion, Git 2.23 introduced `git switch` (for branches) and `git restore` (for files)."
                )
            },
            {
                "heading": "Commands Comparison",
                "body": (
                    "- Create branch: `git branch <name>`\n"
                    "- Switch to branch (old way): `git checkout <name>`\n"
                    "- Switch to branch (modern way): `git switch <name>`\n"
                    "- Create AND switch in one command: `git switch -c <name>` (or `git checkout -b <name>`)."
                )
            },
            {
                "heading": "Working Directory Synchronization",
                "body": (
                    "When you switch branches, Git automatically updates the files in your working directory to match the commit pointed to by that branch. "
                    "If you have unstaged dirty edits that conflict with the destination branch, Git prevents the switch to protect you from data loss."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating and Switching via Modern git switch",
                "code": "# Create and switch to a new feature branch in one command:\ngit switch -c feature/login-page\n\n# Output:\n# Switched to a new branch 'feature/login-page'",
                "explanation": "`git switch -c` (create) is the modern replacement for `git checkout -b`."
            },
            {
                "title": "Listing All Branches",
                "code": "# List all local branches:\ngit branch\n\n# List both local AND remote-tracking branches:\ngit branch -a",
                "explanation": "`-a` displays all local and remote branches in the repository."
            },
            {
                "title": "Switching Back to Previous Branch Quickly",
                "code": "# Switch to the previous branch you were on (like TV remote 'last channel'):\ngit switch -\n\n# Output:\n# Switched to branch 'main'",
                "explanation": "`git switch -` toggles back to the previously active branch."
            },
            {
                "title": "Legacy checkout Syntax (For Reference)",
                "code": "# Older syntax still widely encountered in tutorials:\ngit checkout -b feature/payment\ngit checkout main",
                "explanation": "Legacy equivalent of git switch."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create and Switch to Feature Branch",
            description="Use `git switch -c` to create and switch to a new branch named 'feature/api-v2', create a file 'api.txt', stage, and commit it.",
            starter_code="# Create branch feature/api-v2, write api.txt, stage, commit\n",
            solution_code="git switch -c feature/api-v2\necho 'v2' > api.txt\ngit add api.txt\ngit commit -m 'feat: add api v2 file'",
            expected_output="Switched to a new branch 'feature/api-v2'\n[feature/api-v2 ...] feat: add api v2 file"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why did Git 2.23 introduce `git switch` and `git restore`?",
                options=[
                    "To separate branch management and file restoration, which were previously both overloaded onto `git checkout`",
                    "Because `git checkout` was deleted from Git",
                    "To make Git incompatible with older servers",
                    "To require cloud authentication"
                ],
                correct_answer="To separate branch management and file restoration, which were previously both overloaded onto `git checkout`",
                explanation="`git switch` manages branches, while `git restore` handles files, clarifying CLI responsibilities."
            ),
            QuizQuestionBlueprint(
                question="Which modern command creates AND immediately switches to a new branch named 'dev'?",
                options=["git switch -c dev", "git branch --jump dev", "git new branch dev", "git checkout --new dev"],
                correct_answer="git switch -c dev",
                explanation="`git switch -c <branch>` creates and checks out the new branch in a single step."
            ),
            QuizQuestionBlueprint(
                question="What shortcut switches back to the previously checked-out branch (similar to a 'last channel' TV button)?",
                options=["git switch -", "git switch --back", "git switch prev", "git switch ~1"],
                correct_answer="git switch -",
                explanation="`git switch -` (or `git checkout -`) returns to the previous branch."
            ),
            QuizQuestionBlueprint(
                question="What happens to the files on your hard drive when you switch branches in Git?",
                options=[
                    "Git updates, adds, or removes files in your working directory so it matches the snapshot of the target branch",
                    "Nothing, you must manually copy files",
                    "Your files are permanently deleted",
                    "Git opens every file in Notepad"
                ],
                correct_answer="Git updates, adds, or removes files in your working directory so it matches the snapshot of the target branch",
                explanation="Git synchronizes your working tree with the commit pointed to by the target branch."
            ),
            QuizQuestionBlueprint(
                question="Which command lists both local branches and remote-tracking branches?",
                options=["git branch -a", "git branch -l", "git branch --all-local", "git branch --net"],
                correct_answer="git branch -a",
                explanation="The `-a` (or `--all`) flag lists both local and remote branches."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 13: Renaming and Deleting Branches
    # ----------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Renaming and Deleting Branches",
        concept="Safely maintaining repository hygiene by renaming branches (`-m`) and deleting merged or obsolete branches safely (`-d`) vs forcefully (`-D`).",
        analogy="Deleting a merged branch is like recycling the scratch paper you used to solve a math problem after you've already written the answer on the final exam. Force-deleting (`-D`) is throwing away paper with unfinished problems you might regret losing.",
        theory_sections=[
            {
                "heading": "Branch Maintenance and Hygiene",
                "body": (
                    "In agile teams where multiple feature branches are spawned weekly, maintaining clean branch lists is critical. "
                    "Keeping stale, merged branches clutters autocompletion and complicates release planning."
                )
            },
            {
                "heading": "Safe Deletion (`-d`) vs Force Deletion (`-D`)",
                "body": (
                    "- `git branch -d <name>`: Safe deletion. Git checks if the branch has been fully merged into your upstream or current branch. "
                    "If unmerged commits exist, Git refuses to delete it to prevent accidental loss of work.\n"
                    "- `git branch -D <name>`: Force deletion (equivalent to `git branch --delete --force`). "
                    "Destroys the pointer immediately even if unmerged commits are present."
                )
            },
            {
                "heading": "Renaming Branches (`-m`)",
                "body": (
                    "To rename your currently active branch: `git branch -m <new-name>`. "
                    "To rename another branch without switching to it: `git branch -m <old-name> <new-name>`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Renaming Current Branch to Modern Convention",
                "code": "# Rename current active branch (e.g., from master to main):\ngit branch -m main",
                "explanation": "Updates the local pointer name in .git/refs/heads/."
            },
            {
                "title": "Renaming an Arbitrary Branch",
                "code": "# Rename a branch without checking it out first:\ngit branch -m old-feature-name feature/shopping-cart",
                "explanation": "Takes old name followed by new name."
            },
            {
                "title": "Safe Deletion of Merged Feature Branch",
                "code": "# Delete a branch that has already been merged into main:\ngit switch main\ngit branch -d feature/shopping-cart\n\n# Output confirms deletion:\n# Deleted branch feature/shopping-cart (was 4b2c1d0).",
                "explanation": "Git verifies merge status before deleting."
            },
            {
                "title": "Force Deletion of Experimental Abandoned Branch",
                "code": "# Force-delete an experimental branch with unmerged commits:\ngit branch -D experiment/failed-ai-model\n\n# Output:\n# Deleted branch experiment/failed-ai-model (was 9f8e7d6).",
                "explanation": "`-D` overrides Git's safety warning."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create, Rename, and Delete Branch",
            description="Create branch 'temp-fix', rename it to 'bugfix-temp', switch back to 'main', and delete 'bugfix-temp' using `git branch -D`.",
            starter_code="# Create temp-fix, rename to bugfix-temp, switch to main, delete\n",
            solution_code="git branch temp-fix\ngit branch -m temp-fix bugfix-temp\ngit switch main\ngit branch -D bugfix-temp",
            expected_output="Deleted branch bugfix-temp (was ...)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What protection does `git branch -d` provide that `git branch -D` does not?",
                options=[
                    "It refuses to delete a branch if it contains unmerged commits, preventing accidental code loss",
                    "It requires a password before deleting",
                    "It backs up the branch to an external USB drive",
                    "It only deletes files smaller than 1MB"
                ],
                correct_answer="It refuses to delete a branch if it contains unmerged commits, preventing accidental code loss",
                explanation="Safe delete `-d` checks merge status; force delete `-D` discards the pointer unconditionally."
            ),
            QuizQuestionBlueprint(
                question="Can you delete the branch you are currently standing on / checked out to?",
                options=[
                    "No, Git will prevent you from deleting the currently active HEAD branch",
                    "Yes, Git will switch you to a random branch automatically",
                    "Yes, but your terminal will close",
                    "Only if you use `--force-all`"
                ],
                correct_answer="No, Git will prevent you from deleting the currently active HEAD branch",
                explanation="You cannot delete the active branch; you must switch to another branch first."
            ),
            QuizQuestionBlueprint(
                question="Which command renames your currently checked-out branch to 'main'?",
                options=["git branch -m main", "git rename-branch main", "git branch --name main", "git update branch main"],
                correct_answer="git branch -m main",
                explanation="`git branch -m <name>` moves/renames the current branch."
            ),
            QuizQuestionBlueprint(
                question="What is the equivalent long-form flag for `git branch -D`?",
                options=["git branch --delete --force", "git branch --drop", "git branch --destroy", "git branch --discard"],
                correct_answer="git branch --delete --force",
                explanation="`-D` is shortcut for `--delete --force`."
            ),
            QuizQuestionBlueprint(
                question="When you delete a branch in Git, does Git immediately delete the underlying commit objects from disk?",
                options=[
                    "No, only the pointer is deleted; commits remain in the database until garbage collection cleans them up",
                    "Yes, all commit objects are zeroed out instantly",
                    "Yes, and files on disk are shredded",
                    "Git writes zeroes over the hard drive sectors"
                ],
                correct_answer="No, only the pointer is deleted; commits remain in the database until garbage collection cleans them up",
                explanation="Deleting a branch merely removes the ref pointer; commits linger until pruned by GC."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 14: Merging Branches (git merge)
    # ----------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: Merging Branches (`git merge`)",
        concept="Integrating divergent lines of development by merging feature branches into main lines using `git merge`.",
        analogy="Merging is like two streams uniting into a single river. Your teammate worked on the stream that flows from the left (frontend), you worked on the stream on the right (backend), and `git merge` combines their waters into one powerful current.",
        theory_sections=[
            {
                "heading": "The Purpose of Merging",
                "body": (
                    "Branching allows developers to work in isolation. Once a feature is developed, tested, and reviewed, "
                    "it must be incorporated back into the shared branch (usually `main`). "
                    "The `git merge` command reconciles separate commit histories into one."
                )
            },
            {
                "heading": "The Standard Merging Workflow",
                "body": (
                    "Always remember: **You merge the target branch INTO your current branch**.\n"
                    "1. Switch to the receiving branch: `git switch main`\n"
                    "2. Run the merge: `git merge feature/auth`\n"
                    "Git will analyze the commit history, find the common ancestor, and integrate the changes."
                )
            },
            {
                "heading": "Merge Commits",
                "body": (
                    "When histories have diverged, Git generates a special commit called a **Merge Commit**. "
                    "Unlike standard commits which have exactly one parent commit, a merge commit has **two parent commits**, "
                    "tying the two historical branches together."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Executing a Standard Merge Workflow",
                "code": "# 1. Switch to the receiving branch:\ngit switch main\n\n# 2. Merge the feature branch into main:\ngit merge feature/user-profile\n\n# Output confirms merge details:\n# Updating 7a4e8c1..4b2c1d0\n# Fast-forward\n#  profile.html | 24 ++++++++++++++++++++++++\n#  1 file changed, 24 insertions(+)",
                "explanation": "Incorporates feature branch commits into main."
            },
            {
                "title": "Aborting a Merge with Conflicts",
                "code": "# If a merge runs into conflicts and you want to roll back to pre-merge state:\ngit merge --abort",
                "explanation": "Safely cancels the merge and restores your branch."
            },
            {
                "title": "Inspecting Merge Parents in Git Log",
                "code": "# Merge commits have two parents visible in raw commit metadata:\ngit cat-file -p HEAD\n\n# Output includes:\n# tree d8329fc...\n# parent 7a4e8c1... (Main branch parent)\n# parent 4b2c1d0... (Feature branch parent)",
                "explanation": "Reveals the two parent hashes linked by the merge."
            },
            {
                "title": "Checking Merged vs Unmerged Branches",
                "code": "# List branches whose changes have already been merged into current branch:\ngit branch --merged\n\n# List branches that still have pending unmerged changes:\ngit branch --no-merged",
                "explanation": "Helps identify which branches are safe to delete."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Branch, Commit, and Merge into Main",
            description="Create and switch to branch 'feat-docs', create 'README.md', stage and commit it, switch back to 'main', and merge 'feat-docs' into 'main'.",
            starter_code="# Create branch, commit README, switch to main, and merge\n",
            solution_code="git switch -c feat-docs\necho '# Project Docs' > README.md\ngit add README.md\ngit commit -m 'docs: add initial readme'\ngit switch main\ngit merge feat-docs",
            expected_output="Updating ...\nFast-forward\n README.md | 1 +\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="If you want to merge changes from `feature` into `main`, which branch must you be currently standing on when running `git merge feature`?",
                options=[
                    "`main`",
                    "`feature`",
                    "`origin`",
                    "It does not matter"
                ],
                correct_answer="`main`",
                explanation="You always check out the branch that will receive the incoming changes before running merge."
            ),
            QuizQuestionBlueprint(
                question="How many parent commits does a standard non-fast-forward merge commit have?",
                options=["Two", "One", "Zero", "Three"],
                correct_answer="Two",
                explanation="A merge commit binds two divergent branches and references both parent commit hashes."
            ),
            QuizQuestionBlueprint(
                question="Which command cancels an in-progress merge and restores your repository to its exact pre-merge state?",
                options=["git merge --abort", "git merge --cancel", "git merge --stop", "git undo merge"],
                correct_answer="git merge --abort",
                explanation="`git merge --abort` resets the working tree and index to before the merge command was run."
            ),
            QuizQuestionBlueprint(
                question="Which command lists all local branches whose commits have already been safely integrated into your current branch?",
                options=["git branch --merged", "git branch --safe", "git branch --done", "git branch --clean"],
                correct_answer="git branch --merged",
                explanation="`git branch --merged` displays branches fully merged into the checked-out branch."
            ),
            QuizQuestionBlueprint(
                question="Does running `git merge feature` delete the `feature` branch after merging?",
                options=[
                    "No, Git preserves the feature branch pointer; you must manually delete it if desired",
                    "Yes, Git deletes merged branches instantly",
                    "Only on Friday evenings",
                    "Only if the commit message says 'delete'"
                ],
                correct_answer="No, Git preserves the feature branch pointer; you must manually delete it if desired",
                explanation="Git never deletes branches automatically after a merge; developers manage branch lifecycles."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 15: Types of Merges (Fast-Forward vs 3-Way/Recursive)
    # ----------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Types of Merges (Fast-Forward vs 3-Way/Recursive)",
        concept="Contrasting Fast-Forward merges against 3-Way recursive merges and controlling history topology using `--no-ff` and `--ff-only` flags.",
        analogy="Fast-Forward is like walking straight ahead along a single road where someone simply moved the destination sign further down the path. A 3-Way merge is like two hikers who took different trails across a mountain meeting up at a lodge and combining their maps into a new master map.",
        theory_sections=[
            {
                "heading": "Fast-Forward Merge",
                "body": (
                    "A **Fast-Forward (FF)** merge occurs when the target branch (`main`) has had **no new commits** since the feature branch diverged. "
                    "Because there is no divergent history to reconcile, Git simply advances the `main` pointer forward to the tip of the feature branch. "
                    "No new commit is created."
                )
            },
            {
                "heading": "3-Way Merge (Recursive / ORT Strategy)",
                "body": (
                    "When both `main` and `feature` have accumulated new commits since diverging, a simple pointer shift is impossible. "
                    "Git performs a **3-Way Merge** by comparing three snapshots:\n"
                    "1. Common Ancestor (the point where the branches diverged).\n"
                    "2. Tip of receiving branch (`main`).\n"
                    "3. Tip of incoming branch (`feature`).\n"
                    "Git combines these changes into an explicit **Merge Commit**."
                )
            },
            {
                "heading": "Enforcing Merge Policies (`--no-ff` vs `--ff-only`)",
                "body": (
                    "- `git merge --no-ff <branch>`: Forces Git to create a merge commit even if a fast-forward is possible. Preserves the visual group of commits that formed a feature.\n"
                    "- `git merge --ff-only <branch>`: Refuses to merge unless a fast-forward is possible, preventing unexpected merge commits."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Visualizing Fast-Forward Merge",
                "code": "# Before Fast-Forward:\n# A --- B (main)\n#        \\\n#         C --- D (feature)\n#\n# After git merge feature (Fast-Forward):\n# A --- B --- C --- D (main, feature)",
                "explanation": "main pointer simply slides forward to commit D."
            },
            {
                "title": "Visualizing 3-Way Merge with Merge Commit",
                "code": "# Diverged branches:\n# A --- B --- E (main)\n#        \\\n#         C --- D (feature)\n#\n# After 3-Way Merge:\n# A --- B --- E ------- M (main) <-- Merge commit M has parents E and D\n#        \\             /\n#         C --- D ----+",
                "explanation": "Merge commit M reconciles both divergent historical paths."
            },
            {
                "title": "Forcing a Merge Commit with --no-ff",
                "code": "# Force creation of explicit merge commit for feature traceability:\ngit merge --no-ff feature/billing-module -m \"Merge feature 'billing-module'\"",
                "explanation": "Preserves feature boundary in git log graph."
            },
            {
                "title": "Strict Fast-Forward Only Merge",
                "code": "# Fail immediately if a fast-forward is not possible:\ngit merge --ff-only origin/main",
                "explanation": "Guarantees linear history or stops to alert the developer."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execute Merge with --no-ff",
            description="Create branch 'quick-patch', commit a file 'patch.txt', switch to 'main', and merge 'quick-patch' using `--no-ff` to force an explicit merge commit.",
            starter_code="# Create branch, commit file, switch to main, merge --no-ff\n",
            solution_code="git switch -c quick-patch\necho 'patch' > patch.txt\ngit add patch.txt\ngit commit -m 'fix: apply security patch'\ngit switch main\ngit merge --no-ff quick-patch -m 'Merge branch quick-patch'",
            expected_output="Merge made by the 'ort' strategy.\n patch.txt | 1 +\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Under what condition can Git perform a 'Fast-Forward' merge?",
                options=[
                    "When the receiving branch has no new commits since the feature branch diverged from it",
                    "Only when all files are written in JavaScript",
                    "When both branches have hundreds of conflicting commits",
                    "Only when using a high-speed internet connection"
                ],
                correct_answer="When the receiving branch has no new commits since the feature branch diverged from it",
                explanation="Fast-forward happens when the target branch head is directly reachable along the commit history line."
            ),
            QuizQuestionBlueprint(
                question="What are the three snapshots used by Git during a '3-Way Merge'?",
                options=[
                    "The common ancestor commit, the receiving branch tip commit, and the incoming branch tip commit",
                    "Yesterday's commit, today's commit, and tomorrow's commit",
                    "Working directory, Staging area, and Trash folder",
                    "Local branch, Remote branch, and GitHub backup"
                ],
                correct_answer="The common ancestor commit, the receiving branch tip commit, and the incoming branch tip commit",
                explanation="A 3-way merge analyzes the common merge-base ancestor and the two branch endpoints."
            ),
            QuizQuestionBlueprint(
                question="Why do many teams use the `--no-ff` flag when merging feature branches?",
                options=[
                    "It guarantees that an explicit merge commit is created, preserving the historical existence and group of the feature branch",
                    "It speeds up execution by 500%",
                    "It encrypts the merge with SSL",
                    "It bypasses test suite execution"
                ],
                correct_answer="It guarantees that an explicit merge commit is created, preserving the historical existence and group of the feature branch",
                explanation="`--no-ff` maintains feature branch history and context in the git commit graph."
            ),
            QuizQuestionBlueprint(
                question="What does the command `git merge --ff-only <branch>` do if the branches have diverged?",
                options=[
                    "It refuses to merge and aborts with an error, preventing accidental merge commits",
                    "It automatically deletes the other branch",
                    "It performs a 3-way merge anyway",
                    "It forces your computer to reboot"
                ],
                correct_answer="It refuses to merge and aborts with an error, preventing accidental merge commits",
                explanation="`--ff-only` ensures only fast-forward updates occur; if histories diverged, it halts."
            ),
            QuizQuestionBlueprint(
                question="What is the default merge strategy used by modern Git for 3-way merges?",
                options=["ORT (Ostensibly Recursive's Twin)", "Octopus", "Subtree", "SquashOnly"],
                correct_answer="ORT (Ostensibly Recursive's Twin)",
                explanation="Git 2.33+ replaced the older 'recursive' strategy with the significantly faster and safer 'ORT' strategy."
            )
        ]
    )
]
