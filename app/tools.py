from langchain_core.tools import tool


@tool
def create_ticket(title: str, description: str, type: str, difficulty: str, xp: int) -> bool:
    """This function is used to create a ticket for a big goal.

    Args:
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        type (str): The type of the ticket (e.g. "mental", "physical", "habit", "challenge").
        difficulty (str): The difficulty level of the ticket (e.g. "easy", "medium", "hard").
        xp (int): The XP value associated with the ticket.

    Returns:
        bool: True if the ticket was created successfully, False otherwise.
    """
    print(locals())
    return True
