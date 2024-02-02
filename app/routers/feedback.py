from fastapi import APIRouter
from app.schemas import Feedback, FeedbackResponse
from app.temp_data.feedbacks import feedbacks

feedback_router = APIRouter(
    prefix="/feedback",
    tags=["Lesson_3"]
)


@feedback_router.post("", response_model=FeedbackResponse)
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return FeedbackResponse(message=f"Feedback received. Thank you, {feedback.name}!")


@feedback_router.get("", response_model=list[Feedback])
async def get_all_feedback():
    return feedbacks
