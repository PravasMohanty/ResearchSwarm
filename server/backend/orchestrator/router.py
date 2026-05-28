class TaskRouter:

    def route_task(
        self,
        task_type: str
    ) -> str:

        routes = {

            "research": "research_node",
            "writer": "writer_node",
            "critic": "critic_node",
            "analysis": "analysis_node",
            "coding": "coding_node"
        }

        return routes.get(
            task_type,
            "research_node"
        )


router = TaskRouter()