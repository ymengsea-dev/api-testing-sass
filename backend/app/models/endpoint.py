import uuid
from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Uuid
from app.db.database import Base

# model for store each endpoint from user input curl
class Endpoint(Base):
    __tablename__ = "endpoints"
    id = Column(Uuid, primary_key=True, unique=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    method: Mapped[str] = mapped_column(String) # http method: POST/GET/PUT/PATCH
    base_url: Mapped[str] = mapped_column(String) # endpoint url
    header: Mapped[dict] = mapped_column(JSON)
    body: Mapped[dict] = mapped_column(JSON)