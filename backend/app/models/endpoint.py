import uuid
from sqlalchemy import Column, String, Uuid
from app.db.database import Base

# model for store each endpoint from user input curl
class Endpoint(Base):
    __tablename__ = "endpoints"
    id = Column(Uuid, primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    method = Column(String) # http method: POST/GET/PUT/PATCH
    base_url = Column(String, nullable=False) # endpoint url
    header = Column(String)
    body = Column(String)