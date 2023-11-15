import uvicorn
import cloudinary
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from app.core.settings import settings
from app.route import route

app = FastAPI(title="Sports", version="1.1.1")

app.include_router(route, prefix="")

cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, debug=settings.DEBUG)
