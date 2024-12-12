from fastapi import FastAPI
from .routes import api_router

app = FastAPI()

# Include routes from the api_router
app.include_router(api_router)
