import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    usuario_valido = "admin@gmail.com"
    password_valido = "1234"

    titulo = ft.Text(
        "Inicio de sesión",
        size=30,
        weight=ft.FontWeight.BOLD,
    )

    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=350,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=350
    )

    mensaje = ft.Text("", color="red")

    def pantalla_principal():

        page.clean()

        # Barra inferior
        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ]
        )

        # Panel superior
        panel = ft.Container(
            content=ft.Text(
                "Panel Principal",
                size=20,
                color="white"
            ),
            bgcolor=ft.Colors.BLACK87,
            padding=10,
            width=page.width
        )

        bienvenida = ft.Text(
            "Bienvenido al Sistema",
            size=30,
            weight=ft.FontWeight.BOLD
        )

        subtitulo = ft.Text(
            "Has iniciado sesión correctamente.",
            color="grey"
        )

        page.add(
            ft.Column(
                [
                    panel,
                    ft.Container(height=120),
                    bienvenida,
                    subtitulo
                ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
            )
        )

        page.update()

    def login(e):

        if correo.value == usuario_valido and contraseña.value == password_valido:
            pantalla_principal()
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        width=200,
        on_click=login,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    registro = ft.ElevatedButton(
        "Registrarme",
        width=200,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_800,
            color=ft.Colors.WHITE,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    link_forgot = ft.TextButton("¿Olvidaste tu contraseña?")

    page.add(
        ft.Column(
            [
                titulo,
                correo,
                contraseña,
                mensaje,
                link_forgot,
                ft.Row(
                    [iniciar_sesion, registro],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)