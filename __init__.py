from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <iframe src="https://www.youtube.com/embed/YQHsXMglC9A" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
