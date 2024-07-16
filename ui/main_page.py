import flet as ft
from ui.header import HeaderInMainPage

class MainPage(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

        self.header = HeaderInMainPage(page=page)

        self.page_without_header = ft.Column(
            controls=[

            ],
            expand = True,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            on_scroll_interval = 0,
            on_scroll=self.on_scroll
        )

        self.controls = [
            self.page_without_header,
            self.header
        ]

        self.page.on_resized = self.page_on_resize

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
