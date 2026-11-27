# Git and GitHub workflow

A quick reference for managing the credit card fraud detection project through the VS Code terminal.

## 1. Before starting a coding session

Open the project root in VS Code and open the integrated terminal.

```powershell
git status
git pull --ff-only
```

Check that local changes are committed or safely backed up before pulling. If the pull fails, inspect the error rather than forcing an update.

## 2. After completing a meaningful piece of work

Save your files in VS Code, then run:

```powershell
git status
git add <file-or-folder>
git diff --cached --stat
git commit -m "Describe what you changed"
git push
```

Replace `<file-or-folder>` with the actual path. Stage only the files you intend to commit.

### Example

```powershell
git add src/main.py requirements.txt
git commit -m "Add FastAPI application and health check endpoint"
git push
```

## 3. Common commands

| Command | Purpose |
|---|---|
| `git status` | Inspect local changes and branch status |
| `git pull --ff-only` | Download and safely fast-forward to remote changes |
| `git add <path>` | Stage selected changes |
| `git diff` | Review unstaged tracked changes |
| `git diff --cached` | Review staged changes before committing |
| `git commit -m "message"` | Save a version locally |
| `git push` | Upload local commits to GitHub |
| `git log -5 --oneline` | View the five most recent commits |
| `git remote -v` | Check which remote repository is connected |

## 4. Temporarily saving unfinished work

```powershell
git stash push -u -m "Work in progress"
git stash list
```

To restore the saved changes when safe:

```powershell
git stash apply 'stash@{0}'
```

Check the restored files before dropping the stash. Applying a stash can cause conflicts if the same files have changed since it was created.

## 5. Good habits

- Use Git through VS Code instead of manually uploading files to GitHub.
- Commit after each meaningful milestone, not every minor edit.
- Use short, descriptive commit messages.
- Review staged files before committing.
- Never commit secrets, API keys, credentials, virtual environments or excluded datasets.
- Check `.gitignore` before adding generated files or model artefacts.
- If a notebook changes on disk after pulling, close and reopen its tab. Do not save an outdated editor copy over the new file.
- Avoid force pushes and destructive reset commands unless you understand their consequences.

## 6. Next Git skills to learn

- Branching
- Pull requests
- Merge conflict resolution
- Collaborative code reviews
