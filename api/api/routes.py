from fastapi import APIRouter
from fastapi.responses import JSONResponse

api_router = APIRouter()

# Example route
@api_router.get("/political-data")
def get_political_data():
    data = {"region": "Syria", "GDP": 1000000}  # Example data
    return JSONResponse(content=data)
