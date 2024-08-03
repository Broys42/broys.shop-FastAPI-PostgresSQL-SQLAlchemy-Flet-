import flet as ft
from ui.headphones_item import HeadphonesItem
from src.viewmodel.viewmodel import ViewModel

class HeadphonesRow(ft.Row):
    def __init__(self, page: ft.Page, viewmodel: ViewModel):
        super().__init__()
        self.viewmodel = viewmodel
        self.page = page
        self.headphones_items : list[HeadphonesItem] = []
        self.wrap = True
        self.width = 1440
        self.scroll = False
        self.run_spacing = 50
        self.spacing = 50
        self.key = "34"
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [

        ]

        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        # self.height = e.page.height
        self.width = 1440
        self.page.update()

    async def set_headphones_in_controls(self):
        result = await self.viewmodel.headphones.get_all_headphones()
        for i in result:
            headphones_item = HeadphonesItem(i.id, i.name, i.description, i.price, i.image)
            self.headphones_items.append(headphones_item)
        self.controls.extend(self.headphones_items)
        self.page.update()


#Test launch (python -m ui.headphones_row)
if __name__ == "__main__":
    def main(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        headphones_column = HeadphonesRow(page)
        page.add(headphones_column)
        page.expand_loose = True
        # page.bgcolor = "black"
        page.update()
    app = ft.app(main)
