from app.models.endpoint import Endpoint
from fastapi import HTTPException, status
from app.schemas.endpoint_schema import EndpointCreate, EndpointOut, Field
from sqlalchemy.orm import Session
from app.core.curl_parser import curl_parser
from uuid import UUID

def create_new_endpoint_service(payload: EndpointCreate, db: Session):
    name = payload.name
    curl_data = curl_parser(payload.curl_url)

    new_endpoint = Endpoint(
        name = name,
        method = curl_data["method"],
        base_url = curl_data["url"],
        header = curl_data["headers"],
        body = curl_data["body"]
    )

    db.add(new_endpoint)
    db.commit()
    db.refresh(new_endpoint)

    fields = []

    for key, value in new_endpoint.body.items():
        field = Field(
            name=key,
            inferred_type=type(value).__name__,
            required=False
        )
        fields.append(field)

    # print(curl_data["method"])
    # print(curl_data["url"])
    # print(curl_data["headers"])
    # print(curl_data["body"])

    return EndpointOut(
            id = new_endpoint.id,
            name = new_endpoint.name,
            url = new_endpoint.base_url,
            method = new_endpoint.method,
            field = fields,
        )

def get_all_endpoints_service(db: Session):

    endpoints = db.query(Endpoint).all()

    results = []

    for endpoint in endpoints:
        fields = []
        if endpoint.body:
            for key, value in endpoint.body.items():
                fields.append(
                    Field(
                        name=key,
                        inferred_type=type(value).__name__,
                        required=False
                    )
                )
        endpoint_out = EndpointOut(
            id=endpoint.id,
            name=endpoint.name,
            url=endpoint.base_url,
            method=endpoint.method,
            field=fields
        )

        results.append(endpoint_out)

    return results

def delete_endpoint_by_id_service(id: UUID, db: Session):

    endpoint = (
        db.query(Endpoint)
        .filter(Endpoint.id == id)
        .first()
    )

    if endpoint is None:
        raise HTTPException(
            status_code=404,
            detail= f"endpoint with the id {id} not found"
        )

    db.delete(endpoint)
    db.commit()

    return {
        "status": "204 no content",
        "message": "delete success",
    }

def delete_all_endpoint_service( db: Session):

    deleted_count = db.query(Endpoint).delete()

    db.commit()

    return {
        "status": "204 no content",
        "message": f"{deleted_count} endpoints deleted successfully"
    }