from fastapi import FastAPI
from app.routers import comman, chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comman.router)
app.include_router(chat.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
