import flet as ft

class TopContainer(ft.Container):
    def __init__(self, bgcolor):
        super().__init__(bgcolor=bgcolor, expand=True)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ ft.Text("HEADER",size=40,color="white",weight=ft.FontWeight.BOLD)]
        )
