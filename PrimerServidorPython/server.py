from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader


HTML = """
<!DOCTYPE html>
<html>
<head>
	<title>Servidor Python</title>
</head>
<body>
    <h1>Hola desde el servidor en Python</h1>
</body>
</html>
"""


def application(env, start_response):

    #headers = [ ('Content-Type', 'text/plain'), ]
    headers = [ ('Content-Type', 'text/html'), ]
    start_response('200 OK', headers)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    html = template.render(
        {
            'title': 'Servidor Python',
            'text': 'Este es un servidor de Python'
        }
    )
    
    #return ['Hello world from Python server'.encode('utf-8')]
    return [bytes(html, 'utf-8')]


server = make_server('localhost', 8000, application)
server.serve_forever()
