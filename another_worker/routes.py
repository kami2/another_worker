from another_worker import app
from quart import render_template


@app.route("/")
async def hello():
    return await render_template("index.html", welcome_text="Hello World, I am Quart app")