import uuid
from sqlalchemy import Column, String, Uuid, DateTime
from app.db.database import Base

# model for building actual http request
# build structure for based-url, test-case 
class TestSuite(Base):
    __tablename__ = "test_suite"
    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String) # this generally from the endpoint name
    endpoint_id = Column(Uuid)
    test_case_id = Column(Uuid)
    status = Column(String)
    start_at = Column(DateTime)
    finished_at = Column(DateTime)