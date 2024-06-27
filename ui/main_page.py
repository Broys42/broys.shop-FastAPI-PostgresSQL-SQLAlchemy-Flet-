import flet as ft

class MainPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resized = self.page_on_resize
        self.expand = True
        #Expand create white borders. To fix this list is a little bit scaled
        self.scale = 1.02
        self.on_scroll_interval = 1
        self.scroll = ft.ScrollMode.ALWAYS
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [

        ]
        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()


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
