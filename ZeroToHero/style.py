# style.py

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin
)
answer_style = message_style | dict(
    margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)
button_style = dict(
    background_color="#CEFFEE", box_shadow=shadow,
    color="black", padding="1em", margin_left="1em",
)

nav_link_style = dict(
    color="#333",  # Adjust color as needed
    text_decoration="none",
    margin_right="1em",
)

nav_bar_style = dict(
    background_color="#f0f0f0",  # Adjust background color as needed
    padding="1em",
    box_shadow="0px 2px 4px rgba(0, 0, 0, 0.1)",  # Adjust shadow as needed
    display="flex",
    align_items="center",
)

