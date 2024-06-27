import flet as ft

class MainPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resize = self.page_on_resize

        self.expand = 1
        #Expand create white borders. To fix this list is a little bit scaled
        self.scale = 1.02
        self.on_scroll_interval = 1
        self.scroll = ft.ScrollMode.ALWAYS

        self.controls = [

        ]

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()
