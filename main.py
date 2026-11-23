from tasks import get_goals, build_task_graph
from ao_star import AOStar


def show_goals(goals):
    print("\nChoose your study goal:")
    for number, goal in enumerate(goals, start=1):
        print(f"{number}. {goal}")
    print(f"{len(goals) + 1}. Exit")


def main():
    goals = get_goals()

    while True:
        print("\n" + "=" * 48)
        print("          SMART STUDY TASK PLANNER")
        print("                Using AO*")
        print("=" * 48)

        show_goals(goals)
        choice = input("\nEnter your choice: ").strip()

        if choice == str(len(goals) + 1):
            print("\nThank you for using Smart Study Task Planner!")
            break

        if not choice.isdigit() or not (1 <= int(choice) <= len(goals)):
            print("\nInvalid choice. Please choose a number from the menu.")
            continue

        goal_name = goals[int(choice) - 1]
        graph, start_node = build_task_graph(goal_name)

        print(f"\nGoal: {goal_name}")
        print("\nSearching for a suitable plan using AO*...\n")

        planner = AOStar(graph)
        result = planner.search(start_node)

        if result is None:
            print("Sorry, a plan could not be found.")
            continue

        print("-" * 48)
        print("RECOMMENDED STUDY PLAN")
        print("-" * 48)
        for index, task in enumerate(result["plan"], start=1):
            print(f"{index}. {task}")

        print("\nEstimated total effort: "
              f"{result['cost']:.1f} hours")
        print("Plan generated successfully!")
        print("-" * 48)

        again = input("\nPress Enter to return to the menu...")
        if again.lower() == "q":
            break


if __name__ == "__main__":
    main()
