import reflex as rx

class State(rx.State):
    username: str = ""
    password: str = ""

    def login(self):
        # Aquí podrías agregar tu lógica de autenticación
        if self.username == "admin" and self.password == "1234":
            print("Inicio de sesión exitoso")
        else:
            print("Usuario o contraseña incorrectos")

def login_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.heading("Iniciar Sesión", size="lg", mb="4"),
            rx.input(
                placeholder="Usuario",
                value=State.username,
                on_change=State.set_username,
                mb="3",
                width="100%"
            ),
            rx.input(
                placeholder="Contraseña",
                type_="password",
                value=State.password,
                on_change=State.set_password,
                mb="3",
                width="100%"
            ),
            rx.button(
                "Entrar",
                on_click=State.login,
                color_scheme="teal",
                width="100%"
            ),
            padding="6",
            box_shadow="lg",
            border_radius="md",
            width="300px",
            background_color="white"
        ),
        height="100vh",
        background_color="#f0f4f8"
    )

app = rx.App()
app.add_page(login_page)
app.compile()
