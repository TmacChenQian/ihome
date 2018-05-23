from flask import Flask


app = Flask(__name__)

@app.route("/index")
def index():
    return "ihome v1_0"

app.run()