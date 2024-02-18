# chatapp.py
import reflex as rx

from ZeroToHero import style
from ZeroToHero.state import State

color = "rgb(107,99,246)"

def qa(desc: str, code: str) -> rx.Component:
    return rx.hstack(
        # rx.box(
        #     rx.text(desc, text_align="left"),
        #     style=style.question_style,
        # ),
        rx.box(
            rx.html(code),
            style={"width": "100vw", "height": "100vh", "overflow": "auto"}
        ),
        # rx.box(
        #     rx.text(answer, text_align="left"),
        #     style=style.answer_style,
        # ),
        margin_y="1em",
    )



def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


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
    return rx.container(
        rx.center(
            rx.vstack(
                rx.heading("Upload your sketch"),
                rx.upload(
                    rx.vstack(
                        rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                        rx.text("Drag and drop files here or click to select files."),
                    ),
                    border=f"1px dotted {color}",
                    padding="5em",
                ),
                rx.button(
                    "Upload",
                    on_click=lambda: State.handle_upload(rx.upload_files()),
                    style={"background-color": color, "color": "white"}  # Change button color to green
                ),
                rx.center(rx.vstack(rx.foreach(rx.selected_files, rx.text))),
            )
        ),
        rx.spacer(height="2em"),  # Add space between upload box and uploaded image
        rx.center(rx.foreach(State.img, lambda img: rx.image(src=img, width="40%", height="40%"))),  # Align selected image to the right
        rx.spacer(height="1em"),
    )



def generate_wireframe() -> rx.Component:
    return rx.center(rx.hstack(
            rx.button(
                "Digitize your drawing",
                on_click=State.generateWireFrame(),
                style={"background-color": "black", "color": "white"}
            ),
        )
    )

def navigation_bar() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.link("Home", href="/", style=style.nav_link_style),
            rx.spacer(),  # Add spacer to push links to the right
            rx.link("Discussion", href="/discussion", style=style.nav_link_style),
            rx.link("Contact", href="/contact", style=style.nav_link_style),
            style={"width": "100%", "justify_content": "space-between"},
        ),
        style=style.nav_bar_style,
    )

def company_name() -> rx.Component:
    return rx.box(
        "Zero to Hero",
        style={
            "font_size": "2em",  # Adjust font size as needed
            "font_weight": "bold",  # Make the font bold
            "margin_bottom": "1em",  # Add space below the company name
            "text_align": "center",  # Center the company name
        },
    )

def contact_page() -> rx.Component:
    return rx.container(
        rx.heading("Contact Us"),
        rx.paragraph("For inquiries, please email us at info@example.com or call us at +123456789."),
        # You can include more contact information or a contact form here
    )


def index() -> rx.Component:
    return rx.container(
        rx.spacer(height="1em"),
        company_name(),
        navigation_bar(),
        rx.spacer(height="2em"),  # Add space between company name and navigation bar
        rx.center(upload_image()),
        rx.spacer(height="1em"),
        generate_wireframe(),
        chat(),
        rx.spacer(height="5em")
        # action_bar()
    )


app = rx.App()
app.add_page(index)


# Define routes for different pages
# @app.route("/contact")
# def contact_route() -> rx.Component:
#     # This route corresponds to the contact page
#     return contact_page()

# # Add routes to your application
# app.add_route("/contact", contact_route)