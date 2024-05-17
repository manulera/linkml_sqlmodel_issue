from sqlmodel import SQLModel, Relationship, Field, create_engine
from typing import Optional
import os


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


import logging

from sqlalchemy import log as sqlalchemy_log

sqlalchemy_log._add_default_handler = lambda x: None

logging.basicConfig(format="%(message)s")

# Remove db file if it exists
if os.path.exists("database.db"):
    os.remove("database.db")

# Create an SQLite database

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)
