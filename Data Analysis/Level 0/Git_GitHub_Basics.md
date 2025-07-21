
# Git & GitHub Basics  
_A Beginner’s Guide to Version Control and Collaboration_

## What is Git?

**Git** is a free and open-source version control system. It helps you:

- Track changes in your code over time
- Work on different versions (branches) of a project
- Revert to earlier versions if needed
- Collaborate with others without overwriting each other’s work

Think of Git as a time machine for your project.

---

## What is GitHub?

**GitHub** is a platform that hosts your Git repositories online. It adds powerful features like:

- Remote backup of your code
- Collaboration tools (pull requests, issues, etc.)
- Web interface for your projects
- Portfolio for developers and data analysts

---

## Installing Git

Download and install Git from:  
--> [https://git-scm.com/downloads](https://git-scm.com/downloads)

After installation, verify by running:

```bash
git --version
```

---

## Basic Git Commands

| Command | Purpose |
|--------|---------|
| `git init` | Initialize a new Git repository |
| `git status` | Check the current state of your repo |
| `git add <file>` | Stage file(s) for committing |
| `git commit -m "message"` | Save your staged changes with a message |
| `git log` | View commit history |
| `git diff` | See changes not yet staged |
| `git clone <url>` | Download a repository from GitHub |
| `git push` | Upload local changes to GitHub |
| `git pull` | Download latest changes from GitHub |

---

## Typical Workflow

```bash
# Clone a GitHub repo
git clone https://github.com/yourusername/data-analysis.git
cd data-analysis

# Make changes and track them
git add .
git commit -m "Add new analysis script"
git push origin main
```

---

## Working with Branches

Branches help isolate features or fixes before merging into the main codebase.

```bash
# Create a new branch
git checkout -b feature-branch

# Switch to main branch
git checkout main

# Merge changes from another branch
git merge feature-branch
```

---

## Collaborating on GitHub

- **Fork**: Make a copy of someone else's repository under your account
- **Clone**: Download the repository to your machine
- **Pull Request**: Propose your changes to be merged
- **Issue**: Report bugs or suggest improvements

---

## Best Practices

- Use meaningful commit messages
- Push changes frequently
- Pull before starting new work
- Keep your main branch clean and functional
- Review code before merging pull requests

---

## Useful GitHub Features

- **README.md**: Explains your project
- **.gitignore**: Tells Git which files/folders to ignore
- **GitHub Actions**: Automate workflows like testing
- **GitHub Pages**: Host web pages from your repo

---

## Test Your Knowledge

- Create a new repository
- Clone it locally
- Make changes and commit
- Push your changes to GitHub
- Create a pull request on a different branch

---

## Final Thoughts

Git and GitHub are essential tools for any data analyst or developer. They allow you to manage your code, collaborate with others, and build a professional portfolio.

Keep practicing - it will soon become second nature.
