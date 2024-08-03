import flet as ft
import asyncio

class Video(ft.Video):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resized = self.page_on_resize

        self.expand = True

        #This VideoMedia add in playlist by playlist_add_media() when Video control added in page
        self.videoBanner = ft.VideoMedia(
            resource='https://github.com/Broys42/broys.shop/raw/main/assets/video/video.mp4',
        )
        # self.is_loaded = False
        self.stop_event = asyncio.Event()
        self.expand=True
        self.playlist_mode=ft.PlaylistMode.SINGLE
        self.fill_color="#e4c4c4"
        self.aspect_ratio=self.page.width/self.page.height
        self.show_controls=False
        self.volume=0
        self.fit=ft.ImageFit.COVER
        self.autoplay=True
        self.filter_quality=ft.FilterQuality.HIGH
        self.muted=True
        # self.on_loaded=lambda e: self.switch_is_loated()
        self.on_enter_fullscreen=lambda e: print("Video entered fullscreen!")
        self.on_exit_fullscreen=lambda e: print("Video exited fullscreen!")

    def add_video_in_playlist(self):
        self.playlist_add(self.videoBanner)

    # def switch_is_loated(self):
    #     self.is_loaded = True

    async def start_loop_play(self):
        #Flet is blinkink color when video is repeating. 7500 is duration of video in mlseconds then jump to 0
        while not self.stop_event.is_set():
            await asyncio.sleep(0.1)
            self.play()
            try:
                if await self.get_current_position_async(0.1) > 7500:
                    self.seek(0)
            except:
                pass

    def start_play(self):
        self.stop_event.clear()
        asyncio.create_task(self.start_loop_play())
        self.page.update()

    def stop_play(self):
        self.stop_event.set()
        self.page.update()

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.aspect_ratio=self.page.width/self.page.height
        self.page.update()

#Test launch (python -m ui.video)
if __name__ == "__main__":
    async def main(page: ft.Page):
        video = Video(page)
        page.add(video)
        video.add_video_in_playlist()
        page.update()
        await video.start_loop_play()

    app = asyncio.run(ft.app_async(main))
