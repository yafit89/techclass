from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_class():
    return 'Hello, class!'

if __name__ == '__main__':
    app.run(debug=True)

    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 5000), debug=True)
