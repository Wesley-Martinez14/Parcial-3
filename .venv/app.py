# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True)
