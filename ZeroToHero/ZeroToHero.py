# chatapp.py
import reflex as rx

from ZeroToHero import style
from ZeroToHero.state import State

color = "rgb(107,99,246)"

def qa(desc: str, code: str) -> rx.Component:
    return rx.hstack(
        rx.text_area(
        value=code,
        # on_change=State.set_code(),
        style=style.question_style,
        ),
        # rx.box(
        #     rx.text(code, text_align="left"),
        #     # style=style.answer_style
        # ),
        rx.box(
            rx.html(code)
        ),
        # rx.box(
        #     rx.text(answer, text_align="left"),
        #     style=style.answer_style,
        # ),
        margin_y="1em",
    )


# def chat() -> rx.Component:
#     return rx.box(
#         rx.foreach(
#             State.chat_history,
#             lambda messages: qa(messages[0], messages[1]),
#         )
#     )


# def action_bar() -> rx.Component:
#     return rx.hstack(
#         rx.chakra.input(
#             value=State.question,
#             placeholder="Ask a question",
#             on_change=State.set_question,
#             style=style.input_style,
#         ),
#         rx.button(
#             "Ask",
#             on_click=State.answer,
#             style=style.button_style,
#         ),
#     )

def upload_image() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Upload Image Here"),
            rx.upload(
                rx.vstack(
                    rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                    rx.text("Drag and drop files here or click to select files"),
                ),
                border=f"1px dotted {color}",
                padding="5em",
            ),
            rx.button(
                "Upload",
                on_click=lambda: State.handle_upload(rx.upload_files()),
            ),
            rx.center(rx.vstack(rx.foreach(rx.selected_files, rx.text))),
            rx.center(rx.foreach(State.img, lambda img: rx.image(src=img, width="10%", height="10%")),)
        )
    )

def generate_wireframe() -> rx.Component:
    return rx.box(rx.hstack(
            rx.button(
                "Generate Wireframe!",
                on_click=State.generateWireFrame(),
                style=style.button_style,
            ),
        )
    )

def index() -> rx.Component:
    return rx.container(
        rx.center(upload_image()),
        generate_wireframe(),
        qa(State.code,State.code)
        # chat()
        # action_bar(),
    )


app = rx.App()
app.add_page(index)

