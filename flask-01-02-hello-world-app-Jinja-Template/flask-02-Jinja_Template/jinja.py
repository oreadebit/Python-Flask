from flask import Flask render_template

app = Flash(__name__)


@app.route("/")
def home():
    return render_template("index.html", name ="Ore", lastname ="Ade")

@app.route("/body/<int:x>/<int:y>")
def body(x, y):
    return render_template("index.html",x=x, y=y, sum = (x, y))


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 3001, debug = False)