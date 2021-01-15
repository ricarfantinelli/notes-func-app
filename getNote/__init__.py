import logging
import os
from bson.json_util import dumps
import pymongo
import azure.functions as func
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ['MyDBConnectionString']
        client = pymongo.MongoClient(url)
        database = client['notes-funcapp-cosmosdb']
        collection = database['samples']

        idnote = req.params.get('id')
        result = collection.find({"_id" : ObjectId(idnote)})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Bad request. url: {url} and database {database} and collection {collection} and result {result} /n Exception: {e}", status_code=200)