import flet as ft
from ui.cart_item import CartItem
from ui.info_title import InfoTitle


class CartInfo(ft.Column):
    def __init__(self):
        super().__init__()
        self.scroll = ft.ScrollMode.ALWAYS
        self.title = InfoTitle("Корзина")

        self.column_with_title = ft.Column(
            controls=[
                self.title
            ]
        )

        self.cart_items = ft.Column(
            controls=[
                CartItem(),
                CartItem(),
                CartItem(),
                CartItem(),
                CartItem(),
            ],
            # expand=True,
            scroll=ft.ScrollMode.ALWAYS,
        )

        self.controls = [
            self.column_with_title,
            self.cart_items
        ]


# Test launch (python -m ui.cart_info)
if __name__ == "__main__":
    def main(page: ft.Page):
        cart_info = CartInfo()
        page.bgcolor = "black"
        page.add(cart_info)

    app = ft.app(main)
