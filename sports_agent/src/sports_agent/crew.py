from crewai import Agent, Crew 
from crewai.project import CrewBase, agent, crew, task, after_kickoff, before_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from sports_agent.tools.custom_tool import PastResultTool
from crewai import Task, Process
from crewai import LLM
from typing import List

from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

from pydantic import BaseModel, Field

class F1Session(BaseModel):
    """ Details about one F1 Session  """
    session_key: str = Field(description="Session number provided by API.")
    circuit_short_name: str = Field(description="Circuit Name")
    country_name: str = Field(description="Country name of the Circuit Name")
    date_start: str = Field(description="The UTC session starting date and time, in ISO 8601 format.")
    date_end: str = Field(description="The UTC session ending date and time, in ISO 8601 format.")
    position: str = Field(description = "Driver Position")
    driver_name: str = Field(description = "Driver Name")

class F1SessionResultList(BaseModel):
    """ List of F1 sessions with results  """
    sessions: List[F1Session] = Field(description="List of F1 Sessions with results")

#llm = LLM(model="ollama/lfm2.5-thinking:latest",base_url="http://localhost:11434")

llm = LLM(model = "openai/gpt-4o")



@CrewBase
class SportsAgent():
    """SportsAgent crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    
    @agent
    def sports_analyst_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config['sports_analyst_agent'],
            verbose=True, llm=llm 
        )
    
    @agent
    def information_analyst_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config['information_analyst_agent'],
            tools=[ PastResultTool(), 
                  #SerperDevTool()
                  ], 
            verbose=True, llm=llm 
        )
   
    @task 
    def get_past_result_task(self) -> Task:
        return Task(
            config=self.tasks_config['get_past_result_task'],
            output_pydantic = F1SessionResultList 
        )

    @task 
    def analyze_past_result_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_past_result_task'],
            markdown = True 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SportsAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge
        
        
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        ) 