from pydantic import BaseModel

class PostCreate(BaseModel):
    user_id: int
    title: str
    body: str

class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    user_id: int
    
    class Config:
        from_attributes = True