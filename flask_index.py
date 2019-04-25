from flask import Flask, render_template, request

from utils import file_loading

app = Flask(__name__)

file_loading.load_json()


@app.route('/')
def hello_world():
    web_data = file_loading.get_data()
    return render_template('index.html', web_data=web_data)


@app.route("/contact")
def cantact():
    return render_template('contact.html')

@app.route("/privacy_policy")
def privacy_policy():
    return render_template('privacy_policy.html')


@app.route('/reload_data')
def reload_data():
    file_loading.load_json()
    return "Success"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4789)
