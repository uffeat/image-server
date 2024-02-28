from ._anvil_designer import Form1Template
from anvil import *
from anvil.server import call as call_server
from anvil.js.window import fetch

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        image = call_server('get_image', 'test')
        self.image_1.source = image

        fetch('https://image-server.anvil.app/_/api/my-url')
