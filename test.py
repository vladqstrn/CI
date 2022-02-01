from asyncio import constants
from string import ascii_lowercase
from time import sleep
import pymongo as pm 
import string
import random
from datetime import datetime
import sys
import logging as log
import os

log.basicConfig(stream=sys.stdout, level=log.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
MONGO_CONNECTION_URL = os.environ.get('MONGO_CONNECTION_URL')
log.info(f"URL {MONGO_CONNECTION_URL}")
db_client = pm.MongoClient(MONGO_CONNECTION_URL)
current_db = db_client["mongo_test"]
collection = current_db["workers"]
letters = string.ascii_lowercase
teh_stack = ['python', 'js', 'java', 'c++', 'r', 'go', 'php']

while True:
    
    name = str.capitalize(''.join(random.choice(letters) for _ in range(0,5)))
    age = random.choice(range(20,70))
    stack = random.choice(teh_stack)
    sallary = random.choice(range(20000,200000))
    date = datetime.now()
    insert_res = collection.insert_one({"Name": name, "Age": age, "Stack": stack, "Sallary": sallary, "Date": date})
    cnt = collection.count_documents({})
    log.info(f"Counter value is {cnt}")
    log.info(f"insert ack is {insert_res.acknowledged}")
    sleep(15)
    