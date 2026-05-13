from dotenv import load_dotenv
import os
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is worst"

llm = ChatOllama(model='gemma3:270m')
tools = [search]
agent = create_agent(model = llm, tools = tools)

def main():
    print("hello hi from tavily")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather of Tokyo")})
    print(result)


if __name__ == "__main__":
    main()