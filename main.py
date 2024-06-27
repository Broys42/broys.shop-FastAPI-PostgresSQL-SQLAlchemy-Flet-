import asyncio
import uvicorn
from contextlib import asynccontextmanager
import flet as ft
from ui.banner import Banner
from ui.video import Video
from ui.main_page import MainPage
from ui.headphones_row import HeadphonesRow
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
    page.bgcolor = ft.LinearGradient(colors=[ft.colors.BLUE, ft.colors.YELLOW])
    video = Video(page)
    banner = Banner(page, video)
    headphones_row = HeadphonesRow(page)
    main_page = MainPage(page)
    main_page.controls.extend([banner, headphones_row])

    def scroll_to_key(e):
        print("Пошла")
        main_page.scroll_to(key="34", duration=1000)

    banner.container_for_button.on_click = scroll_to_key

    page.add(main_page)
    video.playlist_add(video.videoBanner)
    page.update()
    await video.start_loop_play()


flet_app = FastAPI()

flet_app.mount("/", flet_fastapi.app(main))

app.mount("/", flet_app)
