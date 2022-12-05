import pandas as pd
import pymongo

dataframe=pd.read_csv("https://raw.githubusercontent.com/vigneshk/Admission-Dataset/master/Admission.csv")

#connect with the mongodb
dbConn = pymongo.MongoClient("mongodb://localhost:27017/")

dbname='ineuron'

db=dbConn[dbname]

collection_name='Addmision_details'

collection=db[collection_name]

records = dataframe.to_dict('records')

col = collection.insert_many(records)

col.inserted_ids

result=collection.find()
for i in result:
    print(i)
