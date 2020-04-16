from flask import Flask, render_template,abort
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
    return render_template(
        "index.html",
        books = db
    )    

@app.route("/cscl/<int:indx>")
def lib_page_view(indx):
    try:
        book = db[indx]
        return render_template("library.html", book=book, indx=indx, max_indx= len(db)-1)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
