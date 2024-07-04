import logging

from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.core.config import templates
from src.core.dependencies import lifespan
from src.database import get_current_user
from src.bus import get_bus_info


app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(__name__)

app.mount("/static", StaticFiles(directory="src/static/"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> str:
    return templates.TemplateResponse(
        "bus_info.html", {"request": request, "data": []},
        block_name=None,
    )


@app.post("/", response_class=HTMLResponse)
async def bus_info(request: Request, bus_line: str = Form(...)) -> str:
    data = await get_bus_info(bus_line)
    print("asdçkjfhasdlçkfjhasdlkjfhasdlkjf chego aqui klkkkkj")
    print(bus_line, data)
    return templates.TemplateResponse(
        "bus_info.html", {"request": request, "data": data},
        block_name="content",
    )


@app.get("/test", response_class=HTMLResponse)
async def mytest(request: Request) -> str:
    return templates.TemplateResponse(
        "test.html", {"request": request, "data": []},
        block_name=None,
    )
