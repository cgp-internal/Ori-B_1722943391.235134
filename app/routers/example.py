from fastapi import APIRouter, HTTPException
from app.services.example_service import ExampleService

router = APIRouter()
example_service = ExampleService()

@router.get("/examples/")
async def read_examples():
    return example_service.get_all_examples()

@router.get("/examples/{id}")
async def read_example(id: int):
    example = example_service.get_example_by_id(id)
    if example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return example

@router.post("/examples/")
async def create_example(name: str, description: str):
    return example_service.create_example(name, description)

@router.put("/examples/{id}")
async def update_example(id: int, name: str, description: str):
    example = example_service.update_example(id, name, description)
    if example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return example

@router.delete("/examples/{id}")
async def delete_example(id: int):
    example = example_service.delete_example(id)
    if example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return {"message": "Example deleted successfully"}