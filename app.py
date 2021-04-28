from flask import Flask, render_template, request, redirect
import json
from configurationsGetter import get_configuration


app = Flask(__name__)


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
    return render_template("configuration.html")


if __name__ == '__main__':
    app.run()
