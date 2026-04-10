from crewai import Task
from crewai.project import CrewBase, agent, crew, task

@task("Past Results Task")
def create_tasks(sport, agent):
    return Task(
        description=f"Analyze past results for {sport} and provide a summary of the results",
        expected_output=f"A list of past results for {sport}",
        agent=agent
    )

