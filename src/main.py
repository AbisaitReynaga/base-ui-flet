import flet as ft
from templates.MainLayout import MainLayout

def main(page: ft.Page):
    page.title="UI structure"
    page.add(MainLayout())

ft.app(target=main)
