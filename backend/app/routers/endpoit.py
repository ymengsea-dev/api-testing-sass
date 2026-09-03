from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.endpoint_schema import EndpointCreate
from app.services.endpoint_service import create_new_endpoint_service, get_all_endpoints_service, delete_endpoint_by_id_service, delete_all_endpoint_service
from typing import Annotated
from uuid import UUID

router = APIRouter(prefix= "/endpoint", tags=["endpoint"])

@router.post("/create-endpoint")
def create_new_endpoint(payload: Annotated[EndpointCreate, Form()], db:  Session = Depends(get_db)):
    return create_new_endpoint_service(payload, db)

@router.get("/get-endpoints")
def get_all_endpoints(db: Session = Depends(get_db)):
    return get_all_endpoints_service(db)

@router.delete("/delete/{endpoint_id}")
def delete_endpoint_by_id(endpoint_id: UUID, db: Session = Depends(get_db)):
    return delete_endpoint_by_id_service(endpoint_id,db)

@router.delete("/delete-all")
def delete_all_endpoint(db: Session = Depends(get_db)):
    return delete_all_endpoint_service(db)