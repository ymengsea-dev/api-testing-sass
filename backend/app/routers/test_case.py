from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from uuid import UUID

from app.schemas.test_case_schema import TestCaseCreate
from app.services.test_case_service import create_new_test_case_service, get_all_test_case_service, update_test_case_service, delete_test_case_service, get_test_case_by_id_service

router = APIRouter(prefix="/test_case", tags=["test case"])

@router.post("/create-test-case")
def create_new_test_case(payload: TestCaseCreate, db: Session = Depends(get_db)):
    return create_new_test_case_service(payload, db)

@router.get("/test-cases")
def get_all_test_case(db: Session = Depends(get_db)):
    return get_all_test_case_service(db)

@router.get("/get-by-id/{test_case_id}")
def get_test_case_by_id(test_case_id: UUID, db: Session = Depends(get_db)):
    return get_test_case_by_id_service(test_case_id, db)

@router.put("/update-test-case/{test_case_id}")
def update_test_case(test_case_id: UUID, paylaod: TestCaseCreate, db: Session = Depends(get_db)):
    return update_test_case_service(test_case_id, paylaod, db)

@router.delete("/delete-test-case/{test_case_id}")
def delete_test_case(test_case_id: UUID, db: Session = Depends(get_db)):
    return delete_test_case_service(test_case_id, db)
