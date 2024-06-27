import flet as ft
import asyncio

class Video(ft.Video):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resized = self.page_on_resize

        #Video doesnt have auto-fullscreen-mode so to fill white frame video is little bit scaled
        self.scale = 1.05

        #This VideoMedia later add in playlist by playlist_add_media()
        self.videoBanner = ft.VideoMedia(
            resource='https://github.com/Broys42/broys.shop/raw/main/assets/video/video.mp4',
        )
        self.is_loaded = False

        self.expand=True
        self.playlist_mode=ft.PlaylistMode.LOOP
        self.fill_color=ft.colors.BLUE_400
        self.aspect_ratio=self.page.width/self.page.height
        self.show_controls=False
        self.volume=0
        self.fit=ft.ImageFit.COVER
        self.autoplay=True
        self.filter_quality=ft.FilterQuality.HIGH
        self.muted=True
        self.on_loaded=lambda e: self.switch_is_loated()
        self.on_enter_fullscreen=lambda e: print("Video entered fullscreen!")
        self.on_exit_fullscreen=lambda e: print("Video exited fullscreen!")

    def add_video_in_playlist(self):
        self.playlist_add(self.videoBanner)

    def switch_is_loated(self):
        self.is_loaded = True

    async def start_loop_play(self):
        while True:
            await asyncio.sleep(0.1)
            self.play()

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.aspect_ratio=self.page.width/self.page.height
        self.page.update()

#Test launch
if __name__ == "__main__":
    async def main(page: ft.Page):
        video = Video(page)
        page.add(video)
        video.add_video_in_playlist()
        page.update()
        await video.start_loop_play()

    app = asyncio.run(ft.app_async(main))
