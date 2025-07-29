from datetime import datetime
from langchain_core.tools import tool
from app.models import Task


@tool("create_ticket", args_schema=Task, parse_docstring=True)
def create_ticket(**kwargs) -> bool:
    """This function is used to create a ticket for a user's goal.

    Args:
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        type_ (str): The type of the ticket (e.g. "mental", "physical", "habit", "challenge").
        difficulty (str): The difficulty level of the ticket (e.g. "easy", "medium", "hard").
        xp (int): The XP value associated with the ticket.

    Returns:
        bool: True if the ticket was created successfully, False otherwise.
    """
    task = Task(**kwargs)
    print("created", task)
    return True


@tool("refine_goal")
def refine_goal(refined_goal: str) -> str:
    """Refine a user goal into a more specific and actionable goal.

    Args:
        refined_goal (str): The refined user goal.

    Returns:
        str: The refined goal.
    """
    print(f"Refined goal: {refined_goal}")
    return refined_goal
