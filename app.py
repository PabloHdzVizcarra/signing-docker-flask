import os
import signal

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>HELLO THIS CONTAINER IS SIGNED</h1>'


@app.route('/hello')
def hello_world_two():
    return "Hello World Version 1.9"


@app.route('/down')
def down_application():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})


@app.route('/liveness')
def liveness_test():
    return "OK"


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
