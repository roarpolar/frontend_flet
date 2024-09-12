import flet as ft  # Importa a biblioteca corretamente
from authentication_page import show_authentication_page  # Importa a função de autenticação

def main(page: ft.Page):
    page.bgcolor = '#041955'
    #page.theme_mode = 'white'
    page.title = 'Arpol Quality Care'
    page.window_width = 450 
    page.window_height = 700 
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor='blue')
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = ft.BottomAppBar(
        bgcolor='F6F6F6FF',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.BLUE, icon_size=28),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.BLUE,  icon_size=28),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.BLUE,  icon_size=28),
                ft.IconButton(icon=ft.icons.FAVORITE,  icon_color=ft.colors.BLUE,  icon_size=28)
            ]
        ),
    )

    # Container Principal
    _main = ft.Container(
        width=400, 
        height=600,
        bgcolor='#FCFAA7', 
        border_radius=16, 
        alignment=ft.alignment.center,  # Centraliza o conteúdo verticalmente
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.4, color='black')),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Alinha os itens no centro da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha horizontalmente no centro
            spacing=20,  # Adiciona espaço entre os controles
            controls=[
                # Adiciona a primeira imagem (logo.png) ao topo
                ft.Image(
                    src='assets/image/logo.png',
                    width=100,  # Ajuste o tamanho da imagem conforme necessário
                    height=100,
                    fit=ft.ImageFit.CONTAIN  # Garante que a imagem se ajuste sem distorção
                ),
                ft.Text(
                    value='Sejam Bem-vindos',
                    color='black',
                    size=24,  # Aumenta o tamanho da fonte
                    weight=ft.FontWeight.BOLD  # Deixa o texto em negrito
                ),
                # Segunda imagem (arpolar.png)
                ft.Image(
                    src='assets/image/arpolar.png',
                    width=200,  # Ajuste o tamanho da imagem conforme necessário
                    height=200,
                    fit=ft.ImageFit.CONTAIN  # Garante que a imagem se ajuste sem distorção
                ),
                # Botão de "Acessar Aqui"
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Acessar Aqui",
                        width=150,
                        on_click=lambda e: show_authentication_page(page),  # Chama a página de autenticação
                    #    on_click=lambda e: print("Botão 'Acessar Aqui' clicado!"),
                        bgcolor='#041955',  # Define a cor de fundo do botão
                        color='white'  # Define a cor do texto como branca
                    )
                )   
            ]
        )
    )

    # Stack principal 
    _stack_main = ft.Stack(
        alignment=ft.alignment.center,
        controls=[
            _main

        ]
    )

    
    page.add(_stack_main)


ft.app(target=main)

