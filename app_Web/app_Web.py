import reflex as rx

class State(rx.State):
    username: str = ""
    password: str = ""

    def login(self):
        if self.username == "admin" and self.password == "1234":
            print("Inicio de sesión exitoso")
        else:
            print("Usuario o contraseña incorrectos")

def login_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.heading("Iniciar Sesión", size="4", mb="4", color="white"),
            rx.input(
                placeholder="Usuario",
                value=State.username,
                on_change=State.set_username,
                mb="3",
                width="100%",
                background_color="#2d3748",
                color="white",
                _placeholder={"color": "#a0aec0"},
            ),
            rx.input(
                placeholder="Contraseña",
                type_="password",
                value=State.password,
                on_change=State.set_password,
                mb="3",
                width="100%",
                background_color="#2d3748",
                color="white",
                _placeholder={"color": "#a0aec0"},
            ),
            rx.button(
                "Entrar",
                on_click=State.login,
                color_scheme="teal",
                width="100%",
                mt="4"
            ),
            padding="6",
            box_shadow="dark-lg",
            border_radius="md",
            width="300px",
            background_color="#1a202c"  # Caja oscura
        ),
        height="100vh",
        background_color="#171923"  # Fondo de toda la pantalla
    )


# Lo correcto es solo definir el app y agregar la página
app = rx.App()
app.add_page(login_page, route="/")  # Definimos la ruta de la página
