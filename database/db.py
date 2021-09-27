import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from __init__ import app
from celery_ import make_celery
from ml.main import extract_data
import json
import uuid

clust=MongoClient("mongodb://localhost:27017/")
db=clust["resume_ner"]
collection=db["result"]

celery = make_celery(app) 

@celery.task(name='celery_task.fileupload')
def fileupload(file_names):
    all_files=[]
    for file in file_names:
        record_uuid = uuid.uuid4()
        path = 'uploads/' + file
        ml_output=json.dumps(extract_data(path))
        all_files.append({'path':file,'record_uuid':str(record_uuid),'content':ml_output})
    x=collection.insert_many(all_files)
    return str(x.inserted_ids)
    # return "Output Recorded In Database"

# def insert(all_file):
#     x=collection.insert_many(all_file)
#     return x.inserted_ids


# def retrieve(collection):
#     all_details=[]
#     for info in collection.find():
#         all_details.append(info)
#     return all_details
