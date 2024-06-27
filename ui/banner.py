import flet as ft
import asyncio

class Banner(ft.Stack):
    def __init__(self, page: ft.Page, video: ft.Video):
        super().__init__()
        self.video = video
        self.page = page
        self.height = self.page.height
        self.width = self.page.width

        self.title = ft.Text(
            value="Пусть музыка станет ближе",
            size=40,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        )

        self.subtitle = ft.Text(
            value="Новая коллекция игровых наушников ниже!",
            size=20,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL
        )

        self.button_background = ft.Container(
            bgcolor='#ffffff',
            width=300,
            height=50
        )

        self.button_text = ft.Text(
            value="Перейти к товару",
            size=15,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD
        )

        self.button = ft.Stack(
            controls=[
                self.button_background,
                self.button_text
            ],
            alignment=ft.alignment.center,
        )

        #Stack dont support click event so button also plased in container
        self.container_for_button = ft.Container(
            content=self.button,
        )

        self.text_column = ft.Column(
            controls=[
            self.title,
            self.subtitle,
            ],
            spacing=-10,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.text_and_button_column = ft.Column(
            controls=[
            self.text_column,
            self.container_for_button
            ],
            spacing=40,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.container = ft.Container(
            content=self.text_and_button_column,
            alignment=ft.alignment.center
        )

        self.controls = [
            self.video,
            self.container,
        ]

        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()

#Test launch
if __name__ == "__main__":
    from video import Video
    import asyncio
    async def main(page: ft.Page):
        video = Video(page)
        banner = Banner(page, video)
        page.add(banner)
        video.add_video_in_playlist()
        page.update()
        await video.start_loop_play()
    app = asyncio.run(ft.app_async(main))
