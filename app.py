from flask import Flask, render_template
app = Flask(__name__)
from model import db
@app.route('/')
def index():
    return render_template(
        'index.html', 
        message = "Next time on Yu-Gi-Oh!..."
    )
    
@app.route("/cscl")
def lib_view():
    book = db[0]
    return render_template("library.html", book=book)

if __name__ == '__main__':
    app.run(debug=True)
