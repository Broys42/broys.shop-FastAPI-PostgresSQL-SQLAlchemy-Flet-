import flet as ft

class MainButton(ft.Stack):
    def __init__(self, button_text, width = None):
        super().__init__()
        self.button_text = button_text

        self.button_background = ft.Container(
            bgcolor='#ffffff',
            width=width,
            height=50
        )

        self.button_text = ft.Text(
            value=f"{button_text}",
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
        main_btn = MainButton(button_text="Тестовая кнопка")
        page.bgcolor = "black"
        page.add(main_btn)

    ft.app(main)
