from app.models.test_case import TestCase
from fastapi import status
from app.core.exceptions import UserAlreadyExistsError, NotFoundError
from app.schemas.test_case_schema import TestCaseCreate, TestCaseOut
from app.schemas.api_response import ApiResponse
from sqlalchemy.orm import Session
from uuid import UUID

def create_new_test_case_service(payload: TestCaseCreate, db: Session):

    if db.query(TestCase).filter(TestCase.name == payload.name).first():
        raise UserAlreadyExistsError(f"test case with the name {payload.name} is already exist")

    new_test_case = TestCase(
        name = payload.name,
        inferred_type = payload.inferred_type,
        value = payload.value   
    )

    db.add(new_test_case)
    db.commit()
    db.refresh(new_test_case)

    response_data = TestCaseOut(
        id=new_test_case.id,
        name=new_test_case.name,
        inferred_type=new_test_case.inferred_type,
        value=new_test_case.value, 
    )

    response = ApiResponse(
        success=True,
        status=status.HTTP_201_CREATED,
        message="new test case has successfully created",
        data=response_data,
    )

    return response

def get_all_test_case_service(db: Session):

    test_cases = db.query(TestCase).all()

    response_data = []

    if test_cases:
        for test_case in test_cases:
            data = TestCaseOut(
                id=test_case.id,
                name=test_case.name,
                inferred_type=test_case.inferred_type,
                value=test_case.value,
            )
            response_data.append(data)

    response = ApiResponse(
        success=True,
        status=status.HTTP_200_OK,
        message="successfully get all test case",
        data=response_data,
    )

    return response

def get_test_case_by_id_service(id: UUID, db: Session):
    test_case = db.query(TestCase).filter(TestCase.id == id).first()

    if not test_case:
        raise NotFoundError(f"test case with id {id}")

    reponse_data = TestCaseOut(
        id = test_case.id,
        name = test_case.name,
        inferred_type= test_case.inferred_type,
        value=test_case.value,
    )

    response = ApiResponse(
        success=True,
        status=status.HTTP_200_OK,
        message=f"successfully get test case with id {id}",
        data=reponse_data
    )

    return response
    

def update_test_case_service(id: UUID, payload: TestCaseCreate, db: Session):

    old_test_case = db.query(TestCase).filter(TestCase.id == id).first()

    if not old_test_case:
        raise NotFoundError(f"test case with id {id} not found")

    if payload.name is not None:
        old_test_case.name = payload.name

    if payload.inferred_type is not None:
        old_test_case.inferred_type = payload.inferred_type

    if payload.value is not None:
        old_test_case.value = payload.value

    db.commit()
    db.refresh(old_test_case)

    updated_resposne = TestCaseOut (
        id = old_test_case.id,
        name = old_test_case.name,
        inferred_type = old_test_case.inferred_type,
        value = old_test_case.value,
    )

    reponse = ApiResponse(
        success=True,
        status=status.HTTP_200_OK,
        message="successfully updated test case",
        data=updated_resposne,
    )

    return reponse

def delete_test_case_service(id: UUID, db: Session):

    test_case = db.query(TestCase).filter(TestCase.id == id).first()

    if test_case is None:
        raise NotFoundError(f"test case with id {id} not found")

    db.delete(test_case)
    db.commit()

    response = ApiResponse(
        success= True,
        status=status.HTTP_200_OK,
        message=f"test case with id {id} have been deleted",
        data=None,
    )

    return response
