import flet as ft


class Header(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.height = 50
        self.page = page
        self.alignment=ft.alignment.center
        self.background_color = ft.Container(
            bgcolor="#ffffff",
            padding=0
        )

        self.scroll_to_headphones = ft.Container(
            content=ft.Text("Headphones"),
        )

        self.scroll_to_begin = ft.Container(
            content=ft.Text("Begin"),
        )

        self.show_contacts_button = ft.Container(
            content=ft.Text("Contacts"),
        )

        self.text_buttons_row = ft.Row(
            controls=[
                self.scroll_to_begin,
                self.scroll_to_headphones,
                self.show_contacts_button
            ],
            spacing=30
        )

        self.header_buttons = ft.Row(
            controls=[
                ft.Text("Logo"),
                self.text_buttons_row,
                ft.Text("")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.controls = [
            self.background_color,
            self.header_buttons
        ]

#Test launch (python -m ui.header)
if __name__ == "__main__":
    def main(page: ft.Page):
        page.padding = 0
        header = Header()
        page.add(header)
        page.bgcolor = "black"
        page.update()
    app = ft.app(main)
