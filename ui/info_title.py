import flet as ft

class InfoTitle(ft.Column):
    def __init__(self, title):
        super().__init__()
        self.title = title

        self.text_title = ft.Text(
            value=f"{title}",
            size=24,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD
        )

        self.divider = ft.Divider(height=4, thickness=1, color="white")

        self.controls = [
            self.text_title,
            self.divider
        ]

#Test launch (python -m ui.info_title)
if __name__ == "__main__":
    def main(page: ft.Page):
        info_title = InfoTitle("Заголовок")
        page.bgcolor = "black"
        page.add(info_title)
    app = ft.app(main)
