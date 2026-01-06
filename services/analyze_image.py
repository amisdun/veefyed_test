import logging
import random

from fastapi import HTTPException
from starlette import status

from utils.get_image import get_image


def analyze_image(image_id: str):
    logging.info(f"Analyzing image: {image_id}")

    image = get_image(image_id)

    if image is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found",
        )

    return {
        "image_id": image_id,
        "skin_type": random.choice(["Oily", "Dry", "Combination", "Normal"]),
        "issues": ["Hyperpigmentation"] if random.random() > 0.5 else ["Acne"],
        "confidence": round(random.uniform(0.80, 0.99), 2),
    }
