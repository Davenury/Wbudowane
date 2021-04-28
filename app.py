from flask import Flask, render_template, request, redirect
import json
from configurationsGetter import get_configuration
import subprocess

app = Flask(__name__)


def read_wifi():
    wifis = []
    with open('network/wifi.txt') as f:
        for line in f:
            wifis += line
    return wifis


@app.route('/')
def home():
    config = get_configuration()
    email = config["email"]
    net = config["ssid"]
    password = config["password"]
    return render_template("home.html", net=net, email=email)


@app.route('/configuration', methods=['POST', 'GET'])
def configuration():
    if request.method == "POST":
        if request.form.get('email') and request.form.get("wifi") and request.form.get("password"):
            configurations = {
                'email': request.form.get("email"),
                'ssid': request.form.get("wifi"),
                'password': request.form.get("password")
            }
            with open('./configuration.json', "w") as f:
                json.dump(configurations, f)
            update_wifi()
        return redirect('/')
    process = subprocess.Popen(['network/find_wifi.sh'])
    process.wait()
    wifis = read_wifi()
    return render_template("configuration.html", wifis=wifis, len=len(wifis))


if __name__ == '__main__':
    app.run()
