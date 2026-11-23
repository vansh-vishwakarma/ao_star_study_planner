
def get_goals():
    return [
        "Prepare for DSA Exam",
        "Prepare for Python Exam",
        "Prepare for AI Exam",
    ]

def leaf(name, hours):
    """Create a task that has no subtasks."""
    return {
        "name": name,
        "cost": hours,
        "heuristic": 0,
        "options": [],
    }


def internal(name, heuristic, options):
    """Create a goal with one or more alternative task groups."""
    return {
        "name": name,
        "cost": 0,
        "heuristic": heuristic,
        "options": options,
    }


def build_task_graph(goal_name):
    """Return (graph, start_node) for the selected goal."""

    if goal_name == "Prepare for DSA Exam":
        graph = {
            "goal": internal("Prepare for DSA Exam", 3.0,
                             [["concepts", "practice", "revision"]]),

            "concepts": internal("Study DSA concepts", 1.0,
                                 [["read_notes"], ["watch_lectures"]]),
            "practice": internal("Practice DSA questions", 1.0,
                                 [["arrays", "linked_lists"],
                                  ["mixed_questions"]]),
            "revision": internal("Revise for DSA", 1.0,
                                 [["previous_papers", "mock_test"]]),

            "read_notes": leaf("Read class notes", 2.0),
            "watch_lectures": leaf("Watch topic lectures", 2.5),
            "arrays": leaf("Practice array questions", 1.5),
            "linked_lists": leaf("Practice linked-list questions", 2.0),
            "mixed_questions": leaf("Solve mixed DSA questions", 4.0),
            "previous_papers": leaf("Solve previous-year papers", 2.0),
            "mock_test": leaf("Attempt a timed mock test", 1.0),
        }
        return graph, "goal"

    if goal_name == "Prepare for Python Exam":
        graph = {
            "goal": internal("Prepare for Python Exam", 3.0,
                             [["concepts", "coding", "revision"]]),
            "concepts": internal("Learn Python concepts", 1.0,
                                 [["read_notes"], ["watch_lectures"]]),
            "coding": internal("Practice Python programming", 1.0,
                               [["basic_programs", "functions_oop"],
                                ["mini_project"]]),
            "revision": internal("Revise Python", 1.0,
                                 [["important_questions", "mock_test"]]),
            "read_notes": leaf("Read Python class notes", 2.0),
            "watch_lectures": leaf("Watch Python topic lectures", 2.5),
            "basic_programs": leaf("Practice basic Python programs", 1.5),
            "functions_oop": leaf("Practice functions and OOP programs", 2.0),
            "mini_project": leaf("Build a small Python practice project", 4.0),
            "important_questions": leaf("Revise important questions", 2.0),
            "mock_test": leaf("Attempt a Python mock test", 1.0),
        }
        return graph, "goal"

    if goal_name == "Prepare for AI Exam":
        graph = {
            "goal": internal("Prepare for AI Exam", 3.0,
                             [["concepts", "search", "revision"]]),
            "concepts": internal("Study AI concepts", 1.0,
                                 [["read_notes"], ["watch_lectures"]]),
            "search": internal("Practice AI search algorithms", 1.0,
                               [["uninformed", "informed"],
                                ["solve_search_problems"]]),
            "revision": internal("Revise AI topics", 1.0,
                                 [["important_questions", "mock_test"]]),
            "read_notes": leaf("Read AI class notes", 2.0),
            "watch_lectures": leaf("Watch AI topic lectures", 2.5),
            "uninformed": leaf("Practice BFS and DFS", 1.5),
            "informed": leaf("Practice A* and AO* concepts", 2.0),
            "solve_search_problems": leaf("Solve AI search problems", 4.0),
            "important_questions": leaf("Revise important AI questions", 2.0),
            "mock_test": leaf("Attempt an AI mock test", 1.0),
        }
        return graph, "goal"

    raise ValueError("Unknown goal selected.")
