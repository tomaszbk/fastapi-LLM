from fastapi import APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from app.model import generate_image, generate_text_response
import io


router = APIRouter()


@router.get("/image")
def generate_image_route(prompt: str):
    """Generates an image with the provided text."""
    image = generate_image(prompt)
    # Convert the image to bytes
    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    # Create a StreamingResponse with the image bytes
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")


@router.get("/text")
def generate_text_route(prompt: str):
    """Generates an image with the provided text."""
    response = generate_text_response(prompt)
    # Convert the image to bytes

    return {'response': response}