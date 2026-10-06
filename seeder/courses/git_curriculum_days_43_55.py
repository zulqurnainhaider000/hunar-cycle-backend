"""
Git & Version Control System Curriculum - Days 43 to 55
Module 7: Debugging & Code Search (Days 43-45)
Module 8: Git Internals & Expert Features (Days 46-51)
Module 9: Standards & Automation (Days 52-55)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_43_TO_55 = [
    # ----------------------------------------------------
    # Day 43: Searching code history with git grep
    # ----------------------------------------------------
    DayBlueprint(
        order=43,
        title="Day 43: Searching code history with `git grep`",
        concept="Conducting lightning-fast code searches across tracked files, branches, and historical revisions using `git grep`.",
        analogy="Standard filesystem search is like walking through a warehouse opening every box, including trash bins and moldy basements (`node_modules`). `git grep` is an x-ray scanner that only searches the verified, cataloged inventory in milliseconds.",
        theory_sections=[
            {
                "heading": "Why `git grep` Over Standard grep?",
                "body": (
                    "Standard OS `grep` scans every directory on your disk, frequently choking on massive directories like `node_modules/`, "
                    "`venv/`, or compiled binary caches. `git grep` searches strictly the files tracked in Git's index or object database. "
                    "It is multithreaded, blazing fast, and automatically respects `.gitignore`."
                )
            },
            {
                "heading": "Searching Outside the Working Directory",
                "body": (
                    "The greatest superpower of `git grep` is searching code **in other branches or older historical commits** "
                    "without needing to checkout those branches! You can search a tag from 2 years ago or a feature branch in seconds."
                )
            },
            {
                "heading": "Useful Search Flags",
                "body": (
                    "- `-n`: Print line numbers of matches.\n"
                    "- `-i`: Case-insensitive search.\n"
                    "- `-c`: Print count of matches per file rather than the matching lines.\n"
                    "- `--and`, `--or`: Boolean logic combinations."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Basic Fast Search in Tracked Files",
                "code": "# Search for 'DATABASE_URL' with line numbers in all tracked files:\ngit grep -n \"DATABASE_URL\"\n\n# Output:\n# config/database.js:4:const DATABASE_URL = process.env.DATABASE_URL;\n# src/server.js:12:connect(DATABASE_URL);",
                "explanation": "Skips node_modules and untracked files automatically."
            },
            {
                "title": "Searching in an Older Commit or Branch",
                "code": "# Search for a deprecated function inside an older release tag:\ngit grep \"renderLegacyHeader\" v1.0.0\n\n# Search across all branches simultaneously:\ngit grep \"SECRET_KEY\" $(git rev-parse --branches)",
                "explanation": "Queries git object database without switching branches."
            },
            {
                "title": "Case-Insensitive Count of Occurrences",
                "code": "# Count occurrences of 'todo' per file:\ngit grep -i -c \"TODO\"\n\n# Output:\n# src/auth.js:3\n# src/payment.js:1",
                "explanation": "Generates aggregate count statistics per file."
            },
            {
                "title": "Boolean Combinations in git grep",
                "code": "# Find lines matching both 'export' AND 'stripe':\ngit grep -e \"export\" --and -e \"stripe\"",
                "explanation": "Combines search tokens using logical operators."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Search Tracked Files with Line Numbers",
            description="Run `git grep` with line numbers (`-n`) and case-insensitive matching (`-i`) for the pattern 'CONFIG'.",
            starter_code="# Run git grep for 'CONFIG' with -n and -i\n",
            solution_code="git grep -n -i \"CONFIG\"",
            expected_output="file:line: content"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `git grep` drastically faster and cleaner than standard operating system `grep`?",
                options=[
                    "It searches only tracked Git files and ignores ignored folders like `node_modules/` and build directories automatically",
                    "It uses an AI model to guess results",
                    "It only searches the first 10 files",
                    "It deletes non-matching files"
                ],
                correct_answer="It searches only tracked Git files and ignores ignored folders like `node_modules/` and build directories automatically",
                explanation="`git grep` leverages Git's index and ignores untracked/ignored directory bloat."
            ),
            QuizQuestionBlueprint(
                question="How can you search for a text string inside an older release tag `v2.0.0` without checking it out?",
                options=["git grep \"string\" v2.0.0", "git find \"string\" in v2.0.0", "git search --tag v2.0.0 \"string\"", "git checkout v2.0.0 && grep"],
                correct_answer="git grep \"string\" v2.0.0",
                explanation="Passing a treeish reference like `v2.0.0` directs `git grep` to inspect that historical tree."
            ),
            QuizQuestionBlueprint(
                question="Which flag passed to `git grep` prints the line number for every matched line?",
                options=["-n", "-l", "-c", "-p"],
                correct_answer="-n",
                explanation="`-n` prefixes matching lines with their 1-indexed line numbers."
            ),
            QuizQuestionBlueprint(
                question="What does `git grep -c \"pattern\"` output?",
                options=[
                    "The count of matching occurrences in each file",
                    "The commit date of matches",
                    "The author of each match",
                    "The color of matching text"
                ],
                correct_answer="The count of matching occurrences in each file",
                explanation="`-c` displays the aggregate count of matching lines per file."
            ),
            QuizQuestionBlueprint(
                question="Which flag makes `git grep` ignore letter casing during its search?",
                options=["-i (or --ignore-case)", "-u", "-s", "--exact"],
                correct_answer="-i (or --ignore-case)",
                explanation="`-i` enables case-insensitive matching."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 44: Automated bug finding with git bisect
    # ----------------------------------------------------
    DayBlueprint(
        order=44,
        title="Day 44: Automated bug finding with `git bisect`",
        concept="Finding the exact commit that introduced a regression using binary search algorithms via `git bisect` and automated test scripts.",
        analogy="Your application worked perfectly 500 commits ago, but is broken today. Instead of testing all 500 commits one by one like a turtle, `git bisect` cuts the problem in half: test commit 250 (good or bad?), then test 125, then 62. In just 9 tests ($O(\\log n)$), you pinpoint the exact guilty commit.",
        theory_sections=[
            {
                "heading": "The Power of Binary Search in Git",
                "body": (
                    "When a bug appears and nobody knows which commit caused it, testing history sequentially is exhausting. "
                    "`git bisect` uses a binary search algorithm through your commit history. "
                    "Even across 1,000 commits, binary search pinpoints the exact culprit in approximately 10 steps ($2^{10} = 1024$)."
                )
            },
            {
                "heading": "The Manual Bisect Workflow",
                "body": (
                    "1. Start bisect: `git bisect start`\n"
                    "2. Mark current broken commit: `git bisect bad`\n"
                    "3. Mark a known good historical commit: `git bisect good <hash>`\n"
                    "4. Git automatically checks out the midpoint commit. You test the code.\n"
                    "5. Type `git bisect good` or `git bisect bad`. Repeat until Git identifies the first bad commit!\n"
                    "6. Reset workspace: `git bisect reset`."
                )
            },
            {
                "heading": "Fully Automated Bisect (`git bisect run`)",
                "body": (
                    "You don't even have to test manually! If you write a quick test script (e.g. `npm test` or `pytest`), "
                    "running `git bisect run ./test.sh` executes the binary search completely autonomously in seconds."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Starting a Manual Bisect Session",
                "code": "# 1. Start bisect mode:\ngit bisect start\n\n# 2. Tell Git the current HEAD is broken:\ngit bisect bad\n\n# 3. Tell Git version v1.2.0 was known to be working:\ngit bisect good v1.2.0\n\n# Output:\n# Bisecting: 128 revisions left to test after this (roughly 7 steps)\n# [4b2c1d0f...] fix: update redis pool size",
                "explanation": "Git automatically checks out the halfway commit."
            },
            {
                "title": "Marking Commits Good or Bad",
                "code": "# Run your app or tests, then inform Git:\n# If it works:\ngit bisect good\n\n# If the bug is present:\ngit bisect bad\n\n# When complete, Git announces the culprit:\n# 7a4e8c1d5f is the first bad commit",
                "explanation": "Repeatedly narrows search space by 50% per step."
            },
            {
                "title": "Fully Automated Bisect with Test Script",
                "code": "# Automated bisect using an executable exit code (0 = good, non-zero = bad):\ngit bisect start HEAD v1.0.0\ngit bisect run npm test\n\n# Git runs through all test steps automatically without human intervention!",
                "explanation": "Autonomous regression hunting via exit codes."
            },
            {
                "title": "Cleaning Up and Ending Bisect Session",
                "code": "# Return HEAD back to your original branch:\ngit bisect reset",
                "explanation": "Restores original workspace state."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Start Bisect and Mark Boundaries",
            description="Write the sequence of commands to start `git bisect`, mark HEAD as `bad`, and mark commit 'a1b2c3d' as `good`.",
            starter_code="# Start bisect, mark HEAD bad, mark a1b2c3d good\n",
            solution_code="git bisect start\ngit bisect bad\ngit bisect good a1b2c3d",
            expected_output="Bisecting: ... revisions left to test..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What mathematical algorithmic technique does `git bisect` use to locate a bug in commit history?",
                options=["Binary Search ($O(\\log n)$)", "Linear Scan ($O(n)$)", "Bubble Sort", "Monte Carlo Simulation"],
                correct_answer="Binary Search ($O(\\log n)$)",
                explanation="`git bisect` divides the commit candidate pool in half at every step."
            ),
            QuizQuestionBlueprint(
                question="Roughly how many test steps are required for `git bisect` to pinpoint a bug across a history of 1,024 commits?",
                options=["Approximately 10 steps", "512 steps", "1,024 steps", "Exactly 2 steps"],
                correct_answer="Approximately 10 steps",
                explanation="Because $2^{10} = 1024$, binary search resolves 1,024 commits in ~10 evaluations."
            ),
            QuizQuestionBlueprint(
                question="How can you make `git bisect` run completely automatically without manual testing?",
                options=[
                    "Use `git bisect run <test-script>` where the script exits 0 for success and non-zero for failure",
                    "Pay for GitHub Enterprise",
                    "Add an AI flag `--ai`",
                    "Git bisect cannot be automated"
                ],
                correct_answer="Use `git bisect run <test-script>` where the script exits 0 for success and non-zero for failure",
                explanation="`git bisect run` checks script exit codes to automate bisect iterations."
            ),
            QuizQuestionBlueprint(
                question="What command must you run when finished with a bisect session to return to your original checked-out branch?",
                options=["git bisect reset", "git bisect stop", "git bisect end", "git switch -"],
                correct_answer="git bisect reset",
                explanation="`git bisect reset` cleans bisect references and restores HEAD."
            ),
            QuizQuestionBlueprint(
                question="What does `git bisect skip` do when you encounter a commit that cannot be tested (e.g. broken build due to unrelated bug)?",
                options=[
                    "Tells Git to pick a nearby commit to test instead of the current one",
                    "Aborts the entire bisect",
                    "Deletes the commit",
                    "Marks the commit as good"
                ],
                correct_answer="Tells Git to pick a nearby commit to test instead of the current one",
                explanation="`skip` bypasses untestable intermediate commits."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 45: Viewing exact differences (git diff variants)
    # ----------------------------------------------------
    DayBlueprint(
        order=45,
        title="Day 45: Viewing exact differences (`git diff` variants)",
        concept="Mastering diff variations: unstaged changes, staged changes (`--staged`), comparing branches (`..` vs `...`), word diffs, and statistical diff summaries.",
        analogy="`git diff` is like looking at two versions of a contract with red pen and green highlighter. Plain `git diff` shows what you scribbled in pencil on your desk; `git diff --staged` shows what you've photocopied into the final envelope ready to mail.",
        theory_sections=[
            {
                "heading": "The Anatomy of Git Diff",
                "body": (
                    "`git diff` calculates and displays unified diffs showing line additions (`+`) and deletions (`-`). "
                    "Mastering its targeting parameters is essential for verifying code before committing."
                )
            },
            {
                "heading": "The Three Fundamental Diff Scopes",
                "body": (
                    "1. `git diff`: Differences between **Working Directory** and **Staging Area (Index)** (unstaged edits).\n"
                    "2. `git diff --staged` (or `--cached`): Differences between **Staging Area** and **Last Commit (HEAD)** (what will be committed).\n"
                    "3. `git diff HEAD`: Differences between **Working Directory** and **Last Commit** (all modifications)."
                )
            },
            {
                "heading": "Comparing Branches: Double-Dot vs Triple-Dot",
                "body": (
                    "- `git diff branchA..branchB`: Direct difference between the tips of both branches.\n"
                    "- `git diff branchA...branchB` (Triple-Dot): Compares the tip of `branchB` with the **common ancestor** of both branches. "
                    "This is the **exact diff that GitHub displays on a Pull Request!**"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Unstaged vs Staged Diffs",
                "code": "# View what is modified on disk but NOT yet staged:\ngit diff\n\n# View what IS staged and about to be committed:\ngit diff --staged",
                "explanation": "Differentiates unstaged edits from staged snapshots."
            },
            {
                "title": "Pull Request Diff View (Triple-Dot)",
                "code": "# Compare feature branch changes relative to common ancestor with main (PR view):\ngit diff main...feature/billing",
                "explanation": "Displays only the changes introduced on the feature branch."
            },
            {
                "title": "Word-by-Word Diffing (--word-diff)",
                "code": "# Highlight individual modified words inside lines rather than entire lines:\ngit diff --word-diff\n\n# Output: The timeout is [-30-]{+60+} seconds.",
                "explanation": "Ideal for reviewing prose, documentation, and single-variable changes."
            },
            {
                "title": "Statistical Diff Summary (--stat)",
                "code": "# Display compact summary of files changed and insertion/deletion counts:\ngit diff --stat HEAD~3 HEAD\n\n# Output:\n#  src/auth.js | 15 +++++++++++---\n#  1 file changed, 11 insertions(+), 4 deletions(-)",
                "explanation": "High-level numeric change metrics."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Staged Differences with Stats",
            description="Run `git diff` for staged files only with statistical summary enabled (`--staged --stat`).",
            starter_code="# Run git diff for staged files with stat flag\n",
            solution_code="git diff --staged --stat",
            expected_output="... files changed, ... insertions(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does `git diff --staged` (or `git diff --cached`) display?",
                options=[
                    "The differences between the files currently in the Staging Area and the last commit (HEAD)",
                    "The differences between your local repo and the remote GitHub server",
                    "Deleted files only",
                    "Unstaged modifications in your working tree"
                ],
                correct_answer="The differences between the files currently in the Staging Area and the last commit (HEAD)",
                explanation="`--staged` shows precisely what will go into the next commit snapshot."
            ),
            QuizQuestionBlueprint(
                question="What is the significance of the triple-dot syntax in `git diff main...feature`?",
                options=[
                    "It compares the tip of `feature` to the common ancestor where it diverged from `main` (the exact view used by GitHub PRs)",
                    "It merges the branches three times",
                    "It compares three branches simultaneously",
                    "It runs three tests"
                ],
                correct_answer="It compares the tip of `feature` to the common ancestor where it diverged from `main` (the exact view used by GitHub PRs)",
                explanation="Triple-dot diff isolates changes introduced exclusively on the feature branch."
            ),
            QuizQuestionBlueprint(
                question="Which flag highlights changed words in-line using brackets (e.g. `[-old-]{+new+}`) instead of showing full lines?",
                options=["--word-diff", "--inline-diff", "--char-diff", "--compact"],
                correct_answer="--word-diff",
                explanation="`--word-diff` provides inline word-level diffing."
            ),
            QuizQuestionBlueprint(
                question="What does running plain `git diff` with no flags show?",
                options=[
                    "Changes in your working directory that have NOT yet been staged into the index",
                    "Changes that have already been pushed to GitHub",
                    "Every commit made in the past year",
                    "The list of repository branches"
                ],
                correct_answer="Changes in your working directory that have NOT yet been staged into the index",
                explanation="Plain `git diff` compares the working tree to the staging area."
            ),
            QuizQuestionBlueprint(
                question="Which flag displays a compact summary showing file names, modified line counts, and histogram bars?",
                options=["--stat", "--summary", "--count", "-s"],
                correct_answer="--stat",
                explanation="`--stat` outputs the diffstat summary table."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 46: How Git stores data (Objects, Blobs, Trees, SHA-1)
    # ----------------------------------------------------
    DayBlueprint(
        order=46,
        title="Day 46: How Git stores data (Objects, Blobs, Trees, SHA-1)",
        concept="Peeking under the hood of Git's content-addressable database: Blobs (file contents), Trees (directories), Commits (metadata), and SHA-1/SHA-256 cryptographic hashing.",
        analogy="Git is not really a version control system—it is a content-addressable key-value database with a version control UI built on top! Every piece of data is assigned a unique cryptographic fingerprint (SHA hash). If two identical files exist anywhere in the project, Git only stores one copy.",
        theory_sections=[
            {
                "heading": "Content-Addressable Storage",
                "body": (
                    "Git stores all information inside `.git/objects/`. "
                    "The key is a 40-character SHA-1 (or 64-char SHA-256) hash computed from the object's header and payload. "
                    "The first 2 characters become a subdirectory name (e.g. `.git/objects/7a/`), and the remaining 38 characters form the file name."
                )
            },
            {
                "heading": "The 4 Fundamental Object Types",
                "body": (
                    "1. **Blob (Binary Large Object)**: Stores raw file contents only. Does NOT store filename, permissions, or timestamps!\n"
                    "2. **Tree**: Represents a directory. Stores directory mappings: file modes, type (blob/tree), SHA hashes, and file/folder names.\n"
                    "3. **Commit**: Points to a top-level Tree object, parent commit SHA(s), author metadata, committer metadata, and the commit message.\n"
                    "4. **Annotated Tag**: An object containing tagger metadata, a message, and a pointer to a commit."
                )
            },
            {
                "heading": "Plumbing vs Porcelain Commands",
                "body": (
                    "High-level user-facing commands (`commit`, `checkout`, `branch`) are called **Porcelain**. "
                    "Low-level internal inspection commands (`cat-file`, `hash-object`, `ls-tree`) are called **Plumbing**."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Hashing Raw Data with git hash-object",
                "code": "# Calculate SHA-1 hash of string content and store it in database (-w):\necho \"Hello Git Internals\" | git hash-object -w --stdin\n\n# Output:\n# 806659f8a84ffcf47a27a052ff23970b8fbe15cb\n# Stored inside .git/objects/80/6659f8a84ffcf47a27a052ff23970b8fbe15cb",
                "explanation": "Demonstrates direct key-value object generation."
            },
            {
                "title": "Inspecting Object Type and Content with git cat-file",
                "code": "# Check the type of an object hash (-t):\ngit cat-file -t 806659f\n# Output: blob\n\n# Pretty-print the content of the object (-p):\ngit cat-file -p 806659f\n# Output: Hello Git Internals",
                "explanation": "Plumbing command to decompress and inspect any Git object."
            },
            {
                "title": "Inspecting a Directory Tree Object",
                "code": "# Inspect the tree object pointed to by HEAD:\ngit cat-file -p HEAD^{tree}\n\n# Output lists directory entries:\n# 100644 blob e69de29...    README.md\n# 040000 tree a1b2c3d...    src",
                "explanation": "Trees map filenames and permissions to underlying blobs and sub-trees."
            },
            {
                "title": "Inspecting Raw Commit Object Metadata",
                "code": "# View raw commit object bytes:\ngit cat-file -p HEAD\n\n# Output:\n# tree d8329fc...\n# parent 7a4e8c1...\n# author Alice Dev <alice@dev.io> 1695000000 -0400\n# committer Alice Dev <alice@dev.io> 1695000000 -0400\n# \n# feat: implement core engine",
                "explanation": "Exposes the internal raw structure of a commit object."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Object Type and Content",
            description="Use `git cat-file -t HEAD` to display the object type of HEAD, and `git cat-file -p HEAD` to display its raw contents.",
            starter_code="# Inspect HEAD object type and pretty-print content\n",
            solution_code="git cat-file -t HEAD\ngit cat-file -p HEAD",
            expected_output="commit\ntree ...\nauthor ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which Git object type stores raw file contents but does NOT store the filename or file permissions?",
                options=["Blob", "Tree", "Commit", "Tag"],
                correct_answer="Blob",
                explanation="Blobs store only raw bytes; filenames and modes are stored in Tree objects."
            ),
            QuizQuestionBlueprint(
                question="Which Git object represents a directory and maps filenames and permissions to blob and subtree hashes?",
                options=["Tree", "Blob", "Commit", "Branch"],
                correct_answer="Tree",
                explanation="Tree objects correspond to filesystem directories."
            ),
            QuizQuestionBlueprint(
                question="Which low-level plumbing command allows you to inspect the type (`-t`) and pretty-print the content (`-p`) of any object hash?",
                options=["git cat-file", "git inspect", "git read-object", "git dump"],
                correct_answer="git cat-file",
                explanation="`git cat-file` is the primary plumbing tool for inspecting database objects."
            ),
            QuizQuestionBlueprint(
                question="Why is Git described as a 'content-addressable' storage system?",
                options=[
                    "Because keys are cryptographic hashes computed directly from the object's content; identical content always produces the identical key",
                    "Because it requires an email address to commit",
                    "Because files are sorted by home address",
                    "Because it uses IP addresses"
                ],
                correct_answer="Because keys are cryptographic hashes computed directly from the object's content; identical content always produces the identical key",
                explanation="Object keys are cryptographic digests of their payload."
            ),
            QuizQuestionBlueprint(
                question="What are low-level internal Git commands called, as opposed to high-level user commands like `commit` and `checkout`?",
                options=["Plumbing commands (vs Porcelain)", "Kernel commands", "System calls", "Bytecode"],
                correct_answer="Plumbing commands (vs Porcelain)",
                explanation="Linus Torvalds coined 'Porcelain' for user tools and 'Plumbing' for engine internals."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 47: Git Submodules
    # ----------------------------------------------------
    DayBlueprint(
        order=47,
        title="Day 47: Git Submodules",
        concept="Embedding and managing nested Git repositories inside a parent repository while pinning external dependencies to exact commit SHAs.",
        analogy="Think of building a car. You don't build the car battery from scratch inside the car blueprint; you source the battery from a specialized battery company repository (`submodule`). You specify the exact model serial number (commit SHA) of the battery you installed in your car.",
        theory_sections=[
            {
                "heading": "What is a Git Submodule?",
                "body": (
                    "A Git submodule allows you to keep a Git repository as a subdirectory of another Git repository. "
                    "This is ideal for shared libraries, microservice shared types, or vendor dependencies developed independently."
                )
            },
            {
                "heading": "The `.gitmodules` Configuration File",
                "body": (
                    "When you add a submodule, Git creates a `.gitmodules` file in the project root tracking the path and remote URL:\n"
                    "```ini\n"
                    "[submodule \"libs/auth\"]\n"
                    "    path = libs/auth\n"
                    "    url = https://github.com/org/auth-lib.git\n"
                    "```"
                )
            },
            {
                "heading": "Submodules Pin Exact Commits, Not Branches",
                "body": (
                    "A critical rule: **A parent repository does not track a branch of the submodule; it tracks a specific commit SHA.** "
                    "When cloning a repository with submodules, submodules are empty directories until you run `git submodule update --init --recursive`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Adding a Submodule to a Project",
                "code": "# Add external repository into the 'libs/math' folder:\ngit submodule add https://github.com/org/math-lib.git libs/math\n\n# Stage .gitmodules and the submodule reference commit:\ngit commit -m \"chore: add math-lib as submodule\"",
                "explanation": "Creates .gitmodules file and tracks directory as a gitlink."
            },
            {
                "title": "Cloning a Repo with Submodules",
                "code": "# Option A: Clone and initialize all nested submodules in one step:\ngit clone --recurse-submodules https://github.com/org/parent-app.git\n\n# Option B: If already cloned without submodules:\ngit submodule update --init --recursive",
                "explanation": "Initializes and checks out nested submodules."
            },
            {
                "title": "Updating Submodule to Latest Upstream Commit",
                "code": "# Fetch and update submodule to latest remote branch commit:\ngit submodule update --remote libs/math\n\n# Stage the updated commit pointer in the parent repository:\ngit add libs/math\ngit commit -m \"chore: update math-lib to latest release\"",
                "explanation": "Parent repo explicitly commits the updated submodule SHA pointer."
            },
            {
                "title": "Removing a Submodule Cleanly",
                "code": "# De-initialize and remove submodule:\ngit submodule deinit -f libs/math\ngit rm -f libs/math\nrm -rf .git/modules/libs/math",
                "explanation": "Cleans config, index, and .git/modules store."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Initialize Submodules in Existing Repo",
            description="Write the command to initialize and update all submodules recursively in an already-cloned repository.",
            starter_code="# Initialize and update submodules recursively\n",
            solution_code="git submodule update --init --recursive",
            expected_output="Submodule ... registered for path ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does a parent Git repository track regarding a submodule inside it?",
                options=[
                    "The exact commit SHA-1 hash of the submodule repository",
                    "A moving branch name that updates on every commit",
                    "A copy of all files inside its own commit tree",
                    "A URL link only with no version control"
                ],
                correct_answer="The exact commit SHA-1 hash of the submodule repository",
                explanation="The parent repo stores a 'gitlink' (mode 160000) pointing to an exact commit SHA."
            ),
            QuizQuestionBlueprint(
                question="Which file in the repository root maps submodule paths to their remote repository URLs?",
                options=[".gitmodules", ".submodules", ".gitconfig", ".gitattributes"],
                correct_answer=".gitmodules",
                explanation="`.gitmodules` is a version-controlled text file tracking submodule paths and URLs."
            ),
            QuizQuestionBlueprint(
                question="When you clone a repository that contains submodules, what are the submodule directories by default before running `update`?",
                options=[
                    "Empty directories",
                    "Zip archives",
                    "Fully downloaded directories",
                    "Symbolic links"
                ],
                correct_answer="Empty directories",
                explanation="Standard clone skips submodule contents unless `--recurse-submodules` is passed."
            ),
            QuizQuestionBlueprint(
                question="Which flag passed to `git clone` automatically downloads and initializes all nested submodules during the initial clone?",
                options=["--recurse-submodules", "--all-submodules", "--include-modules", "--deep"],
                correct_answer="--recurse-submodules",
                explanation="`--recurse-submodules` instructs Git to initialize all submodules upon clone."
            ),
            QuizQuestionBlueprint(
                question="What command fetches and advances a submodule to the latest commit on its remote branch?",
                options=["git submodule update --remote", "git submodule push", "git submodule pull-all", "git update --sub"],
                correct_answer="git submodule update --remote",
                explanation="`--remote` queries the remote repository instead of keeping the pinned commit."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 48: Git Worktrees
    # ----------------------------------------------------
    DayBlueprint(
        order=48,
        title="Day 48: Git Worktrees",
        concept="Checking out and developing multiple branches simultaneously in separate filesystem directories without re-cloning using `git worktree`.",
        analogy="Normally, working in Git is having one desk: to look at another blueprint, you have to pack up everything on your desk and unfold the other blueprint. A Git Worktree is buying a second desk right next to your first desk so you can work on both blueprints at the same time without packing anything up.",
        theory_sections=[
            {
                "heading": "The Limitation of a Single Working Tree",
                "body": (
                    "Normally, a Git repository has exactly one working directory. If you are running a 30-minute test suite on `feature-A`, "
                    "you cannot switch to `hotfix-B` without killing your running test suite or stashing dirty files. "
                    "Historically, developers cloned the entire repository a second time, wasting gigabytes of disk space."
                )
            },
            {
                "heading": "The Solution: `git worktree`",
                "body": (
                    "Git allows attaching multiple linked working directories to a single `.git` repository! "
                    "Each worktree checks out a different branch into its own folder on your disk. "
                    "They share the exact same `.git` object database, hooks, and configuration, consuming zero extra storage for repository history."
                )
            },
            {
                "heading": "Worktree Rules",
                "body": (
                    "- Two worktrees **cannot** check out the same branch at the same time (prevents index corruption).\n"
                    "- When finished, remove the worktree with `git worktree remove`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Adding a Worktree for Hotfix Development",
                "code": "# Create a new folder '../hotfix-app' checking out branch 'hotfix-bug':\ngit worktree add ../hotfix-app -b hotfix-bug\n\n# Output confirms separate working directory attached to same repo:\n# Preparing worktree (new branch 'hotfix-bug')\n# HEAD is now at 7a4e8c1 fix: base setup",
                "explanation": "Spawns new folder checked out to distinct branch."
            },
            {
                "title": "Listing All Active Worktrees",
                "code": "# List all attached working trees and their active branches:\ngit worktree list\n\n# Output:\n# /Users/dev/my-app         7a4e8c1 [main]\n# /Users/dev/hotfix-app     7a4e8c1 [hotfix-bug]",
                "explanation": "Displays all linked filesystem trees."
            },
            {
                "title": "Working in Parallel",
                "code": "# Work in your hotfix tree, commit, and push:\ncd ../hotfix-app\necho 'hotfix' > bug.txt\ngit commit -am \"fix: urgent production issue\"\ngit push origin hotfix-bug",
                "explanation": "Independent working directory operating on shared database."
            },
            {
                "title": "Removing Worktree After Completion",
                "code": "# Delete the worktree directory and unregister it:\ncd /Users/dev/my-app\ngit worktree remove ../hotfix-app\n\n# Prune stale worktree references:\ngit worktree prune",
                "explanation": "Cleans up temporary directory cleanly."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="List and Prune Worktrees",
            description="Run `git worktree list` to inspect active worktrees and `git worktree prune` to clean stale references.",
            starter_code="# List worktrees and prune stale references\n",
            solution_code="git worktree list\ngit worktree prune",
            expected_output="... [main]\n..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary operational advantage of `git worktree` over cloning a repository multiple times?",
                options=[
                    "It allows working on multiple branches simultaneously in separate folders while sharing the exact same local `.git` object database and history",
                    "It doubles CPU performance",
                    "It creates branches without names",
                    "It bypasses merge conflicts"
                ],
                correct_answer="It allows working on multiple branches simultaneously in separate folders while sharing the exact same local `.git` object database and history",
                explanation="Worktrees share the `.git` storage engine without duplicating repository history."
            ),
            QuizQuestionBlueprint(
                question="Can two different worktrees have the exact same branch checked out at the same time?",
                options=[
                    "No, Git explicitly forbids checking out the same branch in multiple worktrees to prevent index and HEAD corruption",
                    "Yes, with no limitations",
                    "Only if using Linux",
                    "Only if you force push"
                ],
                correct_answer="No, Git explicitly forbids checking out the same branch in multiple worktrees to prevent index and HEAD corruption",
                explanation="Git enforces a 1-to-1 mapping between active branches and worktrees."
            ),
            QuizQuestionBlueprint(
                question="Which command displays all active worktree paths and their assigned branches?",
                options=["git worktree list", "git worktree show", "git worktree --all", "git worktree status"],
                correct_answer="git worktree list",
                explanation="`git worktree list` shows all active filesystem directories linked to the repository."
            ),
            QuizQuestionBlueprint(
                question="How do you safely remove and unregister a worktree folder `../temp-fix` when you are done?",
                options=["git worktree remove ../temp-fix", "rmdir ../temp-fix", "git delete worktree ../temp-fix", "git drop ../temp-fix"],
                correct_answer="git worktree remove ../temp-fix",
                explanation="`git worktree remove` deletes the directory and cleans the internal worktree registry."
            ),
            QuizQuestionBlueprint(
                question="Where does Git store the internal metadata for additional worktrees?",
                options=["Inside `.git/worktrees/`", "In `/tmp/`", "In `node_modules/`", "On GitHub servers"],
                correct_answer="Inside `.git/worktrees/`",
                explanation="Metadata and dedicated HEAD/Index references are saved in `.git/worktrees/<name>/`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 49: Git Hooks (Pre-commit, Pre-push, Husky)
    # ----------------------------------------------------
    DayBlueprint(
        order=49,
        title="Day 49: Git Hooks (Pre-commit, Pre-push, Husky)",
        concept="Automating client-side quality gates using Git lifecycle hooks (pre-commit, commit-msg, pre-push) and configuring team-wide hooks with Husky.",
        analogy="A Git hook is like a bouncer at a nightclub door. Before you are allowed to make a commit or push (`the nightclub`), the bouncer checks your shoes and ID (`runs linter and unit tests`). If your tests fail, the bouncer denies entry.",
        theory_sections=[
            {
                "heading": "What are Git Hooks?",
                "body": (
                    "Git hooks are custom shell scripts triggered at key points in Git's execution lifecycle. "
                    "They reside inside `.git/hooks/`. If a hook script exits with a non-zero code (`exit 1`), "
                    "Git halts and aborts the operation."
                )
            },
            {
                "heading": "Essential Client-Side Hook Types",
                "body": (
                    "1. `pre-commit`: Runs before the commit message is created. Used for running linters, code formatters, and secrets scanners (e.g. detect leaked AWS keys).\n"
                    "2. `commit-msg`: Runs after the message is entered. Used to validate commit message format (e.g. enforcing Conventional Commits).\n"
                    "3. `pre-push`: Runs before pushing to remote. Used to run full test suites to prevent breaking CI."
                )
            },
            {
                "heading": "Sharing Hooks Across Teams (Husky / core.hooksPath)",
                "body": (
                    "Files inside `.git/hooks/` are **not committed to version control** by default. "
                    "To share hooks across teams, modern projects configure `core.hooksPath` to point to a committed folder "
                    "(e.g. `.husky/` or `.githooks/`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Simple pre-commit Hook",
                "code": "# Inside .git/hooks/pre-commit:\n#!/bin/sh\necho \"Running pre-commit linter checks...\"\n\n# Run linter:\nnpm run lint\nif [ $? -ne 0 ]; then\n    echo \"❌ Lint errors found! Commit rejected.\"\n    exit 1\nfi\necho \"✅ Lint passed!\"",
                "explanation": "Bash script that halts commit if linter exits with error."
            },
            {
                "title": "Making Hook Executable",
                "code": "# On Unix/macOS/Linux, hooks must have executable permissions:\nchmod +x .git/hooks/pre-commit",
                "explanation": "Hooks without executable bit will be ignored by Git."
            },
            {
                "title": "Configuring Committed Hooks Directory",
                "code": "# Point Git to use version-controlled .githooks directory for all contributors:\ngit config core.hooksPath .githooks",
                "explanation": "Shares hooks with team via version control."
            },
            {
                "title": "Bypassing Hooks in Emergencies (--no-verify)",
                "code": "# Skip client-side hooks when making an urgent emergency commit or push:\ngit commit -m \"hotfix: critical fix\" --no-verify\ngit push origin main --no-verify",
                "explanation": "`--no-verify` skips pre-commit and commit-msg hooks."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Custom Hooks Path",
            description="Configure git locally to use directory '.githooks' as the active hooks path via `core.hooksPath`.",
            starter_code="# Set local core.hooksPath to .githooks\n",
            solution_code="git config core.hooksPath .githooks",
            expected_output="core.hooksPath configured to .githooks"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if a `pre-commit` hook script exits with a non-zero exit code (`exit 1`)?",
                options=[
                    "Git aborts the commit immediately, and no commit is created",
                    "Git creates the commit anyway with a warning",
                    "Git deletes the repository",
                    "Git forces you to enter a password"
                ],
                correct_answer="Git aborts the commit immediately, and no commit is created",
                explanation="Non-zero exit codes signal failure and halt Git operations."
            ),
            QuizQuestionBlueprint(
                question="Why are files placed directly inside `.git/hooks/` not automatically shared with teammates who clone the repo?",
                options=[
                    "The `.git/` directory is local to each machine and is never transferred over the network during clone, push, or pull",
                    "Hooks are encrypted for security",
                    "Git hooks only run on Linux",
                    "GitHub deletes hooks on upload"
                ],
                correct_answer="The `.git/` directory is local to each machine and is never transferred over the network during clone, push, or pull",
                explanation="The `.git` folder is excluded from versioning for security and portability."
            ),
            QuizQuestionBlueprint(
                question="Which flag allows a developer to bypass client-side pre-commit hooks during an urgent emergency commit?",
                options=["--no-verify (or -n)", "--skip-checks", "--force-commit", "--ignore-hooks"],
                correct_answer="--no-verify (or -n)",
                explanation="`--no-verify` skips pre-commit and commit-msg hooks."
            ),
            QuizQuestionBlueprint(
                question="Which Git hook is executed specifically to validate the structure of the commit message text?",
                options=["commit-msg", "pre-commit", "post-commit", "pre-push"],
                correct_answer="commit-msg",
                explanation="`commit-msg` receives the path to the message file and can enforce standards."
            ),
            QuizQuestionBlueprint(
                question="What Git configuration setting directs Git to look for hooks in a version-controlled directory like `.husky/`?",
                options=["core.hooksPath", "git.hooksDir", "hooks.location", "system.hooksPath"],
                correct_answer="core.hooksPath",
                explanation="`core.hooksPath` overrides the default `.git/hooks` path."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 50: Handling Large Files with Git LFS
    # ----------------------------------------------------
    DayBlueprint(
        order=50,
        title="Day 50: Handling Large Files with Git LFS",
        concept="Solving repository bloat from video assets, ML models, and binary datasets using Git Large File Storage (LFS) text pointer replacement.",
        analogy="Standard Git is like a backpack: if you try to put a 500-pound grand piano (`a 5GB machine learning model`) into your backpack, the backpack rips open and everyone carrying it falls over. Git LFS leaves the heavy piano in a warehouse and only puts a lightweight luggage claim receipt ticket into your backpack.",
        theory_sections=[
            {
                "heading": "The Problem with Large Binaries in Git",
                "body": (
                    "Git was architected for plain text source code. If you commit a 100MB video and edit it 10 times, "
                    "Git stores all 10 full 100MB versions in `.git/objects/`, bloating the repository by 1GB. "
                    "Every coworker who clones the project is forced to download that entire bloated history."
                )
            },
            {
                "heading": "How Git LFS Works",
                "body": (
                    "Git Large File Storage (LFS) replaces large files inside your Git repository with tiny **text pointer files** (~130 bytes). "
                    "The actual heavy binary files are uploaded to dedicated LFS cloud storage. "
                    "When you checkout a branch, Git LFS downloads only the specific binary versions required for your active snapshot."
                )
            },
            {
                "heading": "The `.gitattributes` File",
                "body": (
                    "Git LFS uses `.gitattributes` to define which file extensions should be intercepted and managed by LFS:\n"
                    "`*.psd filter=lfs diff=lfs merge=lfs -text`"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Installing and Initializing Git LFS",
                "code": "# Install Git LFS hooks on your machine once:\ngit lfs install\n\n# Output:\n# Git LFS initialized.",
                "explanation": "Installs smudge and clean filters in global git config."
            },
            {
                "title": "Tracking Large File Extensions",
                "code": "# Track all 3D assets, zip files, and ML model weights:\ngit lfs track \"*.mp4\"\ngit lfs track \"*.zip\"\ngit lfs track \"*.onnx\"\n\n# Always commit the generated .gitattributes file:\ngit add .gitattributes\ngit commit -m \"chore: configure git lfs tracking\"",
                "explanation": "Registers file patterns in .gitattributes."
            },
            {
                "title": "Anatomy of an LFS Pointer File",
                "code": "# What Git actually commits to repository history (tiny ~130 byte text pointer):\n# version https://git-lfs.github.com/spec/v1\n# oid sha256:4d7a8c1d5f2a1b9e3f4a5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f\n# size 104857600",
                "explanation": "Points to remote storage using SHA-256 and byte size."
            },
            {
                "title": "Listing and Pulling LFS Assets",
                "code": "# List all LFS files in current commit:\ngit lfs ls-files\n\n# Download LFS binaries for current branch:\ngit lfs pull",
                "explanation": "Inspects and synchronizes LFS binary objects."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Track Binary Extension with Git LFS",
            description="Use `git lfs track` to track all '*.tar.gz' files and verify that `.gitattributes` is updated.",
            starter_code="# Track *.tar.gz with git lfs\n",
            solution_code="git lfs track \"*.tar.gz\"",
            expected_output="Tracking \"*.tar.gz\""
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How does Git LFS (Large File Storage) prevent repository bloat when managing large binary files?",
                options=[
                    "It replaces large files in the Git repository with tiny ~130-byte text pointer files and stores the heavy binaries on a remote LFS server",
                    "It deletes all images older than 7 days",
                    "It compresses images into text characters",
                    "It limits files to 10 lines of code"
                ],
                correct_answer="It replaces large files in the Git repository with tiny ~130-byte text pointer files and stores the heavy binaries on a remote LFS server",
                explanation="Pointers keep the git graph tiny while binaries download on-demand."
            ),
            QuizQuestionBlueprint(
                question="Which version-controlled file records which file extensions are managed by Git LFS?",
                options=[".gitattributes", ".gitignore", ".gitmodules", ".gitlfs"],
                correct_answer=".gitattributes",
                explanation="`.gitattributes` configures filters, diff drivers, and merge handlers for LFS."
            ),
            QuizQuestionBlueprint(
                question="What happens if you commit a 2GB file WITHOUT Git LFS enabled in standard Git?",
                options=[
                    "The 2GB file is permanently embedded into Git's object database, forcing every future clone to download it forever",
                    "Git rejects the file automatically",
                    "Git uploads the file to YouTube",
                    "The file is converted into Python"
                ],
                correct_answer="The 2GB file is permanently embedded into Git's object database, forcing every future clone to download it forever",
                explanation="Git packs raw binary history forever unless rewritten or LFS is used."
            ),
            QuizQuestionBlueprint(
                question="Which one-time command sets up Git LFS on a developer's computer system?",
                options=["git lfs install", "git lfs setup", "git lfs enable", "git lfs start"],
                correct_answer="git lfs install",
                explanation="`git lfs install` initializes required system filters."
            ),
            QuizQuestionBlueprint(
                question="Which command downloads the actual binary assets for the current checked-out branch if they were skipped during clone?",
                options=["git lfs pull", "git lfs download", "git lfs sync", "git lfs fetch-all"],
                correct_answer="git lfs pull",
                explanation="`git lfs pull` fetches and checks out the binary files for the current commit."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 51: Git Aliases (Command shortcuts)
    # ----------------------------------------------------
    DayBlueprint(
        order=51,
        title="Day 51: Git Aliases (Command shortcuts)",
        concept="Accelerating developer velocity by engineering custom shorthand commands, shell macros, and complex graph aliases in `.gitconfig`.",
        analogy="Typing `git log --graph --oneline --decorate --all` twenty times a day is like manually dialing a 20-digit international phone number every time you call your mom. An alias is setting up a 1-button speed dial: `git lg`.",
        theory_sections=[
            {
                "heading": "Why Use Git Aliases?",
                "body": (
                    "Professional developers type hundreds of Git commands weekly. "
                    "Aliases allow creating custom shortcuts (e.g. `git st` for `git status`), fixing common typos (`git cm` for `git commit -m`), "
                    "and constructing powerful diagnostic pipelines."
                )
            },
            {
                "heading": "Configuring Simple Aliases",
                "body": (
                    "Aliases are configured under the `[alias]` section of `.gitconfig`:\n"
                    "- `git config --global alias.co checkout`\n"
                    "- `git config --global alias.br branch`\n"
                    "- `git config --global alias.st status`\n"
                    "- `git config --global alias.unstage \"restore --staged\"`"
                )
            },
            {
                "heading": "Shell Command Aliases (The `!` Prefix)",
                "body": (
                    "If an alias begins with an exclamation mark `!`, Git executes it as a **full shell script**. "
                    "This lets you combine multiple commands, use shell pipelines, and call external utilities."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Essential Daily Velocity Aliases",
                "code": "# Configure staple shortcuts globally:\ngit config --global alias.st \"status -s\"\ngit config --global alias.co checkout\ngit config --global alias.sw switch\ngit config --global alias.br branch\ngit config --global alias.cm \"commit -m\"",
                "explanation": "High-frequency daily shorthand."
            },
            {
                "title": "The Famous 'Pretty Graph' Alias (git lg)",
                "code": "# The ultimate single-line graph alias:\ngit config --global alias.lg \"log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit\"\n\n# Run with:\ngit lg",
                "explanation": "Creates stunning, colorized ASCII history logs."
            },
            {
                "title": "Shell Pipeline Alias with Exclamation Mark (!)",
                "code": "# Alias that updates main, deletes merged local branches, and prunes remotes:\ngit config --global alias.cleanup \"!git switch main && git pull --rebase && git fetch --prune && git branch --merged | grep -v '^*\\|main' | xargs -n 1 git branch -d\"",
                "explanation": "Executes shell pipeline with the ! prefix."
            },
            {
                "title": "Viewing All Configured Aliases",
                "code": "# List all custom aliases defined in your git config:\ngit config --get-regexp alias",
                "explanation": "Inspects active user aliases."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Custom Git Alias",
            description="Configure a global alias `st` mapped to `status -s` and verify it with `git config --global --get alias.st`.",
            starter_code="# Set alias.st globally to 'status -s'\n",
            solution_code="git config --global alias.st \"status -s\"\ngit config --global --get alias.st",
            expected_output="status -s"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the exclamation mark `!` prefix signify when defining an alias in Git config?",
                options=[
                    "It executes the alias in the system shell rather than as a native sub-command, enabling shell scripts and pipelines",
                    "It marks the alias as dangerous",
                    "It runs the command with sudo permissions",
                    "It suppresses all output"
                ],
                correct_answer="It executes the alias in the system shell rather than as a native sub-command, enabling shell scripts and pipelines",
                explanation="The `!` prefix allows running arbitrary shell commands and pipelines."
            ),
            QuizQuestionBlueprint(
                question="In which configuration file are `--global` Git aliases stored?",
                options=["~/.gitconfig", "/etc/gitconfig", ".git/config", ".git/aliases"],
                correct_answer="~/.gitconfig",
                explanation="Global user preferences and aliases reside in `~/.gitconfig`."
            ),
            QuizQuestionBlueprint(
                question="Which command displays all aliases currently configured in your Git environment?",
                options=["git config --get-regexp alias", "git alias --list", "git show aliases", "git shortcuts"],
                correct_answer="git config --get-regexp alias",
                explanation="`git config --get-regexp alias` filters configuration keys starting with 'alias'."
            ),
            QuizQuestionBlueprint(
                question="If you configure `git config --global alias.unstage \"restore --staged\"`, what command can you now run to unstage `app.py`?",
                options=["git unstage app.py", "git restore-now app.py", "git alias unstage app.py", "git stage --undo app.py"],
                correct_answer="git unstage app.py",
                explanation="The alias maps `git unstage` directly to `git restore --staged`."
            ),
            QuizQuestionBlueprint(
                question="Why do engineering teams recommend custom aliases like `git lg`?",
                options=[
                    "It condenses complex, hard-to-remember formatting flags into a simple 2-letter command, increasing developer productivity",
                    "It prevents syntax errors in code",
                    "It bypasses authentication",
                    "It encrypts git logs"
                ],
                correct_answer="It condenses complex, hard-to-remember formatting flags into a simple 2-letter command, increasing developer productivity",
                explanation="Aliases eliminate keystrokes and simplify repetitive complex flags."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 52: Conventional Commits Standard (feat:, fix:, chore:)
    # ----------------------------------------------------
    DayBlueprint(
        order=52,
        title="Day 52: Conventional Commits Standard (feat:, fix:, chore:)",
        concept="Adopting the industry-standard Conventional Commits specification to enable automated Semantic Versioning, automated changelog generation, and machine-readable histories.",
        analogy="Writing unstructured commit messages is like scribbling handwritten notes on medical bottles. Conventional Commits is like an FDA standardized pharmaceutical label: everyone knows that `feat` means a new medicine, `fix` means fixing a formula flaw, and `!` means an explosive warning.",
        theory_sections=[
            {
                "heading": "The Conventional Commits Specification",
                "body": (
                    "The Conventional Commits specification is a lightweight convention on top of commit messages. "
                    "It provides an easy set of rules for creating an explicit commit history, which makes it easy to write automated tools on top of.\n"
                    "Structure:\n"
                    "```text\n"
                    "<type>[optional scope]: <description>\n"
                    "\n"
                    "[optional body]\n"
                    "\n"
                    "[optional footer(s)]\n"
                    "```"
                )
            },
            {
                "heading": "Standard Structural Types",
                "body": (
                    "- `feat:` Introduces a new feature (correlates with `MINOR` in SemVer).\n"
                    "- `fix:` Patches a bug (correlates with `PATCH` in SemVer).\n"
                    "- `docs:` Documentation only changes.\n"
                    "- `style:` Changes that do not affect code meaning (white-space, formatting).\n"
                    "- `refactor:` Code change that neither fixes a bug nor adds a feature.\n"
                    "- `perf:` Code change that improves performance.\n"
                    "- `test:` Adding missing tests or correcting existing tests.\n"
                    "- `chore:` Build process or auxiliary tool changes (dependency updates)."
                )
            },
            {
                "heading": "Breaking Changes (`!` and `BREAKING CHANGE:`)",
                "body": (
                    "Appending a `!` after the type/scope (e.g. `feat(api)!: drop support for v1 endpoints`) or adding "
                    "`BREAKING CHANGE: <explanation>` in the footer signifies a breaking API change (correlates with `MAJOR` in SemVer)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Standard Feature and Fix Commits",
                "code": "# Adding a new user-facing feature:\ngit commit -m \"feat(auth): add OAuth2 login with GitHub\"\n\n# Patching a bug:\ngit commit -m \"fix(checkout): resolve price calculation rounding error\"",
                "explanation": "Clear machine-readable type and scope."
            },
            {
                "title": "Commit with Breaking Change Indicator (!)",
                "code": "# Breaking change indicated with exclamation mark:\ngit commit -m \"feat(api)!: change user response schema to camelCase\"\n\n# Or with explicit footer:\ngit commit \\\n  -m \"refactor(db): drop support for PostgreSQL 11\" \\\n  -m \"BREAKING CHANGE: Upgraded internal query drivers. PostgreSQL 12+ is now required.\"",
                "explanation": "Triggers automated major version increment in CI/CD."
            },
            {
                "title": "Chore and Documentation Commits",
                "code": "# Updating project dependencies:\ngit commit -m \"chore(deps): bump express from 4.18.2 to 4.19.2\"\n\n# Updating documentation:\ngit commit -m \"docs(readme): add docker compose deployment instructions\"",
                "explanation": "Categorizes non-feature maintenance."
            },
            {
                "title": "Automated Changelog Generation",
                "code": "# Tools like standard-version parse conventional commits automatically:\n# npx standard-version\n# Automatically increments SemVer version in package.json and updates CHANGELOG.md!",
                "explanation": "Powers zero-touch release automation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Conventional Commit Message",
            description="Create a file 'api.py', stage it, and commit it using Conventional Commits format: 'feat(api): implement health check endpoint'.",
            starter_code="# Create api.py, stage it, and commit using Conventional Commits\n",
            solution_code="echo 'def health(): return 200' > api.py\ngit add api.py\ngit commit -m \"feat(api): implement health check endpoint\"",
            expected_output="[main ...] feat(api): implement health check endpoint\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In the Conventional Commits specification, which commit type corresponds directly to a SemVer `MINOR` version bump?",
                options=["feat:", "fix:", "chore:", "docs:"],
                correct_answer="feat:",
                explanation="`feat:` represents new backwards-compatible functionality, incrementing the MINOR version."
            ),
            QuizQuestionBlueprint(
                question="How is a breaking API change indicated in a Conventional Commit header?",
                options=[
                    "By adding an exclamation mark `!` immediately after the type/scope (e.g. `feat(api)!: ...`)",
                    "By writing the commit in ALL CAPS",
                    "By adding three question marks",
                    "By prefixing with `danger:`"
                ],
                correct_answer="By adding an exclamation mark `!` immediately after the type/scope (e.g. `feat(api)!: ...`)",
                explanation="The `!` modifier denotes a breaking change, signaling a MAJOR version bump."
            ),
            QuizQuestionBlueprint(
                question="Which commit type should be used for updating a project's build scripts or npm dependency versions without altering product features?",
                options=["chore:", "feat:", "fix:", "style:"],
                correct_answer="chore:",
                explanation="`chore:` is standard for auxiliary tools, build scripts, and dependencies."
            ),
            QuizQuestionBlueprint(
                question="What is the primary benefit of enforcing Conventional Commits across an engineering organization?",
                options=[
                    "It enables automated Semantic Versioning, automated CHANGELOG.md generation, and clear changelog categorization",
                    "It reduces lines of code by 50%",
                    "It prevents merge conflicts permanently",
                    "It compiles the code automatically"
                ],
                correct_answer="It enables automated Semantic Versioning, automated CHANGELOG.md generation, and clear changelog categorization",
                explanation="Standardized commit schemas unlock full release automation pipelines."
            ),
            QuizQuestionBlueprint(
                question="Which commit type applies strictly to formatting, whitespace, and semicolons without altering code logic?",
                options=["style:", "refactor:", "perf:", "fix:"],
                correct_answer="style:",
                explanation="`style:` denotes cosmetic, non-functional formatting adjustments."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 53: Semantic Versioning (SemVer)
    # ----------------------------------------------------
    DayBlueprint(
        order=53,
        title="Day 53: Semantic Versioning (SemVer)",
        concept="Mastering the SemVer specification (`MAJOR.MINOR.PATCH`), pre-release tags, and mapping release cycles to Git tags and automated release bots.",
        analogy="Semantic Versioning is a universal contract between library creators and consumers: PATCH says 'I fixed a leak under the hood; nothing you do will break.' MINOR says 'I gave you a new stereo; everything still works.' MAJOR says 'I replaced the steering wheel with an airplane joystick; you must adapt your driving.'",
        theory_sections=[
            {
                "heading": "The SemVer Formula (`MAJOR.MINOR.PATCH`)",
                "body": (
                    "Semantic Versioning 2.0.0 uses a 3-part numerical format: `X.Y.Z`\n"
                    "1. **MAJOR (`X`)**: Incremented when you make incompatible API changes (breaking changes).\n"
                    "2. **MINOR (`Y`)**: Incremented when you add functionality in a backwards-compatible manner.\n"
                    "3. **PATCH (`Z`)**: Incremented when you make backwards-compatible bug fixes."
                )
            },
            {
                "heading": "Pre-Release and Build Metadata",
                "body": (
                    "- **Pre-Release Identifiers**: `1.0.0-alpha.1`, `2.1.0-beta.3`, `3.0.0-rc.1`. Indicates software is unstable or undergoing testing.\n"
                    "- **Build Metadata**: `1.0.0+20130313144700`."
                )
            },
            {
                "heading": "Zero Major (`0.y.z`) Initial Development",
                "body": (
                    "Major version zero (`0.y.z`) is for initial development. Anything MAY change at any time. "
                    "The public API should not be considered stable until version `1.0.0` is published."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Git Tags to SemVer",
                "code": "# Patch Release (Bug fix):\ngit tag -a v1.0.1 -m \"Release v1.0.1 (Patch): fix security vulnerability\"\n\n# Minor Release (New feature, backwards-compatible):\ngit tag -a v1.1.0 -m \"Release v1.1.0 (Minor): add export to CSV feature\"\n\n# Major Release (Breaking API change):\ngit tag -a v2.0.0 -m \"Release v2.0.0 (Major): redesign authentication architecture\"",
                "explanation": "Tags represent formal SemVer milestone pins."
            },
            {
                "title": "Pre-Release Candidate Tagging",
                "code": "# Tagging a release candidate before final release:\ngit tag -a v2.0.0-rc.1 -m \"Release Candidate 1 for testing\"",
                "explanation": "Designates test candidate builds."
            },
            {
                "title": "Sorting Tags by SemVer Version",
                "code": "# Sort git tags according to SemVer versioning rules (-V / --sort=v:refname):\ngit tag -l --sort=v:refname\n\n# Output orders correctly: v0.9.0, v1.0.0, v1.0.10 (not lexicographical v1.0.10 before v1.0.2)",
                "explanation": "Ensures proper numerical version ordering."
            },
            {
                "title": "Inspecting Latest Tag via git describe",
                "code": "# Find the most recent tag reachable from current commit:\ngit describe --tags\n\n# Output:\n# v1.1.0-4-g7a4e8c1 (4 commits past v1.1.0 tag at hash 7a4e8c1)",
                "explanation": "Calculates dynamic build versions based on Git history."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create SemVer Tag and Inspect with git describe",
            description="Tag the current commit with annotated SemVer tag 'v1.2.0' and run `git describe --tags`.",
            starter_code="# Create annotated tag v1.2.0 and describe\n",
            solution_code="git tag -a v1.2.0 -m \"Release v1.2.0\"\ngit describe --tags",
            expected_output="v1.2.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In SemVer `2.4.1`, what does the number `4` represent?",
                options=["MINOR version (backwards-compatible new features)", "MAJOR version", "PATCH version", "Build number"],
                correct_answer="MINOR version (backwards-compatible new features)",
                explanation="In `X.Y.Z`, `X` is Major, `Y` is Minor, and `Z` is Patch."
            ),
            QuizQuestionBlueprint(
                question="When MUST the `MAJOR` version number be incremented in SemVer?",
                options=[
                    "When breaking, incompatible API changes are introduced that require consumers to update their code",
                    "Every time a bug is fixed",
                    "Once every calendar year",
                    "When the author changes jobs"
                ],
                correct_answer="When breaking, incompatible API changes are introduced that require consumers to update their code",
                explanation="Major bumps indicate backwards-incompatible API modifications."
            ),
            QuizQuestionBlueprint(
                question="What does a major version of `0` (e.g. `0.4.2`) signify according to the SemVer specification?",
                options=[
                    "Initial rapid development phase; the public API is unstable and may change at any time",
                    "The project has been abandoned",
                    "The project is 100% bug-free",
                    "The project cannot be downloaded"
                ],
                correct_answer="Initial rapid development phase; the public API is unstable and may change at any time",
                explanation="Version `0.x.x` represents initial pre-release experimental development."
            ),
            QuizQuestionBlueprint(
                question="Which flag sorts Git tags by proper semantic version numbers rather than strict alphabetical text order?",
                options=["--sort=v:refname", "--sort-semver", "--sort=version-desc", "-n"],
                correct_answer="--sort=v:refname",
                explanation="`--sort=v:refname` applies natural version sorting (e.g. 1.10 after 1.2)."
            ),
            QuizQuestionBlueprint(
                question="What does `git describe --tags` output when standing 3 commits ahead of tag `v1.0.0`?",
                options=[
                    "A human-readable string like `v1.0.0-3-g<hash>`, showing the tag, commit offset, and commit hash",
                    "An error message",
                    "A list of all contributors",
                    "The commit message of v1.0.0"
                ],
                correct_answer="A human-readable string like `v1.0.0-3-g<hash>`, showing the tag, commit offset, and commit hash",
                explanation="`git describe` calculates version distances from the nearest ancestor tag."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 54: Intro to Git Automation (GitHub Actions / GitLab CI)
    # ----------------------------------------------------
    DayBlueprint(
        order=54,
        title="Day 54: Intro to Git Automation (GitHub Actions / GitLab CI)",
        concept="Understanding Continuous Integration and Continuous Deployment (CI/CD) pipelines triggered automatically by Git lifecycle events (`push`, `pull_request`).",
        analogy="Git automation is like an automated quality control assembly line in a car factory. The moment a worker pushes a new car chassis onto the conveyor belt (`git push`), robot lasers automatically measure the bolts, spray water to test for leaks, and crash-test the brakes without human intervention.",
        theory_sections=[
            {
                "heading": "What is Git Automation / CI/CD?",
                "body": (
                    "**Continuous Integration (CI)** automatically builds and runs tests on every push or pull request to verify that new code doesn't break the system. "
                    "**Continuous Deployment (CD)** automatically deploys verified code to staging or production servers."
                )
            },
            {
                "heading": "GitHub Actions Architecture",
                "body": (
                    "GitHub Actions uses YAML files located in `.github/workflows/`:\n"
                    "- **Workflows**: Automated procedures made of one or more jobs.\n"
                    "- **Events**: Specific Git activities that trigger the workflow (e.g., `on: [push, pull_request]`).\n"
                    "- **Jobs**: Sets of steps executing on a clean virtual runner (e.g., `ubuntu-latest`).\n"
                    "- **Steps**: Individual tasks running shell commands or pre-built community actions (`actions/checkout`, `actions/setup-node`)."
                )
            },
            {
                "heading": "GitLab CI Equivalency",
                "body": (
                    "In GitLab, automation is defined in a single `.gitlab-ci.yml` file in the root directory, "
                    "executing stages (build, test, deploy) across GitLab Runners."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Simple GitHub Actions Workflow (.github/workflows/ci.yml)",
                "code": "# Basic automated CI workflow:\nname: Node.js CI\n\non:\n  push:\n    branches: [ main ]\n  pull_request:\n    branches: [ main ]\n\njobs:\n  build-and-test:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Check out repository code\n        uses: actions/checkout@v4\n\n      - name: Set up Node.js\n        uses: actions/setup-node@v4\n        with:\n          node-version: 20\n\n      - name: Install dependencies\n        run: npm ci\n\n      - name: Run automated test suite\n        run: npm test",
                "explanation": "Standard pipeline running on every push and PR."
            },
            {
                "title": "Triggering Actions Locally Using 'act'",
                "code": "# Test GitHub Actions locally before pushing using the 'act' CLI tool:\nact pull_request",
                "explanation": "Runs workflows in local Docker containers."
            },
            {
                "title": "Viewing Workflow Runs via GitHub CLI",
                "code": "# Inspect status of cloud CI runs directly in terminal:\ngh run list\n\n# View live logs of active run:\ngh run watch",
                "explanation": "Monitors automated cloud pipelines from terminal."
            },
            {
                "title": "Branch Protection Rule Enforcement",
                "code": "# In GitHub Settings -> Branches -> Branch protection rules:\n# - Require a pull request before merging\n# - Require status checks to pass before merging: [build-and-test]\n# - Require linear history",
                "explanation": "Prevents broken code from merging to main."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect GitHub Actions Runs with CLI",
            description="Use the GitHub CLI to view recent workflow runs with `gh run list --limit 5`.",
            starter_code="# Inspect GitHub Actions workflow runs\n",
            solution_code="gh run list --limit 5",
            expected_output="STATUS ... TITLE ... WORKFLOW ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Where must GitHub Actions workflow YAML files be stored in a Git repository?",
                options=[
                    "Inside the `.github/workflows/` directory",
                    "Inside `/etc/actions/`",
                    "Inside `.git/actions/`",
                    "In the root folder named `workflow.txt`"
                ],
                correct_answer="Inside the `.github/workflows/` directory",
                explanation="GitHub looks specifically in `.github/workflows/` for workflow definitions."
            ),
            QuizQuestionBlueprint(
                question="Which action keyword in GitHub Actions triggers a workflow whenever code is pushed to the repository?",
                options=["on: [push]", "trigger: push", "when: commit", "start: push"],
                correct_answer="on: [push]",
                explanation="The `on` block defines which webhook events initiate workflow execution."
            ),
            QuizQuestionBlueprint(
                question="What does the standard action `actions/checkout@v4` do inside a GitHub Actions job?",
                options=[
                    "Clones your repository code into the virtual runner so subsequent job steps can access and test it",
                    "Checks out a hotel room for developers",
                    "Deletes your branch after tests",
                    "Publishes packages to npm"
                ],
                correct_answer="Clones your repository code into the virtual runner so subsequent job steps can access and test it",
                explanation="`actions/checkout` checks out your repo into `$GITHUB_WORKSPACE`."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Branch Protection Rule' in GitHub?",
                options=[
                    "A repository setting that forbids direct pushes to `main` and enforces passing CI tests and peer reviews before merging",
                    "An encryption cipher for branches",
                    "A tool that renames branches to protect privacy",
                    "A firewall that blocks foreign IP addresses"
                ],
                correct_answer="A repository setting that forbids direct pushes to `main` and enforces passing CI tests and peer reviews before merging",
                explanation="Protection rules enforce code review and automated CI verification."
            ),
            QuizQuestionBlueprint(
                question="What file defines continuous integration pipelines in GitLab?",
                options=[".gitlab-ci.yml", ".github/workflows/main.yml", "pipeline.json", "gitlab.conf"],
                correct_answer=".gitlab-ci.yml",
                explanation="GitLab repositories utilize `.gitlab-ci.yml` in the project root."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 55 (Capstone Project): Building an automated CI/CD pipeline triggering on git push
    # ----------------------------------------------------
    DayBlueprint(
        order=55,
        title="Day 55 (Capstone Project): Building an automated CI/CD pipeline triggering on `git push`",
        concept="The Grand Capstone: Assembling end-to-end version control mastery by building an automated GitHub Actions pipeline with linter enforcement, test validation, SemVer tagging, and release artifact deployment.",
        analogy="Today is graduation day. You will build a complete, professional automated continuous integration and delivery pipeline from scratch. When you type `git push`, your code will be tested, linted, packaged, and tagged automatically like in top-tier tech companies.",
        theory_sections=[
            {
                "heading": "Capstone Project Overview",
                "body": (
                    "In this comprehensive capstone project, you will unify all 55 days of version control engineering:\n"
                    "1. Set up a clean repository with Conventional Commits rules and a strict `.gitignore`.\n"
                    "2. Build a multi-stage GitHub Actions CI workflow triggered on `push` and `pull_request`.\n"
                    "3. Configure automated linting, test execution, and security secrets scanning.\n"
                    "4. Implement automated release tagging when PRs merge into `main`."
                )
            },
            {
                "heading": "Production Pipeline Architecture",
                "body": (
                    "- **Stage 1 (Lint & Security)**: Runs `flake8` or `eslint` to enforce code cleanliness and scans for exposed API secrets.\n"
                    "- **Stage 2 (Unit & Integration Tests)**: Executes test suites across multiple OS environments (Ubuntu, Windows, macOS matrix).\n"
                    "- **Stage 3 (Automated Release)**: On merge to `main`, reads Conventional Commit logs, calculates SemVer version, creates an Annotated Git Tag, and publishes release notes."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Complete Production CI/CD Workflow (.github/workflows/pipeline.yml)",
                "code": "name: Production CI/CD Pipeline\n\non:\n  push:\n    branches: [ main ]\n  pull_request:\n    branches: [ main ]\n\njobs:\n  quality-check:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Set up Python\n        uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - name: Install Lint & Security Tools\n        run: pip install flake8 bandit\n      - name: Code Quality Linting\n        run: flake8 src/ --max-line-length=88\n      - name: Security Scan\n        run: bandit -r src/\n\n  test-suite:\n    needs: quality-check\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Set up Python\n        uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - name: Install Dependencies & Run Pytest\n        run: |\n          pip install pytest\n          pytest tests/",
                "explanation": "Multi-job pipeline with dependency ordering using 'needs'."
            },
            {
                "title": "Automated Semantic Release Job",
                "code": "  release:\n    needs: test-suite\n    if: github.ref == 'refs/heads/main' && github.event_name == 'push'\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n        with:\n          fetch-depth: 0\n      - name: Automated Semantic Release\n        uses: cycjimmy/semantic-release-action@v4\n        env:\n          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}",
                "explanation": "Automatically cuts SemVer tags and releases on main pushes."
            },
            {
                "title": "Deploying Capstone Pipeline via Git",
                "code": "# 1. Create and stage workflow:\nmkdir -p .github/workflows\n# (Save workflow YAML as pipeline.yml)\ngit add .github/workflows/pipeline.yml\n\n# 2. Commit following Conventional Commits:\ngit commit -m \"ci: implement automated multi-stage CI/CD pipeline\"\n\n# 3. Push to remote and watch automation trigger!\ngit push origin main",
                "explanation": "Pushes the workflow definition directly to the remote repository."
            },
            {
                "title": "Monitoring Live Workflow with GitHub CLI",
                "code": "# Watch the capstone pipeline execute in real time:\ngh run watch\n\n# Check pipeline success:\ngh run view --log",
                "explanation": "Monitors deployment success from terminal."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Deploy Capstone CI Workflow and Push",
            description="Stage the workflow file '.github/workflows/pipeline.yml' and commit it with conventional commit message 'ci: add production workflow'.",
            starter_code="# Stage workflow file and commit\n",
            solution_code="git add .github/workflows/pipeline.yml\ngit commit -m \"ci: add production workflow\"",
            expected_output="[main ...] ci: add production workflow\n 1 file changed, ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In GitHub Actions, how do you ensure that the `test-suite` job only runs AFTER the `quality-check` job has successfully passed?",
                options=[
                    "By adding `needs: quality-check` inside the `test-suite` job definition",
                    "By adding `after: quality-check`",
                    "By numbering the jobs 1 and 2",
                    "GitHub Actions always runs jobs sequentially by default"
                ],
                correct_answer="By adding `needs: quality-check` inside the `test-suite` job definition",
                explanation="The `needs` keyword establishes dependency order between jobs."
            ),
            QuizQuestionBlueprint(
                question="Why is `fetch-depth: 0` required when checking out code in an automated release job like Semantic Release?",
                options=[
                    "To fetch the entire commit history and all tags so the release bot can calculate the previous version and parse all commits since the last release",
                    "To download code 10x faster",
                    "To fetch zero files",
                    "To disable Git history"
                ],
                correct_answer="To fetch the entire commit history and all tags so the release bot can calculate the previous version and parse all commits since the last release",
                explanation="Semantic release tools need full history and tags to determine the next version bump."
            ),
            QuizQuestionBlueprint(
                question="What condition ensures that a deployment or release job runs ONLY when commits are pushed directly to `main` (and not on pull requests)?",
                options=[
                    "`if: github.ref == 'refs/heads/main' && github.event_name == 'push'`",
                    "`if: branch == 'all'`",
                    "`when: always`",
                    "`run-on: main`"
                ],
                correct_answer="`if: github.ref == 'refs/heads/main' && github.event_name == 'push'`",
                explanation="Conditional `if` expressions prevent deployment steps from firing on PR previews."
            ),
            QuizQuestionBlueprint(
                question="Where are private secrets (e.g. AWS access keys or NPM tokens) securely stored and accessed in GitHub Actions workflows?",
                options=[
                    "In GitHub Repository Settings -> Secrets and variables -> Actions, referenced as `${{ secrets.MY_SECRET }}`",
                    "Committed in plain text inside `.env` in the repository",
                    "In the commit message body",
                    "In the public README file"
                ],
                correct_answer="In GitHub Repository Settings -> Secrets and variables -> Actions, referenced as `${{ secrets.MY_SECRET }}`",
                explanation="Secrets are encrypted in repo settings and injected as environment variables."
            ),
            QuizQuestionBlueprint(
                question="Congratulations on completing the 55-Day Git roadmap! What is the ultimate mark of Git and version control mastery in a professional team?",
                options=[
                    "Crafting atomic commits, maintaining clean linear branches, collaborating with empathy in code reviews, and automating testing/releases via CI/CD",
                    "Knowing how to type `git push --force` faster than coworkers",
                    "Memorizing all SHA-1 hashes",
                    "Never committing any code"
                ],
                correct_answer="Crafting atomic commits, maintaining clean linear branches, collaborating with empathy in code reviews, and automating testing/releases via CI/CD",
                explanation="True mastery is combining technical precision, empathy, and automation."
            )
        ],
        is_project_day=True,
        project_name="Building an automated CI/CD pipeline triggering on git push"
    )
]
