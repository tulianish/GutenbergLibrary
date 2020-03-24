from flask import Flask
import datetime,pymongo,requests


app = Flask(__name__)


# MongoDB connector
mongo_client = pymongo.MongoClient("mongodb://35.171.85.141:27017/")
mongo_db_name = mongo_client["gutenberg"]
collection = mongo_db_name["logs"]

@app.route('/logs/<keyword>', methods=['GET'])
def LogHandler(keyword):
    logsearch = list(collection.find({"keyword": keyword}))

    if logsearch:
        frequency = int(logsearch[0].get("frequency"))
        updatedTime = datetime.datetime.now()
        collection.update_one({"keyword": keyword}, {"$set": {"frequency": frequency+1, "timestamp": updatedTime }})
        return "1"
    else:
        document = {'keyword': keyword, 'frequency': 1, 'timestamp': datetime.datetime.now()}
        collection.insert_one(document)
        return "1"
