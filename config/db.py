from pymongo import MongoClient
import certifi
ca = certifi.where()


MongoUri = ""
conn = MongoClient(MongoUri, tlsCAFile=ca)