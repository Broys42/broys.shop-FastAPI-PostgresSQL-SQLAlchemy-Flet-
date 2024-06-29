import flet as ft


class Footer(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.height = 50
        self.page = page
        self.alignment = ft.alignment.center

        self.background_color = ft.Container(
            bgcolor="#ffffff",
            padding=0
        )

        self.show_github_button = ft.Container(
            content=ft.Text(
                value="Github",
                weight=ft.FontWeight.BOLD,
            ),
            url="https://github.com/Broys42"
        )

        self.show_resume = ft.Container(
            content=ft.Text(
                value="Resume",
                weight=ft.FontWeight.BOLD,
            ),
            url="https://novosibirsk.hh.ru/resume/32ccd64aff0d5596750039ed1f75587771386a"
        )

        self.show_telegram = ft.Container(
            content=ft.Text(
                value="Telegram",
                weight=ft.FontWeight.BOLD
            ),
            url="https://t.me/clixi42"
        )

        self.footer_buttons = ft.Row(
            controls=[
                self.show_resume,
                self.show_github_button,
                self.show_telegram
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.controls = [
            self.background_color,
            self.footer_buttons
        ]

#Test launch (python -m ui.footer)
if __name__ == "__main__":
    def main(page: ft.Page):
        page.padding = 0
        footer = Footer(page)
        page.add(footer)
        page.bgcolor = "black"
        page.update()
    app = ft.app(main)
