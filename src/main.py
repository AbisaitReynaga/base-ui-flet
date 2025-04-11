import flet as ft
from templates.MainLayout import MainLayout

def main(page: ft.Page):
    page.window_width = 900
    page.window_height = 600
    page.add(MainLayout())

ft.app(target=main)
