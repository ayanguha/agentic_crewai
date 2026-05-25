# SportsAgent Crew

Welcome to the SportsAgent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Local Development

**Add your `OPENAI_API_KEY` into the `.env` file**

### Databricks deployment 

#### Get the key from `.env`
```
grep '^OPENAI_API_KEY=' .env | sed 's/^OPENAI_API_KEY=//'
```

#### Databricks CLI for Scope and Secret Management

```
databricks secrets create-scope f1_analyzer_scope

```

```
openai_api_key=$(grep '^OPENAI_API_KEY=' .env | sed 's/^OPENAI_API_KEY=//')

databricks secrets put-secret --json '{
  "scope": "f1_analyzer_scope",
  "key": "OPENAI_API_KEY",
  "string_value": "'"$openai_api_key"'"
}'
```

#### DAB deployment

This is essential to have App created with Resources. 

```
databricks bundle deploy --profile dbrx-free

```

#### App deployment

```
databricks apps start  f1-analyzer-app

databricks sync . /Workspace/Users/guha.ayan@gmail.com/.bundle/f1_analyzer/dev/files

databricks apps deploy f1-analyzer-app --source-code-path /Workspace/Users/guha.ayan@gmail.com/.bundle/f1_analyzer/dev/files


```

Start the app

```
databricks apps start f1-analyzer-app
```

### Customizing

- Modify `src/sports_agent/config/agents.yaml` to define your agents
- Modify `src/sports_agent/config/tasks.yaml` to define your tasks
- Modify `src/sports_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/sports_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the sports-agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The sports-agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

