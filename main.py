import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from api.routes import router
from infrastructure.messaging import quote_worker, processed_quotes

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
    return templates.TemplateResponse(name="validate_quote.html", request=request, context={})

@app.get('/processed-quotes', response_class=HTMLResponse)
async def show_processed_quotes(request: Request):
    return templates.TemplateResponse(
        "processed_quotes.html",
        {"request": request, "processed_quotes": processed_quotes}
    )
