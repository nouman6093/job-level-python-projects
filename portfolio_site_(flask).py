#download required files from here: https://drive.google.com/drive/folders/1ocxH8A7YpWoYDSPy1r4Mw-g1gW8RC5sr?usp=drive_link
#this code will create a basic portfolio webpage
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
