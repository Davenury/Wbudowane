import json


def get_configurations():
    with open('./configuration.json') as f:
        data = json.load(f)
        net = data.get('net')
        email = data.get('email')
        password = data.get('password')
    return net, email, password
