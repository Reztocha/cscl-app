from flask import (Flask, render_template,abort,redirect,url_for,request)
app = Flask(__name__)
from model import db, save_db
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
        
@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == 'POST':
        book = {
            "title": request.form['title'],
            "author": request.form['author'],
            "isbn": request.form['isbn'],
            "publication_year": request.form['publication_year'], 
            "publisher": request.form['publisher'], 
            "image_url_s": request.form['image_url_s'], 
            "image_url_m": request.form['image_url_m'], 
            "image_url_l": request.form['image_url_l'], 
            "copies": request.form['copies'], 
            "available": request.form['available']
        }
        db.append(book)
        save_db()
        return redirect(url_for('lib_page_view',indx= len(db)-1))
    else:
        return render_template("add_book.html")
    

if __name__ == '__main__':
    app.run(debug=True)
