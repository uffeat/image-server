import anvil.server
from anvil.tables import app_tables

def get_image(name):
    row = app_tables.images.get(name=name)
    image = row['file']
    return image
    
