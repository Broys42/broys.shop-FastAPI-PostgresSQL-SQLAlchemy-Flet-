import flet as ft
from ui.headphones_item import HeadphonesItem

class HeadphonesRow(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.wrap = True
        self.width = 1440
        self.scroll = False
        self.run_spacing = 50
        self.spacing = 50
        self.key = "34"
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [

        ]

        self.page.on_resized = self.page_on_resize

        for i in range(10):
            self.controls.append(HeadphonesItem())

    def page_on_resize(self, e: ft.WindowResizeEvent):
        # self.height = e.page.height
        self.width = 1440
        self.page.update()

#Test launch (python -m ui.headphones_row)
if __name__ == "__main__":
    def main(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        headphones_column = HeadphonesRow(page)
        page.add(headphones_column)
        page.expand_loose = True
        page.bgcolor = "black"
        page.update()
    app = ft.app(main)
