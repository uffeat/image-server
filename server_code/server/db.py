import anvil.server
from anvil.tables import app_tables

def get_image(name):
    row = app_tables.images.get(name=name)
    image = row['file']

    print(image.content_type)


    return image
    

if __name__ == "__main__":
    server_key = 'server_EJJ3X6EFJZWY5DQ6ML4UXFR7-YLALERW7EPQHRHXJ'
    client_key = ''