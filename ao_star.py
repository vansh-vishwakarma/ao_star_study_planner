class AOStar:
    def __init__(self, graph):
        self.graph = graph
        self.value = {}
        self.solved = {}
        self.solution = {}
        self.visiting = set()

        for node_id, node in graph.items():
            self.value[node_id] = node["heuristic"]
            self.solved[node_id] = False
            self.solution[node_id] = None

            
            if not node["options"]:
                self.value[node_id] = node["cost"]
                self.solved[node_id] = True

    def _option_cost(self, node_id, option):
        
        node_cost = self.graph[node_id]["cost"]
        return node_cost + sum(self.value[child] for child in option)

    def _best_option(self, node_id):
        options = self.graph[node_id]["options"]
        if not options:
            return None, self.graph[node_id]["cost"]

        scored = [
            (self._option_cost(node_id, option), index, option)
            for index, option in enumerate(options)
        ]
        cost, _, option = min(scored, key=lambda item: item[0])
        return option, cost

    def _solve(self, node_id):
        if node_id not in self.graph:
            raise KeyError(f"Task '{node_id}' is missing from the graph.")

        if self.solved[node_id]:
            return

        if node_id in self.visiting:
            raise ValueError("Cycle detected. AO* graph must be acyclic.")

        self.visiting.add(node_id)
        node = self.graph[node_id]

        if not node["options"]:
            self.value[node_id] = node["cost"]
            self.solved[node_id] = True
            self.visiting.remove(node_id)
            return

    
        while True:
            best_group, best_cost = self._best_option(node_id)
            self.solution[node_id] = best_group
            self.value[node_id] = best_cost

            
            unsolved_child = next(
                (child for child in best_group if not self.solved[child]),
                None
            )

            if unsolved_child is not None:
                self._solve(unsolved_child)
                continue

         
            best_actual = self._option_cost(node_id, best_group)
            other_estimates = [
                self._option_cost(node_id, option)
                for option in node["options"]
                if option != best_group
            ]

            if all(best_actual <= estimate for estimate in other_estimates):
                self.value[node_id] = best_actual
                self.solved[node_id] = True
                break

            
        self.visiting.remove(node_id)

    def search(self, start_node):
        
        self._solve(start_node)

        if not self.solved[start_node]:
            return None

        plan = []
        self._collect_plan(start_node, plan, set())

        return {
            "plan": plan,
            "cost": self.value[start_node],
        }

    def _collect_plan(self, node_id, plan, visited):
        
        if node_id in visited:
            return
        visited.add(node_id)

        node = self.graph[node_id]
        if not node["options"]:
            plan.append(node["name"])
            return

        chosen_group = self.solution[node_id]
        if chosen_group is None:
            return

        for child in chosen_group:
            self._collect_plan(child, plan, visited)
