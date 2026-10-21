# AGENTS.md

## Rules (must follow)

### Responses
- Keep answers short and simple, unless I ask for more.
- Use English for basic response. But for real case, variables, or data, use the real data

### Planning
- Always ask questions first. Never assume the design, tools, or features.
- Use sub-agents to research and to double-check the plan before showing it to me.

### Making changes
- Don't do the work yourself when possible. Use sub-agents.
- Split the plan into parts that can run in parallel, and act only as the coordinator.
- Use a strong model for hard tasks (like coding) and a cheaper one for easy tasks (like docs).
- After every change, check your work. This project has no automatic checks, so manually confirm that the front end and back end still match up.
- Always update code changes to CHANGELOG.md efficiently. do not make it too wordy.

---

## About this project

A qr generator from any link/web address using python only