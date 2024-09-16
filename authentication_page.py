import flet as ft
import requests
#from typing import Tuple

def login_request(matricula: ft.Page, colaborador: ft.Page):
    """Envia uma requisição POST para autenticar o usuário e retorna o resultado."""
    data = {
        'nome': matricula,
        'senha': ''
    }

    response = requests.post('http://localhost:8000/colaborador/colaborador/', json=data)
    
    # Verifica o status da resposta
    if response.status_code == 200:
        try:
            data = response.json()
            success = data.get('success', False)  # Espera-se um booleano
            message = data.get('message', 'Erro desconhecido')  # Espera-se uma string
            return success, message
        except requests.exceptions.JSONDecodeError:
            return False, 'Erro ao processar a resposta do servidor'
    else:
        return False, f'Erro no servidor: {response.status_code}'
 

def show_authentication_page(page: ft.Page) -> None:
    """Exibe a página de autenticação e lida com o login do usuário."""
    
    # Definindo o tamanho da janela
    page.window.width = 450
    page.window.height = 700

    matricula_field = ft.TextField(
        label='Matricula',
        width=250,
        key='matricula_field'
    )

    senha_field = ft.TextField(
        label='Senha',
        password=True,
        width=250,
        key='senha_field'
    )

    def on_login_click(e: ft.ControlEvent) -> None:
        """Ação a ser realizada quando o botão de login é clicado."""
        matricula_value = matricula_field.value
        senha_value = senha_field.value
        success, message = login_request(matricula_value, senha_value)
        
        if success:
            from option_pages import show_options_page
            show_options_page(page)
        else:
            # Exibir mensagem de erro como SnackBar corretamente
            snack_bar = ft.SnackBar(
                content=ft.Text(message),
                open=True
            )
            
            page.snack_bar = snack_bar  # Define o snack_bar no objeto page
            page.update()  # Atualiza a página para exibir o snack_bar

    auth_page = ft.Container(
        width=400,
        height=600,
        bgcolor='#E8EAF6',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.9, color='black')),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Image(
                    src='assets/image/logo.png',
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN
                ),
                ft.Text(
                    value='Autenticação',
                    color='black',
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                matricula_field,
                senha_field,
                ft.ElevatedButton(
                    text="Entrar",
                    bgcolor='#041955',
                    color='white',
                    on_click=on_login_click
                )
            ]
        )
    )

    page.controls.clear()
    page.add(auth_page)
    page.update()




