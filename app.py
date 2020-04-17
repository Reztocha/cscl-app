from flask import (Flask, render_template,abort,redirect,url_for,request)
app = Flask(__name__)
from model import db, save_db

@app.route('/')
def index():
    return render_template(
        'splash.html'
    )
    
@app.route("/cscl")
def lib_view():
    return render_template(
        "index.html",
        books = db
    )

@app.route("/cscl/<int:indx>", methods=["GET", "POST"])
def lib_page_view(indx):
    try:
        book = db[indx]
        if request.method == 'POST':
            if request.form['available'] == 'Checkout':
                if book["available"] > 0:
                    book["available"] = int(book["available"]) - 1
            elif request.form['available'] == 'Return':
                if book["copies"] > book["available"]:
                    book["available"] = int(book["available"]) + 1
            else:
                pass # ?
            save_db()
        return render_template("library.html", book=book, indx=indx, max_indx=len(db)-1)
    except IndexError:
        abort(404)
        
@app.route('/admin')
def admin():
    return render_template(
        "admin.html",
        books = db
    )

@app.route("/admin/<int:indx>")
def admin_lib_view(indx):
    try:
        book = db[indx]
        return render_template("admin_library.html", book=book, indx=indx, max_indx=len(db)-1)
    except IndexError:
        abort(404)

@app.route('/admin/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == 'POST':
        books = ["isbn", "title", "author", "publication_year", "publisher", "image_url_s", "image_url_m","image_url_l", "copies", "available"] 
        book = {}
        for attr in books:
            if request.form[attr] == '':
                book[attr] = ""
                if attr == "image_url_s":
                    book[attr] = "../static/thumbz-s.jpg"
                if attr == "image_url_m":
                    book[attr] = "../static/thumbz-m.jpg"
                if attr == "image_url_l":
                    book[attr] = "../static/thumbz-l.jpg"
            else:
                if(attr == "copies" or attr == "available"):
                    book[attr] = int(request.form[attr])
                else:
                    book[attr] = request.form[attr]
        db.append(book)
        save_db()
        return redirect(url_for('admin_lib_view',indx= len(db)-1))
    else:
        return render_template("add_book.html")
    
@app.route("/admin/remove_book/<int:indx>", methods=['GET','POST'])
def remove_book(indx):
    if request.method == 'POST':
        del db[indx]
        save_db()
        return redirect(url_for('admin'))
    else:
        return render_template("remove_book.html", book=db[indx])

@app.route("/admin/edit_book/<int:indx>", methods=['GET','POST'])
def edit_book(indx):
    try:
        book = db[indx]
        if request.method == 'POST':
            books = ["isbn", "title", "author", "publication_year", "publisher", "image_url_s", "image_url_m","image_url_l", "copies", "available"] 
            book = {}
            for attr in books:
                if request.form[attr] == '':
                    book[attr] = ""
                    if attr == "image_url_s":
                        book[attr] = "../static/thumbz-s.jpg"
                    if attr == "image_url_m":
                        book[attr] = "../static/thumbz-m.jpg"
                    if attr == "image_url_l":
                        book[attr] = "../static/thumbz-l.jpg"
                else:
                    if(attr == "copies" or attr == "available"):
                        book[attr] = int(request.form[attr])
                    else:
                        book[attr] = request.form[attr]
            save_db()
            return redirect(url_for('admin'))
        else:
            return render_template("edit_book.html", book=book, indx=indx)
    except IndexError:
        abort(404)
        
if __name__ == '__main__':
    app.run(debug=True)