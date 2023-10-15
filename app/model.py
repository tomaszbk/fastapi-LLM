from diffusers import StableDiffusionPipeline
import torch
from loguru import logger
import os

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
     torch_dtype=torch.float16,
     cache_dir='./ml-models'   
)
pipe.to("cuda")


def generate_image(prompt: str):
    """Generates an image from the provided prompt."""
    # run both experts
    image = pipe(prompt=prompt).images[0]

    return image
