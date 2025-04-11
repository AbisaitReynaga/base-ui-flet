import flet as ft

class SideBarContainer(ft.Container):
    def __init__(self):
        super().__init__(bgcolor="red",expand=True)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ ft.Text("NAV MENU",size=40,color="white",weight=ft.FontWeight.BOLD)]
        )