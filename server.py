from sanic import Sanic
from sanic import Blueprint
from sanic.response import html
from jinja2 import Environment, FileSystemLoader

class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        template_env = Environment(loader=FileSystemLoader('./templates'))
        bp = Blueprint("main")
        self.sanic = Sanic()

        @bp.route("/")
        async def home(request):
            template = template_env.get_template("home.html")
            return html(template.render())
            
        self.sanic.blueprint(bp);

    def run(self):
        self.sanic.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web_server = WebServer("0.0.0.0", 8000)
    web_server.run()
