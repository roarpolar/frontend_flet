# option_pages.py
import flet as ft
from authentication_page import show_authentication_page

def show_options_page(page):
    options_page = ft.Container(
        width=400,
        height=600,
        bgcolor='#F5F5F5',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.9, color='black')),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text(
                    value='Página de Opções',
                    color='black',
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.ElevatedButton(
                    text="Voltar para Login",
                    bgcolor='#041955',
                    color='white',
                    on_click=lambda e: show_authentication_page(page)
                )
            ]
        )
    )
    page.controls.clear()
    page.add(options_page)
    page.update()