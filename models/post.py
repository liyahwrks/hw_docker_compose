from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from models.base import Base

class Post(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, 
        ForeignKey("user.id", ondelete="CASCADE"),  
        nullable=False
    ) 
    title = Column(String(200), nullable=False)  
    body = Column(Text, nullable=False) 
    
    user = relationship(
        "User", 
        back_populates="posts",
        lazy="joined"  
    )
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title[:20]}...', user_id={self.user_id})>"