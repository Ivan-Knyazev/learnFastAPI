from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    name: str
    message: Optional[str] = None


class FeedbackResponse(BaseModel):
    message: str
