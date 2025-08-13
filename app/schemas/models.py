import uuid
from sqlmodel import SQLModel, Field, Relationship

from app.schemas.domain import UserBase


class Follows(SQLModel, table=True):
    followee_id: uuid.UUID | None = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    follower_id: uuid.UUID | None = Field(
        default=None, foreign_key="user.id", primary_key=True
    )


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    followers: list["User"] = Relationship(
        back_populates="followees",
        link_model=Follows,
        sa_relationship_kwargs=dict(
            primaryjoin="User.id==Follows.followee_id",
            secondaryjoin="User.id==Follows.follower_id",
        ),
    )
    followees: list["User"] = Relationship(
        back_populates="followers",
        link_model=Follows,
        sa_relationship_kwargs=dict(
            primaryjoin="User.id==Follows.follower_id",
            secondaryjoin="User.id==Follows.followee_id",
        ),
    )
