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
        self.conteiner_for_button = ft.Container(
            content=self.button,
            on_click=self.on_button_click
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
            self.conteiner_for_button
            ],
            spacing=40,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.conteiner = ft.Container(
            content=self.text_and_button_column,
            alignment=ft.alignment.center
        )

        self.controls = [
            self.video,
            self.conteiner,
        ]

        self.page.on_resize = self.page_on_resize

    def on_button_click(self):
        print("button clicked")

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()
