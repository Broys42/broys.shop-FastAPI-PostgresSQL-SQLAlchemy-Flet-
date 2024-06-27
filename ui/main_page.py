import flet as ft

class MainPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resized = self.page_on_resize

        self.expand = 1
        #Expand create white borders. To fix this list is a little bit scaled
        self.scale = 1.02
        self.on_scroll_interval = 1
        self.scroll = ft.ScrollMode.ALWAYS

        self.controls = [

        ]

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()


#Test launch
if __name__ == "__main__":
    from video import Video
    from banner import Banner
    import asyncio
    async def main(page: ft.Page):
        video = Video(page)
        banner = Banner(page, video)
        spacer = ft.Container(bgcolor="#000000", height=10000, key="34")
        main_page = MainPage(page)
        main_page.controls.extend([banner, spacer])
        page.add(main_page)
        video.playlist_add(video.videoBanner)
        page.update()

        await video.start_loop_play()

        def scroll_to_key(e):
            main_page.scroll_to(key="34", duration=1000)

        banner.container_for_button.on_click = scroll_to_key
        page.update()

    app = asyncio.run(ft.app_async(main))
