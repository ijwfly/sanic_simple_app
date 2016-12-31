from sanic import Sanic
from sanic import Blueprint
from sanic.response import html
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates'))
bp = Blueprint("main")

@bp.route("/")
async def test(request):
    template = env.get_template('home.html')
    return html(template.render())

app = Sanic()
app.blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)