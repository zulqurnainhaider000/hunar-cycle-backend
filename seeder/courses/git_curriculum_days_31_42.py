"""
Git & Version Control System Curriculum - Days 31 to 42
Module 5: Advanced Git Operations (Days 31-37)
Module 6: Collaboration & Workflows (Days 38-41)
Module 7: Debugging & Code Search (Day 42 of 42-45)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_42 = [
    # ----------------------------------------------------
    # Day 31: Merge vs Rebase (The Golden Rule of Rebasing)
    # ----------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Merge vs Rebase (The Golden Rule of Rebasing)",
        concept="Mastering the architectural trade-offs between merging and rebasing, and enforcing the Golden Rule of Rebasing to prevent team divergence.",
        analogy="Merging is like preserving the raw, uncut film footage of a movie—every mistake, blooper, and camera reset is preserved forever in the archives. Rebasing is editing that film into a clean, polished 2-hour movie for theater audiences.",
        theory_sections=[
            {
                "heading": "The Philosophical Debate: Merge vs Rebase",
                "body": (
                    "In the Git world, there are two distinct schools of thought regarding commit history:\n"
                    "1. **The Historical Record School (Merge)**: Commit history is an immutable, chronologically true record of what actually happened. "
                    "Messy branches, experiments, and merge commits should never be altered because they represent ground truth.\n"
                    "2. **The Story / Clean Documentation School (Rebase)**: Commit history is a piece of documentation explaining how the software evolved. "
                    "No one cares that you tried 4 failed approaches on a Tuesday night; history should be edited into a clean, linear sequence before publication."
                )
            },
            {
                "heading": "The Golden Rule of Rebasing",
                "body": (
                    "> **\"Never rebase a branch that is shared on a public or remote repository.\"**\n\n"
                    "Rebasing rewrites commit hashes. If Developer A and Developer B both cloned a branch, and Developer A rebases and force-pushes it, "
                    "Developer B's local branch becomes completely desynchronized with identical changes under different hashes. "
                    "When Developer B tries to merge or pull, duplicate commits, ghost conflicts, and hours of debugging ensue."
                )
            },
            {
                "heading": "Industry Best Practice Synthesis",
                "body": (
                    "- Rebase your **private local feature branches** onto `main` before submitting a Pull Request to keep them current and clean.\n"
                    "- Never rebase `main`, `master`, `develop`, or any shared release branch."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Safe Practice: Rebasing Local Feature Branch",
                "code": "# 1. You are on private local branch feature/search:\ngit switch feature/search\n\n# 2. Rebase onto latest main before opening PR:\ngit fetch origin\ngit rebase origin/main\n\n# 3. Clean linear commits are ready for peer review",
                "explanation": "Safe: rewriting private history before publication."
            },
            {
                "title": "Catastrophic Anti-Pattern (Violating the Golden Rule)",
                "code": "# DANGEROUS: Rebasing shared main and force pushing:\ngit switch main\ngit rebase feature\ngit push origin main --force   # <-- RUINS COLLABORATORS' REPOSITORIES!",
                "explanation": "Forces all collaborators to manually repair their local branches."
            },
            {
                "title": "Trade-Off Matrix: Merge vs Rebase",
                "code": "# Criterion           | Merge              | Rebase\n# --------------------+--------------------+--------------------\n# History Style       | Non-linear (Graph) | Strictly Linear\n# Preserves Context   | Yes (exact times)  | No (rewrites history)\n# Cleanliness         | Can get noisy      | Pristine\n# Public Safety       | 100% Safe          | DANGEROUS on public",
                "explanation": "Summarizes key decision criteria."
            },
            {
                "title": "Inspecting Diverged Commits",
                "code": "# Check if local branch diverged from upstream:\ngit status\n# Output: Your branch and 'origin/feature' have diverged,\n# and have 2 and 2 different commits each, respectively.",
                "explanation": "Indicates history was rewritten or commits were pushed remotely."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Evaluate Safe Rebase Command",
            description="Write the sequence to fetch remote updates from 'origin' and rebase the current local feature branch onto 'origin/main'.",
            starter_code="# Fetch origin and rebase onto origin/main\n",
            solution_code="git fetch origin\ngit rebase origin/main",
            expected_output="Successfully rebased and updated refs/heads/..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the universally recognized 'Golden Rule of Rebasing' in Git?",
                options=[
                    "Never rebase a branch that has been published or shared on a public remote repository",
                    "Never rebase on a Monday",
                    "Always rebase directly on the production server",
                    "Only rebase files smaller than 10KB"
                ],
                correct_answer="Never rebase a branch that has been published or shared on a public remote repository",
                explanation="Rewriting shared public commits forces all collaborators into messy conflict loops."
            ),
            QuizQuestionBlueprint(
                question="What is the primary advantage of the 'Historical Record' approach (preferring `git merge`)?",
                options=[
                    "It preserves the authentic, chronological truth of how and when commits were authored and merged",
                    "It takes zero disk space",
                    "It prevents syntax errors",
                    "It makes code run 2x faster"
                ],
                correct_answer="It preserves the authentic, chronological truth of how and when commits were authored and merged",
                explanation="Merging preserves the unaltered historical timeline and true authoring context."
            ),
            QuizQuestionBlueprint(
                question="Why is it safe to rebase your personal, private feature branch before opening a Pull Request?",
                options=[
                    "Because nobody else is working on or tracking your private branch yet, so rewriting its history affects only you",
                    "Because Git disables security checks for feature branches",
                    "Because private branches are encrypted",
                    "Because rebase is only allowed by owners"
                ],
                correct_answer="Because nobody else is working on or tracking your private branch yet, so rewriting its history affects only you",
                explanation="Local unpushed branches have no dependent collaborators to break."
            ),
            QuizQuestionBlueprint(
                question="If a developer violates the Golden Rule and force-pushes a rebased `main` branch, what happens to coworkers?",
                options=[
                    "Coworkers' local `main` branches desynchronize, causing duplicate commits and merge errors upon next pull",
                    "Coworkers are banned from GitHub",
                    "Coworkers' operating systems crash",
                    "Nothing happens; Git fixes it silently"
                ],
                correct_answer="Coworkers' local `main` branches desynchronize, causing duplicate commits and merge errors upon next pull",
                explanation="Coworkers hold identical changes with different parent SHAs, resulting in duplicate history."
            ),
            QuizQuestionBlueprint(
                question="Which team strategy provides the best balance: clean feature branches with clear integration records?",
                options=[
                    "Rebase local feature branch against main to stay updated, then merge with `--no-ff` or Squash into main",
                    "Never commit more than once a month",
                    "Delete all branches every morning",
                    "Use email instead of Git"
                ],
                correct_answer="Rebase local feature branch against main to stay updated, then merge with `--no-ff` or Squash into main",
                explanation="Keeps feature branches clean and conflict-free while preserving explicit pull request boundaries."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 32: Interactive Rebase (git rebase -i)
    # ----------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Interactive Rebase (`git rebase -i`)",
        concept="Taking total surgical control of your commit history: reordering, rewording, dropping, splitting, and editing past commits using interactive rebase scripts.",
        analogy="Interactive rebase is like being the director in a video editing studio with the timeline scrubber open. You can drag scenes into a different order, cut out bloopers (`drop`), re-title a scene (`reword`), or cut a scene in half (`edit`).",
        theory_sections=[
            {
                "heading": "The Superpower of Interactive Rebase",
                "body": (
                    "When building a complex feature over several days, your local commit log is often messy: "
                    "`'wip'`, `'fixed typo'`, `'oops forgot semicolon'`, `'tests passing'`. "
                    "`git rebase -i <base>` opens an interactive todo list in your text editor, allowing you to rewrite history before sharing your code."
                )
            },
            {
                "heading": "Interactive Rebase Commands (The Todo List)",
                "body": (
                    "- `pick` (or `p`): Keep and apply the commit as-is.\n"
                    "- `reword` (or `r`): Keep the commit, but pause to edit its commit message.\n"
                    "- `edit` (or `e`): Pause execution at this commit so you can amend files or split it.\n"
                    "- `drop` (or `d`): Completely delete the commit from history!\n"
                    "- `reorder`: Simply cut and paste lines in the editor to reorder commits."
                )
            },
            {
                "heading": "Caution: Oldest Commits Are at the Top",
                "body": (
                    "Unlike `git log` where the newest commit is on top, interactive rebase lists commits in **chronological execution order** "
                    "(oldest commit at the top, newest commit at the bottom)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Launching Interactive Rebase for Last 4 Commits",
                "code": "# Open interactive rebase editor for the last 4 commits:\ngit rebase -i HEAD~4",
                "explanation": "Launches your text editor with the interactive rebase instruction list."
            },
            {
                "title": "Sample Interactive Rebase Todo Script",
                "code": "# Contents inside editor:\n# pick 7a4e8c1 feat: add user model\n# reword 3f2a1b9 oops typo in user model\n# pick 1c0d4e8 feat: add user controller\n# drop 9e8d7c6 test debug logging\n\n# Save and exit editor to execute the plan!",
                "explanation": "Executes renames, picks, and drops in chronological order."
            },
            {
                "title": "Splitting a Commit with 'edit'",
                "code": "# When rebase pauses at a commit marked 'edit':\ngit reset HEAD~1\ngit add file1.py\ngit commit -m \"feat: part 1\"\ngit add file2.py\ngit commit -m \"feat: part 2\"\ngit rebase --continue",
                "explanation": "Splits a single large commit into multiple clean commits."
            },
            {
                "title": "Aborting Interactive Rebase at Any Point",
                "code": "# If you get confused or make a mistake, abort safely:\ngit rebase --abort",
                "explanation": "Restores your branch to its exact state before launching the rebase."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate Interactive Rebase Command",
            description="Write the command to launch interactive rebase for the last 3 commits on your current branch.",
            starter_code="# Launch interactive rebase for HEAD~3\n",
            solution_code="git rebase -i HEAD~3",
            expected_output="Opens interactive rebase todo file in editor"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In what chronological order does the interactive rebase (`git rebase -i`) todo list display commits?",
                options=[
                    "Oldest commit at the top, newest commit at the bottom (execution order)",
                    "Newest commit at the top, oldest at the bottom (like `git log`)",
                    "Random order",
                    "Alphabetical order by author name"
                ],
                correct_answer="Oldest commit at the top, newest commit at the bottom (execution order)",
                explanation="The todo script runs top-to-bottom, applying older commits first."
            ),
            QuizQuestionBlueprint(
                question="Which interactive rebase action allows you to change a commit message without modifying its code?",
                options=["reword (or r)", "pick (or p)", "edit (or e)", "amend (or a)"],
                correct_answer="reword (or r)",
                explanation="`reword` pauses at that commit specifically to allow editing its message."
            ),
            QuizQuestionBlueprint(
                question="What happens if you change the action of a commit line in the todo list to `drop` (or delete the line)?",
                options=[
                    "Git completely discards and deletes that commit from your branch history",
                    "Git pauses with an unrecoverable error",
                    "Git emails the author",
                    "The commit is moved to a new branch"
                ],
                correct_answer="Git completely discards and deletes that commit from your branch history",
                explanation="Marking a commit as `drop` or deleting its line excludes it from replay."
            ),
            QuizQuestionBlueprint(
                question="How can you change the order of two commits using interactive rebase?",
                options=[
                    "Cut and paste the commit lines into the desired order inside the editor todo script",
                    "Pass the `--sort` flag to git",
                    "Use `git swap <hash1> <hash2>`",
                    "Commits cannot be reordered in Git"
                ],
                correct_answer="Cut and paste the commit lines into the desired order inside the editor todo script",
                explanation="Git applies commits in the exact line order specified in the todo script."
            ),
            QuizQuestionBlueprint(
                question="Which action command pauses rebase execution so you can run `git reset HEAD~1` and split one commit into two?",
                options=["edit (or e)", "pause (or p)", "break (or b)", "split (or s)"],
                correct_answer="edit (or e)",
                explanation="`edit` halts the replay process, returning control to your terminal shell."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 33: Squashing Commits
    # ----------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: Squashing Commits",
        concept="Condensing multiple exploratory or micro-commits into a single cohesive, production-ready atomic commit using `squash` and `fixup`.",
        analogy="You are baking a cake. You tried 3 different amounts of sugar, spilled some flour, cleaned the counter, and finally baked it. Squashing is serving the finished cake on a clean plate with a recipe card, without making the guest eat the 5 failed attempts.",
        theory_sections=[
            {
                "heading": "Why Squash Commits?",
                "body": (
                    "During development, making frequent micro-commits ('fixed typo', 'WIP', 'debugging print statements') is healthy. "
                    "However, merging 20 messy micro-commits into `main` pollutes repository history and makes `git bisect` painful. "
                    "Squashing melts multiple adjacent commits into a single unified commit."
                )
            },
            {
                "heading": "The Difference Between `squash` and `fixup`",
                "body": (
                    "In interactive rebase (`git rebase -i`):\n"
                    "- `squash` (or `s`): Melts the commit into the commit directly above it and **prompts you to combine both commit messages**.\n"
                    "- `fixup` (or `f`): Melts the commit into the commit directly above it and **silently discards the current commit's message**."
                )
            },
            {
                "heading": "Auto-Squashing with `--fixup`",
                "body": (
                    "Modern Git supports instant targeted fixups: `git commit --fixup <commit-hash>`. "
                    "When you later run `git rebase -i --autosquash`, Git automatically arranges the fixup commits next to their targets "
                    "and sets their action to `fixup`!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Interactive Squash Todo Script",
                "code": "# git rebase -i HEAD~3\n# Todo script inside editor:\n\npick 7a4e8c1 feat: add user profile page\nsquash 3f2a1b9 fix styling on profile page\nfixup 1c0d4e8 remove console.log statements\n\n# All 3 commits melt into one single commit under 7a4e8c1",
                "explanation": "Combines 3 commits into 1 clean commit."
            },
            {
                "title": "Squash and Merge via GitHub / CLI",
                "code": "# Perform squash merge from CLI:\ngit switch main\ngit merge --squash feature/search\ngit commit -m \"feat: implement full-text search engine\"",
                "explanation": "Stops all feature commits and creates 1 single commit on main."
            },
            {
                "title": "The Modern Auto-Squash Workflow",
                "code": "# Create a targeted fixup commit for older commit 7a4e8c1:\ngit commit --fixup 7a4e8c1\n\n# Automatically reorder and fixup without manual script editing:\ngit rebase -i --autosquash HEAD~5",
                "explanation": "Git pairs fixups with their target commits automatically."
            },
            {
                "title": "Configuring Global Autosquash",
                "code": "# Configure Git to always auto-squash during interactive rebases:\ngit config --global rebase.autoSquash true",
                "explanation": "Saves time in daily developer workflows."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Global Auto-Squash",
            description="Configure git globally to enable `rebase.autoSquash` and verify with `git config --get`.",
            starter_code="# Set rebase.autoSquash globally to true\n",
            solution_code="git config --global rebase.autoSquash true\ngit config --global --get rebase.autoSquash",
            expected_output="true"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the key difference between the `squash` and `fixup` actions in `git rebase -i`?",
                options=[
                    "`squash` combines commit messages for review; `fixup` silently discards the second commit's message",
                    "`fixup` deletes code, while `squash` keeps it",
                    "`squash` only works on images",
                    "`fixup` requires a password"
                ],
                correct_answer="`squash` combines commit messages for review; `fixup` silently discards the second commit's message",
                explanation="`fixup` folds the code into the parent commit without cluttering the log message."
            ),
            QuizQuestionBlueprint(
                question="Into which commit does a line marked `squash` get merged?",
                options=[
                    "The commit immediately preceding (above) it in the rebase todo list",
                    "The very first commit in repository history",
                    "The latest commit on main",
                    "A random commit"
                ],
                correct_answer="The commit immediately preceding (above) it in the rebase todo list",
                explanation="Squash merges into the previous commit listed above it."
            ),
            QuizQuestionBlueprint(
                question="What does running `git merge --squash feature` produce on the destination branch?",
                options=[
                    "It stages all changes from the feature branch into a single pending commit without creating a merge commit",
                    "It creates 50 separate commits",
                    "It deletes the feature branch instantly",
                    "It rebases the branch onto origin"
                ],
                correct_answer="It stages all changes from the feature branch into a single pending commit without creating a merge commit",
                explanation="`--squash` condenses the entire branch into a single staged changeset."
            ),
            QuizQuestionBlueprint(
                question="Which command creates a commit specifically tagged to be automatically squashed into an older commit during rebase?",
                options=["git commit --fixup <commit-hash>", "git commit --squash-target <hash>", "git commit --attach <hash>", "git commit --fold <hash>"],
                correct_answer="git commit --fixup <commit-hash>",
                explanation="`--fixup` sets the message to `fixup! <subject>` for automated squashing."
            ),
            QuizQuestionBlueprint(
                question="Why is squashing pull requests standard policy at tech companies like Google and Meta?",
                options=[
                    "It ensures every feature merged into main is encapsulated in exactly one atomic, easily-revertible commit",
                    "It reduces hard drive costs on cloud servers",
                    "It disables compiler warnings",
                    "It allows juniors to bypass senior code review"
                ],
                correct_answer="It ensures every feature merged into main is encapsulated in exactly one atomic, easily-revertible commit",
                explanation="Single-commit PRs keep the trunk history clean and make production rollbacks trivial."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 34: Cherry-Picking (git cherry-pick)
    # ----------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Cherry-Picking (`git cherry-pick`)",
        concept="Selectively copying specific individual commits from one branch and applying them onto another branch without merging the entire branch.",
        analogy="You go to a buffet. You don't want to buy the entire 40-course buffet tray (merging the whole branch). You just want one delicious strawberry pastry from table 3 (`cherry-pick`) and put it onto your personal plate (`current branch`).",
        theory_sections=[
            {
                "heading": "What is Cherry-Picking?",
                "body": (
                    "`git cherry-pick <commit-hash>` takes the changes introduced by a specific commit from anywhere in your repository "
                    "and reapplies them as a brand-new commit on top of your currently checked-out branch."
                )
            },
            {
                "heading": "Common Production Scenarios",
                "body": (
                    "1. **Emergency Hotfixes**: A critical bugfix was committed to an unreleased `feature` branch or `develop` branch. "
                    "You need that exact bugfix in the production `release-v1.0` branch immediately, but you cannot release the other unfinished features.\n"
                    "2. **Accidental Branch Commits**: You accidentally committed a change to `main` instead of `feature`. "
                    "You switch to `feature`, cherry-pick the commit, and reset `main`."
                )
            },
            {
                "heading": "Cherry-Picking Flags and Ranges",
                "body": (
                    "- `git cherry-pick -n <hash>`: (`--no-commit`) Applies changes to staging area without creating a commit.\n"
                    "- `git cherry-pick A..B`: Cherry-picks a range of commits sequentially.\n"
                    "- `git cherry-pick -x <hash>`: Appends `(cherry picked from commit ...)` to the message for audit trails."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Basic Cherry-Pick Workflow",
                "code": "# 1. Switch to destination branch (e.g. production release):\ngit switch release-v2.1\n\n# 2. Grab specific bugfix commit from develop branch:\ngit cherry-pick 7a4e8c1\n\n# Output confirms new commit created on release branch:\n# [release-v2.1 4d3c2b1] fix: patch security vulnerability in auth\n#  1 file changed, 2 insertions(+), 1 deletion(-)",
                "explanation": "Applies targeted commit onto the active branch."
            },
            {
                "title": "Cherry-Picking with Provenance Audit Trail (-x)",
                "code": "# Add original commit reference in commit message body:\ngit cherry-pick -x 7a4e8c1\n\n# Generated message:\n# fix: patch security vulnerability\n# (cherry picked from commit 7a4e8c1d5f2a1b9e3f4a5c6d7e8f9a0b1c2d3e4f)",
                "explanation": "Standard for backporting patches across maintenance branches."
            },
            {
                "title": "Cherry-Pick Without Committing (-n)",
                "code": "# Apply changes directly into staging area for inspection:\ngit cherry-pick -n 3f2a1b9",
                "explanation": "Leaves changes staged for manual verification."
            },
            {
                "title": "Resolving Cherry-Pick Conflicts",
                "code": "# If conflict occurs, resolve markers, stage, and continue:\ngit add src/auth.py\ngit cherry-pick --continue\n\n# Or abort cleanly:\ngit cherry-pick --abort",
                "explanation": "Standard continuation and abort semantics."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate Cherry-Pick Command",
            description="Write the command to cherry-pick commit '8f4a1c2' onto your active branch with the `-x` audit provenance flag.",
            starter_code="# Cherry-pick commit 8f4a1c2 with provenance flag\n",
            solution_code="git cherry-pick -x 8f4a1c2",
            expected_output="[main ...] ... (cherry picked from commit 8f4a1c2...)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does `git cherry-pick <commit-hash>` do?",
                options=[
                    "Copies the changes from a specific commit and applies them as a new commit on the currently active branch",
                    "Deletes the commit from the repository",
                    "Merges all commits from the repository into one",
                    "Renames the branch to cherry"
                ],
                correct_answer="Copies the changes from a specific commit and applies them as a new commit on the currently active branch",
                explanation="Cherry-picking applies the patch of a single targeted commit to HEAD."
            ),
            QuizQuestionBlueprint(
                question="What is a classic, practical production use case for `git cherry-pick`?",
                options=[
                    "Backporting a critical bugfix commit from a development branch into an active production release branch without bringing unfinished features",
                    "Backing up code to Google Drive",
                    "Renaming all files in the project",
                    "Generating documentation websites"
                ],
                correct_answer="Backporting a critical bugfix commit from a development branch into an active production release branch without bringing unfinished features",
                explanation="Cherry-pick allows surgically porting hotfixes across divergent branches."
            ),
            QuizQuestionBlueprint(
                question="What does the `-x` flag do during `git cherry-pick -x <hash>`?",
                options=[
                    "Appends a note `(cherry picked from commit <hash>)` to the commit message for traceability and audit compliance",
                    "Executes tests before picking",
                    "Encrypts the commit with XML",
                    "Pushes the commit to remote immediately"
                ],
                correct_answer="Appends a note `(cherry picked from commit <hash>)` to the commit message for traceability and audit compliance",
                explanation="`-x` provides provenance for backported commits across long-term branches."
            ),
            QuizQuestionBlueprint(
                question="What does the `-n` (or `--no-commit`) flag do during a cherry-pick?",
                options=[
                    "Applies the changes to the working directory and index without automatically creating a commit object",
                    "Cancels the cherry-pick",
                    "Skips numeric characters",
                    "Runs in non-interactive mode"
                ],
                correct_answer="Applies the changes to the working directory and index without automatically creating a commit object",
                explanation="`-n` allows modifying or testing the picked changes prior to committing."
            ),
            QuizQuestionBlueprint(
                question="Does cherry-picking a commit change its SHA-1 hash on the destination branch?",
                options=[
                    "Yes, because its parent commit, author timestamp, and commit timestamp are different, a new SHA-1 hash is generated",
                    "No, Git guarantees identical hashes across all branches",
                    "Only on Windows systems",
                    "Only if the commit has conflicts"
                ],
                correct_answer="Yes, because its parent commit, author timestamp, and commit timestamp are different, a new SHA-1 hash is generated",
                explanation="New parents and timestamps result in a brand-new commit object."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 35: Tagging Releases (Lightweight vs Annotated)
    # ----------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Tagging Releases (Lightweight vs Annotated)",
        concept="Marking specific milestone releases (e.g. `v1.0.0`) in repository history using Lightweight tags and cryptographically signed Annotated tags.",
        analogy="If a branch is a movable Post-it note that moves every time you make a commit, a Git Tag is a permanent brass commemorative plaque screwed into a specific stone on the wall. It never moves.",
        theory_sections=[
            {
                "heading": "What is a Git Tag?",
                "body": (
                    "Tags are reference pointers used to mark specific release points in history (e.g. `v1.0.0`, `v2.4.1-beta`). "
                    "Unlike branches which move forward automatically with every new commit, **tags are static and permanent**. "
                    "They permanently point to the exact same commit forever."
                )
            },
            {
                "heading": "Lightweight vs Annotated Tags",
                "body": (
                    "1. **Lightweight Tags**: Simply a pointer to a commit hash (stored in `.git/refs/tags/`). Contains no extra metadata.\n"
                    "2. **Annotated Tags (`-a`)**: Stored as full independent objects in the Git object database. "
                    "They contain the tagger's name, email, date, an explicit tagging message, and can be cryptographically signed with GPG (`-s`). "
                    "**Production software releases should ALWAYS use Annotated tags.**"
                )
            },
            {
                "heading": "Pushing Tags to Remote",
                "body": (
                    "`git push` does not transfer tags to remote servers by default. "
                    "You must push tags explicitly using `git push origin <tagname>` or `git push origin --tags`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating an Annotated Production Release Tag",
                "code": "# Create annotated tag with release notes message:\ngit tag -a v1.0.0 -m \"Release version 1.0.0: stable production launch\"\n\n# Inspect the tag object:\ngit show v1.0.0\n# Output displays tagger name, date, message, and commit details",
                "explanation": "Annotated tags are permanent database objects."
            },
            {
                "title": "Creating a Lightweight Tag",
                "code": "# Quick private pointer without metadata:\ngit tag v1.0.0-draft",
                "explanation": "Simple reference bookmark without tagger metadata."
            },
            {
                "title": "Tagging an Older Historical Commit",
                "code": "# Tag a commit made 3 days ago by passing its hash:\ngit tag -a v0.9.0 7a4e8c1 -m \"Retroactive tag for beta release\"",
                "explanation": "Applies a tag backwards in time to historical commits."
            },
            {
                "title": "Publishing and Deleting Tags",
                "code": "# Push single tag to GitHub:\ngit push origin v1.0.0\n\n# Push all local tags in batch:\ngit push origin --tags\n\n# Delete a tag locally and on remote:\ngit tag -d v1.0.0\ngit push origin --delete v1.0.0",
                "explanation": "Publishing and cleanup lifecycle commands."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create and Inspect Annotated Tag",
            description="Create an annotated tag 'v1.0.0' with message 'Initial Release' on HEAD and list all tags.",
            starter_code="# Create annotated tag v1.0.0 and list tags\n",
            solution_code="git tag -a v1.0.0 -m \"Initial Release\"\ngit tag -l",
            expected_output="v1.0.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why should production software releases always use Annotated tags (`-a`) rather than Lightweight tags?",
                options=[
                    "Annotated tags store the tagger's name, email, date, and release message as an immutable object in the Git database",
                    "Annotated tags make the application compile faster",
                    "Lightweight tags expire after 30 days",
                    "GitHub refuses to download lightweight tags"
                ],
                correct_answer="Annotated tags store the tagger's name, email, date, and release message as an immutable object in the Git database",
                explanation="Annotated tags provide a verifiable audit trail with author identity and messages."
            ),
            QuizQuestionBlueprint(
                question="Does a standard `git push origin main` command automatically upload your local tags to GitHub?",
                options=[
                    "No, tags must be pushed explicitly using `git push origin <tag>` or `git push origin --tags`",
                    "Yes, all tags are always pushed with branches",
                    "Only if you use `--force`",
                    "Only on Sundays"
                ],
                correct_answer="No, tags must be pushed explicitly using `git push origin <tag>` or `git push origin --tags`",
                explanation="Git deliberately isolates tags from regular branch pushes."
            ),
            QuizQuestionBlueprint(
                question="What is the primary operational difference between a Git Branch and a Git Tag?",
                options=[
                    "A branch pointer advances automatically with each new commit; a tag remains permanently anchored to its assigned commit",
                    "Branches cost money; tags are free",
                    "Tags can only be created by repository administrators",
                    "Branches only exist locally"
                ],
                correct_answer="A branch pointer advances automatically with each new commit; a tag remains permanently anchored to its assigned commit",
                explanation="Tags are static milestone pins; branches are dynamic movable heads."
            ),
            QuizQuestionBlueprint(
                question="Which flag allows you to cryptographically sign an annotated tag with your GPG key for security verification?",
                options=["-s (or --sign)", "-p", "-k", "--secure"],
                correct_answer="-s (or --sign)",
                explanation="`git tag -s` cryptographically signs the tag using GnuPG."
            ),
            QuizQuestionBlueprint(
                question="How do you delete a tag named 'v0.5.0' from the remote repository on origin?",
                options=["git push origin --delete v0.5.0", "git tag -d remote v0.5.0", "git remote drop tag v0.5.0", "git erase tag v0.5.0"],
                correct_answer="git push origin --delete v0.5.0",
                explanation="`git push <remote> --delete <tag>` removes the remote tag ref."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 36: The Ultimate Safety Net (git reflog)
    # ----------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: The Ultimate Safety Net (`git reflog`)",
        concept="Leveraging the local Reference Log (`reflog`) to effortlessly recover accidentally deleted branches, botched rebases, and hard resets.",
        analogy="If `git log` is the public history of the kingdom, `git reflog` is the flight recorder (black box) under the floorboards of your personal cockpit. Every time your hands touched the controls—even if you crashed the plane—the black box recorded the exact coordinates.",
        theory_sections=[
            {
                "heading": "Git Almost Never Deletes Data",
                "body": (
                    "When developers panic thinking they 'deleted all their work' after a `git reset --hard` or deleting an unmerged branch, "
                    "the commit objects are almost certainly still sitting unharmed in the `.git/objects/` database! "
                    "Git only deleted the **pointer** to those commits."
                )
            },
            {
                "heading": "What is `git reflog`?",
                "body": (
                    "The **Reference Log** (`reflog`) is an audit log that records every single change to the `HEAD` reference on your local machine: "
                    "commits, branch checkouts, rebases, amends, merges, and resets. "
                    "Each entry receives a selector like `HEAD@{0}` (now), `HEAD@{1}` (previous step), etc."
                )
            },
            {
                "heading": "Local Scope and Expiration",
                "body": (
                    "The reflog is strictly local to your machine—it is never pushed to remote servers or shared with coworkers. "
                    "Entries are preserved by default for **90 days** before being cleaned by `git gc` (garbage collection)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting the Reference Log",
                "code": "# View recent movements of HEAD:\ngit reflog\n\n# Output sample:\n# 7a4e8c1 (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1\n# 4b2c1d0 HEAD@{1}: commit: critical feature code\n# 3f2a1b9 HEAD@{2}: checkout: moving from dev to main",
                "explanation": "Reveals previous HEAD locations before destructive actions."
            },
            {
                "title": "Recovering from git reset --hard Disaster",
                "code": "# 1. You accidentally wiped out commits:\ngit reset --hard HEAD~2\n\n# 2. Check reflog to find the hash of the lost commit:\ngit reflog\n# Notice 4b2c1d0 is where HEAD was before the reset!\n\n# 3. Jump right back to safety:\ngit reset --hard 4b2c1d0",
                "explanation": "Instantly reverses a destructive hard reset."
            },
            {
                "title": "Recovering an Accidentally Deleted Branch",
                "code": "# 1. You accidentally deleted branch 'feat-payment':\ngit branch -D feat-payment\n\n# 2. Find the last commit that was on that branch via reflog:\ngit reflog\n# 9c8b7a1 HEAD@{3}: commit: finish stripe webhook\n\n# 3. Recreate the branch from that commit:\ngit switch -c feat-payment 9c8b7a1",
                "explanation": "Restores deleted branches in seconds."
            },
            {
                "title": "Inspecting Branch-Specific Reflogs",
                "code": "# View reflog for a specific branch rather than global HEAD:\ngit reflog show feature/auth",
                "explanation": "Narrows audit log to single branch movements."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Reflog Output",
            description="Run `git reflog -n 5` to inspect the last 5 movements of the local HEAD reference.",
            starter_code="# Run git reflog limited to 5 entries\n",
            solution_code="git reflog -n 5",
            expected_output="... HEAD@{0}: ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `git reflog` considered the ultimate safety net for Git developers?",
                options=[
                    "It tracks every movement of HEAD locally, allowing you to find commit hashes lost to hard resets, deleted branches, or bad rebases",
                    "It automatically emails GitHub customer support",
                    "It recovers deleted files from your computer's Recycle Bin",
                    "It backs up your code to an external hard drive"
                ],
                correct_answer="It tracks every movement of HEAD locally, allowing you to find commit hashes lost to hard resets, deleted branches, or bad rebases",
                explanation="Reflog records historical pointer states even when commits become unreferenced."
            ),
            QuizQuestionBlueprint(
                question="Is your local `reflog` published to GitHub when you run `git push`?",
                options=[
                    "No, the reflog is strictly local to your machine and is never shared over the network",
                    "Yes, all reflog logs are public on your GitHub profile",
                    "Only if you pay for GitHub Pro",
                    "Only on Linux machines"
                ],
                correct_answer="No, the reflog is strictly local to your machine and is never shared over the network",
                explanation="Reflogs are personal, machine-specific audit trails."
            ),
            QuizQuestionBlueprint(
                question="What does the selector `HEAD@{1}` represent in `git reflog`?",
                options=[
                    "The state of HEAD immediately prior to its current position",
                    "The first commit in the repository",
                    "The remote tracking branch",
                    "The author of the commit"
                ],
                correct_answer="The state of HEAD immediately prior to its current position",
                explanation="`HEAD@{0}` is current; `HEAD@{1}` is one step backwards in your personal action history."
            ),
            QuizQuestionBlueprint(
                question="How long does Git retain reflog entries by default before automatic garbage collection purges them?",
                options=["90 days", "24 hours", "7 days", "Forever"],
                correct_answer="90 days",
                explanation="The default expiry (`gc.reflogExpire`) is 90 days for reachable refs."
            ),
            QuizQuestionBlueprint(
                question="If you accidentally force-delete a branch (`git branch -D my-work`), how do you restore it using reflog?",
                options=[
                    "Find the commit hash where the branch was standing in `git reflog` and run `git switch -c my-work <hash>`",
                    "Run `git undo branch`",
                    "Re-clone the repository from GitHub",
                    "You cannot; the work is permanently lost"
                ],
                correct_answer="Find the commit hash where the branch was standing in `git reflog` and run `git switch -c my-work <hash>`",
                explanation="Re-creating a branch pointing to the reflog hash fully restores the branch."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 37 (Project): Disaster Recovery Lab (Recovering lost commits & dropped stashes)
    # ----------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37 (Project): Disaster Recovery Lab (Recovering lost commits & dropped stashes)",
        concept="Hands-on emergency response simulation: recovering orphaned commits, restoring dropped stashes via `fsck`, and rescuing branches from botched rebases.",
        analogy="Today is emergency firefighter drill for Git. You will intentionally trigger three common developer nightmares (accidentally running `--hard`, dropping the wrong stash, deleting a branch), and rescue all lost data using forensic Git tools.",
        theory_sections=[
            {
                "heading": "The Anatomy of 'Lost' Objects",
                "body": (
                    "When a commit or stash is deleted in Git, the object data (`zlib`-compressed blob/tree/commit) remains in `.git/objects/`. "
                    "It is called a **dangling object** (an object not reachable from any named branch, tag, or ref). "
                    "Until `git gc` runs, these objects can be identified and recovered with 100% precision."
                )
            },
            {
                "heading": "The Detective Tool: `git fsck`",
                "body": (
                    "`git fsck` (File System Consistency Check) inspects the internal database for unreachable and dangling objects. "
                    "Running `git fsck --lost-found` scans every loose object and writes all orphaned commits and blobs into `.git/lost-found/`."
                )
            },
            {
                "heading": "Lab Scenario Breakdown",
                "body": (
                    "1. **Disaster A**: Botched hard reset recovery using `git reflog`.\n"
                    "2. **Disaster B**: Dropped stash recovery using `git fsck --lost-found`.\n"
                    "3. **Disaster C**: Rescuing a rebase conflict gone wrong."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Disaster 1: Rescuing an Overwritten Hard Reset",
                "code": "# Find the commit hash before reset:\ngit reflog\n# 4b2c1d0 HEAD@{1}: commit: vital payment logic\n\n# Create rescue branch pointing to that commit:\ngit switch -c rescue/payment-feature 4b2c1d0",
                "explanation": "Recovers commits orphaned by git reset --hard."
            },
            {
                "title": "Disaster 2: Recovering an Accidentally Dropped Stash",
                "code": "# 1. You ran git stash drop by mistake!\n# 2. Find dangling commits in the object database:\ngit fsck --lost-found\n\n# Output displays dangling commits:\n# dangling commit a1b2c3d4e5f...\n\n# 3. Inspect which dangling commit holds your lost stash:\ngit show a1b2c3d\n\n# 4. Re-apply it directly:\ngit stash apply a1b2c3d",
                "explanation": "Recovers dropped stashes using git fsck."
            },
            {
                "title": "Inspecting Lost Objects in .git/lost-found",
                "code": "# Inspect files recovered by git fsck --lost-found:\nls -la .git/lost-found/commit/",
                "explanation": "Lists all salvaged commit objects."
            },
            {
                "title": "Aborting Failed Disaster Rescue",
                "code": "# If midway through recovery you get stuck in a bad rebase:\ngit rebase --abort\n# Or if stuck in a bad merge:\ngit merge --abort",
                "explanation": "Clean abort resets back to prior clean baseline."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Scan for Dangling Objects with fsck",
            description="Run `git fsck --lost-found` to scan the repository database for dangling orphaned commits and blobs.",
            starter_code="# Run git fsck with lost-found flag\n",
            solution_code="git fsck --lost-found",
            expected_output="Checking object directories..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'dangling commit' in Git?",
                options=[
                    "A valid commit object that exists in the database but is no longer referenced by any branch, tag, or active ref",
                    "A commit that failed to compile",
                    "A commit with a syntax error",
                    "A commit waiting for credit card payment"
                ],
                correct_answer="A valid commit object that exists in the database but is no longer referenced by any branch, tag, or active ref",
                explanation="Dangling commits have no pointers leading to them, but their content is intact."
            ),
            QuizQuestionBlueprint(
                question="Which low-level diagnostic command scans the Git object database to find all unreachable and dangling objects?",
                options=["git fsck --lost-found", "git scan --orphans", "git find-lost", "git rescue --all"],
                correct_answer="git fsck --lost-found",
                explanation="`git fsck --lost-found` identifies and exports unreachable objects."
            ),
            QuizQuestionBlueprint(
                question="If you accidentally run `git stash drop` on valuable work, can it be recovered?",
                options=[
                    "Yes, by finding the dangling commit using `git fsck` and running `git stash apply <hash>`",
                    "No, dropping a stash shreds the hard drive sectors instantly",
                    "Only if you call GitHub support",
                    "Only by writing the code again from memory"
                ],
                correct_answer="Yes, by finding the dangling commit using `git fsck` and running `git stash apply <hash>`",
                explanation="Stash drops remove the ref, but the commit object remains recoverable via `fsck`."
            ),
            QuizQuestionBlueprint(
                question="Where does `git fsck --lost-found` write the extracted orphaned objects?",
                options=["Inside `.git/lost-found/`", "In the desktop Trash", "In `/var/tmp/git/`", "In the Windows registry"],
                correct_answer="Inside `.git/lost-found/`",
                explanation="Orphaned commits and blobs are saved to `.git/lost-found/commit/` and `other/`."
            ),
            QuizQuestionBlueprint(
                question="What is the safest way to preserve an orphaned commit once you find its hash in `git reflog`?",
                options=[
                    "Create a new named branch pointing directly to it: `git branch rescue-branch <hash>`",
                    "Write the hash down on a sticky note",
                    "Print the hash on paper",
                    "Email the hash to coworkers"
                ],
                correct_answer="Create a new named branch pointing directly to it: `git branch rescue-branch <hash>`",
                explanation="Creating a branch attaches a ref pointer to the commit, preventing garbage collection."
            )
        ],
        is_project_day=True,
        project_name="Disaster Recovery Lab (Recovering lost commits & dropped stashes)"
    ),

    # ----------------------------------------------------
    # Day 38: Forking a Repository (Open Source)
    # ----------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Forking a Repository (Open Source)",
        concept="Understanding the fork-and-pull collaboration model used in open-source ecosystems like GitHub and GitLab.",
        analogy="If a public open-source project is a restaurant kitchen, you don't have a key to walk in and mess with their stove. Forking is photocopying their menu and kitchen blueprint so you can build an identical kitchen in your own backyard, cook new dishes, and invite the head chef over to taste-test your recipe.",
        theory_sections=[
            {
                "heading": "What is a Fork?",
                "body": (
                    "A **Fork** is not a native Git command; it is a feature provided by hosting platforms (GitHub, GitLab, Bitbucket). "
                    "When you fork a repository, the platform creates an entirely independent server-side clone under your personal account. "
                    "You have full write (push) permissions to your fork, while the original repository remains protected."
                )
            },
            {
                "heading": "The Triangular Fork Workflow",
                "body": (
                    "In open-source contribution:\n"
                    "1. **Upstream (Original repo)**: You have read-only access.\n"
                    "2. **Origin (Your fork on GitHub)**: You have full read/write access.\n"
                    "3. **Local (Your computer)**: You clone your fork, configure `upstream` pointing to original, and code in feature branches."
                )
            },
            {
                "heading": "Keeping Your Fork Synchronized with Upstream",
                "body": (
                    "As months pass, the original project advances. To prevent your fork from rotting, you fetch from `upstream`, "
                    "merge `upstream/main` into your local `main`, and push back to your `origin`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Cloning Your Personal Fork",
                "code": "# 1. Clone your personal fork to your laptop:\ngit clone https://github.com/my-username/open-source-project.git\ncd open-source-project",
                "explanation": "origin points to your personal fork."
            },
            {
                "title": "Configuring the Upstream Remote",
                "code": "# 2. Connect the original authoritative project as 'upstream':\ngit remote add upstream https://github.com/original-author/open-source-project.git\n\n# Verify remotes:\ngit remote -v\n# origin    https://github.com/my-username/open-source-project.git (fetch & push)\n# upstream  https://github.com/original-author/open-source-project.git (fetch & push)",
                "explanation": "Establishes connection to the authoritative source."
            },
            {
                "title": "Syncing Local Fork with Upstream Changes",
                "code": "# 3. Fetch latest upstream developments:\ngit fetch upstream\n\n# 4. Merge upstream's main into your local main:\ngit switch main\ngit merge upstream/main\n\n# 5. Push updated main to your personal GitHub fork:\ngit push origin main",
                "explanation": "The standard synchronization rhythm."
            },
            {
                "title": "Working in Feature Branches for PRs",
                "code": "# Always create feature branches for contributions:\ngit switch -c fix/docs-typo\n# Make edits, commit, and push to YOUR fork:\ngit push -u origin fix/docs-typo",
                "explanation": "Never submit PRs directly from your fork's main branch."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Configure Upstream Remote for Fork",
            description="Add a remote named 'upstream' pointing to 'https://github.com/upstream-org/project.git' and list remotes verbosely.",
            starter_code="# Add upstream remote and list -v\n",
            solution_code="git remote add upstream https://github.com/upstream-org/project.git\ngit remote -v",
            expected_output="upstream\thttps://github.com/upstream-org/project.git (fetch)\nupstream\thttps://github.com/upstream-org/project.git (push)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'Fork' in platforms like GitHub and GitLab?",
                options=[
                    "A server-side copy of a repository created under your personal account where you have full write/push permissions",
                    "A native Git CLI command added in version 2.0",
                    "A tool for deleting duplicate files",
                    "A method for compressing repositories"
                ],
                correct_answer="A server-side copy of a repository created under your personal account where you have full write/push permissions",
                explanation="Forks provide contributors with an independent copy to work on without compromising the upstream repo."
            ),
            QuizQuestionBlueprint(
                question="What is the conventional name for the remote bookmark pointing to the original authoritative project in a forked workflow?",
                options=["upstream", "origin", "central", "parent"],
                correct_answer="upstream",
                explanation="`upstream` universally designates the primary source repository."
            ),
            QuizQuestionBlueprint(
                question="Why should you avoid creating pull requests directly from your fork's `main` branch?",
                options=[
                    "Using dedicated feature branches allows working on multiple independent contributions simultaneously and keeps your local `main` clean for upstream syncs",
                    "GitHub blocks pull requests from `main`",
                    "It deletes your fork automatically",
                    "It charges extra subscription fees"
                ],
                correct_answer="Using dedicated feature branches allows working on multiple independent contributions simultaneously and keeps your local `main` clean for upstream syncs",
                explanation="Feature branches isolate PRs, keeping your main branch clean to track upstream."
            ),
            QuizQuestionBlueprint(
                question="Which commands sync your local repository with changes made to the original project?",
                options=[
                    "`git fetch upstream` followed by merging `upstream/main` into your local `main`",
                    "`git push --all`",
                    "`git rebase --everything`",
                    "`git sync origin`"
                ],
                correct_answer="`git fetch upstream` followed by merging `upstream/main` into your local `main`",
                explanation="Fetching from upstream and integrating keeps your local clone up to date."
            ),
            QuizQuestionBlueprint(
                question="Does forking an open-source repository notify or require approval from the original repository maintainer?",
                options=[
                    "No, forking public repositories is entirely self-service and can be done freely without maintainer permissions",
                    "Yes, maintainers must approve each fork within 48 hours",
                    "Only if you fork during business hours",
                    "Only on private enterprise repositories"
                ],
                correct_answer="No, forking public repositories is entirely self-service and can be done freely without maintainer permissions",
                explanation="Public open-source repositories are freely forkable by any registered user."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 39: Pull Requests (PRs) / Merge Requests
    # ----------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Pull Requests (PRs) / Merge Requests",
        concept="Engineering professional Pull Requests (PRs) and Merge Requests (MRs): PR templates, scope containment, and automated CI check integration.",
        analogy="A Pull Request is like presenting a formal proposal at an architectural firm. You don't just dump construction materials on the floor; you present the blueprints, explain the benefits, show safety inspection test results, and invite senior architects to review your plans before anyone pours concrete.",
        theory_sections=[
            {
                "heading": "What is a Pull Request (PR)?",
                "body": (
                    "A Pull Request (known as a **Merge Request** in GitLab) is a mechanism for telling a team: "
                    "'I have pushed changes to branch X; please review my code diff, discuss potential design improvements, and pull it into branch Y.' "
                    "It is the central nexus of modern code collaboration."
                )
            },
            {
                "heading": "Anatomy of an Exceptional Pull Request",
                "body": (
                    "1. **Clear, Descriptive Title**: Follows conventional commit format (e.g. `feat(auth): add OAuth2 refresh token handling`).\n"
                    "2. **The 'Why' Context**: Explains the business problem or bug being solved, linking to relevant issue tickets (`Fixes #142`).\n"
                    "3. **Visual Proof**: Screenshots, GIF recordings, or CLI logs demonstrating that the feature works as expected.\n"
                    "4. **Automated Testing**: Unit, integration, or end-to-end tests validating that regressions cannot occur."
                )
            },
            {
                "heading": "PR Size and Reviewability",
                "body": (
                    "Studies across Google and Microsoft show that code review quality drops exponentially when a PR exceeds **400 lines of code**. "
                    "Small, focused PRs are reviewed and merged 3x faster, with significantly fewer production defects."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating Branch and Pushing for PR",
                "code": "# 1. Create a focused branch:\ngit switch -c feat/dark-mode-toggle\n\n# 2. Commit atomic changes with clear message:\ngit add src/theme.js\ngit commit -m \"feat: implement dark mode toggle switch\"\n\n# 3. Push to remote:\ngit push -u origin feat/dark-mode-toggle\n\n# GitHub prints direct terminal link to open PR:\n# https://github.com/org/repo/pull/new/feat/dark-mode-toggle",
                "explanation": "Pushes branch and exposes direct URL to create PR."
            },
            {
                "title": "Using GitHub CLI (gh) to Open PR from Terminal",
                "code": "# Create PR directly from command line using GitHub CLI:\ngh pr create \\\n  --title \"feat: implement dark mode toggle switch\" \\\n  --body \"Resolves #142. Adds user toggle for dark mode and persists preference to localStorage.\" \\\n  --reviewer techlead,janedev",
                "explanation": "Automates PR creation without opening web browser."
            },
            {
                "title": "PR Template (.github/pull_request_template.md)",
                "code": "# Sample template markdown:\n## Summary\nBrief description of changes.\n\n## Motivation / Context\nFixes #<issue_number>\n\n## Checklist\n- [ ] Unit tests added\n- [ ] Linter passing\n- [ ] Tested on mobile and desktop",
                "explanation": "Enforces consistent documentation across team contributors."
            },
            {
                "title": "Responding to PR Feedback",
                "code": "# Simply push new commits to your branch—the PR updates automatically!\necho '/* fix reviewer comment */' >> src/theme.js\ngit commit -am \"refactor: address reviewer feedback on contrast ratio\"\ngit push",
                "explanation": "Existing PR updates live with every push to that branch."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate Branch and Push for PR",
            description="Write the sequence to create branch 'fix/login-bug', commit a change with message 'fix: handle null password', and push setting upstream tracking.",
            starter_code="# Create branch, commit, and push with upstream\n",
            solution_code="git switch -c fix/login-bug\ngit commit -am \"fix: handle null password\"\ngit push -u origin fix/login-bug",
            expected_output="Branch 'fix/login-bug' set up to track remote branch 'fix/login-bug'..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the term used in GitLab for what GitHub calls a 'Pull Request'?",
                options=["Merge Request (MR)", "Code Proposal", "Patch Ticket", "Sync Request"],
                correct_answer="Merge Request (MR)",
                explanation="GitLab refers to code review requests as Merge Requests."
            ),
            QuizQuestionBlueprint(
                question="According to software engineering research at Google and Microsoft, what happens to code review thoroughness when a PR exceeds ~400 lines of code?",
                options=[
                    "Reviewer defect detection drops drastically as reviewers experience cognitive fatigue and tend to rubber-stamp the PR",
                    "Reviewers find 10x more bugs",
                    "The code runs faster",
                    "GitHub blocks the PR from merging"
                ],
                correct_answer="Reviewer defect detection drops drastically as reviewers experience cognitive fatigue and tend to rubber-stamp the PR",
                explanation="Smaller PRs (<400 lines) result in dramatically higher defect detection and faster turnaround."
            ),
            QuizQuestionBlueprint(
                question="When a code reviewer asks for changes on your open Pull Request, what is the proper procedure?",
                options=[
                    "Make the requested changes locally, commit, and push to the same feature branch; the PR updates automatically",
                    "Close the PR, delete your branch, and open an entirely new repository",
                    "Email the reviewer your modified files",
                    "Force-push directly to the `main` branch"
                ],
                correct_answer="Make the requested changes locally, commit, and push to the same feature branch; the PR updates automatically",
                explanation="Pull Requests continuously track their source branch; pushing commits updates the PR."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of adding a `.github/pull_request_template.md` file to a repository?",
                options=[
                    "It pre-populates the PR description box with a standardized checklist and prompts for context",
                    "It compiles the code before PR creation",
                    "It automatically merges PRs",
                    "It pays reviewers a bonus"
                ],
                correct_answer="It pre-populates the PR description box with a standardized checklist and prompts for context",
                explanation="PR templates provide structured prompts for testing, issue links, and documentation."
            ),
            QuizQuestionBlueprint(
                question="Which official command-line tool allows developers to create, review, and merge Pull Requests directly inside the terminal without opening a browser?",
                options=["The GitHub CLI (`gh`)", "Git Bash", "Git GUI", "npm"],
                correct_answer="The GitHub CLI (`gh`)",
                explanation="The GitHub CLI (`gh`) provides complete terminal management of PRs, issues, and releases."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 40: Code Review Best Practices
    # ----------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Code Review Best Practices",
        concept="Developing constructive, high-empathy code review standards: separating automated linting from human architectural critique, nitpicks, and empathy.",
        analogy="Code review is not a spelling test or an interrogation where you prove you are smarter than your teammate. It is a safety co-pilot check in an airplane cockpit: both pilots want to land the plane safely without the engines catching fire.",
        theory_sections=[
            {
                "heading": "The Purpose of Code Review",
                "body": (
                    "Code review serves three critical organizational goals:\n"
                    "1. **Quality & Correctness**: Catching bugs, race conditions, edge cases, and security vulnerabilities.\n"
                    "2. **Knowledge Sharing**: Spreading domain knowledge across the team so no single developer is an isolated bottleneck.\n"
                    "3. **Consistency**: Ensuring long-term architecture aligns with company coding standards."
                )
            },
            {
                "heading": "Human Review vs Automated Checks",
                "body": (
                    "**Never argue about formatting, whitespace, or style rules in a human code review!** "
                    "Linters (ESLint, Black, Prettier) and CI bots should automatically reject formatting violations. "
                    "Human reviews should focus on architectural decisions, security implications, data race conditions, and business logic clarity."
                )
            },
            {
                "heading": "Conventional Comments Framework",
                "body": (
                    "Label review feedback with explicit intent prefixes:\n"
                    "- `praise:` Highlight brilliant solutions or clean design.\n"
                    "- `nitpick (or nit):` Minor stylistic preference that does not block approval.\n"
                    "- `question:` Seeking clarification without implying the code is wrong.\n"
                    "- `blocking / issue:` Critical defect or security flaw requiring resolution before merge."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Poor vs Empathetic Review Comments",
                "code": "# POOR REVIEW COMMENTS:\n# - \"This is bad.\"\n# - \"Why didn't you use a hashmap here?\"\n# - \"Fix this formatting.\"\n\n# EMPATHETIC, ACTIONABLE COMMENTS:\n# - \"praise: Love how you simplified this recursion into an iterative loop!\"\n# - \"question: If the network drops during this await call, what prevents duplicate billing charges?\"\n# - \"nit: We could extract this magic number 86400 into a named constant SECONDS_IN_A_DAY for readability.\"",
                "explanation": "Clear prefixes prevent tone misinterpretations across text."
            },
            {
                "title": "Automating Style Verification with Pre-Commit Hooks",
                "code": "# In package.json or git hooks:\n# Enforce linting and formatting before commits can even be created\nnpm run lint && npm run test",
                "explanation": "Eliminates stylistic debates from human code reviews."
            },
            {
                "title": "Checking Out a Coworker's PR Locally for Testing",
                "code": "# Using GitHub CLI to pull and test coworker's PR #42 locally:\ngh pr checkout 42\n\n# Run local test suite:\npytest tests/",
                "explanation": "Allows hands-on testing of PR branches."
            },
            {
                "title": "Approving and Merging via Terminal",
                "code": "# Review and merge from command line:\ngh pr review --approve -b \"LGTM! Architecture looks solid.\"\ngh pr merge --squash --delete-branch",
                "explanation": "Approves and executes clean squash-and-delete workflow."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Checkout Coworker PR Locally",
            description="Write the GitHub CLI command to check out Pull Request number 105 to your local workspace for manual verification.",
            starter_code="# Checkout PR 105 using gh\n",
            solution_code="gh pr checkout 105",
            expected_output="Switched to branch '...'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What should human code reviewers focus on rather than arguing about whitespace or formatting?",
                options=[
                    "System architecture, security risks, business logic correctness, and edge-case handling",
                    "Font size and monitor resolutions",
                    "Which text editor the author used",
                    "Fixing punctuation in comments"
                ],
                correct_answer="System architecture, security risks, business logic correctness, and edge-case handling",
                explanation="Automated tools handle formatting; humans review logic and architecture."
            ),
            QuizQuestionBlueprint(
                question="In the 'Conventional Comments' code review standard, what does the `nit:` or `nitpick:` label signal to the PR author?",
                options=[
                    "A minor, non-blocking suggestion that the author can address or ignore without holding up PR approval",
                    "A critical security emergency requiring immediate shutdown",
                    "That the PR is rejected",
                    "That the author should be fired"
                ],
                correct_answer="A minor, non-blocking suggestion that the author can address or ignore without holding up PR approval",
                explanation="`nit:` explicitly conveys that the comment is optional and non-blocking."
            ),
            QuizQuestionBlueprint(
                question="What does the common developer review acronym 'LGTM' stand for?",
                options=[
                    "Looks Good To Me",
                    "Let's Go To Meet",
                    "Linux General Template Module",
                    "Large Git Test Merge"
                ],
                correct_answer="Looks Good To Me",
                explanation="LGTM indicates approval after reviewing code."
            ),
            QuizQuestionBlueprint(
                question="Why is it best practice to automate linting and formatting via CI rather than during code review?",
                options=[
                    "It removes emotional arguments about style, saves valuable engineering review time, and guarantees consistency",
                    "Linters cost money to run manually",
                    "Developers dislike reading code",
                    "Git will reject unlinted files automatically"
                ],
                correct_answer="It removes emotional arguments about style, saves valuable engineering review time, and guarantees consistency",
                explanation="Automated enforcement frees humans to focus on higher-level architecture."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended attitude during peer code reviews?",
                options=[
                    "High empathy, psychological safety, and viewing review as collaborative learning rather than judgment",
                    "Aggressive criticism to find every flaw",
                    "Rejecting every first attempt to test perseverance",
                    "Approving everything instantly without reading"
                ],
                correct_answer="High empathy, psychological safety, and viewing review as collaborative learning rather than judgment",
                explanation="Psychological safety fosters collaborative software craftsmanship."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 41: Popular Workflows (Gitflow, GitHub Flow, Trunk-Based)
    # ----------------------------------------------------
    DayBlueprint(
        order=41,
        title="Day 41: Popular Workflows (Gitflow, GitHub Flow, Trunk-Based)",
        concept="Architecting branching models for engineering teams: evaluating Gitflow (traditional releases), GitHub Flow (continuous deployment), and Trunk-Based Development (high velocity).",
        analogy="Branching workflows are like company traffic rules. Gitflow is a heavy freight train system with strict depots and track schedules. GitHub Flow is a fleet of express courier delivery vans. Trunk-Based Development is a high-speed bullet train where everyone rides on one main track with short pit-stops.",
        theory_sections=[
            {
                "heading": "Comparing the 3 Major Branching Strategies",
                "body": (
                    "Different engineering organizations adopt different branching strategies based on deployment frequency and team size."
                )
            },
            {
                "heading": "1. Gitflow (Traditional / Scheduled Releases)",
                "body": (
                    "Designed by Vincent Driessen in 2010. Employs multiple long-lived branches:\n"
                    "- `main`: Contains strictly production releases tagged with SemVer.\n"
                    "- `develop`: The central integration branch for next-release features.\n"
                    "- Supporting branches: `feature/*` (spawns from develop), `release/*` (prepares release), `hotfix/*` (spawns from main for urgent production patches).\n"
                    "Ideal for: Embedded software, mobile apps with slow app-store reviews, or enterprise software with strict quarterly release schedules."
                )
            },
            {
                "heading": "2. GitHub Flow (Lightweight & Continuous)",
                "body": (
                    "A radically simpler model for web applications deployed continuously:\n"
                    "- Anything in `main` is deployable.\n"
                    "- To work on something new, create a descriptive branch off `main`.\n"
                    "- Push to remote and open a Pull Request.\n"
                    "- Merge to `main` and deploy immediately."
                )
            },
            {
                "heading": "3. Trunk-Based Development (High Velocity DevOps)",
                "body": (
                    "The gold standard at modern high-velocity companies (Google, Meta, Netflix). "
                    "Developers merge small, frequent commits into the single `trunk` (main) multiple times per day. "
                    "Incomplete features are hidden behind **Feature Flags** (Feature Toggles) in production rather than isolated on long-lived branches."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Gitflow Branching Topology",
                "code": "# main:    v1.0 ------------------------------- v1.1\n#                 \\                         /\n# release:         +--- 1.1-rc1 --- 1.1-rc2+\n#                             /\n# develop: ---------*--------*-------------------\n#                    \\\n# feature:            +-- feat-a --+",
                "explanation": "Multiple long-lived branches coordinating release stages."
            },
            {
                "title": "GitHub Flow Topology",
                "code": "# main:  ================*=======================*===> (Always Deployable)\n#                         \\                     /\n# feature:                 +-- fix/navbar-bug -+ (PR & Merge)",
                "explanation": "Simple, short-lived branch workflow."
            },
            {
                "title": "Trunk-Based Feature Flag Concept",
                "code": "# In Trunk-Based Development, code is merged to main daily,\n# but hidden behind runtime feature toggles:\n\nif feature_flags.is_enabled(\"new_checkout_ui\", user):\n    render_new_checkout()\nelse:\n    render_legacy_checkout()",
                "explanation": "Decouples code deployment from feature release."
            },
            {
                "title": "Cleaning Up Local Branches in Trunk-Based Flow",
                "code": "# Trunk-based developers constantly prune short-lived branches:\ngit switch main\ngit pull --rebase\ngit branch -d feature/quick-fix",
                "explanation": "Maintains a clean local working tree."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Clean Up Merged Branch",
            description="Switch to 'main', pull upstream updates, and safely delete a local merged branch named 'feature/done'.",
            starter_code="# Switch to main, pull, and delete feature/done safely\n",
            solution_code="git switch main\ngit pull\ngit branch -d feature/done",
            expected_output="Deleted branch feature/done (was ...)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which branching strategy uses long-lived `main`, `develop`, `release/*`, `feature/*`, and `hotfix/*` branches?",
                options=["Gitflow", "GitHub Flow", "Trunk-Based Development", "One-Branch Flow"],
                correct_answer="Gitflow",
                explanation="Gitflow is famous for its formal multi-branch structure for scheduled releases."
            ),
            QuizQuestionBlueprint(
                question="What is the foundational rule of GitHub Flow?",
                options=[
                    "Anything in the `main` branch is always stable, tested, and deployable to production",
                    "Developers can only push code once a week",
                    "Every branch must have 5 reviewers",
                    "There are no branches allowed"
                ],
                correct_answer="Anything in the `main` branch is always stable, tested, and deployable to production",
                explanation="GitHub Flow is optimized for continuous deployment where main is always release-ready."
            ),
            QuizQuestionBlueprint(
                question="In Trunk-Based Development, how do developers merge unfinished features into `main` without exposing broken code to users?",
                options=[
                    "By hiding incomplete code paths behind Feature Flags (toggles)",
                    "By commenting out the code",
                    "By encrypting the files",
                    "By renaming files to `.secret`"
                ],
                correct_answer="By hiding incomplete code paths behind Feature Flags (toggles)",
                explanation="Feature flags decouple code deployment from feature exposure to end-users."
            ),
            QuizQuestionBlueprint(
                question="Why have many modern web engineering teams transitioned away from Gitflow to Trunk-Based Development?",
                options=[
                    "Long-lived branches in Gitflow cause massive merge conflicts ('merge hell') and delay continuous feedback",
                    "Gitflow is illegal in open source",
                    "Gitflow only works on SVN",
                    "Gitflow consumes too much electricity"
                ],
                correct_answer="Long-lived branches in Gitflow cause massive merge conflicts ('merge hell') and delay continuous feedback",
                explanation="Long-lived branches diverge heavily, leading to painful integration bottlenecks."
            ),
            QuizQuestionBlueprint(
                question="In Gitflow, from which branch is an emergency `hotfix/*` branch cut to patch a production vulnerability?",
                options=["Directly from `main`", "From `develop`", "From a feature branch", "From a stash"],
                correct_answer="Directly from `main`",
                explanation="Hotfixes branch directly from `main` and are merged back into both `main` and `develop`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 42: Finding authors with git blame
    # ----------------------------------------------------
    DayBlueprint(
        order=42,
        title="Day 42: Finding authors with `git blame`",
        concept="Investigating line-by-line file history, authorship, commit hashes, and commit dates using `git blame` to diagnose bugs and understand architectural rationale.",
        analogy="`git blame` is not about finding someone to yell at or fire; it is like reading the signature and timestamp stamped on every brick of a skyscraper so you can call the engineer who placed that brick and ask: 'Why did you put a load-bearing column here?'",
        theory_sections=[
            {
                "heading": "The Purpose of `git blame`",
                "body": (
                    "When troubleshooting a legacy codebase, you often encounter a perplexing line of code: e.g. `timeout = 42.5;`. "
                    "Why 42.5? Who wrote it? Which issue ticket prompted it? "
                    "`git blame <file>` displays the file annotated line-by-line with the commit hash, author name, timestamp, and line number."
                )
            },
            {
                "heading": "Filtering Line Ranges (`-L`)",
                "body": (
                    "Blaming an entire 3,000-line file can flood your terminal. "
                    "Use `-L <start>,<end>` to blame only the specific lines you care about (e.g. `git blame -L 120,135 src/auth.py`)."
                )
            },
            {
                "heading": "Ignoring Whitespace and Formatting Noise (`-w`)",
                "body": (
                    "If someone ran an automatic code formatter (like Prettier or Black) across the whole project, "
                    "`git blame` might show the formatter's author on every line! "
                    "Passing `-w` (ignore whitespace) or configuring `.git-blame-ignore-revs` skips formatting revisions to reveal the true original author."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Line Range with git blame",
                "code": "# Blame lines 10 to 15 of auth.js:\ngit blame -L 10,15 src/auth.js\n\n# Output:\n# 7a4e8c1d (Alice Dev 2023-08-14 14:22:01 -0400 10) const TOKEN_EXPIRY = 3600;\n# 4b2c1d0f (Bob Smith 2023-09-02 09:15:33 -0400 11) function verifyToken(token) {",
                "explanation": "Annotates exact line author, timestamp, and commit SHA."
            },
            {
                "title": "Ignoring Whitespace Changes",
                "code": "# Skip trivial indentation or formatting changes to find real author:\ngit blame -w -L 50,60 src/database.py",
                "explanation": "Ignores whitespace-only commits."
            },
            {
                "title": "Showing Author Email Instead of Name",
                "code": "# Display author email address for direct outreach:\ngit blame -e -L 1,5 README.md\n# 7a4e8c1d (<alice@dev.io> 2023-01-10 1) # Project Overview",
                "explanation": "Displays author email directly in blame annotations."
            },
            {
                "title": "Ignoring Massive Reformatting Commits Globally",
                "code": "# Tell git blame to ignore cosmetic reformatting commits listed in a file:\ngit config --global blame.ignoreRevsFile .git-blame-ignore-revs",
                "explanation": "Standard enterprise practice when adopting automated linters."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Blame Specific Line Range with Whitespace Ignored",
            description="Run `git blame` on file 'app.py' restricted to lines 1 to 10 while ignoring whitespace modifications with the `-w` flag.",
            starter_code="# Run git blame on lines 1 to 10 of app.py with -w\n",
            solution_code="git blame -w -L 1,10 app.py",
            expected_output="... (Author Date Line#) ..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What information does `git blame <filename>` display for each line of a file?",
                options=[
                    "The commit hash, author name, timestamp, and line content of who last modified that line",
                    "A list of syntax errors in that line",
                    "How much memory that line consumes",
                    "The download speed of the file"
                ],
                correct_answer="The commit hash, author name, timestamp, and line content of who last modified that line",
                explanation="`git blame` annotates each line with historical authorship and commit provenance."
            ),
            QuizQuestionBlueprint(
                question="Which flag restricts `git blame` to a specific line range, such as lines 25 to 50?",
                options=["-L 25,50", "-r 25-50", "--lines 25:50", "-s 25,50"],
                correct_answer="-L 25,50",
                explanation="The `-L <start>,<end>` flag scopes blame to a designated line window."
            ),
            QuizQuestionBlueprint(
                question="Why is the `-w` flag useful when running `git blame`?",
                options=[
                    "It ignores whitespace-only changes, preventing code-formatter commits (like Prettier or Black) from masking the true original author",
                    "It writes the output to a Word document",
                    "It warns you of bugs",
                    "It runs only on Wednesdays"
                ],
                correct_answer="It ignores whitespace-only changes, preventing code-formatter commits (like Prettier or Black) from masking the true original author",
                explanation="`-w` filters out cosmetic whitespace changes to uncover semantic code authors."
            ),
            QuizQuestionBlueprint(
                question="What is the primary professional purpose of using `git blame` in software engineering?",
                options=[
                    "To understand the historical context, issue ticket, and rationale behind a puzzling piece of code",
                    "To publicly shame junior developers in company Slack channels",
                    "To calculate employee salaries",
                    "To delete old code"
                ],
                correct_answer="To understand the historical context, issue ticket, and rationale behind a puzzling piece of code",
                explanation="Blame leads you directly to the commit message explaining why the code exists."
            ),
            QuizQuestionBlueprint(
                question="Which file can be configured via `blame.ignoreRevsFile` to permanently hide mass-refactoring commits from `git blame`?",
                options=[".git-blame-ignore-revs", ".gitignore", ".gitmodules", ".gitattributes"],
                correct_answer=".git-blame-ignore-revs",
                explanation="`.git-blame-ignore-revs` contains a list of commit hashes to skip during blame inspection."
            )
        ]
    )
]
