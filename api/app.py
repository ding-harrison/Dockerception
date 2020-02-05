from flask import Flask
import docker
app = Flask(__name__)

d_client = docker.from_env()

@app.route("/")
def start_docker():
    volumes = { "dockerception":{"bind": "/data", "mode": "rw"} }
    return d_client.containers.run("reader_writer", volumes=volumes, tty=True)

@app.route("/reader")
def reader():
    volumes = {"dockerception":{"bind": "/data", "mode": "rw"} }
    return d_client.containers.run("reader", volumes=volumes, tty=True)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
