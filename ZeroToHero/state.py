# state.py
import reflex as rx
import asyncio
from openai import OpenAI
import os

import json
import re

import requests
import base64

os.environ["OPENAI_API_KEY"] = "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"

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

def encode_image(img):
    return base64.b64encode(img).decode('utf-8')

def separate_code_and_text(input_string):
    """
    Separates code chunks and text from a given string.
    
    Args:
    - input_string (str): The string to be processed, containing code chunks marked with triple backticks.
    
    Returns:
    - Tuple[List[str], List[str]]: A tuple containing two lists, the first with code chunks and the second with text segments.
    """
    # Pattern to find code chunks
    pattern = r"```(.*?)```"
    
    # Extract code chunks
    code_chunks = re.findall(pattern, input_string, re.DOTALL)
    
    # Split the string by code chunks to get text segments, including text directly adjacent to code chunks
    text_parts = re.split(pattern, input_string, flags=re.DOTALL)
    
    # Extract text segments, which are in every other place excluding the code chunks
    text_segments = text_parts[0::2]
    
    # Optionally, clean up text segments to remove leading/trailing whitespace or empty strings
    text_segments = [text.strip() for text in text_segments if text.strip()]
    
    return code_chunks, text_segments


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

    def clear_images(self):
        """Clear the list of images."""
        self.img = []

    def answer(self):
        # Our chatbot has some brains now!
        client = OpenAI()
        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield

    def generateWireFrame(self):
        # Our chatbot has some brains now!

        image_path = rx.get_asset_path(self.img[0])

        # Read the image data
        with open(image_path, "rb") as f:
            image_data = f.read()

    # Encode the image
        encoded_image = encode_image(image_data)
        print("hello nirvan I'm thinking right now ")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OpenAI.api_key}"
            }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "Could you please transform this hand-drawn wireframe into a working HTML/CSS/JS mockup? I'd like the code to reflect the layout, details, and features as closely as possible to what's depicted, with placeholders for images and text. The mockup should include features just as shown in the drawing. For example, the shapes, size, and placements of the placeholders should roughly be the same as the boxes drawn. Additionally, I'd like interactive elements. Please put all of the code into 1 html file."
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 3000
            }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        response_json = response.json()

        ret = response_json['choices'][0]['message']['content']

        code, text = separate_code_and_text(ret)

        self.chat_history.append((text, code))


