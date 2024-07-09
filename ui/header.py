import flet as ft


class Header(ft.Stack):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.height = 50
        self.page = page
        self.alignment = ft.alignment.center

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

        self.scroll_to_headphones_button = ft.Container(
            content=ft.Text(
                value="Наушники",
                weight=ft.FontWeight.BOLD,
            ),
        )

        self.scroll_to_begin_button = ft.Container(
            content=ft.Text(
                value="В начало",
                weight=ft.FontWeight.BOLD,
            )
        )

        self.show_contacts_button = ft.Container(
            content=ft.Text(
                value="Контакты",
                weight=ft.FontWeight.BOLD
            ),
        )

        self.logo_text = ft.Container(
            content=ft.Text(
                value="BROYS SHOP",
                weight=ft.FontWeight.BOLD,
            ),
            padding=ft.Padding(left=30, right=0, top=0, bottom=0),
            width=150
        )

        self.text_buttons_row = ft.Row(
            controls=[
                self.scroll_to_begin_button,
                self.scroll_to_headphones_button,
                self.show_contacts_button
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        #No IconButton to avoid all control animation
        self.shop_bag_icon = ft.Icon(
            name="SHOPPING_BAG",
            color="black",
            size=20,
        )

        self.container_for_icon = ft.Container(
            content=self.shop_bag_icon,
            alignment=ft.alignment.center_right,
            padding=ft.Padding(left=0, right=30, top=0, bottom=0),
            width=150
        )

        self.header_buttons = ft.Row(
            controls=[
                self.logo_text,
                self.text_buttons_row,
                self.container_for_icon
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
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
