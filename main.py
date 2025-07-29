from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from app.tools import create_ticket
from app.prompts import SYSTEM_PROMPT_TEMPLATE
from app.models import User, Goal
from dotenv import load_dotenv

load_dotenv()


def main():
    llm = ChatOllama(
        model="llama3-groq-tool-use",
        temperature=0.1,
    )
    agent = create_react_agent(
        model=llm,
        tools=[create_ticket],
        prompt=SYSTEM_PROMPT_TEMPLATE,
    )
    user = User(username="awesome_user")
    user_goal = "I want to become a pentester."
    goal = Goal(user_id=user.id, title=user_goal)

    result = agent.invoke(
        {"messages": [{"role": "user", "content": goal.title}]},
        {"recursion_limit": 30}
    )


if __name__ == "__main__":
    main()
