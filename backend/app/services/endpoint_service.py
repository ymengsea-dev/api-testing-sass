from fastapi import HTTPException, status
from app.models.endpoint import Endpoint
from app.schemas.endpoint_schema import EndpointCreate
from sqlalchemy.orm import Session

def create_new_endpoint_service(payload: EndpointCreate, db: Session):
    
    name = payload.name
    print("endpoint name:", name)
    url = payload.curl_url
    print("curl url:", url)
    
    return "hell yeahhh"