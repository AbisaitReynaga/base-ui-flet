import flet as ft

class Content(ft.Container):
    def __init__(self):
        super().__init__(bgcolor="cyan",expand=True)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ ft.Text("CONTENT",size=40,color="white",weight=ft.FontWeight.BOLD)]
        )