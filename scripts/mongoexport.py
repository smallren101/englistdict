import json

import pymongo


mongo = pymongo.MongoClient('127.0.0.1', 27017)
db = mongo['english']
col = db['danci']

# with col.find(projection={'_id': False}, no_cursor_timeout=True) as results:
#     with open('danci.json', 'w') as f:
#         for res in results:
#             f.write(json.dumps(res))
#             f.write('\n')


with open('danci.json', 'r') as f:
    for res in f.readlines():
        col.insert_one(json.loads(res))
