import asyncio
import flet as ft
from ui.main_btn import MainButton
from ui.item_counter import ItemCounter
from ui.header import HeaderOutsideMainPage
from ui.footer import Footer

class HeadphonesPage(ft.Stack):
    def __init__(self, page: ft.Page, headphones_id):
        super().__init__()
        self.page = page
        self.expand = True

        self.page.padding = 0

        self.header = HeaderOutsideMainPage(self.page)
        self.footer = Footer(self.page)

        self.headphones_id = headphones_id

        self.add_in_cart_button = MainButton(
            button_text="Добавить в корзину", width=300)

        self.item_counter = ItemCounter()

        self.item_image = ft.Image(
            src="https://raw.githubusercontent.com/Broys42/broys.shop/main/assets/images/headphones/a50-gallery-ps4-01-refresh.png",
            width=500,
            height=450,
            fit=ft.ImageFit.FIT_HEIGHT
        )

        self.item_title = ft.Text(
            value=f"{self.headphones_id}",
            size=40,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD
        )

        self.item_price = ft.Text(
            value="Item Price",
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL
        )

        self.item_description = ft.Text(
            value="Цвет - Пиксельный Арт\nРазмер - 450x400мм\nТолщина - 4мм\nМатериал - Ткань\nОснова - Эко Резина\nТип поверхности - Баланс",
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        )

        self.item_title_and_divider = ft.Column(
            controls=[
                self.item_title,
                ft.Divider(thickness=1, color="white")
            ],
            spacing=0
        )

        self.item_counter_and_description = ft.Column(
            controls=[
                self.item_counter,
                self.item_description,
            ],
            spacing=10
        )

        self.item_info_pannel = ft.Column(
            controls=[
                self.item_title_and_divider,
                self.item_counter_and_description,
                self.add_in_cart_button
            ],
            width=300,
            height=400,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.item_card = ft.Row(
            controls=[
            self.item_image,
            self.item_info_pannel
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )


        # Divider is save space for header
        self.page_with_divider = ft.Column(
            controls=[
                ft.Divider(height=50),
                self.item_card,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )

        self.page_without_header = ft.Column(
            controls=[
                self.page_with_divider,
                self.footer
            ],
            alignment=ft.alignment.center,
        )

        self.controls = [
            self.page_without_header,
            self.header,
        ]

        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.page.update()

    def change_product(self, headphones_id):
        self.headphones_id=headphones_id
        print("Updated")
        self.update()


# Test launch (python -m ui.item_page)
if __name__ == "__main__":
    async def main(page: ft.Page):
        page.bgcolor = "#e4c4c4"
        item_page=HeadphonesPage(page=page, headphones_id=123)
        page.padding = 0
        page.add(item_page)

    asyncio.run(ft.app_async(main))
