## README

### Overview

This project is an AI-powered task delegation system using multiple agents to automate task creation, agent development, tool implementation, and crew assembly. The project uses the following libraries and models:

- **Pandas** for data management.
- **CrewAI** for agent-based task automation.
- **Langchain** for LLM management.
- **Ollama** and **ChatGroq** as language models.
- **CrewAI Tools** for handling task documentation and file reading.

### Project Structure

1. **Agents**
   - **Organizational_Agent**: Defines the structure of the crew and determines the agents and tasks needed to accomplish the goal.
   - **Task_Creation_Agent**: Implements the tasks defined by the Organizational_Agent based on given documentation.
   - **Agent_Creation_Agent**: Implements agents to execute tasks defined by the Organizational_Agent.
   - **Tool_Development_Agent**: Implements tools for agents to use based on predefined documentation.
   - **Crew_Assembly_Agent**: Assembles the agents and tasks into a working crew.

2. **Tasks**
   - Tasks are instances of the `Task` class from `crewai`. Each task contains:
     - A description.
     - Expected output.
     - A corresponding agent to execute the task.

3. **Crew**
   - A `Crew` consists of agents, tasks, and a manager LLM, with options for hierarchical processing and memory.

### Prerequisites

- Python 3.8 or higher.
- Install required libraries:
  ```bash
  pip install pandas crewai langchain-llms langchain-groq crewai-tools
  ```
- Set up the required API keys as environment variables, including:
  - `GROQ_API_KEY`.

### How to Run

1. Ensure the necessary documentation files (`task_docs.txt`, `agent_docs.txt`, `tool_docs.txt`, `crew_docs.txt`, `delegation_docs.txt`) are available.
2. Run the main script:
   ```bash
   python main.py
   ```

### Customization

- Modify the LLM models (e.g., switching from `llama3` to another model) by updating the model name in the `Ollama` or `ChatGroq` instances.
- Modify agent roles and goals as needed to suit different project structures.

### License

This project is licensed under the MIT License.
