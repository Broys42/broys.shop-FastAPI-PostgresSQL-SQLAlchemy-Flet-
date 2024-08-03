import flet as ft

class HeadphonesItem(ft.Column):
    def __init__(self, id, name, price, description, image):
        super().__init__()
        self.name : str = name
        self.price : int = price
        self.description : str = description
        self.image : str = image
        self.id : int = id

        self.background_rectangle = ft.Container(
            bgcolor="#f3f3f3",
        )

        self.headphones_image = ft.Image(
            src=self.image
        )

        self.item_title = ft.Text(
            value=self.name,
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.NORMAL
        )

        self.item_price = ft.Text(
            value=str(self.price) + "₽",
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
