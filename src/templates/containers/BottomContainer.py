import flet as ft

class BottomContainer(ft.Container):
    def __init__(self, bgcolor):
        super().__init__(bgcolor=bgcolor, expand=True)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ ft.Text("FOOTER",size=40,color="white",weight=ft.FontWeight.BOLD)]
        )
