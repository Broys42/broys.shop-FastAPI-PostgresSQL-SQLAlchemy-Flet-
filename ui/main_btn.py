import flet as ft

class MainButton(ft.Stack):
    def __init__(self):
        super().__init__()

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

        self.controls =[
                self.button_background,
                self.button_text
            ]

        self.alignment=ft.alignment.center


#Test launch (python -m ui.main_btn)
if __name__ == "__main__":
    def main(page: ft.Page):
        main_btn = MainButton()
        page.bgcolor = "black"
        page.add(main_btn)

    ft.app(main)
