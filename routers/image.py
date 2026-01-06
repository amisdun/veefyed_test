from fastapi import APIRouter, UploadFile, File

from services.analyze_image import analyze_image
from services.create_image import create_image

router = APIRouter()


@router.post("/image/upload")
async def create(image: UploadFile = File(...)):
    return create_image(image)


@router.post("/image/analyze/{image_id}")
async def analyse(image_id: str):
    return analyze_image(image_id)
