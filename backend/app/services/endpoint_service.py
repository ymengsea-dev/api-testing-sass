from app.models.endpoint import Endpoint
from app.schemas.endpoint_schema import EndpointCreate, EndpointOut, Field
from sqlalchemy.orm import Session
from app.core.curl_parser import curl_parser

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
            method = new_endpoint.method,
            field = fields,
        )