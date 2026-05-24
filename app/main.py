from fastapi import FastAPI
from backend.app.database import Base
from backend.app.database import engine
from backend.app.routes.upload import router as upload_router
from backend.app.routes.chat import router as chat_router
from backend.app.routes.auth_routes import router as auth_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routes
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AI Document Intelligence Platform Running"
    }