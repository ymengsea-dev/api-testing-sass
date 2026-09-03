import uuid
from sqlalchemy import Column, String, Uuid
from app.db.database import Base

# model for creating custom test-case and pre-built test-case
class TestCase(Base):
    __tablename__ = "test_case"
    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String)
    inferred_type = Column(String) # some endpoint accept int or str etc 
    value = Column(String) # case value to for inject to request body
    