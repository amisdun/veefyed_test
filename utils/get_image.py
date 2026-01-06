from pathlib import Path

STORAGE_DIR = Path("images")


def get_image(image_id: str):
    match = next(STORAGE_DIR.glob(f"{image_id}.*"), None)
    return match
