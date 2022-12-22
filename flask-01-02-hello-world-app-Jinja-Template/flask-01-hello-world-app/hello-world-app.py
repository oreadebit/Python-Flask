from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!!!"

@app.route("/second")
def second():
    name = "Ore"
    return f"my name is {name}"

@app.route("/third/subthird")
def third():
    name = "Ore"
    return f"Returned from subthird"

@app.route("/fourth/<string:name>")
def fourth(name):
    name = "Ore"
    return f"Hello its {name} again!"


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 3001, debug = False)