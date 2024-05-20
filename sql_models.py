from sqlmodel import SQLModel, Relationship, Field
from typing import Optional


class TeamSQL(SQLModel, table=True):
    # primary_key is always optional in sqlmodel
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(None)

    people: list["PersonSQL"] = Relationship(back_populates="team")


class PersonSQL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(None)
    age: int = Field(None)

    team_id: Optional[int] = Field(None, foreign_key="teamsql.id")
    team: "TeamSQL" = Relationship(back_populates="people")
