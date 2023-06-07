from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'juser'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": datetime.strftime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f%Z'),
            "updated_at": datetime.strftime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f%Z')
        }