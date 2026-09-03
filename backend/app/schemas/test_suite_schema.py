from pydantic import BaseModel
from uuid import UUID
from app.models.enum_type import TestStatus
from datetime import datetime

class TestSuiteCreate(BaseModel):
    name: str # this will be endpoint name
    endpoint_id: UUID
    test_case_id: list[UUID] # list of what case to test can be more than 1

    class config:
        from_attributes = True

class TestSuiteOut(BaseModel):
    name: str # this will be endpoint name
    test_case_name: str
    status: TestStatus # status for each test case: failed / passed
    start_at: datetime
    finished_at: datetime