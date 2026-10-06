"""
Git & Version Control System Curriculum - Days 16 to 30
Module 2: Branching & Merging (Days 16-17)
Module 3: Remote Repositories (Days 18-23)
Module 4: Undoing Changes (Time Travel) (Days 24-28)
Module 5: Advanced Git Operations (Days 29-30 of 29-37)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_16_TO_30 = [
    # ----------------------------------------------------
    # Day 16: Merge Conflicts (Why they happen & manual resolution)
    # ----------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Merge Conflicts (Why they happen & manual resolution)",
        concept="De-mystifying merge conflicts: identifying conflict markers, manually choosing the correct logic, and completing conflict resolution.",
        analogy="Imagine you and your roommate have a physical paper calendar. You write 'Dinner with Mom at 7 PM' on Friday, and your roommate writes 'Movie Night at 7 PM' on the exact same Friday slot. The calendar cannot physically be both at once—you have to sit down, talk, pick one, and erase the other.",
        theory_sections=[
            {
                "heading": "Why Do Merge Conflicts Occur?",
                "body": (
                    "Git is extremely intelligent at merging file edits automatically as long as the edits touch **different lines** or **different files**. "
                    "A merge conflict occurs only when two separate commits have modified the **exact same lines of the exact same file** since their common ancestor, "
                    "or if one branch deleted a file that the other branch edited. Git halts the merge and asks the human developer to decide which version is correct."
                )
            },
            {
                "heading": "Anatomy of Conflict Markers",
                "body": (
                    "When a conflict occurs, Git writes conflict markers directly into the affected file:\n"
                    "```text\n"
                    "<<<<<<< HEAD (Current receiving branch)\n"
                    "const API_URL = 'https://api.production.com';\n"
                    "=======\n"
                    "const API_URL = 'https://api.staging.internal';\n"
                    ">>>>>>> feature/staging (Incoming branch)\n"
                    "```\n"
                    "- `<<<<<<< HEAD`: Starts the code from the branch you are standing on.\n"
                    "- `=======`: The divider line separating the two competing versions.\n"
                    "- `>>>>>>> branch_name`: Ends the code from the incoming branch."
                )
            },
            {
                "heading": "The 4-Step Conflict Resolution Procedure",
                "body": (
                    "1. Check which files are in conflict using `git status` (shows under 'Unmerged paths').\n"
                    "2. Open each conflicted file in an editor, edit the code to the desired final state, and **delete all conflict markers**.\n"
                    "3. Mark the conflict as resolved by staging the file: `git add <file>`.\n"
                    "4. Complete the merge commit: `git commit` (or `git merge --continue`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Triggering and Spotting a Merge Conflict",
                "code": "# Git alerts you during merge:\n# Auto-merging src/config.js\n# CONFLICT (content): Merge conflict in src/config.js\n# Automatic merge failed; fix conflicts and then commit the result.\n\ngit status\n# Unmerged paths:\n#   both modified:   src/config.js",
                "explanation": "Git halts and flags files requiring manual resolution."
            },
            {
                "title": "Inspecting Conflict Markers in Editor",
                "code": "# Inside src/config.js:\n# <<<<<<< HEAD\n# export const PORT = 8080;\n# =======\n# export const PORT = 9000;\n# >>>>>>> feature/port-update\n\n# Manually edit to desired outcome (e.g. PORT = 9000) and remove <<<<, ====, >>>> markers",
                "explanation": "Human developer selects or synthesizes the correct lines."
            },
            {
                "title": "Staging and Finalizing Conflict Resolution",
                "code": "# 1. Stage the resolved file (tells Git conflict is cleared):\ngit add src/config.js\n\n# 2. Finish the merge commit:\ngit commit -m \"fix: resolve port conflict between main and feature\"\n# Or simply:\n# git merge --continue",
                "explanation": "Staging marks the unmerged path as resolved."
            },
            {
                "title": "Aborting if In Over Your Head",
                "code": "# If you made a mistake or want to back out cleanly:\ngit merge --abort",
                "explanation": "Resets the workspace back to before the conflict was encountered."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Resolve a Simulated Conflict File",
            description="Create a file 'settings.py' with conflict markers, clean the markers leaving only 'THEME = \"dark\"', stage the file, and view status.",
            starter_code="# Write conflicted file, clean markers, stage, and check status\n",
            solution_code="echo 'THEME = \"dark\"' > settings.py\ngit add settings.py\ngit status -s",
            expected_output="M  settings.py"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Under what precise circumstance does Git trigger a merge conflict?",
                options=[
                    "When two branches modify the exact same lines of the same file since their common ancestor",
                    "Whenever any two branches are merged",
                    "When you merge on a weekend",
                    "When files have more than 100 lines of code"
                ],
                correct_answer="When two branches modify the exact same lines of the same file since their common ancestor",
                explanation="Conflicts happen when Git cannot mathematically determine which change should take precedence."
            ),
            QuizQuestionBlueprint(
                question="What does the section between `<<<<<<< HEAD` and `=======` represent?",
                options=[
                    "The code changes that already existed on your currently checked-out branch",
                    "The incoming code from the branch being merged",
                    "The code from the original author 5 years ago",
                    "Deleted code from your hard drive"
                ],
                correct_answer="The code changes that already existed on your currently checked-out branch",
                explanation="HEAD represents the active receiving branch's version."
            ),
            QuizQuestionBlueprint(
                question="After manually editing a conflicted file to keep the correct lines and deleting conflict markers, what command signals to Git that the conflict is resolved?",
                options=["git add <file>", "git resolve <file>", "git clear-conflict", "git fix <file>"],
                correct_answer="git add <file>",
                explanation="Running `git add` on the resolved file transitions it from 'unmerged' to 'staged'."
            ),
            QuizQuestionBlueprint(
                question="What will happen if you stage and commit a conflicted file WITHOUT removing the `<<<<<<<`, `=======`, and `>>>>>>>` markers?",
                options=[
                    "The conflict marker text will literally be committed into your source code and likely cause syntax/compiler errors in production",
                    "Git automatically strips them out for you",
                    "The computer will refuse to boot",
                    "GitHub will automatically delete the repository"
                ],
                correct_answer="The conflict marker text will literally be committed into your source code and likely cause syntax/compiler errors in production",
                explanation="Git commits exactly what is on disk; leaving markers in breaks compilers and runtimes."
            ),
            QuizQuestionBlueprint(
                question="Which command immediately terminates a messy conflict resolution and reverts the repository to the pre-merge state?",
                options=["git merge --abort", "git merge --undo", "git merge --cancel", "git reset --hard origin"],
                correct_answer="git merge --abort",
                explanation="`git merge --abort` safely unwinds the interrupted merge operation."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 17: Using Visual Diff/Merge Tools (VS Code, Meld)
    # ----------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Using Visual Diff/Merge Tools (VS Code, Meld)",
        concept="Configuring graphical 3-way merge tools (`git mergetool`, VS Code 3-way editor) to visually inspect and resolve complex conflicts with confidence.",
        analogy="Solving a 50-file conflict using a basic text terminal is like performing surgery in the dark with a flashlight. A visual 3-way merge tool is like a high-definition operating room microscope with color-coded laser guides.",
        theory_sections=[
            {
                "heading": "Why Graphical Merge Tools?",
                "body": (
                    "In large enterprise applications, a merge conflict can span dozens of files and hundreds of lines. "
                    "Reading raw `<<<<<<< HEAD` markers is tiring and error-prone. "
                    "Visual tools present a side-by-side or 3-pane interface showing: Local (Current), Base (Common Ancestor), and Remote (Incoming)."
                )
            },
            {
                "heading": "VS Code as the Default Merge Tool",
                "body": (
                    "Visual Studio Code features an outstanding built-in 3-way merge editor. "
                    "You can configure Git so that running `git mergetool` automatically launches VS Code's visual conflict resolver."
                )
            },
            {
                "heading": "The 3-Pane Layout",
                "body": (
                    "1. **Left Pane (Current/Ours)**: Your active branch.\n"
                    "2. **Right Pane (Incoming/Theirs)**: The branch being merged.\n"
                    "3. **Bottom Pane (Result)**: The live output file where you can check boxes to accept current, incoming, or both."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Configuring VS Code as Git Diff & Merge Tool",
                "code": "# Set VS Code as default difftool:\ngit config --global diff.tool default-difftool\ngit config --global difftool.default-difftool.cmd \"code --wait --diff \\$LOCAL \\$REMOTE\"\n\n# Set VS Code as default mergetool:\ngit config --global merge.tool code\ngit config --global mergetool.code.cmd \"code --wait --merge \\$REMOTE \\$LOCAL \\$BASE \\$MERGED\"",
                "explanation": "Binds Git's internal diff and merge hooks to VS Code."
            },
            {
                "title": "Disabling Annoying .orig Backup Files",
                "code": "# Prevent Git from leaving .orig backup files on disk after merges:\ngit config --global mergetool.keepBackup false",
                "explanation": "Stops cluttering your working tree with leftover backup files."
            },
            {
                "title": "Launching the Graphical Merge Tool",
                "code": "# When a conflict occurs, launch the configured visual resolver:\ngit mergetool\n\n# VS Code opens with side-by-side 3-way comparison editor",
                "explanation": "Steps through each conflicted file sequentially in your visual editor."
            },
            {
                "title": "Inspecting Differences with git difftool",
                "code": "# Compare working tree changes visually in GUI instead of terminal:\ngit difftool",
                "explanation": "Spawns the GUI tool to review changes side by side."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Git Merge Tool Settings",
            description="Configure git globally to not keep .orig backups after running mergetool, and verify the setting with `git config --get`.",
            starter_code="# Set mergetool.keepBackup to false and read back value\n",
            solution_code="git config --global mergetool.keepBackup false\ngit config --global --get mergetool.keepBackup",
            expected_output="false"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What command launches your configured visual GUI to resolve unmerged files?",
                options=["git mergetool", "git visual-merge", "git diff-gui", "git fix-ui"],
                correct_answer="git mergetool",
                explanation="`git mergetool` iterates through conflicted files and opens the configured GUI tool."
            ),
            QuizQuestionBlueprint(
                question="In a standard 3-way visual merge tool, what does the 'Base' pane represent?",
                options=[
                    "The common ancestor commit before either branch made changes",
                    "The GitHub cloud server",
                    "The local machine's operating system",
                    "The default branch template"
                ],
                correct_answer="The common ancestor commit before either branch made changes",
                explanation="Base is the original snapshot from which both divergent branches evolved."
            ),
            QuizQuestionBlueprint(
                question="Why do developers configure `mergetool.keepBackup` to `false`?",
                options=[
                    "To prevent Git from cluttering the working directory with `.orig` backup files after resolving conflicts",
                    "To speed up internet downloads",
                    "To delete the master branch",
                    "To disable Git history"
                ],
                correct_answer="To prevent Git from cluttering the working directory with `.orig` backup files after resolving conflicts",
                explanation="By default, `git mergetool` creates `.orig` files that must otherwise be manually deleted."
            ),
            QuizQuestionBlueprint(
                question="Which visual tool is built into popular IDEs like Visual Studio Code for interactive conflict resolution?",
                options=[
                    "The 3-Way Merge Editor",
                    "The Hex Dump Disassembler",
                    "The Memory Profiler",
                    "The Task Manager"
                ],
                correct_answer="The 3-Way Merge Editor",
                explanation="VS Code features an interactive 3-way merge editor with checkboxes for accepting changes."
            ),
            QuizQuestionBlueprint(
                question="What does `git difftool` do compared to standard `git diff`?",
                options=[
                    "It opens differences in an external graphical visual tool instead of the terminal text pager",
                    "It automatically fixes linting errors",
                    "It translates code from Python to C",
                    "It publishes diffs to the web"
                ],
                correct_answer="It opens differences in an external graphical visual tool instead of the terminal text pager",
                explanation="`git difftool` invokes an external visual viewer (like VS Code, Meld, or Beyond Compare)."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 18: Concept of Remotes (git remote add, -v)
    # ----------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Concept of Remotes (`git remote add`, `-v`)",
        concept="Understanding remote repository bookmarks, protocol endpoints, and managing upstream and origin remote aliases.",
        analogy="A 'remote' in Git is like an entry in your phone's address book. Instead of having to type out 'https://github.com/my-company/enterprise-project-v2.git' every time you want to talk to the cloud, you save it with the nickname 'origin'.",
        theory_sections=[
            {
                "heading": "What is a Remote Repository?",
                "body": (
                    "A remote repository is a version of your project hosted on the internet or local network (e.g. GitHub, GitLab, private server). "
                    "Git allows you to connect your local repository to multiple remotes simultaneously. "
                    "By default convention, the primary remote you clone from or push to is named `origin`."
                )
            },
            {
                "heading": "Remote Aliases: origin vs upstream",
                "body": (
                    "- `origin`: The default shorthand alias pointing to your own fork or central repo.\n"
                    "- `upstream`: Conventional shorthand alias pointing to the original public project repository when you are contributing via a fork."
                )
            },
            {
                "heading": "Inspecting Remote Connections",
                "body": (
                    "`git remote` lists your configured remote aliases. "
                    "`git remote -v` (verbose) displays the fetch and push URL endpoints mapped to each alias."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Adding a Remote to an Existing Local Repo",
                "code": "# Connect local repository to GitHub repo via HTTPS:\ngit remote add origin https://github.com/username/project.git\n\n# Or via SSH:\ngit remote add origin git@github.com:username/project.git",
                "explanation": "Associates the nickname 'origin' with the remote repository URL."
            },
            {
                "title": "Inspecting Remotes with Verbose Flag",
                "code": "# Display configured remotes and their read/write URLs:\ngit remote -v\n\n# Output:\n# origin  git@github.com:username/project.git (fetch)\n# origin  git@github.com:username/project.git (push)",
                "explanation": "Shows endpoints used for fetching and pushing."
            },
            {
                "title": "Renaming and Removing Remotes",
                "code": "# Rename a remote alias from 'origin' to 'github':\ngit remote rename origin github\n\n# Remove an obsolete remote connection:\ngit remote remove old-server",
                "explanation": "Manage remote bookmarks as server architectures change."
            },
            {
                "title": "Inspecting Remote Metadata and Branches",
                "code": "# Query remote server for detailed tracking information:\ngit remote show origin\n\n# Output displays HEAD branch, remote tracking branches, and sync status",
                "explanation": "Provides deep diagnostic status on remote branch states."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Add and Inspect Remote Alias",
            description="Add a remote named 'origin' with URL 'https://github.com/dev/demo.git' and run `git remote -v` to verify both fetch and push URLs.",
            starter_code="# Add remote origin and list remotes verbosely\n",
            solution_code="git remote add origin https://github.com/dev/demo.git\ngit remote -v",
            expected_output="origin\thttps://github.com/dev/demo.git (fetch)\norigin\thttps://github.com/dev/demo.git (push)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the industry-standard default name given to your primary remote repository bookmark in Git?",
                options=["origin", "master", "central", "cloud"],
                correct_answer="origin",
                explanation="When cloning or setting up primary remotes, Git conventions name it `origin`."
            ),
            QuizQuestionBlueprint(
                question="Which flag passed to `git remote` displays the exact URLs used for fetching and pushing?",
                options=["-v (or --verbose)", "-u", "-a", "--detail"],
                correct_answer="-v (or --verbose)",
                explanation="`git remote -v` prints the fetch and push URLs associated with each remote name."
            ),
            QuizQuestionBlueprint(
                question="Can a single local Git repository be connected to more than one remote server?",
                options=[
                    "Yes, a local repo can track multiple remotes (e.g., origin for your fork, upstream for the main repo)",
                    "No, Git strictly restricts projects to one remote only",
                    "Only if you buy Git Professional license",
                    "Only on Linux machines"
                ],
                correct_answer="Yes, a local repo can track multiple remotes (e.g., origin for your fork, upstream for the main repo)",
                explanation="You can define as many remotes as needed (e.g., `origin`, `upstream`, `staging`, `production`)."
            ),
            QuizQuestionBlueprint(
                question="Which command updates the URL of an existing remote named 'origin'?",
                options=[
                    "git remote set-url origin <new-url>",
                    "git remote change-url origin <new-url>",
                    "git remote update origin <new-url>",
                    "git set origin <new-url>"
                ],
                correct_answer="git remote set-url origin <new-url>",
                explanation="`git remote set-url <name> <url>` modifies the target destination of a remote bookmark."
            ),
            QuizQuestionBlueprint(
                question="What information does `git remote show origin` provide?",
                options=[
                    "Detailed diagnostics including tracked branches, HEAD branch on remote, and push/pull configurations",
                    "The billing invoice for your GitHub account",
                    "The passwords of all team contributors",
                    "The server CPU usage"
                ],
                correct_answer="Detailed diagnostics including tracked branches, HEAD branch on remote, and push/pull configurations",
                explanation="`git remote show` inspects upstream tracking relationships and branch configurations."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 19: Cloning a Repository (git clone)
    # ----------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Cloning a Repository (`git clone`)",
        concept="Mastering repository cloning, shallow clones (`--depth`), single-branch clones, and understanding what happens behind the scenes during a clone.",
        analogy="Cloning a Git repository is not like downloading a ZIP file from Google Drive. It is like photocopying an entire library, including every author's historical revision notes and architectural blue-prints, and placing that complete library on your desk.",
        theory_sections=[
            {
                "heading": "What Happens During `git clone`?",
                "body": (
                    "When you run `git clone <url>`, Git executes four distinct actions:\n"
                    "1. Creates a new local directory.\n"
                    "2. Initializes a local `.git` directory inside it.\n"
                    "3. Fetches all commit objects, blobs, trees, and tags across the repository's entire history.\n"
                    "4. Automatically configures a remote named `origin` and checks out the default branch (`main`)."
                )
            },
            {
                "heading": "Shallow Cloning (`--depth`) for Large Repos",
                "body": (
                    "Some enterprise or open-source repositories (like Linux kernel or Chromium) have 15+ years of history and measure 50+ Gigabytes. "
                    "Running a full clone in CI/CD build runners is wasteful. "
                    "A **shallow clone** (`git clone --depth 1`) fetches only the single most recent commit, reducing download size and time by up to 98%."
                )
            },
            {
                "heading": "Single Branch Cloning",
                "body": (
                    "Using `--single-branch` instructs Git to download only one specific branch rather than fetching references for every experimental branch on the remote server."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Standard Repository Cloning",
                "code": "# Clone public repository via HTTPS into a folder named 'react':\ngit clone https://github.com/facebook/react.git\n\n# Clone into a custom directory name 'my-react':\ngit clone https://github.com/facebook/react.git my-react",
                "explanation": "Copies full history and configures origin remote."
            },
            {
                "title": "High-Speed Shallow Clone for CI/CD Pipelines",
                "code": "# Download ONLY the latest commit (depth 1) to save gigabytes and build fast:\ngit clone --depth 1 https://github.com/large/enterprise-repo.git\n\n# Git history will only show 1 commit locally",
                "explanation": "Dramatically accelerates automated testing and deployment workflows."
            },
            {
                "title": "Cloning a Specific Branch",
                "code": "# Clone only the 'release-v3' branch:\ngit clone -b release-v3 --single-branch https://github.com/org/repo.git",
                "explanation": "Targets a single branch directly upon download."
            },
            {
                "title": "Unshallowing a Shallow Clone",
                "code": "# If you later need the full historical commit log:\ngit fetch --unshallow",
                "explanation": "Converts a shallow clone back into a full-history clone."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execute Shallow Clone Command",
            description="Write the command to shallow-clone a repository from 'https://github.com/org/app.git' with a depth of 1 into directory 'fast_app'.",
            starter_code="# Write the shallow clone command\n",
            solution_code="git clone --depth 1 https://github.com/org/app.git fast_app",
            expected_output="Cloning into 'fast_app'..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between downloading a project ZIP file from GitHub and running `git clone`?",
                options=[
                    "`git clone` downloads the entire `.git` database with full commit history, branches, and remote tracking",
                    "A ZIP file runs faster on Linux",
                    "`git clone` converts code to machine language",
                    "There is no difference"
                ],
                correct_answer="`git clone` downloads the entire `.git` database with full commit history, branches, and remote tracking",
                explanation="Cloning brings down the complete version control repository and sets up tracking."
            ),
            QuizQuestionBlueprint(
                question="Why is `git clone --depth 1` frequently used in CI/CD automated deployment pipelines?",
                options=[
                    "It downloads only the latest single commit snapshot, saving bandwidth and slashing build times",
                    "It automatically runs automated unit tests",
                    "It bypasses authentication requirements",
                    "It compiles the code automatically"
                ],
                correct_answer="It downloads only the latest single commit snapshot, saving bandwidth and slashing build times",
                explanation="CI runners only need the current codebase to build and test, not 10 years of history."
            ),
            QuizQuestionBlueprint(
                question="What remote name is automatically created by Git when you clone a repository?",
                options=["origin", "upstream", "github", "source"],
                correct_answer="origin",
                explanation="Git sets up `origin` pointing back to the cloned URL automatically."
            ),
            QuizQuestionBlueprint(
                question="Which flag allows you to specify a single specific branch to clone rather than all branches?",
                options=["-b (or --branch)", "-s", "-p", "--only"],
                correct_answer="-b (or --branch)",
                explanation="`-b <branch>` checks out the specified branch instead of the remote HEAD default."
            ),
            QuizQuestionBlueprint(
                question="How do you convert an existing shallow clone into a full-history repository?",
                options=["git fetch --unshallow", "git clone --complete", "git history --fill", "git expand"],
                correct_answer="git fetch --unshallow",
                explanation="`git fetch --unshallow` downloads the rest of the historical commit objects."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 20: Pushing Code (git push, upstream -u)
    # ----------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Pushing Code (`git push`, upstream `-u`)",
        concept="Publishing local commits to remote servers, establishing branch tracking with `-u` / `--set-upstream`, and understanding force-pushing hazards.",
        analogy="`git push` is like shipping the packages from your local factory warehouse up to the national distribution center. Using `-u` (set-upstream) is like establishing a dedicated priority conveyor belt between your local office and the cloud branch.",
        theory_sections=[
            {
                "heading": "Publishing Local Commits",
                "body": (
                    "When you make commits locally, your teammates cannot see them. "
                    "`git push` uploads your new commit objects, blobs, and trees to the remote repository and advances the corresponding remote branch pointer."
                )
            },
            {
                "heading": "Setting Upstream Tracking (`-u`)",
                "body": (
                    "The first time you push a newly created local branch, Git doesn't know which remote branch it should correspond to. "
                    "Passing `-u` (or `--set-upstream`) creates a tracking link in `.git/config`. "
                    "Once established, you can simply type `git push` or `git pull` without specifying the remote or branch name ever again."
                )
            },
            {
                "heading": "Force Pushing Dangers (`--force` vs `--force-with-lease`)",
                "body": (
                    "If your local branch history has been rewritten (e.g. via rebase or amend), remote Git will reject standard push. "
                    "`git push --force` brutally overwrites the remote branch, potentially destroying coworkers' work. "
                    "Professionals use `git push --force-with-lease`: it only overwrites if nobody else has pushed commits to that branch in the meantime."
                )
            }
        ],
        code_snippets=[
            {
                "title": "First-Time Push with Upstream Tracking",
                "code": "# Push new feature branch to origin and establish permanent tracking:\ngit push -u origin feature/dark-mode\n\n# Output confirms tracking link:\n# Branch 'feature/dark-mode' set up to track remote branch 'feature/dark-mode' from 'origin'.",
                "explanation": "Configures branch.<name>.remote and merge settings in .git/config."
            },
            {
                "title": "Subsequent Routine Pushing",
                "code": "# Once upstream is established, simple shorthand works:\ngit push",
                "explanation": "Pushes current branch commits to its linked upstream."
            },
            {
                "title": "Pushing All Local Branches or Tags",
                "code": "# Push all local tags to remote:\ngit push origin --tags\n\n# Push all local branches:\ngit push --all origin",
                "explanation": "Publishes version release tags or multiple branches in batch."
            },
            {
                "title": "Safe Force-Pushing with Lease",
                "code": "# Safer force push that checks if remote was updated by a teammate:\ngit push --force-with-lease",
                "explanation": "Guarantees you don't inadvertently overwrite a coworker's pushed commits."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate First-Time Upstream Push",
            description="Write the command to push the local branch 'feature/payments' to remote 'origin' while setting it as the upstream tracking reference.",
            starter_code="# Write the git push command with upstream flag\n",
            solution_code="git push -u origin feature/payments",
            expected_output="Branch 'feature/payments' set up to track remote branch 'feature/payments' from 'origin'."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the purpose of the `-u` flag in `git push -u origin main`?",
                options=[
                    "It sets up an upstream tracking link so future `git push` and `git pull` calls know where to sync automatically",
                    "It unlocks unlimited cloud storage on GitHub",
                    "It uncompresses the commit files",
                    "It marks the commit as Urgent"
                ],
                correct_answer="It sets up an upstream tracking link so future `git push` and `git pull` calls know where to sync automatically",
                explanation="`-u` (short for `--set-upstream`) binds the local branch to the remote branch."
            ),
            QuizQuestionBlueprint(
                question="Why is `git push --force-with-lease` preferred over `git push --force`?",
                options=[
                    "It verifies whether teammates have pushed new commits to the remote branch before overwriting it, preventing accidental data loss",
                    "It costs less money on cloud hosting bills",
                    "It works without entering passwords",
                    "It only forces pushes on Fridays"
                ],
                correct_answer="It verifies whether teammates have pushed new commits to the remote branch before overwriting it, preventing accidental data loss",
                explanation="`--force-with-lease` aborts if the remote ref has moved past your local tracking ref."
            ),
            QuizQuestionBlueprint(
                question="What happens if you attempt a standard `git push` when the remote branch contains commits that your local branch does not have?",
                options=[
                    "Git rejects the push ('fetch first') because the update is non-fast-forward",
                    "Git automatically deletes the remote commits",
                    "Git crashes your terminal",
                    "Git converts your code into an email"
                ],
                correct_answer="Git rejects the push ('fetch first') because the update is non-fast-forward",
                explanation="Git protects remote history by preventing pushes that would orphan remote commits."
            ),
            QuizQuestionBlueprint(
                question="Which command pushes all local Git tags to the remote repository?",
                options=["git push origin --tags", "git push --all-tags", "git upload tags", "git tag --push"],
                correct_answer="git push origin --tags",
                explanation="Tags are not transferred during standard `git push`; `--tags` pushes them explicitly."
            ),
            QuizQuestionBlueprint(
                question="How do you delete a branch named 'feature-test' directly on the remote server?",
                options=["git push origin --delete feature-test", "git remote delete branch feature-test", "git erase feature-test", "git remote kill feature-test"],
                correct_answer="git push origin --delete feature-test",
                explanation="`git push <remote> --delete <branch>` deletes the ref on the remote host."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 21: Fetching vs Pulling (git fetch vs git pull)
    # ----------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Fetching vs Pulling (`git fetch` vs `git pull`)",
        concept="Understanding the vital architectural difference between safe read-only synchronization (`git fetch`) and aggressive fetch-plus-merge (`git pull`).",
        analogy="`git fetch` is like receiving a letter in your mailbox: the mail has arrived safely at your house, but you haven't opened it yet. `git pull` is like the mail carrier bursting through your front door and dumping the mail directly onto your dining room plate while you are eating.",
        theory_sections=[
            {
                "heading": "The Core Equation: Pull = Fetch + Merge",
                "body": (
                    "Many beginners assume `git pull` is the opposite of `git push`. In reality, `git pull` is a composite command:\n"
                    "$$\\text{git pull} = \\text{git fetch} + \\text{git merge}$$\n"
                    "Understanding this separation is essential for preventing unexpected merge conflicts."
                )
            },
            {
                "heading": "Why `git fetch` is 100% Safe",
                "body": (
                    "`git fetch` downloads all new commit objects, blobs, and branch references from the remote server into your local `.git` database. "
                    "However, it **never touches your working directory or active branch files**. "
                    "You can inspect what your coworkers did without altering a single line of your in-progress work."
                )
            },
            {
                "heading": "`git pull --rebase`",
                "body": (
                    "By default, `git pull` uses merge, creating unnecessary merge commits every time you sync with upstream. "
                    "Using `git pull --rebase` fetches remote changes and replays your local unpushed commits on top of the latest remote commits, "
                    "keeping project history clean and linear."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Safe Fetch and Review Workflow",
                "code": "# 1. Safely download all remote updates without modifying working files:\ngit fetch origin\n\n# 2. Inspect incoming commits from remote main before integrating:\ngit log HEAD..origin/main --oneline\n\n# 3. View exact diff between your local branch and remote:\ngit diff HEAD origin/main",
                "explanation": "Allows thorough review of remote changes before merging."
            },
            {
                "title": "Standard git pull",
                "code": "# Fetch and immediately merge remote changes into current branch:\ngit pull\n\n# Output confirms fetch + merge strategy (Fast-forward or 3-way):\n# Updating 7a4e8c1..4b2c1d0\n# Fast-forward",
                "explanation": "Composite command for direct integration."
            },
            {
                "title": "Linear History with git pull --rebase",
                "code": "# Fetch and rebase your local unpushed commits on top of incoming changes:\ngit pull --rebase origin main",
                "explanation": "Avoids messy merge bubble commits in team workflows."
            },
            {
                "title": "Setting Rebase as Global Default for Pull",
                "code": "# Configure Git to always use rebase whenever git pull is run:\ngit config --global pull.rebase true",
                "explanation": "Industry standard setting for clean Git graphs."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Pull Rebase and Safe Fetch",
            description="Set global config `pull.rebase` to `true`, and write the command to fetch updates from 'origin' safely without modifying working files.",
            starter_code="# Configure pull.rebase true and fetch from origin\n",
            solution_code="git config --global pull.rebase true\ngit fetch origin",
            expected_output="Config set and remote fetched"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does `git fetch` do to your active working directory files?",
                options=[
                    "Absolutely nothing; `git fetch` only updates the local database and remote tracking pointers without touching your working files",
                    "It overwrites all local files with remote versions",
                    "It deletes all uncommitted files",
                    "It prompts you with a merge conflict modal"
                ],
                correct_answer="Absolutely nothing; `git fetch` only updates the local database and remote tracking pointers without touching your working files",
                explanation="`git fetch` is safe and non-destructive; it never modifies your working tree."
            ),
            QuizQuestionBlueprint(
                question="What two operations are automatically performed when you run a standard `git pull`?",
                options=[
                    "`git fetch` followed immediately by `git merge`",
                    "`git add` followed by `git commit`",
                    "`git clone` followed by `git branch`",
                    "`git stash` followed by `git pop`"
                ],
                correct_answer="`git fetch` followed immediately by `git merge`",
                explanation="`git pull` combines downloading remote commits (fetch) with integrating them (merge)."
            ),
            QuizQuestionBlueprint(
                question="How does `git pull --rebase` improve project history compared to standard `git pull`?",
                options=[
                    "It replays your local unpushed commits on top of incoming remote commits, avoiding noisy merge commits and keeping history linear",
                    "It skips test execution",
                    "It compresses file sizes on disk",
                    "It encrypts your commit logs"
                ],
                correct_answer="It replays your local unpushed commits on top of incoming remote commits, avoiding noisy merge commits and keeping history linear",
                explanation="Rebase preserves a straight, readable single-line timeline."
            ),
            QuizQuestionBlueprint(
                question="Which command lets you view the commits present on `origin/main` that you do not yet have on your local `HEAD`?",
                options=["git log HEAD..origin/main --oneline", "git show --remote-only", "git list incoming", "git status --remote"],
                correct_answer="git log HEAD..origin/main --oneline",
                explanation="The double-dot revision range `HEAD..origin/main` displays commits in the remote ref missing locally."
            ),
            QuizQuestionBlueprint(
                question="Which configuration command enforces rebase as the default behavior for all future `git pull` calls?",
                options=["git config --global pull.rebase true", "git config --global merge.pull false", "git rebase --default", "git pull --set-default rebase"],
                correct_answer="git config --global pull.rebase true",
                explanation="Setting `pull.rebase true` prevents unnecessary merge commits upon pulling."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 22: Remote Tracking Branches
    # ----------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Remote Tracking Branches",
        concept="Understanding remote-tracking branches (`origin/main`), how they act as immutable local mirrors of remote server states, and tracking relationships.",
        analogy="A remote-tracking branch is like a photograph of your friend's whiteboard in another city. You cannot erase or draw on the photograph yourself (`origin/main` is read-only locally); you can only update the photo by fetching a new picture.",
        theory_sections=[
            {
                "heading": "What is a Remote-Tracking Branch?",
                "body": (
                    "Remote-tracking branches are references to the state of branches on remote repositories. "
                    "They take the format `<remote>/<branch>` (e.g. `origin/main` or `origin/feature-login`). "
                    "They live locally on your hard drive in `.git/refs/remotes/`, but they are **read-only bookmarks**. "
                    "You cannot check them out directly or commit to them; Git updates them automatically when you `fetch`, `pull`, or `push`."
                )
            },
            {
                "heading": "Tracking Relationships (Upstream)",
                "body": (
                    "When your local `main` is configured to track `origin/main`, `git status` can immediately inform you:\n"
                    "`\"Your branch is ahead of 'origin/main' by 2 commits, and behind by 1 commit\"`.\n"
                    "This informs you whether you need to push, pull, or reconcile diverged history."
                )
            },
            {
                "heading": "Pruning Stale Remote References (`git remote prune`)",
                "body": (
                    "When coworkers delete branches on GitHub, your local repository still retains their ghost remote tracking references. "
                    "Running `git fetch --prune` or `git remote prune origin` deletes these dead tracking branches locally."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Remote-Tracking Branches",
                "code": "# List all branches, highlighting remote-tracking references in red:\ngit branch -a\n# * main\n#   remotes/origin/HEAD -> origin/main\n#   remotes/origin/main\n#   remotes/origin/feature-auth",
                "explanation": "Reveals both local branches and cached remote-tracking pointers."
            },
            {
                "title": "Inspecting Behind/Ahead Status",
                "code": "# git status compares your local branch with its remote tracking branch:\ngit status\n\n# Output:\n# On branch main\n# Your branch is ahead of 'origin/main' by 1 commit.\n#   (use \"git push\" to publish your local commits)",
                "explanation": "Indicates unsynced commits in either direction."
            },
            {
                "title": "Checking Out a Remote Branch Automatically",
                "code": "# When checking out a branch that exists on origin but not locally:\ngit switch feature-auth\n\n# Git automatically creates a local branch and sets it to track origin/feature-auth:\n# Switched to a new branch 'feature-auth'\n# Branch 'feature-auth' set up to track remote branch 'feature-auth' from 'origin'.",
                "explanation": "Modern Git infers tracking configuration seamlessly."
            },
            {
                "title": "Pruning Deleted Remote Branches",
                "code": "# Clean up local ghost references for branches deleted on GitHub:\ngit fetch --prune\n\n# Output:\n#  - [deleted]         (none)     -> origin/feature-old-test",
                "explanation": "Synchronizes local remote refs with actual server state."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Tracking Branches and Prune",
            description="Run `git branch -vv` to view local branches with their upstream tracking branch and commit status.",
            starter_code="# Run git branch with verbose tracking info\n",
            solution_code="git branch -vv",
            expected_output="* main ... [origin/main] ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Can you directly commit new changes to a remote-tracking branch like `origin/main`?",
                options=[
                    "No, remote-tracking branches are read-only local bookmarks updated exclusively via fetch, pull, or push",
                    "Yes, you can edit them directly with Notepad",
                    "Yes, if you use `--force`",
                    "Only with admin rights on GitHub"
                ],
                correct_answer="No, remote-tracking branches are read-only local bookmarks updated exclusively via fetch, pull, or push",
                explanation="Remote-tracking branches reflect remote states and cannot be committed to locally."
            ),
            QuizQuestionBlueprint(
                question="What does it mean when `git status` reports 'Your branch is ahead of origin/main by 2 commits'?",
                options=[
                    "You have 2 commits saved locally that have not yet been pushed to the remote repository",
                    "The remote server has 2 new commits you need to download",
                    "Your computer is 2 hours ahead in time",
                    "Your code has 2 fatal bugs"
                ],
                correct_answer="You have 2 commits saved locally that have not yet been pushed to the remote repository",
                explanation="'Ahead' means local has new commits ready to be published via `git push`."
            ),
            QuizQuestionBlueprint(
                question="What does `git fetch --prune` do?",
                options=[
                    "Removes local remote-tracking branch references that have been deleted on the remote server",
                    "Deletes all your local branches",
                    "Deletes files older than 30 days",
                    "Empties the operating system trash bin"
                ],
                correct_answer="Removes local remote-tracking branch references that have been deleted on the remote server",
                explanation="Pruning removes local tracking refs for deleted remote branches."
            ),
            QuizQuestionBlueprint(
                question="Which flag passed to `git branch` displays upstream tracking relationships and commit disparity in brackets `[origin/main: ahead 1, behind 2]`?",
                options=["-vv", "-t", "--upstream-all", "-d"],
                correct_answer="-vv",
                explanation="`git branch -vv` shows local branches, commit hashes, and linked tracking branches."
            ),
            QuizQuestionBlueprint(
                question="Where are remote tracking branch references stored inside the repository filesystem?",
                options=[
                    "Inside `.git/refs/remotes/`",
                    "Inside `/tmp/remote/`",
                    "In the Windows Registry",
                    "On AWS S3"
                ],
                correct_answer="Inside `.git/refs/remotes/`",
                explanation="Remote refs are saved as plain text files in `.git/refs/remotes/<remote-name>/`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 23 (Project): Syncing Local & Remote Lab (End-to-End Workflow)
    # ----------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23 (Project): Syncing Local & Remote Lab (End-to-End Workflow)",
        concept="End-to-end practical mastery lab: simulating multi-developer collaboration, remote bare repositories, feature branches, pushing, pulling, and resolving sync discrepancies.",
        analogy="Today is the flight simulator where we put together everything learned in Modules 1-3. You will act as both Developer A and Developer B pushing and pulling to a shared central server without crashing the airplane.",
        theory_sections=[
            {
                "heading": "Lab Objective: Simulating Team Collaboration Locally",
                "body": (
                    "In this milestone lab, we simulate an entire production engineering workflow on our local machine using Git's DVCS power:\n"
                    "1. Instantiate a central bare repository (`central.git`) to simulate GitHub.\n"
                    "2. Clone it as **Developer Alice** and commit the foundational architecture.\n"
                    "3. Clone it as **Developer Bob**, add a feature branch, and push.\n"
                    "4. Have Alice fetch Bob's feature, review diffs, integrate, and verify."
                )
            },
            {
                "heading": "Key Competencies Tested",
                "body": (
                    "- Creating bare server repos (`git init --bare`).\n"
                    "- Cloning across local file paths.\n"
                    "- Configuring upstream branch tracking (`-u`).\n"
                    "- Using `git fetch` and inspecting remote branches.\n"
                    "- Fast-forward and 3-way integration."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Phase 1: Setting Up the Mock Central Server",
                "code": "# Create central bare repo acting as GitHub:\nmkdir /tmp/central.git\ncd /tmp/central.git\ngit init --bare",
                "explanation": "Creates bare server repository for multi-user collaboration."
            },
            {
                "title": "Phase 2: Alice Clones and Seeds Initial Project",
                "code": "# Alice clones and creates first commit:\ngit clone /tmp/central.git /tmp/alice_repo\ncd /tmp/alice_repo\necho 'console.log(\"App initialized\");' > app.js\ngit add app.js\ngit commit -m \"feat: initial application scaffolding\"\ngit branch -M main\ngit push -u origin main",
                "explanation": "Initializes project and pushes main branch to remote."
            },
            {
                "title": "Phase 3: Bob Clones and Pushes Feature",
                "code": "# Bob clones the central server:\ngit clone /tmp/central.git /tmp/bob_repo\ncd /tmp/bob_repo\ngit switch -c feature/login\necho 'export const login = () => true;' > auth.js\ngit add auth.js\ngit commit -m \"feat: implement login service\"\ngit push -u origin feature/login",
                "explanation": "Bob works on isolated branch and publishes upstream."
            },
            {
                "title": "Phase 4: Alice Fetches and Integrates Bob's Code",
                "code": "# Back in Alice's repo:\ncd /tmp/alice_repo\ngit fetch origin\ngit log HEAD..origin/feature/login --oneline\ngit merge origin/feature/login -m \"Merge Bob's login feature\"\ngit push origin main",
                "explanation": "Full fetch, review, merge, and deployment loop."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execute End-to-End Collaboration Script",
            description="Write the sequence of Git commands to fetch from remote 'origin', review remote log with `git log HEAD..origin/main --oneline`, and merge `origin/main`.",
            starter_code="# Fetch origin, inspect log range, and merge origin/main\n",
            solution_code="git fetch origin\ngit log HEAD..origin/main --oneline\ngit merge origin/main",
            expected_output="Updating ...\nFast-forward"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `git init --bare` used to create the central mock server in collaboration labs?",
                options=[
                    "Bare repositories do not have working directory trees, making them safe push targets for multiple developers",
                    "Bare repositories are free while regular repos cost money",
                    "Bare repos automatically host a web server on port 80",
                    "Bare repos convert JavaScript to Python"
                ],
                correct_answer="Bare repositories do not have working directory trees, making them safe push targets for multiple developers",
                explanation="Pushing to non-bare repos with checked-out files can cause index corruption."
            ),
            QuizQuestionBlueprint(
                question="When Developer Alice runs `git fetch origin`, can she see Developer Bob's newly pushed branch?",
                options=[
                    "Yes, Bob's branch becomes available locally as `origin/feature/login`",
                    "No, Alice must re-clone the entire repository",
                    "Only if Bob emails Alice his password",
                    "Only if Alice reboots her machine"
                ],
                correct_answer="Yes, Bob's branch becomes available locally as `origin/feature/login`",
                explanation="`git fetch` pulls in all new branches and commits published by teammates."
            ),
            QuizQuestionBlueprint(
                question="What revision range syntax displays the exact commits Bob introduced that Alice does not yet have?",
                options=["HEAD..origin/feature/login", "HEAD - origin", "HEAD && origin", "origin % HEAD"],
                correct_answer="HEAD..origin/feature/login",
                explanation="The `A..B` syntax lists commits reachable from B but not from A."
            ),
            QuizQuestionBlueprint(
                question="In modern trunk-based and feature-branch collaboration, what is the best practice after your feature branch is merged into `main`?",
                options=[
                    "Delete the feature branch both locally and on the remote to maintain repository cleanliness",
                    "Never touch the repository again",
                    "Keep all branches forever to show how much work was done",
                    "Rename all files to `.bak`"
                ],
                correct_answer="Delete the feature branch both locally and on the remote to maintain repository cleanliness",
                explanation="Deleting merged branches keeps lists uncluttered and minimizes confusion."
            ),
            QuizQuestionBlueprint(
                question="What happens if Bob attempts to push to `main` while Alice has already pushed new commits to `main`?",
                options=[
                    "Bob's push is rejected; he must first fetch/pull Alice's commits and reconcile history",
                    "Alice's work is permanently deleted from the server",
                    "The server automatically creates a fork",
                    "Bob's computer will lock up"
                ],
                correct_answer="Bob's push is rejected; he must first fetch/pull Alice's commits and reconcile history",
                explanation="Git protects remote history by enforcing non-fast-forward push rejection."
            )
        ],
        is_project_day=True,
        project_name="Syncing Local & Remote Lab (End-to-End Workflow)"
    ),

    # ----------------------------------------------------
    # Day 24: Unstaging Files (git restore --staged / git reset HEAD)
    # ----------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Unstaging Files (`git restore --staged` / `git reset HEAD`)",
        concept="Safely removing mistakenly staged files from the Index without losing or altering changes in the working directory.",
        analogy="You accidentally packed your passport into a suitcase that you only meant to pack socks into. Unstaging is taking the passport out of the suitcase and setting it back on your bedroom desk. The passport is not shredded or lost; it is just no longer in the suitcase.",
        theory_sections=[
            {
                "heading": "The Need to Unstage",
                "body": (
                    "It is extremely common to accidentally run `git add .` and realize you staged a temporary debug script, a secret credentials file, "
                    "or an unfinished feature. You need to pull that file back out of the Staging Area (Index) without destroying the code you wrote in your working directory."
                )
            },
            {
                "heading": "The Modern Command: `git restore --staged`",
                "body": (
                    "Git 2.23 introduced `git restore` to replace ambiguous uses of `git reset`. "
                    "Running `git restore --staged <file>` copies the file's state from `HEAD` into the Index, "
                    "leaving your working directory file untouched."
                )
            },
            {
                "heading": "The Legacy Command: `git reset HEAD <file>`",
                "body": (
                    "In older versions of Git, the command `git reset HEAD <file>` achieved the exact same result. "
                    "You will encounter `git reset HEAD` in older guides and scripts."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Unstaging a Single File (Modern Syntax)",
                "code": "# 1. Accidentally stage secret file:\ngit add .env\n\n# 2. Safely unstage it using modern git restore:\ngit restore --staged .env\n\n# Status shows .env is back to untracked/unstaged state:\ngit status -s\n# ?? .env",
                "explanation": "Modern, explicit command to remove a file from the index."
            },
            {
                "title": "Unstaging All Staged Files at Once",
                "code": "# Remove everything from staging without affecting working tree:\ngit restore --staged .\n# Or legacy syntax:\n# git reset HEAD",
                "explanation": "Empties the staging index in a single operation."
            },
            {
                "title": "Legacy Unstaging with git reset HEAD",
                "code": "# Classic syntax still supported in all Git versions:\ngit reset HEAD src/debug.py",
                "explanation": "Points the index back to HEAD for that file."
            },
            {
                "title": "Verifying Working Directory Preservation",
                "code": "# Confirm that un-staged file still retains your written code:\ncat .env\n# PORT=3000\n# DB_PASS=secret",
                "explanation": "The file on disk remains completely untouched."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Stage and Safely Unstage File",
            description="Create file 'temp.log', stage it with `git add`, and use `git restore --staged` to unstage it safely.",
            starter_code="# Create temp.log, stage it, and unstage using git restore --staged\n",
            solution_code="echo 'temp data' > temp.log\ngit add temp.log\ngit restore --staged temp.log",
            expected_output="File removed from staging index"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does `git restore --staged <file>` do to the content of the file on your hard drive?",
                options=[
                    "It leaves the file on your hard drive completely unchanged; it only removes it from the staging index",
                    "It deletes the file from disk permanently",
                    "It reverts the file to an empty 0-byte file",
                    "It renames the file to `.bak`"
                ],
                correct_answer="It leaves the file on your hard drive completely unchanged; it only removes it from the staging index",
                explanation="`--staged` targets only the index, preserving working tree edits."
            ),
            QuizQuestionBlueprint(
                question="What was the primary command used for unstaging files before Git 2.23 introduced `git restore`?",
                options=["git reset HEAD <file>", "git unstage <file>", "git remove --index <file>", "git drop <file>"],
                correct_answer="git reset HEAD <file>",
                explanation="`git reset HEAD <file>` was the traditional way to copy HEAD's version into index."
            ),
            QuizQuestionBlueprint(
                question="How can you unstage ALL currently staged files in the repository simultaneously?",
                options=["git restore --staged .", "git clear index", "git drop --all", "git empty stage"],
                correct_answer="git restore --staged .",
                explanation="Passing `.` unstages all files in the current directory and subdirectories."
            ),
            QuizQuestionBlueprint(
                question="If you accidentally run `git add secret_password.txt`, what is the best immediate command to run?",
                options=[
                    "git restore --staged secret_password.txt",
                    "git commit -m 'delete password'",
                    "git push --force",
                    "format C:"
                ],
                correct_answer="git restore --staged secret_password.txt",
                explanation="Unstaging immediately removes the file from the pending commit snapshot."
            ),
            QuizQuestionBlueprint(
                question="Which Git tree does `git restore --staged` modify?",
                options=["The Staging Area (Index)", "The Working Directory", "The Remote Repository", "The Git Commit History"],
                correct_answer="The Staging Area (Index)",
                explanation="The command specifically updates the Index tree."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 25: Discarding Working Dir Changes (git restore)
    # ----------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Discarding Working Dir Changes (`git restore`)",
        concept="Reverting dirty local modifications in the working tree back to the last committed state using `git restore` (and legacy `git checkout --`).",
        analogy="You are writing an essay with pencil on paper, realize your last three paragraphs make no sense, and want to erase them back to where you were this morning. `git restore` is that heavy-duty eraser.",
        theory_sections=[
            {
                "heading": "The Danger of Discarding Working Directory Changes",
                "body": (
                    "Unlike commits and staged files which are recorded in Git's object database, **uncommitted changes in your working directory exist only in memory/disk**. "
                    "When you tell Git to discard them, **they are permanently destroyed and cannot be recovered via Git history**. "
                    "Always exercise extreme caution before discarding working directory edits."
                )
            },
            {
                "heading": "The Modern Command: `git restore <file>`",
                "body": (
                    "`git restore <file>` overwrites the specified file in your working directory with the version currently in the Index (or HEAD). "
                    "All unstaged edits in that file vanish."
                )
            },
            {
                "heading": "Legacy Syntax: `git checkout -- <file>`",
                "body": (
                    "Historically, developers ran `git checkout -- <file>`. "
                    "The double-dash `--` was required to tell Git: 'the following argument is a file path, not a branch name'."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Discarding Changes in a Single File",
                "code": "# You made bad edits to app.py and want to discard them:\ngit restore app.py\n\n# app.py is immediately restored to the clean version matching HEAD/Index",
                "explanation": "Overwrites working tree file with clean index version."
            },
            {
                "title": "Discarding All Unstaged Changes in Entire Project",
                "code": "# Discard all unstaged changes across all files in current directory:\ngit restore .\n\n# Caution: Permanently deletes all unstaged edits!",
                "explanation": "Restores all tracked files to pristine state."
            },
            {
                "title": "Legacy Syntax with Double-Dash",
                "code": "# Classic checkout syntax:\ngit checkout -- app.py\ngit checkout -- .",
                "explanation": "Legacy equivalent of git restore."
            },
            {
                "title": "Interactive Discard with Patch Mode",
                "code": "# Interactively discard only specific lines/hunks from a file:\ngit restore -p app.py",
                "explanation": "Allows selectively undoing some lines while keeping others."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Modify File and Discard Changes",
            description="Assume 'main.py' is tracked. Append 'broken code' to it, and use `git restore` to discard the unstaged modification.",
            starter_code="# Append broken text and discard with git restore\n",
            solution_code="echo 'broken code' >> main.py\ngit restore main.py",
            expected_output="Working directory clean"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Can uncommitted working directory changes discarded via `git restore <file>` be recovered using Git history?",
                options=[
                    "No, because uncommitted changes were never recorded in Git's database, they are permanently erased",
                    "Yes, through `git reflog`",
                    "Yes, by calling `git undo`",
                    "Yes, from the `.git/trash` directory"
                ],
                correct_answer="No, because uncommitted changes were never recorded in Git's database, they are permanently erased",
                explanation="Git can only recover data that was committed or staged at least once."
            ),
            QuizQuestionBlueprint(
                question="What was the purpose of the `--` double-dash in legacy `git checkout -- <filename>`?",
                options=[
                    "It tells Git that the string following it is a file path, preventing ambiguity if a branch shares the same name",
                    "It encrypts the checkout",
                    "It forces Git to delete the file",
                    "It enables double-speed checkout"
                ],
                correct_answer="It tells Git that the string following it is a file path, preventing ambiguity if a branch shares the same name",
                explanation="The `--` separator separates flags/refs from pathspecs."
            ),
            QuizQuestionBlueprint(
                question="Which flag allows interactively choosing which specific lines to discard from a file?",
                options=["-p (or --patch)", "-i", "--select", "-s"],
                correct_answer="-p (or --patch)",
                explanation="`git restore -p` prompts you for each hunk so you can discard selectively."
            ),
            QuizQuestionBlueprint(
                question="What does `git restore .` do in a dirty working directory with unstaged edits in tracked files?",
                options=[
                    "Discards all unstaged modifications across all tracked files in the current directory and subdirectories",
                    "Commits everything to main",
                    "Stashes changes into a zip file",
                    "Pushes changes to GitHub"
                ],
                correct_answer="Discards all unstaged modifications across all tracked files in the current directory and subdirectories",
                explanation="`git restore .` resets all tracked files in the working directory."
            ),
            QuizQuestionBlueprint(
                question="Does `git restore .` delete brand-new UNTRACKED files on disk?",
                options=[
                    "No, `git restore` only operates on tracked files; untracked files are untouched (use `git clean` to delete untracked files)",
                    "Yes, it deletes all files on disk",
                    "Only if they are empty",
                    "Only on Windows"
                ],
                correct_answer="No, `git restore` only operates on tracked files; untracked files are untouched (use `git clean` to delete untracked files)",
                explanation="Untracked files are not known to Git; removing them requires `git clean`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 26: Amending Commits (git commit --amend)
    # ----------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Amending Commits (`git commit --amend`)",
        concept="Modifying the most recent commit to fix typos, include forgotten staged files, or revise commit messages without creating ugly 'fix typo' micro-commits.",
        analogy="You mailed a birthday card, but before the mail truck drove away, you realized you forgot to slip a $20 bill inside and misspelled your friend's name on the envelope. `--amend` lets you pull the letter back, put the $20 in, write a clean new envelope, and seal it.",
        theory_sections=[
            {
                "heading": "The Purpose of `--amend`",
                "body": (
                    "Every developer knows the frustration of committing, only to realize 3 seconds later that they forgot to format a file, "
                    "left in a `console.log`, or made an embarrassing typo in the commit subject. "
                    "`git commit --amend` replaces the tip commit with a new commit combining the previous commit and your newly staged changes."
                )
            },
            {
                "heading": "Under the Hood: Amending Creates a Brand-New Commit",
                "body": (
                    "Git commits are immutable. Amending does not actually edit the old commit object in-place. "
                    "Instead, Git generates an entirely **new commit object** with a **different SHA-1 hash** and points your branch pointer to it. "
                    "The old commit becomes an orphan (eventually collected by GC)."
                )
            },
            {
                "heading": "The Golden Rule of Amending",
                "body": (
                    "**Never amend a commit that has already been pushed to a shared public remote branch!** "
                    "Because amending changes the SHA-1 hash, pushing an amended commit requires a force-push, "
                    "which desynchronizes coworker clones and causes chaos."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Fixing Just the Commit Message",
                "code": "# Change the message of your last commit without modifying any files:\ngit commit --amend -m \"feat: implement OAuth2 authentication with Google\"",
                "explanation": "Rewrites the commit subject/body cleanly."
            },
            {
                "title": "Adding a Forgotten Staged File to Last Commit",
                "code": "# 1. Stage the file you forgot:\ngit add forgotten_style.css\n\n# 2. Fold it into the previous commit without changing the message:\ngit commit --amend --no-edit\n\n# Output confirms files updated under same commit message:\n# [main 9c8b7a1] feat: build header navbar\n#  2 files changed, 40 insertions(+)",
                "explanation": "`--no-edit` retains existing commit message."
            },
            {
                "title": "Verifying Hash Change After Amend",
                "code": "# Compare commit SHA before and after amend:\ngit log -n 1 --oneline\n# Notice the hash changed from 7a4e8c1 to 9c8b7a1",
                "explanation": "Demonstrates that amending creates a brand new commit object."
            },
            {
                "title": "Recovering Original Pre-Amend Commit via Reflog",
                "code": "# If you made a mistake during amend, reflog has your old commit:\ngit reflog\n# 9c8b7a1 HEAD@{0}: commit (amend): ...\n# 7a4e8c1 HEAD@{1}: commit: ...",
                "explanation": "Git keeps the pre-amend commit safe in the reflog."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Amend Most Recent Commit Without Editing Message",
            description="Stage a new file 'extra.txt' and fold it into the previous commit using `git commit --amend --no-edit`.",
            starter_code="# Stage extra.txt and run amend with --no-edit\n",
            solution_code="echo 'extra' > extra.txt\ngit add extra.txt\ngit commit --amend --no-edit",
            expected_output="[main ...] ...\n Date: ...\n 1 file changed, 1 insertion(+)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens under the hood to the SHA-1 hash when you run `git commit --amend`?",
                options=[
                    "A brand-new commit object with a different SHA-1 hash is generated, replacing the previous commit",
                    "The old commit object's bytes are edited in place while keeping the exact same hash",
                    "The hash is reset to all zeroes",
                    "Git deletes all hashes permanently"
                ],
                correct_answer="A brand-new commit object with a different SHA-1 hash is generated, replacing the previous commit",
                explanation="Git commits are cryptographically immutable; amending always produces a new commit."
            ),
            QuizQuestionBlueprint(
                question="Which flag allows you to add staged files to the last commit without re-opening the text editor or changing the commit message?",
                options=["--no-edit", "--quick", "--silent", "--skip-message"],
                correct_answer="--no-edit",
                explanation="`--no-edit` retains the existing commit log message intact."
            ),
            QuizQuestionBlueprint(
                question="Why is amending commits that have already been pushed to a shared remote considered dangerous?",
                options=[
                    "Because it alters the commit hash, requiring a disruptive force-push that corrupts teammates' branch histories",
                    "Because GitHub disables accounts that amend commits",
                    "Because it slows down computer performance",
                    "Because it converts private repos into public ones"
                ],
                correct_answer="Because it alters the commit hash, requiring a disruptive force-push that corrupts teammates' branch histories",
                explanation="Rewriting public history causes non-fast-forward divergence for collaborators."
            ),
            QuizQuestionBlueprint(
                question="Can you use `git commit --amend` to modify a commit that occurred 5 commits ago?",
                options=[
                    "No, `--amend` strictly modifies only the single most recent commit (HEAD)",
                    "Yes, by passing `--depth 5`",
                    "Yes, by passing `-n 5`",
                    "Yes, if you are root administrator"
                ],
                correct_answer="No, `--amend` strictly modifies only the single most recent commit (HEAD)",
                explanation="`--amend` only touches HEAD; modifying older commits requires interactive rebase."
            ),
            QuizQuestionBlueprint(
                question="If you accidentally break your code during an amend, where can you find the hash of the pre-amended commit to recover it?",
                options=["Inside `git reflog`", "In the browser cookies", "In the bash history", "It cannot be found anywhere"],
                correct_answer="Inside `git reflog`",
                explanation="`git reflog` records all movements of HEAD, including before and after amend operations."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 27: Deep dive into git reset (--soft, --mixed, --hard)
    # ----------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Deep dive into `git reset` (`--soft`, `--mixed`, `--hard`)",
        concept="Mastering Git's most potent time-machine command by understanding how `--soft`, `--mixed`, and `--hard` manipulate the Three Trees (HEAD, Index, Working Directory).",
        analogy="Imagine your project history as three concentric rooms: the Vault (Commit History), the Packaging Room (Staging Index), and the Workshop (Working Directory).\n- `--soft`: Moves the Vault pointer back, leaves packages ready to ship.\n- `--mixed`: Moves Vault pointer back and unpacks the packages onto the workshop tables.\n- `--hard`: Moves Vault pointer back, burns the packages, and sweeps the workshop tables completely clean.",
        theory_sections=[
            {
                "heading": "The Power of `git reset`",
                "body": (
                    "`git reset` moves the current branch pointer backward along the commit chain. "
                    "The key question is: what should happen to the changes that were in those undone commits? "
                    "The three flags (`--soft`, `--mixed`, `--hard`) provide the answer."
                )
            },
            {
                "heading": "Comparing the Three Modes",
                "body": (
                    "1. `git reset --soft HEAD~1`:\n"
                    "   - Moves HEAD and branch pointer back 1 commit.\n"
                    "   - **Staging Index**: Untouched (changes remain staged).\n"
                    "   - **Working Directory**: Untouched.\n"
                    "   - Perfect for: Redoing a commit message or grouping several commits together.\n\n"
                    "2. `git reset --mixed HEAD~1` (Default if no flag passed):\n"
                    "   - Moves HEAD and branch pointer back 1 commit.\n"
                    "   - **Staging Index**: Reset to match destination commit (unstages changes).\n"
                    "   - **Working Directory**: Untouched (your written code is completely safe on disk).\n"
                    "   - Perfect for: Splitting a commit into multiple smaller commits.\n\n"
                    "3. `git reset --hard HEAD~1`:\n"
                    "   - Moves HEAD and branch pointer back 1 commit.\n"
                    "   - **Staging Index**: Reset.\n"
                    "   - **Working Directory**: Reset (destroys all code written in those commits).\n"
                    "   - **DANGER**: Completely discards work!"
                )
            },
            {
                "heading": "Relative Revision Syntax: `HEAD~1` vs `HEAD^`",
                "body": (
                    "- `HEAD~1` (or `HEAD^`): 1 commit before HEAD.\n"
                    "- `HEAD~3`: 3 commits before HEAD."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Using --soft to Squash or Redo Commit",
                "code": "# Undo last commit, keeping all changes staged ready to commit:\ngit reset --soft HEAD~1\n\ngit status\n# Changes to be committed: (Files are green and staged)",
                "explanation": "Allows instantly modifying or adding to the commit."
            },
            {
                "title": "Using --mixed (Default) to Unstage and Restructure",
                "code": "# Undo last commit and unstage changes (code is safe on disk):\ngit reset --mixed HEAD~1\n# Or simply: git reset HEAD~1\n\ngit status\n# Changes not staged for commit: (Files are red and unstaged)",
                "explanation": "Default behavior: code stays in working directory."
            },
            {
                "title": "Using --hard to Completely Obliterate Commits",
                "code": "# Nuclear option: completely wipe out the last 2 commits and disk changes:\ngit reset --hard HEAD~2\n\n# Output confirms HEAD pointer shifted:\n# HEAD is now at 7a4e8c1 feat: base setup",
                "explanation": "DANGER: Destroys both staging index and working tree edits."
            },
            {
                "title": "Undoing an Accidental --hard Reset via Reflog",
                "code": "# If you ran --hard by mistake, rescue it immediately:\ngit reflog\n# 7a4e8c1 HEAD@{0}: reset: moving to HEAD~2\n# b3c2a1d HEAD@{1}: commit: valuable work\n\n# Restore back to the lost commit:\ngit reset --hard b3c2a1d",
                "explanation": "Reflog can recover committed work even after --hard reset."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Perform Soft Reset on HEAD",
            description="Run `git reset --soft HEAD~1` to step back one commit while keeping changes staged.",
            starter_code="# Execute soft reset to previous commit\n",
            solution_code="git reset --soft HEAD~1",
            expected_output="HEAD is now at ... (changes staged in index)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens to your working directory files when you run `git reset --soft HEAD~1`?",
                options=[
                    "Your files remain completely untouched, and the changes from the undone commit remain staged in the index",
                    "All your files are deleted permanently",
                    "Your files are unstaged and converted to text",
                    "Your branch is deleted"
                ],
                correct_answer="Your files remain completely untouched, and the changes from the undone commit remain staged in the index",
                explanation="`--soft` only shifts the branch/HEAD pointer; index and working tree remain intact."
            ),
            QuizQuestionBlueprint(
                question="What is the default mode of `git reset` if no flag (`--soft`, `--mixed`, `--hard`) is specified?",
                options=["--mixed", "--soft", "--hard", "--delete"],
                correct_answer="--mixed",
                explanation="Running `git reset HEAD~1` defaults to `--mixed` mode."
            ),
            QuizQuestionBlueprint(
                question="Which mode of `git reset` destroys uncommitted changes in your working directory and overwrites tracked files?",
                options=["--hard", "--soft", "--mixed", "--clean"],
                correct_answer="--hard",
                explanation="`--hard` overwrites both the Index and the Working Directory."
            ),
            QuizQuestionBlueprint(
                question="What does the syntax `HEAD~2` specify?",
                options=[
                    "Two commits prior to the current HEAD commit along the primary ancestor path",
                    "Two branches away from HEAD",
                    "Two files inside HEAD",
                    "HEAD multiplied by 2"
                ],
                correct_answer="Two commits prior to the current HEAD commit along the primary ancestor path",
                explanation="`~N` moves back N generations of parent commits."
            ),
            QuizQuestionBlueprint(
                question="If you accidentally run `git reset --hard` and lose a commit, what tool lets you find the lost commit hash to recover it?",
                options=["`git reflog`", "`git trash`", "`git undo`", "`git rescue`"],
                correct_answer="`git reflog`",
                explanation="`git reflog` tracks HEAD moves, allowing recovery of orphaned commits."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 28: Reverting Commits (git revert - safe public undo)
    # ----------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Reverting Commits (`git revert` - safe public undo)",
        concept="Safely undoing mistakes on public shared branches by generating an inverse compensating commit rather than rewriting historical graphs.",
        analogy="In accounting, if an accountant accidentally enters '+$500', they are legally forbidden from erasing the ledger page. Instead, they make a new entry '-$500' to negate the error while keeping the audit trail transparent. `git revert` is that legal accounting entry.",
        theory_sections=[
            {
                "heading": "Reset vs Revert: The Public History Rule",
                "body": (
                    "When you make a mistake locally on your private branch, `git reset` is fine because nobody else has those commits. "
                    "However, if you push a buggy commit to a shared team branch (like `main`), using `git reset` rewrites history, breaks teammates' repos, "
                    "and requires an aggressive force push.\n"
                    "The professional, safe solution is `git revert`."
                )
            },
            {
                "heading": "How `git revert` Operates",
                "body": (
                    "`git revert <commit-hash>` does not delete the target commit. "
                    "Instead, it calculates the exact opposite diff (insertions become deletions, deletions become insertions) "
                    "and creates a brand-new commit that undoes the unwanted changes while moving the timeline **forward**."
                )
            },
            {
                "heading": "Reverting Merge Commits (`-m`)",
                "body": (
                    "Because merge commits have two parents, Git cannot guess which parent branch line you wish to keep as mainline. "
                    "To revert a merge commit, you must pass `-m 1` (or `-m 2`) to declare the mainline parent."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reverting the Most Recent Commit Safely",
                "code": "# Safely negate the changes introduced in HEAD on shared branch:\ngit revert HEAD\n\n# Git opens editor with pre-filled message:\n# Revert \"feat: broken payment gateway\"\n# This reverts commit a1b2c3d4e5f...",
                "explanation": "Creates an inverse commit without modifying historical commits."
            },
            {
                "title": "Reverting a Specific Historical Commit Without Prompt",
                "code": "# Revert an older commit by hash without prompting for editor confirmation:\ngit revert --no-edit 7a4e8c1\n\n# Output confirms new commit created:\n# [main e9d8c7b] Revert \"feat: problematic feature\"\n#  1 file changed, 5 deletions(-)",
                "explanation": "`--no-edit` uses default revert commit message."
            },
            {
                "title": "Reverting Multiple Commits in Batch",
                "code": "# Revert range of commits without committing each individually (-n / --no-commit):\ngit revert -n HEAD~3..HEAD\n\n# Now stage and create one single clean rollback commit:\ngit commit -m \"rollback: revert unstable features from sprint 24\"",
                "explanation": "Stages inverse changes into working directory and index."
            },
            {
                "title": "Reverting a 2-Parent Merge Commit",
                "code": "# Revert a merge commit specifying parent 1 (mainline) as base:\ngit revert -m 1 4b2c1d0",
                "explanation": "The `-m 1` flag designates parent 1 as the mainline."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execute Safe git revert",
            description="Run `git revert --no-edit HEAD` to safely undo the latest commit with an inverse commit.",
            starter_code="# Revert the HEAD commit without opening text editor\n",
            solution_code="git revert --no-edit HEAD",
            expected_output="[main ...] Revert \"...\"\n 1 file changed, ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `git revert` considered safe for shared public branches while `git reset` is dangerous?",
                options=[
                    "`git revert` creates a new forward commit that negates changes without rewriting or destroying past history",
                    "`git revert` runs 10x faster",
                    "`git revert` automatically tests the code before running",
                    "`git revert` disables git push security checks"
                ],
                correct_answer="`git revert` creates a new forward commit that negates changes without rewriting or destroying past history",
                explanation="Revert appends a new compensating commit, avoiding history rewrites."
            ),
            QuizQuestionBlueprint(
                question="What does `git revert` do to the original buggy commit in your repository history?",
                options=[
                    "It leaves the original commit untouched in history and appends a new inverse commit",
                    "It deletes the original commit permanently",
                    "It zeroes out the original author's name",
                    "It marks the commit as private"
                ],
                correct_answer="It leaves the original commit untouched in history and appends a new inverse commit",
                explanation="Git history remains completely immutable and intact."
            ),
            QuizQuestionBlueprint(
                question="What does the `--no-edit` flag do during a `git revert`?",
                options=[
                    "Accepts the default generated commit message (e.g. 'Revert \"title\"') without opening your text editor",
                    "Prevents the commit from being reverted",
                    "Skips file modifications",
                    "Deletes all commit notes"
                ],
                correct_answer="Accepts the default generated commit message (e.g. 'Revert \"title\"') without opening your text editor",
                explanation="`--no-edit` automatically applies the standard revert message."
            ),
            QuizQuestionBlueprint(
                question="Why must you pass the `-m` flag (e.g., `git revert -m 1 <hash>`) when reverting a merge commit?",
                options=[
                    "Because merge commits have multiple parents, and Git needs to know which parent branch to treat as the mainline to preserve",
                    "Because merge commits are larger than 1MB",
                    "Because it stands for 'mandatory'",
                    "To send an email notification to the author"
                ],
                correct_answer="Because merge commits have multiple parents, and Git needs to know which parent branch to treat as the mainline to preserve",
                explanation="The `-m <parent-number>` tells Git which parent represents the mainline."
            ),
            QuizQuestionBlueprint(
                question="What does the `-n` (or `--no-commit`) flag do in `git revert -n <hash>`?",
                options=[
                    "Applies the inverse changes to the staging area and working directory without automatically creating the commit",
                    "Cancels the revert operation",
                    "Reverts only numerical values",
                    "Deletes the commit without staging"
                ],
                correct_answer="Applies the inverse changes to the staging area and working directory without automatically creating the commit",
                explanation="`-n` stages the inverse changes, allowing you to combine multiple reverts into one."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 29: Git Stash (Saving & popping temporary work)
    # ----------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Git Stash (Saving & popping temporary work)",
        concept="Shelving uncommitted, half-finished modifications on an internal stack using `git stash` to clean your working tree for urgent hotfixes.",
        analogy="You are cooking a complex three-course meal when your smoke alarm goes off. You don't throw your food in the trash; you put the chopped ingredients into a Tupperware container in the fridge (`stash`), handle the fire alarm, and then pull the Tupperware back out (`stash pop`) to resume cooking exactly where you left off.",
        theory_sections=[
            {
                "heading": "Why Use Git Stash?",
                "body": (
                    "You are in the middle of building a feature with 4 half-edited files when your team lead calls: an emergency bug has broken production "
                    "and you must switch to `main` immediately to deploy a fix. "
                    "Git will refuse to let you switch branches with conflicting dirty edits. "
                    "You don't want to make an embarrassing 'wip half finished junk' commit. "
                    "`git stash` saves your dirty working directory and staging area onto a local stack and cleans your workspace."
                )
            },
            {
                "heading": "The Stash Stack Architecture",
                "body": (
                    "Git stores stashes in a Last-In, First-Out (LIFO) stack referenced by index:\n"
                    "- `stash@{0}`: The most recently stashed changes.\n"
                    "- `stash@{1}`: The second most recently stashed changes.\n"
                    "- `git stash pop`: Applies `stash@{0}` and immediately drops it from the stack.\n"
                    "- `git stash apply`: Applies `stash@{0}` but keeps it on the stack for safety."
                )
            },
            {
                "heading": "Stashing Untracked Files (`-u` / `--include-untracked`)",
                "body": (
                    "By default, `git stash` only stores tracked modified files. Brand new files you haven't yet added will be ignored and left in your directory. "
                    "Always use `git stash -u` (or `git stash -a` for all files including ignored) to ensure a truly pristine workspace."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Basic Stash with Descriptive Message",
                "code": "# Stash all modified AND untracked files with a clear label:\ngit stash push -u -m \"WIP: half-finished cart checkout logic\"\n\n# Output confirms working tree is clean:\n# Saved working directory and index state On feature/cart: WIP: half-finished...\ngit status\n# nothing to commit, working tree clean",
                "explanation": "Labels the stash and cleans the working tree."
            },
            {
                "title": "Listing and Inspecting Saved Stashes",
                "code": "# List all stashes stored on the stack:\ngit stash list\n# stash@{0}: On feature/cart: WIP: half-finished cart checkout logic\n\n# Inspect diff inside a stash without applying it:\ngit stash show -p stash@{0}",
                "explanation": "Views diffs stored in the stash stack."
            },
            {
                "title": "Restoring Work via Pop vs Apply",
                "code": "# Apply and remove top stash from stack:\ngit stash pop\n\n# Or apply without removing from stack:\ngit stash apply stash@{0}",
                "explanation": "`pop` cleans up the stack; `apply` retains it."
            },
            {
                "title": "Dropping or Clearing Stashes",
                "code": "# Delete a specific stash:\ngit stash drop stash@{0}\n\n# Clear all stashes on your machine:\ngit stash clear",
                "explanation": "Cleans up stash inventory."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Stash Untracked Work and Restore",
            description="Create an untracked file 'draft.py', stash it with `-u -m \"wip draft\"`, verify status is clean, and restore with `git stash pop`.",
            starter_code="# Create draft.py, stash with -u, verify clean, pop stash\n",
            solution_code="echo 'draft' > draft.py\ngit stash push -u -m \"wip draft\"\ngit status\ngit stash pop",
            expected_output="Saved working directory...\nnothing to commit, working tree clean\nDropped refs/stash@{0}..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between `git stash pop` and `git stash apply`?",
                options=[
                    "`git stash pop` applies the changes and deletes them from the stash list; `git stash apply` applies changes but preserves them in the stash list",
                    "`git stash pop` deletes changes without applying them",
                    "`git stash apply` requires a password",
                    "`git stash pop` only works on Linux"
                ],
                correct_answer="`git stash pop` applies the changes and deletes them from the stash list; `git stash apply` applies changes but preserves them in the stash list",
                explanation="`pop` = `apply` + `drop` in a single command."
            ),
            QuizQuestionBlueprint(
                question="Why must you pass the `-u` (or `--include-untracked`) flag to `git stash` when you have created new files?",
                options=[
                    "By default, `git stash` only stashes tracked modified files; untracked new files are left behind unless `-u` is passed",
                    "To enable encryption",
                    "To upload the stash to GitHub",
                    "To automatically commit the files"
                ],
                correct_answer="By default, `git stash` only stashes tracked modified files; untracked new files are left behind unless `-u` is passed",
                explanation="Without `-u`, newly created untracked files remain in the working tree."
            ),
            QuizQuestionBlueprint(
                question="Which data structure does Git use internally to hold multiple saved stashes?",
                options=["A LIFO (Last-In, First-Out) stack", "A FIFO queue", "A binary search tree", "A relational database"],
                correct_answer="A LIFO (Last-In, First-Out) stack",
                explanation="The most recent stash is placed at index 0 (`stash@{0}`)."
            ),
            QuizQuestionBlueprint(
                question="Which command inspects the exact code diff inside a saved stash without applying it to your files?",
                options=["git stash show -p stash@{0}", "git view stash", "git diff-stash", "git inspect stash"],
                correct_answer="git stash show -p stash@{0}",
                explanation="`git stash show -p` prints the full patch diff of the stash."
            ),
            QuizQuestionBlueprint(
                question="Which command permanently empties and deletes all stashes currently saved on the stack?",
                options=["git stash clear", "git stash destroy --all", "git stash wipe", "git stash purge"],
                correct_answer="git stash clear",
                explanation="`git stash clear` deletes the entire stash history."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 30: Git Rebase (Clean linear history)
    # ----------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: Git Rebase (Clean linear history)",
        concept="Replaying commits onto a new base tip to eliminate diamond merge histories and maintain pristine linear project logs.",
        analogy="Imagine your feature branch was built on a foundation (base) poured on Monday. In the meantime, your team poured new concrete on Wednesday on `main`. Rebasing is using a crane to lift your entire house off Monday's foundation and gently placing it down on top of Wednesday's fresh concrete.",
        theory_sections=[
            {
                "heading": "The Purpose of Rebasing",
                "body": (
                    "When your feature branch diverges from `main`, you have two choices for synchronizing:\n"
                    "1. **Merge `main` into your feature**: Creates an extra merge commit, cluttering the graph with criss-crossing lines.\n"
                    "2. **Rebase your feature onto `main`**: Rewrites history by reapplying your feature commits one by one on top of `main`'s latest commit."
                )
            },
            {
                "heading": "How Rebase Operates Under the Hood",
                "body": (
                    "Git saves your branch's unique commits as temporary diff patches in `.git/rebase-apply/`, "
                    "resets your branch to point directly to the destination tip (`main`), "
                    "and then sequentially applies each temporary patch as a brand-new commit with new SHA-1 hashes. "
                    "The result is a completely straight, linear history without any merge commits."
                )
            },
            {
                "heading": "Handling Conflicts During Rebase",
                "body": (
                    "If a conflict occurs during rebase, Git pauses execution:\n"
                    "1. Resolve conflict markers in your editor.\n"
                    "2. Stage the resolved files: `git add <file>`.\n"
                    "3. Continue the rebase: `git rebase --continue` (DO NOT run `git commit`!).\n"
                    "To cancel: `git rebase --abort`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Visualizing Rebase",
                "code": "# Before rebase:\n#       C---D  (feature)\n#      /\n# A---B---E---F  (main)\n#\n# After git switch feature; git rebase main:\n# A---B---E---F---C'---D'  (main, feature)\n# (Commits C and D are replayed on top of F as C' and D')",
                "explanation": "Creates a straight linear line of progression."
            },
            {
                "title": "Executing a Standard Rebase",
                "code": "# 1. Switch to the feature branch you want to move:\ngit switch feature/billing\n\n# 2. Rebase onto latest main:\ngit rebase main\n\n# Output confirms sequential patch replay:\n# Successfully rebased and updated refs/heads/feature/billing.",
                "explanation": "Replays feature commits on top of current main."
            },
            {
                "title": "Resolving Conflicts During Rebase",
                "code": "# When paused by a conflict, edit files, stage, and continue:\ngit add src/billing.py\ngit rebase --continue\n\n# If you wish to abort and return to initial state:\ngit rebase --abort",
                "explanation": "Never run git commit during rebase; use --continue."
            },
            {
                "title": "Viewing Linear Graph After Rebase",
                "code": "# Notice the single straight line with zero merge bubbles:\ngit log --graph --oneline",
                "explanation": "Confirms completely linear git history."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execute Rebase Command",
            description="Assume you are on branch 'feature'. Write the command to rebase 'feature' on top of branch 'main'.",
            starter_code="# Rebase current branch on top of main\n",
            solution_code="git rebase main",
            expected_output="Successfully rebased and updated refs/heads/feature."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary aesthetic and architectural benefit of using `git rebase` instead of `git merge`?",
                options=[
                    "It creates a perfectly straight, linear commit history without cluttered merge bubbles and criss-crossing lines",
                    "It doubles your internet download speed",
                    "It converts your project into a single zip file",
                    "It requires no disk space"
                ],
                correct_answer="It creates a perfectly straight, linear commit history without cluttered merge bubbles and criss-crossing lines",
                explanation="Rebasing replays commits to maintain a clean linear progression."
            ),
            QuizQuestionBlueprint(
                question="What happens to the commit hashes (SHA-1) of your feature branch commits when you rebase them?",
                options=[
                    "They are assigned brand-new SHA-1 hashes because their parent commits and timestamps have changed",
                    "They keep their exact identical hashes",
                    "All hashes are deleted",
                    "The hashes are converted to numbers from 1 to 10"
                ],
                correct_answer="They are assigned brand-new SHA-1 hashes because their parent commits and timestamps have changed",
                explanation="Rebase recreates commits; new parents produce new SHA-1 hashes."
            ),
            QuizQuestionBlueprint(
                question="When a conflict occurs during a rebase, what command should you run AFTER fixing the conflict and running `git add`?",
                options=["git rebase --continue", "git commit", "git merge", "git push --force"],
                correct_answer="git rebase --continue",
                explanation="`git rebase --continue` signals Git to resume replaying the remaining patches."
            ),
            QuizQuestionBlueprint(
                question="Which command cancels an in-progress rebase and returns the branch to its exact starting position?",
                options=["git rebase --abort", "git rebase --stop", "git rebase --cancel", "git reset --all"],
                correct_answer="git rebase --abort",
                explanation="`git rebase --abort` safely abandons the rebase operation."
            ),
            QuizQuestionBlueprint(
                question="Under the hood, where does Git store temporary patch files while applying a rebase?",
                options=[
                    "Inside `.git/rebase-apply/` or `.git/rebase-merge/`",
                    "In the Windows Registry",
                    "In browser local storage",
                    "On GitHub's cloud servers"
                ],
                correct_answer="Inside `.git/rebase-apply/` or `.git/rebase-merge/`",
                explanation="Git manages in-flight rebase state in dedicated `.git` subdirectories."
            )
        ]
    )
]
