import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import router
from infrastructure.messaging import quote_worker

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(quote_worker())
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello QUOTEVAL"}

