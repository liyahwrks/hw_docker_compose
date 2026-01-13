from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.base import Base

class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False) 
    username = Column(String(50), nullable=False)  
    email = Column(String(100), nullable=False) 
    
    posts = relationship(
        "Post", 
        back_populates="user",
        cascade="all, delete-orphan", 
        lazy="noload"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    def __str__(self):
        return f"{self.name} (@{self.username})"