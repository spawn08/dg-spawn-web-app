import json

data = {}


def load_json():
    global data
    with open("/opt/spawn-python-app/FlaskWebApp/data/web_data.json", 'rb') as file:
        json_data = file.read()
        print(json_data)
    data = json.loads(json_data)
    pass;


def get_data():
    return data;


#load_json()
#print(data)
#web_daat = data.get('nav_bar')
#for web_daat in data:
#    print(web_daat)
