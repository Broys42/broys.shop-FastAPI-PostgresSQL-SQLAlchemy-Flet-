import asyncio
import uvicorn
from contextlib import asynccontextmanager
import flet as ft
from ui.banner import Banner
from ui.video import Video
import flet.fastapi as flet_fastapi
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

async def main(page: ft.Page):
    video = Video(page)
    video.height = page.window.height
    banner = Banner(page, video)
    await page.add_async(banner)
    await video.playlist_add_async(video.videoBanner)
    page.update()
    while True:
        await asyncio.sleep(0.1)
        video.play()

flet_app = FastAPI()

flet_app.mount("/", flet_fastapi.app(main))

app.mount("/flet-app", flet_app)
