import flet as ft
from ui.header import HeaderOutsideMainPage
from ui.delivery_info import DeliveryInfo
from ui.cart_info import CartInfo
from ui.footer import Footer


class CheckoutPage(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

        self.header = HeaderOutsideMainPage(self.page)
        self.footer = Footer(self.page)

        self.cart_info = ft.Container(
            content=CartInfo(),
            expand=True,
            padding=ft.Padding(left=30,right=30,top=10,bottom=10)
        )
        self.delivery_info = ft.Container(
            content=DeliveryInfo(),
            expand=True,
            padding=ft.Padding(left=30,right=30,top=10,bottom=10)
        )

        self.info = ft.Row(
            controls=[
                self.delivery_info,
                self.cart_info
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=50,
        )

        self.page_with_divider = ft.Column(
            controls=[
                ft.Divider(height=50),
                self.info,
            ],
            expand = True,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            on_scroll_interval = 0,
        )

        self.page_without_header = ft.Column(
            controls=[
                self.page_with_divider,
                self.footer
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )


        self.controls = [
            self.page_without_header,
            self.header,
        ]

        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.page.update()


# Test launch (python -m ui.checkout_page)
if __name__ == "__main__":
    def main(page: ft.Page):
        checkout_page = CheckoutPage(page)
        page.padding = 0
        page.bgcolor = "#e4c4c4"
        page.add(checkout_page)

    app = ft.app(main)
