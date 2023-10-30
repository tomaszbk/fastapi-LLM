from fastapi import APIRouter
from app.model import generate_text_response


router = APIRouter()


@router.get("/text")
def generate_text_route(prompt: str):
    """Generates an image with the provided text."""
    response = generate_text_response(prompt)
    return {'response': response}
