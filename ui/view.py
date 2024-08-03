import asyncio
import flet as ft
from ui.banner import Banner
from ui.video import Video
from ui.footer import Footer
from ui.main_page import MainPage
from ui.headphones_row import HeadphonesRow
from ui.item_page import HeadphonesPage
from src.viewmodel.viewmodel import ViewModel
from fastapi import FastAPI, Request, Response
import fastapi
from flet import fastapi as flet_fastapi
import re
import repath

class View():
    def __init__(self, viewmodel: ViewModel):
        self.viewmodel = viewmodel
        self.product_id = 0
        self.headphones_id = 0


    async def main(self, page: ft.Page):
        self.page = page
        self.templeroute = TemplateRoute(self.page.route)
        self.main_page = MainPage(self.page)
        self.video = Video(self.page)
        self.banner = Banner(self.page, self.video)
        self.headphones_row = HeadphonesRow(self.page, self.viewmodel)
        await self.headphones_row.set_headphones_in_controls()
        self.footer = Footer(self.page)
        self.main_page.page_without_header.controls.extend([self.banner, self.headphones_row, self.footer])

        async def set_main_page():
            self.page.clean()
            self.page.add(self.main_page)

            def scroll_to_key(e, key: str):
                self.main_page.page_without_header.scroll_to(key=key, duration=1000)

            def scroll_to_begin(e):
                self.main_page.page_without_header.scroll_to(offset=0, duration=1000)

            self.banner.container_for_button.on_click = lambda e: scroll_to_key(e=e, key="34")
            self.main_page.header.scroll_to_headphones_button.on_click = lambda e: scroll_to_key(e=e, key="34")
            self.main_page.header.scroll_to_begin_button.on_click = lambda e: scroll_to_begin(e=e)
            self.video.playlist_add(self.video.videoBanner)
            self.video.start_play()
            self.page.update()

        async def set_headphones_page():
            self.video.stop_play()
            await self.page.clean_async()
            self.page.bgcolor = "000000"
            self.page.padding = 0
            self.headphones_page = HeadphonesPage(page=self.page, headphones_id=self.headphones_id)
            self.page.add(self.headphones_page)

        async def check_route(route : ft.RouteChangeEvent):
            self.templeroute.route = route.route

            #Headphones page
            if self.page.route.startswith("/headphones"):
                if self.templeroute.match("/headphones/:id"):
                    self.headphones_id = self.templeroute.id
                    await set_headphones_page()
                self.page.update()

            #Main page
            if self.page.route == "/":
                # self.page.views.clear()
                await set_main_page()
                self.page.padding = 0
                self.page.update()

        await check_route(ft.RouteChangeEvent(route=self.templeroute.route))
        self.page.on_route_change = check_route

class TemplateRoute():
    def __init__(self, route: str) -> None:
        self.__last_params = {}
        self.route = route

    def match(self, route_template: str) -> bool:
        # remove old properties
        for k in self.__last_params:
            setattr(self, k, None)

        # perform new match
        pattern = repath.pattern(route_template)
        match = re.match(pattern, self.route)

        if match:
            self.__last_params = match.groupdict()
            for k, v in self.__last_params.items():
                setattr(self, k, v)
            return True
        return False
