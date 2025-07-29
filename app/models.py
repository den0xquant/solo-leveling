from typing import Literal
from uuid import uuid4
from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model to represent a user in the system.
    This model is used to define users that can interact with the system.
    It inherits from Pydantic's BaseModel to provide data validation and serialization.

    Args:
        BaseModel (_type_): _description_
    Attributes:
        id (str): Unique identifier for the user.
        username (str): Username of the user.
        level (int): Level of the user, indicating their progress or experience in the system.
    """

    id: str = Field(default_factory=lambda: uuid4().hex)
    username: str
    level: int = Field(
        default=1, description="User's level in the system, must be at least 1"
    )


class Goal(BaseModel):
    """
    Goal model to represent a goal in the system.
    This model is used to define goals that can be set by users in the system.

    Args:
        BaseModel (_type_): _description_
    Attributes:
        id (str): Unique identifier for the goal.
        user_id (str): Identifier for the user who owns the goal.
        title (str): Title of the goal.
    """

    id: str = Field(default_factory=lambda: uuid4().hex)
    user_id: str
    title: str


class Task(BaseModel):
    """
    Task model to represent a task in the system.
    This model is used to define tasks that can be assigned to users in the system.
    It inherits from Pydantic's BaseModel to provide data validation and serialization.

    Args:
        BaseModel (_type_): _description_
    Attributes:
        id (str): Unique identifier for the task.
        goal_id (str): Identifier for the goal this task belongs to.
        title (str): Title of the task.
        description (str): Description of the task.
        type (str): Type of the task, e.g., "daily", "weekly", etc.
        difficulty (str): Difficulty level of the task, e.g., "easy", "medium", "hard".
        xp (int): Experience points awarded for completing the task.
        status (str): Current status of the task, e.g., "pending", "completed".
        created_at (str): Timestamp when the task was created.
        updated_at (str): Timestamp when the task was last updated.
    """

    id: str = Field(default_factory=lambda: uuid4().hex)
    goal_id: str
    title: str
    description: str
    type: str
    difficulty: str
    xp: int
    status: str
    created_at: str
    updated_at: str


class Milestone(BaseModel):
    """
    Milestone model to represent a milestone in the system.
    This model is used to define milestones that can be achieved by users in the system.
    It inherits from Pydantic's BaseModel to provide data validation and serialization.

    Args:
        BaseModel (_type_): _description_
    Attributes:
        id (UUID): Unique identifier for the milestone.
        name (str): Name of the milestone.
        description (str): Description of the milestone.
        trigger_type (Literal["level_up", "goal_complete", "xp", "task_count", "custom"]): Type of trigger for the milestone.
        trigger_value (int): Value associated with the trigger.
        reward (str | None): Reward associated with the milestone, can be None if no reward is given.
    """

    id: str = Field(default_factory=lambda: uuid4().hex)
    user_id: str
    name: str
    description: str
    trigger_type: Literal["level_up", "goal_complete", "xp", "task_count", "custom"]
    trigger_value: int
    reward: str | None
