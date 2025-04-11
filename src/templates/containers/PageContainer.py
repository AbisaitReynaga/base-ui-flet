import flet as ft
from .SideBarContainer import SideBarContainer
from .Content import Content
class PageContainer(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Row(col=2,controls=[SideBarContainer()],expand=True),
                ft.Row(col=10,controls=[Content()])
            ]
        )
