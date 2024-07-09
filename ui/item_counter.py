import flet as ft


class ItemCounter(ft.Row):
    def __init__(self):
        super().__init__()
        self.spacing = 15
        self.count = 0

        self.button_background = ft.Container(
            bgcolor="white"
        )

        self.minus_button = ft.Stack(
            controls=[
                self.button_background,
                ft.Text(
                    value="-",
                    weight=ft.FontWeight.BOLD
                )
            ],
            width=50,
            height=50,
            alignment=ft.alignment.center
        )

        self.plus_button = ft.Stack(
            controls=[
                self.button_background,
                ft.Text(
                    value="+",
                    weight=ft.FontWeight.BOLD
                )
            ],
            width=50,
            height=50,
            alignment=ft.alignment.center
        )

        self.count_number = ft.Stack(
            controls=[
                self.button_background,
                ft.Text(
                    value=f"{self.count}",
                    weight=ft.FontWeight.BOLD
                )
            ],
            width=50,
            height=50,
            alignment=ft.alignment.center
        )

        self.controls = [
            self.minus_button,
            self.count_number,
            self.plus_button
        ]


# Test launch (python -m ui.item_counter)
if __name__ == "__main__":
    def main(page: ft.Page):
        item_counter = ItemCounter()
        page.bgcolor = "black"
        page.add(item_counter)

    ft.app(main)
