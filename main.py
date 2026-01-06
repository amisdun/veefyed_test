from fastapi import FastAPI
from routers import image

app = FastAPI()

app.include_router(image.router, prefix="/api/v1", tags=["image_api"])


@app.get("/")
async def root():
    return {"message": "Healthy"}
