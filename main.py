from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from app.tools import create_ticket
from app.prompts import SYSTEM_PROMPT_TEMPLATE
from dotenv import load_dotenv

load_dotenv()


def main():
    llm = ChatOllama(
        model="llama3-groq-tool-use",
        temperature=0.1
    )
    agent = create_react_agent(
        model=llm,
        tools=[create_ticket],
        prompt=SYSTEM_PROMPT_TEMPLATE,
    )

    user_goal = "I want to do 100 push-ups in 30 days. I need a structured plan to achieve this goal."
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_goal}]},
        {"recursion_limit": 30}
    )


if __name__ == "__main__":
    main()
