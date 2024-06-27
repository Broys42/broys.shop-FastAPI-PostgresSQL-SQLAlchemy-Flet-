import asyncio
import uvicorn
from contextlib import asynccontextmanager
import flet as ft
from ui.banner import Banner
from ui.video import Video
from ui.main_page import MainPage
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
    banner = Banner(page, video)
    main_page = MainPage(page)
    main_page.controls.append(banner)
    spacer = ft.Container(bgcolor="#000000", height=10000, key="34")
    main_page.controls.append(spacer)

    def scroll_to_key(e):
        main_page.scroll_to(key="34", duration=1000)

    banner.container_for_button.on_click = scroll_to_key

    await page.add_async(main_page)
    await video.playlist_add_async(video.videoBanner)

    page.update()
    while True:
        await asyncio.sleep(0.1)
        video.play()

flet_app = FastAPI()

flet_app.mount("/", flet_fastapi.app(main))

app.mount("/flet-app", flet_app)
