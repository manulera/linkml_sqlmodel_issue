import os
import logging
from sqlmodel import SQLModel, create_engine
from sqlalchemy import log as sqlalchemy_log

# Logging settings to have the mnimum output (mostly SQL)
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
