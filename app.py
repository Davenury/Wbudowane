from flask import Flask, render_template, request, redirect
import json
from configurationsGetter import get_configuration
import subprocess
from network.connect_to_wifi import update_wifi

app = Flask(__name__)


def get_rid_of_signs(wifis):
    new_wifis = []
    for wifi in wifis:
        new_wifis.append(wifi.replace('"', ""))
    return new_wifis


def read_wifi():
    with open('wifi.txt') as f:
        wifis = f.readlines()
    wifis = get_rid_of_signs(wifis)
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
        config = get_configuration()
        if request.form.get('email'):
            config["email"] = request.form.get("email")
        if request.form.get("wifi") and request.form.get("password"):
            config['ssid'] = request.form.get("wifi")
            config['password'] = request.form.get("password")
        with open('./configuration.json', "w") as f:
            json.dump(config, f)
            update_wifi()
        return redirect('/')
    process = subprocess.Popen(['network/find_wifi.sh'])
    process.wait()
    wifis = read_wifi()
    return render_template("configuration.html", wifis=wifis, len=len(wifis))


if __name__ == '__main__':
    app.run()
