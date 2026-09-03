from uuid import UUID
from pydantic import BaseModel

# schema for handle test case creation
class TestCaseCreate(BaseModel):
    name: str
    inferred_type: str
    value: str

    class config:
        from_attributes = True 

class TestCaseOut(BaseModel):
    id = UUID
    name = str
    inferred_type: str
    value: str