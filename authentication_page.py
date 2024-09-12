# authentication_page.py
import flet as ft
import requests

# Função para fazer a requisição de login
def login_request(matricula, senha):
    url = "http://localhost:8000/api/login/"  # URL da sua API de login
    data = {
        "matricula": matricula.value,
        "password": senha.value
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Login bem-sucedido!")
            return True, "Login efetuado com sucesso!"
        elif response.status_code == 401:
            return False, "Credenciais inválidas. Verifique sua matrícula e senha."
        elif response.status_code == 404:
            return False, "Usuário não cadastrado. Entre em contato com a supervisão."
        else:
            return False, f"Erro de login: {response.status_code}"
    except Exception as e:
        return False, f"Erro ao conectar com a API: {e}"
    
# Função para exibir a página de autenticação
def show_authentication_page(page):
    # Criação do container da página de autenticação
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
                                # Adiciona a primeira imagem (logo.png) ao topo
                ft.Image(
                    src='assets/image/logo.png',
                    width=100,  # Ajuste o tamanho da imagem conforme necessário
                    height=100,
                    fit=ft.ImageFit.CONTAIN
                ),  # Garante que a imagem se ajuste sem distorção
                ft.Text(
                    value='Autenticação',
                    color='black',
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                # Campo de login
                ft.TextField(
                    label='Matricula',
                    width=250
                ),
                # Campo de senha
                ft.TextField(
                    label='Senha',
                    password=True,
                    width=250
                ),
                # Botão de login
                ft.ElevatedButton(
                    text="Entrar",
                    bgcolor='#041955',
                    color='white',
                    on_click=lambda e: print("Login efetuado!")  # Lógica de autenticação aqui
                )
            ]
        )
    )
    # Atualiza o conteúdo da página para exibir a página de autenticação
    page.controls.clear()
    page.add(auth_page)
    page.update()
