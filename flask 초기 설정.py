# app.py
from flask import Flask # 1

app = Flask(__name__) # 2

@app.route("/") # 3
def hello_world():
	return "hello world"

if __name__ == '__main__': # 4
    app.run()