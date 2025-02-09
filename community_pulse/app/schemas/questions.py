from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=5)


class QuestionResponse(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True
class MessageResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True