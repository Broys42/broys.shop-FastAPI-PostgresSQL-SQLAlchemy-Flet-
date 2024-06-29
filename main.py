import asyncio
import uvicorn
from contextlib import asynccontextmanager
import flet as ft
import flet.fastapi as flet_fastapi
from ui.view import View
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

view = View()

flet_app = FastAPI()

flet_app.mount("/", flet_fastapi.app(view.main))

app.mount("/", flet_app)
