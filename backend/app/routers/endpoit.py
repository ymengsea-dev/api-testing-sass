from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.endpoint_schema import EndpointCreate, EndpointOut
from app.services.endpoint_service import create_new_endpoint_service
from typing import Annotated

router = APIRouter(prefix= "/endpoint", tags=["endpoint"])

@router.post("/create-endpoint")
def create_new_endpoint(payload: Annotated[EndpointCreate, Form()], db:  Session = Depends(get_db)):
    return create_new_endpoint_service(payload, db)