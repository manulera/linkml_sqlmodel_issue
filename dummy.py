from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class Person(ConfiguredBaseModel):
    """
    A person
    """
    id: int = Field(..., description="""A unique identifier for a thing""")
    name: str = Field(..., description="""A human-readable name for a thing""")
    age: Optional[int] = Field(None, description="""The age of the person""")
    team_id: Optional[int] = Field(None, description="""The team to which the person belongs""")


class Team(ConfiguredBaseModel):
    """
    A team
    """
    id: int = Field(..., description="""A unique identifier for a thing""")
    name: str = Field(..., description="""A human-readable name for a thing""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Person.model_rebuild()
Team.model_rebuild()

