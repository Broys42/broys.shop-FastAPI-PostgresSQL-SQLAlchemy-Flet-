import flet as ft
from ui.delivery_textfield import DeliveryTextField
from ui.main_btn import MainButton
from ui.info_title import InfoTitle


class DeliveryInfo(ft.Column):
    def __init__(self):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.scroll = ft.ScrollMode.ALWAYS
        self.spacing = 30

        self.title = InfoTitle("Информация о доставке")

        self.city = DeliveryTextField("Город")
        self.postoffice = DeliveryTextField("Почтовое отделение")
        self.email = DeliveryTextField("Email")
        self.fio = DeliveryTextField("Получатель (ФИО полностью)")
        self.comment = DeliveryTextField("Комментарий")
        self.promocode = DeliveryTextField("Промокод")

        self.checkout_button = MainButton("Оформить заказ")

        self.controls = [
            self.title,
            self.fio,
            self.email,
            self.city,
            self.postoffice,
            self.comment,
            self.promocode,
            self.checkout_button
        ]


# Test launch (python -m ui.delivery_info)
if __name__ == "__main__":
    def main(page: ft.Page):
        delivery_info = DeliveryInfo()
        page.bgcolor = "black"
        page.add(delivery_info)

    app = ft.app(main)
