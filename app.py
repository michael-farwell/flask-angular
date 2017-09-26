from flask import Flask, jsonify

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/get_title', methods=['GET'])
def get_title():
    print('Getting title...')
    title = 'AngularJS/Flask Web App'
    return jsonify(title)


@app.route('/get_user/<user>')
def get_user(user):
    print('Getting user...')
    user = user
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
