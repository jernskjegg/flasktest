from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Works</h1>"

@app.route("/home")
def home():
    return "<h1>Home</h1>"

@app.route("/admin")
def admin():
    return "<h1>Soon</h1>"

@app.route("/json")
def json():
    return jsonify({"mykey": "JSON Value!", "mylist" : [1,2,3,4,5]})

@app.route("/dynamic", defaults={"user_input" : "Default."})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h1>The string the user entered was: { user_input } </h1>"

@app.route("/query")
def query():
    user_input = request.args.get("user_input")
    return f"<h1>The query string contains: { user_input } </h1>"

@app.route("/form")
def form_get():
    return """
    <form method = "POST">
        <input type = "text" name="user_input">
        <input type = "submit">
    </form>
    """
@app.route("/form", methods=["POST"])
def form_post():
    user_potato = request.form["user_input"]
    return f"<h1> The user input was: { user_potato }</h1>"

@app.route("/accept_json", methods= ["POST"])
def accept_json():
    return jsonify({"resuts" : "Done"})