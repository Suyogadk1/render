from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Cloud deployment successful"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it can be accessed from outside the container.
    app.run(host="0.0.0.0", port=8080)
