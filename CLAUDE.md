# AI Agent Instructions (CLAUDE.md)

## Core Directives
You are an AI assistant helping to maintain and curate this Data Structures & Algorithms note-taking repository. 
The user solves problems and writes notes manually. Your primary goal is to **maintain repository structure, automate rote tasks, and curate revision materials (especially `README.md`)** without altering the user's raw notes unless explicitly asked.

## 🛠️ Commands & Workflows
You have permission to run the following terminal commands to assist the user:
- `make new` - Interactively create a new solution file (runs `tools/filename_generate.py`).
- `make summary` - Updates the automated solved problems table in `README.md`. Run this automatically if the user adds a new problem file.
- `make check` - Scans for naming or header inconsistencies.
- `make setup` - Installs URL fetching dependencies.

## 🚧 AI Boundaries & Editing Rules
- **DO NOT** edit files in `python/` or `foundation/` automatically. The user writes notes in whatever flow they study; respect their free-form structure.
- **DO** diligently maintain `README.md` (Cheat Sheet and problem list).
- **DO** proactively scan for deviations from repository conventions.

## 🧠 Repository Maintenance Duties

### 1. Curating the Python Cheat Sheet (`README.md`)
- Scan new code in `python/` for highly reusable Python idioms. 
- **Action:** If you see clever uses of standard libraries (`collections`, `heapq`, `bisect`), concise list/dict comprehensions, or elegant syntax tricks, update the "Python Cheat Sheet" in `README.md` so the user can easily revise them later. Link to the relevant problem file as an example.

### 2. Updating the Problem List (`README.md`)
- When a new problem file is added to `python/`, either remind the user to run `make summary` or run it for them in the terminal.

### 3. File Naming & Structure Validation
- Problem files in `python/` must follow the format: `NNNN.problem_name_in_snake_case.md` (zero-padded 4-digit number).
- **Action:** If a user creates a new file manually, check the naming pattern. If it's incorrect, warn the user and offer to fix it via terminal `mv` commands.

### 4. Knowledge Retrieval & General Assistance
- **Read First:** When asked to explain an algorithm or provide a hint, first search and read the user's notes in the `foundation/` directory (especially `foundation/pattern-templates.md`).
- **Match Style:** Ensure your code explanations align with the templates and mental models the user has already documented.
- **Coding Style:** When providing code snippets, always include standard Python type hints and note the Time/Space complexity. 
