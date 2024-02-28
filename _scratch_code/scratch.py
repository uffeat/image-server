html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="#" type="image/x-icon" />
    <title>Index</title>
    <link rel="stylesheet" href="/_/theme/styles.css">
    
    <script type="module" src="/_/theme/main.js"></script>
  </head>
  <body>
    <h1>{headline}</h1>
  </body>
</html>
"""

html = html.format(headline="Hello")

print(html)