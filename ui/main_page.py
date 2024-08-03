import flet as ft
from ui.header import HeaderInMainPage
from ui.video import Video
from ui.footer import Footer
from ui.banner import Banner
from ui.headphones_row import HeadphonesRow
from src.viewmodel.viewmodel import ViewModel

class MainPage(ft.Stack):
    def __init__(self, page: ft.Page, viewmodel: ViewModel):
        super().__init__()
        self.page = page
        self.expand = True
        self.viewmodel = viewmodel

        self.page.padding = 0

        self.header = HeaderInMainPage(page=page)
        self.header.scroll_to_begin_button.on_click = lambda e: self.scroll_to_begin(e=e)
        self.header.scroll_to_headphones_button.on_click = lambda e: self.scroll_to_headphones(e=e)

        self.footer = Footer(self.page)

        self.video = Video(self.page)
        self.banner = Banner(self.page, self.video)
        self.banner.container_for_button.on_click = lambda e: self.scroll_to_headphones(e=e)
        self.headphones_row = HeadphonesRow(self.page, self.viewmodel)

        self.page_without_header = ft.Column(
            controls=[
                self.banner,
                self.headphones_row,
                self.footer
            ],
            expand = True,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            # on_scroll_interval = 0,
            on_scroll=self.on_scroll
        )

        self.controls = [
            self.page_without_header,
            self.header
        ]

        self.page.on_resized = self.page_on_resize

    def start_video(self):
        self.video.playlist_add(self.video.videoBanner)
        self.video.start_play()

    def scroll_to_begin(self, e):
        self.page_without_header.scroll_to(offset=0, duration=1000)

    def scroll_to_headphones(self, e):
        self.page_without_header.scroll_to(key="34", duration=1000)

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.page.update()

    def on_scroll(self, e: ft.OnScrollEvent):
        if e.pixels > 100:
            self.header.change_transparency_of_background(to_transparent=False)
        else:
            self.header.change_transparency_of_background(to_transparent=True)

#Test launch (python -m ui.main_page)
if __name__ == "__main__":
    from ui.video import Video
    from ui.banner import Banner
    from ui.headphones_row import HeadphonesRow
    import asyncio
    async def main(page: ft.Page):
        page.expand_loose = True
        video = Video(page)
        banner = Banner(page, video)
        headphones_row = HeadphonesRow(page)
        main_page = MainPage(page)
        main_page.controls.extend([banner, headphones_row])

        def scroll_to_key(e):
            main_page.scroll_to(key="34", duration=1000)

        banner.container_for_button.on_click = scroll_to_key

        page.add(main_page)
        video.playlist_add(video.videoBanner)

        await video.start_loop_play()

        page.update()

    app = asyncio.run(ft.app_async(main))
