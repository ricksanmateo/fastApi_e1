from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import posts, users, auth, vote
from .config import settings

print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)
origins = [
    "*"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Root Directory
@app.get("/")
async def root():
    return {"message": "Hello this a fast API2"}




