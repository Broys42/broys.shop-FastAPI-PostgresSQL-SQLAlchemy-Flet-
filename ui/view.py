import flet as ft
from ui.banner import Banner
from ui.video import Video
from ui.footer import Footer
from ui.main_page import MainPage
from ui.headphones_row import HeadphonesRow
from src.viewmodel.viewmodel import ViewModel

class View():
    def __init__(self, viewmodel: ViewModel):
        self.viewmodel = viewmodel

    async def main(self, page: ft.Page):
        page.bgcolor = ft.LinearGradient(colors=[ft.colors.BLUE, ft.colors.YELLOW])
        page.padding = 0
        video = Video(page)
        banner = Banner(page, video)
        headphones_row = HeadphonesRow(page, self.viewmodel)
        await headphones_row.set_headphones_in_controls()
        footer = Footer(page)
        main_page = MainPage(page)
        main_page.page_without_header.controls.extend([banner, headphones_row, footer])
        page.add(main_page)

        def scroll_to_key(e, key: str):
            main_page.page_without_header.scroll_to(key=key, duration=1000)

        def scroll_to_begin(e):
            main_page.page_without_header.scroll_to(offset=0, duration=1000)

        banner.container_for_button.on_click = lambda e: scroll_to_key(e=e, key="34")
        main_page.header.scroll_to_headphones_button.on_click = lambda e: scroll_to_key(e=e, key="34")
        main_page.header.scroll_to_begin_button.on_click = lambda e: scroll_to_begin(e=e)

        video.playlist_add(video.videoBanner)
        page.update()

        await video.start_loop_play()
