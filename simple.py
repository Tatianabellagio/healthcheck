from flask import Flask, render_template
import utility as ut
server = Flask(__name__)

@server.route('/')
def hello():
    return 'Hello, World!'

@server.route("/healthcheck")
def healthcheck():
    return render_template("healthcheck.html")

@server.route("/healthcheck_monitoreo")
def healthcheck_monitoreo():
    return {
        'cantidad_testeos': ut.load_data_json()
    }

if __name__ == '__main__':
    server.run(debug= True, host='0.0.0.0',port=8080)