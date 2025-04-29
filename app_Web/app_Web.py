# PAGINA DESDE CERO

import reflex as rx

class State(rx.State):
    pass

def index():
    return rx.text("Hola Mundo")

app = rx.App()
app.add_page(index)
