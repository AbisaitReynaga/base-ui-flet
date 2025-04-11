import flet as ft
from .containers.TopContainer import TopContainer
from .containers.PageContainer import PageContainer
from .containers.BottomContainer import BottomContainer

class MainLayout(ft.Container):
    def __init__(self):
        layout = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[TopContainer("blue")], expand=1),
                ft.Row(controls=[PageContainer()], expand=8),
                ft.Row(controls=[BottomContainer("purple")], expand=1),
            ]
        )
        super().__init__(content=layout, expand=True)
