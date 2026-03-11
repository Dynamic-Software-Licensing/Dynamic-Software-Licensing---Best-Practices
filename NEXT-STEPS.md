# Next Steps

## 1. Push to GitHub

```bash
cd /Users/thomaspister/Documents/dynamic-software-licensing

# Set Git identity (if not already set)
git config user.name "Your Name"
git config user.email "you@example.com"

# Connect to new empty GitHub repo and push
git remote add origin https://github.com/YOUR-ORG/YOUR-REPO.git
git push -u origin main
```

## 2. GitHub Repository Settings

After pushing, configure the following in GitHub → Settings:

### Actions → General
- Workflow permissions: **Read and write permissions**
- Allow GitHub Actions to create and approve pull requests: **on**
- If auto-Draft-PR still fails: add `PR_BOT_TOKEN` secret (PAT with `repo` scope)

### Branches → Add branch ruleset for `main`
- Require a pull request before merging
- Required approvals: 1 (or 2 for normative content)
- Dismiss stale reviews when new commits are pushed
- Required status checks before merging:
  - `Validate branch naming convention`
  - `Validate PR description`
  - `Check status fields in changed chapter index files`
  - `Lint markdown files`
- Restrict direct pushes to `main`
- Allow force pushes: off

### Pull Requests
- Automatically delete head branches: **on**
- Require conversation resolution before merging: **on**

## 3. GitHub Project

Create a new GitHub Project (board view):

Required fields to add:
- `Status` (Single select): Backlog / Ready / Drafting / Review / Editor Decision / Done / Deferred
- `Chapter` (Text)
- `Type` (Single select): Editorial / Terminology / Informative / Normative / Structural
- `Priority` (Single select): P1 / P2 / P3
- `Owner` (Person)
- `Reviewer` (Person)
- `Editor` (Person)
- `Target Date` (Date)
- `Milestone` (Text)
- `Blocked` (Single select): Yes / No

Recommended automations in Project:
- PR opened as Draft → Status: `Drafting`
- PR set to Ready for review → Status: `Review`
- PR merged → Status: `Done`
- Issue closed → Status: `Done`

## 4. GitHub Labels

Create the following labels (used by auto-label Action):
- `chapter`
- `annex`
- `schema`
- `diagram`
- `governance`
- `workflow`
- `terminology`
- `change-request`
- `editorial`

## 5. First Milestone

Once the repo and project are set up:

1. Define Milestone M1 in GitHub (Milestones → New milestone)
2. Create 3–5 issues using the issue templates
3. Assign Owner, Reviewer, Editor, deadline per issue
4. Add all issues to the Project
5. Contributors create branches and start working

## 6. Key Files in This Repo

| File | Purpose |
|---|---|
| `WORKFLOW.md` | Team operating model: milestones, issues, roles, delivery |
| `GOVERNANCE.md` | Roles, status definitions, editorial rules |
| `CONTRIBUTING.md` | Branch, PR, git commands, writing rules |
| `README.md` | Entry point and navigation |
| `.github/workflows/` | All GitHub Actions automations |
| `.github/ISSUE_TEMPLATE/` | Issue templates: change-request, editorial, terminology |
| `.github/pull_request_template.md` | PR template with checklist validation |
