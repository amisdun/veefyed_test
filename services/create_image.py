import logging
import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException
import shutil

from starlette import status

from utils.get_image import STORAGE_DIR
from utils.get_image_ext import get_image_ext, ALLOWED_EXTENSIONS


def create_image(file: UploadFile):
    logging.info(f"Check image size {file.filename}")
    check_image_size(file.size)

    logging.info(f"Get image ext {file.filename}")
    extension = get_image_ext(file)

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File extension '{extension}' is not allowed. allowed extensions are {ALLOWED_EXTENSIONS}",
        )

    image_id = uuid.uuid4()

    folder = Path(STORAGE_DIR)
    folder.mkdir(exist_ok=True)

    file_path = folder / f"{image_id}{extension}"

    with open(file_path, "wb") as buffer:
        logging.info(f"Saving image to {file_path}")
        shutil.copyfileobj(file.file, buffer)

    return {"image_id": image_id}


def check_image_size(size: int):
    max_size = 5 * 1024 * 1024
    if size > max_size:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File is too large, file should be 5MB",
        )
