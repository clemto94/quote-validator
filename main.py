import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api.routes import router
from infrastructure.messaging import quote_worker

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(quote_worker())
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

# Configuration des templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello QUOTEVAL"}

@app.get("/validate-form")
async def validate_form(request: Request):
    return templates.TemplateResponse("validate_quote.html", {"request": request})

