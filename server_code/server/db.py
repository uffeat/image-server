from anvil.tables import app_tables

def get_image(name):
    row = app_tables.images.get(name=name)
    image = row['file']

    print(image.content_type)


    return image
    

if __name__ == "__main__":
    from anvil.server import connect
    server_key = 'server_EJJ3X6EFJZWY5DQ6ML4UXFR7-YLALERW7EPQHRHXJ'
    client_key = 'client_YX4A2VNK2JA7ZWYNHOKHVYDV-YLALERW7EPQHRHXJ'

    connect("server_EJJ3X6EFJZWY5DQ6ML4UXFR7-YLALERW7EPQHRHXJ")

    print(get_image('test'))

    

    