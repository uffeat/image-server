import anvil.server
from .db import get_image as _get_image


@anvil.server.callable
def get_image(name):
    """."""
    return _get_image(name)

