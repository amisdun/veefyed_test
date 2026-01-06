from pathlib import Path
from fastapi import UploadFile, HTTPException, status

ALLOWED_EXTENSIONS = {".jpeg", ".png"}


def get_image_ext(file: UploadFile) -> str:
    extension = Path(file.filename).suffix.lower()
    return extension
