import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Dict, Any

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response

from api.routes import router
from infrastructure.messaging import quote_worker

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    asyncio.create_task(quote_worker())
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

# Configuration des templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello QUOTEVAL"}

@app.get("/validate-form", response_class=Response)
async def validate_form(request: Request) -> Response:
    """
    Affiche le formulaire de validation de devis.
    
    Returns:
        Response: Une page HTML contenant le formulaire de validation
    """
    return templates.TemplateResponse("validate_quote.html", {"request": request})

