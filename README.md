# AO* Based Smart Study Task Planner

A beginner-friendly, terminal-based Artificial Intelligence project built with
Python's standard library.

## Features

- Three sample goals: DSA, Python, and AI exam preparation.
- Explicit AND-OR task graph.
- AO* search with heuristic estimates and cost evaluation.
- Chooses between alternative ways of completing a task.
- Displays the selected plan and estimated effort in hours.
- No database, web framework, or third-party package required.

## Requirements

- Python 3.8 or newer
- Windows, macOS, or Linux terminal

## Run the project

1. Extract `AO_Study_Planner.zip`.
2. Open the extracted `AO_Study_Planner` folder.
3. Open Command Prompt / Terminal in that folder.
4. Run:

   ```bash
   python main.py
   ```

   On some systems, use:

   ```bash
   python3 main.py
   ```

## Project files

- `main.py` — terminal menu and program flow.
- `tasks.py` — sample goals and AND-OR task graphs.
- `ao_star.py` — AO* search implementation.

## How the graph works

Each node contains:
- `cost`: effort spent at that node, in hours.
- `heuristic`: estimated minimum remaining effort.
- `options`: OR alternatives. Each option is a list of children that are
  all required together (an AND group).

For example:

```python
"practice": {
    "name": "Practice DSA",
    "cost": 0,
    "heuristic": 1,
    "options": [
        ["arrays", "linked_lists"],
        ["mixed_questions"]
    ]
}
```

The first option means both array and linked-list practice are required.
The second option is an alternative: solve mixed questions instead.

## Important note about estimates

The sample hour values and heuristics are illustrative. Change them in
`tasks.py` to match your team's assumptions. For the AO* optimality
guarantee, heuristic values should be admissible lower bounds (they should
not overestimate the actual minimum remaining effort). The supplied graph
is finite and acyclic.

## Suggested project extensions

- Allow students to enter their own task graph.
- Add a difficulty or priority field.
- Let the user mark completed tasks.
- Save plans to a simple text file.
