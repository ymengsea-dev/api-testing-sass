from pydantic import BaseModel
from uuid import UUID
from app.models.enum_type import HttpMethod


# schema for handle endpoint creation
class EndpointCreate(BaseModel):
    name: str
    curl_url: str

class Field(BaseModel):
    name: str
    inferred_type: str
    required: bool = False

class EndpointOut(BaseModel):
    id: UUID
    name: str
    url: str
    method: HttpMethod
    field: list[Field]

    class Config:
        from_attributes = True 
        #allow to build obj from a normal 
        #python object attri such as SQLAlchemy model instance.
