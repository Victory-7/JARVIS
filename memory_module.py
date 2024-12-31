import json

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data):
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
