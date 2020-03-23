from flask import Flask, render_template, request,redirect
import pymongo

app = Flask(__name__)

# MongoDB connector
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db_name = mongo_client["gutenberg"]
collection = mongo_db_name["notes"]


@app.route('/notes/all', methods=['GET'])
def NoteAllHandler():
    result = collection.find({})
    return render_template("home.html",result=result)


@app.route('/', methods=['GET'])
def NoteHomeHandler():
    return redirect("http://127.0.0.1:5003/notes/all")

@app.route('/notes/add', methods=['POST'])
def NoteAddHandler():
    note = request.form['notes']
    keyword = request.form['keyword']

    notesearch = list(collection.find({"keyword": keyword}))

    if notesearch:
        collection.update({"keyword": keyword}, {"$push" : {"notes": {"note": note}}})
        return redirect("/notes/all")

    else:
        document = {'keyword': keyword, 'notes': [ {"note" : note }]}
        collection.insert_one(document)
        return redirect("/notes/all")