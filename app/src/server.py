from flask import Flask

server = Flask(__name__)
@server.route("/")

def hello():
    return "<p style='color: red; font-size: 40;'>Hello World!</p>"
if __name__ == "__main__":
    server.run(host='0.0.0.0')
