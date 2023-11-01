from flask import Flask
import sys
sys.path.append('src')

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

if __name__=="__main__":
    app.run()