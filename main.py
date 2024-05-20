from sql_models import TeamSQL, PersonSQL
from db import engine

from sqlmodel import Session

with Session(engine) as session:

    team_red = TeamSQL(name="Red")
    new_person = PersonSQL(name="Alice", age=30, team=team_red)
    session.add(new_person)
    session.commit()

    # We can access the fields:
    print()
    print("Fields:")
    print(new_person.id)
    print(new_person.name)

    # To access the entire model, we have to refresh it:
    print()
    session.refresh(new_person)
    print("Model:")
    print(new_person)
