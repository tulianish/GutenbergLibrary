from flask import Flask, render_template, request
import pymongo, json

app = Flask(__name__)

# MongoDB connector
mongo_client = pymongo.MongoClient("mongodb://35.171.85.141:27017/")
mongo_db_name = mongo_client["gutenberg"]
collection = mongo_db_name["books"]
collection_catalogue = mongo_db_name["catalogue"]


@app.route('/catalogue/<keyword>', methods=['GET'])
def CatalogHandler(keyword):
    result = collection.find({"$or": [
        {"book_name": { "$regex": keyword}},
        {"author": { "$regex": keyword}}
    ]}, {"_id": 0, " book_id": 0})

    if result.count() != 0:
        returnableResult = []
        for each in result:
            returnableResult.append({"book_name": each.get("book_name"), "author": each.get("author")})

        catalogue_result = collection_catalogue.find({"keyword" : keyword},{"_id":0})
        if catalogue_result.count()==0:
            document = { "keyword" : keyword, "result" : returnableResult}
            collection_catalogue.insert_one(document)
        return json.dumps(returnableResult)

    else:
        return "0"
