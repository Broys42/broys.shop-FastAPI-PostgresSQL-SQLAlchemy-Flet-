import flet as ft


class DeliveryTextField(ft.Column):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.text_title = ft.Text(
            value=f"{self.title}",
            size=17,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.NORMAL
        )

        self.textField = ft.TextField(
            cursor_color=ft.colors.BLACK,
            border_color=ft.colors.BLACK,
            focused_border_color=ft.colors.BLACK,
            color=ft.colors.BLACK,
        )

        self.controls = [
            self.text_title,
            self.textField
        ]

# Test launch (python -m ui.delivery_textfield)
if __name__ == "__main__":
    def main(page: ft.Page):
        delivery_textfield = DeliveryTextField("Тест")
        page.bgcolor = "black"
        page.add(delivery_textfield)

    app = ft.app(main)
