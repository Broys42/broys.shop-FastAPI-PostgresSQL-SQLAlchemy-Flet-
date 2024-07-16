import flet as ft
from ui.item_counter import ItemCounter


class CartItem(ft.Column):
    def __init__(self):
        super().__init__()
        self.divider = ft.Divider(height=4, thickness=1, color="white")

        self.item_image = ft.Image(
            src="https://raw.githubusercontent.com/Broys42/broys.shop/main/assets/images/headphones/a50-gallery-ps4-01-refresh.png",
        )

        self.item_title = ft.Text(
            value="Название",
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD
        )

        self.item_price = ft.Text(
            value="Цена",
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.NORMAL
        )

        self.item_info = ft.Column(
            controls=[
                self.item_title,
                self.item_price
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.item_counter = ItemCounter()

        self.item = ft.Row(
            controls=[
                self.item_image,
                self.item_info
            ]
        )

        self.item_with_counter = ft.Row(
            controls=[
                self.item,
                self.item_counter
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=150
        )

        self.controls = [
            self.item_with_counter,
            self.divider
        ]


# Test launch (python -m ui.cart_item)
if __name__ == "__main__":
    def main(page: ft.Page):
        cart_item = CartItem()
        page.bgcolor = "#e4c4c4"
        page.add(cart_item)

    app = ft.app(main)
