from sqlalchemy import Column, Text, Integer, String
from app.database import Base
metadata = Base.metadata

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(Text, unique=True, nullable=False)
    password = Column(String, nullable=False)
    imageURL = Column(String)

    def __repr__(self):
        return f"id: {self.id}, name: {self.username}"