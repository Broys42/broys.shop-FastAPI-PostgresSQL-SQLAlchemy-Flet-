import flet as ft
from ui.main_btn import MainButton
from ui.item_counter import ItemCounter


class ItemPage(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.height = 500
        self.add_in_cart_button = MainButton()
        self.item_counter = ItemCounter()

        self.add_in_cart_button.button_text.value = "Добавить в корзину"

        self.item_image = ft.Image(
            src="https://raw.githubusercontent.com/Broys42/broys.shop/main/assets/images/headphones/a50-gallery-ps4-01-refresh.png",
            width=500,
            height=500,
            fit = ft.ImageFit.FIT_HEIGHT
        )

        self.item_title = ft.Text(
            value="Item Title",
            size=50,
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

        self.item_info_pannel = ft.Column(
            controls=[
                self.item_title,
                ft.Divider(thickness=3, color="white"),
                self.item_counter,
                self.item_description,
                self.add_in_cart_button
            ],
            width=300,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.controls = [
            self.item_image,
            self.item_info_pannel
        ]


#Test launch (python -m ui.item_page)
if __name__ == "__main__":
    def main(page: ft.Page):
        item_page = ItemPage(page)
        page.add(item_page)
        page.bgcolor = "black"
        page.update()

    ft.app(main)
