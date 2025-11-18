from sqlalchemy import Column, Integer, Numeric, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
import enum, uuid
from app.db import Base

class PropertyStatus(str, enum.Enum):
    available = "available"
    under_offer = "under_offer"
    sold = "sold"
    inactive = "inactive"

class Property(Base):
    __tablename__ = "properties"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text)
    address_line = Column(Text)
    number = Column(Text)
    neighborhood = Column(Text)
    city = Column(Text)
    state = Column(Text)
    zip = Column(Text)
    area_m2 = Column(Numeric(12,2))
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    parking_spots = Column(Integer)
    price_requested = Column(Numeric(14,2))
    status = Column(Enum(PropertyStatus), default=PropertyStatus.available, nullable=False)
