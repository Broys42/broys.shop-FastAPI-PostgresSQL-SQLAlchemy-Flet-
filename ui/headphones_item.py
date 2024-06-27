import flet as ft

class HeadphonesItem(ft.Column):
    def __init__(self):
        super().__init__()
        self.background_rectangle = ft.Container(
            bgcolor="#f3f3f3",
        )

        self.headphones_image = ft.Image(
            src='https://raw.githubusercontent.com/Broys42/broys.shop/main/assets/images/headphones/a50-gallery-ps4-01-refresh.png'
        )

        self.item_title = ft.Text(
            value="G 735 - WHITE",
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.NORMAL
        )

        self.item_price = ft.Text(
            value="2500",
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD
        )

        self.title_and_price = ft.Column(
            controls=[
                self.item_title,
                self.item_price
            ],
            spacing=5
        )

        self.image_and_background = ft.Stack(
            controls=[
                self.background_rectangle,
                self.headphones_image
            ],
            alignment=ft.alignment.center,
            height=400,
            width=400
        )


        self.controls = [
            self.image_and_background,
            self.title_and_price
        ]


#Test launch (python -m ui.headphones_ui)
if __name__ == "__main__":
    def main(page: ft.Page):
        headphones = HeadphonesItem()
        page.add(headphones)
        page.bgcolor = "black"
        page.update()
    app = ft.app(main)
