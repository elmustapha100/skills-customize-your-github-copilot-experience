from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define Pydantic model for request/response validation
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

# In-memory storage for items
items_db = []

# Task 1: Basic endpoints
@app.get("/")
def read_root():
    """Welcome endpoint - returns a greeting message."""
    return {"message": "Welcome to the FastAPI REST API"}

# TODO: Add POST endpoint to create new items

# Task 2: Implement request validation (using Pydantic models above)

# Task 3: Implement CRUD operations
@app.get("/items")
def get_all_items():
    """Get all items from the database."""
    return items_db

# TODO: Add GET /items/{item_id} endpoint
# TODO: Add PUT/PATCH endpoint to update items
# TODO: Add DELETE endpoint to remove items

# Task 4: Add error handling with proper status codes
# Remember to use HTTPException for errors like:
# - HTTPException(status_code=404, detail="Item not found")
# - HTTPException(status_code=400, detail="Invalid data")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
