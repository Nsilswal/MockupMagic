# chatapp.py
import reflex as rx

from ZeroToHero import style
from ZeroToHero.state import State

color = "rgb(107,99,246)"

class TextAreaControlled(rx.State):
    text:str

    def getText(self):
        print(self.text)
        return self.text



def qa(desc: str, code: str) -> rx.Component:
    return rx.hstack(
        rx.text_area(
            value = State.code,
            on_change = State.update_code(TextAreaControlled.text),
            on_focus = TextAreaControlled.set_text,
            style={"width": "30vw", "height": "100vh"}
        ),
        rx.box(
            rx.html(State.code),
            style={"width": "70vw", "height": "100vh"}
        ),
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
            rx.link("Discussion", href="/discussion_forum", style=style.nav_link_style),
            rx.link("Contact", href="/contact_page", style=style.nav_link_style),
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

@rx.page(route="/contact_page")
def contact_page() -> rx.Component:
    return rx.container(
        rx.spacer(height="1em"),
        company_name(),  # Include company name (optional)
        navigation_bar(),  # Include navigation bar
        rx.spacer(height="2em"),
        rx.center(
            rx.vstack(
                # Our email section
                rx.heading("Our Email"),
                rx.text("You can reach us via email at info@example.com."),
                rx.spacer(height="2em"),

                # Directly send us a message section
                rx.heading("Send Us a Message"),
                rx.text("Use the form below to send us a message."),
                rx.container(
                    rx.chakra.input(placeholder="Your Name", style={"margin-bottom": "1em"}),
                    rx.chakra.input(placeholder="Your Email", style={"margin-bottom": "1em"}),
                    rx.chakra.text_area(placeholder="Your Message", style={"margin-bottom": "1em"}),
                    rx.button("Send Message", style={"background-color": color, "color": "white"})
                )
            )
        ),
        style={"margin-left": "5%", "width": "90%"}
    )

@rx.page(route="/discussion_forum")
def discussion_forum() -> rx.Component:
    return rx.container(
        rx.spacer(height="1em"),
        company_name(),  # Include company name (optional)
        navigation_bar(),  # Include navigation bar
        rx.spacer(height="2em"),

        # Display discussion topics
        rx.heading("Discussion Topics"),
        rx.container(
            # Each topic can be a link to view the details
            rx.link("Topic 1", href="/discussion_forum/topic1"),
            rx.link("Topic 2", href="/discussion_forum/topic2"),
            # Add more topics as needed
        ),
        rx.spacer(height="2em"),

        # User comments section
        rx.heading("User Comments"),
        rx.container(
            # Display user comments
            rx.text("User 1: This is a comment."),
            rx.text("User 2: Another comment here."),
            # Add more comments as needed
        ),
        rx.spacer(height="2em"),

        # Form for posting new comments
        rx.heading("Post a New Comment"),
        rx.container(
            rx.chakra.input(placeholder="Your Name", style={"margin-bottom": "1em"}),
            rx.chakra.text_area(placeholder="Your Comment", style={"margin-bottom": "1em"}),
            rx.button("Post Comment", style={"background-color": color, "color": "white"})
        )
    )

@rx.page()
def index() -> rx.Component:
    return rx.box(
        rx.spacer(height="1em"),
        company_name(),
        navigation_bar(),
        rx.spacer(height="2em"),  # Add space between company name and navigation bar
        rx.center(upload_image()),
        rx.spacer(height="1em"),
        generate_wireframe(),
        qa(State.code,State.code),
        # chat(),
        rx.spacer(height="5em")
        # action_bar()
    )


app = rx.App()
# app.add_page(index())
# app.add_page(app())


# Define routes for different pages
# @app.route("/contact")
# def contact_route() -> rx.Component:
#     # This route corresponds to the contact page
#     return contact_page()

# # Add routes to your application
# app.add_route("/contact", contact_route)