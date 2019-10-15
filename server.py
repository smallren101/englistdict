import math

import pymongo
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
db_english = pymongo.MongoClient("127.0.0.1", 27017)["english"]
col = db_english['danci']
PER_PAGE = 13


def insert_mongo(query):
    args = query.get('args')
    res = col.find_one({'args': args})
    try:
        res.get('_id')
    except Exception as e:
        col.insert(query)


@app.route('/api1/danci', methods=['GET', ])
def index():
    if request.method == 'GET':
        args = request.args['ci'].strip()
        if args:
            result = [col.find_one({'args': args})]

            if result[0] is not None:
                for res in result:
                    res["_id"] = str(res["_id"])

                return jsonify({"code": 0, "data": result, "page_total": 1})
            else:
                url = "http://dict.youdao.com/w/" + args + "/"
                soup = BeautifulSoup(requests.get(url).text, features="html.parser")
                trans = soup.find('div', {'id': 'phrsListTab'}).find_all("ul", limit=1)[0]
                if trans:
                    trans = trans.text.strip('\n').split('\n')

                pronounce = soup.find('div', {'id': 'phrsListTab'}).find("div", {"class": "baav"})
                if pronounce:
                    pronounce = pronounce.text.strip('\n')

                additional = soup.find('div', {'id': 'phrsListTab'}).find("p", {"class": "additional"})
                if additional:
                    additional = additional.text
                query = {"args": args, "trans": trans, "pronounce": pronounce, "additional": additional}
                insert_mongo(query)

                result = [col.find_one({'args': args})]
                for res in result:
                   res["_id"] = str(res["_id"])
                return jsonify({"code": 0, "data": result, "page_total": 1})
        else:
            page = int(request.args.get('page') or 1)
            start = (page - 1) * PER_PAGE
            result = list(col.find().sort('_id', 1).skip(start).limit(PER_PAGE))
            for res in result:
                res["_id"] = str(res["_id"])

            return jsonify({"code": 0, "data": result, "page_total": math.ceil(col.count()/13)})
    else:
        return jsonify({"code": 200})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
