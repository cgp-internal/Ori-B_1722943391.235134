from fastapi import FastAPI
from app.db.session import get_session
from app.routers import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    db = get_session()
    try:
        yield db
    finally:
        db.close()

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)