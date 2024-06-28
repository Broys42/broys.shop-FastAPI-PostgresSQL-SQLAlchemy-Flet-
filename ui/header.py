import flet as ft


class Header(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.height = 50
        self.page = page
        self.alignment=ft.alignment.center

        self.transparent_background_color = ft.Container(
            bgcolor="#00ffffff",
            padding=0
        )

        self.not_transparent_background_color = ft.Container(
            bgcolor="#ffffff",
            padding=0
        )

        self.transparent_switcher = ft.AnimatedSwitcher(
            self.transparent_background_color,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=500,
            switch_in_curve=ft.AnimationCurve.EASE_IN,
            switch_out_curve=ft.AnimationCurve.EASE_IN,
        )

        self.scroll_to_headphones = ft.Container(
            content=ft.Text(
                value="Headphones",
                weight=ft.FontWeight.BOLD
            ),
        )

        self.scroll_to_begin = ft.Container(
            content=ft.Text(
                value="Begin",
                weight=ft.FontWeight.BOLD,
                color="#000000"
            ),
            margin=10
        )

        self.show_contacts_button = ft.Container(
            content=ft.Text(
                value="Contacts",
                weight=ft.FontWeight.BOLD
            ),
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
            self.transparent_switcher,
            self.header_buttons
        ]

    def change_transparency_of_background(self, to_transparent: bool):
        self.transparent_switcher.content = self.transparent_background_color if to_transparent else self.not_transparent_background_color
        self.transparent_switcher.update()

#Test launch (python -m ui.header)
if __name__ == "__main__":
    def main(page: ft.Page):
        page.padding = 0
        header = Header(page)
        page.add(header)
        page.bgcolor = "black"
        page.update()
    app = ft.app(main)
