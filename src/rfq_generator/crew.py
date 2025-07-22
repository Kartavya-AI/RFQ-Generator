from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class RfqGenerator():
    """RfqGenerator crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def requirement_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['requirement_analyst'],
            verbose=True
        )

    @agent
    def rfq_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['rfq_writer'],
            verbose=True
        )

    @agent
    def rfq_polisher(self) -> Agent:
        return Agent(
            config=self.agents_config['rfq_polisher'],
            verbose=True
        )

    @task
    def parse_requirement_task(self) -> Task:
        return Task(
            config=self.tasks_config['parse_requirement_task']
        )

    @task
    def generate_rfq_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_rfq_task'],
            context=[self.parse_requirement_task()],
        )

    @task
    def polish_rfq_task(self) -> Task:
        return Task(
            config=self.tasks_config['polish_rfq_task'],
            context=[self.parse_requirement_task(),self.generate_rfq_task()],
            output_file='rfq_final.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RfqGenerator crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
