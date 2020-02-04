from flask import Flask
import docker
app = Flask(__name__)

d_client = docker.from_env()

@app.route("/")
def hello_world():
    return 'Hello, world'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
