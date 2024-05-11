
import pandas as pd
import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from crewai_tools import FileReadTool

taks_docs = ''
with open('task_docs.txt', "r") as docs:
    task_docs = dosc

agent_docs = ''
with open('agent_docs.txt', 'r') as docs:
    agent_docs = docs

tool_docs = ''
with open('tool_docs.txt', 'r') as docs:
    tool_docs = docs

crew_docs = ''
with open('crew_docs.txt', 'r') as docs:
    crew_docs = docs

delegation_docs = ''
with open('delegation_docs.txt', 'r') as docs:
    delegation_docs = docs

def main():
    model = 'llama3-8b-8192'

    llm_groq= ChatGroq(
        temperature=0, 
        groq_api_key=os.environ['GROQ_API_KEY'], 
        model_name=model    
    )
    llm = Ollama(model="llama3", temperature=0.4)

    file_read_tool = FileReadTool('./docs.txt')

    Organizational_Agent = Agent( # will figure out what agents tasks and tools to create basicaly build the structure of the crew to then be implemented
        role='Organizational_Agent',
        goal=f"""
            Define what tasks agents and tools will be create a crew to accomplish the task at hand.
            Your final responce should be a complete list of task agents and tools, no code.

            Use this documentation for creating such a list

            Documentation
            -------------

            {delegation_docs}

            -------------
            Reply with the final list
        """,
        backstory="""
            You are a master at delegating tasks and creating agents will al the required tools for the function of these agents.
        """,
        verbose=True,
        allow_delegation=True,
        llm=llm
        #tools=TODO
    ),
    
    Task_Creation_Agent = Agent(# a good example of a goal
        role='Task_Creation_Agent',
        goal=f"""
            Implement the tasks that the Organizational_Agent created.
            All tasks must be an instance of the python crewai 'Task' class, with a discription, expected output and a corisponding agent to execute this task.
            All tasks must be created in accordence with the following documentation:

            Documentation
            -------------

            {task_docs}

            -------------
            Reply with all the tasks properly formated. Use nothing but python code.
            """,
        backstory="""
            You are a master at implementing tasks with very detailed discriptions, expected outputs and properly delegating these tasks to the apropriat agents.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[file_read_tool]
    )

    Agent_Creation_Agent = Agent(
        role='Agent_Creation_Agent',
        goal="""
            Implement the agents that the Organizational_Agent created.
            All agents must be an instance of the python crewai 'agent' class, with a goal, a roal, backstory, tools that the agent can use, alocated llm, verbose setting and an allow_delegation setting.
            All agents must be created in accordence with the following documentation:

            Documentation
            -------------

            {agent_docs}

            -------------
            Reply with all the agents properly formated. Use nothing but python code.
        """,
        backstory="""
            You are a master at implementing agents, creaing very detailed goals and backstories for these agents.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Tool_Development_Agent = Agent(
        role='Tool_Development_Agent',
        goal="""
            Implement the tools that the Organizational_agent created.
            All tools must be an instance of the python crewai 'tool' class, with a #TODO.
            All tools must be created in accordence with the following documentation:

            Documentation
            -------------

            {tool_docs}

            -------------
            Reply with all the tools properly formated. Use nothing but python code.
        """,
        backstory="""
            
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Crew_Assembly_Agent = Agent(
        role='Crew_Assembly_Agent',
        goal="""
            
        """,
        backstory="""
            
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    task_create_tasks = Task(
        description="""
            
        """,
        agent=Task_Creation_Agent,
        expected_output="""
            
        """
    )

    task_create_agents = Task(
        description="""
            
        """,
        agent=Agent_Creation_Agent,
        expected_output="""
            
        """
    )

    task_develop_tools = Task(
        description="""
            
        """,
        agent=Tool_Development_Agent,
        expected_output="""
            
        """
    )

    task_assemble_crew = Task(
        description="""
            
        """,
        agent=Crew_Assembly_Agent,
        expected_output="""
            
        """
    )

    task = Task(
        description="""
            
        """,
        agent=Crew_Assembly_Agent,
        expected_output="""
            
        """,
        tools = [file_read_tool]
    )
    crew = Crew(
        agents=[Task_Creation_Agent, Agent_Creation_Agent, Tool_Development_Agent, Crew_Assembly_Agent],
        tasks=[task_assemble_crew, task_create_agents, task_create_tasks, task_develop_tools],
        verbose=2,
        process=Process.hierarchical,
        manager_llm=llm,
        memory=True,
        full_output=True,
    )

    result = crew.kickoff()

    print(result)


if __name__ == "__main__":
    main()
